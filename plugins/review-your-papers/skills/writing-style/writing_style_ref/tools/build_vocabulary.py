"""Build Hang's technical vocabulary from the papers, with the reference dissertations as a second source.

Writes tech-vocabulary.md (the curated term list), word-list.md (every word the papers use,
by familiarity, and the words only the reference dissertations use), and tech-vocabulary.json
(both, plus the lexicons that check_vocabulary.py reads).
Run from the dissertation folder:  python writing_style_ref/tools/build_vocabulary.py
Edit tools/vocab_authored.py to add, move, or remove terms; never edit the generated files.

Hang's papers and drafts set the familiarity tiers. The Short, Vázquez, and Bobu dissertations
are counted separately: they never raise a tier, and a term only they use is "Reference only".
"""

import bisect
from collections import Counter, defaultdict
import datetime
import json
from pathlib import Path
import re
import runpy
import sys
from urllib.parse import quote

sys.path.insert(0, str(Path(__file__).resolve().parent))
import vocab_corpus as vc  # noqa: E402

HERE = vc.HERE
A = runpy.run_path(str(HERE / 'tools' / 'vocab_authored.py'))
CATEGORIES = A['CATEGORIES']
NOTES = A['NOTES']
GENERAL = vc.general_english()
DISSERTATION_TERMS = A['DISSERTATION_TERMS']
REFS = list(vc.REFERENCES)
TIERS = ['Core', 'Familiar', 'Dissertation term', 'Used', 'Once', 'Reference only', 'Cited only', 'Not found']
TIER_RULES = [
    ('Core', 'Used in at least three of the six studies and at least five times, or in two studies at least twenty times.',
     'Hang writes it routinely. Use it without explanation.'),
    ('Familiar', 'Used in two studies, or at least five times in one.',
     'Hang has written it in more than a passing way. Use it freely.'),
    ('Dissertation term', 'Not in the papers, but the writing style reference sets it as the dissertation\'s wording.',
     'Hang chose it for the dissertation. Use it as the style reference entry says.'),
    ('Used', 'Used two to four times, all in one study.',
     'Hang has written it, in one context. Keep to that sense.'),
    ('Once', 'Used once.',
     'Hang has written it once. Prefer a Core or Familiar word, or check the sense.'),
    ('Reference only', 'Not in the papers, but used in the Short, Vázquez, or Bobu dissertation.',
     'Hang has read it in a dissertation used as a style reference. Define it on first use, and check that the field meaning fits.'),
    ('Cited only', 'Not in the papers or the reference dissertations, but in the title of a cited work.',
     'Hang has seen it in a title. Gloss it on first use, or ask before relying on it.'),
]
WARN = []
INFO = []


def tier(uses, fams, cited=0, chosen=False, ref=0):
    if uses == 0:
        if chosen:
            return 'Dissertation term'
        if ref:
            return 'Reference only'
        return 'Cited only' if cited else 'Not found'
    if (fams >= 3 and uses >= 5) or (fams >= 2 and uses >= 20):
        return 'Core'
    if fams >= 2 or uses >= 5:
        return 'Familiar'
    return 'Used' if uses >= 2 else 'Once'


# ---------------------------------------------------------------------------
# Corpora

END = re.compile(r'(?<!e\.g)(?<!i\.e)(?<!\bal)(?<!\bvs)(?<!\bFig)(?<!\bEq)(?<!\bSec)[.?!](?=\s)|\u00a7')


def make_doc(family, kind, rel, text, pages=None):
    flat = text.replace('\n', ' ')
    return {'family': family, 'kind': kind, 'file': rel, 'text': text, 'flat': flat, 'pages': pages,
            'nl': [i for i, c in enumerate(text) if c == '\n'],
            'ends': [m.end() for m in END.finditer(flat)], 'words': len(vc.words(text))}


DOCS = [make_doc(fam, kind, rel, text) for fam, kind, rel, text in vc.documents()]
RDOCS = [make_doc(name, 'reference', pdf, text, pages) for name, pdf, text, pages in vc.reference_documents()]
TITLES = {}
for fam, rel, line, title in vc.bib_titles():
    TITLES.setdefault(title.lower(), {'title': title, 'families': set(), 'file': rel, 'line': line})['families'].add(fam)


def line_of(doc, pos):
    return bisect.bisect_right(doc['nl'], pos - 1) + 1


def link(doc, line):
    if doc['kind'] == 'reference':
        page = doc['pages'][line - 1]
        return f"[{doc['family']}, PDF p. {page}](../{quote(doc['file'], safe='/')}#page={page})"
    return f"[{doc['family']}:{line}](../reference_papers/{quote(doc['file'], safe='/')})"


def clean_piece(s):
    # \u2039math\u203a rather than [math]: a bracketed word followed by "(" would read as a Markdown link
    s = s.replace('\u00a7', ' ').replace('MATH', '\u2039math\u203a')
    s = re.sub('[\ufffd\ue000-\uf8ff]+', '\u2039math\u203a', s)   # equation symbols the PDF text could not decode
    return re.sub(r'\s+', ' ', s)


def sentence_span(doc, m):
    ends = doc['ends']
    k = bisect.bisect_right(ends, m.start())
    j = bisect.bisect_left(ends, m.end())
    return (ends[k - 1] if k else 0), (ends[j] if j < len(ends) else len(doc['flat']))


def snippet(doc, m):
    start, end = sentence_span(doc, m)
    flat = doc['flat']
    pre_raw, post_raw = clean_piece(flat[start:m.start()]), clean_piece(flat[m.end():end])
    pre, post = pre_raw.split(), post_raw.split()
    mid = clean_piece(m.group(0)).strip()
    if len(pre) > 12:
        pre = ['…'] + pre[-12:]
    if len(post) > 12:
        post = post[:12] + ['…']
    # keep a word that runs on from the term (state-action, agent's) attached to it
    text = (' '.join(pre) + (' ' if pre and pre_raw.endswith(' ') else '') + '**' + mid + '**'
            + (' ' if post_raw.startswith(' ') else '') + ' '.join(post))
    text = re.sub(r'\s+([,.;:?!)])', r'\1', text).replace('( ', '(').strip()
    if text.endswith(' \u2014'):
        text = text[:-2]
    return text.replace('|', '/')


def example_score(doc, m):
    """Prefer a full sentence from a paper, without math, where the term is not a heading."""
    start, end = sentence_span(doc, m)
    sent = doc['flat'][start:end]
    n = len(clean_piece(sent).split())
    score = 100 if doc['kind'] == 'paper' else 0
    score += 50 if 8 <= n <= 45 else (20 if n >= 6 else 0)
    score -= 15 * sent.count('MATH')
    text = m.group(0)
    if ' ' in text and text == text.title() and not vc.is_acronym(text.split()[0]):
        score -= 40   # Title Case: usually a heading or a run-in paragraph title
    if re.search(r'\\|\[|\]|\{|\}', sent):
        score -= 10
    if doc['kind'] == 'reference':
        if re.search('[^\x00-\u024f\u2013-\u2026]', sent):
            score -= 30   # unreadable math symbols in the PDF text
        if re.search(r'\b(?:Figure|Fig\.|Table|Algorithm) \d|\b[A-Z]{4,}\b|^\s*(?:Abstract|Summary)\b', sent):
            score -= 30   # a caption, figure label, or heading run into the sentence
    return score


def best_example(per_doc):
    best = None
    for order, (d, ms) in enumerate(per_doc):
        for m in ms[:40]:
            score = example_score(d, m) - order * 0.01
            if best is None or score > best[0]:
                best = (score, d, m)
    if not best:
        return None
    _, d, m = best
    line = line_of(d, m.start())
    ex = {'family': d['family'], 'kind': d['kind'], 'file': d['file'], 'line': line,
          'text': snippet(d, m), 'link': link(d, line)}
    if d['kind'] == 'reference':
        ex['page'] = d['pages'][line - 1]
    return ex


def scan(rx):
    """Uses of a term in Hang's text and in the reference dissertations, the best examples, and the cited titles."""
    st = {'paper': 0, 'draft': 0, 'families': Counter(), 'example': None, 'cited': 0, 'cited_families': set(),
          'cited_example': None, 'reference': Counter(), 'reference_example': None}
    own, ref = [], []
    for d in DOCS + RDOCS:
        ms = list(rx.finditer(d['flat']))
        if not ms:
            continue
        if d['kind'] == 'reference':
            st['reference'][d['family']] += len(ms)
            ref.append((d, ms))
        else:
            st[d['kind']] += len(ms)
            st['families'][d['family']] += len(ms)
            own.append((d, ms))
    st['example'] = best_example(own)
    st['reference_example'] = best_example(ref)
    for t in TITLES.values():
        if rx.search(t['title']):
            st['cited'] += 1
            st['cited_families'] |= t['families']
            if not st['cited_example']:
                st['cited_example'] = t['title']
    return st


def studies(fams):
    return ', '.join(f for f in vc.FAMILIES if fams.get(f))


def ref_cell(counts):
    return ' · '.join(f'{n} {counts[n]}' for n in REFS if counts.get(n))


# ---------------------------------------------------------------------------
# Lexicons of single words

tokens = []
for d in DOCS:
    for n, line in enumerate(d['text'].split('\n'), 1):
        for w in vc.words(line):
            tokens.append((d, n, w))
KNOWN = {vc.norm(w) for _, _, w in tokens}
LEX = defaultdict(lambda: {'paper': 0, 'draft': 0, 'families': Counter(), 'forms': Counter()})
SURFACE = {}
for d, n, w in tokens:
    form = vc.norm(w)
    lem = vc.lemma(w, KNOWN)
    SURFACE[form] = lem
    if lem.lower() in vc.STOPWORDS or len(lem) < 2 or not re.search('[A-Za-z]{2}', lem):
        continue
    e = LEX[lem]
    e[d['kind']] += 1
    e['families'][d['family']] += 1
    e['forms'][form] += 1
for e in LEX.values():
    e['uses'] = e['paper'] + e['draft']
    e['tier'] = tier(e['uses'], len(e['families']))
CITED_WORDS = Counter()
for t in TITLES.values():
    for w in set(vc.norm(x) for x in vc.words(t['title'])):
        CITED_WORDS[w] += 1
STEMS = defaultdict(set)
for lem in LEX:
    if not vc.is_acronym(lem):
        STEMS[vc.stem(lem.split('-')[-1]) if '-' not in lem else lem].add(lem)

# Reference dissertations: word families, joined to Hang's forms where the papers have them
rtokens = [(d, w) for d in RDOCS for w in vc.words(d['text'])]
RKNOWN = {vc.norm(w) for _, w in rtokens} | KNOWN
RLEX = defaultdict(Counter)
RLOWER = Counter()   # uses written in lower case; a word never written so is a name (Chester, Adam)
RSURFACE = set()
for d, w in rtokens:
    form = vc.norm(w)
    if len(form) < 2 or form.lower() in vc.STOPWORDS:
        continue
    RSURFACE.add(form.lower())
    lem = vc.lemma(w, KNOWN) if vc.lemma(w, KNOWN) in KNOWN else vc.lemma(w, RKNOWN)
    RLEX[lem][d['family']] += 1
    RLOWER[lem] += w[:1].islower()


def hang_has(lem):
    """True when the papers use the word in any inflection (aspect when the papers write aspects)."""
    low = lem.lower()
    forms = {low} | set(vc.lemma_candidates(low)) | vc.inflect(low, True) | vc.inflect(low, False)
    return any(f in LEX or f in SURFACE for f in forms)


# ---------------------------------------------------------------------------
# Curated terms

TERMS = []
seen = {}
covered = set()
for cat in CATEGORIES:
    groups = cat.get('groups') or [(None, cat['terms'])]
    for group, entries in groups:
        for entry in entries:
            display, forms, flags = vc.parse_term(entry)
            key = display.lower()
            if key in seen:
                WARN.append(f'"{display}" is listed twice ({seen[key]} and {cat["title"]})')
            seen[key] = cat['title']
            for f in forms:
                for w in f.lower().split():
                    covered.add(w)
                    covered |= {x.lower() for x in vc.inflect(w, True) | vc.inflect(w, False)}
            st = scan(vc.term_regex(forms, flags))
            uses = st['paper'] + st['draft']
            chosen = DISSERTATION_TERMS.get(display)
            note = NOTES.get(display, '')
            if chosen:
                ref = f"Style reference: [{chosen[0]}](hangs-writing-style-reference.md#{chosen[1]})."
                note = (note + ' ' + ref).strip()
            rec = {
                'term': display, 'forms': forms, 'flags': flags, 'category': cat['title'], 'category_id': cat['id'],
                'group': group, 'uses': uses, 'paper': st['paper'], 'draft': st['draft'],
                'families': dict(st['families']),
                'tier': tier(uses, len(st['families']), st['cited'], bool(chosen), sum(st['reference'].values())),
                'reference': dict(st['reference']), 'cited_titles': st['cited'], 'example': st['example'],
                'reference_example': st['reference_example'], 'note': note,
                'style_reference': chosen[1] if chosen else None,
            }
            if rec['tier'] == 'Not found':
                INFO.append(f'"{display}" ({cat["title"]}) is not in the papers, the reference dissertations, or the cited titles')
            TERMS.append(rec)
for key in DISSERTATION_TERMS:
    if key.lower() not in seen:
        WARN.append(f'DISSERTATION_TERMS names "{key}", which no group lists')

# Acronyms and the expansions the papers, or else the reference dissertations, give them
SMALL = {'of', 'from', 'for', 'the', 'and', 'with', 'to', 'in', 'on', 'a', 'by'}


def definitions(docs):
    defs = defaultdict(Counter)
    for d in docs:
        flat = re.sub(r'\s+', ' ', d['flat'])
        for m in re.finditer(r'\(([A-Za-z][A-Za-z0-9-]*?)s?\)', flat):
            acr = m.group(1)
            if not vc.is_acronym(acr):
                continue
            before = vc.words(flat[max(0, m.start() - 200):m.start()])
            letters = ''.join(c.lower() for c in acr if c.isalpha())
            for k in range(1, min(9, len(before)) + 1):
                cand = before[-k:]
                if cand[0].lower() in SMALL:
                    continue
                sig = [w for w in cand if w.lower() not in SMALL]
                inits = {''.join(p[0].lower() for w in ws for p in w.split('-') if p) for ws in (cand, sig)}
                inits |= {''.join(w[0].lower() for w in ws) for ws in (cand, sig)}
                if letters in inits:
                    defs[acr][' '.join(cand)] += 1
                    break
    return defs


DEFS = definitions(DOCS)
RDEFS = {d['family']: definitions([d]) for d in RDOCS}
ACRS = []
listed = {a for a, _ in A['ACRONYMS']}
for acr, exp in A['ACRONYMS']:
    # RQ1, H2: a number may follow the acronym
    rx = re.compile(r'(?<![A-Za-z0-9\-])' + re.escape(acr).replace('\\ ', '[-\\s]+') + r'(?:s|\d+)?(?![A-Za-z0-9])')
    st = scan(rx)
    detected = DEFS[acr].most_common(1)
    ref_defs = [(n, RDEFS[n][acr].most_common(1)[0][0]) for n in REFS if RDEFS[n][acr]]
    exp_rx = re.compile(re.escape(exp).replace('\\ ', '[-\\s]+').replace('\\-', '[-\\s]?'), re.I) if exp else None
    if detected:
        expansion, how = detected[0][0], 'Defined in the papers'
    elif exp_rx and any(exp_rx.search(d['flat']) for d in DOCS):
        expansion, how = exp, 'Written out in the papers'
    elif ref_defs:
        if len({e.lower() for _, e in ref_defs}) == 1:
            expansion = ref_defs[0][1]
        else:
            expansion = '; '.join(f'{e} ({n})' for n, e in ref_defs)
        how = 'Defined in ' + ' and '.join(n for n, _ in ref_defs)
    elif exp_rx and any(exp_rx.search(t['title']) for t in TITLES.values()):
        expansion, how = exp, 'Written out in a cited title'
    else:
        expansion = exp or ''
        how = 'Not written out in the papers' if st['paper'] + st['draft'] else 'Not written out in the sources'
    uses = st['paper'] + st['draft']
    ACRS.append({'acronym': acr, 'expansion': expansion, 'how': how, 'uses': uses,
                 'paper': st['paper'], 'draft': st['draft'], 'families': dict(st['families']),
                 'reference': dict(st['reference']),
                 'tier': tier(uses, len(st['families']), st['cited'], False, sum(st['reference'].values()))})
for acr, c in DEFS.items():
    if acr not in listed and sum(c.values()) >= 1:
        WARN.append(f'Acronym defined in the papers but not listed: {acr} = {c.most_common(1)[0][0]}')

# Terms seen only in cited titles
CITED = []
for entry in A['CITED_ONLY']:
    display, forms, flags = vc.parse_term(entry)
    st = scan(vc.term_regex(forms, flags))
    uses = st['paper'] + st['draft']
    if uses:
        WARN.append(f'Cited-only term "{display}" is used {uses} times in the papers; move it to a category')
    if not st['cited']:
        WARN.append(f'Cited-only term "{display}" is not in any cited title')
    CITED.append({'term': display, 'uses': uses, 'cited_titles': st['cited'],
                  'cited_families': [f for f in vc.FAMILIES if f in st['cited_families']],
                  'example_title': st['cited_example'], 'reference': dict(st['reference'])})

# Common academic words checked against the papers and the reference dissertations
PROSE = []
for entry in A['PROSE_WORDS_TO_CHECK']:
    single = ' ' not in entry.strip()
    flags = 'v' if single and not entry.endswith('ly') else 'x'
    display, forms, _ = vc.parse_term(entry)
    st = scan(vc.term_regex(forms, flags))
    PROSE.append({'word': display, 'uses': st['paper'] + st['draft'], 'families': dict(st['families']),
                  'reference': dict(st['reference'])})

# Frequent, less common words not yet in any category (shown by this script, for curation)
UNSORTED = []
for lem, e in sorted(LEX.items(), key=lambda x: -x[1]['uses']):
    if e['uses'] < 6 or vc.is_acronym(lem) or not re.fullmatch(r'[a-z][a-z-]+', lem):
        continue
    if lem in covered or GENERAL.get(lem, 0) >= 4.6:
        continue
    UNSORTED.append((lem, e['uses'], len(e['families'])))

# ---------------------------------------------------------------------------
# Markdown

today = datetime.date.today()
DATE = f"{today.strftime('%B')} {today.day}, {today.year}"
tier_rank = {t: i for i, t in enumerate(TIERS)}
tier_count = Counter(t['tier'] for t in TERMS)


def slug(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


def uses_cell(r):
    if not r['uses']:
        return '0'
    s = str(r['uses'])
    if r['draft'] and r['paper']:
        s += f" ({r['draft']} in drafts)"
    elif r['draft']:
        s += ' (drafts only)'
    return s


def term_cell(r):
    s = f"**{r['term']}**"
    others = [f for f in r['forms'][1:]]
    if others:
        s += ' (also ' + ', '.join(others) + ')'
    if r['note']:
        s += '<br>' + r['note']
    return s


def example_cell(r):
    ex = r['example']
    if ex:
        return f"{ex['text']} — {ex['link']}"
    ex = r.get('reference_example')
    if ex:
        return f"*Reference:* {ex['text']} — {ex['link']}"
    return f"Cited in {r['cited_titles']} titles" if r['cited_titles'] else ''


fam_words = Counter()
fam_files = defaultdict(lambda: [0, 0])
for d in DOCS:
    fam_words[(d['family'], d['kind'])] += d['words']
    fam_files[d['family']][0 if d['kind'] == 'paper' else 1] += 1
total_words = sum(fam_words.values())
ref_words = sum(d['words'] for d in RDOCS)
ref_only = [r for r in TERMS if r['tier'] == 'Reference only']

md = [f"""# Hang's technical vocabulary

This list collects technical terms and estimates how familiar each one is to Hang. The estimate comes from how often, and in how many studies, Hang's papers use a term. Three dissertations that Hang uses as style references, by Short, Vázquez, and Bobu, are a second source. They show the words Hang has read, are counted in their own column, and never raise a tier. The list covers {len(TERMS)} terms in {len(CATEGORIES)} groups, {len(ACRS)} acronyms, and {len(CITED)} terms that Hang has met only in the titles of cited work. {len(ref_only)} of the terms are Reference only. [word-list.md](word-list.md) lists every word the papers use, with the same familiarity estimate, and the words only the reference dissertations use.

Use it together with [Hang's writing style reference](hangs-writing-style-reference.md). When drafting or revising dissertation prose, prefer terms marked Core or Familiar. A term marked Once, Reference only, or Cited only is one Hang has met but seldom or never writes, so check its sense or define it. A word that is in none of the lists falls outside the vocabulary. `python writing_style_ref/tools/check_vocabulary.py <file>` lists such words in a draft.

Built on {DATE} from {total_words:,} words of Hang's own text in {len(DOCS)} files and {ref_words:,} words of the three reference dissertations.

## How familiarity is estimated

| Tier | Rule | What it suggests |
| --- | --- | --- |"""]
md.extend(f'| {t} | {rule} | {use} |' for t, rule, use in TIER_RULES)
md.append(f"""
Terms per tier: {', '.join(f'{tier_count[t]} {t}' for t in TIERS if tier_count[t])}.

A use is one occurrence in a paper or a draft. A study is one of the six paper families below. The count is by word form, so a common word such as state, return, or progress is counted in every sense, and a term also counts inside a longer term (reward function inside learned reward function). Drafts count as Hang's own writing, since they are earlier versions written for the same studies. Each paper was coauthored, and CHARM was written with a co-first author, so a term found only in CHARM is weaker evidence of Hang's own word choice. The prospectus is single-authored. Comments, math, citations, and the notes of coauthors and advisors in the LaTeX are not counted.

The Reference dissertations column counts the same term in the three dissertations. A high count there and none in the papers means the term belongs to the field, or to a neighboring field, more than to Hang's own writing. Where the papers have no example, the example comes from a reference dissertation and is marked *Reference*. Those examples quote another writer and are not models of Hang's wording.

## Sources

| Study | Papers | Drafts | Words in papers | Words in drafts |
| --- | --- | --- | --- | --- |""")
for fam in vc.FAMILIES:
    md.append(f"| {fam} | {fam_files[fam][0]} | {fam_files[fam][1]} | {fam_words[(fam, 'paper')]:,} | {fam_words[(fam, 'draft')]:,} |")
md.append('\nThe files are listed in `tools/vocab_corpus.py`. The ACM and conference template files in the same folders, and the copies of the Progress files kept in `CHARM/`, are left out. Cited titles come from each study\'s `.bib` files.\n')
md.append('| Reference dissertation | PDF pages used | Words |\n| --- | --- | --- |')
for d in RDOCS:
    ref = vc.REFERENCES[d['family']]
    rng = ', '.join(f'{a}–{b}' if a != b else str(a) for a, b in ref['pages'])
    md.append(f"| [{ref['title']}](../{quote(ref['pdf'], safe='/')}) | {rng} | {d['words']:,} |")
md.append('\nOnly the abstract and the chapters are used. The front matter, the tables of contents, and the bibliography are left out, and running heads and page numbers are removed. The text was extracted with pdftotext into `sources/reference-dissertations/`. Bobu\'s equations come out of the PDF as unreadable symbols, so a few counts of short words there may be off.\n')

md.append('## Quick list\n')
md.append('The terms Hang uses in each group, most used first. Core terms are in bold. Terms marked Used, Once, '
          'Reference only, or Cited only are in the tables below.\n')
for cat in CATEGORIES:
    rows = [r for r in sorted(TERMS, key=lambda r: (-r['uses'], r['term'].lower()))
            if r['category_id'] == cat['id'] and r['tier'] in ('Core', 'Familiar', 'Dissertation term')]
    names = [f"**{r['term']}**" if r['tier'] == 'Core' else r['term'] + (' (dissertation term)' if r['tier'] == 'Dissertation term' else '')
             for r in rows]
    n_ref = sum(1 for r in ref_only if r['category_id'] == cat['id'])
    tail = f' Reference only: {n_ref} terms.' if n_ref else ''
    md.append(f"- [{cat['title']}](#{slug(cat['title'])}). " + (', '.join(names) + '.' if names else 'None.') + tail)
md.append('')

md.append('## Groups\n')
for cat in CATEGORIES:
    n = sum(1 for r in TERMS if r['category_id'] == cat['id'] and r['tier'] != 'Not found')
    md.append(f"- [{cat['title']}](#{slug(cat['title'])}) ({n} terms)")
md.append('- [Field terms in none of the sources](#field-terms-in-none-of-the-sources)')
md.append('- [Acronyms](#acronyms)')
md.append('- [Terms seen only in cited titles](#terms-seen-only-in-cited-titles)')
md.append('- [Common academic words and the papers](#common-academic-words-and-the-papers)\n')

HEAD = ('| Term | Familiarity | Uses | Studies | Reference dissertations | Example |\n'
        '| --- | --- | --- | --- | --- | --- |')


def table(rows):
    out = [HEAD]
    rows = [r for r in rows if r['tier'] != 'Not found']
    for r in sorted(rows, key=lambda r: (tier_rank[r['tier']], -r['uses'], -sum(r['reference'].values()), r['term'].lower())):
        out.append(f"| {term_cell(r)} | {r['tier']} | {uses_cell(r)} | {studies(r['families'])} | "
                   f"{ref_cell(r['reference'])} | {example_cell(r)} |")
    return out


for cat in CATEGORIES:
    md.append(f"## {cat['title']}\n")
    md.append(cat['about'] + '\n')
    if cat.get('groups'):
        for group, _ in cat['groups']:
            md.append(f'### {group}\n')
            md.extend(table([r for r in TERMS if r['category_id'] == cat['id'] and r['group'] == group]))
            md.append('')
    else:
        md.extend(table([r for r in TERMS if r['category_id'] == cat['id']]))
        md.append('')

missing = [r for r in TERMS if r['tier'] == 'Not found']
md.append('## Field terms in none of the sources\n')
md.append(f'These {len(missing)} standard terms were searched for and are in neither the papers, the reference dissertations, '
          'nor the cited titles. Hang may still know them, but the sources give no evidence of it. '
          'Where a near term is listed above, it is named.\n')
md.append('| Term | Group | Nearest term the papers use |\n| --- | --- | --- |')
NEAR = A.get('NEAREST', {})
for r in missing:
    md.append(f"| {r['term']} | {r['category']} | {NEAR.get(r['term'], '')} |")
md.append('')

md.append('## Acronyms\n')
md.append('The expansion is the one the papers define, where they define one, and otherwise the one a reference '
          'dissertation defines. Uses count the short form only.\n')
md.append('| Acronym | Stands for | Source of the expansion | Familiarity | Uses | Studies | Reference dissertations |\n'
          '| --- | --- | --- | --- | --- | --- | --- |')
for a in sorted(ACRS, key=lambda a: (tier_rank[a['tier']], -a['uses'], -sum(a['reference'].values()), a['acronym'].lower())):
    md.append(f"| **{a['acronym']}** | {a['expansion']} | {a['how']} | {a['tier']} | {uses_cell(a)} | "
              f"{studies(a['families'])} | {ref_cell(a['reference'])} |")

md.append('\n## Terms seen only in cited titles\n')
md.append('These terms are in the titles of works the papers cite and nowhere in the papers\' own text. Hang has read them, '
          'which is weaker evidence than writing them. The last column shows where a reference dissertation uses the term.\n')
md.append('| Term | Cited titles | Cited in | Example title | Reference dissertations |\n| --- | --- | --- | --- | --- |')
for c in sorted(CITED, key=lambda c: (-c['cited_titles'], c['term'].lower())):
    md.append(f"| **{c['term']}** | {c['cited_titles']} | {', '.join(c['cited_families'])} | "
              f"{(c['example_title'] or '').replace('|', '/')} | {ref_cell(c['reference'])} |")

used = [p for p in PROSE if p['uses']]
unused = [p for p in PROSE if not p['uses']]


def prose_ref(p):
    c = ref_cell(p['reference'])
    return f" ({c})" if c else ''


md.append(f"""
## Common academic words and the papers

These {len(PROSE)} words and phrases are frequent in academic prose and in text drafted by assistants. Each was searched for in the papers and in the reference dissertations.

**Used in the papers** ({len(used)}). """ + ', '.join(f"{p['word']} ({p['uses']})" for p in sorted(used, key=lambda p: -p['uses'])) + '.')
md.append(f"""
**Not used in the papers** ({len(unused)}). """ + ', '.join(p['word'] + prose_ref(p) for p in sorted(unused, key=lambda p: p['word'])) + '.')
md.append("""
A word in the second list is not wrong, but Hang has not used it in the papers. Counts in parentheses show where a reference dissertation uses it. Hang's own wording takes priority over the reference dissertations, as in the writing style reference, so in prose written for Hang choose a word from the lists above unless Hang introduces it.
""")

md.append(f"""## Rebuilding

Edit `tools/vocab_authored.py` to add, move, or remove a term, then run `python writing_style_ref/tools/build_vocabulary.py` from the dissertation folder. The build prints terms that it could not find and frequent words from the papers that no group lists yet. To check a draft against the vocabulary, run `python writing_style_ref/tools/check_vocabulary.py chapters/<file>.tex`. General English frequencies come from a snapshot of wordfreq in `sources/general-english-zipf.tsv`, made with `tools/make_general_english.py`. The reference dissertation text is extracted again with `tools/extract_reference_text.py`.
""")
if WARN:
    md.append('## Build notes\n')
    md.extend('- ' + w for w in WARN)
    md.append('')
(HERE / 'tech-vocabulary.md').write_text('\n'.join(md).rstrip() + '\n', encoding='utf-8')

# word-list.md
wl = [f"""# Words in Hang's papers

Every word family in Hang's papers and drafts, grouped by the familiarity tiers of [Hang's technical vocabulary](tech-vocabulary.md). A word family joins the plural and verb forms that occur in the papers (demonstrations with demonstration, annotated with annotate). The number after a word is its count of uses.

Very common English words (Zipf frequency 5.0 or above in general English, such as make, time, and result) are left out here, since they say little about technical vocabulary. They are still in `tech-vocabulary.json` and count as known in the checker. Names, acronyms, and dataset labels are listed after the tiers. The last section lists words that only the reference dissertations use.

Built on {DATE} from {total_words:,} words in {len(DOCS)} files and {ref_words:,} words of the reference dissertations.
"""]
words_by_tier = defaultdict(list)
names = []
for lem, e in LEX.items():
    if vc.is_acronym(lem) or lem[:1].isupper():
        names.append((lem, e))
        continue
    if not re.fullmatch(r"[a-z][a-z'-]*[a-z]", lem) or len(lem) < 3:
        continue
    if GENERAL.get(lem, 0) >= 5.0:
        continue
    words_by_tier[e['tier']].append((lem, e))
for t in ('Core', 'Familiar', 'Used', 'Once'):
    items = sorted(words_by_tier[t], key=lambda x: x[0])
    wl.append(f'## {t} ({len(items)} words)\n')
    wl.append(dict((r[0], r[1]) for r in TIER_RULES)[t] + '\n')
    for letter in sorted({w[0] for w, _ in items}):
        row = [f'{w} {e["uses"]}' for w, e in items if w[0] == letter]
        wl.append(f'**{letter.upper()}** ' + ' · '.join(row) + '\n')
wl.append(f'## Names, acronyms, and labels ({len(names)})\n')
wl.append(' · '.join(f'{w} {e["uses"]}' for w, e in sorted(names, key=lambda x: x[0].lower())) + '\n')

INITIAL = {n: n[0] for n in REFS}
ref_words_only = []
for lem, c in RLEX.items():
    if hang_has(lem) or vc.is_acronym(lem) or lem[:1].isupper():
        continue
    if not re.fullmatch(r"[a-z][a-z'-]*[a-z]", lem) or len(lem) < 3 or lem in vc.STOPWORDS:
        continue
    z = GENERAL.get(lem, 0)
    n_refs, total = len(c), sum(c.values())
    if z >= 5.0 or total < 3 or not (n_refs >= 2 or z >= 3.0):
        continue
    if RLOWER[lem] < max(2, total // 2) or (len(lem) <= 3 and z < 4.0):
        continue   # names (Chester, Adam, Bartneck) and abbreviations (alg, arg)
    ref_words_only.append((lem, total, ''.join(INITIAL[n] for n in REFS if c.get(n))))
ref_words_only.sort()
wl.append(f'## Only in the reference dissertations ({len(ref_words_only)} words)\n')
wl.append('Words that the Short (S), Vázquez (V), or Bobu (B) dissertation uses at least three times and Hang\'s papers '
          'never use. A word is kept when two of the dissertations use it or when it is in the general English list, '
          'which removes most of the symbols that the PDF equations turn into. Names (words the dissertations write only '
          'with a capital, such as the robot Chester) and short abbreviations are left out, and so are very common words. '
          'Reference only in the sense of the tiers, so Hang has read them but not written them.\n')
for letter in sorted({w[0] for w, _, _ in ref_words_only}):
    row = [f'{w} {n} ({s})' for w, n, s in ref_words_only if w[0] == letter]
    wl.append(f'**{letter.upper()}** ' + ' · '.join(row) + '\n')
(HERE / 'word-list.md').write_text('\n'.join(wl).rstrip() + '\n', encoding='utf-8')

# JSON
data = {
    'built': today.isoformat(),
    'corpus': [{'family': d['family'], 'kind': d['kind'], 'file': d['file'], 'words': d['words']} for d in DOCS],
    'references': [{'name': d['family'], 'title': vc.REFERENCES[d['family']]['title'], 'file': d['file'],
                    'pages': vc.REFERENCES[d['family']]['pages'], 'words': d['words']} for d in RDOCS],
    'tiers': [{'tier': t, 'rule': r, 'use': u} for t, r, u in TIER_RULES],
    'terms': TERMS,
    'acronyms': ACRS,
    'cited_only': CITED,
    'prose_words': PROSE,
    'lexicon': {lem: {'uses': e['uses'], 'paper': e['paper'], 'draft': e['draft'],
                      'families': dict(e['families']), 'forms': dict(e['forms']), 'tier': e['tier']}
                for lem, e in sorted(LEX.items())},
    'surface': dict(sorted(SURFACE.items())),
    'stems': {s: sorted(v) for s, v in sorted(STEMS.items())},
    'cited_words': dict(sorted(CITED_WORDS.items())),
    'reference_lexicon': {lem: dict(c) for lem, c in sorted(RLEX.items())},
    'reference_surface': sorted(RSURFACE),
}


def dump(value):
    """One line per list item or dictionary entry, so the file stays small and diffs stay readable."""
    one = lambda v: json.dumps(v, ensure_ascii=False, separators=(',', ':'))  # noqa: E731
    if isinstance(value, list) and not all(isinstance(v, str) for v in value):
        return '[\n' + ',\n'.join('  ' + one(v) for v in value) + '\n ]'
    if isinstance(value, dict) and value and all(isinstance(v, (dict, list)) for v in value.values()):
        return '{\n' + ',\n'.join('  ' + one(k) + ':' + one(v) for k, v in value.items()) + '\n }'
    return one(value)


(HERE / 'tech-vocabulary.json').write_text(
    '{\n' + ',\n'.join(f' {json.dumps(k)}: {dump(v)}' for k, v in data.items()) + '\n}\n', encoding='utf-8')

print(f'{len(TERMS)} terms, {len(ACRS)} acronyms, {len(CITED)} cited-only terms, {len(PROSE)} prose words checked.')
print('Tiers:', dict(tier_count))
print(f'Lexicon: {len(LEX)} word families from {total_words:,} words in {len(DOCS)} files; '
      f'{len(RLEX)} from {ref_words:,} words of the reference dissertations; '
      f'{len(ref_words_only)} listed as reference-only words.')
for w in WARN:
    print('NOTE:', w)
for w in INFO:
    print('Not found:', w)
if UNSORTED:
    print(f'\nFrequent words not in any group ({len(UNSORTED)}):')
    print(', '.join(f'{w} ({n}, {f})' for w, n, f in UNSORTED))
