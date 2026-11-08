# Review template

One shared page for every "list the changes, let me accept or reject, apply later" task. A review is a folder under `waiting_for_review/` that holds a list of items; this folder turns that list into the Markdown list and the review page, and later applies the decisions.

| File | What it is |
| --- | --- |
| `review.html` | The page. It looks like the deletion review and edits like the discussion review. Copied unchanged into each review folder. Change it here, never in a copy. |
| `build_review.py` | Reads a review's `items.txt`, and `disagreements.txt` if there is one, and writes its `suggestions.md`, `review-data.js`, `requests.json` and `review.html`. |
| `apply_decisions.py` | Applies the saved decisions to the `.tex` files and records what changed and why in `change-record.md`. Dry run unless `--write`. |
| `review_lib.py` | Code shared by the two scripts. |
| `second-agent-brief.md` | Instructions for a second agent that looks over a built review and adds its disagreements. |
| `example/` | A seven-item review of a toy document in `example/sample/`, with a second agent's disagreement on five items. Safe to play with. |

## The steps

1. **Write the request and the items** in `waiting_for_review/<name>/items.txt` (format below). Record the question or request word for word, and say which request each item addresses. `<name>` becomes the review's id, so use letters, digits and hyphens.
2. **Build**, from the dissertation folder:
   ```
   python waiting_for_review/_template/build_review.py waiting_for_review/<name>
   ```
   It finds each passage in the `.tex` files, fills in chapter, section and line, and reports any item whose passage is missing or not unique. Fix those and build again.
   If you want a second agent to look it over, this is the moment. See [A second agent's disagreement](#a-second-agents-disagreement).
3. **Review**: open `waiting_for_review/<name>/review.html`. Accept, reject, edit the wording or leave a note, then click **Save batch**.
4. **Apply**, as often as you like:
   ```
   python waiting_for_review/_template/apply_decisions.py waiting_for_review/<name>            # dry run
   python waiting_for_review/_template/apply_decisions.py waiting_for_review/<name> --write    # edits the .tex files
   ```
5. **Read the record**: `waiting_for_review/<name>/change-record.md` lists what changed, under the request each change was made for.

Rebuilding is safe at any time. Decisions are stored by item id and are dropped only for an item whose text changed. Adding or changing a request does not count as changing an item's text, so saved decisions are kept.

## On the page

Each card shows the original passage and the proposed text side by side, with the reason underneath.

When an `items.json` item contains optional `repetition` evidence, its card first shows the repeated passages, their locations, the shared wording, and the keep/delete/shorten recommendation. This metadata is also included in Markdown and searchable on the page. It does not affect passage application or decision hashes. Its fields are `shared`, `match`, `action`, `target_label`, and `occurrences`; each occurrence supplies `original`, `file`, `line`, `line_end`, `where`, `role` (`keep`, `delete`, `shorten`, or `other`), and a visible `label`. Existing reviews without this metadata retain their regular layout.

- **Accept / Reject / Reset.** Click a pressed button again to undo it.
- **Accept the rest / Reject the rest.** Decide every remaining undecided item in the review, including items hidden by chapter, decision, change type or search filters. Earlier accept and reject decisions, notes and saved wording are kept. The confirmation shows how many items will be decided; the buttons are disabled when nothing remains undecided. **Accept all shown / Reject all shown / Reset all shown** changes only the items in the current list.
- **Edit the wording** opens the suggested LaTeX in place of the proposed text. **Save wording** keeps your version without changing the decision; **Save and accept** does both. You can edit before or after deciding, and **Reset to the suggestion** goes back. Your wording is what gets applied. On a deletion, editing lets you keep a shorter version instead of removing the passage.
- **Two options.** An item a second agent disagreed with has the original across the top and option A and option B side by side below it, each with its own reason. **Accept A** or **Accept B** (keys `A` and `B`) chooses one. **Reject both** leaves the original. If option B is to leave the passage as it is, the button says **Keep the original (B)** instead. Each option can be edited separately. **Accept the rest** and **Accept all shown** skip these cards, because accepting needs a choice. **Reject the rest** and **Reject all shown** include them, since neither option is then written. "With two options" in the decision filter lists them.
- **Add a note** attaches a comment to an item, with or without a decision. Notes are saved in the batch and printed when the batch is applied.
- **Readable / Changes / LaTeX** switch between simplified prose, the differences marked word by word on the LaTeX source, and the exact source that will be written, tags included. The choice is remembered.
- **Highlight differences** (ticked by default, key `H`) works in the Readable view. Where an item rewords existing text, the words that were removed are tinted in the original and the words that were added are tinted in the proposed text, so a small edit in a long sentence is easy to find. On a card with two options, each option is tinted where it differs from the original and also underlined where it differs from the other option. A citation that changed shows its keys instead of "[citation]". A deletion or an insertion has no second wording to compare, so nothing is tinted there. If the two versions read the same and differ only in the source (line breaks, a comment, a label), the card says "differs in the LaTeX only". Inside a stretch that was rewritten, a short word that happens to occur in both versions is tinted with the rest.
- The sidebar filters by chapter and shows how many items in each are decided. The filters above the list narrow it by decision, change type, or search text; "Not saved yet" shows what the next batch will contain.
- **Saved batches** lists every batch, where its file is, and whether it has been applied.

## Saving decisions in batches

You do not have to decide everything at once. Each click on **Save batch** writes the decisions made since the previous batch to one file in the same folder as the page:

```
waiting_for_review/<name>/<name>.decisions.20261011-141500.json
```

The name carries the date and time the batch was saved. Inside, `saved_at` is the batch time and each decision has its own `decided_at`. A decision changed or cleared after it was saved goes into the next batch, and the later batch wins.

A browser may only write to a folder you point it to, so the first save asks for the folder (the page shows its path, with a button to copy it). The page refuses any folder other than its own. After that it writes there directly; after a browser restart it may ask once for permission, not for the folder. In a browser without this ability (Firefox, Safari) the batch is downloaded instead, and the apply step moves it from Downloads into the review folder.

Unsaved decisions are kept in the browser, so closing the tab loses nothing. Opening the page in another browser and choosing the folder reads the saved batches back.

## Applying

`apply_decisions.py` reads every batch in time order. For each item:

- **accepted**: the passage becomes the revised text (your wording, if you edited it), wrapped in `\hang{<type> start}` and `\hang{<type> end}`. On an item with two options, it becomes the option you chose.
- **rejected**: the passage stays as the original. If the change was already in the text, the original is put back.
- **undecided**: left as it is.

It is safe to run after every batch: what is already in place is recognised. Changing your mind between option A, option B and rejecting both also works, including after an option that removed the passage has been applied. A passage is changed only when it is found exactly once (line wrapping aside); anything else is reported and skipped. Each file is copied to `<name>/backups/<time>/` first. `--batch 20261011-141500` limits a run to one batch; a batch that a later batch has overruled is not applied on its own. Notes left on the page are printed at the end of the run.

After a run with `--write`, the page shows which items are in the dissertation and which batches were applied.

## Requests and the change record

A review records why it exists, separately from the page. The page and `review-data.js` carry none of this, so they look and behave the same with or without it.

| File | Written by | What it holds |
| --- | --- | --- |
| `items.txt` | you | The `@request` records, word for word, and a `request:` line on each item. |
| `requests.json` | the build | The requests and a map from each item to its requests. Only the apply step reads it. |
| `suggestions.md` | the build | The requests at the top, and a **Request** line on each item. |
| `change-record.md` | the apply step | The changes, grouped by request. |
| `change-record.json` | the apply step | The same changes as data. It is only added to, never rewritten. |

For each change, the record gives the item, its location, what was done (replaced, inserted, removed, put back), the exact text before and after, whether the wording was yours, the reason on the item, your note, the batch, the time and the backup folder. A table at the top counts, per request, what is in the text now, what was rejected, and what is not decided or not applied yet. Rejected items are listed under their request, without before and after text, because nothing changed. Undoing an applied change adds a new entry and keeps the old one, so the history stays complete. Each file is rewritten or added to only by a run with `--write`; a dry run names the requests it would record under.

The record sits in the review folder and moves with it, so it is still there after the review goes to `legacy/`.

## A second agent's disagreement

A second agent can read what was generated and, where it would do something differently, add its own option to that entry. You then see both options on one card and choose.

1. **The second agent reads `suggestions.md`** and checks each entry against the `.tex` file. To ask for this, point a fresh agent at `second-agent-brief.md` and name the review.
2. **It writes `waiting_for_review/<name>/disagreements.txt`** next to the items. It does not edit `items.txt`, so the first agent's wording stays exactly as written and is option A.
3. **Build again.** The build puts each disagreement on the entry it names, in `suggestions.md` and on the page. It reports how many items were looked at and how many were disagreed with.

```
@reviewer
by: Claude Sonnet 5.5
date: 2026-11-02
covers: all

@disagree C3-001
against: 24917304d123
note: The passive keeps "was conducted", which tells the reader nothing.
--- revised
Forty-six participants took part in a study \cite{x}.

@disagree C3-002
against: 22cefb1f9904
action: keep
note: This chapter is the only place that states the order of the clips.

@disagree C3-003
against: d2bf0f67c225
action: remove
note: The next section reports this, so the sentence can go altogether.
```

`by:` and `covers:` are required. `covers:` says what was looked at, `all` or a list of ids, so that silence on an entry is not mistaken for agreement. `against:` is the Version line of the entry in `suggestions.md`, and each disagreement needs a reason in `note:`. An option is another wording in a `--- revised` block, `action: keep` (leave the passage as it is), or `action: remove` (remove the passage, only on an entry that rewords one). Each entry takes one disagreement, so a card never shows more than two options. The second wording replaces the same passage as option A and takes the same tags.

Adding a disagreement is safe at any time:

- **Decisions already saved are kept**, because the disagreement is not part of the item's hash. A decision made before the disagreement arrived still counts. The card is flagged "decided before option B", and the apply step prints a note about it.
- **If the entry changes later**, the build reports the disagreement as written against an earlier version, and the card is flagged, until the second agent has looked again and updated `against:`.
- **If option B changes or is withdrawn after you chose it**, the item is undecided again and the apply step skips it, so a wording you did not see is never written.

To test the second agent's options on a scratch copy, run `apply_decisions.py` with `--accept-all --prefer-second`. Options that leave the passage as it is count as rejected there.

The change record says which option was chosen and by whom, gives the reason for each, and keeps the wording that was not used. A review without `disagreements.txt` builds and behaves as before, and its `suggestions.md` only gains the Version line.

## items.txt

Plain text, LaTeX written exactly as in the `.tex` file. No escaping.

```
@review
title: Pronoun revision review
description: One or two sentences shown at the top of the page.

@request R1
asked: 2026-10-11
by: Hang
--- text
replace first-person pronouns in the results sections

@item C3-001
type: pronoun
file: chapters/charm.tex
request: R1
note: Why this change. Shown on the card and in the Markdown list.
--- original
We conducted a study with 46 participants \cite{x}.
--- revised
A study was conducted with 46 participants \cite{x}.
```

`@request` holds one question or request, in the asker's own words, in a `--- text` block that may run over several lines. Split a message that asks for several things into several requests, so that each item can point to the part it answers. `asked:`, `by:` and `source:` (where it was written down, such as `suggestions/reuth/suggestions.txt`) are optional. Declare requests above the items.

`request:` on an item names what the item addresses:

| On the item | Meaning |
| --- | --- |
| `request: R1` or `request: R1, R2` | The edit addresses these requests. |
| no `request:` line | The review's request if it has exactly one. With several, the build reports the item. |
| `request: none` | Nobody asked for this edit (a side finding, for example). It is recorded as such, so it is never credited to a request it does not answer. |

A review with no `@request` still builds and applies, but the build reports it and the record lists its changes under "Request not recorded".

`type` is the change type. It becomes the tag, so `type: pronoun` is written as `\hang{pronoun start}` ... `\hang{pronoun end}`. A revision on one line gets the tags inline; one with line breaks gets them on their own lines.

What an item does follows from the blocks it has:

| Blocks | Result when accepted |
| --- | --- |
| `--- original` and `--- revised` | The original is replaced by the revision. |
| `--- original` only | The original is removed. With `delete_style: mark` it is kept and wrapped in the tags instead. If the reviewer edits it on the page, the shorter version replaces it, tagged. |
| `--- anchor` and `--- revised` | The revision is inserted after the anchor, a passage already in the file. `position: before` inserts it before. |

Quote enough of the original for it to occur once in the file. Line breaks inside it do not have to match the file.

Optional lines on an item: `title:` (a heading on the card), `tags:` (comma separated), `where:` (replaces the chapter and section found automatically), `group:` (replaces grouping by chapter), `marker:` (tag text, if it should differ from the type), `markers: no` (no tags), `marker_style: inline` or `block`, `sep: space` (for an insert inside a paragraph). Optional lines under `@review`: `type.<type>: Label`, `group.<key>: Label`, `delete_style: mark`, `macro.\name{}: text shown in the readable view`, `root:` (only if the dissertation is not the nearest folder above with a `main.tex`).

Items can also come from `items.json` (`{"review": {...}, "requests": [{"id": "R1", "text": "..."}], "items": [...]}` with the same keys) when a script generates them, or be split over `items/*.txt`.

## Changes already made in the text

If a change was put straight into a `.tex` file between `\hang{<type> start}` and `\hang{<type> end}`, list it the same way: the text before the change as `--- original`, the new text as `--- revised`. The build sees that the tagged revision is in the file and marks the item "already in the text". Accepting it leaves it there; rejecting it puts the original back.

## Checking a reading instead of a change

A review with `mode: check` under `review` holds readings of a source, such as handwriting in a PDF, for someone to confirm. It is written as `items.json`. The items use the same page, batches and notes, with these differences:

- **Accept** means the reading is right. **Edit the wording** corrects it; the corrected text is saved in the batch as `revised_override`.
- `revised` is the reading and `original` is the text it refers to. Both are shown as plain text, so `%`, `_` and `~` in a note stay as written. The Readable, Changes and LaTeX views are hidden.
- The build does not look for the passage in a file, so `file` only names the source.
- **Nothing can be applied.** `apply_decisions.py` says so and stops, even with `--write`. Reading the batches is the next step's job.

Optional keys on such an item, none of which affects its hash: `image` and `image_size` (`[width, height]` in pixels, shown at 72%), `image_label`, `reading_label`, `original_label`, `source_label` (replaces the file and line under the title), `page_image` and `page_box` (`[left, top, right, bottom]` as fractions of the page) for the "See it on the page" view. A tag starting with `unsure` is shown as a flag. The search box also finds tags. `chris-handwriting-review/tools/make_items.py` is a working example.

## What it does not do

Each item is one passage in one file. A change that moves text between files, or that depends on another item being accepted, has to be written as separate items, with the dependency explained in their notes.

A second agent's option replaces the same passage as the entry it disagrees with. A change that needs a wider passage has to be a new item. Two options are not available in a `mode: check` review.
