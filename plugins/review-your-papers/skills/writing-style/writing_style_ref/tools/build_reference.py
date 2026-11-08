"""Build local Markdown and JSON from the authored guide, the source snapshots, the imported
review decisions, Hang's instructions, and Hang's hand edits."""

from collections import Counter
import json
from pathlib import Path
import re
import runpy
from urllib.parse import quote

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parent
AUTHORED = runpy.run_path(str(HERE / 'tools' / 'authored_entries.py'))
ENTRIES = AUTHORED['ENTRIES']
REVIEW_CHECKS = AUTHORED['REVIEW_CHECKS']
HAND_CHECKS = AUTHORED['HAND_CHECKS']
QUICK_REFERENCE = AUTHORED['QUICK_REFERENCE']
UNCITED = AUTHORED['UNCITED']
PENDING_REVIEWS = AUTHORED['PENDING_REVIEWS']
UPDATE_SUMMARY = AUTHORED['UPDATE_SUMMARY']
SOURCE_ENTRIES = json.loads((HERE / 'sources' / 'source-entries.json').read_text(encoding='utf-8'))
REVIEWS = json.loads((HERE / 'sources' / 'review-decisions.json').read_text(encoding='utf-8'))['reviews']
INSTRUCTIONS = json.loads((HERE / 'sources' / 'hang-instructions.json').read_text(encoding='utf-8'))['instructions']
HAND_EDITS = json.loads((HERE / 'sources' / 'hand-edits.json').read_text(encoding='utf-8'))['edits']
CATEGORIES = ['Vocabulary', 'Wording preference', 'Writing style', 'Sentence style',
              'Sentence structure', 'Storytelling style', 'Talk and film text']
MAIN = 'hangs-writing-style-reference.md'
DECISIONS = 'review-decisions.md'
SIGNALS = 'preference-signals.md'
REVIEW_DIR = 'reviews'
HAND_HEADING = "Hang's hand edits"
# Hang's own words and edits weigh most, then declines, then acceptances. A note that Hang left
# on a decision adds to its weight. A decision Hang delegated, or one that was inferred, weighs nothing.
WEIGHTS = {'instruction': 5, 'hand edit': 4, 'edited': 4, 'declined': 3, 'accepted': 1}
NOTE_BONUS = 2
STRONG = 3
# The technical vocabulary is built separately by tools/build_vocabulary.py.
VOCAB = HERE / 'tech-vocabulary.json'
VOCAB_TERMS = (sum(1 for t in json.loads(VOCAB.read_text(encoding='utf-8'))['terms'] if t['tier'] != 'Not found')
               if VOCAB.exists() else 0)
EXAMPLE_SELECTION = {
    'Teachers and collection settings': 4,
    'Imperfect teaching and structured behavior': 2,
    'Method operations and their objects': 4,
    'Accuracy consistency and robustness': 2,
    'Practical purpose': 2,
    'Emphasis': 2,
    'Study actions leading to the analytical question': 3,
    'An intuition leading to an operation': 5,
    'Purpose attached to an action': 2,
    'Known information leading to new information': 3,
    'Means expressed with by': 1,
    'Procedural series and enumerations': 3,
    'Local reasons and governing conditions': 7,
    'An introduction built around a consequential assumption': 4,
    'A study finding leading to a method': 3,
    'The three stage dissertation arc': 3,
    'A results paragraph answering one comparison': 3,
    'Discussion synthesis and its boundary': 4,
}
EXAMPLE_NOTES = {
    'Impersonal dissertation voice': 'paper voice before dissertation adaptation',
    'Established dissertation terminology': 'historical wording to adapt using the guidance above',
    'Literal wording': 'the explicitly announced analogy',
    'Few colons and semicolons': 'a colon before an announced term, the use that remains',
}
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
          'October', 'November', 'December']


def slug(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


def strip_prefix(s, prefix):
    return s[len(prefix):] if s.startswith(prefix) else s


def key(e):
    return ('v:' + strip_prefix(e['source_id'], 'LIB-')) if e['source'] == 'v1' else 'c:' + e['source_id']


def write(name, text):
    path = HERE / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + '\n', encoding='utf-8')


def day(iso):
    y, m, d = iso[:10].split('-')
    return f"{MONTHS[int(m) - 1]} {int(d)}, {y}"


def source_label(e):
    return f"{e['source']} {e['source_id']}"


def original_entry_link(e):
    # The original library folders were removed after the merge; the snapshots are the retained copies.
    snapshot = 'v1-library.md' if e['source'] == 'v1' else 'claude-library.md'
    return f"[{source_label(e)}](sources/{snapshot})"


def evidence_link(ev):
    # Line numbers are prose because generic Markdown file links do not navigate source lines.
    label = f"{ev['paper']}, line {ev['line']}"
    if ev.get('line_end', ev['line']) != ev['line']:
        label += f"–{ev['line_end']}"
    return f"[{label}](../{quote(ev['file'], safe='/')})"


def plain(s):
    """Wording as the reference quotes it: no tags, emphasis as *...*, one space."""
    s = re.sub(r'\\hang\{[^{}]*\}', ' ', s or '')
    s = re.sub(r'\\textit\{([^{}]*)\}', r'*\1*', s)
    s = s.replace('\\%', '%')
    return re.sub(r'\s+', ' ', s).strip()


def quoted(s):
    return '“' + s.rstrip('.') + '”'


def fence(text, lang):
    return '~~~' + lang + '\n' + text.strip('\n') + '\n~~~\n'


def plural(n, word):
    return f"{n} {word}" + ('' if n == 1 else ('es' if word.endswith('ch') else 's'))


source_by_key = {key(e): e for e in SOURCE_ENTRIES}
used = [k for e in ENTRIES for k in e['sources']]
assert set(used) == set(source_by_key), ('Unmapped', set(source_by_key) - set(used),
                                      'Unknown', set(used) - set(source_by_key))
assert all(n == 1 for n in Counter(used).values()), 'Each original entry needs one primary home.'
assert len({slug(e['title']) for e in ENTRIES}) == len(ENTRIES)
assert all(e['category'] in CATEGORIES for e in ENTRIES)

review_items, review_by_id = {}, {}
for review in REVIEWS:
    review_by_id[review['review_id']] = review
    for item in review['items']:
        assert item['id'] not in review_items, 'Review item ids must differ: ' + item['id']
        review_items[item['id']] = dict(item, review_id=review['review_id'])
instructions = {h['id']: h for h in INSTRUCTIONS}
hand_edits = {h['id']: h for h in HAND_EDITS}
assert not set(instructions) & set(review_items) and not set(hand_edits) & set(review_items)


def review_file(review_id):
    return f"{REVIEW_DIR}/{review_id}.md"


def evidence_href(ev_id, from_dir=''):
    prefix = '../' if from_dir else ''
    if ev_id in review_items:
        return f"{prefix}{review_file(review_items[ev_id]['review_id'])}#{slug(ev_id)}"
    return f"{prefix}{SIGNALS}#{slug(ev_id)}"


def outcome(item):
    if item['source'] != 'hang':
        verb = 'declined' if item['status'] == 'rejected' else 'accepted with an edit' if item['edited'] else 'accepted'
        return verb + ' under delegation' if item['source'] == 'assistant-delegated' else verb + ' by inference'
    if item['status'] == 'rejected':
        return 'declined'
    return "accepted with Hang's edit" if item['edited'] else 'accepted'


def item_weight(item):
    if item['source'] != 'hang':
        return 0
    base = WEIGHTS['edited'] if item['edited'] else WEIGHTS['declined'] if item['status'] == 'rejected' else WEIGHTS['accepted']
    return base + (NOTE_BONUS if item.get('comment') else 0)


def evidence_weight(ev_id):
    if ev_id in instructions:
        return WEIGHTS['instruction']
    if ev_id in hand_edits:
        return WEIGHTS['hand edit']
    return item_weight(review_items[ev_id])


def evidence_kind(ev_id):
    if ev_id in instructions:
        return 'instruction'
    if ev_id in hand_edits:
        return 'hand edit'
    item = review_items[ev_id]
    return 'edit' if item['edited'] else 'decline' if item['status'] == 'rejected' else 'acceptance'


def hang_note(item):
    return item['comment'] if item['source'] == 'hang' and item.get('comment') else ''


def hand_texts(edit, side):
    return [plain(c[side]) for c in edit['changes'] if c[side]]


def review_line(x):
    """One example as a sentence, after its wording has been checked against its record."""
    ev_id, kind, a, b = x['item'], x['kind'], x['a'], x['b']
    where = ev_id + ' ' + kind
    qa, qb = quoted(a), quoted(b)
    link = f"[{ev_id}]({evidence_href(ev_id)})"
    if kind == 'said':
        h = instructions.get(ev_id)
        assert h and a and any(a in t for t in h['excerpts']), where
        text = f"{qa}."
        label = f"Hang's instruction, {day(h['date'])}"
    elif kind == 'hand':
        h = hand_edits.get(ev_id)
        assert h, where
        assert not a or any(a in t for t in hand_texts(h, 'before')), where
        assert not b or any(b in t for t in hand_texts(h, 'after')), where
        assert a or b or x['note'], where
        if a and b:
            text = f"{qa} became {qb}."
        elif a:
            text = f"{qa} was removed."
        elif b:
            text = f"Hang wrote {qb}."
        else:
            text = ''
        label = "Hang's own edit"
    else:
        item = review_items.get(ev_id)
        assert item, 'Unknown review item: ' + ev_id
        assert item_weight(item) > 0, 'A decision that Hang did not make cannot be cited: ' + ev_id
        original, suggested, final = plain(item['original']), plain(item['suggested']), plain(item['final'])
        if kind == 'accepted':
            assert item['status'] == 'accepted' and a in original and (not b or b in final), where
            if not a:
                assert b, where
                text = f"Accepted {qb}."
            elif b:
                text = f"{qa} became {qb}."
            else:
                cut = item['type'] in ('cut', 'delete', 'drop') or item['op'] == 'delete' or '[HY removed]' in final
                moved = '[HY moved' in final
                text = f"{qa} was {'moved' if moved else 'cut' if cut else 'replaced'}."
        elif kind == 'edited':
            assert item['edited'] and (a or b), where
            assert (not a or a in suggested) and (not b or b in final), where
            if a and b:
                text = f"Suggested {qa}. Hang's wording is {qb}."
            elif a:
                assert a not in final, where
                text = f"Hang deleted the suggested {qa}."
            else:
                assert b not in suggested, where
                text = f"Hang added {qb}."
        elif kind == 'declined':
            assert item['status'] == 'rejected' and a in suggested and (not b or b in original) and (a or b), where
            text = (f"Suggested {qa}. Hang kept {qb}." if a and b else f"Suggested {qa}." if a else f"Hang kept {qb}.")
        elif kind == 'kept':
            assert item['status'] == 'accepted' and b in final, where
            text = f"Kept {qb}."
        else:
            assert kind == 'note' and (x['note'] or hang_note(item)), where
            text = ''
        if hang_note(item):
            text = (text + f" Hang's note: {quoted(hang_note(item))}.").strip()
        label = outcome(item)
    text = (text + ' ' + x['note']).strip()
    return f"{link}, {label} (weight {evidence_weight(ev_id)}). {text}".rstrip()


compiled = []
for i, e in enumerate(ENTRIES, 1):
    evidence = {}
    for src_key in e['sources']:
        for ev in source_by_key[src_key]['evidence']:
            fingerprint = (ev['file'], ev['line'], ev['quote'])
            if fingerprint not in evidence:
                evidence[fingerprint] = dict(ev, source_entries=[])
            evidence[fingerprint]['source_entries'].append(src_key)
    evidence_list = list(evidence.values())
    assert evidence_list or e['review'], 'A pattern needs paper evidence or evidence from Hang: ' + e['title']
    candidates = [j for j, ev in enumerate(evidence_list) if 60 <= len(ev['quote']) <= 450]
    example_index = EXAMPLE_SELECTION.get(e['title'], (candidates or [0])[0]) if evidence_list else None
    review = [dict(x, text=review_line(x), weight=evidence_weight(x['item'])) for x in e['review']]
    order = sorted(range(len(review)), key=lambda j: (-review[j]['weight'], j))
    review = [review[j] for j in order]
    distinct = list(dict.fromkeys(x['item'] for x in review))
    kinds = Counter(evidence_kind(v) for v in distinct)
    notes = sum(1 for v in distinct if v in review_items and hang_note(review_items[v]))
    compiled.append(dict(e, id=f'HSR-{i:02d}', anchor=slug(e['title']),
                         evidence=evidence_list, example_index=example_index,
                         example_note=EXAMPLE_NOTES.get(e['title'], ''), review=review,
                         weight=sum(evidence_weight(v) for v in distinct),
                         evidence_counts=dict(kinds), hang_notes=notes))
by_title = {e['title']: e for e in compiled}

cited_in = {}
for e in compiled:
    for x in e['review']:
        if e not in cited_in.setdefault(x['item'], []):
            cited_in[x['item']].append(e)

uncited_reason = {}
for reason, ids in UNCITED.items():
    for ev_id in ids:
        assert ev_id in review_items or ev_id in hand_edits or ev_id in instructions, 'Unknown id in UNCITED: ' + ev_id
        assert ev_id not in cited_in, 'Cited and also listed as not used: ' + ev_id
        assert ev_id not in uncited_reason, 'Listed twice in UNCITED: ' + ev_id
        uncited_reason[ev_id] = reason
strong_ids = [v for v in review_items if evidence_weight(v) >= STRONG] + list(hand_edits) + list(instructions)
missing = [v for v in strong_ids if v not in cited_in and v not in uncited_reason]
assert not missing, 'Strong signals neither cited nor explained: ' + ', '.join(missing)


def summary(e):
    counts = e['evidence_counts']
    parts = [plural(counts[k], k) for k in ('instruction', 'hand edit', 'edit', 'decline', 'acceptance') if counts.get(k)]
    if e['hang_notes']:
        parts.append(plural(e['hang_notes'], 'note'))
    return f"**Evidence from Hang** · weight {e['weight']}" + (' (' + ', '.join(parts) + ')' if parts else '')


def quick_weight(titles):
    ids = list(dict.fromkeys(x['item'] for t in titles for x in by_title[t]['review']))
    return sum(evidence_weight(v) for v in ids)


hang_items = [i for i in review_items.values() if i['source'] == 'hang']
delegated_items = [i for i in review_items.values() if i['source'] != 'hang']
totals = {
    'decided': len(review_items), 'by_hang': len(hang_items), 'delegated': len(delegated_items),
    'accepted': sum(i['status'] == 'accepted' and not i['edited'] for i in hang_items),
    'edited': sum(i['edited'] for i in hang_items),
    'declined': sum(i['status'] == 'rejected' for i in hang_items),
    'notes': sum(bool(hang_note(i)) for i in hang_items),
}
review_ids_text = ', '.join(r['review_id'] for r in REVIEWS)
new_oct19 = [e for e in compiled if e['updated'] == 'New pattern.']
revised_oct19 = [e for e in compiled if e['updated'] and e['updated'] != 'New pattern.']

quick = '\n'.join(f"{n}. {text} (weight {quick_weight(titles)})" for n, (text, titles) in enumerate(QUICK_REFERENCE, 1))
intro = f"""# Hang's writing style reference

Use this reference when drafting or revising Hang Yu's dissertation, and the wording of the dissertation talk and film. The voice is direct, concrete, explanatory, and attentive to how non-experts actually teach robots. State what was done, what was found, and what the finding means. Explain methods through their operations, keep scientific terms stable, and make claim strength match the evidence.

The dissertation default is impersonal. Use this dissertation, this chapter, the study, the method, participants, or results as the subject. Preserve the directness of the papers without importing their first-person voice into new dissertation prose.

The reference rests on two kinds of evidence. Paper examples show how the published manuscripts are written. Evidence from Hang shows what Hang asked for, edited, declined, or accepted. It comes from Hang's messages in the sessions on the dissertation and the talk, from Hang's own edits of the chapters and slides, and from {totals['decided']} decisions in {len(REVIEWS)} reviews, {totals['by_hang']} of them made by Hang. Evidence from Hang is the later and more direct statement of preference, so it takes priority where the two differ.

Current instructions and the meaning, data, and definitions of the passage take priority over a reusable form. Square brackets mark slots to fill. Forms in this guide are reusable wording, not empirical findings. Paper examples retain source wording. Their older terminology, first person, stronger claims, and punctuation do not override the guidance.

## How the evidence is weighted

Hang asked for declines, notes, and edits to count for more than acceptances. Each piece of evidence from Hang carries a weight, and each pattern shows the sum over the evidence it cites, with the heaviest first. A decision that an assistant made under Hang's delegation, or one that was inferred from Hang's other decisions, is kept in the record with weight 0 and is never cited.

| Evidence | Weight |
| --- | ---: |
| An instruction in Hang's own words | {WEIGHTS['instruction']} |
| An edit Hang made by hand to a chapter or a slide | {WEIGHTS['hand edit']} |
| A suggestion that Hang accepted with an edit | {WEIGHTS['edited']} |
| A suggestion that Hang declined | {WEIGHTS['declined']} |
| A note that Hang left on a decision | adds {NOTE_BONUS} |
| A suggestion that Hang accepted as written | {WEIGHTS['accepted']} |
| A decision made under delegation or inferred | 0 |

[Every weighted signal, and the patterns ranked by weight](preference-signals.md) · [The record of each review]({DECISIONS})

## Quick reference

The weight after each item is the total weight of the evidence that the patterns behind it cite.

{quick}

## Find a pattern

"""

main = [intro]
for category in CATEGORIES:
    main.append(f"- [{category}](#{slug(category)})")
main.append(f'\n[Complete paper evidence](source-evidence.md) · [Weighted signals]({SIGNALS}) · [All review decisions]({DECISIONS}) · [Source map and merge decisions](source-map.md) · [Technical vocabulary](tech-vocabulary.md) · [All words in the papers](word-list.md)\n')

main.append(f"## What changed on October 19, 2026\n\n{UPDATE_SUMMARY}\n")
main.append('**New patterns**\n')
main.extend(f"- [{e['title']}](#{e['anchor']}) ({e['category']}), weight {e['weight']}" for e in new_oct19)
main.append('\n**Revised patterns**\n')
main.extend(f"- [{e['title']}](#{e['anchor']}). {e['updated']}" for e in revised_oct19)
main.append(f"\nThe Chapter 8 review of October 12, 2026 had added four patterns and revised {sum(bool(e['changed']) and not e['new'] for e in compiled)}. What it changed in each pattern is listed in [source-map.md](source-map.md#changes-from-evidence-from-hang).\n")

for category in CATEGORIES:
    main.append(f'## {category}\n')
    if category == 'Vocabulary' and VOCAB_TERMS:
        main.append('The patterns below are about word choice. For single technical terms, [Hang\'s technical vocabulary]'
                    f'(tech-vocabulary.md) lists {VOCAB_TERMS} terms from the papers and the reference dissertations with an '
                    'estimate of how familiar each one is to Hang, and [word-list.md](word-list.md) lists every word the papers use.\n')
    if category == 'Talk and film text':
        main.append('These patterns are for the slides, the speaker notes, and the film of the dissertation talk. They rest on the reviews '
                    'of the talk and the film and on Hang\'s messages about them. The chapters keep the patterns above.\n')
    for e in compiled:
        if e['category'] != category:
            continue
        main.extend([f"### {e['title']}\n", e['guidance'] + '\n', f"**{e['forms_label']}**\n"])
        main.extend('- ' + form for form in e['forms'])
        main.append('\n**Keep the meaning.** ' + e['boundary'] + '\n')
        if e['review']:
            main.append(summary(e) + '\n')
            main.extend('- ' + x['text'] for x in e['review'])
            main.append('')
        if e['evidence']:
            sample = e['evidence'][e['example_index']]
            note = f" ({e['example_note']})" if e['example_note'] else ''
            main.append('**Paper example**' + note + ' — ' + evidence_link(sample) + '\n')
            main.append('\n'.join('> ' + line for line in sample['quote'].splitlines()) + '\n')
            main.append(f"[All source examples for this pattern](source-evidence.md#{e['anchor']}).\n")
        else:
            main.append('**Basis.** This pattern comes from the evidence from Hang above. It has no paper example.\n')

main.append(f"""## Scope of this reference

The two source libraries draw on CHARM, Demonstration Sidetracks, STEADY, Progress, PHIRL, and the RSS Pioneers prospectus. Five are coauthored and the prospectus is single-authored. These sources support a reference for the dissertation's manuscript voice, not attribution of every sentence to Hang personally.

The guide combines observed manuscript patterns, dissertation preferences recorded in the source libraries, reusable editorial forms, and evidence from Hang. The reviews record each decision and the final wording, and only sometimes a note from Hang, so the guidance drawn from a decision is a reading of what changed. Hang's instructions are quoted as typed, including spelling. A later instruction from Hang replaces any pattern. Some edited wording in the record still needs a check before it is used, and [{DECISIONS}]({DECISIONS}) lists those items.

Reviews that were still undecided on October 19, 2026 give no evidence, except where Hang applied their suggestions by hand. They are listed in [{DECISIONS}]({DECISIONS}#undecided-reviews).
""")
write(MAIN, '\n'.join(main))

evidence_doc = ["""# Source evidence for Hang's writing style reference

Examples are grouped under the same patterns as the [main reference](hangs-writing-style-reference.md). Source line numbers identify LaTeX source lines, not PDF pages. Identical file, line, and quotation records within a pattern are shown once, with all source-entry attributions. Patterns that rest only on evidence from Hang have no paper examples, and their evidence is listed in [preference-signals.md](preference-signals.md).

The v1 library preserves LaTeX excerpts. The Claude library transcribes emphasis, omits citations, and uses ellipses for omissions. The excerpts below preserve those respective representations. Quoted wording is evidence of manuscript practice, including occasional grammar, punctuation, or claims that the merged guide qualifies. It is not an instruction to reuse an outdated term, number, or claim.

The complete original entry text and metadata are retained in [source-entries.json](sources/source-entries.json). The original library texts are also preserved as [v1](sources/v1-library.md) and [Claude](sources/claude-library.md) snapshots. Their relative paths were written for the original folders.
"""]
for e in compiled:
    if not e['evidence']:
        continue
    evidence_doc.append(f"## {e['title']}\n")
    evidence_doc.append(f"[Merged guidance]({MAIN}#{e['anchor']})\n")
    for ev in e['evidence']:
        attributed = ', '.join(source_label(source_by_key[k]) for k in ev['source_entries'])
        evidence_doc.append(f"**{evidence_link(ev)}** — {attributed}\n")
        evidence_doc.append('```text\n' + ev['quote'] + '\n```\n')
write('source-evidence.md', '\n'.join(evidence_doc))


def used_in(ev_id, from_dir=''):
    prefix = '../' if from_dir else ''
    patterns = cited_in.get(ev_id, [])
    if patterns:
        return 'Used in: ' + ', '.join(f"[{e['title']}]({prefix}{MAIN}#{e['anchor']})" for e in patterns) + '.'
    if ev_id in uncited_reason:
        return 'Not used in a pattern: ' + uncited_reason[ev_id]
    return ''


# One record per review, kept beside the index.
index_rows = []
for review in REVIEWS:
    c = review['counts']
    items = review['items']
    mine = [i for i in items if i['source'] == 'hang']
    others = [i for i in items if i['source'] != 'hang']
    lang = 'latex' if review['document'] == 'dissertation' else 'text'
    group_label = {g['key']: g['label'] for g in review['groups']}
    dates = sorted(i['decided_at'] for i in items)
    weight = sum(item_weight(i) for i in items)
    doc = [f"# {review['title']}\n",
           f"Review `{review['review_id']}` of the {review['document']}, from `{review['folder']}`. "
           f"Decided between {day(dates[0])} and {day(dates[-1])}. Decisions files: "
           + ', '.join('`' + b['file'] + '`' + ('' if b['source'] == 'hang' else f" ({b['source']})") for b in review['batches']) + '.\n',
           '[All reviews](../review-decisions.md) · [Weighted signals](../preference-signals.md) · [Main reference](../hangs-writing-style-reference.md)\n',
           '| Outcome | Decided by Hang | Not decided by Hang |', '| --- | ---: | ---: |']
    for label, test in [('Accepted as suggested', lambda i: i['status'] == 'accepted' and not i['edited']),
                        ("Accepted with Hang's edit", lambda i: i['edited']),
                        ('Declined', lambda i: i['status'] == 'rejected')]:
        doc.append(f"| {label} | {sum(map(test, mine))} | {sum(map(test, others))} |")
    doc.append(f"| Notes from Hang | {sum(bool(hang_note(i)) for i in mine)} | |\n")
    if others:
        sources = sorted(set(i['source'] for i in others))
        doc.append(f"{len(others)} decisions in this review were not made by Hang ({', '.join(sources)}). "
                   "They are listed with the reason that was recorded for them and carry no weight.\n")
    if c['items'] > c['decided']:
        doc.append(f"{c['items'] - c['decided']} of the {c['items']} items had no decision when the review was imported.\n")
    checks = [i for i in items if i['id'] in REVIEW_CHECKS]
    if checks:
        doc.append('**To check before the accepted wording is used**\n')
        doc.extend(f"- [{i['id']}](#{slug(i['id'])}). {REVIEW_CHECKS[i['id']]}" for i in checks)
        doc.append('')
    for item in items:
        where = item.get('where') or ''
        if item.get('line'):
            where = (where + ', ' if where else '') + f"`{item['file']}`, line {item['line']}"
        type_label = review['types'].get(item['type'], item['type'])
        head = (f"**{outcome(item)[0].upper() + outcome(item)[1:]}** · weight {item_weight(item)} · {type_label} · "
                f"{group_label.get(item['group'], item['group'])}" + (f" · {where}" if where else ''))
        doc.extend([f"### {item['id']}\n", head + '\n'])
        if item['source'] != 'hang':
            doc.append(f"Decided by an assistant ({item['source']}), not by Hang."
                       + (f" Recorded reason: {item['comment']}" if item.get('comment') else '') + '\n')
        if item['title']:
            doc.append(f"Suggestion: {item['title']}\n")
        accepted, inserted = item['status'] == 'accepted', item['op'] == 'insert'
        if inserted:
            doc.extend(['New text, placed next to this passage:\n', fence(item['anchor'] or '(no anchor)', lang)])
        elif item['original']:
            doc.extend(['Original' + ('' if accepted else ', which stayed') + ':\n', fence(item['original'], lang)])
        if not accepted:
            doc.extend(['Declined suggestion:\n', fence(item['suggested'] or '(delete the passage)', lang)])
        elif item['edited']:
            doc.extend(['Suggested:\n', fence(item['suggested'] or '(delete the passage)', lang),
                        ("Hang's wording:\n" if item['source'] == 'hang' else 'Final wording, set by the assistant:\n'),
                        fence(item['final'] or '(empty)', lang)])
        else:
            doc.extend(['Accepted wording:\n', fence(item['suggested'] or '(delete the passage)', lang)])
        if hang_note(item):
            doc.append(f"Hang's note: {hang_note(item)}\n")
        if item['id'] in REVIEW_CHECKS:
            doc.append('To check: ' + REVIEW_CHECKS[item['id']] + '\n')
        if item['note']:
            doc.append('Note written with the suggestion: ' + item['note'] + '\n')
        line = used_in(item['id'], from_dir=REVIEW_DIR)
        if line:
            doc.append(line + '\n')
    write(review_file(review['review_id']), '\n'.join(doc))
    index_rows.append(f"| [{review['title']}]({review_file(review['review_id'])}) | {review['document']} | "
                      f"{day(dates[0])} | {c['decided']} | {len(mine)} | "
                      f"{sum(i['status'] == 'accepted' and not i['edited'] for i in mine)} | {sum(i['edited'] for i in mine)} | "
                      f"{sum(i['status'] == 'rejected' for i in mine)} | {sum(bool(hang_note(i)) for i in mine)} | {weight} |")

decisions_doc = [f"""# Review decisions behind Hang's writing style reference

This file indexes the reviews whose decisions the [main reference]({MAIN}) draws on. Each suggestion was written by an assistant. Hang accepted it, accepted it with an edit, or declined it, and sometimes left a note. In two reviews Hang delegated the remaining decisions, and those decisions are kept with weight 0. The record of each review is in its own file under `{REVIEW_DIR}/`.

The review folders are removed when a review is finished, so the wording is kept here. Line numbers are those of the file at the time of the review. Dissertation text is LaTeX, as it was on the review page, and slide text is as it was in the deck. Most decisions record no reason, so each "Used in" link leads to a reading of the decision, not to a statement by Hang.

| Review | Document | First decision | Decisions | By Hang | Accepted | Edited | Declined | Notes | Weight |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |"""]
decisions_doc.extend(index_rows)
decisions_doc.append(f"| Total | | | {totals['decided']} | {totals['by_hang']} | {totals['accepted']} | {totals['edited']} | "
                     f"{totals['declined']} | {totals['notes']} | {sum(item_weight(i) for i in hang_items)} |\n")
decisions_doc.append('## To check before the accepted wording is used\n')
decisions_doc.extend(f"- [{k}]({evidence_href(k)}) ({review_items[k]['review_id']}). {v}" for k, v in REVIEW_CHECKS.items())
decisions_doc.append('\n## Undecided reviews\n')
decisions_doc.append('These review folders had no saved decisions on October 19, 2026, or had items left open, so they give no evidence of preference. '
                     f"Where Hang applied suggestions by hand, the edits are recorded in [{SIGNALS}]({SIGNALS}#{slug(HAND_HEADING)}).\n")
decisions_doc.extend(f"- `{p['folder']}`. {p['note']}" for p in PENDING_REVIEWS)
write(DECISIONS, '\n'.join(decisions_doc))

# Every weighted signal in one place.
all_ids = list(instructions) + list(hand_edits) + [i['id'] for i in hang_items]
by_kind = Counter(evidence_kind(v) for v in all_ids)
weight_by_kind = Counter()
for v in all_ids:
    weight_by_kind[evidence_kind(v)] += evidence_weight(v)
note_count = totals['notes']
signals = [f"""# Preference signals behind Hang's writing style reference

Hang asked on October 19, 2026 to update the reference from every writing suggestion and change in `waiting_for_review/` and in the talk's `wait_to_review/`, and from the interaction history, with more weight on rejections, notes, and edits. This file lists that evidence with its weight. The [main reference]({MAIN}) cites it pattern by pattern, heaviest first.

## How evidence is weighted

| Evidence | Weight each | Count | Total weight |
| --- | ---: | ---: | ---: |
| An instruction in Hang's own words | {WEIGHTS['instruction']} | {by_kind['instruction']} | {weight_by_kind['instruction']} |
| An edit Hang made by hand | {WEIGHTS['hand edit']} | {by_kind['hand edit']} | {weight_by_kind['hand edit']} |
| A suggestion Hang accepted with an edit | {WEIGHTS['edited']} | {by_kind['edit']} | {weight_by_kind['edit']} |
| A suggestion Hang declined | {WEIGHTS['declined']} | {by_kind['decline']} | {weight_by_kind['decline']} |
| A suggestion Hang accepted as written | {WEIGHTS['accepted']} | {by_kind['acceptance']} | {weight_by_kind['acceptance']} |
| A note Hang left on a decision, added to that decision | {NOTE_BONUS} | {note_count} | included above |
| A decision made under delegation or inferred | 0 | {totals['delegated']} | 0 |

Instructions are quoted from Hang's messages in the Claude Code sessions for the dissertation and the talk, and from the preferences file Hang wrote for the slides. Messages that pasted another reviewer's text are not counted as Hang's words. Hand edits compare the chapters with the commit of October 14, 2026, and quote the feedback log of the talk for slide edits.

Every signal of weight {STRONG} or more is either cited by a pattern or listed at the end with the reason it is not.

## Patterns by weight

| Pattern | Category | Weight | Evidence |
| --- | --- | ---: | --- |"""]
for e in sorted(compiled, key=lambda e: -e['weight']):
    if e['weight']:
        signals.append(f"| [{e['title']}]({MAIN}#{e['anchor']}) | {e['category']} | {e['weight']} | {summary(e).split('(')[-1].rstrip(')') if '(' in summary(e) else ''} |")
signals.append("\n## Hang's instructions\n")
for h in INSTRUCTIONS:
    when = day(h['date']) + (f", {h['time']}" if h.get('time') else '')
    origin = f"session `{h['session'][:8]}`" if h['source'] == 'message' else f"`{h['file']}`"
    signals.append(f"### {h['id']}\n")
    signals.append(f"{h['topic']}. {when}, {h['project']}, {origin}. Weight {WEIGHTS['instruction']}.\n")
    signals.append('\n>\n'.join('> ' + x for x in h['excerpts']) + '\n')
    signals.append(used_in(h['id']) + '\n')
signals.append(f"## {HAND_HEADING}\n")
for h in HAND_EDITS:
    signals.append(f"### {h['id']}\n")
    signals.append(f"{h['topic']}. {h['origin'][0].upper() + h['origin'][1:]}, {h['dated']}. Weight {WEIGHTS['hand edit']}.\n")
    lang = 'latex' if h['where'] == 'dissertation' else 'text'
    for c in h['changes']:
        if c['before']:
            signals.extend([f"Before (`{c['file']}`):\n", fence(c['before'], lang)])
        if c['after']:
            signals.extend(['After:\n', fence(c['after'], lang)])
    if h.get('applied'):
        signals.append('Applied by hand: ' + ', '.join(h['applied']) + '. Not applied: ' + ', '.join(h['not_applied']) + '.\n')
    if h['note']:
        signals.append(h['note'] + '\n')
    if h['id'] in HAND_CHECKS:
        signals.append('To check: ' + HAND_CHECKS[h['id']] + '\n')
    signals.append(used_in(h['id']) + '\n')
signals.append('## Declines, edits, and notes in the reviews\n')
signals.append('Accepted suggestions without a note are in the record of each review and are not repeated here.\n')
for review in REVIEWS:
    strong = [i for i in review['items'] if item_weight(i) >= STRONG]
    if not strong:
        continue
    signals.append(f"### {review['title']}\n")
    for i in strong:
        note = f" Hang's note: {quoted(hang_note(i))}." if hang_note(i) else ''
        signals.append(f"- [{i['id']}]({evidence_href(i['id'])}) · {outcome(i)} · weight {item_weight(i)} · {i['title'] or i['type']}.{note} {used_in(i['id'])}".rstrip())
    signals.append('')
signals.append('## Strong signals not used in a pattern\n')
signals.append('Each of these carries weight but does not bear on wording, or is already covered elsewhere, for the reason given.\n')
for reason, ids in UNCITED.items():
    signals.append(f"- {reason} " + ', '.join(f"[{v}]({evidence_href(v)})" for v in ids) + '.')
write(SIGNALS, '\n'.join(signals))

metadata = {
    'schema': 'hang-writing-style-reference/3',
    'title': "Hang's writing style reference",
    'prepared': '2026-10-12',
    'revised': '2026-10-19',
    'status': 'Working reference requested by Hang, revised on October 12, 2026 from the Chapter 8 review and on October 19, 2026 from all reviews, Hang\'s messages, and Hang\'s hand edits, with weights that favor declines, notes, and edits.',
    'source_counts': dict(Counter(e['source'] for e in SOURCE_ENTRIES)),
    'source_entry_count': len(SOURCE_ENTRIES),
    'entry_count': len(compiled),
    'categories': CATEGORIES,
    'weights': dict(WEIGHTS, note_bonus=NOTE_BONUS, delegated=0),
    'precedence': ['Current user instructions', 'Current passage facts and definitions',
                   "Hang's instructions, hand edits, and review decisions, by weight", 'Merged dissertation guidance',
                   'Paper wording examples'],
    'reviews': [dict(review_id=r['review_id'], title=r['title'], document=r['document'], folder=r['folder'],
                     counts=r['counts'], batches=r['batches']) for r in REVIEWS],
    'pending_reviews': PENDING_REVIEWS,
    'instructions': INSTRUCTIONS,
    'hand_edits': HAND_EDITS,
    'review_checks': REVIEW_CHECKS,
    'hand_checks': HAND_CHECKS,
    'quick_reference': [dict(text=t, patterns=p, weight=quick_weight(p)) for t, p in QUICK_REFERENCE],
    'uncited': UNCITED,
    'entries': compiled,
}
write('library.json', json.dumps(metadata, ensure_ascii=False, indent=2))

from_papers = sum(bool(e['sources']) for e in compiled)
notes = [f"""# Source map and merge decisions

The reference combines all {len(SOURCE_ENTRIES)} reusable entries: 38 from writing-style-library-v1 and 58 from writing-style-library-claude. They are organized into {from_papers} merged patterns. Each original entry has one primary home in the table below. Overlapping material is synthesized in that home, while the full original entry remains in the source archive. A further {len(compiled) - from_papers} patterns come from evidence from Hang and have no original entry.

## Resolved differences

| Topic | Resolution |
| --- | --- |
| Dissertation voice | Use the impersonal dissertation preference recorded in Claude WRD-02. Retain v1's emphasis on concrete subjects and purposeful passives. Original first-person quotations remain evidence. |
| Evidence verbs | Change the grammatical subject without automatically changing found to suggested. Select the verb by the claim's evidential job. |
| Literal synthesis wording | Replace v1's proposed Read together opening with These findings suggest or a specific statement of the connection, following Claude's literal wording preference. Preserve the underlying synthesis structure. |
| Sentence length and fixed counts | Keep the observed short-to-medium cadence, but treat about 20 words, seven introduction moves, one intuition, and a three-sentence example as flexible patterns. Preserve meaning and necessary conditions. |
| Scalar scales | Scope Claude's 0 to 10 correction to the relevant STEADY scalar feedback context. Current introduction and discussion passages distinguish STEADY's 0 to 10 from CHARM's five-point scale. Do not impose one range on every signal. |
| Progress wording | Prefer degree of completion / degree of task completion and the recorded under-explored as a human teaching signal wording. Preserve formal definitions and numerical ranges by chapter. |
| Null results | No difference was detected describes the tested result. It does not establish equivalence or justify the difference vanishes. |
| Hypothesis verdicts | Retain supported / not supported wording, with the same evidential limits; an equality hypothesis is not established merely by a nonsignificant difference test. |
| Shared references | Keep the reference-state explanation and the possibility of user-dependent scaling. Common endpoints do not imply identical intermediate annotations. |
| Source grammar and counts | Preserve original quotations and approximate counts in the archive. Use polished reusable forms in the guide. Corpus absence and frequency do not establish grammatical bans or writing quotas. |
| Emphasis | Preserve italics for the technical signal and selective rhetorical emphasis. Do not apply once-per-paragraph advice in a way that breaks consistent term formatting. |
| Chapter continuity | Keep the three-stage conceptual arc and explicit study-to-method transitions. Do not imply shared datasets, participants, or an end-to-end controlled evaluation. |
| Colons and semicolons | Hang's instruction of October 12, 2026 (use fewer) replaces the dissertation advice of Claude SEN-04, which was to use the colon as the papers do, and limits the semicolon list of Claude STR-09 to long lists whose items contain commas. The punctuation review of the same day then showed the four kinds of colon Hang keeps. The paper quotations with colons remain as evidence of the earlier habit. |
| One job per sentence | Keep the pattern, and add the limits shown by the reviews. Two studies or two requirements become two sentences. A which clause that interprets a result, a while contrast, a chain joined by but, and a numbered list of questions stay attached. |
| Talk and film text | The talk and the film use a spoken voice with first person and few words, so their patterns form a category of their own. The dissertation patterns still govern the chapters. |
| Weights | Declines, notes, edits, hand edits, and instructions count for more than acceptances, at Hang's request of October 19, 2026. Delegated and inferred decisions count for nothing. |

The records in the two library folders described initial proposals. Consolidating them into this working reference did not fabricate accept/reject decisions or apply their proposed dissertation changes. The two folders were removed from `waiting_for_review` after the merge, and their library texts remain in `sources/`.

## Changes from evidence from Hang

The Chapter 8 writing review of October 12, 2026 was the first review brought into the reference. On October 19, 2026, the decisions of {len(REVIEWS)} reviews ({totals['decided']} decisions, {totals['by_hang']} by Hang), {len(INSTRUCTIONS)} instructions, and {len(HAND_EDITS)} hand edits were brought in. The full record is in [{DECISIONS}]({DECISIONS}) and [{SIGNALS}]({SIGNALS}).

| Pattern | Weight | Change on October 12 | Change on October 19 | Evidence cited |
| --- | ---: | --- | --- | --- |"""]
for e in compiled:
    if e['review']:
        ids = ', '.join(dict.fromkeys(x['item'] for x in e['review']))
        notes.append(f"| [{e['title']}]({MAIN}#{e['anchor']}) | {e['weight']} | {e['changed'] or ''} | {e['updated'] or ''} | {ids} |")
hang_strong = [v for v in review_items if evidence_weight(v) >= STRONG]
notes.append(f"\n{len(cited_in)} pieces of evidence are cited by at least one pattern. Of the {len(hang_strong)} review decisions with weight "
             f"{STRONG} or more, {sum(v in cited_in for v in hang_strong)} are cited and the others are listed with a reason in "
             f"[{SIGNALS}]({SIGNALS}#strong-signals-not-used-in-a-pattern).\n")
notes.append("""## Coverage by category

| Category | Patterns |
| --- | ---: |""")
for category in CATEGORIES:
    notes.append(f"| {category} | {sum(e['category'] == category for e in compiled)} |")
notes.extend(['\n## Entry mapping\n', '| Original entry | Original title | Merged pattern |', '| --- | --- | --- |'])
mapping = {k: e for e in compiled for k in e['sources']}
for original in SOURCE_ENTRIES:
    e = mapping[key(original)]
    notes.append(f"| {original_entry_link(original)} | {original['title']} | [{e['title']}]({MAIN}#{e['anchor']}) |")
notes.append("""
The pattern that held Claude SEN-04 was titled A colon that introduces the point before the review. It is now Few colons and semicolons.

## Archive and maintenance

- `sources/source-entries.json` preserves all 96 source entries, including original guidance and all 280 evidence occurrences.
- `sources/v1-library.md` and `sources/claude-library.md` preserve the original library files byte for byte.
- `sources/review-decisions.json` preserves the suggestions, decisions, final wording, and notes of each imported review.
- `sources/hang-instructions.json` keeps the quoted instructions, with the session and time of each message.
- `sources/hand-edits.json` keeps Hang's hand edits, with the text before and after.
- `sources/preservation-baseline.json` records hashes of the source packages, manuscripts, chapters, and principal LaTeX files before the merge.
- `tools/authored_entries.py` contains the edited merged guidance, its source mapping, the evidence each pattern cites, the quick reference, and the reasons strong signals are not used.
- `tools/import_review.py` copies the decisions of a finished review into `sources/review-decisions.json`.
- `tools/build_reference.py` generates the reader files and structured library from that guidance and the preserved records, and sets the weights.
- `tools/validate_reference.py` checks coverage, quotes, evidence wording, file links, and preservation without applying dissertation edits.

If facts or definitions change in the dissertation, update the relevant guidance deliberately. A source excerpt is historical evidence, not an instruction to restore older values. The dissertation files change as writing continues, so the validation report counts those changes without treating them as errors. A change to a paper source is an error, because the quotations depend on it.
""")
write('source-map.md', '\n'.join(notes))

write('README.md', f"""# Hang's writing style reference

Start with [Hang's writing style reference]({MAIN}). It holds {len(compiled)} patterns across vocabulary, wording preference, writing style, sentence style, sentence structure, storytelling style, and talk and film text. {from_papers} of them combine the two writing style libraries built from the papers, and {len(compiled) - from_papers} come from evidence from Hang. The opening quick reference is useful before drafting. The detailed entries provide forms, meaning boundaries, weighted evidence from Hang, and paper examples.

| File | Use |
| --- | --- |
| [{MAIN}]({MAIN}) | The complete writing reference and quick reference |
| [{SIGNALS}]({SIGNALS}) | Every instruction, hand edit, decline, edit, and note from Hang, with its weight, and the patterns ranked by weight |
| [{DECISIONS}]({DECISIONS}) | The index of the {len(REVIEWS)} imported reviews, with the record of each in `{REVIEW_DIR}/` |
| [source-evidence.md](source-evidence.md) | All retained paper excerpts, grouped by merged pattern |
| [source-map.md](source-map.md) | How all 96 original entries were combined, how differences were resolved, and what the evidence from Hang changed |
| [library.json](library.json) | The merged guidance, evidence, and weights in a structured format |
| [validation.md](validation.md) | Coverage, quotation, evidence wording, link, and preservation checks |
| [tech-vocabulary.md](tech-vocabulary.md) | Technical terms from the papers and the three reference dissertations, each with an estimate of how familiar it is to Hang, an example, and its source |
| [word-list.md](word-list.md) | Every word family the papers use, grouped by the same familiarity estimate, and the words only the reference dissertations use |
| [tech-vocabulary.json](tech-vocabulary.json) | The vocabulary and the full word list in a structured format, read by the checker |
| [vocabulary-check-chapters.md](vocabulary-check-chapters.md) | The chapters checked against the vocabulary, as an example of the checker's report |
| [sources](sources/) | Preserved original entries, library snapshots, review decisions, Hang's instructions and hand edits, general English word frequencies, and the text of the reference dissertations |

Use the guide for new dissertation prose while preserving the current passage's facts and definitions. Paper quotations illustrate wording and do not supply facts for a different study. Evidence from Hang takes priority over the paper examples, heavier evidence over lighter, and the impersonal dissertation voice takes priority over first-person source examples in the chapters.

Prepared on October 12, 2026 from the two libraries that were then in `waiting_for_review`. Revised the same day from the decisions of the Chapter 8 writing review and from Hang's request to use fewer colons and semicolons. The technical vocabulary was added on October 17, 2026 from a scan of the papers in `reference_papers/` (CHARM, Demonstration Sidetracks, PHIRL, Progress, the prospectus, and STEADY), and expanded the same day with the Short, Vázquez, and Bobu dissertations in `dessertation_reference/`, which are counted separately and never raise a familiarity tier. Revised on October 19, 2026 from {totals['decided']} decisions in {len(REVIEWS)} reviews of the dissertation, the talk, and the film ({totals['by_hang']} of them by Hang), from {len(INSTRUCTIONS)} instructions in Hang's messages, and from {len(HAND_EDITS)} of Hang's hand edits, with more weight on declines, notes, and edits.

To rebuild after editing the guidance in `tools/authored_entries.py`, run `python writing_style_ref/tools/build_reference.py` from the dissertation folder. Then run `python writing_style_ref/tools/validate_reference.py`.

To bring in a later review, run `python writing_style_ref/tools/import_review.py <review folder>` before the review folder is removed. The folder can be in `waiting_for_review/` or in the talk's `wait_to_review/` (`../dissertation_presentation/wait_to_review/<folder>`). Add `--prefix X-` when the review's item ids repeat those of an imported review. Then cite its decisions in `tools/authored_entries.py`, or list a strong decision in `UNCITED` with its reason, and rebuild. The build stops when a decline, edit, or note is neither cited nor explained. Hang's instructions and hand edits are snapshots in `sources/hang-instructions.json` and `sources/hand-edits.json`, made by `tools/collect_hang_evidence.py`. Add a new instruction or hand edit there and rerun it before citing it.

To rebuild the technical vocabulary after adding a paper to `tools/vocab_corpus.py` or editing the term list in `tools/vocab_authored.py`, run `python writing_style_ref/tools/build_vocabulary.py`, then `build_reference.py` and `validate_reference.py`. If the reference dissertation PDFs change, run `tools/extract_reference_text.py` first. To check a draft, run `python writing_style_ref/tools/check_vocabulary.py chapters/<file>.tex`, or pass `--out <file>.md` to save the report. The example report is made with `python writing_style_ref/tools/check_vocabulary.py "chapters/*.tex" --out writing_style_ref/vocabulary-check-chapters.md`.
""")

print(f'Built {len(compiled)} patterns from {len(SOURCE_ENTRIES)} source entries, {len(review_items)} review decisions '
      f'({totals["by_hang"]} by Hang), {len(INSTRUCTIONS)} instructions, and {len(HAND_EDITS)} hand edits.')
print('Category counts:', dict(Counter(e['category'] for e in compiled)))
print(f'Evidence cited: {len(cited_in)}. Strong review decisions cited: {sum(v in cited_in for v in hang_strong)} of {len(hang_strong)}.')
