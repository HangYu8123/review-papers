"""Build the committee writing style reference from authored_entries.py.

Run from the dissertation folder:

    python committee_style_ref/tools/build_reference.py

It writes committee-writing-style-reference.md, source-evidence.md,
writer-profiles.md, and library.json. It stops if a quotation is not found on
its page, if a measure named in the guidance does not exist, or if a pattern of
Hang's reference that an entry points to does not exist.
"""
import datetime
import json
import re
import runpy
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as C

HERE = C.HERE
AUTHORED = runpy.run_path(str(HERE / 'tools' / 'authored_entries.py'))
ENTRIES = AUTHORED['ENTRIES']
BRIEF = AUTHORED['BRIEF']
CATEGORIES = ['Vocabulary', 'Wording preference', 'Writing style', 'Sentence style',
              'Sentence structure', 'Storytelling style']
MAIN = 'committee-writing-style-reference.md'
EVIDENCE = 'source-evidence.md'
PROFILES = 'writer-profiles.md'
HANG_REF = '../writing_style_ref/hangs-writing-style-reference.md'
RELATION = {
    'same': "Hang's reference says the same",
    'adds': "Adds to Hang's reference",
    'differs': "Differs from Hang's preference, which takes priority",
}
PLACEHOLDER = re.compile(r'\{(\w+)\.(\w+)\}')


def slug(s):
    # The anchor that GitHub and VS Code give a heading.
    return re.sub(r'[^\w\- ]', '', s.lower()).replace(' ', '-')


def write(name, text):
    with open(str(HERE / name), 'w', encoding='utf-8', newline='\n') as f:
        f.write(text.rstrip() + '\n')


def number(v):
    if isinstance(v, float):
        return '%.1f' % v
    return '{:,}'.format(v) if isinstance(v, int) else str(v)


def nice_date(iso):
    d = datetime.datetime.strptime(iso, '%Y-%m-%d')
    return '%s %d, %d' % (d.strftime('%B'), d.day, d.year)


def listed(items):
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return items[0] + ' and ' + items[1]
    return ', '.join(items[:-1]) + ', and ' + items[-1]


def names(keys):
    return listed([C.SOURCES[k]['author'] for k in C.ORDER if k in keys])


def closest(name):
    # The writer or writers whose value for a measure is nearest to the draft's.
    gap = {k: abs(METRICS[k][name] - METRICS['draft'][name]) for k in C.ORDER}
    best = min(gap.values())
    return names([k for k in C.ORDER if gap[k] - best < 0.05])


def load_metrics():
    metrics = {k: C.measure(C.prose(k)) for k in C.ORDER}
    draft = HERE / 'sources' / 'draft-profile.json'
    if not draft.exists():
        sys.exit('sources/draft-profile.json is missing. Run tools/profile_draft.py first.')
    metrics['draft'] = json.loads(draft.read_text(encoding='utf-8'))
    return metrics


METRICS = load_metrics()
ERRORS = []


def fill(text):
    def repl(m):
        who, name = m.group(1), m.group(2)
        if who not in METRICS or name not in METRICS[who]:
            ERRORS.append('Unknown measure {%s.%s}' % (who, name))
            return m.group(0)
        return number(METRICS[who][name])
    return PLACEHOLDER.sub(repl, text)


def hang_headings():
    text = (HERE / HANG_REF).resolve().read_text(encoding='utf-8')
    return {slug(h) for h in re.findall(r'^#{2,3} (.+)$', text, flags=re.M)}


def prepare():
    headings = hang_headings()
    seen = set()
    for e in ENTRIES:
        if e['category'] not in CATEGORIES:
            ERRORS.append('Unknown category: ' + e['title'])
        if e['relation'] not in RELATION:
            ERRORS.append('Unknown relation: ' + e['title'])
        if e['title'] in seen:
            ERRORS.append('Duplicate title: ' + e['title'])
        seen.add(e['title'])
        if e['relation'] != 'same' and e['title'] not in BRIEF:
            ERRORS.append('No line in BRIEF for: ' + e['title'])
        e['slug'] = slug(e['title'])
        e['guidance_text'] = fill(e['guidance'])
        e['fit_text'] = fill(e['fit'])
        for h in e['hang']:
            if slug(h) not in headings:
                ERRORS.append("Not a pattern of Hang's reference: %s (in %s)" % (h, e['title']))
        for k in e['who']:
            if not any(x['key'] == k for x in e['quotes']):
                ERRORS.append('No quotation from %s: %s' % (k, e['title']))
        for x in e['quotes']:
            if x['key'] not in e['who']:
                ERRORS.append('Quotation from a writer not listed in who: ' + e['title'])
            x['match'] = C.find_quote(x['key'], x['page'], x['text'])
            if not x['match']:
                ERRORS.append('Quotation not found: %s, %s page %d, found on %s: %s' % (
                    e['title'], x['key'], x['page'], C.locate(x['key'], x['text']) or 'no page', x['text'][:60]))
            x['cite'] = C.cite(x['key'], x['page'])
    for title in BRIEF:
        if title not in seen:
            ERRORS.append('BRIEF names a pattern that does not exist: ' + title)
    if ERRORS:
        sys.exit('\n'.join(['Build stopped.'] + ERRORS))


def quote_block(x, base):
    text = x['text'].replace('[...]', '[…]')
    return ['> ' + text, '>', '> — [%s](%s)' % (x['cite'], C.pdf_link(x['key'], x['page'], base)), '']


def entry_lines(e):
    out = ['### ' + e['title'], '',
           '*Seen in %s. %s.*' % (names(e['who']), RELATION[e['relation']]), '',
           e['guidance_text'], '', '**Reusable forms**', '']
    out += ['- ' + f for f in e['forms']]
    related = listed(['[%s](%s#%s)' % (h, HANG_REF, slug(h)) for h in e['hang']])
    out += ['', "**In Hang's dissertation.** %s" % e['fit_text'], '',
            ("The related pattern in Hang's reference is %s." if len(e['hang']) == 1
             else "Related patterns in Hang's reference are %s.") % related, '',
            '**Examples**', '']
    shown = []
    for k in C.ORDER:
        first = [x for x in e['quotes'] if x['key'] == k][:1]
        shown += first
    for x in shown:
        out += quote_block(x, '..')
    out += ['[All %d source examples for this pattern](%s#%s).' % (len(e['quotes']), EVIDENCE, e['slug']), '']
    return out


def link(e):
    return '[%s](#%s)' % (e['title'], e['slug'])


def profile_table(rows):
    out = ["| Measure | Short | Vázquez | Bobu | Hang's draft |", '| --- | --- | --- | --- | --- |']
    for label, name in rows:
        cells = [number(METRICS[k][name]) for k in C.ORDER + ['draft']]
        out.append('| %s | %s |' % (label, ' | '.join(cells)))
    return out


def openers(k, n=4):
    return ', '.join('%s (%d)' % (o, c) for o, c in METRICS[k]['top_openers'][:n])


def by_title(title):
    return [e for e in ENTRIES if e['title'] == title][0]


def main_file():
    m = METRICS
    draft = m['draft']
    counts = {r: [e for e in ENTRIES if e['relation'] == r] for r in RELATION}
    n_quotes = sum(len(e['quotes']) for e in ENTRIES)
    L = ['# Committee writing style reference', '',
         "This reference describes how three dissertations are written. They are by Elaine Schaertl Short (University of Southern California, 2017), Marynel Vázquez (Carnegie Mellon University, 2017), and Andreea Bobu (University of California, Berkeley, 2023). Hang named them as the sources for the committee writing style, and Short is Hang's adviser. The reference shows what these readers did in their own dissertations, which is a guide to what they will find familiar in one.", '',
         "Use it together with [Hang's writing style reference](%s). Hang's reference says how Hang writes. This one says what the three did, where they agree with one another, and where they differ. When the two references differ, Hang's instructions and Hang's reference take priority. Each pattern has a line on how it relates to Hang's dissertation." % HANG_REF, '',
         'A dissertation shows how its author wrote at that time, with that adviser and those coauthors. It does not state what the author asks of a student now. The patterns are observations, and the forms are reusable wording. Square brackets mark slots to fill. Quotations keep the source wording, including first person, spelling, and punctuation. They are evidence of a pattern and not text to copy.', '',
         'The reference has %d patterns and %d quotations, each checked against its page. Page numbers are the printed page, followed by the page of the PDF file.' % (len(ENTRIES), n_quotes), '',
         '## Quick reference', '',
         'These are the practices that all three share.', '',
         '1. State the thesis in one sentence and repeat that sentence in the abstract, the introduction, and the conclusion.',
         '2. Name the gap precisely. Say what prior work covers, what it leaves out, and why.',
         '3. Show a problem in a short scene before stating it in general terms.',
         '4. Open each chapter with what it presents and what was found, and say how it follows from the chapter before.',
         '5. Report every study in the same order, with questions or hypotheses first and the verdict attached to the result that decides it.',
         '6. Give a result with its values and its test in one sentence, and keep the interpretation in a hedged clause after it.',
         '7. Report a difference that was not found as not found. Do not call the conditions equal.',
         '8. Offer explanations for an unexpected result as possibilities.',
         '9. Grade the strength of evidence in words, such as preliminary, limited, some support, and a trend, with the value beside the word.',
         '10. State limitations plainly and tie each one to the design of the study.',
         '11. Derive future work from the scope and limits of the dissertation, with a modal that shows how firm the plan is.',
         '12. Define each term in a full sentence when it first matters, and say what is outside the scope.',
         '13. End each chapter with what it showed and what that provides for the next one.',
         '14. Keep the final chapter short, and close on what the work is for.', '',
         '## Find a pattern', '']
    L += ['- [%s](#%s)' % (c, slug(c)) for c in CATEGORIES]
    L += ['', '[The three writers at a glance](#the-three-writers-at-a-glance) · [Where the three agree](#where-the-three-agree) · [Where they differ](#where-they-differ) · [Compared with Hang\'s reference](#compared-with-hangs-reference)', '',
          '[All source examples](%s) · [Full measures for each writer](%s)' % (EVIDENCE, PROFILES), '',
          '## The three writers at a glance', '',
          "The measures come from the running prose of the numbered chapters, as extracted from the PDF files. Rates are per 1,000 words. The last column is Hang's draft as compiled in main.pdf on %s, measured the same way. All values are approximate, and [writer-profiles.md](%s) says how they were counted." % (nice_date(draft['date']), PROFILES), '']
    L += profile_table([
        ('Words measured', 'words'),
        ('Mean words per sentence', 'sent_mean'),
        ('Median words per sentence', 'sent_median'),
        ('Sentences of 35 words or more (%)', 'long_share'),
        ('We, our, us', 'we'),
        ('Colons', 'colon'),
        ('Semicolons', 'semicolon'),
        ('Question marks', 'question'),
        ('Contractions', 'contraction'),
        ('Suggest and its forms', 'suggest'),
        ('May', 'may'),
        ('Might', 'might'),
        ('Could', 'could'),
    ])
    L += ['',
          '**Short (adviser).** Formal, and impersonal in the parts that frame the work. Sentences are the longest of the three and often carry a result with its condition and its interpretation. Each contribution moves through the same verbs, which are formalized, developed, instantiated, and validated. A chapter opens with a short abstract and ends with a Summary. Claims are graded with words such as some support, limited evidence, and preliminary. The dissertation closes on an ethical concern of the field. Most frequent sentence openers are %s.' % openers('short'), '',
          '**Vázquez.** Direct and orderly, with we throughout. Sentences are the shortest of the three, and colons and semicolons are the rarest. General statements are followed by For example, and reasons and limits are counted with First, Second, and Third. Discussion paragraphs open with a lead sentence that states the point. The goal of the dissertation is set apart in one sentence, and the scope is stated early. Most frequent sentence openers are %s.' % openers('vazquez'), '',
          '**Bobu.** Argumentative and vivid, with we throughout and I in the final chapter. One household example runs through most chapters. The approach is set against the usual one with rather than, instead, and by contrast. Evaluative words are stronger, and the register is at times conversational. Limits are stated at length, and each chapter says where it was published and with whom. Most frequent sentence openers are %s.' % openers('bobu'), '',
          "**Hang's draft.** In mean sentence length the draft is closest to %s, in colons to %s, and in semicolons to %s. It uses first person less than any of the three. Its structure, with an overview, contributions, an outline, and a Summary at the end of each chapter, is closest to Short's. Most frequent sentence openers are %s." % (closest('sent_mean'), closest('colon'), closest('semicolon'), openers('draft')), '',
          '## Where the three agree', '',
          '- A chapter is the subject of presents, introduces, describes, and reviews. See %s.' % link(by_title('Verbs for what a chapter does')),
          '- Terms are defined in a full sentence, and the scope is stated. See %s and %s.' % (link(by_title('Definitions in a full sentence')), link(by_title('Scope statements'))),
          '- Hypotheses are numbered, and the verdict is attached to the result that decides it. See %s.' % link(by_title('Hypotheses and verdicts')),
          '- A result is stated firmly, and its interpretation is hedged. A null result is reported as not found. See %s and %s.' % (link(by_title('A result with the clause that interprets it')), link(by_title('A difference that was not found'))),
          '- An unexpected result gets possible explanations. See %s.' % link(by_title('Possible explanations')),
          '- Limitations are plain and tied to the design. See %s.' % link(by_title('Limitations stated plainly')),
          '- Future work comes from the scope and limits of the dissertation. See %s.' % link(by_title('Future work from scope and limits')),
          '- Each chapter says where it was published and who contributed. See %s.' % link(by_title('Where the work was published and who did it')),
          '- The introduction has one figure of the whole approach. See %s.' % link(by_title('Pointing to figures, sections, and chapters')),
          '- The final chapter is three to four pages. See %s.' % link(by_title('The final chapter')), '',
          '## Where they differ', '',
          '- **First person.** We, our, and us appear %s, %s, and %s times per 1,000 words in Short, Vázquez, and Bobu. See %s.' % (number(m['short']['we']), number(m['vazquez']['we']), number(m['bobu']['we']), link(by_title('First person and the impersonal voice'))),
          '- **Sentence length.** The mean is %s, %s, and %s words. See %s.' % (number(m['short']['sent_mean']), number(m['vazquez']['sent_mean']), number(m['bobu']['sent_mean']), link(by_title('Sentence length'))),
          '- **Colons and semicolons.** Colons appear %s, %s, and %s times per 1,000 words, and semicolons %s, %s, and %s times. See %s.' % (number(m['short']['colon']), number(m['vazquez']['colon']), number(m['bobu']['colon']), number(m['short']['semicolon']), number(m['vazquez']['semicolon']), number(m['bobu']['semicolon']), link(by_title('Colons and semicolons'))),
          '- **Evaluative words and register.** Short is restrained, and Bobu is vivid and at times conversational. See %s and %s.' % (link(by_title('Evaluative and emphatic words')), link(by_title('Register'))),
          '- **Where related work sits.** Short has one background chapter, Vázquez adds short sections before each experiment, and Bobu has a section in each chapter. See %s.' % link(by_title('Related work that ends on this work')),
          '- **How a chapter ends.** Short ends a chapter with a Summary, and Bobu ends a chapter with a Discussion. See %s.' % link(by_title('Chapter endings')),
          '- **Where contributions are listed.** Short and Vázquez list them for the whole dissertation, and Bobu lists them in each chapter. See %s.' % link(by_title('Contribution statements')), '',
          "## Compared with Hang's reference", '',
          "Of the %d patterns, %d say the same as Hang's reference, %d add something it does not cover, and %d differ from Hang's preference. Where they differ, Hang's preference takes priority." % (len(ENTRIES), len(counts['same']), len(counts['adds']), len(counts['differs'])), '',
          "**Differs from Hang's preference**", '']
    L += ['- %s. %s' % (link(e), BRIEF[e['title']]) for e in counts['differs']]
    L += ['', "**Adds to Hang's reference**", '']
    L += ['- %s. %s' % (link(e), BRIEF[e['title']]) for e in counts['adds']]
    L += ['', "**Says the same as Hang's reference**", '',
          ', '.join(link(e) for e in counts['same']) + '.', '']
    for c in CATEGORIES:
        L += ['## ' + c, '']
        for e in ENTRIES:
            if e['category'] == c:
                L += entry_lines(e)
    L += ['## Scope of this reference', '',
          'The sources are three dissertations. The abstract, the introduction, and the final chapter of each were read closely, together with the openings, results, discussions, and summaries of selected chapters. The remaining text was searched for the patterns found there. A pattern marked as seen in a writer has at least one checked quotation from that writer, and a writer who is not named may still use the pattern in a part that was not read.', '',
          'Chapters of all three dissertations were first published as papers with coauthors. The patterns describe the dissertations and do not attribute each sentence to its named author. The measures are counts on text extracted from the PDF files, with figures, tables, equations, and reference lists left out as far as the extraction allows. They show differences of degree and are not targets.', '',
          "The lines headed In Hang's dissertation are readings made when this reference was prepared, on %s, from Hang's reference and from the dissertation files of that day. They are not Hang's decisions, and a later instruction from Hang replaces them. This reference changes no dissertation text." % nice_date(draft['date']), '']
    return '\n'.join(L)


def evidence_file():
    L = ['# Source evidence for the committee writing style reference', '',
         'Examples are grouped under the same patterns as the [main reference](%s). Each quotation was checked against the text of its page. Page numbers are the printed page, followed by the page of the PDF file, and each link opens the PDF at that page. […] marks an omission inside a quotation.' % MAIN, '',
         'Quotations keep the source wording, including first person, spelling, and punctuation. A few quotations are the part of a sentence that shows the pattern, and these begin without a capital or end without a period. Citation numbers in square brackets belong to the source.', '']
    for c in CATEGORIES:
        for e in ENTRIES:
            if e['category'] != c:
                continue
            L += ['## ' + e['title'], '', '%s · [Guidance](%s#%s)' % (c, MAIN, e['slug']), '']
            for k in C.ORDER:
                for x in e['quotes']:
                    if x['key'] == k:
                        L += quote_block(x, '..')
    return '\n'.join(L)


def profiles_file():
    draft = METRICS['draft']
    rows = [('Paragraphs measured', 'paragraphs'), ('Words measured', 'words'), ('Sentences measured', 'sentences'),
            ('Mean words per sentence', 'sent_mean'), ('Median words per sentence', 'sent_median'),
            ('Sentences of 12 words or fewer (%)', 'short_share'), ('Sentences of 35 words or more (%)', 'long_share'),
            ('We, our, us', 'we'), ('Colons', 'colon'), ('Semicolons', 'semicolon'), ('Question marks', 'question'),
            ('Contractions', 'contraction'), ('Suggest and its forms', 'suggest'), ('May', 'may'), ('Might', 'might'),
            ('Could', 'could'), ('Can', 'can'), ('Likely', 'likely'), ('Tend and its forms', 'tend'),
            ('Enable and its forms', 'enable'), ('Leverage and its forms', 'leverage'),
            ('This dissertation (count)', 'n_this_dissertation'), ('This thesis (count)', 'n_this_thesis'),
            ('This work (count)', 'n_this_work'), ('This chapter (count)', 'n_this_chapter')]
    L = ['# Measures for each writer', '',
         'These are the measures that the [main reference](%s) cites. Rates are per 1,000 words unless a row says count or percent.' % MAIN, '']
    L += profile_table(rows)
    L += ['', '## Sentence openers', '',
          'The number of sentences that begin with the word or phrase followed by a comma.', '',
          "| Opener | Short | Vázquez | Bobu | Hang's draft |", '| --- | --- | --- | --- | --- |']
    for o in C.OPENERS:
        key = C.opener_key(o)
        L.append('| %s | %s |' % (o, ' | '.join(str(METRICS[k][key]) for k in C.ORDER + ['draft'])))
    L += ['', '## How the measures were counted', '',
          'The text of each PDF was extracted with pdftotext, one block for each page. Only the numbered chapters were measured, which are PDF pages %s for Short, %s for Vázquez, and %s for Bobu. Running heads and page numbers were removed. A line counts as prose when it has at least 20 words, which leaves out headings, captions that are short, table cells, and most equations. Lines with symbols that the extraction could not read were left out, and this removes much of the mathematics in Bobu.' % tuple('%d to %d' % C.SOURCES[k]['body'] for k in C.ORDER), '',
          'Sentences were split at a period, question mark, or exclamation mark that is followed by a capital letter, after common abbreviations such as e.g., i.e., et al., Fig., and Sec. were protected. Sentences of fewer than three words were dropped. A colon between two digits was not counted. Contractions include those inside quoted speech of participants.', '',
          "Hang's draft was measured from main.pdf as compiled on %s, pages %d to %d, after %d review markers were removed from the text. The snapshot is in [sources/draft-profile.json](sources/draft-profile.json). Run `python committee_style_ref/tools/profile_draft.py` and then the build to refresh it." % (nice_date(draft['date']), draft['body'][0], draft['body'][1], draft['review_markers_removed']), '',
          'Short cites with author and year in parentheses, and Vázquez and Bobu cite with numbers in square brackets. Citations are part of the measured text, so Short\'s sentences are slightly longer for that reason alone. The measures are approximate and are meant for comparison between the writers.', '']
    return '\n'.join(L)


def library():
    return dict(
        title='Committee writing style reference',
        sources={k: {f: C.SOURCES[k][f] for f in ('full', 'year', 'title', 'school', 'pdf')} for k in C.ORDER},
        measures={k: METRICS[k] for k in C.ORDER + ['draft']},
        patterns=[dict(category=e['category'], title=e['title'], slug=e['slug'], seen_in=e['who'],
                       relation=e['relation'], guidance=e['guidance_text'], forms=e['forms'],
                       in_hangs_dissertation=e['fit_text'], related_in_hangs_reference=e['hang'],
                       examples=[dict(writer=x['key'], pdf_page=x['page'],
                                      printed_page=C.printed_page(x['key'], x['page']),
                                      text=x['text'], match=x['match']) for x in e['quotes']])
                  for e in ENTRIES])


def main():
    prepare()
    write(MAIN, main_file())
    write(EVIDENCE, evidence_file())
    write(PROFILES, profiles_file())
    write('library.json', json.dumps(library(), indent=2, ensure_ascii=False))
    n_quotes = sum(len(e['quotes']) for e in ENTRIES)
    print('%d patterns, %d quotations' % (len(ENTRIES), n_quotes))


if __name__ == '__main__':
    main()
