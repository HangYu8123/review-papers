# Hang's reviewing voice

Use a restrained, professional register in plain English. Follow Hang's current instructions first, then the facts and definitions, then explicit past edits and decisions, then guideline.md and style_guide_portable/writing-style-guide.md. The raw reviews and older writing_style_ref/ supply examples rather than a requirement to repeat their phrasing.

## Voice and tone

Use the authors, the method, the experiment, or the results as the subject. First person is appropriate for a personal concern, the recommendation, and the requested expertise caveat, but should not frame every judgment. Do not use "we" for the reviewer.

State what the evidence establishes. Replace "As far as I know" and "new to me" with a bounded description of the contribution. A small literature search supports a comparison to the works examined, not a claim about the whole field. Put the search limits in the evidence. Replace "I worked through the equations" with the relevant conclusion, and retain the derivation in the evidence.

Be considerate through accurate acknowledgment and proportionate requests. Prefer "Please clarify ...", "The comparison would be stronger with ...", and "It would help to ...". Avoid "I would love to see", repeated "I appreciate", "a bit", "quite", and conversational fillers. Acknowledging uncertainty does not require a first-person hedge. For example, write "The number of training runs is not reported" rather than assuming that each model was trained once.

## Section forms

**Summary.** Open with "In this work, the authors proposed [method] for [problem]." Explain the central approach and contribution in about three sentences. A second paragraph gives the evaluation setting and main result in one or two sentences. Usually keep the whole summary to 80 to 140 words and the second paragraph to 45 words or fewer. Avoid a second statement of novelty and lists of implementation details or timings.

**Strengths.** Give the specific contribution and one reason it matters, usually in one or two sentences and 25 to 60 words. One supporting fact is enough; the evidence carries detailed comparisons. Shorter points are fine when complete.

- "The method reduces repeated computation by reusing intermediate results."
- "The ablation study isolates the contribution of the proposed component."

These are examples of sentence form. Use them only when the current paper supports them. Put derivations, condition-specific values, and additional results in the evidence. A strength needs neither a field-wide novelty claim nor a speculative closing sentence about other applications.

**Weaknesses.** State one concern, one decisive example with its location, and the implication or needed clarification. Usually use two or three sentences and 40 to 90 words. Credit a controlled comparison or acknowledged limitation before explaining the remaining concern. Use "My largest concern is" only when that concern drives the recommendation. Do not repeat all of a table or bundle unrelated concerns to save a bullet.

**Areas for improvement.** Give one or two proportionate actions, usually in two or three sentences per point. Prefer clarifications and analyses of available data. Offer narrowing a claim when that resolves the gap, and mark new training or robot experiments as optional when recommending minor revisions. Do not assume work is cheap because a component already appears in a figure.

**Overall recommendation.** Use one short paragraph, usually three or four sentences. Give the main strength, the deciding concern, the recommendation using the venue's options, and the requested expertise caveat. For example, "Thus, I recommend accepting the paper with minor revisions. While I am not an expert in this field, I would not argue if my recommendation largely disagrees with other reviewers'." Preserve this first-person judgment without carrying that voice through the technical points.

## Sentence rules

Read the portable guide's Core philosophy and Quick reference before drafting, and consult its sections on claims, sentence style, and editing while revising. Use style_guide_portable/vocabulary.md for unfamiliar wording. The following rules are the ones most often needed in reviews.

1. Name the actor and use a concrete verb. Keep the paper's defined names for methods, metrics, and datasets.
2. Give each sentence one main job. Keep a governing condition with its claim and a result with its interpreting clause.
3. Use few colons and semicolons, and no em dashes. State the relation with because, since, which, or a new sentence.
4. When a number is essential to the review text, keep its measure, baseline, and condition with it. Distinguish percentage points from relative percentages. Move secondary values into the evidence instead of leaving a vague numerical claim.
5. Report observations directly, qualify interpretations, and mark untested explanations as possibilities. Use can for a supported capability and may or might for a possible explanation.
6. A difference that was not detected does not establish equivalence. Use significantly only for a supported statistical claim. A descriptive word such as comparable can be clarified by stating the measured tradeoff.
7. Use literal wording and complete clauses. Avoid inflated praise, figurative summaries, adjective stacks, and closing sentences that merely restate the point.
8. Keep value words next to what earns them. Say robust to what, or replace the adjective with the supported result.

## Editing and evidence

The review text carries the judgment and its essential support. Evidence objects carry the audit: exact values, additional conditions, derivations, calculations, assumptions, related-work comparisons, and decisions about a reference review. Shortening the review must not delete this support.

Preserve Hang's claims, technical terms, and edited wording. Correct an error without unnecessary rewording, and offer optional rewording separately. A rejected proposal should not return unchanged. If Hang wants to write the fix, let that wording replace the proposal and check it against the same principle. If a passage already works, leave it alone.

Before handoff, read the review text without the evidence. Each point should be understandable on its own, while the second summary paragraph stays within one or two sentences. Then read the evidence to confirm that compression did not overstate a result or hide an assumption.
