# Applying the writing references to a paper review

Keep the review method in [SKILL.md](../SKILL.md) and the substantive expectations in [the advisor's guide](advisor-guide.md). These remain the foundation. The style collections help choose the wording of a proposed revision and the explanation that accompanies it. The portable guide in this skill's `style_guide_portable/` covers ordinary reviews. The two full references in the shared folder `../../paper-review-shared/` are large source libraries, so open them only for the rows of the table below that name them.

## Read by purpose

| Decision | Read |
| --- | --- |
| Ordinary tone, claim wording, minimal editing | [Portable writing guide](../../writing-style-portable/writing-style-guide.md), especially Core philosophy, Quick reference, and Editing someone else's text |
| Technical word choice and stable meanings | [Portable vocabulary](../../writing-style-portable/vocabulary.md); use [the full technical vocabulary](../../writing-style/writing_style_ref/tech-vocabulary.md) for examples and sources |
| A preference needs explanation or appears to conflict with the summary | The relevant entry in [Hang's full reference](../../writing-style/writing_style_ref/hangs-writing-style-reference.md), then its linked evidence |
| A sentence was reviewed before | [Review index](../../writing-style/writing_style_ref/review-decisions.md), the relevant record in `writing_style_ref/reviews/`, and the current paper's own decision record |
| Strength or origin of a preference | [Preference signals](../../writing-style/writing_style_ref/preference-signals.md); [source map](../../writing-style/writing_style_ref/source-map.md) for how patterns were merged |
| Committee-facing clarity, study reporting, or a long document | The relevant entry in [the committee reference](../../writing-style/committee_style_ref/committee-writing-style-reference.md); [field conventions](../../writing-style-portable/field-conventions.md) for the broader comparison |
| Evidence of a writing pattern | [Hang's paper excerpts](../../writing-style/writing_style_ref/source-evidence.md) or [committee excerpts](../../writing-style/committee_style_ref/source-evidence.md); [writer profiles](../../writing-style/committee_style_ref/writer-profiles.md) for approximate measures |
| Structured lookup across many patterns | The relevant `library.json` in `writing_style_ref/` or `committee_style_ref/`; avoid loading both in full for a small review |

Read the starting passages of the portable guide specified in SKILL.md before proposing wording. When a row sends you to a full reference, search headings or pattern names to retrieve only the detailed entries needed. Examples of useful searches are `Qualifying a result`, `Few colons and semicolons`, `Impersonal dissertation voice`, `Contribution statements`, and `A difference that was not found`.

## Resolve conflicts by kind

The current user's instructions and the passage's facts, measurements, definitions, and intended meaning come first. Neither the advisor's guide nor a style example supplies missing study facts.

For the review's argument chain, section purposes, figure checks, pacing, and decisions, use SKILL.md and the advisor's guide. Treat the guide's conference-paper lengths and structures as defaults scaled to the actual venue and genre.

For wording, prefer the current author's explicit choices. When reviewing Hang's writing, the recorded evidence has this order:

1. An explicit instruction from Hang (weight 5).
2. A hand edit or an accepted suggestion that Hang edited (weight 4).
3. A declined suggestion (weight 3). A note adds weight 2 to its decision.
4. A suggestion accepted as written (weight 1).
5. The portable summary, then field conventions and published examples.

Delegated or inferred decisions have weight 0 and are not evidence of Hang's preference. These weights describe the source library's evidence; do not compute a new numerical score for each proposed edit. A rejection establishes what was declined in that context, not a universal ban on a word. The current paper's explicit decisions take priority over a reusable pattern.

Committee dissertations show how their authors wrote at a particular time. They do not establish what those people require from a student now. In particular, do not import first person, stronger value words, or heavier punctuation from their quotations when those conflict with the author's stated preference.

For another student's paper, preserve that student's definitions and established voice. Use Hang's patterns as guidance for concrete wording and careful editing, not as evidence that the student shares Hang's past choices.

## Apply the guidance in a proposal

- Keep the original excerpt verbatim, including LaTeX, citations, spelling, and punctuation. Distinguish a proposed correction from the original.
- Prefer moving, cutting, or correcting existing wording. Give optional rewording its own proposal so it can be declined without losing a necessary correction.
- Name the actor and the operation. Explain a method through its inputs, computation, and outputs before describing its benefits. Do not use synonyms to vary a defined technical term.
- Preserve counts, units, scales, conditions, statistical results, and citations. When a required fact is missing, identify the gap and ask for that fact rather than drafting it from an example in the reference library.
- Keep observation, interpretation, and possible explanation distinct. An association does not establish causation. A nonsignificant comparison does not establish equivalence. Do not routinely weaken a supported positive finding, remove `significantly`, or add a new caveat sentence.
- Give a quantitative comparison its measure, baseline, and available uncertainty. Use the analysis actually reported; do not impose a significance cutoff or infer a future significant result from the guide's illustrative statistics. If inferential details are unclear, flag the missing information for the author.
- Keep a governing condition attached to its claim and a result attached to the clause that interprets it. Sentence or paragraph length is a diagnostic, not a reason by itself to split.
- Prefer literal relations such as `suggests`, `is associated with`, and `helps explain`. Avoid ornamental academic wording, figurative summaries, and value words without supporting results.
- Use few colons and semicolons, and replace em dashes in new proposed prose, following the portable guide's exceptions for lists, quotations, equations, citations, and headings. Do not alter quoted source passages to enforce this preference.
- Choose voice by genre. A conference paper can use `we` for the authors' actions; an algorithm is the subject of its computations. A thesis or dissertation normally uses the impersonal voice described in Hang's reference. Slide and film patterns do not govern paper prose.
- Treat vocabulary familiarity as evidence of Hang's usage, not of the intended reader's knowledge. Define a term when the audience needs it, even if it is marked Core or Familiar. An unlisted term is not automatically wrong.
- Avoid adding closing links, limitations, or subsections that the author did not ask for. Propose a minimal addition when a fact or argument link needed to understand the existing work is missing. Label unresolved content as a question rather than inventing it.
- Check earlier decisions before revisiting a sentence. Do not submit a declined edit again as a new proposal. If a new concern requires revisiting it, state the concern as a question and preserve the author's decision until they change it.

Keep structural reasons tied to the advisor's guide and wording reasons tied to a named style principle. A short reference such as `Advisor guide, Introduction` or `Portable guide, Correct without rewording` is enough. Do not add evidence weights, library maintenance details, or long source quotations to each student-facing card.

If the paper needs cuts, use the guide's sequence of content editing, cleanup, and final layout adjustments. Do not remove a result merely because it is nonsignificant or change which hypotheses appear supported. Show the exact proposed cut and its effect on the argument for the author to decide.

## Scope of the bundled sources

This skill carries `style_guide_portable/`. The shared folder `paper-review-shared/` holds `writing_style_ref/` and `committee_style_ref/`, including their evidence and source snapshots, for both this skill and the `review-paper` skill. The review can use this guidance without access to the original dissertation project.

The larger libraries are historical source collections. Their README files, validation reports, source records, and build scripts may refer to an earlier dissertation folder, original PDFs, or paper source files that were not provided here. Those paths are provenance, not required inputs to a paper review. Do not claim to have opened a PDF that is absent. Use the bundled excerpts and extracted texts when checking a writing pattern; request the original only when the task needs it. Do not run library rebuild, import, or extraction scripts as part of an ordinary review.

Use the supported review helpers in `scripts/structure_scan.py` and `scripts/figures.py`, and the editing and review templates, as described in SKILL.md. The source libraries, the templates, and the installed skill are reference material; save new papers, decisions, and review outputs in the task's own directory.
