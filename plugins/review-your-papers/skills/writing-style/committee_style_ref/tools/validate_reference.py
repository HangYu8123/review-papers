"""Check the committee writing style reference and write validation.md.

Run from the dissertation folder after build_reference.py:

    python committee_style_ref/tools/validate_reference.py
"""
import datetime
import hashlib
import json
import re
import runpy
import sys
from pathlib import Path
from urllib.parse import unquote

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as C

HERE = C.HERE
ROOT = C.ROOT
MAIN = 'committee-writing-style-reference.md'
FILES = [MAIN, 'source-evidence.md', 'writer-profiles.md', 'README.md']
ERRORS = []
NOTES = []


def check(condition, message):
    if not condition:
        ERRORS.append(message)
    return condition


def slug(s):
    # The anchor that GitHub and VS Code give a heading.
    return re.sub(r'[^\w\- ]', '', s.lower()).replace(' ', '-')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def anchors(path):
    text = path.read_text(encoding='utf-8')
    return {slug(h) for h in re.findall(r'^#{1,6} (.+)$', text, flags=re.M)}


def main():
    rows = []
    library = json.loads((HERE / 'library.json').read_text(encoding='utf-8'))
    patterns = library['patterns']
    authored = runpy.run_path(str(HERE / 'tools' / 'authored_entries.py'))['ENTRIES']

    # Patterns
    check(len(patterns) == len(authored), 'library.json and authored_entries.py have different numbers of patterns')
    main_text = (HERE / MAIN).read_text(encoding='utf-8')
    evidence_text = (HERE / 'source-evidence.md').read_text(encoding='utf-8')
    for p in patterns:
        check('\n### %s\n' % p['title'] in main_text, 'Pattern missing from the main reference: ' + p['title'])
        check('\n## %s\n' % p['title'] in evidence_text, 'Pattern missing from the evidence file: ' + p['title'])
    by_category = {}
    for p in patterns:
        by_category[p['category']] = by_category.get(p['category'], 0) + 1
    rows.append(('Patterns', '%d patterns across %d categories (%s)' % (
        len(patterns), len(by_category), ', '.join('%s %d' % kv for kv in by_category.items()))))
    relation = {}
    for p in patterns:
        relation[p['relation']] = relation.get(p['relation'], 0) + 1
    rows.append(("Relation to Hang's reference", '%d say the same, %d add to it, %d differ from Hang\'s preference' % (
        relation.get('same', 0), relation.get('adds', 0), relation.get('differs', 0))))

    # Quotations
    exact = letters = 0
    letters_only = []
    per_writer = {k: 0 for k in C.ORDER}
    for p in patterns:
        for k in p['seen_in']:
            check(any(x['writer'] == k for x in p['examples']), 'No quotation from %s in %s' % (k, p['title']))
        for x in p['examples']:
            per_writer[x['writer']] += 1
            result = C.find_quote(x['writer'], x['pdf_page'], x['text'])
            if result == 'exact':
                exact += 1
            elif result == 'letters':
                letters += 1
                letters_only.append((p['title'], x))
            else:
                ERRORS.append('Quotation not found on its page: %s, %s' % (p['title'], C.cite(x['writer'], x['pdf_page'])))
            check(x['text'] in main_text or x['text'].replace('[...]', '[…]') in evidence_text,
                  'Quotation missing from the evidence file: ' + x['text'][:50])
    total = exact + letters
    rows.append(('Quotations', '%d checked against the text of their pages (%s)' % (
        total, ', '.join('%s %d' % (C.SOURCES[k]['author'], per_writer[k]) for k in C.ORDER))))
    rows.append(('Quotation wording', '%d match in wording and punctuation, %d match in letters and digits only' % (exact, letters)))

    # Page numbers
    seen = missing = 0
    for key in C.ORDER:
        src = C.SOURCES[key]
        for n in range(src['body'][0], src['body'][1] + 1):
            numbers = [l.strip() for l in C.pages(key)[n] if l.strip().isdigit()]
            if str(n - src['offset']) in numbers[:2] + numbers[-2:]:
                seen += 1
            else:
                missing += 1
    check(missing == 0, 'Printed page number not found on %d pages' % missing)
    rows.append(('Printed page numbers', 'The printed number was found on %d of %d chapter pages' % (seen, seen + missing)))

    # Measures named in the text
    left = []
    for name in FILES:
        path = HERE / name
        if path.exists():
            left += re.findall(r'\{\w+\.\w+\}', path.read_text(encoding='utf-8'))
    check(not left, 'Measures not filled in: ' + ', '.join(sorted(set(left))))
    rows.append(('Measures in the text', 'All measures named in the guidance were filled in from the counts'))

    # Statements about the draft that depend on the counts
    m = library['measures']
    draft = m['draft']
    three = lambda name: [m[k][name] for k in C.ORDER]
    claims = [(name, min(three(name)) <= draft[name] <= max(three(name)))
              for name in ('sent_mean', 'long_share', 'suggest', 'may', 'might', 'could')]
    claims += [('colon', draft['colon'] <= sorted(three('colon'))[1]),
               ('semicolon', draft['semicolon'] <= sorted(three('semicolon'))[1]),
               ('we', draft['we'] < min(three('we')))]
    failed = [name for name, ok in claims if not ok]
    check(not failed, 'A statement about the draft no longer holds for: ' + ', '.join(failed))
    rows.append(("Statements about Hang's draft", '%d of %d comparisons with the three writers hold for the snapshot of %s' % (
        len(claims) - len(failed), len(claims), draft['date'])))
    main_pdf = ROOT / 'main.pdf'
    if main_pdf.exists() and sha(main_pdf) != draft['sha256']:
        NOTES.append('main.pdf has changed since the snapshot of the draft was taken. Run tools/profile_draft.py and the build to refresh the last column.')

    # Guidance punctuation
    text = ' '.join(p['guidance'] + ' ' + p['in_hangs_dissertation'] for p in patterns)
    colons, semicolons = text.count(':'), text.count(';')
    check(colons == 0 and semicolons == 0, 'Colons or semicolons in the guidance text: %d and %d' % (colons, semicolons))
    rows.append(('Colons and semicolons in the guidance text', '%d colons and %d semicolons in the guidance and the lines on Hang\'s dissertation' % (colons, semicolons)))

    # Links
    n_links = 0
    hang_links = 0
    for name in FILES:
        path = HERE / name
        if not check(path.exists(), 'Missing file: ' + name):
            continue
        for target in re.findall(r'\]\(([^)\s]+)\)', path.read_text(encoding='utf-8')):
            if re.match(r'https?://', target):
                continue
            n_links += 1
            file_part, _, fragment = target.partition('#')
            dest = (HERE / unquote(file_part)).resolve() if file_part else path
            if dest == HERE / 'validation.md':
                continue
            if not check(dest.exists(), 'Broken link in %s: %s' % (name, target)):
                continue
            if 'writing_style_ref' in file_part:
                hang_links += 1
            if fragment and dest.suffix == '.md':
                check(fragment in anchors(dest), 'Broken anchor in %s: %s' % (name, target))
            if fragment and dest.suffix == '.pdf':
                key = [k for k in C.ORDER if C.SOURCES[k]['pdf'].endswith(dest.name)]
                page = int(fragment.split('=')[1])
                check(key and page in C.pages(key[0]), 'Page out of range in %s: %s' % (name, target))
    rows.append(('Local links', '%d file, heading, and page links checked, including %d into Hang\'s reference' % (n_links, hang_links)))

    # Sources
    hashes = json.loads((HERE / 'sources' / 'pdf-hashes.json').read_text(encoding='utf-8'))
    same = 0
    for key in C.ORDER:
        pdf = ROOT / hashes[key]['file']
        check(len(C.pages(key)) == hashes[key]['pages'], 'Page count differs for ' + key)
        if pdf.exists():
            if check(sha(pdf) == hashes[key]['sha256'], 'PDF changed since its text was extracted: ' + hashes[key]['file']):
                same += 1
        else:
            NOTES.append('PDF not found, so its hash was not compared: ' + hashes[key]['file'])
    rows.append(('Source PDFs', '%d of %d PDF files match the hashes recorded when their text was extracted' % (same, len(C.ORDER))))

    length = len(main_text.split())
    rows.append(('Approximate main reference length', '{:,} whitespace-delimited words'.format(length)))
    rows.append(('Overall result', 'PASS' if not ERRORS else 'FAIL'))

    out = ['# Validation of the committee writing style reference', '',
           'Checked on %s.' % datetime.date.today().strftime('%B %d, %Y').replace(' 0', ' '), '',
           '| Check | Result |', '| --- | --- |']
    out += ['| %s | %s |' % row for row in rows]
    out += ['',
            'A quotation check establishes that the wording is in the source on the cited page. It does not establish that the pattern is typical of the writer, which rests on the reading described in the scope section of the main reference. The lines on Hang\'s dissertation were not checked by this tool, apart from the comparisons of counts listed above.', '']
    if letters_only:
        out += ['## Quotations that match in letters and digits only', '',
                'The extracted text of these pages differs from the quotation in a hyphen or a space, because a word was divided at the end of a line in the PDF or a figure sits inside the paragraph. The words of each quotation match the page in order.', '']
        for title, x in letters_only:
            out.append('- %s. %s. “%s…”' % (title, C.cite(x['writer'], x['pdf_page']), x['text'][:60].rstrip()))
        out.append('')
    if NOTES:
        out += ['## Notes', ''] + ['- ' + n for n in NOTES] + ['']
    if ERRORS:
        out += ['## Issues', ''] + ['- ' + e for e in ERRORS] + ['']
    with open(str(HERE / 'validation.md'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(out).rstrip() + '\n')
    print('PASS' if not ERRORS else 'FAIL')
    for e in ERRORS:
        print(' -', e)
    for n in NOTES:
        print(' note:', n)
    sys.exit(1 if ERRORS else 0)


if __name__ == '__main__':
    main()
