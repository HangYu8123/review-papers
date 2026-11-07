# Full talk wording review

Review `full-talk-wording-review` of the slides, from `../dissertation_presentation/wait_to_review/full-talk-wording-review`. Decided between October 17, 2026 and October 17, 2026. Decisions files: `full-talk-wording-review.decisions.20261017-212326.json`, `full-talk-wording-review.decisions.20261017-214356.json` (assistant-delegated).

[All reviews](../review-decisions.md) · [Weighted signals](../preference-signals.md) · [Main reference](../hangs-writing-style-reference.md)

| Outcome | Decided by Hang | Not decided by Hang |
| --- | ---: | ---: |
| Accepted as suggested | 55 | 51 |
| Accepted with Hang's edit | 3 | 29 |
| Declined | 16 | 11 |
| Notes from Hang | 0 | |

91 decisions in this review were not made by Hang (assistant-delegated). They are listed with the reason that was recorded for them and carry no weight.

### S03-G01

**Accepted** · weight 1 · Typos and grammar · Slide 3 · Robots belong to the world, not the lab. · Slide 3 — slide text

Suggestion: Complete the comparison and verb phrase

Original:

~~~text
…which means their teaching will be noisier and challenging for robots to learn
~~~

Accepted wording:

~~~text
…which means their teaching will be noisier and more challenging for robots to learn from
~~~

Note written with the suggestion: Grammar-only correction. Add more to make the comparison parallel, and from to complete learn from. Alternative for the same passage: S03-S01. Choose one final version.

Used in: [Correcting a sentence without rewording it](../hangs-writing-style-reference.md#correcting-a-sentence-without-rewording-it), [Slide text in the presenter's voice](../hangs-writing-style-reference.md#slide-text-in-the-presenter-s-voice).

### S03-W01

**Accepted** · weight 1 · Optional wording · Slide 3 · Robots belong to the world, not the lab. · Slide 3 — slide text

Suggestion: Remove mostly only

Original:

~~~text
In labs and data farms: robots mostly only need to interact with or learn from experts.
~~~

Accepted wording:

~~~text
In labs and data farms, robots mainly interact with and learn from experts.
~~~

Note written with the suggestion: Remove the redundant mostly only and state the two activities directly. Style reference: Direct subjects and concrete details.

### S03-W02

**Accepted** · weight 1 · Optional wording · Slide 3 · Robots belong to the world, not the lab. · Slide 3 — slide text

Suggestion: Name the setting directly

Original:

~~~text
Out there: they have to adapt to people with diverse backgrounds and little robot experience.
~~~

Accepted wording:

~~~text
In everyday settings, robots must adapt to people with diverse backgrounds and little robotics experience.
~~~

Note written with the suggestion: Name the setting in place of Out there. Robotics experience is the more natural phrase here.

### S03-S01

**Declined** · weight 3 · Precision and claim scope · Slide 3 · Robots belong to the world, not the lab. · Slide 3 — slide text

Suggestion: Avoid treating diversity as a cause of noisy teaching

Original, which stayed:

~~~text
…which means their teaching will be noisier and challenging for robots to learn
~~~

Declined suggestion:

~~~text
…so robots need to learn from varied, imperfect teaching.
~~~

Note written with the suggestion: Alternative to the grammar-only correction on this text. The original makes diverse backgrounds imply noisier teaching. This version states the learning requirement without that universal inference. Choose one version. Style reference: Describing human teaching without blame. Alternative for the same passage: S03-G01. Choose one final version.

Used in: [Correcting a sentence without rewording it](../hangs-writing-style-reference.md#correcting-a-sentence-without-rewording-it).

### S04-W01

**Declined** · weight 3 · Optional wording · Slide 4 · Why learn from non-experts? · Slide 4 — slide text

Suggestion: Make the training relationship explicit

Original, which stayed:

~~~text
Varied data, like these 34 successful demos, can make models more robust.
~~~

Declined suggestion:

~~~text
Models trained on varied demonstrations, such as these 34 successful examples, can become more robust.
~~~

Note written with the suggestion: Keep can, name what the models train on, and avoid the repetition of models. This remains a possible benefit rather than a measured result of the pictured dataset.

Used in: [Slide text in the presenter's voice](../hangs-writing-style-reference.md#slide-text-in-the-presenter-s-voice).

### S05-S01

**Accepted** · weight 1 · Precision and claim scope · Slide 5 · Non-expert teaching is imperfect · Slide 5 — slide text

Suggestion: Distinguish the scale from how people use it

Original:

~~~text
Everyone has their own scale
~~~

Accepted wording:

~~~text
People use the same rating scale differently
~~~

Note written with the suggestion: All participants used the same numerical scale. The point is that they used its values differently, rather than that each person had a different scale.

### S05-W01

**Accepted** · weight 1 · Optional wording · Slide 5 · Non-expert teaching is imperfect · Slide 5 — slide text

Suggestion: State what demonstrations reflect

Original:

~~~text
Demos carry more than the task
~~~

Accepted wording:

~~~text
Demonstrations reflect the teacher and the task
~~~

Note written with the suggestion: Replace the figurative carry more than the task with the concrete relationship shown by the example. Style reference: Literal wording.

### S05-W02

**Accepted** · weight 1 · Optional wording · Slide 5 · Non-expert teaching is imperfect · Slide 5 — slide text

Suggestion: Clarify the row ordering

Original:

~~~text
45 crowdworkers rated the same 100 robot clips, twice. One row per person, from low to high average rating.
~~~

Accepted wording:

~~~text
45 crowdworkers rated the same 100 robot clips twice. Each row represents one participant, ordered by average rating from low to high.
~~~

Note written with the suggestion: Remove an unnecessary comma and make the row ordering explicit. The participant count and repeated-rating design are unchanged.

### S06-W01

**Accepted** · weight 1 · Optional wording · Slide 6 · Simple assumptions can backfire · Slide 6 — slide text

Suggestion: Describe the processed training data

Original:

~~~text
What trains a better VLA
~~~

Accepted wording:

~~~text
Training data after removing pause frames
~~~

Note written with the suggestion: Replace the informal question-like label with a description of what the image shows. Avoid implying that this particular image alone establishes better performance.

### S06-W02

**Accepted** · weight 1 · Optional wording · Slide 6 · Simple assumptions can backfire · Slide 6 — slide text

Suggestion: Remove unsupported emphasis

Original:

~~~text
Pausing is natural for people, yet removing pause frames can clearly improve VLA models.
~~~

Accepted wording:

~~~text
Pausing is natural during demonstrations. Removing pause frames can improve VLA performance.
~~~

Note written with the suggestion: Use two concrete statements and remove clearly, which adds emphasis without specifying a measure. Keep can and the original claimed benefit.

Used in: [Measured results and plain premises on slides](../hangs-writing-style-reference.md#measured-results-and-plain-premises-on-slides).

### S06-W03

**Accepted** · weight 1 · Optional wording · Slide 6 · Simple assumptions can backfire · Slide 6 — slide text

Suggestion: State the guessing payoff

Original:

~~~text
a guess: 1 point if it is lucky
~~~

Accepted wording:

~~~text
guess: 1 point if correct, 0 if incorrect
~~~

Note written with the suggestion: State the scoring rule rather than describing a correct answer as lucky. This is the rule already described in the notes.

### S06-W04

**Accepted** · weight 1 · Optional wording · Slide 6 · Simple assumptions can backfire · Slide 6 — slide text

Suggestion: Label the response directly

Original:

~~~text
honest: 0 points
~~~

Accepted wording:

~~~text
“I don’t know”: 0 points
~~~

Note written with the suggestion: Label the response being scored rather than treating honest as a category parallel to a guess.

### S06-S01

**Accepted with Hang's edit** · weight 4 · Precision and claim scope · Slide 6 · Simple assumptions can backfire · Slide 6 — speaker notes

Suggestion: Describe the incentive without saying every guess pays

Original:

~~~text
so guessing always pays.
~~~

Suggested:

~~~text
so a guess can earn a point, while ‘I don’t know’ cannot.
~~~

Hang's wording:

~~~text
so the expectation of guess is positive, while ‘I don’t know’ is 0.
~~~

Note written with the suggestion: Under the displayed rule, an incorrect guess also earns zero. Always pays overstates the example. This wording uses only the scoring rule already on the slide.

Used in: [Measured results and plain premises on slides](../hangs-writing-style-reference.md#measured-results-and-plain-premises-on-slides).

### S06-W05

**Accepted** · weight 1 · Optional wording · Slide 6 · Simple assumptions can backfire · Slide 6 — slide text

Suggestion: Name the consequences precisely

Original:

~~~text
Oversimplifying human teaching can mean more data or worse robots.
~~~

Accepted wording:

~~~text
Oversimplifying human teaching can increase data requirements or reduce robot performance.
~~~

Note written with the suggestion: Replace more data or worse robots with the two specific consequences intended. Style reference: Direct subjects and concrete details.

### S07-S01

**Declined** · weight 3 · Precision and claim scope · Slide 7 · Go outside the lab and learn from imperfection · Slide 7 — slide text

Suggestion: Keep the participant description accurate across studies

Original, which stayed:

~~~text
We recruit participants in public spaces and through crowdsourcing, and none of them are robot experts.
~~~

Declined suggestion:

~~~text
We study teaching by passersby and crowdworkers, alongside demonstrations from people with varying levels of robotics experience.
~~~

Note written with the suggestion: The PHIRL appendix describes system developers, expert users, and non-expert users in the real-robot dataset (Dissertation/chapters/appendix-phirl.tex, line 314). Keep the focus on non-expert teaching without saying every participant in the dissertation was a non-expert.

Used in: [Measured results and plain premises on slides](../hangs-writing-style-reference.md#measured-results-and-plain-premises-on-slides).

### S07-S02

**Declined** · weight 3 · Precision and claim scope · Slide 7 · Go outside the lab and learn from imperfection · Slide 7 — speaker notes

Suggestion: Remove the all-participants expertise claim from the notes

Original, which stayed:

~~~text
First, go outside the lab: most of our participants were recruited in public spaces, like the atrium of a university building, or through crowdsourcing, and none of them were robot experts.
~~~

Declined suggestion:

~~~text
First, go outside the lab: we recruited passersby in public spaces, such as a university atrium, and crowdworkers to study non-expert teaching directly.
~~~

Note written with the suggestion: The real-robot PHIRL dataset also includes developers and expert users, as described in Dissertation/chapters/appendix-phirl.tex, line 314. Scope this motivation to the public-space and online teaching studies.

Used in: [Measured results and plain premises on slides](../hangs-writing-style-reference.md#measured-results-and-plain-premises-on-slides).

### S08-G01

**Accepted** · weight 1 · Typos and grammar · Slide 8 · Learning from Both Human Feedback and Human Demonstrations · Slide 8 — slide text

Suggestion: Complete the demonstration-quality clause

Original:

~~~text
Dense, but less accurate locally: demonstrations carry  policy information, but not always optimal framewise.
~~~

Accepted wording:

~~~text
Dense, but less accurate locally: demonstrations carry policy information, but are not always optimal framewise.
~~~

Note written with the suggestion: Grammar-only correction. Add are to complete the final clause and remove the double space before policy information. The optional wording item on this passage is a separate alternative. Alternative for the same passage: S08-W01. Choose one final version.

### S08-W01

**Declined** · weight 3 · Optional wording · Slide 8 · Learning from Both Human Feedback and Human Demonstrations · Slide 8 — slide text

Suggestion: Explain local demonstration quality

Original, which stayed:

~~~text
Dense, but less accurate locally: demonstrations carry  policy information, but not always optimal framewise.
~~~

Declined suggestion:

~~~text
Dense information about how to perform the task, although individual actions may be sub-optimal.
~~~

Note written with the suggestion: Optional alternative to the grammar-only correction on this text. Name the information and explain framewise through individual actions. Choose one version. Style reference: Imperfect teaching and structured behavior. Alternative for the same passage: S08-G01. Choose one final version.

Used in: [Slide text in the presenter's voice](../hangs-writing-style-reference.md#slide-text-in-the-presenter-s-voice).

### S08-S01

**Declined** · weight 3 · Precision and claim scope · Slide 8 · Learning from Both Human Feedback and Human Demonstrations · Slide 8 — slide text

Suggestion: Separate sparsity from feedback accuracy

Original, which stayed:

~~~text
Sparse, but more accurate: it takes less expertise to judge than to perform.
~~~

Declined suggestion:

~~~text
Sparse information about behavior quality. Judging a behavior can require less expertise than performing it.
~~~

Note written with the suggestion: Make the information explicit. The original more accurate does not identify the measure or comparison, and judging a task does not guarantee accurate feedback. Style reference: Information dimensions.

Used in: [Slide text in the presenter's voice](../hangs-writing-style-reference.md#slide-text-in-the-presenter-s-voice).

### S08-W02

**Accepted** · weight 1 · Optional wording · Slide 8 · Learning from Both Human Feedback and Human Demonstrations · Slide 8 — slide text

Suggestion: State the benefit of combining signals

Original:

~~~text
Together they reduce the data need for feedback and relax the quality bar for demonstrations
~~~

Accepted wording:

~~~text
Combining them can reduce the amount of feedback needed and allow learning from sub-optimal demonstrations
~~~

Note written with the suggestion: Replace data need and quality bar with the actual quantities. Keep the benefit conditional rather than presenting it as universal.

### S08-W03

**Accepted** · weight 1 · Optional wording · Slide 8 · Learning from Both Human Feedback and Human Demonstrations · Slide 8 — speaker notes

Suggestion: Explain dense demonstrations in concrete terms

Original:

~~~text
They're dense, every frame is information, but they're locally less accurate, a human hand wobbles.
~~~

Accepted wording:

~~~text
They provide information throughout the trajectory, but individual actions may be sub-optimal, for example when a demonstrator makes a small control error.
~~~

Note written with the suggestion: Explain dense through the trajectory and use the study’s control-error terminology instead of equating demonstration quality with a wobbling human hand. Style reference: Imperfect teaching and structured behavior.

### S08-S02

**Accepted** · weight 1 · Precision and claim scope · Slide 8 · Learning from Both Human Feedback and Human Demonstrations · Slide 8 — speaker notes

Suggestion: Keep the feedback intuition without a general accuracy claim

Original:

~~~text
It's sparse, one number per clip, but more accurate, and judging a behavior takes less expertise than performing it.
~~~

Accepted wording:

~~~text
Feedback is sparse, for example one number per clip. Judging a behavior can require less expertise than performing it, although the ratings can still vary across people.
~~~

Note written with the suggestion: The original makes an unqualified accuracy comparison. This version preserves the intuition while acknowledging the variation introduced on the next slides.

### S09-G01

**Accepted** · weight 1 · Typos and grammar · Slide 9 · Model, mitigate, leverage · Slides 9, 31, 32, 46 — slide text

Suggestion: Remove the comma in the roadmap question

Original:

~~~text
Can we make human feedback more reliable, and more informative?
~~~

Accepted wording:

~~~text
Can we make human feedback more reliable and more informative?
~~~

Note written with the suggestion: Remove the comma between parallel complements. Apply the same punctuation correction to every roadmap copy.

### S09-W01

**Accepted** · weight 1 · Optional wording · Slide 9 · Model, mitigate, leverage · Slides 9, 31, 46, 47 — slide text

Suggestion: Distinguish progress from progress annotations

Original:

~~~text
Can a robot learn good rewards from imperfect demos plus a little progress?
~~~

Accepted wording:

~~~text
Can a robot learn an effective reward function from imperfect demonstrations and a few progress annotations?
~~~

Note written with the suggestion: A little progress can mean a small amount of task completion. Name progress annotations and reward function explicitly. Style reference: Teaching signals and learning quantities.

### S09-S01

**Accepted** · weight 1 · Precision and claim scope · Slide 9 · Model, mitigate, leverage · Slides 9, 31, 32, 46 — slide text

Suggestion: Avoid an unqualified novelty claim

Original:

~~~text
Progress: a new teaching signal
~~~

Accepted wording:

~~~text
Progress as a human teaching signal
~~~

Note written with the suggestion: Replace new with the role of the signal. The writing reference describes progress as under-explored as a human teaching signal, rather than universally new.

### S11-W01

**Accepted** · weight 1 · Optional wording · Slide 11 · One task, many ways to demonstrate it · Slide 11 — speaker notes

Suggestion: State the question without claiming universal agreement

Original:

~~~text
Everyone accepts this. The question is why.
~~~

Accepted wording:

~~~text
The question is what produces these differences.
~~~

Note written with the suggestion: Remove an absolute claim about consensus and state the research question directly. Style reference: Prior work and research gaps.

Used in: [Measured results and plain premises on slides](../hangs-writing-style-reference.md#measured-results-and-plain-premises-on-slides).

### S11-W02

**Declined** · weight 3 · Optional wording · Slide 11 · One task, many ways to demonstrate it · Slide 11 — slide text

Suggestion: Describe the demonstrated variation directly

Original, which stayed:

~~~text
It is widely accepted that human demonstrations are noisy and multi-policy.
~~~

Declined suggestion:

~~~text
Human demonstrations can be noisy and reflect different policies.
~~~

Note written with the suggestion: Replace the appeal to universal acceptance with the property illustrated. Different policies is clearer than the compressed adjective multi-policy for a broad audience.

Used in: [Measured results and plain premises on slides](../hangs-writing-style-reference.md#measured-results-and-plain-premises-on-slides).

### S12-G01

**Accepted** · weight 1 · Typos and grammar · Slide 12 · Human teaching is noisy. But why? · Slide 12 — slide text

Suggestion: Match section-label capitalization

Original:

~~~text
THE Question
~~~

Accepted wording:

~~~text
THE QUESTION
~~~

Note written with the suggestion: Make the section-label capitalization match slide 11.

### S12-W01

**Declined** · weight 3 · Optional wording · Slide 12 · Human teaching is noisy. But why? · Slide 12 — slide text

Suggestion: Remove the universal claim

Original, which stayed:

~~~text
It's widely accepted that demonstrations are noisy, and everyone does the same task differently…
~~~

Declined suggestion:

~~~text
People can demonstrate the same task in different ways…
~~~

Note written with the suggestion: State the variation without widely accepted or everyone. This also avoids treating every difference as noise.

Used in: [Measured results and plain premises on slides](../hangs-writing-style-reference.md#measured-results-and-plain-premises-on-slides).

### S12-W02

**Accepted** · weight 1 · Optional wording · Slide 12 · Human teaching is noisy. But why? · Slide 12 — slide text

Suggestion: Name the operations and their objects

Original:

~~~text
It's random noise: average it out, keep only binary, or filter it away.
~~~

Accepted wording:

~~~text
Treat imperfections as random noise, average across ratings, use binary feedback, or filter demonstrations.
~~~

Note written with the suggestion: Name what is averaged and filtered. Keep the assumption as a modeling choice rather than leaving it and binary without clear referents.

### S12-W03

**Declined** · weight 3 · Optional wording · Slide 12 · Human teaching is noisy. But why? · Slide 12 — slide text

Suggestion: Explain what structure means here

Original, which stayed:

~~~text
Much of it has structure. We can model it, mitigate it, and leverage it.
~~~

Declined suggestion:

~~~text
Some imperfections follow patterns related to the task and the teacher. This dissertation models, mitigates, and uses those patterns for robot learning.
~~~

Note written with the suggestion: Name the source of the structure and avoid treating the proportion much of it as a measured quantity. Style reference: Literal wording and Conditions attached to benefits.

Used in: [Measured results and plain premises on slides](../hangs-writing-style-reference.md#measured-results-and-plain-premises-on-slides).

### S12-W04

**Accepted** · weight 1 · Optional wording · Slide 12 · Human teaching is noisy. But why? · Slide 12 — speaker notes

Suggestion: Remove an unnecessary consensus claim

Original:

~~~text
Everyone in the field agrees that human teaching is imperfect:
~~~

Accepted wording:

~~~text
Human teaching can be imperfect:
~~~

Note written with the suggestion: Remove an unnecessary universal statement about the entire field while preserving the transition into the two examples.

Used in: [Measured results and plain premises on slides](../hangs-writing-style-reference.md#measured-results-and-plain-premises-on-slides).

### S14-W01

**Accepted** · weight 1 · Optional wording · Slide 14 · How sidetracks were identified · Slide 14 — slide text

Suggestion: Clarify the annotation cross-check

Original:

~~~text
Two robot experts built a codebook and annotated every demonstration. A third cross-checked, and behaviors found in both were kept.
~~~

Accepted wording:

~~~text
Two robot experts developed a codebook through open coding and annotated every demonstration. A third expert cross-checked the annotations, and behaviors identified in both passes were retained.
~~~

Note written with the suggestion: Make the open-coding procedure and both passes explicit. These details already appear in the notes. Style reference: Established dissertation terminology.

### S14-W02

**Accepted** · weight 1 · Optional wording · Slide 14 · How sidetracks were identified · Slide 14 — slide text

Suggestion: Keep the pause definition and task-phase terminology consistent

Original:

~~~text
One second or more without input counts as a pause. Changes of task phase were marked to study when sidetracks happen.
~~~

Accepted wording:

~~~text
At least one second without input counts as a pause. Task-phase changes were marked to study when sidetracks occurred.
~~~

Note written with the suggestion: Use the precise pause threshold and the same term for task-phase changes used in later slides.

### S15-G01

**Accepted** · weight 1 · Typos and grammar · Slide 15 · Four kinds of demonstration sidetracks · Slide 15 — slide text

Suggestion: Complete pushing in the wrong direction

Original:

~~~text
A brief, harmless control error, like pushing the wrong direction
~~~

Accepted wording:

~~~text
A brief, harmless control error, like pushing in the wrong direction
~~~

Note written with the suggestion: Add in to complete the direction phrase, keeping the rest of the wording.

### S15-S01

**Accepted** · weight 1 · Precision and claim scope · Slide 15 · Four kinds of demonstration sidetracks · Slide 15 — slide text

Suggestion: Define pauses by the observed input

Original:

~~~text
No input for a while: reacting, thinking, re-planning
~~~

Accepted wording:

~~~text
No control input for at least one second
~~~

Note written with the suggestion: Use the operational definition given on slides 14 and 16. Thinking and re-planning are possible explanations, not directly observed states. Style reference: Observation interpretation and explanation.

### S16-S01

**Accepted** · weight 1 · Precision and claim scope · Slide 16 · Examples of the four sidetracks · Slide 16 — speaker notes

Suggestion: Keep the sidetrack definition separate from its possible role

Original:

~~~text
None of these breaks the task, but none of them makes progress either.
~~~

Accepted wording:

~~~text
These behaviors do not directly advance task completion, although they may help the demonstrator control the robot.
~~~

Note written with the suggestion: Avoid claiming that every sidetrack is harmless or serves no useful role. The later examples describe grip checks and alignment, so the boundary is direct task completion.

### S17-W01

**Accepted** · weight 1 · Optional wording · Slide 17 · Successful, but far from optimal · Slide 17 — speaker notes

Suggestion: Describe trajectory variation plainly

Original:

~~~text
They're super noisy and multi-policy, everyone found their own way.
~~~

Accepted wording:

~~~text
The trajectories vary widely, and people found different ways to complete the task.
~~~

Note written with the suggestion: Describe the visible variation without super or a compressed technical label. The wording remains natural for speaking.

### S17-S01

**Accepted** · weight 1 · Precision and claim scope · Slide 17 · Successful, but far from optimal · Slide 17 — speaker notes

Suggestion: Qualify the interpretation of purposeful behavior

Original:

~~~text
That's noise with a purpose.
~~~

Accepted wording:

~~~text
These behaviors suggest that some apparent noise reflects how people check their control of the robot.
~~~

Note written with the suggestion: Keep the interpretation bounded rather than assigning a measured purpose to every behavior. Style reference: Observation interpretation and explanation.

### S18-W01

**Accepted with Hang's edit** · weight 4 · Optional wording · Slide 18 · Sidetracks follow the structure of the task · Slide 18 — slide text

Suggestion: Let the percentages express frequency

Original:

~~~text
Often happened within 4 s of a sub-task change
~~~

Suggested:

~~~text
Occurred within 4 s of a task-phase change
~~~

Hang's wording:

~~~text
Often occurred within 4 s of a task-phase change
~~~

Note written with the suggestion: The percentages above this label already quantify frequency. Replace often with the event whose frequency was measured and use task-phase consistently.

Used in: [Slide text in the presenter's voice](../hangs-writing-style-reference.md#slide-text-in-the-presenter-s-voice).

### S18-W02

**Accepted** · weight 1 · Optional wording · Slide 18 · Sidetracks follow the structure of the task · Slide 18 — slide text

Suggestion: Keep the alignment percentage with its definition

Original:

~~~text
Alignments started and ended within 0.1 m of a target: where precision matters
~~~

Accepted wording:

~~~text
73% of alignments started and ended within 0.1 m of a target object, where precise control was needed
~~~

Note written with the suggestion: Attach the percentage to the measured event and replace the colon with a connected clause. Style reference: Numbers and measured comparisons.

### S19-S01

**Declined** · weight 3 · Precision and claim scope · Slide 19 · All demonstrators took sidetracks, often at phase changes · Slide 19 — slide text

Suggestion: Keep the random-noise conclusion tied to the observed patterns

Original, which stayed:

~~~text
Random noise injected into perfect demonstrations would not reproduce this structure.
~~~

Declined suggestion:

~~~text
Random noise alone does not capture these patterns in non-expert demonstrations.
~~~

Note written with the suggestion: The study identifies task-related patterns. The original counterfactual would not reproduce this structure is broader than that observation and does not name a tested noise model.

Used in: [Measured results and plain premises on slides](../hangs-writing-style-reference.md#measured-results-and-plain-premises-on-slides).

### S19-W01

**Declined** · weight 3 · Optional wording · Slide 19 · All demonstrators took sidetracks, often at phase changes · Slide 19 — speaker notes

Suggestion: Distinguish the figure from its internal panels

Original, which stayed:

~~~text
the panel on the right shows that pauses take the biggest share of the time.
~~~

Declined suggestion:

~~~text
the companion panel in that figure shows that pauses take the largest share of time.
~~~

Note written with the suggestion: The same notes then say On the right, timing. Clarify that this first reference belongs to a panel within the left-hand figure so the audience can follow the two figures.

Used in: [Slide text in the presenter's voice](../hangs-writing-style-reference.md#slide-text-in-the-presenter-s-voice).

### S20-W01

**Accepted** · weight 1 · Optional wording · Slide 20 · Alignments start and end close to the target objects · Slide 20 — slide text

Suggestion: Describe where alignment occurred

Original:

~~~text
Alignment happened more where controlling the robot required accuracy.
~~~

Accepted wording:

~~~text
Alignments were more common near target objects, where precise control was needed.
~~~

Note written with the suggestion: Name the observed location and replace happened more with were more common. Keep the first two explanatory sentences and all numbers unchanged.

### S22-S01

**Accepted** · weight 1 · Precision and claim scope · Slide 22 · Same task, different ratings · Slide 22 — slide text

Suggestion: Avoid making noise and teacher characteristics mutually exclusive

Original:

~~~text
is it random noise, or is it the teacher?
~~~

Accepted wording:

~~~text
How are teacher characteristics associated with feedback?
~~~

Note written with the suggestion: Replace the either-or question. The studies allow task, teacher, and other sources of variation to coexist, and the analysis tests associations.

### S22-S02

**Accepted with Hang's edit** · weight 4 · Precision and claim scope · Slide 22 · Same task, different ratings · Slide 22 — speaker notes

Suggestion: Remove the guarantee about discrimination

Original:

~~~text
so the results could never be used to discriminate.
~~~

Suggested:

~~~text
to avoid directly using those demographic attributes in the feedback model.
~~~

Hang's wording:

~~~text
to avoid discrimination from the results
~~~

Note written with the suggestion: Excluding selected attributes does not establish that discrimination is impossible. This version states the design choice already described rather than promising an untested outcome.

Used in: [Measured results and plain premises on slides](../hangs-writing-style-reference.md#measured-results-and-plain-premises-on-slides).

### S23-S01

**Declined** · weight 3 · Precision and claim scope · Slide 23 · Many things could shape feedback · Slide 23 — slide text

Suggestion: Keep robot experience as an association

Original, which stayed:

~~~text
Helps people give more precise feedback
~~~

Declined suggestion:

~~~text
May be associated with greater feedback accuracy
~~~

Note written with the suggestion: The CHARM results report an association with direction accuracy, not an experimentally established improvement in precision. Style reference: Accuracy consistency and robustness.

Used in: [Measured results and plain premises on slides](../hangs-writing-style-reference.md#measured-results-and-plain-premises-on-slides).

### S23-S02

**Accepted** · weight 1 · Precision and claim scope · Slide 23 · Many things could shape feedback · Slide 23 — slide text

Suggestion: Present domain knowledge as a possible influence

Original:

~~~text
Domain knowledge improves clarity and depth
~~~

Accepted wording:

~~~text
Relevant domain knowledge may help people describe task performance
~~~

Note written with the suggestion: Use a possible mechanism appropriate to a candidate-factor slide. Do not treat education as an established causal improvement in clarity and depth.

### S23-W01

**Declined** · weight 3 · Optional wording · Slide 23 · Many things could shape feedback · Slide 23 — slide text

Suggestion: Use plain wording for anonymity

Original, which stayed:

~~~text
More candid, less dialogic feedback
~~~

Declined suggestion:

~~~text
May encourage more candid feedback with less dialogue
~~~

Note written with the suggestion: Replace dialogic with a plain description and keep this unmeasured candidate factor tentative.

Used in: [Measured results and plain premises on slides](../hangs-writing-style-reference.md#measured-results-and-plain-premises-on-slides).

### S23-W02

**Declined** · weight 3 · Optional wording · Slide 23 · Many things could shape feedback · Slide 23 — slide text

Suggestion: State how the interface may matter

Original, which stayed:

~~~text
Voice, video, or VR changes feedback detail
~~~

Declined suggestion:

~~~text
Feedback detail may vary with voice, video, or VR interfaces
~~~

Note written with the suggestion: Make the interface the comparison and avoid promising the same effect across all listed modalities.

Used in: [Measured results and plain premises on slides](../hangs-writing-style-reference.md#measured-results-and-plain-premises-on-slides).

### S23-S03

**Accepted** · weight 1 · Precision and claim scope · Slide 23 · Many things could shape feedback · Slide 23 — slide text

Suggestion: Distinguish a candidate factor from a study result

Original:

~~~text
Reduces feedback depth and quality
~~~

Accepted wording:

~~~text
May limit feedback detail and quality
~~~

Note written with the suggestion: Time pressure is not measured here. Keep the candidate relationship conditional rather than presenting it as a result of CHARM.

Used in: [Measured results and plain premises on slides](../hangs-writing-style-reference.md#measured-results-and-plain-premises-on-slides).

### S23-S04

**Accepted with an edit under delegation** · weight 0 · Precision and claim scope · Slide 23 · Many things could shape feedback · Slide 23 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Keep cognitive load distinct from fatigue while retaining the short candidate-factor format. This follows the accepted tentative wording in S23-S03.

Suggestion: Keep cognitive load distinct from fatigue

Original:

~~~text
Fatigue lowers feedback accuracy
~~~

Suggested:

~~~text
May affect the attention available for judging behavior
~~~

Final wording, set by the assistant:

~~~text
May affect feedback accuracy
~~~

Note written with the suggestion: The heading names cognitive load but the original sentence switches to fatigue and asserts an effect. Keep the description aligned with the heading and its unmeasured status.

### S25-W01

**Accepted under delegation** · weight 0 · Optional wording · Slide 25 · What each passerby did · Slide 25 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Accept the concrete wording and explicit referents. This follows accepted clarifications such as S05-W01, S09-W01, S33-W01, and S64-W01 without changing the study result.

Suggestion: Distinguish questionnaire domains from measures

Original:

~~~text
Six domains, adapted from established scales such as the 10-item Big Five, trust, attitudes toward robots, and teaching style.
~~~

Accepted wording:

~~~text
Six domains, with items adapted from established measures, including the 10-item Big Five Inventory, trust and attitude scales, and teaching-style measures.
~~~

Note written with the suggestion: The original describes the 10-item Big Five as if it were one of the six domains. Distinguish domains from the measures used to construct the questionnaire.

### S25-W02

**Accepted under delegation** · weight 0 · Optional wording · Slide 25 · What each passerby did · Slide 25 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Accept the concrete wording and explicit referents. This follows accepted clarifications such as S05-W01, S09-W01, S33-W01, and S64-W01 without changing the study result.

Suggestion: Clarify what participants watched

Original:

~~~text
Coffee preparation and nut assembly by agents trained for 500, 1,000, or 2,000 epochs, six trajectories in total.
~~~

Accepted wording:

~~~text
Six trajectories across coffee preparation and nut assembly, using agents trained for 500, 1,000, or 2,000 epochs.
~~~

Note written with the suggestion: Put six trajectories next to what participants watched and keep the training amounts attached to the agents.

### S26-W01

**Accepted under delegation** · weight 0 · Optional wording · Slide 26 · CHARM predicts feedback from the task and the teacher · Slide 26 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Accept the concrete wording and explicit referents. This follows accepted clarifications such as S05-W01, S09-W01, S33-W01, and S64-W01 without changing the study result.

Suggestion: Name the oracle assumption

Original:

~~~text
USUAL ORACLES
~~~

Accepted wording:

~~~text
TASK-BASED ORACLES
~~~

Note written with the suggestion: Replace usual with the specific type of simulated teacher being contrasted with CHARM.

### S27-W01

**Accepted under delegation** · weight 0 · Optional wording · Slide 27 · Human characteristics and feedback accuracy · Slide 27 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Report r directly and retain association language and all three numerical values, as requested by Numbers and measured comparisons in the writing reference.

Suggestion: Report correlations directly

Original:

~~~text
Feedback values were mostly correlated with task rewards (0.563, dashed line). Robot experience and educational background also showed positive associations with feedback accuracy, with correlations of 0.25 and 0.16, respectively.
~~~

Accepted wording:

~~~text
Feedback values correlated with task rewards (r = 0.563, dashed line). Robot experience and educational background also showed positive associations with feedback accuracy (r = 0.25 and r = 0.16, respectively).
~~~

Note written with the suggestion: Mostly correlated is unclear because a correlation summarizes the relationship. Label the coefficients with r and retain the association language. Style reference: Numbers and measured comparisons.

### S27-C01

**Accepted with an edit under delegation** · weight 0 · Needs your confirmation · Slide 27 · Human characteristics and feedback accuracy · Slide 27 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Treat the threshold as the magnitude of a correlation, since the displayed discussion includes negative coefficients of −0.24 and −0.12. Describe it as a descriptive threshold and preserve the original paper citation.

Suggestion: Confirm whether the correlation threshold uses absolute values

Original:

~~~text
Bars are correlations between each characteristic domain and feedback delay, feedback accuracy, and absolute difference. Given the feedback value–reward correlation, correlations above 0.1 are considered noteworthy.
Qidi Fang*, Hang Yu*, Shijie Fang, Jindan Huang, Qiuyu Chen, Reuben M. Aronson, Elaine Schaertl Short. “CHARM: Considering Human Attributes for Reinforcement Modeling.” IEEE RO-MAN 2025. *Equal contribution.
~~~

Suggested:

~~~text
Bars show correlations between each characteristic domain and feedback delay, feedback direction accuracy, and absolute difference from the task reward. The analysis uses |r| > 0.1 as a descriptive threshold for discussing associations.
~~~

Final wording, set by the assistant:

~~~text
Bars show correlations between each characteristic domain and feedback delay, feedback direction accuracy, and absolute difference from the task reward. The analysis uses |r| > 0.1 as a descriptive threshold for discussing associations.
Qidi Fang*, Hang Yu*, Shijie Fang, Jindan Huang, Qiuyu Chen, Reuben M. Aronson, Elaine Schaertl Short. “CHARM: Considering Human Attributes for Reinforcement Modeling.” IEEE RO-MAN 2025. *Equal contribution.
~~~

Note written with the suggestion: Confirm that the intended threshold is absolute correlation. Slide 28 discusses −0.24 and −0.12, which are not above +0.1. This wording makes the descriptive threshold explicit and avoids treating it as a significance criterion.

### S28-S01

**Declined under delegation** · weight 0 · Precision and claim scope · Slide 28 · Feedback depends on who is teaching · Slide 28 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Keep the concise result title. The user retained direct scientific framing in S11-W02, S12-W01, and S19-S01. The prediction experiment also supports the relevance of the teacher.

Suggestion: Use association language in the result title

Original, which stayed:

~~~text
Feedback depends on who is teaching
~~~

Declined suggestion:

~~~text
Teacher characteristics are associated with feedback
~~~

Note written with the suggestion: Use the relationship measured by the correlation analysis rather than implying a causal dependency. Style reference: Numbers and measured comparisons.

### S28-W01

**Accepted under delegation** · weight 0 · Optional wording · Slide 28 · Feedback depends on who is teaching · Slide 28 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Name the correlation analysis directly, consistent with the user’s accepted S22-S01 question.

Suggestion: Name the correlation comparison

Original:

~~~text
What lines up with the ratings? (Pearson r)
~~~

Accepted wording:

~~~text
Associations with ratings (Pearson r)
~~~

Note written with the suggestion: Replace lines up with with the name of the comparison shown.

### S28-W02

**Accepted under delegation** · weight 0 · Optional wording · Slide 28 · Feedback depends on who is teaching · Slide 28 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Accept the concrete wording and explicit referents. This follows accepted clarifications such as S05-W01, S09-W01, S33-W01, and S64-W01 without changing the study result.

Suggestion: Keep direction accuracy and the summary statistics together

Original:

~~~text
Rating accuracy is the share of ratings with the same direction as the true reward. Per person it averaged 51.8% (SD 10.9%), and the highest was 74.5%.
~~~

Accepted wording:

~~~text
Rating accuracy is the proportion of ratings with the same direction as the task reward. Across participants, mean accuracy was 51.8% (SD 10.9%), with a maximum of 74.5%.
~~~

Note written with the suggestion: Keep the operational definition and describe the mean and maximum precisely. Style reference: Accuracy consistency and robustness.

### S28-C01

**Accepted under delegation** · weight 0 · Needs your confirmation · Slide 28 · Feedback depends on who is teaching · Slide 28 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Use the magnitude of r for the descriptive threshold, consistently with the negative coefficients displayed on this slide. Do not call this a significance threshold.

Suggestion: Clarify the threshold and avoid a significance implication

Original:

~~~text
Against the 0.56 reference, r above 0.1 is noteworthy. None of the characteristics lined up with rating delay.
~~~

Accepted wording:

~~~text
Associations with |r| > 0.1 are highlighted descriptively. No characteristic showed a clear association with rating delay.
~~~

Note written with the suggestion: Companion to the threshold-confirmation item on slide 27. Confirm the absolute-value threshold before accepting. The coefficient 0.56 does not itself define statistical significance.

### S28-S02

**Accepted under delegation** · weight 0 · Precision and claim scope · Slide 28 · Feedback depends on who is teaching · Slide 28 — speaker notes

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Describe the observed near-zero correlation instead of asserting no relationship. This follows the user’s accepted nondetection wording in S38-S01.

Suggestion: Report the near-zero correlation

Original:

~~~text
The reward has nothing to do with how fast people rate,
~~~

Accepted wording:

~~~text
The observed correlation between reward and rating delay is close to zero,
~~~

Note written with the suggestion: A near-zero observed correlation does not establish that two quantities have no relationship. State the measured result.

### S28-S03

**Accepted under delegation** · weight 0 · Precision and claim scope · Slide 28 · Feedback depends on who is teaching · Slide 28 — speaker notes

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Accept the measured or conditional statement, following accepted S38-S01, S42-S02/S03, and S59-W03, and the writing reference’s guidance on evidence boundaries.

Suggestion: Bound the teacher-characteristic result to the sample

Original:

~~~text
So people with more robot experience or a related education give ratings closer to the true reward.
~~~

Accepted wording:

~~~text
In this sample, greater robot experience and relevant education were associated with ratings closer to the task reward.
~~~

Note written with the suggestion: Keep the finding within the sample and preserve the distinction between association and causation.

### S29-W01

**Accepted under delegation** · weight 0 · Optional wording · Slide 29 · How well can a model predict each person's rating? · Slide 29 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Name the difference unit. Preserve the rounded 23 used in the original chart; use the available chart whitespace if the text box needs more width.

Suggestion: Name percentage points

Original:

~~~text
+23 points
~~~

Accepted wording:

~~~text
+23 percentage points
~~~

Note written with the suggestion: The difference between 32.6% and 55.8% is 23.2 percentage points, rounded here to 23. Name the unit instead of points. Style reference: Numbers and measured comparisons.

### S29-S01

**Accepted with an edit under delegation** · weight 0 · Precision and claim scope · Slide 29 · How well can a model predict each person's rating? · Slide 29 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Keep the reported significance and make the important validation boundary visible. Use two concise lines rather than a long sentence.

Suggestion: Keep the cross-validation boundary with the result

Original:

~~~text
Both gains p < 0.001 (paired t-tests, 10-fold CV)
~~~

Suggested:

~~~text
Both gains were statistically significant (p < 0.001, paired t-tests, 10-fold CV). Feedback from the same participants appeared in training and test folds.
~~~

Final wording, set by the assistant:

~~~text
Both gains: p < 0.001 (paired t-tests, 10-fold CV).
The same participants appeared in training and test folds.
~~~

Note written with the suggestion: Move the important validation boundary already in the notes onto the result slide. This distinguishes rating prediction for represented participants from generalization to new teachers.

### S30-W01

**Accepted under delegation** · weight 0 · Optional wording · Slide 30 · Imperfections have structure · Slide 30 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Clarify prediction accuracy and the adding-into phrase while preserving both reported values and the successful-demonstration takeaway.

Suggestion: Clarify both takeaways

Original:

~~~text
Noisy demonstrations do not mean failed demonstrations.
Adding teacher characteristics into feedback prediction lifted rating prediction from 33% to 56%
~~~

Accepted wording:

~~~text
Noisy demonstrations can still succeed.
Including teacher characteristics improved rating prediction accuracy from 33% to 56%.
~~~

Note written with the suggestion: Replace the awkward adding into and name prediction accuracy. Retain the rounded values already used in the notes.

### S30-W02

**Accepted with an edit under delegation** · weight 0 · Optional wording · Slide 30 · Imperfections have structure · Slide 30 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Preserve the scientific contrast that the user retained in S12-W03 and S19-S01, while removing structured with patterns.

Suggestion: Explain the structure without repetition

Original:

~~~text
Some imperfections in human demonstrations are not random errors. They are structured with patterns.
~~~

Suggested:

~~~text
Some imperfections in human demonstrations follow patterns related to the task.
~~~

Final wording, set by the assistant:

~~~text
Some imperfections in human demonstrations are not random errors. They follow task-related patterns.
~~~

Note written with the suggestion: Remove the repetition structured with patterns and name what the patterns relate to. Style reference: Literal wording.

### S30-S01

**Declined under delegation** · weight 0 · Precision and claim scope · Slide 30 · Imperfections have structure · Slide 30 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Keep this concise takeaway. The evaluation boundary is already in the notes and is added to the detailed result slide, so repeating it here would burden the recap.

Suggestion: Keep the prediction benefit within its evaluation scope

Original, which stayed:

~~~text
Human feedback values are associated with the teacher's characteristics. Including those characteristics improves feedback prediction accuracy.
~~~

Declined suggestion:

~~~text
Human feedback values are associated with teacher characteristics. Including those characteristics improved prediction accuracy within the study’s cross-validation design.
~~~

Note written with the suggestion: Use the past tense for the measured result and keep the evaluation scope attached. The same-participant cross-validation caveat is already in slide 29’s notes.

### S33-W01

**Accepted** · weight 1 · Optional wording · Slide 33 · Each participant rated the same 100 clips twice · Slide 33 — slide text

Suggestion: Clarify the participant groups

Original:

~~~text
The robot and one clip (left), and the two groups that rated both sessions (right).
~~~

Accepted wording:

~~~text
The robot and an example clip (left), and the two participant groups that completed both rating sessions (right).
~~~

Note written with the suggestion: Groups do not rate sessions. They complete sessions and rate clips. This version identifies both the participants and the repeated-session design.

### S33-G01

**Accepted** · weight 1 · Typos and grammar · Slide 33 · Each participant rated the same 100 clips twice · Slide 33 — slide text

Suggestion: Match the tense of the study description

Original:

~~~text
Participants were not told that the clips repeat.
~~~

Accepted wording:

~~~text
Participants were not told that the clips would repeat.
~~~

Note written with the suggestion: Match the past-tense study description. Keep the rest of the sentence unchanged.

### S33-W02

**Accepted** · weight 1 · Optional wording · Slide 33 · Each participant rated the same 100 clips twice · Slide 33 — slide text

Suggestion: Explain the scale-design choice

Original:

~~~text
The scales. Good or bad, or 0 to 10 with no negative range, so the scale does not suggest a split.
~~~

Accepted wording:

~~~text
Binary good/bad or scalar 0–10. The scalar scale had no negative values, so it did not impose a positive/negative division.
~~~

Note written with the suggestion: Name the two modalities and explain the intended scale distinction. A split alone does not tell the audience what was avoided.

### S34-G01

**Accepted under delegation** · weight 0 · Typos and grammar · Slide 34 · Thumbs up or 10 out of 10? · Slide 34 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Accept the minimal grammar correction. The user consistently accepted error-only fixes, and the writing reference says to preserve the surrounding wording.

Suggestion: Remove for twice

Original:

~~~text
They rated the same 100 clips for twice, without being told
~~~

Accepted wording:

~~~text
They rated the same 100 clips twice, without being told
~~~

Note written with the suggestion: Remove for before twice. Keep the original wording otherwise.

### S34-W01

**Accepted with an edit under delegation** · weight 0 · Optional wording · Slide 34 · Thumbs up or 10 out of 10? · Slide 34 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Keep the conditions parallel and compact enough for the existing procedure column.

Suggestion: Describe the two rating conditions in parallel

Original:

~~~text
45 participants rated the task with binary good / bad, 45 with a scalar 0–10
~~~

Suggested:

~~~text
45 participants gave binary good/bad ratings, and 45 gave scalar ratings from 0 to 10
~~~

Final wording, set by the assistant:

~~~text
45 participants used binary good/bad ratings, and 45 used scalar ratings (0–10)
~~~

Note written with the suggestion: Use parallel clauses and name ratings as the object of both conditions. Style reference: Matched factors and endpoints.

### S34-S01

**Accepted under delegation** · weight 0 · Precision and claim scope · Slide 34 · Thumbs up or 10 out of 10? · Slide 34 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Name total study completion time rather than implying an equivalence or a per-rating measure. This matches accepted S38-S01.

Suggestion: Name the measured time comparison

Original:

~~~text
Providing scalar feedback did not take longer: about 29 to 30 minutes per study in both conditions.
~~~

Accepted wording:

~~~text
Study completion time was about 29–30 minutes in both conditions.
~~~

Note written with the suggestion: The reported measure is total completion time. State the observation instead of asserting that scalar feedback never takes longer.

### S34-W02

**Accepted under delegation** · weight 0 · Optional wording · Slide 34 · Thumbs up or 10 out of 10? · Slide 34 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Name the binary comparison and retain the ±2 tolerance, following the writing reference on nondetected differences.

Suggestion: Name the nonsignificant comparison

Original:

~~~text
within ±2: no statistical significance
~~~

Accepted wording:

~~~text
Within ±2, no significant difference from binary
~~~

Note written with the suggestion: No statistical significance is incomplete because it does not name the comparison. Preserve the tolerance and the nondetection wording.

### S34-S02

**Accepted under delegation** · weight 0 · Precision and claim scope · Slide 34 · Thumbs up or 10 out of 10? · Slide 34 — speaker notes

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Accept the measured or conditional statement, following accepted S38-S01, S42-S02/S03, and S59-W03, and the writing reference’s guidance on evidence boundaries.

Suggestion: Keep the interpretation distinct from the result

Original:

~~~text
So the instability in scalar feedback is mostly small wobble, which means it can be fixed.
~~~

Accepted wording:

~~~text
The agreement within a tolerance of two points suggests that much of the variation is small. This motivates methods that account for variation in scalar feedback.
~~~

Note written with the suggestion: The agreement result motivates a correction method but does not by itself establish that all variation can be fixed. Style reference: Reporting findings and interpretations.

### S35-W01

**Accepted with an edit under delegation** · weight 0 · Optional wording · Slide 35 · STEADY stabilizes scalar feedback · Slide 35 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Name the two classes in a compact label that fits the existing procedure row.

Suggestion: Name the STEADY classification

Original:

~~~text
Label each new rating by the side it joins
~~~

Suggested:

~~~text
Classify each new rating as preferred or non-preferred
~~~

Final wording, set by the assistant:

~~~text
Classify ratings as preferred or non-preferred
~~~

Note written with the suggestion: Replace the metaphor the side it joins with the two named classes already shown on the slide.

### S35-W02

**Accepted with an edit under delegation** · weight 0 · Optional wording · Slide 35 · STEADY stabilizes scalar feedback · Slide 35 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Name the distribution centers and retain the compact procedural label.

Suggestion: Explain how the confidence weight varies

Original:

~~~text
Weight it: lower between the two centers, higher beyond them
~~~

Suggested:

~~~text
Assign a lower weight between the distribution centers and a higher weight beyond them
~~~

Final wording, set by the assistant:

~~~text
Lower weights between distribution centers, higher weights beyond them
~~~

Note written with the suggestion: Name the distribution centers and make the two weight assignments parallel.

### S35-W03

**Accepted under delegation** · weight 0 · Optional wording · Slide 35 · STEADY stabilizes scalar feedback · Slide 35 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Accept the concrete wording and explicit referents. This follows accepted clarifications such as S05-W01, S09-W01, S33-W01, and S64-W01 without changing the study result.

Suggestion: Describe the plotted return directly

Original:

~~~text
Each dot is one TAMER agent trained on one participant's feedback (45 per condition), run on the real robot. STEADY beats all four baselines (p < 0.001).
~~~

Accepted wording:

~~~text
Each dot shows the return of a TAMER agent trained on one participant’s feedback and evaluated on the real robot (45 participants per condition). STEADY outperformed all four baselines (p < 0.001).
~~~

Note written with the suggestion: Name what the dot represents, keep the participant count, and use the past tense for the study result. Style reference: Numbers and measured comparisons.

### S35-W04

**Accepted with an edit under delegation** · weight 0 · Optional wording · Slide 35 · STEADY stabilizes scalar feedback · Slide 35 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Keep can and the benefit of magnitudes, using a shorter version that fits the existing takeaway area.

Suggestion: State the role of feedback magnitudes

Original:

~~~text
Processed well, scalar can outperform binary: the magnitudes carry additional information.
~~~

Suggested:

~~~text
Processing scalar feedback can improve learning over binary feedback by using information in the rating magnitudes.
~~~

Final wording, set by the assistant:

~~~text
Processing scalar feedback can improve learning by using information in its magnitudes.
~~~

Note written with the suggestion: Name scalar feedback rather than the adjective scalar, and replace Processed well with the operation that matters. Keep can.

### S36-S01

**Accepted with an edit under delegation** · weight 0 · Precision and claim scope · Slide 36 · Progress: how much of the task is done? · Slide 36 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Follow accepted S38-S01 and keep the statistical observation, measure, sample size, and times within the existing one-line footer.

Suggestion: Avoid interpreting nondetection as no extra effort

Original:

~~~text
No extra effort: similar NASA-TLX workload, and 22 vs. 23 minutes to rate (online study I, n = 40).
~~~

Suggested:

~~~text
Online study I (n = 40) detected no significant difference in NASA-TLX workload or rating time (about 22 vs. 23 minutes).
~~~

Final wording, set by the assistant:

~~~text
Online study I (n = 40): no significant difference in NASA-TLX workload or rating time (22 vs. 23 min).
~~~

Note written with the suggestion: A nonsignificant comparison does not establish no extra effort. State what the study detected and keep the approximate times and sample size. Style reference: Reporting a difference that was not detected.

### S36-S02

**Accepted under delegation** · weight 0 · Precision and claim scope · Slide 36 · Progress: how much of the task is done? · Slide 36 — speaker notes

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Keep the spoken description of this effort comparison consistent with accepted S38-S01.

Suggestion: Remove the no-extra-cost guarantee from the notes

Original:

~~~text
And it costs nothing extra: in a first online study with 40 people, we found no difference in NASA-TLX workload, and rating took about 22 minutes versus 23 for scalar feedback.
~~~

Accepted wording:

~~~text
In the first online study with 40 people, we detected no significant difference in NASA-TLX workload or rating time. Rating took about 22 minutes with progress and 23 minutes with scalar feedback.
~~~

Note written with the suggestion: Keep the spoken explanation aligned with the bounded statistical statement suggested for the slide. Style reference: Reporting a difference that was not detected.

### S37-G01

**Accepted under delegation** · weight 0 · Typos and grammar · Slide 37 · Progress · Slide 37 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Accept the minimal grammar correction. The user consistently accepted error-only fixes, and the writing reference says to preserve the surrounding wording.

Suggestion: Fix subject–verb agreement twice

Original:

~~~text
Ratings depends on the rater. Feedback values depends on both the ground truth and who is teaching.
~~~

Accepted wording:

~~~text
Ratings depend on the rater. Feedback values depend on both the ground truth and who is teaching.
~~~

Note written with the suggestion: Change depends to depend to agree with the plural subjects Ratings and Feedback values. Keep the wording.

### S37-G02

**Accepted under delegation** · weight 0 · Typos and grammar · Slide 37 · Progress · Slide 37 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Choose the minimal grammar-only correction, following the user’s grammar-first choices in S03-G01 and S08-G01.

Suggestion: Complete the while clause

Original:

~~~text
Detours. Demonstrations contain sidetracks that do not contribute to task completion while may not be harmful to the task completion.
~~~

Accepted wording:

~~~text
Detours. Demonstrations contain sidetracks that do not contribute to task completion, while they may not be harmful to task completion.
~~~

Note written with the suggestion: Supply they after while and remove the unnecessary second the. This is the minimal grammar correction. Alternative for the same passage: S37-W02. Choose one final version.

### S37-G03

**Accepted under delegation** · weight 0 · Typos and grammar · Slide 37 · Progress · Slide 37 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Choose the minimal correction rather than the separate optional rewrite, following the user’s selected grammar-only variants.

Suggestion: Correct the preposition and endpoint phrase

Original:

~~~text
Grounded with the task. It describes the task's state with start point and end point as reference.
~~~

Accepted wording:

~~~text
Grounded in the task. It describes the task’s state with a start point and an end point as references.
~~~

Note written with the suggestion: Use grounded in, add the missing articles, and match references to the two endpoints. This keeps the original sentence structure. Alternative for the same passage: S37-W03. Choose one final version.

### S37-S01

**Accepted with an edit under delegation** · weight 0 · Precision and claim scope · Slide 37 · Progress · Slide 37 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Retain the original contrast and state the distinction between direction and magnitude without a blanket claim that all non-experts judge correctly.

Suggestion: Avoid a blanket claim about judging feedback direction

Original:

~~~text
Direction, not scale. Non-experts judge good vs. bad well, but struggle to calibrate magnitudes.
~~~

Suggested:

~~~text
Direction and magnitude. Ratings can have the correct direction even when their numerical values differ.
~~~

Final wording, set by the assistant:

~~~text
Direction, not scale. Ratings can agree in direction while differing in magnitude.
~~~

Note written with the suggestion: Non-experts judge good vs. bad well is a broad ability claim, while CHARM reports mean direction accuracy of 51.8%. Describe what was measured without turning all participants into accurate judges. Style reference: Accuracy consistency and robustness.

### S37-W01

**Accepted with an edit under delegation** · weight 0 · Optional wording · Slide 37 · Progress · Slide 37 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Name task completion as the quantity while keeping the existing progress panel concise.

Suggestion: Identify what progress changes represent

Original:

~~~text
Informative. Changes carry both the direction and the magnitudes.
~~~

Suggested:

~~~text
Informative. Changes in progress indicate the direction and magnitude of changes in task completion.
~~~

Final wording, set by the assistant:

~~~text
Informative. Changes show the direction and magnitude of task completion.
~~~

Note written with the suggestion: Name what changes and what the magnitudes describe. Progress changes describe task completion, rather than an unspecified numerical magnitude.

### S37-W02

**Declined under delegation** · weight 0 · Optional wording · Slide 37 · Progress · Slide 37 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Choose the separate minimal grammar correction S37-G02, following the user’s choice of grammar-only versions in S03 and S08.

Suggestion: Optional shorter sidetrack summary

Original, which stayed:

~~~text
Detours. Demonstrations contain sidetracks that do not contribute to task completion while may not be harmful to the task completion.
~~~

Declined suggestion:

~~~text
Sidetracks. Some actions do not advance task completion, although they may help the demonstrator control the robot.
~~~

Note written with the suggestion: Optional polished alternative to the grammar-only correction on this text. Use the established term and avoid repeating task completion. Choose one version. Style reference: Imperfect teaching and structured behavior. Alternative for the same passage: S37-G02. Choose one final version.

### S37-W03

**Declined under delegation** · weight 0 · Optional wording · Slide 37 · Progress · Slide 37 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Choose the separate minimal grammar correction S37-G03. Keep the user’s sentence structure while correcting its preposition and articles.

Suggestion: Optional definition using the preferred terminology

Original, which stayed:

~~~text
Grounded with the task. It describes the task's state with start point and end point as reference.
~~~

Declined suggestion:

~~~text
Grounded in the task. Progress describes the degree of task completion, with 0 and 100 as shared endpoints.
~~~

Note written with the suggestion: Optional polished alternative to the grammar-only correction on this text. Use the reference’s preferred definition, degree of task completion. Shared endpoints do not imply identical intermediate ratings. Choose one version. Alternative for the same passage: S37-G03. Choose one final version.

### S37-S02

**Accepted under delegation** · weight 0 · Precision and claim scope · Slide 37 · Progress · Slide 37 — speaker notes

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Accept the measured or conditional statement, following accepted S38-S01, S42-S02/S03, and S59-W03, and the writing reference’s guidance on evidence boundaries.

Suggestion: Explain task grounding without dismissing rater variation

Original:

~~~text
It's grounded in the state of the task rather than the rater's taste.
~~~

Accepted wording:

~~~text
It asks about the degree of task completion and gives raters shared endpoints.
~~~

Note written with the suggestion: Replace taste with the task-based question. Progress is still a human judgment, so the wording should not imply that it removes all effects of the rater.

### S38-S01

**Accepted** · weight 1 · Precision and claim scope · Slide 38 · Progress and scalar feedback took similar effort · Slide 38 — speaker notes

Suggestion: Keep the effort conclusion within the study result

Original:

~~~text
So progress is no harder to give than a score.
~~~

Accepted wording:

~~~text
This study did not detect a difference in the effort required to give progress or scalar feedback.
~~~

Note written with the suggestion: Do not turn nonsignificant comparisons into a claim of equal effort. Style reference: Reporting a difference that was not detected.

Used in: [Measured results and plain premises on slides](../hangs-writing-style-reference.md#measured-results-and-plain-premises-on-slides).

### S39-W01

**Accepted under delegation** · weight 0 · Optional wording · Slide 39 · Five ways the same task can go · Slide 39 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: The notes and progress.tex, line 152, describe a cup drop. Correct the conflicting caption to match both sources.

Suggestion: Match the Failure caption to the notes and dissertation

Original:

~~~text
Misses the cup at the very beginning
~~~

Accepted wording:

~~~text
Drops the cup at the very beginning
~~~

Note written with the suggestion: The speaker notes and Dissertation/chapters/progress.tex, line 152, describe the Failure scenario as dropping the cup. Match the caption to those sources; confirm against the video if that scenario has since changed.

### S40-S01

**Accepted under delegation** · weight 0 · Precision and claim scope · Slide 40 · Progress reflects task completion · Slide 40 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Accept the measured or conditional statement, following accepted S38-S01, S42-S02/S03, and S59-W03, and the writing reference’s guidance on evidence boundaries.

Suggestion: Separate the rating pattern from its explanation

Original:

~~~text
Scalar ends at 91: the last motions looked fine. Progress ends at 23: the cup fell at the start.
~~~

Accepted wording:

~~~text
Scalar feedback ends at 91 despite the early cup failure. Progress ends at 23, reflecting incomplete task completion.
~~~

Note written with the suggestion: Keep the reported values but avoid asserting an unmeasured explanation of the raters’ motives. Cup failure also avoids resolving the misses/drops inconsistency prematurely. Style reference: Observation interpretation and explanation.

### S40-S02

**Accepted under delegation** · weight 0 · Precision and claim scope · Slide 40 · Progress reflects task completion · Slide 40 — speaker notes

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Accept the measured or conditional statement, following accepted S38-S01, S42-S02/S03, and S59-W03, and the writing reference’s guidance on evidence boundaries.

Suggestion: Report the Imperfect rating without assigning motive

Original:

~~~text
It punishes the harmless dropped cup, 63, even though the task got done.
~~~

Accepted wording:

~~~text
Its final rating is lower for Imperfect, about 63, even though that scenario finishes the task.
~~~

Note written with the suggestion: Report the observed rating without attributing punishment to participants. Style reference: Observation interpretation and explanation.

### S40-S03

**Accepted under delegation** · weight 0 · Precision and claim scope · Slide 40 · Progress reflects task completion · Slide 40 — speaker notes

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Accept the measured or conditional statement, following accepted S38-S01, S42-S02/S03, and S59-W03, and the writing reference’s guidance on evidence boundaries.

Suggestion: Keep the Failure interpretation tied to the observations

Original:

~~~text
because the last few motions looked great, while progress correctly says 23, the cup fell right at the beginning.
~~~

Accepted wording:

~~~text
while progress ends at 23. The task failed near the beginning, even though the robot continued moving.
~~~

Note written with the suggestion: Remove an untested causal explanation and avoid calling a partial-completion estimate simply correct. This wording also leaves the cup-action inconsistency for confirmation.

### S41-W01

**Accepted under delegation** · weight 0 · Optional wording · Slide 41 · Progress and scalar feedback in each scenario · Slide 41 — speaker notes

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Accept the concrete wording and explicit referents. This follows accepted clarifications such as S05-W01, S09-W01, S33-W01, and S64-W01 without changing the study result.

Suggestion: Match each standard deviation to its signal

Original:

~~~text
for example 15.6 versus 28.3 standard deviation for Failure.
~~~

Accepted wording:

~~~text
for example, the standard deviation in Failure was 15.6 for progress and 28.3 for scalar feedback.
~~~

Note written with the suggestion: Name the statistic before the numbers and attach each number to its condition. Style reference: Numbers and measured comparisons.

### S42-W01

**Accepted** · weight 1 · Optional wording · Slide 42 · Non-experts can rate their own demonstrations well · Slide 42 — slide text

Suggestion: Name what the ratings reflect

Original:

~~~text
Non-experts can rate their own demonstrations well
~~~

Accepted wording:

~~~text
Non-experts’ progress ratings reflect task completion
~~~

Note written with the suggestion: The slide reports task-completion ratings and consistency, rather than a general ability to rate demonstrations well. Name the measured relationship.

### S42-S01

**Accepted under delegation** · weight 0 · Precision and claim scope · Slide 42 · Non-experts can rate their own demonstrations well · Slide 42 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: These people rated different demonstrations, so variation across participants is more precise than disagreement about the same behavior.

Suggestion: Distinguish variation from disagreement on identical behavior

Original:

~~~text
DISAGREEMENT BETWEEN PEOPLE (AVERAGE SD)
~~~

Accepted wording:

~~~text
VARIATION ACROSS PARTICIPANTS (AVERAGE SD)
~~~

Note written with the suggestion: Different participants rated different demonstrations. Variation is more precise than disagreement, which can imply that they judged the same behavior. Style reference: Accuracy consistency and robustness.

### S42-S02

**Accepted** · weight 1 · Precision and claim scope · Slide 42 · Non-experts can rate their own demonstrations well · Slide 42 — slide text

Suggestion: Keep the failure result within the sample

Original:

~~~text
final progress for every failed demo: all failures caught
~~~

Accepted wording:

~~~text
final progress for every failed demonstration in this study
~~~

Note written with the suggestion: Retain the reported threshold while keeping the claim within the observed sample. All failures caught can sound like a validated general failure detector.

### S42-S03

**Accepted** · weight 1 · Precision and claim scope · Slide 42 · Non-experts can rate their own demonstrations well · Slide 42 — speaker notes

Suggestion: State the observed threshold result precisely

Original:

~~~text
so the last progress value alone caught all of the failures.
~~~

Accepted wording:

~~~text
so a final-progress threshold of 90 identified every failed demonstration in this sample.
~~~

Note written with the suggestion: Name the threshold already displayed and the sample boundary, rather than implying general failure-detection performance.

Used in: [Measured results and plain premises on slides](../hangs-writing-style-reference.md#measured-results-and-plain-premises-on-slides).

### S43-W01

**Accepted with an edit under delegation** · weight 0 · Optional wording · Slide 43 · Feedback can be made reliable · Slide 43 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Keep the storytelling transition, consistent with the user’s rejection of deleting the first-person recap in S59-W01, while replacing vague dynamics.

Suggestion: Name the question answered by Part 2

Original:

~~~text
We then explored: can we mitigate the dynamics in human teaching?
~~~

Suggested:

~~~text
Can variation in human feedback be mitigated?
~~~

Final wording, set by the assistant:

~~~text
We then explored whether we could mitigate variation in human feedback.
~~~

Note written with the suggestion: Name feedback variation instead of the vague dynamics in human teaching, and remove presenter narration. Style reference: Direct subjects and concrete details.

### S43-S01

**Accepted with an edit under delegation** · weight 0 · Precision and claim scope · Slide 43 · Feedback can be made reliable · Slide 43 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Follow accepted S38-S01 by reporting nondetection rather than equivalence. Name return and average SD, keeping the three existing bullets.

Suggestion: Use the measured comparisons in the recap

Original:

~~~text
Scalar matches binary self-consistency within ±2
STEADY beat binary feedback by 4.2 return 
progress spread 11.6 vs. 25.5
~~~

Suggested:

~~~text
No significant difference in self-agreement between binary and scalar ratings within ±2
STEADY improved return over binary feedback by 4.2
Average SD across participants: 11.6 for progress vs. 25.5 for scalar feedback
~~~

Final wording, set by the assistant:

~~~text
No significant self-agreement difference from binary within ±2
STEADY improved return over binary feedback by 4.2
Average SD: 11.6 for progress vs. 25.5 for scalar feedback
~~~

Note written with the suggestion: Matches implies equivalence, which the nonsignificant comparison does not establish. Name return and average SD rather than leaving 4.2 return and spread undefined. Style reference: Reporting a difference that was not detected.

### S43-W02

**Accepted under delegation** · weight 0 · Optional wording · Slide 43 · Feedback can be made reliable · Slide 43 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Accept the concrete wording and explicit referents. This follows accepted clarifications such as S05-W01, S09-W01, S33-W01, and S64-W01 without changing the study result.

Suggestion: Use the established signal name in the takeaway

Original:

~~~text
Well-processed human scalar feedback, while noisier, can be beneficial for learning because of its magnitudes.
~~~

Accepted wording:

~~~text
Processing scalar evaluative feedback can improve learning by using information in its magnitudes.
~~~

Note written with the suggestion: Replace well-processed and beneficial with the specific operation and outcome. Keep the established signal name and can.

### S43-S02

**Accepted with an edit under delegation** · weight 0 · Precision and claim scope · Slide 43 · Feedback can be made reliable · Slide 43 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Use the preferred definition and the measured comparison without repeating the heading or asserting universal reliability.

Suggestion: State the measured consistency benefit

Original:

~~~text
A reliable and consistent feedback signal that describes task completion, from totally incomplete to fully complete.
~~~

Suggested:

~~~text
Progress describes the degree of task completion and varied less across participants than scalar evaluative feedback in these studies.
~~~

Final wording, set by the assistant:

~~~text
Describes the degree of task completion and varied less across people than scalar feedback in these studies.
~~~

Note written with the suggestion: Replace broad reliable and consistent with the observed comparison and study scope. Style reference: Accuracy consistency and robustness.

### S45-W01

**Declined under delegation** · weight 0 · Optional wording · Slide 45 · What the first two parts mean for learning · Slide 45 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: The existing short definition is already clear. Adding degree of makes this narrow recap panel overflow; use the fuller definition on the dedicated progress slides.

Suggestion: Use the preferred definition of progress

Original, which stayed:

~~~text
Progress describes task completion and varied less across people than scalar feedback.
~~~

Declined suggestion:

~~~text
Progress describes the degree of task completion and varied less across people than scalar feedback.
~~~

Note written with the suggestion: Use the preferred definition degree of task completion. All other wording is retained. Style reference: Teaching signals and learning quantities.

### S47-W01

**Accepted under delegation** · weight 0 · Optional wording · Slide 47 · 1. Model · Slide 47 — speaker notes

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Apply the same question wording as accepted S09-W01 so the roadmap and spoken Part 3 transition agree.

Suggestion: Clarify the Part 3 question in the notes

Original:

~~~text
Can a robot learn a good reward function from imperfect demonstrations, plus a little bit of progress?
~~~

Accepted wording:

~~~text
Can a robot learn an effective reward function from imperfect demonstrations and a few progress annotations?
~~~

Note written with the suggestion: Keep this spoken question aligned with the roadmap and distinguish annotations from task progress.

### S48-S01

**Declined under delegation** · weight 0 · Precision and claim scope · Slide 48 · Where should a robot's reward come from? · Slide 48 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Keep the motivating comparison about collection cost and repeated human involvement. The user retained comparable concise motivation and framing in S04-W01 and S12-W03.

Suggestion: Describe human effort without an unsupported cost ranking

Original, which stayed:

~~~text
Demonstrations are cheaper now (UMI, egocentric video), but a person in the loop is still expensive.
~~~

Declined suggestion:

~~~text
Demonstrations can be collected through UMI and egocentric video, while repeated human feedback during training still requires human time.
~~~

Note written with the suggestion: Replace the unqualified current cost ranking with the collection routes and recurring effort being compared. No cost estimate is supplied on this slide.

### S49-G01

**Accepted under delegation** · weight 0 · Typos and grammar · Slide 49 · Learn like a student with an answer key · Slide 49 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Correct the conventional name Newton’s second law and remove the extra article, preserving the analogy.

Suggestion: Correct Newton’s second law

Original:

~~~text
The teacher explains the Newton’s second rule in class
~~~

Accepted wording:

~~~text
The teacher explains Newton’s second law in class
~~~

Note written with the suggestion: Remove the before the possessive name and use the conventional term second law.

### S49-W01

**Accepted under delegation** · weight 0 · Optional wording · Slide 49 · Learn like a student with an answer key · Slide 49 — speaker notes

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Use the same conventional term as the corrected slide caption.

Suggestion: Use the same physics term in the notes

Original:

~~~text
A teacher explains the law of force in class;
~~~

Accepted wording:

~~~text
A teacher explains Newton’s second law in class;
~~~

Note written with the suggestion: Use the same conventional term as the slide. This changes the analogy’s wording, not the method.

### S49-S01

**Accepted under delegation** · weight 0 · Precision and claim scope · Slide 49 · Learn like a student with an answer key · Slide 49 — speaker notes

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Accept the measured or conditional statement, following accepted S38-S01, S42-S02/S03, and S59-W03, and the writing reference’s guidance on evidence boundaries.

Suggestion: Describe alignment as an optimization objective

Original:

~~~text
it aligns its learned reward with those labels, and repeats until they agree.
~~~

Accepted wording:

~~~text
it alternates reward learning with updates that encourage agreement with those labels.
~~~

Note written with the suggestion: The method optimizes an alignment loss; the wording should not promise exact agreement or define it as the stopping rule unless that is the actual implementation. Style reference: Method operations and their objects.

### S50-W01

**Accepted under delegation** · weight 0 · Optional wording · Slide 50 · PHIRL aligns learned rewards with progress · Slide 50 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Accept the concrete wording and explicit referents. This follows accepted clarifications such as S05-W01, S09-W01, S33-W01, and S64-W01 without changing the study result.

Suggestion: Use the method’s annotation terminology

Original:

~~~text
20% of demos get progress labels
~~~

Accepted wording:

~~~text
20% of demonstrations receive progress annotations
~~~

Note written with the suggestion: Use demonstrations rather than demos and annotations consistently with the method description. The appendix describes two out of ten demonstrations for the real-robot task, so the 20% proportion also applies there.

### S50-W02

**Accepted with an edit under delegation** · weight 0 · Optional wording · Slide 50 · PHIRL aligns learned rewards with progress · Slide 50 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Distinguish changes from absolute progress values, in a compact rule that retains the alignment objective.

Suggestion: Distinguish progress changes from progress values

Original:

~~~text
Magnitude. bigger progress → bigger rewards
~~~

Suggested:

~~~text
Magnitude. Larger increases in progress should correspond to larger rewards
~~~

Final wording, set by the assistant:

~~~text
Magnitude. Larger progress changes should earn larger rewards
~~~

Note written with the suggestion: Bigger progress can mean a higher progress value rather than a larger change. State that this alignment term compares changes. Style reference: Teaching signals and learning quantities.

### S50-S01

**Accepted with an edit under delegation** · weight 0 · Precision and claim scope · Slide 50 · PHIRL aligns learned rewards with progress · Slide 50 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Keep the original compact terminology and add should to mark the alignment objective.

Suggestion: Present completion alignment as an objective

Original:

~~~text
Completion. successful demos earn more total reward than failed ones
~~~

Suggested:

~~~text
Completion. Successful demonstrations should receive more total reward than failed demonstrations
~~~

Final wording, set by the assistant:

~~~text
Completion. Successful demos should earn more total reward than failed ones
~~~

Note written with the suggestion: These are alignment objectives. Use should consistently with the delta rule rather than presenting perfect satisfaction as guaranteed.

### S51-W01

**Declined under delegation** · weight 0 · Optional wording · Slide 51 · First, infer a reward from all demonstrations · Slide 51 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: The original advantage decomposition is already understandable and preserves its optimum condition. Changing built from to composed of adds no material clarity.

Suggestion: Describe the advantage decomposition directly

Original, which stayed:

~~~text
At the optimum, f is an advantage built from state-only parts:
~~~

Declined suggestion:

~~~text
At the optimum, f represents an advantage composed of state-only terms:
~~~

Note written with the suggestion: Replace built from parts with the mathematical relationship while preserving the optimum condition and the technical term advantage.

### S52-W01

**Accepted with an edit under delegation** · weight 0 · Optional wording · Slide 52 · Then, align the reward with progress · Slide 52 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Keep the rule label consistent with slide 50 while preserving the compact formula caption.

Suggestion: Use a consistent alignment-term label

Original:

~~~text
Magnitudes. Bigger progress jumps get bigger rewards.
~~~

Suggested:

~~~text
Magnitude. Larger progress changes should receive larger rewards.
~~~

Final wording, set by the assistant:

~~~text
Magnitude. Larger progress changes should earn larger rewards.
~~~

Note written with the suggestion: Match the singular label Magnitude used on slide 50 and state this as an alignment objective.

### S52-W02

**Accepted with an edit under delegation** · weight 0 · Optional wording · Slide 52 · Then, align the reward with progress · Slide 52 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Replace out-earn with the actual total-reward comparison in a caption short enough to stay above the formula.

Suggestion: Replace out-earn with the actual reward relation

Original:

~~~text
Completion. Successful demos out-earn failed ones.
~~~

Suggested:

~~~text
Completion. Successful demonstrations should receive more total reward than failed demonstrations.
~~~

Final wording, set by the assistant:

~~~text
Completion. Higher total reward for successful than failed demos.
~~~

Note written with the suggestion: Replace the figurative out-earn with the reward comparison and make the optimization objective explicit.

### S52-W03

**Accepted with an edit under delegation** · weight 0 · Optional wording · Slide 52 · Then, align the reward with progress · Slide 52 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Name hinge loss, separate the definitions, retain the threshold of 90, and preserve the original paper citation.

Suggestion: Separate the two mathematical definitions

Original:

~~~text
Hinge ℓ with margin m ≥ 0; a demonstration counts as failed if its final progress is below 90.
“PHIRL: Progress-Heuristicized Inverse Reinforcement Learning.” Under review, 2026.
~~~

Suggested:

~~~text
Hinge loss ℓ with margin m ≥ 0. A demonstration is classified as failed if its final progress is below 90.
~~~

Final wording, set by the assistant:

~~~text
Hinge loss ℓ with margin m ≥ 0. A demonstration is classified as failed if its final progress is below 90.
“PHIRL: Progress-Heuristicized Inverse Reinforcement Learning.” Under review, 2026.
~~~

Note written with the suggestion: Add loss after hinge and split the two definitions. Preserve the margin and classification threshold.

### S52-S01

**Accepted under delegation** · weight 0 · Precision and claim scope · Slide 52 · Then, align the reward with progress · Slide 52 — speaker notes

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Accept the measured or conditional statement, following accepted S38-S01, S42-S02/S03, and S59-W03, and the writing reference’s guidance on evidence boundaries.

Suggestion: Avoid an unsupported stopping criterion

Original:

~~~text
PHIRL alternates it with the AIRL update until they agree.
~~~

Accepted wording:

~~~text
PHIRL alternates alignment updates with AIRL updates to encourage agreement between learned rewards and progress annotations.
~~~

Note written with the suggestion: Name what is being aligned and avoid implying that exact agreement defines convergence. Style reference: Method operations and their objects.

### S53-W01

**Accepted with an edit under delegation** · weight 0 · Optional wording · Slide 53 · PHIRL-online labels the robot's rollouts with a VLM · Slide 53 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: The user accepted the matching clarification in S53-W02. Keep all four existing bullet paragraphs and use the documented additional online-label counts.

Suggestion: Clarify that the 400/600 labels are additional online labels

Original:

~~~text
Gemma 3 12B, fine-tuned with LoRA
Labels the policy's rollouts with progress during training
Only shapes the reward, and its labels are never imitated
Same label budget as the humans (400 or 600)
~~~

Suggested:

~~~text
Gemma 3 12B, fine-tuned with LoRA
Annotates policy rollouts with progress during training
The annotations shape the reward rather than serve as demonstration targets
Adds 400 online labels for PH or 600 for MH, matching the human annotation count
~~~

Final wording, set by the assistant:

~~~text
Gemma 3 12B, fine-tuned with LoRA
Progress labels for policy rollouts during training
Labels shape the reward, not imitation targets
400 (PH) / 600 (MH) extra labels, matching humans
~~~

Note written with the suggestion: Dissertation/chapters/phirl.tex, line 510, specifies an additional 400/600 online labels, matching the human count. Make additional explicit and scope PH/MH to the simulation datasets. The real-robot appendix separately reports 100 additional online labels. The first lines distinguish reward alignment from imitation targets.

### S53-W02

**Accepted** · weight 1 · Optional wording · Slide 53 · PHIRL-online labels the robot's rollouts with a VLM · Slide 53 — speaker notes

Suggestion: Clarify the additional online labels in the narration

Original:

~~~text
And we gave it the same number of labels the humans provided.
~~~

Accepted wording:

~~~text
In simulation, we added 400 online labels for PH and 600 for MH, matching the human annotation counts.
~~~

Note written with the suggestion: Make clear that these are additional VLM-generated labels, rather than labels provided to the model. Dissertation/chapters/phirl.tex, line 510, gives this count.

### S53-W03

**Declined** · weight 3 · Optional wording · Slide 53 · PHIRL-online labels the robot's rollouts with a VLM · Slide 53 — slide text

Suggestion: Name return in both task comparisons

Original, which stayed:

~~~text
PickPlaceCan, MH - p < 0.001
~~~

Declined suggestion:

~~~text
PickPlaceCan, MH — return, p < 0.001
~~~

Note written with the suggestion: Add return to match the Lift comparison immediately above and identify the reported measure.

Used in: [Measured results and plain premises on slides](../hangs-writing-style-reference.md#measured-results-and-plain-premises-on-slides).

### S53-W04

**Accepted** · weight 1 · Optional wording · Slide 53 · PHIRL-online labels the robot's rollouts with a VLM · Slide 53 — slide text

Suggestion: Clarify the no-human-annotation comparison

Original:

~~~text
With no human labels, off-the-shelf Gemma 3 still improved Lift, though less than human progress.
~~~

Accepted wording:

~~~text
In the no-human-annotation setting, progress estimates from off-the-shelf Gemma 3 improved Lift performance in most settings, with smaller gains than human annotations.
~~~

Note written with the suggestion: Name progress estimates as the input and keep in most settings, which appears in the notes. Compare gains rather than a model against human progress.

### S54-W01

**Accepted with an edit under delegation** · weight 0 · Optional wording · Slide 54 · Two tasks, two data qualities, four baselines · Slide 54 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Name the two dataset types without implying there are only two individual datasets across both tasks.

Suggestion: Use a natural comparison title

Original:

~~~text
Two tasks, two data qualities, four baselines
~~~

Suggested:

~~~text
Two tasks, two demonstration datasets, four baselines
~~~

Final wording, set by the assistant:

~~~text
Two tasks, two dataset types, four baselines
~~~

Note written with the suggestion: Replace the unnatural data qualities with the datasets compared on the slide.

### S54-W02

**Declined under delegation** · weight 0 · Optional wording · Slide 54 · Two tasks, two data qualities, four baselines · Slide 54 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Keep the named skill groups and their two-per-group breakdown. These are the dataset’s documented categories, rather than casual judgments introduced by this deck.

Suggestion: Describe demonstrator skill neutrally

Original, which stayed:

~~~text
PH: 200 demonstrations from one proficient operator
MH: 300 from six operators (2 worse, 2 okay, 2 better)
~~~

Declined suggestion:

~~~text
PH: 200 demonstrations from one proficient operator
MH: 300 demonstrations from six operators with varying skill levels (two per skill group)
~~~

Note written with the suggestion: Use a neutral description of skill variation in place of worse, okay, better. Preserve the dataset sizes and operator counts. Style reference: Describing human teaching without blame.

### S54-W03

**Accepted with an edit under delegation** · weight 0 · Optional wording · Slide 54 · Two tasks, two data qualities, four baselines · Slide 54 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Identify what the label counts and statistical comparison refer to. Keep the existing three paragraphs and avoid adding a semicolon.

Suggestion: Attach each count and test to its object

Original:

~~~text
PPO policy, 500 episodes, 10 parallel environments
20% of demonstrations get 10 progress labels each (400 or 600)
100 evaluation rollouts, compared with Welch's t-test
~~~

Suggested:

~~~text
PPO policy, 500 episodes, 10 parallel environments
20% of demonstrations receive 10 progress annotations each (400 or 600 total)
100 evaluation rollouts; returns compared using Welch’s t-test
~~~

Final wording, set by the assistant:

~~~text
PPO policy, 500 episodes, 10 parallel environments
20% of demonstrations receive 10 progress labels each (400 or 600 total)
100 evaluation rollouts, with returns compared using Welch’s t-test
~~~

Note written with the suggestion: Make total refer to annotation counts and name returns as the quantity compared by the statistical test.

### S55-S01

**Accepted under delegation** · weight 0 · Precision and claim scope · Slide 55 · Larger gains on the longer task and noisier demos · Slide 55 — speaker notes

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Accept the measured or conditional statement, following accepted S38-S01, S42-S02/S03, and S59-W03, and the writing reference’s guidance on evidence boundaries.

Suggestion: Describe the observed gain pattern

Original:

~~~text
the gap grows exactly where non-expert data hurts most: longer tasks and noisier demonstrations.
~~~

Accepted wording:

~~~text
the largest gains occur on the longer task and the mixed-quality demonstration dataset.
~~~

Note written with the suggestion: State the observed comparisons instead of claiming that the study established where non-expert data hurts most. The task and data quality differ together, so avoid an untested causal explanation.

### S56-W01

**Declined under delegation** · weight 0 · Optional wording · Slide 56 · Ablation and annotation percentage · Slide 56 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Keep the already clear ablation summary. Lowered return and mattered are natural wording, and contributed is not a more concrete measurement.

Suggestion: Tie the ablation interpretation to return

Original, which stayed:

~~~text
Removing any term lowered the return. Potential shaping mattered in every setting, and completion shaping mattered most when demonstrations failed.
~~~

Declined suggestion:

~~~text
Removing any alignment term reduced return. Potential shaping contributed in every setting, and completion shaping contributed most when demonstrations failed.
~~~

Note written with the suggestion: Replace mattered with the measured outcome, return, while preserving the stated ablation pattern.

### S57-W01

**Accepted under delegation** · weight 0 · Optional wording · Slide 57 · Progress makes rewards harder to hack · Slide 57 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Accept the concrete wording and explicit referents. This follows accepted clarifications such as S05-W01, S09-W01, S33-W01, and S64-W01 without changing the study result.

Suggestion: Describe the reward-hacking example literally

Original:

~~~text
A PPO policy trained on AIRL's reward learns to lift the block and drop it, over and over, to farm reward.
AIRL keeps paying out. PHIRL's reward falls at every drop, because progress falls.
Darker segments mark where reward decreases.
~~~

Accepted wording:

~~~text
A PPO policy trained on AIRL’s reward repeatedly lifts and drops the block, continuing to accumulate reward.
PHIRL’s reward decreases at each drop, consistent with the decrease in progress.
Darker segments mark decreases in reward.
~~~

Note written with the suggestion: Replace farm reward and paying out with the measured reward behavior. Consistent with distinguishes the plotted observation from an independently tested causal explanation.

### S57-C01

**Accepted under delegation** · weight 0 · Needs your confirmation · Slide 57 · Progress makes rewards harder to hack · Slide 57 — speaker notes

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: The current slide contains only Lift-Drop-Loop. The earlier migration review also identifies Touch-and-Stay as intentionally removed, so refer to one displayed example.

Suggestion: Make the reward-hacking introduction match the current slide

Original:

~~~text
During training we ran into two classic reward hacks.
~~~

Accepted wording:

~~~text
During training we observed this reward-hacking behavior.
~~~

Note written with the suggestion: Only Lift-Drop-Loop is shown on the current slide. Confirm that Touch-and-Stay is intentionally absent; if it is, this introduction should refer to the single displayed example.

### S57-C02

**Accepted under delegation** · weight 0 · Needs your confirmation · Slide 57 · Progress makes rewards harder to hack · Slide 57 — speaker notes

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Remove the stale narration of Touch-and-Stay because that example is absent from the current slide and was intentionally removed in the earlier migration review.

Suggestion: Remove narration of the absent Touch-and-Stay example

Original:

~~~text
 [click] In Touch-and-Stay, a policy trained on the environment reward just pokes the can forever instead of picking it up. PHIRL gives it a near-zero reward: not harmful, but no progress, so no pay.
~~~

Accepted wording:

~~~text
(delete the passage)
~~~

Note written with the suggestion: The current slide contains no Touch-and-Stay example. Remove this stale narration if that example was intentionally removed. This is a suggested notes deletion only; no source text has changed.

### S58-C01

**Accepted with an edit under delegation** · weight 0 · Needs your confirmation · Slide 58 · Brushing pom-poms on a real robot · Slide 58 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: The notes and appendix-phirl.tex, line 316, both support two out of ten demonstrations per person. Correct the conflicting six in the slide and keep the original compact formatting.

Suggestion: Resolve 6 versus 2 annotated demonstrations per person

Original:

~~~text
Kinova Gen3 Lite - 60 demonstrations from 6 people (2 worse, 2 okay, 2 better) - 2 annotators labeled 6 demos per person with progress
~~~

Suggested:

~~~text
Kinova Gen3 Lite — 60 demonstrations from 6 people with varying skill levels — 2 annotators provided progress labels for 2 demonstrations per person
~~~

Final wording, set by the assistant:

~~~text
Kinova Gen3 Lite - 60 demonstrations from 6 people with varying skill levels - 2 annotators labeled 2 demos per person with progress
~~~

Note written with the suggestion: The slide says 6 annotated demonstrations per person, but the notes say 2. Dissertation/chapters/appendix-phirl.tex, line 316, supports two out of ten demonstrations and 120 labels. This proposal follows that source; confirm the count if the experiment has since changed.

### S58-W01

**Accepted under delegation** · weight 0 · Optional wording · Slide 58 · Brushing pom-poms on a real robot · Slide 58 — speaker notes

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Use varying skill levels consistently with the corrected slide caption, retaining the six-person count elsewhere in the sentence.

Suggestion: Describe real-robot demonstrators neutrally

Original:

~~~text
two worse, two okay and two better,
~~~

Accepted wording:

~~~text
with varying skill levels,
~~~

Note written with the suggestion: Use neutral language for variation in demonstrator skill, as in the proposed slide wording. The six-person total remains in the surrounding sentence.

### S58-S01

**Accepted under delegation** · weight 0 · Precision and claim scope · Slide 58 · Brushing pom-poms on a real robot · Slide 58 — speaker notes

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Accept the measured or conditional statement, following accepted S38-S01, S42-S02/S03, and S59-W03, and the writing reference’s guidance on evidence boundaries.

Suggestion: State the real-robot result within its task

Original:

~~~text
So the simulation results hold up on a real robot with mixed-quality human demonstrations.
~~~

Accepted wording:

~~~text
The real-robot experiment showed the same performance ordering, with PHIRL and PHIRL-online above the baselines.
~~~

Note written with the suggestion: Name the result observed in this real-robot task instead of implying that all simulation findings generalize. Style reference: Conditions attached to benefits.

### S59-G01

**Accepted** · weight 1 · Typos and grammar · Slide 59 · Learn reward function with progress and demonstrations · Slide 59 — slide text

Suggestion: Add the missing article

Original:

~~~text
Learn reward function with progress and demonstrations
~~~

Accepted wording:

~~~text
Learn a reward function with progress and demonstrations
~~~

Note written with the suggestion: Add the missing article a before reward function. Keep the wording otherwise.

### S59-W01

**Declined** · weight 3 · Optional wording · Slide 59 · Learn reward function with progress and demonstrations · Slide 59 — slide text

Suggestion: Summarize what PHIRL does

Original, which stayed:

~~~text
In the end, we proposed PHIRL, an effective reward learning framework that learns from both human feedback and human demonstrations by aligning the learned reward function with progress annotations.
~~~

Declined suggestion:

~~~text
PHIRL learns a reward function from demonstrations and aligns it with progress annotations.
~~~

Note written with the suggestion: Remove presenter narration and the evaluative effective. Name the two method operations directly. Style reference: Method operations and their objects.

Used in: [Slide text in the presenter's voice](../hangs-writing-style-reference.md#slide-text-in-the-presenter-s-voice).

### S59-W02

**Accepted with an edit under delegation** · weight 0 · Optional wording · Slide 59 · Learn reward function with progress and demonstrations · Slide 59 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Keep the existing one-paragraph recap and its numeric results, while making the simulation comparison specific. The appendix supports 20% annotation in both settings.

Suggestion: Separate the budget and performance comparisons

Original:

~~~text
20% of demonstrations annotated - largest gains on long tasks and noisy demos - 73–84 pom-poms vs. 39–62 for baselines on a real robot
~~~

Suggested:

~~~text
Progress annotations on 20% of demonstrations
Largest simulation gains on the longer task and mixed-quality datasets
Real robot: 73–84 pom-poms removed, compared with 39–62 for the baselines
~~~

Final wording, set by the assistant:

~~~text
20% annotated - largest simulation gains on longer tasks and mixed-quality data - real robot: 73–84 pom-poms vs. 39–62 for baselines
~~~

Note written with the suggestion: Separate the annotation budget, simulation comparison, and real-robot outcome. Keep the 20% proportion, which the appendix also supports for the real-robot dataset.

### S59-W03

**Accepted** · weight 1 · Optional wording · Slide 59 · Learn reward function with progress and demonstrations · Slide 59 — speaker notes

Suggestion: Name the evaluated gains in the spoken recap

Original:

~~~text
With progress on just 20 percent of the demonstrations, it learned more robust rewards, with the biggest gains on long tasks and noisy demonstrations, and it held up on a real robot.
~~~

Accepted wording:

~~~text
With progress annotations on 20 percent of demonstrations, PHIRL outperformed the baselines in simulation and on the real robot. The largest simulation gains were on the longer task and the mixed-quality dataset.
~~~

Note written with the suggestion: State the measured performance comparisons rather than using robust without naming the disturbance or evaluation. The 20% proportion is retained for both settings, consistent with the appendix. Style reference: Accuracy consistency and robustness.

### S60-W01

**Accepted under delegation** · weight 0 · Optional wording · Slide 60 · 4. What's next · Slide 60 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Accept the concrete wording and explicit referents. This follows accepted clarifications such as S05-W01, S09-W01, S33-W01, and S64-W01 without changing the study result.

Suggestion: Name the future-work direction

Original:

~~~text
Keep expanding learning: go real world, go real scenarios
~~~

Accepted wording:

~~~text
Extending robot learning to real-world settings
~~~

Note written with the suggestion: Replace go real world, go real scenarios with the concrete future-work direction. Style reference: Headings that name the question or finding.

### S61-W01

**Accepted with an edit under delegation** · weight 0 · Optional wording · Slide 61 · Robots that learn from more, and from everyone · Slide 61 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Clarify what is expanding and retain the deck’s existing section-label separator.

Suggestion: Clarify what future work expands

Original:

~~~text
FUTURE WORK - KEEP EXPANDING LEARNING
~~~

Suggested:

~~~text
FUTURE WORK — EXPANDING WHAT ROBOTS LEARN FROM
~~~

Final wording, set by the assistant:

~~~text
FUTURE WORK - EXPANDING WHAT ROBOTS LEARN FROM
~~~

Note written with the suggestion: Name what is expanding instead of the vague keep expanding learning. This matches the content and the opening sentence of the notes.

### S61-W02

**Accepted** · weight 1 · Optional wording · Slide 61 · Robots that learn from more, and from everyone · Slide 61 — slide text

Suggestion: Name people and information sources

Original:

~~~text
Robots that learn from more, and from everyone
~~~

Accepted wording:

~~~text
Robots that learn from more people and more sources
~~~

Note written with the suggestion: Replace the incomplete more and the universal everyone with the two concrete directions shown on the slide.

### S61-G01

**Accepted** · weight 1 · Typos and grammar · Slide 61 · Robots that learn from more, and from everyone · Slide 61 — slide text

Suggestion: Correct the VLA/WAM sentence

Original:

~~~text
Large VLA/WAM policies still requires high quality data (UMI, ego centric, and Dagger), while real users could produce massive meaningful data
~~~

Accepted wording:

~~~text
Large VLA/WAM policies still require high-quality data (UMI, egocentric, and DAgger), while real users could produce massive amounts of meaningful data.
~~~

Note written with the suggestion: Grammar-only version. Correct require, high-quality, egocentric and the DAgger capitalization, and add amounts of after massive. The optional rewording below addresses the comparison itself. Alternative for the same passage: S61-W03. Choose one final version.

### S61-W03

**Declined under delegation** · weight 0 · Optional wording · Slide 61 · Robots that learn from more, and from everyone · Slide 61 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: The user explicitly accepted the grammar-only alternative S61-G01. Do not replace that selected sentence with an unselected rewrite.

Suggestion: Optional clearer foundation-model research direction

Original, which stayed:

~~~text
Large VLA/WAM policies still requires high quality data (UMI, ego centric, and Dagger), while real users could produce massive meaningful data
~~~

Declined suggestion:

~~~text
VLA/WAM policies require suitable training data. Future work could examine how to use imperfect demonstrations from non-expert users.
~~~

Note written with the suggestion: Optional alternative to the grammar-only version. UMI is an interface, egocentric describes a viewpoint, and DAgger is a data-aggregation method, so they are not parallel examples of data quality. The proposed text states the planned research question without promising massive meaningful data. Choose one version. Alternative for the same passage: S61-G01. Choose one final version.

### S61-G02

**Accepted** · weight 1 · Typos and grammar · Slide 61 · Robots that learn from more, and from everyone · Slide 61 — slide text

Suggestion: Correct the control modifier and field name

Original:

~~~text
For high level control, agentic AI has demonstrated very strong capability in self-correction and long-horizon task planning. This can also be applied to human-robot-interaction. 
~~~

Accepted wording:

~~~text
For high-level control, agentic AI has demonstrated very strong capability in self-correction and long-horizon task planning. This can also be applied to human-robot interaction.
~~~

Note written with the suggestion: Grammar-only version. Hyphenate high-level as a modifier, remove the hyphen before interaction in the field name, and remove the trailing space. Alternative for the same passage: S61-W04. Choose one final version.

### S61-W04

**Accepted** · weight 1 · Optional wording · Slide 61 · Robots that learn from more, and from everyone · Slide 61 — slide text

Suggestion: Optional concrete agentic HRI direction

Original:

~~~text
For high level control, agentic AI has demonstrated very strong capability in self-correction and long-horizon task planning. This can also be applied to human-robot-interaction. 
~~~

Accepted wording:

~~~text
Future work could examine agentic systems for high-level robot control, including self-correction and planning over long horizons in human-robot interaction.
~~~

Note written with the suggestion: Optional alternative to the grammar-only version. Replace very strong capability with the specific proposed direction. The future-work context calls for a research aim rather than an unmeasured general capability claim. Choose one version. Alternative for the same passage: S61-G02. Choose one final version.

### S61-C01

**Accepted** · weight 1 · Needs your confirmation · Slide 61 · Robots that learn from more, and from everyone · Slide 61 — speaker notes

Suggestion: Make the second future-work direction match the slide

Original:

~~~text
Teaching that's easy for everyone: interfaces that reduce the control burden behind many sidetracks, showing the robot's own progress estimate so people only correct what's wrong, and including children, older adults and people with disabilities.
~~~

Accepted wording:

~~~text
Second, non-expert teaching for foundation models: examine how imperfect human demonstrations and progress annotations could support VLA/WAM training.
~~~

Note written with the suggestion: The current slide’s middle direction is Non-expert data for VLA/WAM, while the notes still describe accessibility interfaces. Confirm which direction you want in the overview. This proposal follows the current slide and the foundation-model slide 64.

### S62-W01

**Declined under delegation** · weight 0 · Optional wording · Slide 62 · Actively sampling demonstrations to annotate · Slide 62 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Keep can and the technical phrase negative reward samples. The style reference warns against routinely replacing can with may when can already expresses a possible future benefit.

Suggestion: Present failed-first sampling as a hypothesis

Original, which stayed:

~~~text
They can shape completion, give negative reward samples, and widen data coverage.
~~~

Declined suggestion:

~~~text
They may inform completion shaping, provide negative reward examples, and broaden data coverage.
~~~

Note written with the suggestion: Keep the proposed benefit tentative and name completion shaping as the method component. This is a future sampling hypothesis, not an evaluated result.

### S63-W01

**Accepted under delegation** · weight 0 · Optional wording · Slide 63 · Learning from more modalities of human teaching · Slide 63 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Accept the concrete wording and explicit referents. This follows accepted clarifications such as S05-W01, S09-W01, S33-W01, and S64-W01 without changing the study result.

Suggestion: Name the modality and its use

Original:

~~~text
For each new one, model how non-experts give it, then leverage it.
~~~

Accepted wording:

~~~text
For each new modality, model how non-experts provide it, then use it to guide learning.
~~~

Note written with the suggestion: Replace the vague new one and give it with the actual modality and operation. Style reference: Method operations and their objects.

### S63-W02

**Accepted under delegation** · weight 0 · Optional wording · Slide 63 · Learning from more modalities of human teaching · Slide 63 — speaker notes

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Keep progress distinct from scalar evaluative feedback, as the reference explicitly requires, and include the central studied teaching signal in the summary.

Suggestion: Keep progress distinct from evaluative feedback

Original:

~~~text
This dissertation studied two forms of teaching, demonstrations and evaluative feedback.
~~~

Accepted wording:

~~~text
This dissertation studied demonstrations, evaluative feedback, and progress as human teaching signals.
~~~

Note written with the suggestion: Keep progress distinct from evaluative feedback, as the style reference requests. Progress is a central studied signal and should not disappear from this summary.

### S63-G01

**Accepted under delegation** · weight 0 · Typos and grammar · Slide 63 · Learning from more modalities of human teaching · Slide 63 — speaker notes

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Accept the minimal grammar correction. The user consistently accepted error-only fixes, and the writing reference says to preserve the surrounding wording.

Suggestion: Complete tells us in the notes

Original:

~~~text
gaze tells which objects a teacher attends to,
~~~

Accepted wording:

~~~text
gaze tells us which objects a teacher attends to,
~~~

Note written with the suggestion: Add the object us after tells. Keep the rest of the clause unchanged.

### S64-W01

**Accepted** · weight 1 · Optional wording · Slide 64 · Non-expert teaching for foundation models · Slide 64 — slide text

Suggestion: Complete the VLM-versus-human comparison

Original:

~~~text
A VLM's progress annotations already improved PHIRL in most cases, though less than human annotations did.
~~~

Accepted wording:

~~~text
VLM-generated progress annotations improved PHIRL in most settings, although human annotations produced larger gains.
~~~

Note written with the suggestion: Give the comparison its own subject and verb instead of ending with did. Remove already, which adds no information. Style reference: Complete clauses in place of elliptical endings.

### S65-W01

**Accepted under delegation** · weight 0 · Optional wording · Slide 65 · Human-in-the-loop agentic robotics · Slide 65 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Accept the concrete wording and explicit referents. This follows accepted clarifications such as S05-W01, S09-W01, S33-W01, and S64-W01 without changing the study result.

Suggestion: Use parallel categories for agent tools

Original:

~~~text
A skill learned from human teaching becomes a tool, next to trainers, evaluators and data collection.
~~~

Accepted wording:

~~~text
A skill learned from human teaching becomes a tool alongside training, evaluation, and data-collection tools.
~~~

Note written with the suggestion: Use parallel tool categories instead of mixing a skill, trainers, evaluators, and the activity data collection.

### S65-W02

**Accepted with an edit under delegation** · weight 0 · Optional wording · Slide 65 · Human-in-the-loop agentic robotics · Slide 65 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: State the retention condition directly, keeping the uncertainty margin described in the notes and fitting the existing narrow column.

Suggestion: Explain the policy-retention criterion

Original:

~~~text
Each round: analyze, act, measure, and keep a new policy only when the gain beats the evaluation's uncertainty.
~~~

Suggested:

~~~text
Each round analyzes results, chooses an action, and evaluates the new policy. The policy is retained only when its gain exceeds a margin based on evaluation uncertainty.
~~~

Final wording, set by the assistant:

~~~text
Each round evaluates a new policy and retains it only when the gain exceeds a margin based on evaluation uncertainty.
~~~

Note written with the suggestion: Replace beats the evaluation’s uncertainty with the margin described in the notes, and separate the procedure from its retention condition.

### S65-W03

**Accepted under delegation** · weight 0 · Optional wording · Slide 65 · Human-in-the-loop agentic robotics · Slide 65 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Accept the concrete wording and explicit referents. This follows accepted clarifications such as S05-W01, S09-W01, S33-W01, and S64-W01 without changing the study result.

Suggestion: Make the human-intervention examples parallel

Original:

~~~text
People step in at chosen points: feedback on an outcome, approving a change, or adjusting a procedure.
~~~

Accepted wording:

~~~text
People step in at chosen points by giving feedback on outcomes, approving changes, or adjusting procedures.
~~~

Note written with the suggestion: Make the examples parallel and attach them to how people participate.

### S66-W01

**Accepted with an edit under delegation** · weight 0 · Optional wording · Slide 66 · Agentic human-robot interaction for non-expert users · Slide 66 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Keep the hidden-needs distinction and the conditional lifting example in a concise lead that fits the current slide.

Suggestion: Distinguish hidden needs from observable behavior

Original:

~~~text
People differ, and a robot cannot see their needs. A child may push less and need the box held lower.
~~~

Suggested:

~~~text
Users have different needs that a robot cannot directly observe. For example, a child may apply less lifting force and need the box held lower.
~~~

Final wording, set by the assistant:

~~~text
Users’ needs are not directly observable. A child may apply less lifting force and need the box held lower.
~~~

Note written with the suggestion: Internal needs are not directly observable, while behavior can provide evidence about them. Apply lifting force also matches the collaborative lifting task better than push. Keep the example conditional.

### S66-W02

**Accepted under delegation** · weight 0 · Optional wording · Slide 66 · Agentic human-robot interaction for non-expert users · Slide 66 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Accept the concrete wording and explicit referents. This follows accepted clarifications such as S05-W01, S09-W01, S33-W01, and S64-W01 without changing the study result.

Suggestion: Keep the planned data format in the conditional

Original:

~~~text
Each record also keeps what the camera tells about the user, the task context, the timing, how the robot was controlled, the interface and modality, and the robot's embodiment.
~~~

Accepted wording:

~~~text
Each record would also include user information inferred from visual input, task context, timing, robot control, the interface and modality, and the robot’s embodiment.
~~~

Note written with the suggestion: Use would for the planned data format and replace what the camera tells with the actual information source. Style reference: Limitations and future work.

### S67-W01

**Accepted** · weight 1 · Optional wording · Slide 67 · Seeding robot skills from 20 years of HRI papers · Slide 67 — slide text

Suggestion: Name the trajectory-extraction operation

Original:

~~~text
716
interaction trajectories read from the papers
~~~

Accepted wording:

~~~text
716
interaction trajectories extracted from the papers
~~~

Note written with the suggestion: Use extracted to name the operation described by the repository work, rather than saying the trajectories themselves were read.

### S67-S01

**Accepted** · weight 1 · Precision and claim scope · Slide 67 · Seeding robot skills from 20 years of HRI papers · Slide 67 — slide text

Suggestion: Keep the untested refinement loop conditional

Original:

~~~text
the skills and the data format both improve with use
~~~

Accepted wording:

~~~text
The skills and data format could improve through use
~~~

Note written with the suggestion: This loop has not yet run on a robot with real users, as the limitation below states. Use could rather than presenting future improvement as observed.

Used in: [Future work and the closing slide in a talk](../hangs-writing-style-reference.md#future-work-and-the-closing-slide-in-a-talk).

### S67-C01

**Accepted** · weight 1 · Needs your confirmation · Slide 67 · Seeding robot skills from 20 years of HRI papers · Slide 67 — speaker notes

Suggestion: Clarify what the 716 trajectories were extracted from

Original:

~~~text
716 of them are re-read as task-level interaction trajectories,
~~~

Accepted wording:

~~~text
the collection also includes 716 task-level interaction trajectories,
~~~

Note written with the suggestion: Them can refer either to the 983 papers or to the 823 knowledge items. Confirm the exact mapping before claiming one trajectory per item or paper. The proposed wording preserves the reported count without choosing that mapping.

### S67-W02

**Accepted** · weight 1 · Optional wording · Slide 67 · Seeding robot skills from 20 years of HRI papers · Slide 67 — slide text

Suggestion: Keep completed work and untested skills distinct

Original:

~~~text
So far the knowledge base, the trajectories and the seed skills are built, but no skill has run on a robot with real users yet, so every skill is still a hypothesis.
~~~

Accepted wording:

~~~text
The knowledge base, trajectories, and seed skills have been built. No skill has yet been tested on a robot with real users, so each remains a hypothesis for evaluation.
~~~

Note written with the suggestion: Split the completed preparation from the untested robot deployment. Preserve the limitation and avoid a long sentence with two so clauses.

Used in: [Future work and the closing slide in a talk](../hangs-writing-style-reference.md#future-work-and-the-closing-slide-in-a-talk).

### S68-S01

**Accepted with an edit under delegation** · weight 0 · Precision and claim scope · Slide 68 · Embrace imperfection · Slide 68 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Name the evaluated CHARM prediction target in a concise final takeaway, preserving the task-related sidetrack finding.

Suggestion: Make the final prediction claim specific

Original:

~~~text
Sidetracks are task-related, and feedback is associated with who is teaching, which a robot can anticipate.
~~~

Suggested:

~~~text
Sidetracks are task-related, and feedback is associated with teacher characteristics. CHARM uses those characteristics to predict feedback values.
~~~

Final wording, set by the assistant:

~~~text
Sidetracks are task-related. CHARM predicts feedback values from teacher characteristics.
~~~

Note written with the suggestion: The original which a robot can anticipate can refer to sidetracks, feedback, or the teacher. Name the prediction actually evaluated rather than implying that the work predicts sidetracks.

### S68-W01

**Accepted with an edit under delegation** · weight 0 · Optional wording · Slide 68 · Embrace imperfection · Slide 68 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Keep the defined quantity and measured comparison compact enough for the existing final-summary column. The notes retain the own-demonstration detail.

Suggestion: Use the measured comparison in the final takeaway

Original:

~~~text
Progress asks about the task instead of the robot, and it varied less across people, even on imperfect demonstrations.
~~~

Suggested:

~~~text
Progress asks about the degree of task completion and varied less across people than scalar evaluative feedback, including when people rated their own demonstrations.
~~~

Final wording, set by the assistant:

~~~text
Progress describes the degree of task completion. Its ratings varied less across people than scalar feedback.
~~~

Note written with the suggestion: Replace the task-versus-robot slogan with the defined quantity and the measured comparison. Keep the public-space study context.

### S68-W02

**Accepted under delegation** · weight 0 · Optional wording · Slide 68 · Embrace imperfection · Slide 68 — slide text

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Use progress annotations consistently with accepted S09-W01, retaining all demonstrations and the 20% budget.

Suggestion: Distinguish annotations from task progress in the final slide

Original:

~~~text
PHIRL learns from all demonstrations, including failed ones, with progress on 20% of them.
~~~

Accepted wording:

~~~text
PHIRL learns from all demonstrations, including failed ones, using progress annotations on 20% of them.
~~~

Note written with the suggestion: Name annotations rather than the ambiguous progress on. Retain all demonstrations and the 20% proportion supported by the experiment descriptions.

### S68-S02

**Accepted under delegation** · weight 0 · Precision and claim scope · Slide 68 · Embrace imperfection · Slide 68 — speaker notes

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Accept the measured or conditional statement, following accepted S38-S01, S42-S02/S03, and S59-W03, and the writing reference’s guidance on evidence boundaries.

Suggestion: Match the spoken prediction claim to CHARM

Original:

~~~text
so a robot can anticipate them instead of throwing them away.
~~~

Accepted wording:

~~~text
and CHARM uses teacher characteristics to predict feedback values.
~~~

Note written with the suggestion: Name the evaluated prediction target rather than implying that the dissertation predicts both sidetracks and feedback.

### S68-S03

**Accepted under delegation** · weight 0 · Precision and claim scope · Slide 68 · Embrace imperfection · Slide 68 — speaker notes

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Accept the measured or conditional statement, following accepted S38-S01, S42-S02/S03, and S59-W03, and the writing reference’s guidance on evidence boundaries.

Suggestion: Report relative consistency rather than universal agreement

Original:

~~~text
Progress asks about the task rather than the robot, so non-experts agree on it, even when their demonstrations are messy.
~~~

Accepted wording:

~~~text
Progress asks about the degree of task completion. Its ratings varied less across participants than scalar evaluative feedback, including when participants rated their own demonstrations.
~~~

Note written with the suggestion: Replace agree with the measured relative variation and avoid asserting that the question wording alone caused the difference. Style reference: Accuracy consistency and robustness.

### S68-W03

**Accepted under delegation** · weight 0 · Optional wording · Slide 68 · Embrace imperfection · Slide 68 — speaker notes

Decided by an assistant (assistant-delegated), not by Hang. Recorded reason: Assistant decision: Match the final narration to the same annotation terminology accepted in S09-W01.

Suggestion: Name progress annotations in the final spoken summary

Original:

~~~text
PHIRL learns from every demonstration, failed ones included, with progress on just 20 percent of them.
~~~

Accepted wording:

~~~text
PHIRL learns from every demonstration, including failed ones, using progress annotations on 20 percent of them.
~~~

Note written with the suggestion: Keep the final spoken summary aligned with the slide and distinguish annotations from task progress.
