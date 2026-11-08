"""List the words in a draft that are outside the vocabulary of Hang's papers.

Usage, from the dissertation folder:
    python writing_style_ref/tools/check_vocabulary.py chapters/discussion.tex
    python writing_style_ref/tools/check_vocabulary.py chapters/*.tex --out report.md
    python writing_style_ref/tools/check_vocabulary.py draft.md --common 4.5

Each word is sorted into one of these groups, first match wins:
  known         the word, or its plural or verb form, is in the papers
  avoid         a common academic word that the papers never use (tech-vocabulary.md lists them)
  related       another word of the same family is in the papers (formalize when only formal is)
  reference     not in the papers, but in a reference dissertation (the committee's Short, Vazquez,
                or Bobu, or one of the 12 recent lab dissertations)
  cited         the word is only in the titles of cited works
  common        not in the papers, but common in general English (Zipf >= --common, default 4.0)
  new           not in the papers and not common: the words to look at first
  acronym       an acronym the papers do not use
  name          a capitalized word that is not in the papers, usually a name
Only the groups after "known" and "common" are reported. Listed multi-word terms that the papers
never use (Reference only, Cited only, or in none of the sources) are reported as phrases.
"""

import argparse
from collections import defaultdict, OrderedDict
import json
from pathlib import Path
import re
import runpy
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import vocab_corpus as vc  # noqa: E402

HERE = vc.HERE
GROUPS = OrderedDict([
    ('avoid', 'Common academic words the papers never use'),
    ('new', 'Uncommon words not in the papers'),
    ('field', 'Listed terms the papers do not use'),
    ('acronym', 'Acronyms not in the papers'),
    ('reference', 'Words from the reference dissertations'),
    ('related', 'Other forms of a paper word'),
    ('cited', 'Words seen only in cited titles'),
    ('name', 'Capitalized words not in the papers (mostly names)'),
])
ABOUT = {
    'avoid': 'Hang has not used these in the papers. Prefer a word from tech-vocabulary.md unless Hang chose this one.',
    'new': 'Neither the papers nor common English use these much. They are the likeliest words to be outside Hang\'s vocabulary.',
    'field': ('Terms from tech-vocabulary.md that the papers never use, with their tier, their uses in the reference '
              'dissertations, and the nearest term the papers use where there is one.'),
    'acronym': 'Check that each is defined, or use the full term. The last column shows uses in the reference dissertations.',
    'reference': ('Hang has not written these, but the reference dissertations use them. The last column names the '
                  'committee dissertations (Short, Vázquez, Bobu) and sums the recent lab dissertations as "lab". A word only one lab dissertation uses is '
                  'weak evidence that the field knows it. Define a technical one on first use, and prefer a paper word '
                  'when one says the same thing.'),
    'related': 'The papers use a different word of the same family, shown in the last column. Usually fine; prefer the paper\'s form when it says the same thing.',
    'cited': 'Hang has read these in cited titles but has not written them. Gloss on first use.',
    'name': 'Usually names of people, places, systems, or datasets. Listed so nothing is missed.',
}


def is_known_form(forms, known):
    """True when another inflection of the word is in the papers (emerge when only emerged is)."""
    for f in forms:
        if (vc.inflect(f, True) | vc.inflect(f, False)) & known:
            return True
    return False


def load():
    path = HERE / 'tech-vocabulary.json'
    if not path.exists():
        sys.exit('tech-vocabulary.json is missing. Run writing_style_ref/tools/build_vocabulary.py first.')
    return json.loads(path.read_text(encoding='utf-8'))


def read_text(path):
    raw = Path(path).read_text(encoding='utf-8', errors='replace')
    if str(path).endswith('.tex'):
        return vc.clean(raw)
    return raw.replace('\r\n', '\n')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('files', nargs='+')
    ap.add_argument('--common', type=float, default=4.0, help='Zipf frequency at or above which a word counts as common English')
    ap.add_argument('--out', help='write the report to this Markdown file instead of printing it')
    ap.add_argument('--limit', type=int, default=0, help='list at most this many words per group')
    args = ap.parse_args()

    data = load()
    surface = data['surface']
    lexicon = data['lexicon']
    known = set(surface) | set(lexicon)
    known_lower = {k.lower() for k in known}
    known_joined = {k.replace('-', '') for k in known_lower}
    stems = data['stems']
    cited = data['cited_words']
    general = vc.general_english()
    avoid = {p['word'].lower() for p in data['prose_words'] if not p['uses'] and ' ' not in p['word']}
    field = [t for t in data['terms'] if not t['uses'] and t['tier'] != 'Dissertation term' and ' ' in t['term']]
    ref_lex = {k.lower(): v for k, v in data.get('reference_lexicon', {}).items()}
    ref_acr = {k: v for k, v in data.get('reference_lexicon', {}).items() if vc.is_acronym(k)}
    ref_surface = set(data.get('reference_surface', []))

    def ref_note(counts):
        return vc.ref_summary(counts)
    authored = runpy.run_path(str(HERE / 'tools' / 'vocab_authored.py'))
    nearest = authored.get('NEAREST', {})
    also_known = {w.lower() for w in authored.get('ALSO_KNOWN', [])}
    for t in data['terms']:
        if t['tier'] == 'Dissertation term':   # chosen by Hang for the dissertation
            for f in t['forms']:
                also_known |= {w.lower() for w in vc.words(f)}

    hits = defaultdict(lambda: {'count': 0, 'where': [], 'group': None, 'note': ''})
    total = checked = 0
    files = []
    for pattern in args.files:
        matches = sorted(Path('.').glob(pattern)) if any(c in pattern for c in '*?[') else [Path(pattern)]
        files.extend(matches)
    if not files:
        sys.exit('No files matched.')

    for path in files:
        text = read_text(path)
        lines = text.split('\n')
        for n, line in enumerate(lines, 1):
            for w in vc.words(line):
                total += 1
                if w.lower() in vc.STOPWORDS or not re.search('[A-Za-z]{2}', w):
                    continue
                if len(w) < 3 and not vc.is_acronym(w):
                    continue   # abbreviations such as Ch and al
                checked += 1
                form = vc.norm(w)
                low = w.lower()
                if low.replace('-', '') in known_joined or vc.lemma(low.replace('-', ''), known_joined) in known_joined:
                    continue   # subtasks when the papers write sub-tasks
                parts = [p for p in w.split('-') if p]
                if len(parts) > 1 and all(vc.norm(p) in known or p.lower() in known_lower
                                          or vc.lemma(p, known_lower) in known_lower
                                          or general.get(p.lower(), 0) >= args.common for p in parts):
                    continue   # a new compound of known words, such as AIRL-based or robot-specific
                if vc.is_acronym(w):
                    if form in known or vc.lemma(w, known) in known:
                        continue
                    group, key = 'acronym', form
                    hits[(group, key)]['note'] = ref_note(ref_acr.get(form) or ref_acr.get(vc.lemma(w, set(ref_acr))) or {})
                else:
                    base = vc.lemma(low, known_lower)
                    forms = {low, base} | set(vc.lemma_candidates(low))
                    if forms & avoid:
                        group, key = 'avoid', base
                    elif forms & known_lower or is_known_form(forms, known_lower) or forms & also_known:
                        continue
                    else:
                        parts = low.split('-')
                        if max(general.get(f, 0) for f in forms) >= args.common:
                            continue
                        st = vc.stem(parts[-1]) if len(parts) == 1 else None
                        if st and st in stems:
                            group, key = 'related', base
                            hits[(group, key)]['note'] = ', '.join(stems[st][:4])
                        elif forms & (set(ref_lex) | ref_surface):
                            group, key = 'reference', base
                            counts = next((ref_lex[f] for f in [base, low] + sorted(forms) if f in ref_lex), {})
                            hits[(group, key)]['note'] = ref_note(counts)
                        elif forms & set(cited):
                            group, key = 'cited', base
                        elif w[:1].isupper() and not (line.lstrip().startswith(w)):
                            group, key = 'name', w
                        else:
                            group, key = 'new', base
                h = hits[(group, key)]
                h['group'] = group
                h['count'] += 1
                where = f'{path.as_posix()}:{n}'
                if len(h['where']) < 3 and where not in h['where']:
                    h['where'].append(where)
        flat = text.replace('\n', ' ')
        for t in field:
            rx = vc.term_regex(t['forms'], t['flags'])
            for m in rx.finditer(flat):
                h = hits[('field', t['term'])]
                h['group'] = 'field'
                h['count'] += 1
                bits = [t['tier'], ref_note(t.get('reference', {})), nearest.get(t['term'], '')]
                h['note'] = '; '.join(b for b in bits[:2] if b) + (f"; nearest: {bits[2]}" if bits[2] else '')
                where = f'{path.as_posix()}:{text.count(chr(10), 0, m.start()) + 1}'
                if len(h['where']) < 3 and where not in h['where']:
                    h['where'].append(where)

    # A word reported as a name in one place and as an ordinary word elsewhere is not a name.
    for (group, key), h in list(hits.items()):
        if group == 'name' and ('new', key.lower()) in hits:
            other = hits[('new', key.lower())]
            other['count'] += h['count']
            other['where'] = (other['where'] + h['where'])[:3]
            del hits[(group, key)]

    out = [f"# Vocabulary check\n",
           f"Files: {', '.join(p.as_posix() for p in files)}\n",
           f"Checked against [Hang's technical vocabulary](tech-vocabulary.md), built on {data['built']}. "
           f"{checked:,} content words of {total:,} words were checked. A word counts as common English at Zipf {args.common} or above.\n"]
    summary = []
    for g, title in GROUPS.items():
        rows = sorted(((k, h) for (gg, k), h in hits.items() if gg == g), key=lambda x: (-x[1]['count'], x[0].lower()))
        summary.append(f'{len(rows)} {title.lower()}')
        if not rows:
            continue
        out.append(f'## {title} ({len(rows)})\n')
        out.append(ABOUT[g] + '\n')
        last = {'related': 'Paper words of the same family', 'field': 'Tier, reference uses, nearest paper term',
                'reference': 'Uses in the reference dissertations',
                'acronym': 'Uses in the reference dissertations'}.get(g, 'General English (Zipf)')
        out.append(f'| Word | Uses here | Where | {last} |\n| --- | --- | --- | --- |')
        for k, h in rows[:args.limit or None]:
            if g in ('related', 'field', 'reference', 'acronym'):
                extra = h['note']
            else:
                z = general.get(k.lower())
                extra = f'{z:.1f}' if z else 'below 3.0'
            out.append(f"| {k} | {h['count']} | {', '.join(h['where'])} | {extra} |")
        out.append('')
    out.insert(3, 'Found: ' + '; '.join(summary) + '.\n')
    report = '\n'.join(out).rstrip() + '\n'
    if args.out:
        Path(args.out).write_text(report, encoding='utf-8')
        print('Wrote', args.out)
        print('Found: ' + '; '.join(summary) + '.')
    else:
        sys.stdout.reconfigure(encoding='utf-8') if hasattr(sys.stdout, 'reconfigure') else None
        print(report)


if __name__ == '__main__':
    main()
