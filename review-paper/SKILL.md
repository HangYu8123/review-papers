---
name: paper-review
description: Draft or revise a peer review of any research paper in Hang's reviewing style, with an interactive review page where each point includes evidence and can be accepted, edited, or rejected. Use when asked to review, referee, critique, or assess a manuscript, draft reviewer comments, fill a venue's review form, or revise a review from saved decisions. Follow the writing guide and review guidelines, and verify any reference review against the manuscript.
---

# Paper review

The output is a draft for Hang to judge, not a finished review. Hang reads each point in the review page, looks at the evidence right under it, and accepts, edits, or rejects it. So two things matter most. Every point must be correct about the paper, because a wrong claim in a review is unfair to the authors and costs Hang credibility. And every point must show its evidence, so Hang can decide in seconds instead of re-reading the paper.

Apply this workflow to the paper being reviewed. Determine its contributions, terminology, evidence, venue, and review identifier from the supplied materials. Do not carry a previous paper's methods, datasets, results, criticisms, or recommendation into a new review.

Paths below are relative to the repository root, the folder that holds `guideline.md`. `SKILL_DIR` is the folder containing this `SKILL.md`, currently `paper-review/`.

## Inputs and outputs

| What | Where |
| --- | --- |
| Manuscript | The paper PDF in the paper folder. If the folder has several PDFs and it is unclear which is the manuscript, ask. |
| Reference review, optional | Usually `<paper>/review.pdf`, or a file the user names. Treat it as a second opinion to verify against the manuscript. |
| Rules | Hang's current instructions, `guideline.md`, `style_guide_portable/writing-style-guide.md`, `previous_reviews/previous_reviews`, `writing_style_ref/` |
| Page | `review_template/review.html`. Its header comment (lines 1 to 110) is the specification of `review-data.js`. |
| Output | `<paper>/review/review.html`, an unchanged copy of the template, and `<paper>/review/review-data.js` |

When Hang asks to revise an existing review, update that review in place, preserving saved decisions and Hang's wording. Before replacing an existing review with a fresh draft, ask whether to replace it or write to `<paper>/review-<YYYYMMDD>/` instead.

Treat the manuscript as confidential, since review copies are marked "For review only". Search the web for related work by topic and title, but never paste manuscript text into a web form, a search engine, or an external tool.

## Workflow

### 1. Read the whole paper

Extract the text with page markers into the scratchpad, then read all of it, including the appendix and any supplement.

```
python SKILL_DIR/scripts/pdf_pages.py <paper>/<manuscript>.pdf <scratchpad>/paper.txt
```

Text extraction scrambles tables and loses figures. Open every page that has a results table or a key figure with the Read tool (for instance `pages: "5-6"`) and read the numbers from the page image. Any number that goes into the review should come from a table or figure you looked at.

While reading, keep notes in `<scratchpad>/notes.md`:

- **Claims**, quoted with location, from the abstract, the contribution list, and the conclusion.
- **Method**, separating what is new from what is taken from earlier work.
- **Experiments**, each with environment, workload (scenes, trials, runs, seeds), baselines, metrics, headline numbers, and location.
- **Limitations the authors state themselves.**
- **Venue and submission id**, usually in the page header, and the review form options if known.

### 2. Check the claims against the evidence

This step produces the weaknesses, so spend real time on it. For each claimed contribution, ask what supports it, whether that support isolates it (an ablation, a controlled baseline), whether it is tested in the setting the claim names (real robot or simulation, the objects or users it claims), how large the test is, and whether uncertainty is reported. Recompute derived numbers such as speedups, ratios, and percentages from counts. When the method's validity rests on a derivation or an equation, work through it instead of flagging it as unclear.

Read [references/calibration.md](references/calibration.md) before drafting any weakness. It lists the ways earlier drafts went wrong, such as claiming the paper omits something it states, or treating a rough calculation as proof of a discrepancy.

### 3. Look at the closest related work

To judge novelty and whether a method is outdated, find the two to four closest prior works with the available web tools (arXiv, project pages), and read at least their abstracts and method overviews. Describe the specific difference supported by those sources. A limited search does not support "first" or a field-wide claim. Put the search scope and any uncertainty in the evidence; do not replace them with "new to me" or "as far as I know" in the review. If there is no web access, record that limit in the evidence and avoid an unsupported novelty claim.

### 4. Check the reference review, if there is one

List each of its points and decide whether it holds, partly holds, or does not hold (a misreading, already addressed in the paper, or minor). Verify by searching `paper.txt` and by checking the passage, derivation, or table it refers to. Check alleged omissions and errors, the venue, generic praise, and requests for additional analyses. Use verified points in your own words, and record each decision in the `reason` of the related evidence, such as "The reference review's missing-control concern is supported by the study design." List the dropped points, with why, in the evidence of the recommendation.

### 5. Read the rules

- `guideline.md` in full. It sets the sections, their order, and the rules for each one.
- `previous_reviews/previous_reviews` in full. It shows Hang's voice and the recommendation template.
- `style_guide_portable/writing-style-guide.md`, starting with Core philosophy, Which guidance wins, and Quick reference, then the sections on claims, sentence style, and editing. Use its companion `vocabulary.md` for word choice. Consult `field-conventions.md` only when useful for the document being reviewed; dissertation structure and casual slide language do not set the style of a peer review.
- [references/review-voice.md](references/review-voice.md), which distills Hang's reviewing voice and the sentence rules from the style reference that apply to reviews.
- `writing_style_ref/hangs-writing-style-reference.md` when more source evidence is needed. Hang's current instructions and the portable guide take precedence over older examples that are casual, verbose, or heavily first person. Use "the authors", the method, or the results as the subject by default. Keep first person for a personal concern, a recommendation, or the requested expertise caveat.

### 6. Draft the five sections

Write the items in this order, with these ids: `summary-1`, `summary-2`, `strength-1` ..., `weakness-1` ..., `improvement-1` ..., `recommendation-1`.

**Summary** (one or two short paragraphs, usually 80 to 140 words total). Summarize the contributions fairly instead of repeating the claimed list. The first paragraph names the problem, approach, and central contribution in about three sentences. Merge claims that are one idea at two levels of detail, and omit implementation details. Hang's summaries open with "In this work, the authors proposed ...". A second paragraph, if needed, gives the evaluation setting and main result in **one or two sentences**, usually no more than 45 words. Omit metric lists, secondary timings, and a repeated novelty judgment. If a quantitative comparison is essential, give one comparison with its measure, baseline, and condition.

**Strengths** (about three to six points). Lead with what is new and why it matters, then what the community gains, then rigor and clarity. Usually use one or two sentences and 25 to 60 words per point, with one supporting fact. Explain what an ablation establishes without reciting its rows. Put exact values, extra conditions, equation checks, and related-work comparisons in the evidence. Do not narrate the review process with "I worked through" or "I checked". Generic praise needs the fact that earns it.

**Weaknesses** (usually three to five points, most important first). Focus on what is really insufficient, such as unclear contributions, insufficient evidence for a claimed contribution, or wrong or very outdated methods. Ignore minor issues, such as typos, one more sensitivity sweep, or a missing citation that changes nothing. Use at most two points of the "more baselines" or "more recent work" kind. Use a restrained and considerate tone, usually two or three sentences and 40 to 90 words. Each point states one concern, gives one decisive example and location, explains which claim it affects, and briefly says what would resolve it. Credit what the authors already did or acknowledged. Move additional examples and calculations into the evidence. Use "My largest concern is" only for the point that really drives the recommendation.

**Areas for improvement** (one or two points, usually two or three sentences each). Say what would make the paper better or acceptable with a reasonable workload. This is different from a weakness. A weakness says what is missing or wrong, and an improvement says what to do. Prefer actions that use what the authors already have, offer a cheaper path next to an experiment (such as narrowing a claim), and mark larger work as optional. Do not claim that a piece of work is small unless the paper shows it. Prefer "Please clarify ..." or "The comparison would be stronger with ..." to conversational requests such as "I would love to see ...".

**Overall recommendation** (one paragraph). Follow the template in `previous_reviews`. Briefly summarize the review, give the recommendation and its reason in one short sentence, and end with the not-an-expert line, such as "While I am not an expert in this field, I would not argue if my recommendation largely disagrees with other reviewers'." Read and use the venue's own decision options. If the recommendation is a judgment call, say so in its evidence and name the alternative.

Categories (subheadings) are optional on strength, weakness, and improvement points, and only when the section has three or more points. The template header lists the category names.

### 7. Write the evidence for each item

Every item gets one to five evidence objects, which the page shows right after the point.

- `where`: the location, such as "Sec. III, p. 4" or "Table 2, ablation rows, p. 5".
- `text`: what the paper (or the external source) says. Quote exactly, in quotation marks, when quoting.
- `reason`: the step from the evidence to the wording of the point. Put calculations, assumptions, equation checks, detailed ablation values, search limits, and reference-review decisions here, so the review text stays short. Retain these details when shortening a point.
- `source`, which the Connections tab counts:
  - `claims`, `method`, `experiments`, `baselines`, or `presentation` for the paper
  - `prior` or `field` for external work, with `url`
  - `guideline`, `previous`, or `style` for Hang's rules
  - `summary`, `strength`, `weakness`, or `improvement` for another part of this review

The first evidence of a point is usually the paper location that supports it. Cite a rule (`guideline`, `previous`, `style`) only when it explains a choice Hang might question, such as a dropped reference-review point or a hedged word.

### 8. Draft the state machine of the paper

After the five sections, map the argument of the paper, not its pipeline. The specification is in the header comment of `review_template/review.html` (the `machine` fields and "How to write the machine"), and [references/data-format.md](references/data-format.md) has a worked example. In short:

1. One intuition state, then two to four contribution states, judged as fairly as in the summary.
2. For each contribution, the work states that carry it (modules, derivations, systems, datasets), with `where` and `novel` only on what is new.
3. One experiment state per experiment that matters, with the environment and total workload in `sub`, and transitions from the work it tests, labeled with the result. Set `weak` when the experiment does not isolate that work, is simulation-only for a real-world claim, or is too small.
4. Context states only when they explain the paper or expose an important weakness.

Use about 8 to 16 states, listed by role in that order, and link each state to the review points about it in `points`.

### 9. Verify before writing the files

Reread the draft as a skeptical co-reviewer who wants to catch you being unfair or wrong. Go through the checklist at the end of [references/calibration.md](references/calibration.md). In short, search `paper.txt` for every quote, check every number against the table image, grep for synonyms before writing that the paper does not state something, redo every calculation, and make sure each request is proportionate to the recommendation. When a point fails, fix or drop it. Do not keep a flawed point and hope Hang catches it.

### 10. Write the files and check them

1. Create `<paper>/review/` and copy `review_template/review.html` into it unchanged. Copy it fresh each time, since the template is the newest version of the page.
2. Write `<paper>/review/review-data.js`. The first line is a comment naming the venue and submission. Then `window.REVIEW_DATA = { ... }` and a final line with `;`. The part from the first `{` to the last `}` must be strict JSON (double quotes, no trailing commas, no comments), because `writing_style_ref/tools/import_review.py` reads it that way. Set `review_id` to a unique identifier derived from this paper's title or submission id, `generated` to the current local time, and `paper` to `{ "id": ..., "venue": ... }` from the supplied manuscript and review form.
3. Run the checker and fix every error. Read each warning and fix it unless there is a reason not to.

```
node SKILL_DIR/scripts/check_review.js <paper>/review/review-data.js
```

4. Open the page for Hang, for instance with `Start-Process "<full path>\review.html"` in PowerShell.

### 11. Hand off and wait

Tell Hang, briefly:

- the path of the page, and how many points each section has;
- the recommendation, and the alternative if it was a judgment call;
- the two or three points you are least sure about, so Hang can start there;
- which reference-review points were dropped, in one line;
- for venue form fields the page does not hold (scores, confidence, questions for the authors, limitations), suggested values in the chat if the venue's form needs them, following how Hang filled them in `previous_reviews`;
- if the venue form asks about LLM use in reviewing, that the answer there needs to reflect how this draft was made.

Then wait for Hang's decisions. Do not write a final review elsewhere or submit anything.

## Revising after Hang's decisions

The page's "Save decisions" button downloads `<review_id>.decisions.<timestamp>.json`, usually into Downloads. When Hang brings one back, or says which points to change:

- An accepted point stays as it is. A point with `revised_override` takes Hang's text as its new `revised`, since that is Hang's own wording. A rejected point with a `comment` is rewritten as the comment asks, or dropped. A reference with `verdict: "disagree"` and a note means the evidence or the point is wrong, so fix it.
- Read all relevant saved batches in time order, with later decisions taking precedence. Hang's edited wording carries more weight than an acceptance without edits. Do not infer pending decisions unless Hang asks; when asked, record inferred decisions separately from explicit choices and explain the basis. Preserve claims, data, citations, and terms, make each change as narrow as possible, and do not propose a rejected change again without addressing the rejection.
- Keep the ids of unchanged items. The page drops a saved decision only when the text or evidence under it changes, so unchanged points keep their decisions.
- Update `generated`, rerun the checker, and summarize what changed.
- Hang's edits and rejections are the strongest evidence of the reviewing style. If Hang wants them kept, offer to put the decisions file in the review folder and run `python writing_style_ref/tools/import_review.py <paper>/review`, and ask before running it, since it changes the style reference.
