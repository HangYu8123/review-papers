"""Validate coverage, paper evidence, evidence wording and weights, relative links, and preservation."""

from collections import Counter
import datetime
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parent
sys.path.insert(0, str(HERE / 'tools'))
import vocab_corpus as vc  # noqa: E402
ERRORS = []
# Counted in the guidance and Keep the meaning text before the October 12, 2026 revision.
MARKS_BEFORE = {':': 11, ';': 34}


def check(condition, message):
    if not condition:
        ERRORS.append(message)


def norm(s):
    # Same comparison conventions used by the Claude source library checker.
    s = re.sub(r'(?<!\\)%.*', '', s)
    s = re.sub(r'\s*\\cite[a-zA-Z]*\*?(?:\[[^\]]*\])*\{[^{}]*\}', '', s)
    s = s.replace('\\thingname{}', 'demonstration sidetracks').replace('\\ThingName{}', 'Demonstration Sidetracks')
    for _ in range(4):
        s = re.sub(r'\\(?:textit|textbf|emph|text)\{([^{}]*)\}', r'\1', s)
    s = re.sub(r'\\(?:noindent|subsection|subsubsection|section|title|item)\b', ' ', s)
    for a, b in [('\\%', '%'), ('\\_', '_'), ('\\&', '&'), ('\\,', ''),
                 ('$', ''), ('*', ''), ('{', ' '), ('}', ' ')]:
        s = s.replace(a, b)
    s = re.sub('[`\'"\u2018\u2019\u201c\u201d]', '', s)
    s = re.sub(r'\s+', ' ', s)
    return re.sub(r'\s+([,.;:)])', r'\1', s).strip()


def plain(s):
    # Review wording as the reference quotes it: no tags, emphasis as *...*, one space.
    s = re.sub(r'\\hang\{[^{}]*\}', ' ', s or '')
    s = re.sub(r'\\textit\{([^{}]*)\}', r'*\1*', s)
    s = s.replace('\\%', '%')
    return re.sub(r'\s+', ' ', s).strip()


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def same_content(path, digest):
    """True when the file matches the recorded hash, allowing for a change of line endings only.
    The paper folders were rewritten from CRLF to LF on October 14, 2026 without other changes."""
    raw = path.read_bytes()
    lf = raw.replace(b'\r\n', b'\n')
    return digest in {hashlib.sha256(x).hexdigest() for x in (raw, lf, lf.replace(b'\n', b'\r\n'))}


def strip_prefix(s, prefix):
    return s[len(prefix):] if s.startswith(prefix) else s


library = json.loads((HERE / 'library.json').read_text(encoding='utf-8'))
originals = json.loads((HERE / 'sources/source-entries.json').read_text(encoding='utf-8'))
reviews = json.loads((HERE / 'sources/review-decisions.json').read_text(encoding='utf-8'))['reviews']
expected_keys = {
    'v:' + strip_prefix(e['source_id'], 'LIB-') if e['source'] == 'v1' else 'c:' + e['source_id']
    for e in originals
}
used = [key for e in library['entries'] for key in e['sources']]
check(set(used) == expected_keys, 'Source coverage differs.')
check(all(v == 1 for v in Counter(used).values()), 'A source entry has multiple primary homes.')
check(len(originals) == 96 and library['source_counts'] == {'v1': 38, 'claude': 58}, 'Source counts differ.')
check(len(library['entries']) == library['entry_count'], 'Entry count differs.')
check(len({e['id'] for e in library['entries']}) == len(library['entries']), 'Duplicate merged ID.')

texts = {}
quote_counts = Counter()
for e in originals:
    for ev in e['evidence']:
        path = ROOT / ev['file']
        if ev['file'] not in texts:
            texts[ev['file']] = path.read_text(encoding='utf-8')
        text = texts[ev['file']]
        lines = text.splitlines()
        at = ev['line']
        if e['source'] == 'v1':
            window = '\n'.join(lines[at-1:ev.get('line_end', at)])
            check(ev['quote'] in window, f"v1 quote mismatch: {e['source_id']} {ev['file']}:{at}")
            check(same_content(path, ev['source_sha256']), f"v1 paper hash changed: {ev['file']}")
        else:
            window = norm('\n'.join(lines[max(0, at-1):at+9]))
            pos = 0
            for part in ev['quote'].split('…'):
                piece = norm(part).rstrip('.,;:')
                if not piece:
                    continue
                found = window.find(piece, pos)
                check(found >= 0, f"Claude quote mismatch: {e['source_id']} {ev['file']}:{at}")
                if found < 0:
                    break
                pos = found + len(piece)
        quote_counts[e['source']] += 1

# Evidence from Hang: every quoted piece of wording must be in its record, and only Hang's own
# decisions may be cited. The weights are recomputed from the record.
instructions = {h['id']: h for h in library['instructions']}
hand_edits = {h['id']: h for h in library['hand_edits']}
weights = library['weights']
review_items = {}
for review in reviews:
    for item in review['items']:
        check(item['id'] not in review_items, 'Duplicate review item id: ' + item['id'])
        review_items[item['id']] = dict(item, review_id=review['review_id'])


def weight_of(ev_id):
    if ev_id in instructions:
        return weights['instruction']
    if ev_id in hand_edits:
        return weights['hand edit']
    item = review_items[ev_id]
    if item['source'] != 'hang':
        return 0
    base = weights['edited'] if item['edited'] else weights['declined'] if item['status'] == 'rejected' else weights['accepted']
    return base + (weights['note_bonus'] if item.get('comment') else 0)


review_examples = said_examples = hand_examples = 0
cited = set()
for e in library['entries']:
    for x in e['review']:
        a, b, kind, ev_id = x['a'], x['b'], x['kind'], x['item']
        cited.add(ev_id)
        if kind == 'said':
            h = instructions.get(ev_id)
            check(h is not None and bool(a) and any(a in t for t in h['excerpts']),
                  f"Instruction wording differs from the record: {e['title']} {ev_id}")
            said_examples += 1
            continue
        if kind == 'hand':
            h = hand_edits.get(ev_id)
            ok = h is not None and (a or b or x['note'])
            if ok:
                ok = ((not a or any(a in plain(c['before']) for c in h['changes']))
                      and (not b or any(b in plain(c['after']) for c in h['changes'])))
            check(ok, f"Hand edit wording differs from the record: {e['title']} {ev_id}")
            hand_examples += 1
            continue
        item = review_items.get(ev_id)
        check(item is not None, 'Unknown review item: ' + ev_id)
        if item is None:
            continue
        check(item['source'] == 'hang', 'A decision that Hang did not make is cited: ' + ev_id)
        review_examples += 1
        original, suggested, final = plain(item['original']), plain(item['suggested']), plain(item['final'])
        ok = {
            'accepted': item['status'] == 'accepted' and a in original and (not b or b in final) and bool(a or b),
            'edited': item['edited'] and bool(a or b) and (not a or a in suggested) and (not b or b in final)
                      and (bool(b) or a not in final) and (bool(a) or b not in suggested),
            'declined': item['status'] == 'rejected' and a in suggested and (not b or b in original),
            'kept': item['status'] == 'accepted' and bool(b) and b in final,
            'note': bool(x['note'] or item.get('comment')),
        }.get(kind, False)
        check(ok, f"Review wording differs from the record: {e['title']} {ev_id} ({kind})")
    distinct = list(dict.fromkeys(x['item'] for x in e['review']))
    check(e['weight'] == sum(weight_of(v) for v in distinct if v in review_items or v in instructions or v in hand_edits),
          'Pattern weight differs from its evidence: ' + e['title'])
    shown = [x['weight'] for x in e['review']]
    check(shown == sorted(shown, reverse=True), 'Evidence is not ordered by weight: ' + e['title'])

# Every strong signal is cited or has a reason, and nothing is both.
uncited = {v: reason for reason, ids in library['uncited'].items() for v in ids}
strong = [v for v in review_items if weight_of(v) >= 3] + list(instructions) + list(hand_edits)
check(all(v in cited or v in uncited for v in strong), 'A strong signal is neither cited nor explained.')
check(not set(uncited) & cited, 'A signal is cited and also listed as not used.')

for review in reviews:
    c = review['counts']
    check(c['decided'] == len(review['items']) == c['accepted'] + c['declined'], 'Review counts differ: ' + review['review_id'])
    check(c['by_hang'] == sum(i['source'] == 'hang' for i in review['items']), 'Counts by Hang differ: ' + review['review_id'])
    for batch in review['batches']:
        source = (ROOT / review['folder'] / batch['file']).resolve()
        if source.exists():
            check(sha(source) == batch['sha256'], 'The decisions file changed after it was imported: ' + batch['file'])

# Chapter hand edits: the text before must be in the commit they were compared with, when git can show it.
commit = json.loads((HERE / 'sources/hand-edits.json').read_text(encoding='utf-8'))['commit']
hand_checked = 0
for h in hand_edits.values():
    for c in h['changes']:
        if not c['before'] or not c['file'].startswith('chapters/') or '*' in c['file']:
            continue
        shown = subprocess.run(['git', '-C', str(ROOT), 'show', f"{commit}:{c['file']}"], capture_output=True,
                               text=True, encoding='utf-8')
        if shown.returncode == 0:
            check(c['before'] in shown.stdout, f"Hand edit text is not in commit {commit}: {h['id']} {c['file']}")
            hand_checked += 1
    for c in h['changes']:
        if c['file'].endswith('feedback_log.md'):
            log = ROOT.parent / 'dissertation_presentation' / 'guidelines' / 'feedback_log.md'
            if log.exists():
                text = log.read_text(encoding='utf-8')
                check((not c['before'] or c['before'] in text) and (not c['after'] or c['after'] in text),
                      f"Slide edit is not in the feedback log: {h['id']}")
                hand_checked += 1

evidence_doc = (HERE / 'source-evidence.md').read_text(encoding='utf-8')
decisions_doc = (HERE / 'review-decisions.md').read_text(encoding='utf-8')
signals_doc = (HERE / 'preference-signals.md').read_text(encoding='utf-8')
main = (HERE / 'hangs-writing-style-reference.md').read_text(encoding='utf-8')
review_docs = {r['review_id']: (HERE / 'reviews' / (r['review_id'] + '.md')).read_text(encoding='utf-8') for r in reviews}
marks = Counter()
for e in library['entries']:
    check(bool(e['guidance'] and e['forms'] and e['boundary'] and (e['evidence'] or e['review'])),
          'Incomplete entry: ' + e['title'])
    check(e['guidance'] in main and e['boundary'] in main, 'Main reference differs from JSON: ' + e['title'])
    check(all(form in main for form in e['forms']), 'Missing reusable form: ' + e['title'])
    check(all(x['text'] in main for x in e['review']), 'Missing review decision: ' + e['title'])
    if e['evidence']:
        sample = e['evidence'][e['example_index']]['quote']
        check('\n'.join('> ' + line for line in sample.splitlines()) in main,
              'Selected paper example differs: ' + e['title'])
    for ev in e['evidence']:
        check(ev['quote'] in evidence_doc, 'Evidence omitted: ' + e['title'])
    for mark in MARKS_BEFORE:
        marks[mark] += (e['guidance'] + e['boundary']).count(mark)
check(set(ev['quote'] for e in originals for ev in e['evidence']) <=
      set(ev['quote'] for e in library['entries'] for ev in e['evidence']), 'A source quotation was lost.')
for item in review_items.values():
    doc = review_docs[item['review_id']]
    check(f"### {item['id']}\n" in doc, 'Review decision missing from the record: ' + item['id'])
    for field in ('original', 'suggested', 'final'):
        if item[field] and not (field == 'final' and not item['edited']) and not (field == 'original' and item['op'] == 'insert'):
            check(item[field].strip('\n') in doc, f"Review wording missing from the record: {item['id']} {field}")
    check(item['review_id'] in decisions_doc, 'Review missing from the index: ' + item['review_id'])
for ev_id in list(instructions) + list(hand_edits):
    check(f"### {ev_id}\n" in signals_doc, 'Signal missing from preference-signals.md: ' + ev_id)

# Paper sources must not change, because the quotations depend on them. The dissertation
# changes as writing continues, and the two original library folders were removed after the merge.
baseline = json.loads((HERE / 'sources/preservation-baseline.json').read_text(encoding='utf-8'))
papers = dissertation = dissertation_changed = removed = 0
for file, digest in baseline.items():
    path = ROOT / file
    if file.startswith('reference_papers/'):
        papers += 1
        check(path.exists() and same_content(path, digest), 'Paper source changed: ' + file)
    elif file.startswith('waiting_for_review/writing-style-library-'):
        removed += not path.exists()
        check(not path.exists() or same_content(path, digest), 'Original library file changed: ' + file)
    else:
        dissertation += 1
        dissertation_changed += not path.exists() or not same_content(path, digest)
snapshot_notes = []
for folder, snapshot in [('writing-style-library-v1', 'v1-library.md'),
                         ('writing-style-library-claude', 'claude-library.md')]:
    original = ROOT / 'waiting_for_review' / folder / 'library.md'
    check((HERE / 'sources' / snapshot).exists(), 'Library snapshot missing: ' + snapshot)
    if original.exists():
        check((HERE / 'sources' / snapshot).read_bytes() == original.read_bytes(), 'Library snapshot differs: ' + snapshot)
        snapshot_notes.append(snapshot + ' matches its original')
    else:
        snapshot_notes.append(snapshot + ' is the retained copy (original folder removed)')

link_count = 0
for file in list(HERE.glob('*.md')) + list((HERE / 'reviews').glob('*.md')):
    if file.name == 'validation.md':
        continue
    text = file.read_text(encoding='utf-8')
    # All authored links use simple Markdown targets; placeholders have no link target.
    for target in re.findall(r'\]\(([^)]+)\)', text):
        if re.match(r'[a-zA-Z]+:', target):
            continue
        path_part, _, fragment = target.partition('#')
        dest = (file.parent / unquote(path_part)).resolve() if path_part else file
        # The report is written at the end of this check.
        check(dest.exists() or dest == HERE / 'validation.md', 'Broken link: ' + target)
        if fragment and dest.exists() and dest.suffix == '.md':
            headings = re.findall(r'^#{1,6} (.+)$', dest.read_text(encoding='utf-8'), re.M)
            anchors = {re.sub(r'[^a-z0-9]+', '-', h.lower()).strip('-') for h in headings}
            check(fragment in anchors, 'Broken anchor: ' + target)
        link_count += 1

# The technical vocabulary: every example must quote its source line, and every listed term must
# have been found in the papers, in a cited title, or set as a dissertation term (or be reported as not found).
vocab_note = 'not built'
vocab_path = HERE / 'tech-vocabulary.json'
if vocab_path.exists():
    vocab = json.loads(vocab_path.read_text(encoding='utf-8'))
    examples = 0
    for term in vocab['terms']:
        ex = term.get('example')
        if not ex:
            continue
        examples += 1
        source = vc.PAPERS / ex['file']
        lines = source.read_text(encoding='utf-8', errors='replace').replace('\r\n', '\n').split('\n')
        bold = re.search(r'\*\*(.+?)\*\*', ex['text'])
        first = bold.group(1).split()[0].split('-')[0].lower() if bold else ''
        check(0 < ex['line'] <= len(lines) and first in lines[ex['line'] - 1].lower(),
              f"Vocabulary example does not match its source line: {term['term']} ({ex['file']}:{ex['line']})")
    # Examples from the reference dissertations must be on the PDF page they cite.
    ref_pages = {}
    for ref in vocab.get('references', []):
        text = vc.reference_text_path(ref['name']).read_text(encoding='utf-8')
        for a, b in [('ﬀ', 'ff'), ('ﬁ', 'fi'), ('ﬂ', 'fl'), ('ﬃ', 'ffi'), ('ﬄ', 'ffl'),
                     ('’', "'"), ('‘', "'")]:
            text = text.replace(a, b)
        pages = re.split(r'^\[\[page (\d+)\]\]$', text, flags=re.M)
        ref_pages[ref['file']] = {int(pages[i]): pages[i + 1].lower() for i in range(1, len(pages) - 1, 2)}
    ref_examples = 0
    for term in vocab['terms']:
        ex = term.get('reference_example')
        if not ex:
            continue
        ref_examples += 1
        bold = re.search(r'\*\*(.+?)\*\*', ex['text'])
        first = bold.group(1).split()[0].split('-')[0].lower() if bold else ''
        page_text = ref_pages.get(ex['file'], {}).get(ex['page'], '')
        check(first and first in page_text,
              f"Reference example is not on its PDF page: {term['term']} ({ex['file']} p. {ex['page']})")
    shown = sum(1 for t in vocab['terms'] if t['tier'] != 'Not found')
    missing = len(vocab['terms']) - shown
    reference_only = sum(1 for t in vocab['terms'] if t['tier'] == 'Reference only')
    vocab_note = (f"{shown} terms with familiarity estimates ({reference_only} Reference only) and {missing} field terms "
                  f"in none of the sources, built {vocab['built']}; {examples} paper examples checked against their "
                  f"source lines and {ref_examples} reference examples against their PDF pages")

word_count = len(main.split())
today = datetime.date.today()
from_papers = sum(bool(e['sources']) for e in library['entries'])
review_total = len(review_items)
report = f"""# Validation of Hang's writing style reference

Checked on {today.strftime('%B')} {today.day}, {today.year}.

| Check | Result |
| --- | --- |
| Source entry coverage | {len(originals)} of 96 entries accounted for, each with one primary merged home |
| Patterns | {len(library['entries'])} patterns across {len(library['categories'])} categories: {from_papers} merged from the source libraries and {len(library['entries']) - from_papers} from evidence from Hang |
| v1 quotation occurrences | {quote_counts['v1']} checked against exact current source lines and file hashes |
| Claude quotation occurrences | {quote_counts['claude']} checked against source-line windows using the original library's transcription conventions |
| Evidence retained | All 280 source quotation occurrences represented; exact duplicates within a pattern combined with attribution |
| Review decisions | {review_total} decisions from {len(reviews)} reviews recorded with their wording, {sum(i['source'] == 'hang' for i in review_items.values())} of them made by Hang; none of the others is cited |
| Evidence from Hang | {len(cited)} pieces cited by at least one pattern: {review_examples} review examples checked against the suggested, final, or original wording of their decision, {said_examples} quotations against Hang's instructions, and {hand_examples} against Hang's hand edits |
| Weights | Every pattern's weight recomputed from its evidence, and its evidence ordered by weight; all {len(strong)} signals of weight 3 or more cited or listed with a reason |
| Hand edits | {hand_checked} texts checked against the commit {commit} or the feedback log of the talk |
| Main guide and structured data | Guidance, forms, boundaries, review examples, and evidence checked for consistency |
| Colons and semicolons in the guidance text | {marks[':']} colons and {marks[';']} semicolons in the guidance and Keep the meaning text, down from {MARKS_BEFORE[':']} and {MARKS_BEFORE[';']} |
| Local links | {link_count} file and heading links checked |
| Technical vocabulary | {vocab_note} |
| Paper sources | {papers} paper source files compared with their pre-merge hashes |
| Dissertation files | {dissertation_changed} of {dissertation} have changed since the merge, which is expected as writing continues |
| Original library folders | {removed} files removed with the two folders after the merge |
| Library snapshots | {'; '.join(snapshot_notes)} |
| Approximate main guide length | {word_count:,} whitespace-delimited words |
| Overall result | {'PASS' if not ERRORS else 'FAIL'} |

The merge was reviewed for voice, claim strength, terminology, scale scope, flexible sentence patterns, and conceptual versus experimental continuity. The entry mapping, the resolutions, and the changes from review decisions are in [source-map.md](source-map.md).

Quotation checks establish source fidelity, not the scientific truth of every historical claim. Approximate corpus frequencies from the source libraries remain archived and were not recomputed as writing targets. The review wording check establishes that each quoted example is in the record of the review. It does not establish why Hang made a decision. This reference does not apply review decisions or the original libraries' proposed passage edits to the dissertation.
"""
if ERRORS:
    report += '\n## Issues\n\n' + '\n'.join('- ' + error for error in ERRORS) + '\n'
(HERE / 'validation.md').write_text(report, encoding='utf-8')
print(f"{'PASS' if not ERRORS else 'FAIL'}: {len(library['entries'])} patterns; {len(originals)} source entries; "
      f"{sum(quote_counts.values())} quote occurrences; {review_examples + said_examples + hand_examples} examples citing "
      f"{len(cited)} pieces of evidence from Hang; {review_total} review decisions; {link_count} links; {papers} paper sources.")
for error in ERRORS:
    print(error)
raise SystemExit(1 if ERRORS else 0)
