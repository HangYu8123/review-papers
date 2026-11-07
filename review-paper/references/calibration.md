# Getting the critique right

A review point is only useful if it holds up when the authors read it. Use these checks to keep criticisms accurate, supported, and proportionate for the paper being reviewed.

## Contents

- Claims about what the paper does not say
- Not reported is not the same as not done
- Reading figures
- Calculations built on assumptions
- Statistics
- Crediting a controlled comparison
- Workload and proportion
- Limitations the authors already state
- Reference reviews
- What counts as minor
- Checklist before writing the files

## Claims about what the paper does not say

"The paper does not state X" is the claim most often wrong. Before writing it, search `paper.txt` for X and for its synonyms, and read the section where X would be. Then say exactly what is missing.

Distinguish the absence of a selection criterion from missing details about how a stated criterion was applied. A qualitative criterion can be present even when the selected sample identifiers or exclusion counts are not reported.

## Not reported is not the same as not done

When the paper does not mention training seeds, the number of runs, or matched initial scenes, ask. Do not write as fact that each model was trained once. "The paper does not say how many training runs were used. Please report it, since ..." is fair. "Each variant was trained once" is not, unless the paper says so.

Identical numbers in two rows of a table can be a coincidence. Mention them as something the authors may want to check, if at all, and not as a sign of an error.

## Reading figures

Read values from a figure as "about" and say so. Check the axes, scale, units, and conditions before interpreting a trend. Distinguish growth order from absolute cost: similar slopes on a log-log plot do not imply equal cost per added unit.

## Calculations built on assumptions

Put a back-of-the-envelope calculation in the evidence `reason`, and keep the review text to what the paper establishes. If it depends on unreported assumptions about aggregation, workload, or matched conditions, ask for the missing information before treating the result as a discrepancy. Check whether an aggregate rate can validly be inverted or combined with another reported measurement.

## Statistics

- A z-score from two standard errors assumes the estimates are independent. Methods evaluated on the same objects or scenes are not independent, so call such a number rough, and prefer asking for a paired interval on the difference.
- Do not call a difference significant unless a test was run.
- "Comparable" can describe a practical speed and success tradeoff and need not be a formal equivalence claim. Criticize the vagueness, and suggest reporting the gap next to the benefit, rather than calling the wording inconsistent.

## Crediting a controlled comparison

Matching data and evaluation conditions can provide a defensible controlled comparison. Credit what the comparison establishes, then identify any claim that extends beyond it. A result from another paper can motivate a question about transfer or confounding, but does not by itself invalidate the current paper's comparison.

## Workload and proportion

- Do not write that an experiment is a small amount of work because a component already appears in the paper. A checkpoint used for one figure may take real effort to run in every trial or on a robot.
- Next to an experiment, offer the cheaper fix when one exists, which is often narrowing the claim to what the evidence supports.
- Match the requests to the recommendation. For minor revisions, ask for clarifications and analyses of existing data, and mark retraining or new robot experiments as optional.
- Separate what is needed (clarify the number of runs, the selection procedure, the tuning split) from what would strengthen the paper (more seeds, another baseline).

## Limitations the authors already state

When the authors state a limitation, acknowledge it and raise it only if it undercuts a claim. Then identify the claim that needs clarification or narrower scope.

## Reference reviews

Verify every point of a reference review against the manuscript. Confirm alleged typos, check equations under the paper's conventions, verify venue information, and distinguish a qualitative example from a quantitative comparison. Keep supported criticisms in your own words and record why unsupported points were dropped. A point's origin in a reference review is not itself a reason to keep or discard it.

## What counts as minor

Leave out typos, wording issues that do not change meaning, one more hyperparameter sweep, a runtime breakdown "for practitioners", and missing citations that do not change the novelty. Keep a presentation issue only when it blocks understanding or misstates a result. Keep a missing comparison only when it changes what is new or whether a claim holds, and use at most two points of the more-baselines or more-recent-work kind.

## Checklist before writing the files

Go through every item of the draft.

1. Each quote appears in `paper.txt` word for word. Search for it.
2. Each number matches the table or figure image, with the right row, column, and unit.
3. Each "the paper does not state" has been searched with synonyms, and says exactly what is missing.
4. Each calculation has been redone, and its assumptions are in the evidence, not in the point.
5. Each weakness says which claim it affects, credits what the authors did or acknowledged, and is not minor.
6. No more than two weaknesses ask for more baselines or more recent work.
7. Each improvement is proportionate to the recommendation and offers a cheaper path when there is one.
8. Novelty wording matches the size of the related-work search.
9. Each reference-review point used has been verified, and each dropped one has a reason in the evidence.
10. The tone is one Hang would sign. Read the weaknesses as the authors would.
11. The text follows [review-voice.md](review-voice.md), including no em dashes and few colons and semicolons.
12. The machine's contributions match the summary, and each weak link matches a weakness.
