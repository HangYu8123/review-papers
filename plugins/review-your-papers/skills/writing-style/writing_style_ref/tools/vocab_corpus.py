"""Read Hang's papers as plain text for the technical vocabulary.

The corpus lists the paper files by family. Each file is either a paper (the latest
manuscript of a study) or a draft (an earlier manuscript, a cut section, or a draft
of the same study). LaTeX is reduced to prose with the line breaks kept, so that every
word can be traced to its source line. Math, citations, labels, comments, and the notes
of co-authors and advisors (\\elaine, \\rma, \\jindan, \\todo, \\hang, \\delete) are removed.
Cited titles from the .bib files form a separate, weaker source of evidence.
"""

from pathlib import Path
import hashlib
import os
import re
from urllib.parse import quote

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parent
# The papers are not bundled with the plugin. Set VOCAB_PAPERS to the dissertation folder's
# reference_papers/ to rebuild from a copy of this folder kept elsewhere.
PAPERS = Path(os.environ.get('VOCAB_PAPERS') or ROOT / 'reference_papers')

# family -> list of (relative path, kind). Identical copies (the Progress files that are
# also in CHARM/) are listed once, under the study they belong to.
CORPUS = {
    'CHARM': [
        ('CHARM/ROMAN 2025.tex', 'paper'),
    ],
    'Sidetracks': [
        ('Demonstration_sidetracks/main.tex', 'paper'),
    ],
    'PHIRL': [
        ('PHIRL/CoRL_2026_main.tex', 'paper'),
        ('PHIRL/introduction.tex', 'paper'),
        ('PHIRL/background.tex', 'paper'),
        ('PHIRL/methodology.tex', 'paper'),
        ('PHIRL/experiment.tex', 'paper'),
        ('PHIRL/conclusion.tex', 'paper'),
        ('PHIRL/appendix.tex', 'paper'),
        ('PHIRL/ICML/ICML 2026 PHIRL.tex', 'draft'),
        ('PHIRL/ICML/naive_baseline.tex', 'draft'),
        ('PHIRL/ICML/real_robot_study.tex', 'draft'),
        ('PHIRL/ICML/square.tex', 'draft'),
        ('PHIRL/ICML/succ_rate_and_learning_curves.tex', 'draft'),
        ('PHIRL/legacy/AAAI 2026 PHIRL.tex', 'draft'),
        ('PHIRL/legacy/PHIRL.tex', 'draft'),
        ('PHIRL/legacy/paper draft.tex', 'draft'),
        ('PHIRL/legacy/neurips_2025.tex', 'draft'),
    ],
    'Progress': [
        ('Progress/Ro-MAN 2024.tex', 'paper'),
        ('Progress/paper_template.tex', 'draft'),
        ('Progress/epitaph for my brain cells.tex', 'draft'),
    ],
    'STEADY': [
        ('STEADY/IEEEexample.tex', 'paper'),
    ],
    'Prospectus': [
        ('prospectus/RSS Pioneers 2026.tex', 'paper'),
        ('prospectus/HRI Pioneers.tex', 'paper'),
        ('prospectus/unused.tex', 'draft'),
    ],
}
FAMILIES = list(CORPUS)

# Bibliographies whose titles show what Hang read and cited. The ACM sample bibliographies
# (sample-base.bib, software.bib) are template files and are not used.
BIBS = {
    'CHARM': ['CHARM/references.bib'],
    'Sidetracks': ['Demonstration_sidetracks/main.bib', 'Demonstration_sidetracks/ref.bib'],
    'PHIRL': ['PHIRL/example.bib', 'PHIRL/ICML/ICML.bib', 'PHIRL/ICML/references.bib',
              'PHIRL/legacy/aaai2026.bib'],
    'Progress': ['Progress/references.bib'],
    'STEADY': ['STEADY/IEEEexample.bib'],
    'Prospectus': ['prospectus/references.bib'],
}

# Files present in reference_papers/ that are not Hang's writing.
NOT_USED = {
    'prospectus/sample-sigconf.tex': 'ACM template',
    'prospectus/sample-sigconf-biblatex.tex': 'ACM template',
    'prospectus/sample-sigconf-i13n.tex': 'ACM template',
    'prospectus/sample-sigconf-lualatex.tex': 'ACM template',
    'prospectus/sample-sigconf-xelatex.tex': 'ACM template',
    'PHIRL/ICML/non_tex/ReproducibilityChecklist.tex': 'conference checklist template',
    'CHARM/Ro-MAN 2024.tex': 'identical copy of Progress/Ro-MAN 2024.tex',
    'CHARM/paper_template.tex': 'identical copy of Progress/paper_template.tex',
    'CHARM/epitaph for my brain cells.tex': 'identical copy of Progress/epitaph for my brain cells.tex',
    'prospectus/sample-base.bib': 'ACM template bibliography',
    'prospectus/software.bib': 'ACM template bibliography',
    'PHIRL/legacy/sample-base.bib': 'ACM template bibliography',
    'PHIRL/legacy/software.bib': 'ACM template bibliography',
}

# Text macros defined in the papers.
TEXT_MACROS = {
    'thingname': 'demonstration sidetracks',
    'ThingName': 'Demonstration Sidetracks',
    'BibTeX': 'BibTeX',
}

# Commands whose arguments are removed with them: (number of {} arguments to drop).
DROP = {
    'cite': 1, 'citep': 1, 'citet': 1, 'citeauthor': 1, 'citeyear': 1, 'nocite': 1,
    'ref': 1, 'autoref': 1, 'eqref': 1, 'cref': 1, 'Cref': 1, 'pageref': 1, 'label': 1,
    'url': 1, 'includegraphics': 1, 'input': 1, 'include': 1, 'bibliography': 1,
    'bibliographystyle': 1, 'vspace': 1, 'hspace': 1, 'setlength': 2, 'addtolength': 2,
    'elaine': 1, 'rma': 1, 'jindan': 1, 'todo': 1, 'hang': 1, 'delete': 1,
    'thanks': 1, 'author': 1, 'affiliation': 1, 'email': 1, 'institution': 1,
    'icmlauthor': 2, 'icmlaffiliation': 2, 'icmlcorrespondingauthor': 2, 'icmlsetsymbol': 2,
    'icmlkeywords': 1, 'icmltitlerunning': 1, 'shortauthors': 0,
    'newcommand': 2, 'renewcommand': 2, 'definecolor': 3, 'color': 1, 'cellcolor': 1,
    'rowcolor': 1, 'captionsetup': 1, 'scalebox': 1, 'adjustbox': 1, 'fontsize': 2,
    'resizebox': 2, 'multicolumn': 2, 'multirow': 2, 'textcolor': 1, 'href': 1,
    'cline': 1, 'cmidrule': 1, 'usepackage': 1, 'documentclass': 1, 'pagestyle': 1,
    'thispagestyle': 1, 'setcounter': 2, 'addbibresource': 1, 'graphicspath': 1,
    'acmConference': 1, 'acmBooktitle': 1, 'acmDOI': 1, 'acmISBN': 1, 'acmYear': 1,
    'copyrightyear': 1, 'setcopyright': 1, 'ccsdesc': 1, 'keywords': 0, 'orcid': 1,
    'renewcommand*': 2, 'raisebox': 1, 'stepcounter': 1, 'addtocounter': 2,
    'linewidth': 0, 'textwidth': 0, 'columnwidth': 0, 'hline': 0, 'toprule': 0,
    'midrule': 0, 'bottomrule': 0, 'centering': 0, 'noindent': 0, 'maketitle': 0,
    'small': 0, 'footnotesize': 0, 'scriptsize': 0, 'tiny': 0, 'large': 0, 'Large': 0,
    'normalsize': 0, 'newline': 0, 'linebreak': 0, 'clearpage': 0, 'newpage': 0,
}
# Environments removed with their content.
DROP_ENVS = {'equation', 'equation*', 'align', 'align*', 'gather', 'gather*', 'multline',
             'multline*', 'eqnarray', 'eqnarray*', 'displaymath', 'math', 'tikzpicture',
             'thebibliography', 'filecontents', 'verbatim', 'lstlisting', 'CCSXML',
             'teaserfigure*'}
# Environments whose first {} argument is a specification, not text.
SPEC_ENVS = {'tabular', 'tabular*', 'tabularx', 'tblr', 'longtable', 'array', 'minipage',
             'subfigure', 'wrapfigure', 'adjustbox', 'multicols', 'tabu'}
# Commands that end a phrase: their content is kept and followed by a boundary.
HEADINGS = {'section', 'section*', 'subsection', 'subsection*', 'subsubsection',
            'subsubsection*', 'paragraph', 'paragraph*', 'title', 'caption', 'subcaption',
            'icmltitle', 'item', 'State', 'Require', 'Ensure', 'For', 'EndFor', 'If',
            'EndIf', 'Return', 'While', 'EndWhile', 'Else', 'Statex', 'Comment'}

BOUNDARY = ' \u00a7 '   # a phrase boundary that no word can cross


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def keep_lines(s):
    """A blank of the same number of lines as s."""
    return ' ' + '\n' * s.count('\n') + ' '


def strip_comments(text):
    out = []
    for line in text.split('\n'):
        m = re.search(r'(?<!\\)%', line)
        out.append(line[:m.start()] if m else line)
    return '\n'.join(out)


def body(text):
    """The document body; a file without \\begin{document} is a section file."""
    m = re.search(r'\\begin\{document\}', text)
    if m:
        head = text[:m.end()]
        text = keep_lines(head) + text[m.end():]
    m = re.search(r'\\end\{document\}', text)
    if m:
        text = text[:m.start()] + keep_lines(text[m.start():])
    return text


def remove_math(text):
    envs = '|'.join(re.escape(e) for e in sorted(DROP_ENVS, key=len, reverse=True))
    text = re.sub(r'\\begin\{(%s)\}.*?\\end\{\1\}' % envs,
                  lambda m: BOUNDARY + keep_lines(m.group(0)), text, flags=re.S)
    text = re.sub(r'\$\$.*?\$\$', lambda m: BOUNDARY + keep_lines(m.group(0)), text, flags=re.S)
    text = re.sub(r'\\\[.*?\\\]', lambda m: BOUNDARY + keep_lines(m.group(0)), text, flags=re.S)
    text = re.sub(r'\\\(.*?\\\)', lambda m: ' MATH ' + keep_lines(m.group(0)), text, flags=re.S)
    text = re.sub(r'(?<!\\)\$(?:\\\$|[^$])*?(?<!\\)\$', lambda m: ' MATH ' + keep_lines(m.group(0)),
                  text, flags=re.S)
    return text


def read_group(text, i, open_ch='{', close_ch='}'):
    """Return (content, end index) of a balanced group starting at text[i], or None."""
    if i >= len(text) or text[i] != open_ch:
        return None
    depth = 0
    j = i
    while j < len(text):
        c = text[j]
        if c == '\\':
            j += 2
            continue
        if c == open_ch:
            depth += 1
        elif c == close_ch:
            depth -= 1
            if depth == 0:
                return text[i + 1:j], j + 1
        j += 1
    return text[i + 1:], len(text)


def skip_space(text, i):
    while i < len(text) and text[i] in ' \t':
        i += 1
    return i


def macros(text):
    """Remove or unwrap LaTeX commands, keeping the line count."""
    out = []
    i = 0
    n = len(text)
    while i < n:
        c = text[i]
        if c != '\\':
            out.append(c)
            i += 1
            continue
        m = re.match(r'\\([A-Za-z]+\*?|.)', text[i:])
        name = m.group(1)
        j = i + m.end()
        if name in ('%', '&', '_', '#', '$'):
            out.append({'%': ' percent ', '&': ' and '}.get(name, ' '))
            i = j
            continue
        if name in ('\\',):
            out.append(BOUNDARY)
            i = j
            continue
        if not name[0].isalpha():
            out.append(' ')
            i = j
            continue
        if name in TEXT_MACROS:
            g = read_group(text, j)
            if g is not None and g[0] == '':
                j = g[1]
            out.append(TEXT_MACROS[name])
            i = j
            continue
        if name in ('begin', 'end'):
            g = read_group(text, j)
            if g is None:
                i = j
                continue
            env, j = g
            k = skip_space(text, j)
            while k < n and text[k] == '[':
                g2 = read_group(text, k, '[', ']')
                j = g2[1]
                k = skip_space(text, j)
            if name == 'begin' and env in SPEC_ENVS:
                for _ in range(2 if env in ('tabular*', 'tabularx') else 1):
                    k = skip_space(text, j)
                    g2 = read_group(text, k)
                    if g2 is not None:
                        out.append(keep_lines(g2[0]))
                        j = g2[1]
            out.append(BOUNDARY)
            i = j
            continue
        # optional arguments are dropped
        k = skip_space(text, j)
        while k < n and text[k] == '[':
            g = read_group(text, k, '[', ']')
            out.append(keep_lines(g[0]))
            j = g[1]
            k = skip_space(text, j)
        base = name.rstrip('*')
        if base in DROP:
            for _ in range(DROP[base]):
                k = skip_space(text, j)
                while k < n and text[k] == '[':
                    g = read_group(text, k, '[', ']')
                    out.append(keep_lines(g[0]))
                    j = g[1]
                    k = skip_space(text, j)
                g = read_group(text, k)
                if g is None:
                    break
                out.append(keep_lines(g[0]))
                j = g[1]
            if base in ('cite', 'citep', 'citet', 'ref', 'autoref', 'eqref', 'cref', 'Cref'):
                out.append(' ')
            elif DROP[base]:
                out.append(BOUNDARY if name not in ('textcolor', 'href', 'multicolumn',
                                                     'multirow', 'resizebox', 'color',
                                                     'cellcolor', 'rowcolor') else ' ')
            i = j
            continue
        # any other command: keep the text of its {} arguments
        if name in HEADINGS:
            out.append(BOUNDARY)
        i = j
        k = skip_space(text, j)
        g = read_group(text, k)
        if g is not None:
            # No padding, so that \textit{progress}-annotated stays one word.
            out.append(macros(g[0]))
            i = g[1]
            if name in HEADINGS:
                out.append(BOUNDARY)
        else:
            out.append(' ')
    return ''.join(out)


def clean(text):
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    text = body(text)
    text = strip_comments(text)
    text = remove_math(text)
    text = macros(text)
    for a, b in [('~', ' '), ('``', '"'), ("''", '"'), ('---', ' \u2014 '), ('--', '\u2013'),
                 ('{', ' '), ('}', ' '), ('&', BOUNDARY), ('\u2011', '-')]:
        text = text.replace(a, b)
    return text


def documents():
    """Yield (family, kind, relative path, cleaned text) for every corpus file."""
    for fam, files in CORPUS.items():
        for rel, kind in files:
            raw = (PAPERS / rel).read_text(encoding='utf-8', errors='replace')
            yield fam, kind, rel, clean(raw)


# ---------------------------------------------------------------------------
# Reference dissertations: not Hang's writing, but read by Hang as style references.
# Their words are counted apart from the papers and never raise a tier of Hang's own use.
#
# Two groups. The committee dissertations (Short, Vázquez, Bobu) are the ones Hang named as
# the committee's style. The lab dissertations are the most recent PhD dissertations from the
# labs of Matarić, Song, Li, Vázquez, and Scassellati that could be retrieved in November 2026
# (12 of 21 requested; see dissertation_reference/README.md). They show the vocabulary that
# current readers in robot learning and HRI know. Bobu's dissertation is in both collections
# and is counted once, as a committee dissertation.

REFERENCE_GROUPS = {
    'committee': 'Committee dissertations',
    'lab': 'Recent lab dissertations',
}
REFERENCES = {
    'Short': {'key': 'short', 'group': 'committee', 'pdf': 'dessertation_reference/Short_2017_USC_thesis.pdf',
              'title': 'Short (2017), Managing Multi-Party Social Dynamics for Socially Assistive Robotics',
              'pages': [(17, 18), (19, 189)]},
    'Vázquez': {'key': 'vazquez', 'group': 'committee', 'pdf': 'dessertation_reference/Vazquez_2017_CMU_thesis.pdf',
                'title': 'Vázquez (2017), Reasoning About Spatial Patterns of Human Behavior During Group Conversations with Robots',
                'pages': [(2, 2), (8, 97)]},
    'Bobu': {'key': 'bobu', 'group': 'committee', 'pdf': 'dessertation_reference/Bobu_2023_Berkeley_EECS-2023-200.pdf',
             'title': 'Bobu (2023), Aligning Robot Representations with Humans',
             'pages': [(5, 6), (15, 199)]},
    # Recent lab dissertations. 'pdf' is relative to LAB_DIR; 'lab' is the advisor's lab.
    'Klein': {'key': 'klein', 'group': 'lab', 'lab': 'Matarić',
              'pdf': 'Maja_Mataric/2023_Lauren_Klein_Modeling_Dyadic_Synchrony.pdf',
              'source': 'https://maja-mataric.web.app/about/people/alumni',
              'title': 'Klein (2023), Modeling Dyadic Synchrony with Heterogeneous Data: Validation in Infant-Mother and Infant-Robot Interactions',
              'pages': [(13, 15), (16, 113)]},
    'Birmingham': {'key': 'birmingham', 'group': 'lab', 'lab': 'Matarić',
                   'pdf': 'Maja_Mataric/2023_Chris_Birmingham_Multiparty_Human_Robot_Interaction.pdf',
                   'source': 'https://maja-mataric.web.app/about/people/alumni',
                   'title': 'Birmingham (2023), Multiparty Human-Robot Interaction: Methods for Facilitating Social Support',
                   'pages': [(11, 11), (12, 86)]},
    'Shi': {'key': 'shi', 'group': 'lab', 'lab': 'Song',
            'pdf': 'Shuran_Song/2026_Haochen_Shi_Bringing_Life_to_Robots.pdf',
            'source': 'https://purl.stanford.edu/yf485jt4430',
            'title': 'Shi (2026), Bringing Life to Robots',
            'pages': [(4, 4), (15, 71)]},
    'Sargent': {'key': 'sargent', 'group': 'lab', 'lab': 'Li',
                'pdf': 'Fei_Fei_Li/2026_Kyle_Sargent_Visual_Generation_and_Compression_for_World_Models.pdf',
                'source': 'https://purl.stanford.edu/hy838rm3130',
                'title': 'Sargent (2026), Visual Generation and Compression for World Models',
                'pages': [(17, 81)]},
    'Gokmen': {'key': 'gokmen', 'group': 'lab', 'lab': 'Li',
               'pdf': 'Fei_Fei_Li/2026_Cem_Gokmen_Building_Simulation_Worlds_for_Robot_Learning.pdf',
               'source': 'https://purl.stanford.edu/bm681rt0728',
               'title': 'Gokmen (2026), Building Simulation Worlds for Robot Learning',
               'pages': [(4, 4), (19, 66)]},
    'Wong': {'key': 'wong', 'group': 'lab', 'lab': 'Li',
             'pdf': 'Fei_Fei_Li/2026_Josiah_Wong_Scaling_Simulation_for_Accelerating_Robot_Learning.pdf',
             'source': 'https://purl.stanford.edu/ny792bn1132',
             'title': 'Wong (2026), Scaling Simulation for Accelerating Robot Learning',
             'pages': [(4, 4), (27, 98)]},
    'Candon': {'key': 'candon', 'group': 'lab', 'lab': 'Vázquez',
               'pdf': 'Marynel_Vazquez/2026_Kate_Candon_Robot_Learning_During_Collaborations_DRAFT.pdf',
               'source': 'https://kccandonk.github.io/dissertation/',
               'title': 'Candon (2026, draft), Robot Learning During Collaborations with Non-Expert Robot Users',
               'pages': [(1, 1), (17, 120)]},
    'Thompson': {'key': 'thompson', 'group': 'lab', 'lab': 'Vázquez',
                 'pdf': 'Marynel_Vazquez/2026_Sydney_Thompson_Modeling_Agent_Associations_DRAFT.pdf',
                 'source': 'https://www.sydneythompson.dev/p/dissertation.html',
                 'title': 'Thompson (2026, draft), Modeling Agent Associations in Human-Robot Interactions',
                 'pages': [(1, 1), (16, 120)]},
    'Tsoi': {'key': 'tsoi', 'group': 'lab', 'lab': 'Vázquez',
             'pdf': 'Marynel_Vazquez/2025_Nathan_Tsoi_Creating_Socially_Competent_Mobile_Robots.pdf',
             'source': 'https://elischolar.library.yale.edu/gsas_dissertations/1727/',
             'title': 'Tsoi (2025), Creating Socially Competent Mobile Robots: Rethinking How to Measure Success',
             'pages': [(1, 3), (18, 166)]},
    'Georgiou': {'key': 'georgiou', 'group': 'lab', 'lab': 'Scassellati',
                 'pdf': 'Brian_Scassellati/2026_Nicholas_Georgiou_Robot_Failures.pdf',
                 'source': 'https://scazlab.yale.edu/news/nicholas-georgiou-successfully-defends-thesis',
                 'title': 'Georgiou (2026), Investigating Human Perceptions and Responses to Robot Failures Across Functional, Social, and Moral Contexts in Human-Robot Interactions',
                 'pages': [(1, 2), (22, 135)]},
    'Ghose': {'key': 'ghose', 'group': 'lab', 'lab': 'Scassellati',
              'pdf': 'Brian_Scassellati/2026_Debasmita_Ghose_Robots_Adapting_to_People.pdf',
              'source': 'https://scazlab.yale.edu/news/debasmita-ghose-successfully-defends-thesis',
              'title': 'Ghose (2026), Robots Adapting to People Without Becoming a Nuisance',
              'pages': [(1, 2), (30, 231)]},
    'Matheus': {'key': 'matheus', 'group': 'lab', 'lab': 'Scassellati',
                'pdf': 'Brian_Scassellati/2026_Kayla_Matheus_Social_Robots_in_Mental_Health.pdf',
                'source': 'https://scazlab.yale.edu/news/kayla-matheus-successfully-defends-thesis',
                'title': 'Matheus (2026), Embodiment, Interactions, and Autonomy for Social Robots in Mental Health',
                'pages': [(1, 2), (29, 407)]},
}
COMMITTEE = [n for n, r in REFERENCES.items() if r['group'] == 'committee']
LAB = [n for n, r in REFERENCES.items() if r['group'] == 'lab']
REFERENCE_TEXT = HERE / 'sources' / 'reference-dissertations'
# The lab dissertations are not bundled with the plugin. Their PDFs and extracted text are kept in
# the repository's dissertation_reference/ folder (text/ holds the text), or in VOCAB_LAB_DISSERTATIONS.
LAB_DIR = Path(os.environ.get('VOCAB_LAB_DISSERTATIONS') or HERE.parents[4] / 'dissertation_reference')
LAB_TEXT = LAB_DIR / 'text'
LIGATURES = {'ﬀ': 'ff', 'ﬁ': 'fi', 'ﬂ': 'fl', 'ﬃ': 'ffi', 'ﬄ': 'ffl',
             '’': "'", '‘': "'", '“': '"', '”': '"', '­': ''}


# Text repairs applied when a PDF is extracted. Gokmen's PDF writes the ff, ffi, and ffl ligatures
# as !, ", and # (a!ordance, e"ciency, shu#ed); one word (a"ected) uses " for ff.
REPAIRS = {
    'Gokmen': [(r'a"ect', 'affect'), (r'(?<=[A-Za-z])!', 'ff'), (r'(?<=[A-Za-z])"(?=[A-Za-z])', 'ffi'),
               (r'(?<=[A-Za-z])#(?=[A-Za-z])', 'ffl')],
}


def repair_text(name, text):
    """The extracted text of a reference dissertation with its known extraction errors repaired."""
    for pattern, replacement in REPAIRS.get(name, []):
        text = re.sub(pattern, replacement, text)
    return text


def reference_link(name, page):
    """Link from writing_style_ref/ to a page of a reference dissertation's PDF."""
    ref = REFERENCES[name]
    base = '..' if ref['group'] == 'committee' else '../../../../../dissertation_reference'
    return f"{base}/{quote(ref['pdf'], safe='/')}#page={page}"


def ref_summary(counts):
    """Uses in the reference dissertations, in one short cell: each committee dissertation by name,
    then the lab dissertations together, with the number that use the term and the one that uses it most.
    For example "Short 3 · Bobu 40 · lab 212 in 9/12 (Tsoi 80)", or "lab: Klein 30" for one lab dissertation."""
    parts = [f'{n} {counts[n]}' for n in COMMITTEE if counts.get(n)]
    lab = {n: counts[n] for n in LAB if counts.get(n)}
    if len(lab) == 1:
        (n, c), = lab.items()
        parts.append(f'lab: {n} {c}')
    elif lab:
        top = max(lab, key=lambda n: (lab[n], -LAB.index(n)))
        parts.append(f'lab {sum(lab.values())} in {len(lab)}/{len(LAB)} ({top} {lab[top]})')
    return ' · '.join(parts)


def reference_text_path(name):
    ref = REFERENCES[name]
    return (REFERENCE_TEXT if ref['group'] == 'committee' else LAB_TEXT) / (ref['key'] + '.txt')


def reference_documents():
    """Yield (name, pdf path, cleaned text, page of each line) for each reference dissertation.

    Only the abstract and the body are kept: front matter, tables of contents, and the
    bibliography are dropped. Running heads and page numbers (short lines that repeat on
    many pages) are blanked, and a word hyphenated at a line break is joined again."""
    for name, ref in REFERENCES.items():
        raw = reference_text_path(name).read_text(encoding='utf-8')
        for a, b in LIGATURES.items():
            raw = raw.replace(a, b)
        lines, pages, page = [], [], 0
        keep = lambda p: any(lo <= p <= hi for lo, hi in ref['pages'])  # noqa: E731
        for line in raw.split('\n'):
            m = re.match(r'\[\[page (\d+)\]\]$', line)
            if m:
                page = int(m.group(1))
                lines.append('')
                pages.append(page)
                continue
            lines.append(line if keep(page) else '')
            pages.append(page)
        counts = {}
        for line in lines:
            s = line.strip()
            if s and len(s) <= 80:
                counts[s] = counts.get(s, 0) + 1
        for i, line in enumerate(lines):
            s = line.strip()
            if re.fullmatch(r'[0-9ivxlcdm]+', s, re.I) or (s and len(s) <= 80 and counts.get(s, 0) >= 4
                                                            and not re.search(r'[.?!]$', s)):
                lines[i] = ''
        seen = set(w.lower() for line in lines for w in WORD.findall(line))
        for i in range(len(lines) - 1):
            m = re.search(r'([A-Za-z]+)-$', lines[i])
            n = re.match(r'([a-z]+)', lines[i + 1])
            if m and n:
                left, right = m.group(1), n.group(1)
                joined = left + ('-' if (left + '-' + right).lower() in seen and (left + right).lower() not in seen else '') + right
                lines[i] = lines[i][:m.start()] + joined
                lines[i + 1] = lines[i + 1][n.end():]
        yield name, ref['pdf'], '\n'.join(lines), pages


BIB_TITLE = re.compile(r'^\s*title\s*=\s*', re.I | re.M)


def bib_titles():
    """Yield (family, relative path, line, title) for every cited title, each title once per family."""
    seen = set()
    for fam, files in BIBS.items():
        for rel in files:
            raw = (PAPERS / rel).read_text(encoding='utf-8', errors='replace').replace('\r\n', '\n')
            for m in BIB_TITLE.finditer(raw):
                j = m.end()
                if j < len(raw) and raw[j] == '{':
                    g = read_group(raw, j)
                    title = g[0] if g else ''
                elif j < len(raw) and raw[j] == '"':
                    k = raw.find('"', j + 1)
                    title = raw[j + 1:k]
                else:
                    continue
                # Expand macros before dropping braces, so that \href{url}{text} keeps only the text.
                t = macros(title).replace('{', '').replace('}', '')
                t = re.sub(r'\S*://\S*', ' ', t)
                t = re.sub(r'\s+', ' ', t).strip()
                key = (fam, t.lower())
                if t and key not in seen:
                    seen.add(key)
                    yield fam, rel, raw.count('\n', 0, m.start()) + 1, t


WORD = re.compile(r"[A-Za-z][A-Za-z0-9]*(?:[-'\u2019][A-Za-z0-9]+)*")


def words(text):
    """Words of a cleaned line; possessive 's is removed."""
    out = []
    for m in WORD.finditer(text):
        w = re.sub(r"['\u2019]s$", '', m.group(0))
        w = w.replace('\u2019', "'")
        if w and w != 'MATH':
            out.append(w)
    return out


# ---------------------------------------------------------------------------
# Word forms shared by build_vocabulary.py and check_vocabulary.py

STOPWORDS = set("""a an the and or but nor so yet for of to in on at by with from into onto upon over
under about above below between among through during before after since until while within without
across along around behind beyond toward towards against via per than as if then else when where
which who whom whose what why how that this these those there here it its they them their theirs
we our ours us i me my you your he she his her him is are was were be been being am do does did
done doing have has had having can could may might must shall should will would not no also only
just even very more most much many some any each every all both either neither such same other
another one two three four five six seven eight nine ten first second third less least few several
own however therefore thus hence moreover furthermore although though because whether e.g i.e et
al etc vs""".split())


def is_acronym(w):
    """LfD, IRL, VLM, Gen3, Lift-PH: a part with two capitals, or with a capital and a digit.
    Title Case compounds such as Human-in-the-Loop are not acronyms."""
    return any(sum(c.isupper() for c in p) >= 2 or (p[:1].isupper() and any(c.isdigit() for c in p))
               for p in w.split('-'))


def norm(w):
    return w if is_acronym(w) else w.lower()


def lemma_candidates(w):
    """Base forms to try for an inflected word, most likely first."""
    if is_acronym(w):
        return [w[:-1]] if w.endswith('s') and len(w) > 2 else []
    if '-' in w:
        head, _, last = w.rpartition('-')
        return [head + '-' + c for c in lemma_candidates(last)] if last else []
    special = {'analyses': 'analysis', 'criteria': 'criterion', 'hypotheses': 'hypothesis'}
    if w in special:
        return [special[w]]
    c = []
    if w.endswith('ies') and len(w) > 4:
        c.append(w[:-3] + 'y')
    if w.endswith('es') and len(w) > 3:
        c += [w[:-2], w[:-1]]
    if w.endswith('s') and not w.endswith(('ss', 'us', 'is', 'ics')) and len(w) > 3:
        c.append(w[:-1])
    if w.endswith('ing') and len(w) > 5:
        c += [w[:-3], w[:-3] + 'e']
        if w[-4] == w[-5]:
            c.append(w[:-4])
    if w.endswith('ied') and len(w) > 4:
        c.append(w[:-3] + 'y')
    if w.endswith('ed') and len(w) > 4:
        c += [w[:-2], w[:-1]]
        if w[-3] == w[-4]:
            c.append(w[:-3])
    return [x for x in c if x and x != w]


def lemma(w, known):
    """The base form of w that occurs in the set `known`, or w itself."""
    w = norm(w)
    for c in lemma_candidates(w):
        if c in known:
            return c
    return w


def _cons(w, i):
    if w[i] in 'aeiou':
        return False
    if w[i] == 'y':
        return i == 0 or not _cons(w, i - 1)
    return True


def _m(s):
    n, i, L = 0, 0, len(s)
    while i < L and _cons(s, i):
        i += 1
    while i < L:
        while i < L and not _cons(s, i):
            i += 1
        if i >= L:
            break
        while i < L and _cons(s, i):
            i += 1
        n += 1
    return n


def _vowel_in(s):
    return any(not _cons(s, i) for i in range(len(s)))


def _double(s):
    return len(s) >= 2 and s[-1] == s[-2] and _cons(s, len(s) - 1)


def _cvc(s):
    return (len(s) >= 3 and _cons(s, len(s) - 3) and not _cons(s, len(s) - 2)
            and _cons(s, len(s) - 1) and s[-1] not in 'wxy')


def stem(w):
    """Porter (1980) stem, used to group a word with its derived forms (annotate, annotator)."""
    w = w.lower()
    if not w.isalpha() or len(w) <= 2:
        return w
    if w.endswith('sses') or w.endswith('ies'):
        w = w[:-2]
    elif w.endswith('s') and not w.endswith('ss'):
        w = w[:-1]
    flag = False
    if w.endswith('eed'):
        if _m(w[:-3]) > 0:
            w = w[:-1]
    elif w.endswith('ed') and _vowel_in(w[:-2]):
        w, flag = w[:-2], True
    elif w.endswith('ing') and _vowel_in(w[:-3]):
        w, flag = w[:-3], True
    if flag:
        if w.endswith(('at', 'bl', 'iz')):
            w += 'e'
        elif _double(w) and w[-1] not in 'lsz':
            w = w[:-1]
        elif _m(w) == 1 and _cvc(w):
            w += 'e'
    if w.endswith('y') and _vowel_in(w[:-1]):
        w = w[:-1] + 'i'
    for suf, rep in [('ational', 'ate'), ('tional', 'tion'), ('enci', 'ence'), ('anci', 'ance'),
                     ('izer', 'ize'), ('abli', 'able'), ('alli', 'al'), ('entli', 'ent'),
                     ('eli', 'e'), ('ousli', 'ous'), ('ization', 'ize'), ('ation', 'ate'),
                     ('ator', 'ate'), ('alism', 'al'), ('iveness', 'ive'), ('fulness', 'ful'),
                     ('ousness', 'ous'), ('aliti', 'al'), ('iviti', 'ive'), ('biliti', 'ble')]:
        if w.endswith(suf):
            if _m(w[:-len(suf)]) > 0:
                w = w[:-len(suf)] + rep
            break
    for suf, rep in [('icate', 'ic'), ('ative', ''), ('alize', 'al'), ('iciti', 'ic'),
                     ('ical', 'ic'), ('ful', ''), ('ness', '')]:
        if w.endswith(suf):
            if _m(w[:-len(suf)]) > 0:
                w = w[:-len(suf)] + rep
            break
    for suf in ['ement', 'ance', 'ence', 'able', 'ible', 'ment', 'ant', 'ent', 'ion', 'ism',
                'ate', 'iti', 'ous', 'ive', 'ize', 'al', 'er', 'ic', 'ou']:
        if w.endswith(suf):
            s = w[:-len(suf)]
            if _m(s) > 1 and (suf != 'ion' or s.endswith(('s', 't'))):
                w = s
            break
    if w.endswith('e'):
        s = w[:-1]
        if _m(s) > 1 or (_m(s) == 1 and not _cvc(s)):
            w = s
    if _m(w) > 1 and _double(w) and w.endswith('l'):
        w = w[:-1]
    return w


def inflect(w, verb):
    """Forms of the last word of a term that count as the same term."""
    if is_acronym(w):
        return {w, w + 's'}
    out = {w}
    lw = w.lower()
    if verb:
        if lw.endswith('e'):
            out |= {w + 's', w + 'd', w[:-1] + 'ing'}
        elif lw.endswith('y') and lw[-2:-1] not in ('a', 'e', 'i', 'o', 'u'):
            out |= {w[:-1] + 'ies', w[:-1] + 'ied', w + 'ing'}
        else:
            out |= {w + 's', w + 'es', w + 'ed', w + 'ing'}
            if _cvc(lw):
                out |= {w + w[-1] + 'ed', w + w[-1] + 'ing'}
    else:
        if lw.endswith('y') and lw[-2:-1] not in ('a', 'e', 'i', 'o', 'u'):
            out.add(w[:-1] + 'ies')
        elif lw.endswith('is'):
            out.add(w[:-2] + 'es')
        elif lw.endswith(('s', 'x', 'ch', 'sh')):
            out.add(w + 'es')
        else:
            out.add(w + 's')
    return out


def parse_term(entry):
    """'display | other ~v' -> (display, [spellings], flags)."""
    flags = ''
    m = re.search(r'\s~([a-z]+)\s*$', entry)
    if m:
        flags, entry = m.group(1), entry[:m.start()]
    forms = [f.strip() for f in entry.split('|') if f.strip()]
    return forms[0], forms, flags


def term_regex(forms, flags):
    alts = []
    case_sensitive = 'c' in flags
    for form in forms:
        ws = form.split()
        if any(is_acronym(w) for w in ws):
            case_sensitive = True
        parts = []
        for i, w in enumerate(ws):
            variants = {w}
            if i == len(ws) - 1 and 'x' not in flags:
                variants = inflect(w, 'v' in flags)
            esc = sorted((re.escape(v).replace('\\-', '[-\\s]?') for v in variants), key=len, reverse=True)
            parts.append('(?:' + '|'.join(esc) + ')')
        alts.append(r'[-\s]+'.join(parts))
    pat = r'(?<![A-Za-z0-9\-])(?:' + '|'.join(alts) + r')(?![A-Za-z0-9])'
    return re.compile(pat, 0 if case_sensitive else re.I)


GENERAL = HERE / 'sources' / 'general-english-zipf.tsv'


def general_english():
    """word -> Zipf frequency in general English (wordfreq snapshot), or {} if the snapshot is missing."""
    if not GENERAL.exists():
        return {}
    out = {}
    for line in GENERAL.read_text(encoding='utf-8').splitlines():
        if line and not line.startswith('#'):
            w, z = line.split('\t')
            out[w] = float(z)
    return out
