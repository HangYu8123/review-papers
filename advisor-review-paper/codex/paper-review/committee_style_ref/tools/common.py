"""Shared helpers: the three sources, their page text, quotation matching, and counts."""
import re
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parent

# body is the first and last PDF page of the numbered chapters. offset is
# PDF page minus printed page inside the body. abstract lists the PDF pages of
# the abstract, which carry no arabic page number.
SOURCES = {
    'short': dict(
        author='Short', full='Elaine Schaertl Short', year=2017,
        title='Managing Multi-Party Social Dynamics for Socially Assistive Robotics',
        school='University of Southern California',
        pdf='dessertation_reference/Short_2017_USC_thesis.pdf',
        body=(19, 189), offset=18, abstract=(17, 18)),
    'vazquez': dict(
        author='Vázquez', full='Marynel Vázquez', year=2017,
        title='Reasoning About Spatial Patterns of Human Behavior During Group Conversations with Robots',
        school='Carnegie Mellon University',
        pdf='dessertation_reference/Vazquez_2017_CMU_thesis.pdf',
        body=(8, 90), offset=7, abstract=(2, 2)),
    'bobu': dict(
        author='Bobu', full='Andreea Bobu', year=2023,
        title='Aligning Robot Representations with Humans',
        school='University of California, Berkeley',
        pdf='dessertation_reference/Bobu_2023_Berkeley_EECS-2023-200.pdf',
        body=(15, 199), offset=14, abstract=(5, 5)),
}
ORDER = ['short', 'vazquez', 'bobu']

UNREADABLE = chr(0xFFFD)
LIGATURES = {chr(0xFB00): 'ff', chr(0xFB01): 'fi', chr(0xFB02): 'fl', chr(0xFB03): 'ffi', chr(0xFB04): 'ffl'}
PUNCT = {chr(0x2018): "'", chr(0x2019): "'", chr(0x201C): '"', chr(0x201D): '"', chr(0x2013): '-',
         chr(0x2014): '-', chr(0x2212): '-', chr(0x00A0): ' ', chr(0x2022): '', chr(0x2026): '...'}
HEADER = re.compile(r"^CHAPTER \d+\. [A-Z0-9 ,:&'" + chr(0x2019) + r"-]+$")
ROMAN = re.compile(r'^[ivxlcIVXLC]+$')
_PAGES = {}


def pages(key):
    """PDF page number -> list of text lines."""
    if key not in _PAGES:
        out, cur = {}, None
        text = (HERE / 'sources' / 'text' / (key + '.txt')).read_text(encoding='utf-8')
        for line in text.split('\n'):
            m = re.match(r'\[\[page (\d+)\]\]$', line)
            if m:
                cur = int(m.group(1))
                out[cur] = []
            elif cur is not None:
                out[cur].append(line)
        _PAGES[key] = out
    return _PAGES[key]


def clean_lines(key, n):
    """Lines of a page without the running head and the page number."""
    out = []
    for line in pages(key).get(n, []):
        s = line.strip()
        if not s or s.isdigit() or ROMAN.match(s) or HEADER.match(s):
            continue
        out.append(s)
    return out


def fold(s):
    for a, b in LIGATURES.items():
        s = s.replace(a, b)
    for a, b in PUNCT.items():
        s = s.replace(a, b)
    return s


def strict(s):
    """Wording and punctuation, with ligatures, quote marks and spacing made uniform."""
    return re.sub(r'\s+', ' ', fold(s)).strip()


def loose(s):
    """Letters and digits only. Survives a hyphen lost at a line break in the PDF text."""
    return re.sub(r'[^a-z0-9]+', '', fold(s).lower())


def match_in(text, quote):
    """Return 'exact', 'letters', or '' for a quotation against a stretch of text.

    [...] marks an omission, and the parts must appear in order.
    """
    parts = [p.strip() for p in quote.split('[...]') if p.strip()]
    for result, norm in (('exact', strict), ('letters', loose)):
        hay, pos, ok = norm(text), 0, True
        for part in parts:
            i = hay.find(norm(part), pos)
            if i < 0:
                ok = False
                break
            pos = i + len(norm(part))
        if ok:
            return result
    return ''


def find_quote(key, page, quote):
    """Check a quotation cited to a PDF page. It may run on to the next page."""
    return match_in(' '.join(clean_lines(key, page) + clean_lines(key, page + 1)), quote)


def locate(key, quote):
    """PDF pages on which a quotation starts, for repairing a wrong page number."""
    found = []
    for n in sorted(pages(key)):
        if match_in(' '.join(clean_lines(key, n)), quote):
            found.append(n)
    if not found:
        for n in sorted(pages(key)):
            if match_in(' '.join(clean_lines(key, n) + clean_lines(key, n + 1)), quote):
                found.append(n)
    return found


def printed_page(key, page):
    """Printed page label for a PDF page, or '' outside the numbered chapters."""
    src = SOURCES[key]
    if src['body'][0] <= page <= src['body'][1]:
        return str(page - src['offset'])
    return ''


def cite(key, page):
    src = SOURCES[key]
    p = printed_page(key, page)
    if p:
        return '%s, p. %s (PDF page %d)' % (src['author'], p, page)
    if src['abstract'][0] <= page <= src['abstract'][1]:
        return '%s, abstract (PDF page %d)' % (src['author'], page)
    return '%s, PDF page %d' % (src['author'], page)


def pdf_link(key, page, base='..'):
    return '%s/%s#page=%d' % (base, SOURCES[key]['pdf'], page)


ABBREV = ['e.g.', 'i.e.', 'et al.', 'Fig.', 'Figs.', 'Sec.', 'Secs.', 'Eq.', 'Eqs.', 'vs.', 'cf.',
          'Alg.', 'approx.', 'etc.', 'Dr.', 'St.', 'pp.', 'No.', 'Ext.', 'resp.']
DOT = chr(0x00B7)


def paragraphs_of(lines):
    """Keep lines that read as running prose. Lines with unreadable symbols are dropped."""
    out = []
    for line in lines:
        if UNREADABLE in line:
            continue
        if len(line.split()) >= 20 and re.search(r'[a-z]{3,}', line):
            out.append(fold(line))
    return out


def prose(key, abstract=False):
    """Paragraph-like lines of the numbered chapters, optionally with the abstract."""
    src = SOURCES[key]
    wanted = list(range(src['body'][0], src['body'][1] + 1))
    if abstract:
        wanted = list(range(src['abstract'][0], src['abstract'][1] + 1)) + wanted
    out = []
    for n in wanted:
        out.extend(paragraphs_of(clean_lines(key, n)))
    return out


def sentences(paragraphs):
    out = []
    for p in paragraphs:
        for a in ABBREV:
            p = p.replace(a, a.replace('.', DOT))
        p = re.sub(r'(\d)\.(\d)', lambda m: m.group(1) + DOT + m.group(2), p)
        for s in re.split(r'(?<=[.!?])["\')\]]?\s+(?=["\'(\[]?[A-Z])', p):
            s = s.replace(DOT, '.').strip()
            if len(s.split()) >= 3:
                out.append(s)
    return out


def words(text):
    return re.findall(r"[A-Za-z][A-Za-z'-]*", text)


OPENERS = ['However', 'Additionally', 'Finally', 'Lastly', 'For example', 'For instance', 'In general',
           'In particular', 'Moreover', 'Furthermore', 'In addition', 'Unfortunately', 'Interestingly',
           'Thus', 'Therefore', 'First', 'Second', 'Third', 'Overall', 'Instead', 'Nonetheless']
RATES = [
    ('we', r"\b(?:[Ww]e|[Oo]ur|us|[Oo]urs|ourselves)\b"),
    ('colon', r"(?<!\d):|:(?!\d)"),
    ('semicolon', r";"),
    ('question', r"\?"),
    ('contraction', r"\b[A-Za-z]+n't\b|\b(?:[Ii]t|[Tt]hat|[Ww]hat|[Tt]here|[Hh]ere|[Ll]et)'s\b|\b[A-Za-z]+'(?:re|ve|ll)\b"),
    ('suggest', r"\b[Ss]uggest\w*"),
    ('may', r"\b[Mm]ay\b"),
    ('might', r"\b[Mm]ight\b"),
    ('could', r"\b[Cc]ould\b"),
    ('can', r"\b[Cc]an\b"),
    ('likely', r"\b[Ll]ikely\b"),
    ('tend', r"\b[Tt]end(?:s|ed|ing)?\b"),
    ('enable', r"\b[Ee]nabl(?:e|es|ed|ing)\b"),
    ('leverage', r"\b[Ll]everag(?:e|es|ed|ing)\b"),
]
COUNTS = [
    ('n_this_dissertation', r"\b[Tt]his dissertation\b"),
    ('n_this_thesis', r"\b[Tt]his thesis\b"),
    ('n_this_work', r"\b[Tt]his work\b"),
    ('n_this_chapter', r"\b[Tt]his chapter\b"),
]


def opener_key(opener):
    return 'open_' + opener.lower().replace(' ', '_')


def measure(paragraphs):
    """Counts and rates for a list of prose paragraphs. Rates are per 1,000 words."""
    text = ' '.join(paragraphs)
    n_words = len(words(text))
    sents = sentences(paragraphs)
    lengths = sorted(len(s.split()) for s in sents)
    mid = len(lengths) // 2
    median = lengths[mid] if len(lengths) % 2 else (lengths[mid - 1] + lengths[mid]) / 2.0
    out = dict(
        paragraphs=len(paragraphs), words=n_words, sentences=len(sents),
        sent_mean=round(sum(lengths) / float(len(lengths)), 1),
        sent_median=int(median) if median == int(median) else median,
        short_share=int(round(100.0 * sum(1 for n in lengths if n <= 12) / len(lengths))),
        long_share=int(round(100.0 * sum(1 for n in lengths if n >= 35) / len(lengths))),
    )
    for name, pattern in RATES:
        out[name] = round(1000.0 * len(re.findall(pattern, text)) / n_words, 1)
    for name, pattern in COUNTS:
        out[name] = len(re.findall(pattern, text))
    for opener in OPENERS:
        out[opener_key(opener)] = sum(1 for s in sents if s.startswith(opener + ','))
    ranked = sorted(((out[opener_key(o)], o) for o in OPENERS), reverse=True)
    out['top_openers'] = [[o, n] for n, o in ranked if n][:8]
    return out
