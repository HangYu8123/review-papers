# Hang's writing style reference

Use this reference when drafting or revising Hang Yu's dissertation, and the wording of the dissertation talk and film. The voice is direct, concrete, explanatory, and attentive to how non-experts actually teach robots. State what was done, what was found, and what the finding means. Explain methods through their operations, keep scientific terms stable, and make claim strength match the evidence.

The dissertation default is impersonal. Use this dissertation, this chapter, the study, the method, participants, or results as the subject. Preserve the directness of the papers without importing their first-person voice into new dissertation prose.

The reference rests on two kinds of evidence. Paper examples show how the published manuscripts are written. Evidence from Hang shows what Hang asked for, edited, declined, or accepted. It comes from Hang's messages in the sessions on the dissertation and the talk, from Hang's own edits of the chapters and slides, and from 679 decisions in 16 reviews, 496 of them made by Hang. Evidence from Hang is the later and more direct statement of preference, so it takes priority where the two differ.

Current instructions and the meaning, data, and definitions of the passage take priority over a reusable form. Square brackets mark slots to fill. Forms in this guide are reusable wording, not empirical findings. Paper examples retain source wording. Their older terminology, first person, stronger claims, and punctuation do not override the guidance.

## How the evidence is weighted

Hang asked for declines, notes, and edits to count for more than acceptances. Each piece of evidence from Hang carries a weight, and each pattern shows the sum over the evidence it cites, with the heaviest first. A decision that an assistant made under Hang's delegation, or one that was inferred from Hang's other decisions, is kept in the record with weight 0 and is never cited.

| Evidence | Weight |
| --- | ---: |
| An instruction in Hang's own words | 5 |
| An edit Hang made by hand to a chapter or a slide | 4 |
| A suggestion that Hang accepted with an edit | 4 |
| A suggestion that Hang declined | 3 |
| A note that Hang left on a decision | adds 2 |
| A suggestion that Hang accepted as written | 1 |
| A decision made under delegation or inferred | 0 |

[Every weighted signal, and the patterns ranked by weight](preference-signals.md) · [The record of each review](review-decisions.md)

## Quick reference

The weight after each item is the total weight of the evidence that the patterns behind it cite.

1. Name the actor or object and use a concrete verb, such as participants provided, the analysis found, or the method infers. (weight 6)
2. Use binary evaluative feedback, scalar evaluative feedback, and *progress* consistently. Keep human annotations distinct from learned rewards and policies, and keep the definitions Hang wrote. (weight 21)
3. Describe progress through the degree of task completion. Keep scale endpoints tied to the particular study and definition. (weight 21)
4. Report observations directly, interpretations with appropriate qualification, and untested explanations as possibilities. Keep the reporting frame of a result, such as Results indicate that. Hang writes both which suggests that and suggesting that. (weight 21)
5. Give the measure, baseline, condition, and relevant uncertainty together. No significant difference was detected does not mean the two conditions are equivalent. (weight 27)
6. Qualify a result when the sentence misstates the evidence, such as a no-difference claim, an unmeasured intention, or a guarantee. Ask before removing significantly from a result the chapter tests, or adding a caveat sentence. (weight 45)
7. Describe imperfect signals and actions precisely. Explain human or interface constraints without attributing unmeasured motives or blame. (weight 5)
8. Give each sentence one main job and keep a governing condition attached. Split two findings or two studies into two sentences. Keep together a result and the which clause that interprets it, a chain joined by but, and a numbered list of questions or findings. (weight 37)
9. Define the signal or quantity before formal notation. Explain the intuition before the method's operations and evaluation. (weight 8)
10. Open a research chapter with its stage sentence and then its own introduction, from the gap to the findings, ending with the related work and the published version. Keep This chapter as the subject of argues, asks, analyzes, defines, measures, and builds on. (weight 112)
11. Connect chapters through questions and contributions while preserving differences in tasks, participants, scales, and evaluations. Name the stages modeling, mitigating, and leveraging. (weight 26)
12. Use few colons and semicolons. State the relation in words with which, since, because, such as, or whereas, or start a new sentence. Keep a colon before a numbered list, after The key intuition is that, before the clause that spells out a named property, and before a quotation. Replace em dashes. (weight 74)
13. Write complete clauses. Give a comparison its own subject and verb instead of ending on did, does not, or so. (weight 12)
14. When correcting a sentence Hang wrote or dictated, fix the error and keep the wording. Propose a rewording separately, with its own reason. (weight 32)
15. Move, cut, and correct before writing new sentences. Hang declined seven of the ten passages that assistants inserted into the chapters without being asked. (weight 59)
16. In text drafted from Hang's notes, write what the notes say. Do not add a closing sentence that links the point back to the dissertation. (weight 20)
17. Choose technical terms that the papers use. A term marked Core or Familiar in [Hang's technical vocabulary](tech-vocabulary.md) needs no explanation. Check a draft for words that the papers never use with `tools/check_vocabulary.py`. (weight 19)
18. On slides, use few words in a spoken, scientific but casual tone. Report results as measured, keep the premise of the talk plain, and keep the lines Hang wrote or dictated. (weight 158)
19. Tell the motivation of a talk or film as a story about the problem, not as a summary of the dissertation's results, and do not overstate what robots can do now. (weight 67)

## Find a pattern


- [Vocabulary](#vocabulary)
- [Wording preference](#wording-preference)
- [Writing style](#writing-style)
- [Sentence style](#sentence-style)
- [Sentence structure](#sentence-structure)
- [Storytelling style](#storytelling-style)
- [Talk and film text](#talk-and-film-text)

[Complete paper evidence](source-evidence.md) · [Weighted signals](preference-signals.md) · [All review decisions](review-decisions.md) · [Source map and merge decisions](source-map.md) · [Technical vocabulary](tech-vocabulary.md) · [All words in the papers](word-list.md)

## What changed on October 19, 2026

Hang asked to update the reference from every writing suggestion and change in `waiting_for_review/` and in the talk's `wait_to_review/`, and from the interaction history, with more weight on rejections, notes, and edits. The update brought in 15 more reviews of the chapters, the talk, and the film, 19 instructions from Hang's messages, and 18 of Hang's hand edits, and gave each piece of evidence a weight. Nine patterns are new, including a category for the talk and the film, and the patterns below were revised. Items 2, 4 to 6, 8, 10 to 12, 14, 15, 18, and 19 of the quick reference are new or extended.

**New patterns**

- [This chapter as the subject](#this-chapter-as-the-subject) (Wording preference), weight 46
- [Chapter openings](#chapter-openings) (Writing style), weight 66
- [Qualifying a result](#qualifying-a-result) (Wording preference), weight 37
- [Study overview tables](#study-overview-tables) (Writing style), weight 33
- [Adding sentences that were not asked for](#adding-sentences-that-were-not-asked-for) (Writing style), weight 39
- [Slide text in the presenter's voice](#slide-text-in-the-presenter-s-voice) (Talk and film text), weight 82
- [Measured results and plain premises on slides](#measured-results-and-plain-premises-on-slides) (Talk and film text), weight 76
- [A motivation told as a story](#a-motivation-told-as-a-story) (Talk and film text), weight 53
- [Future work and the closing slide in a talk](#future-work-and-the-closing-slide-in-a-talk) (Talk and film text), weight 14

**Revised patterns**

- [Teachers and collection settings](#teachers-and-collection-settings). Adds non-expert in participant descriptions and non-lab settings for the studies as a whole.
- [Impersonal dissertation voice](#impersonal-dissertation-voice). Points to This chapter as the subject, and cites Hang's instruction on the impersonal voice.
- [Reporting findings and interpretations](#reporting-findings-and-interpretations). Suggesting that is Hang's form as well as which suggests that. Associated with for an association.
- [Reporting a difference that was not detected](#reporting-a-difference-that-was-not-detected). Hang's own wording of September 26, and three more no-difference claims changed the same way.
- [Numbers and measured comparisons](#numbers-and-measured-comparisons). Corrections that made a number agree with its chapter were accepted.
- [Limitations and future work](#limitations-and-future-work). Inserted limitation sentences were declined. Extending Hang's own limitation sentence was accepted.
- [Contribution statements](#contribution-statements). The first-work claims were replaced with what each chapter does.
- [Established dissertation terminology](#established-dissertation-terminology). Keeps Hang's definitions of sidetracks and their types, and cites Hang's instruction on these terms.
- [Literal wording](#literal-wording). Cites Hang's request to make writing that reads as AI-generated less so.
- [One main job and varied sentence length](#one-main-job-and-varied-sentence-length). A chain joined by but and a numbered list of questions or findings stay in one sentence.
- [Few colons and semicolons](#few-colons-and-semicolons). Records the four kinds of colon that Hang kept in the punctuation review and the kinds that were removed, and that every reviewed em dash was replaced.
- [A roadmap with actual content](#a-roadmap-with-actual-content). A sentence mapping a summary to later chapters was declined, and an outline entry naming what a chapter does was accepted.
- [Procedural series and enumerations](#procedural-series-and-enumerations). First and Second are not added to two results that one sentence lists.
- [The three stage dissertation arc](#the-three-stage-dissertation-arc). The stage headings use modeling, mitigating, and leveraging, and the third question has two wordings by Hang.
- [Headings that name the question or finding](#headings-that-name-the-question-or-finding). Findings as italic statements, chapter titles without the paper prefix, bold paper titles, and the future-work headings Hang wrote.
- [Discussion synthesis and its boundary](#discussion-synthesis-and-its-boundary). Cites Hang's own lead-in to the limits of the combined evidence.
- [Word choices made in review](#word-choices-made-in-review). Adds argue and one reason for a cited claim.
- [Correcting a sentence without rewording it](#correcting-a-sentence-without-rewording-it). Adds the decline rates by where a passage came from, the corrections accepted later on their own, and slide lines.
- [Future work drafted from notes](#future-work-drafted-from-notes). Hang later reworded the accepted agentic robotics text into a direct description of the setting.

The Chapter 8 review of October 12, 2026 had added four patterns and revised 25. What it changed in each pattern is listed in [source-map.md](source-map.md#changes-from-evidence-from-hang).

## Vocabulary

The patterns below are about word choice. For single technical terms, [Hang's technical vocabulary](tech-vocabulary.md) lists 1097 terms from the papers and the reference dissertations with an estimate of how familiar each one is to Hang, and [word-list.md](word-list.md) lists every word the papers use.

### Teachers and collection settings

Use non-experts for the general population, participants inside a study, demonstrators for people who control the robot, and annotators for people who label data. Human teachers is useful for broader teaching claims. Describe the recruitment setting when it affects interpretation, such as a public space, passersby, crowdworkers, or an online study.

**Reusable forms**

- Participants provided [feedback] on [robot behavior].
- Demonstrations were collected from [group] during [task] in [setting].
- Participants then annotated their own demonstrations.
- The annotations were provided by [group].

**Keep the meaning.** Non-expert describes relevant experience, not personal ability. Do not assume that demonstrators and annotators were the same people. Use provide or give for teaching, not supply. Collect data from participants, and do not write collect participants. Public space and online recruitment are distinct settings. Hang adds non-expert where a table describes participants, and writes non-lab settings for where the studies of the dissertation as a whole took place.

**Evidence from Hang** · weight 13 (1 hand edit, 2 edits, 1 acceptance)

- [CT-08](reviews/conclusion-table-review.md#ct-08), accepted with Hang's edit (weight 4). Suggested “& 40 passersby”. Hang's wording is “40 non-expert passersby”.
- [CT-09](reviews/conclusion-table-review.md#ct-09), accepted with Hang's edit (weight 4). Suggested “& 6 annotators”. Hang's wording is “6 non-expert annotators”.
- [HE-12](preference-signals.md#he-12), Hang's own edit (weight 4). “mostly conducted in a public space” became “mostly conducted in non-lab settings”.
- [DW-10](reviews/discussion-writing-review.md#dw-10), accepted (weight 1). “were not supplied exclusively by non-experts” became “were not provided exclusively by non-experts”. The same change was accepted in DW-21 and DW-58.

**Paper example** — [CHARM, line 479](../reference_papers/CHARM/ROMAN%202025.tex)

> We conducted our study in a public space with 46 participants who randomly passed by our setup.

[All source examples for this pattern](source-evidence.md#teachers-and-collection-settings).

### Imperfect teaching and structured behavior

Use imperfections as the umbrella term, then name the property. Sub-optimal describes departure from an optimal policy or trajectory, noisy describes relevant variability or errors, and unsuccessful describes failure to complete the task. Use patterned, systematic, or task-related when the analysis establishes structure. Preserve the distinction between teleoperation errors, exploration, and accommodation behaviors.

**Reusable forms**

- Sub-optimal but successful demonstrations
- Non-optimal behaviors near [task phase changes / target objects]
- Imperfections in human teaching can contain systematic structure.

**Keep the meaning.** A non-optimal action does not make the whole demonstration a failure. Patterned behavior is not automatically intentional, beneficial, or caused by a particular human factor. Name the operational definition behind each descriptor.

**Evidence from Hang** · weight 1 (1 acceptance)

- [DW-03](reviews/discussion-writing-review.md#dw-03), accepted (weight 1). “they were tied to the task” became “they were task-related”.

**Paper example** — [PROG, line 654](../reference_papers/Progress/Ro-MAN%202024.tex)

> We found that non-expert demonstrations are multi-policy and mostly successful, while noisy in a meaningful way.

[All source examples for this pattern](source-evidence.md#imperfect-teaching-and-structured-behavior).

### Teaching signals and learning quantities

Use binary evaluative feedback and scalar evaluative feedback when introducing the two evaluative modalities. Use progress for the signal describing the degree of task completion, and progress annotations or labels for the collected values. Keep reward, reward function, and policy tied to their roles in the learning formulation. Italicize progress when it names the signal.

**Reusable forms**

- Binary evaluative feedback expresses a two-way evaluation.
- Scalar evaluative feedback expresses an evaluation on a scale.
- *Progress* describes the cumulative degree of task completion.
- [Method] aligns learned rewards with progress annotations.

**Keep the meaning.** Feedback, progress, reward, and policy are not stylistic substitutes. Numerical values can represent different quantities. Shorten a signal name only after its referent is clear, and preserve the chapter definition and notation.

**Paper example** — [PH-ABS, line 70](../reference_papers/PHIRL/CoRL_2026_main.tex)

> Specifically, we use *progress*, a feedback modality that describes cumulative task completion.

[All source examples for this pattern](source-evidence.md#teaching-signals-and-learning-quantities).

### Research actions

Choose the verb by the work performed. Investigate or examine a question, characterize a signal or pattern, design a study or instrument, recruit participants, collect data, annotate demonstrations, analyze a relationship, evaluate performance, and validate a design through a stated check. Propose, present, and introduce identify a contribution without claiming an outcome. Describe names a direction without promising a formal definition.

**Reusable forms**

- This chapter investigates how [factor] is associated with [teaching pattern].
- A [study type] was conducted to examine [question].
- [Method] was evaluated on [tasks] against [baselines].

**Keep the meaning.** Investigate does not establish an effect, and evaluate does not say whether the outcome was favorable. Do not replace an open research question with demonstrate or prove. Formalize promises a formal definition, so use it only where one follows.

**Evidence from Hang** · weight 4 (1 edit)

- [DW-30](reviews/discussion-writing-review.md#dw-30), accepted with Hang's edit (weight 4). “are formalized as Agentic Robotics and Agentic HRI” became “they are described in this section as agentic robotics and agentic human-robot interaction (HRI)”.

**Paper example** — [CHARM, line 55](../reference_papers/CHARM/ROMAN%202025.tex)

> We conducted a public space study with two long-horizon tasks and 46 participants.

[All source examples for this pattern](source-evidence.md#research-actions).

### Method operations and their objects

Prefer the operation to a vague benefit, such as predict feedback values, infer a reward function, calculate rewards, shape the learned reward function, align rewards with annotations, reconstruct feedback distributions, and rescale scalar feedback. For signals, use describes, indicates, reflects, carries, or provides according to the information represented.

**Reusable forms**

- [Model] predicts feedback values using [inputs].
- [Method] infers a reward function from demonstrations.
- [Method] rescales scalar feedback based on [statistics].
- [Signal] provides [information] for [operation].

**Keep the meaning.** Predict and infer are not interchangeable when their targets differ. Alignment does not imply numerical identity. Use reconstruct and rescale in new prose, while preserving original spellings in quotations. A method name should be the subject of its computations, not of researchers' observations.

**Paper example** — [PHIRL, line 71](../reference_papers/PHIRL/CoRL_2026_main.tex)

> PHIRL iteratively infers a reward function from demonstrations via inverse reinforcement learning, calculates the learned rewards over the \textit{progress}-annotated demonstrations, and aligns the rewards with \textit{progress} annotations over four dimensions.

[All source examples for this pattern](source-evidence.md#method-operations-and-their-objects).

### Information dimensions

Describe what information a modality contributes, such as dense policy-level information, global information about policies and goals, sparse local evaluations, local critiques of robot actions, or direct policy guidance. Explain what two signals contribute together before calling them complementary.

**Reusable forms**

- [Signal A] provides [dimension A], while [signal B] provides [dimension B].
- Demonstrations and feedback provide complementary information about [specified quantities].

**Keep the meaning.** Density, scope, precision, and accuracy are separate dimensions. Dense does not mean accurate, and complementary information does not by itself establish better learning. Keep qualifications such as relatively or sometimes when the claim needs them.

**Evidence from Hang** · weight 4 (1 edit)

- [DW-12](reviews/discussion-writing-review.md#dw-12), accepted with Hang's edit (weight 4). “Demonstrations supply dense information about how a task can be performed, and *progress* supplies sparse information” became “Demonstrations provide dense information about how a task can be performed, while *progress* provides sparse information”.

**Paper example** — [Progress, line 114](../reference_papers/Progress/Ro-MAN%202024.tex)

> Human feedback and human demonstrations can be complementary due to the difference in human knowledge they carry.

[All source examples for this pattern](source-evidence.md#information-dimensions).

### Accuracy consistency and robustness

Name the dimension and the unit of comparison, such as consistency within a participant, consistency across participants, feedback direction accuracy, numerical precision, robustness to unproductive behaviors, or robustness to reward hacking. Put the operational measure close to the claim. When chapters measured consistency in different ways, say which comparison each chapter made.

**Reusable forms**

- [Signal] was more consistent across [participants / repeated sessions] under [criterion].
- [Model] achieved higher [named metric] than [baseline] under [condition].
- [Method] was evaluated for robustness to [specific disturbance].
- [Signals A] differed in consistency within and between teachers ([chapter A]), and [signals B] differed in consistency between teachers ([chapter B]).

**Keep the meaning.** Consistent ratings can be systematically inaccurate. Direction accuracy does not establish numerical precision. One reward-hacking experiment does not establish resistance to every form of exploitation.

**Evidence from Hang** · weight 1 (1 acceptance)

- [DW-05](reviews/discussion-writing-review.md#dw-05), accepted (weight 1). “differed in how consistent it was within and between teachers” became “*progress* and scalar evaluative feedback differed in consistency between teachers”. The sentence had given all three kinds of feedback the same comparison.

**Paper example** — [CHARM, line 394](../reference_papers/CHARM/ROMAN%202025.tex)

> This suggests that participants with relevant educational backgrounds or greater robot experience tend to provide feedback that is more accurate in direction (e.g., positive vs. negative).

[All source examples for this pattern](source-evidence.md#accuracy-consistency-and-robustness).

### Prior work and research gaps

Use prior work as the usual literature phrase, and narrow it to the relevant methods or studies. State the particular assumption, representation, or missing comparison. Refer to the dissertation's own earlier studies by chapter when writing across chapters.

**Reusable forms**

- Prior [method family] assumes [assumption].
- Existing approaches use [representation].
- Few studies have examined [specific relationship].
- This chapter examines [relationship] in [setting].

**Keep the meaning.** A phrase found in an older paper does not establish the present state of the field. Claims such as few studies, none, and first require literature support. Interprets, assumes, and relies on make different claims, so choose the one the cited work supports.

**Paper example** — [SIDE, line 187](../reference_papers/Demonstration_sidetracks/main.tex)

> Prior work interprets non-optimal behaviors in human demonstrations as random manipulation noise or incorrect behaviors with underlying optimal control policies

[All source examples for this pattern](source-evidence.md#prior-work-and-research-gaps).

### Hedges and degree words

Use can for a supported capability or possibility, may and might for a possible explanation, would for a conditional expectation, and tend to for a pattern that is not universal. Would be expected to states an expectation that was not measured. Use likely only when the evidence warrants that level of commitment. Give a correlation value instead of fairly correlated or relatively high.

**Reusable forms**

- [Method] can use [information] to [operation].
- [Behavior] may reflect [possible explanation].
- [Signal] would be more [property] if [condition].
- [Information] would be expected to matter more when [condition].

**Keep the meaning.** Modal verbs do different jobs and are not interchangeable levels on a confidence scale. In empirical comparisons, use significantly only for a supported statistical claim, and keep the test or its reference nearby. Qualifying a result describes which qualifications Hang accepted and which were declined. Do not lower can to may or could in a sentence Hang wrote as a matter of routine. That change was accepted twice and declined twice in the Chapter 8 review, so propose it only where can would misstate the evidence.

**Evidence from Hang** · weight 8 (1 edit, 1 decline, 1 acceptance)

- [DW-12](reviews/discussion-writing-review.md#dw-12), accepted with Hang's edit (weight 4). “which should matter more when more of the demonstrated behavior does not” became “would be expected to matter more when a larger portion of the demonstrated behaviors does not advance the task”.
- [DW-35](reviews/discussion-writing-review.md#dw-35), declined (weight 3). Suggested “may benefit learning”. Hang kept “can be beneficial”.
- [DW-39](reviews/discussion-writing-review.md#dw-39), accepted (weight 1). “more teaching modalities can improve learning outcomes” became “more teaching modalities may improve learning outcomes”.

**Paper example** — [CHARM, line 394](../reference_papers/CHARM/ROMAN%202025.tex)

> This suggests that participants with relevant educational backgrounds or greater robot experience tend to provide feedback that is more accurate in direction (e.g., positive vs. negative).

[All source examples for this pattern](source-evidence.md#hedges-and-degree-words).

### Value words and novelty

Use effective, robust, informative, promising, and similar value words sparingly, next to the result or mechanism that makes them meaningful. Prefer a concrete research contribution to a general claim of importance. Describe progress as under-explored as a human teaching signal where that is the dissertation's intended claim.

**Reusable forms**

- [Method] improved [metric] under [condition].
- [Signal] provides information about [quantity].
- *Progress* is under-explored as a human teaching signal.

**Keep the meaning.** Robust must say robust to what. A signal is not universally novel because one use is under-explored. Treat one value word per claim as an editing default, not a quota.

**Evidence from Hang** · weight 1 (1 acceptance)

- [DW-59](reviews/discussion-writing-review.md#dw-59), accepted (weight 1). “feedback magnitudes deserve attention” became “differences between teachers appear mainly in the magnitude of feedback”. The finding took the place of a general claim of importance.

**Paper example** — [STEADY, line 135](../reference_papers/STEADY/IEEEexample.tex)

> scalar feedback is a promising signal for use in interactive Reinforcement Learning.

[All source examples for this pattern](source-evidence.md#value-words-and-novelty).

### Word choices made in review

Hang changed or confirmed these words while editing the Chapter 8 suggestions. Write a portion of the demonstrated behaviors, with behaviors in the plural. Use sampling for the active choice of demonstrations to annotate, and prioritized for what a selection strategy annotates first. Use steps for the points of a task, quantities for what two signals describe, and both approaches for two methods. Join two adjectives with and. In the later reviews, Hang accepted argue for the claim of a cited paper and one reason for a cause that the paper names among others.

**Reusable forms**

- a larger portion of the demonstrated behaviors
- actively sampling demonstrations to annotate
- [Failed demonstrations] should be prioritized for annotations.
- a short and clear [segment]
- once a robot is already capable of performing [tasks]
- Users may differ in their preferences, needs, and capabilities.

**Keep the meaning.** These are choices made in one chapter, and each belongs to its context. Share, selecting, and points are not errors elsewhere. Do not replace a defined technical term with one of these words.

**Evidence from Hang** · weight 19 (4 edits, 3 acceptances)

- [DW-12](reviews/discussion-writing-review.md#dw-12), accepted with Hang's edit (weight 4). Suggested “a larger share of the demonstrated behavior”. Hang's wording is “a larger portion of the demonstrated behaviors”.
- [DW-34](reviews/discussion-writing-review.md#dw-34), accepted with Hang's edit (weight 4). Suggested “a short, clear one”. Hang's wording is “a short and clear one”.
- [DW-32](reviews/discussion-writing-review.md#dw-32), accepted with Hang's edit (weight 4). Suggested “failed demonstrations are always annotated”. Hang's wording is “failed demonstrations should be prioritized for annotations”.
- [OA-102](reviews/overall-assessment-review.md#oa-102), accepted with Hang's edit (weight 4). Kept “argue that one reason Large Language Models (LLMs) hallucinate”. The suggestion replaced indicate that ... is the major reason.
- [OA-102](reviews/overall-assessment-review.md#oa-102), accepted with Hang's edit (weight 4). Suggested “binary evaluation rewards guessing over acknowledging uncertainty”. Hang's wording is “the expected rewards of guessing is higher than acknowledging uncertainty”.
- [DW-09](reviews/discussion-writing-review.md#dw-09), accepted (weight 1). “they describe different things” became “they describe different quantities”.
- [DW-28](reviews/discussion-writing-review.md#dw-28), accepted (weight 1). “when the robot has the capbility of performing certain tasks” became “once a robot is already capable of performing certain tasks”.
- [DW-50](reviews/discussion-writing-review.md#dw-50), accepted (weight 1). “users may have different preferences, needs, and capbilities” became “users may differ in their preferences, needs, and capabilities”.

**Basis.** This pattern comes from the evidence from Hang above. It has no paper example.

## Wording preference

### Impersonal dissertation voice

Keep the papers' directness while using the dissertation, chapter, study, method, participants, or results as the subject. Use procedural passives when the procedure or data deserves emphasis. This dissertation describes the overall program, this chapter describes a local study, and the study in [chapter] names an earlier study. A chapter can propose, examine, or present, but it does not collect data or find results, so write In [chapter], [data] was collected. The pattern This chapter as the subject lists the verbs that Hang keeps with This chapter.

**Reusable forms**

- We conducted a study → A study was conducted.
- We propose [method] → This chapter proposes [method].
- We found [result] → The analysis found [result].
- Our key insight is that → The key insight is that
- [Chapter] collected [data] and found [result] → In [chapter], [data] was collected [procedure]. The results show that [result].

**Keep the meaning.** Changing the subject must not change evidential strength, so found does not automatically become suggested. Avoid attributing recruitment, design decisions, or observations to an algorithm or to a chapter. First-person paper quotations remain unchanged. The impersonal default governs new dissertation prose.

**Evidence from Hang** · weight 14 (1 instruction, 2 edits, 1 acceptance)

- [HI-03](preference-signals.md#hi-03), Hang's instruction, October 11, 2026 (weight 5). “we conducted a study -> a study was conducted”.
- [DW-20](reviews/discussion-writing-review.md#dw-20), accepted with Hang's edit (weight 4). “collected *progress* on a segment of a trajectory” became “*progress* was collected on a segment of a trajectory”. The chapter had been the subject of collected and found.
- [DW-06](reviews/discussion-writing-review.md#dw-06), accepted with Hang's edit (weight 4). “The second stage indicates that it can” became “The results of the second stage indicate that it can”.
- [OA-505](reviews/overall-assessment-review.md#oa-505), accepted (weight 1). “From prior work, we expect that binary feedback is noise-reduced” became “From prior work, binary feedback is expected to be noise-reduced”. This was the last we in the chapters.

**Paper example** (paper voice before dissertation adaptation) — [CHARM, line 54](../reference_papers/CHARM/ROMAN%202025.tex)

> In this work, we designed an exploratory study investigating how human feedback patterns are associated with human characteristics.

[All source examples for this pattern](source-evidence.md#impersonal-dissertation-voice).

### Reporting findings and interpretations

Choose a reporting form by its job. A method or participant can report an outcome directly. The analysis found and the results showed suit observations, the results indicate can summarize a pattern, and this suggests or which suggests introduces a bounded interpretation. These results are consistent with links a finding to earlier evidence. Keep the reporting frame when a result from another chapter is brought into a discussion. Results indicate that and The results show that mark the statement as a reported result, so do not delete them to shorten the sentence. After a result, Hang writes both which suggests that and suggesting that, so do not change one into the other. For a result that the studies only associate, write associated with rather than shaped by or affected by.

**Reusable forms**

- [Method] achieved [measured outcome].
- The analysis found [measured relationship].
- The results indicate [pattern].
- This suggests that [bounded interpretation].
- These findings motivate [specific next step].
- Results indicate that [result] ([chapter]), which suggests that [bounded interpretation].
- In [chapter], [signal] was collected on [unit]. The results show that [finding].

**Keep the meaning.** Vary subjects and sentence structure without rotating verbs merely for variety. Demonstrates needs a direct evidential basis. Confirmed requires a specified proposition and an adequate check. Agreement with an earlier observation alone may be better expressed as consistent with. Motivate claims less than support when observations that were not designed as a comparison lead to a next step.

**Evidence from Hang** · weight 21 (5 edits, 1 acceptance)

- [DW-20](reviews/discussion-writing-review.md#dw-20), accepted with Hang's edit (weight 4). Suggested “and the resulting values carried information about task completion”. Hang's wording is “The results show that *progress* values carried information about task completion”.
- [DW-36](reviews/discussion-writing-review.md#dw-36), accepted with Hang's edit (weight 4). Hang added “Results indicate that”. The suggestion had removed Current results indicate that. Hang put the frame back without Current.
- [DW-19](reviews/discussion-writing-review.md#dw-19), accepted with Hang's edit (weight 4). “and they support the selection of what to annotate” became “This motivates the selection of demonstrations to annotate”.
- [CP-17](reviews/connection-paragraph-review.md#cp-17), accepted with Hang's edit (weight 4). Suggested “which suggests that the two carry compatible information”. Hang's wording is “suggesting that the two carry compatible information”. Hang accepted the new subject, The results also showed, and put suggesting that back.
- [CP-14](reviews/connection-paragraph-review.md#cp-14), accepted with Hang's edit (weight 4). Kept “feedback is associated with the characteristics of the teacher”. The suggestion changed shaped by to associated with, and Hang kept it.
- [CP-10](reviews/connection-paragraph-review.md#cp-10), accepted (weight 1). “The first stage of this dissertation found that non-expert feedback is shaped by” became “The results of the first stage of this dissertation indicate that non-expert feedback is associated with”.

**Paper example** — [CHARM, line 56](../reference_papers/CHARM/ROMAN%202025.tex)

> We found that feedback patterns are not only correlated with task statistics, such as rewards, but also correlated with participants' characteristics, especially robot experience and educational background.

[All source examples for this pattern](source-evidence.md#reporting-findings-and-interpretations).

### Reporting a difference that was not detected

Report what the comparison detected, using no difference in [measure] was detected or no statistically significant difference was found. State the compared groups and any tolerance or criterion that governs the analysis. For a planned comparison, write similar performance unless an equivalence test is planned.

**Reusable forms**

- No difference in [measure] was detected between [A] and [B] under [criterion].
- No statistically significant difference in [outcome] was found between [conditions].
- Such a comparison would test whether [method] can reach similar performance with [less effort].

**Keep the meaning.** A nonsignificant result does not establish equivalence, identical performance, or disappearance of an effect. Avoid the difference vanishes and as good as unless the analysis actually supports that stronger claim.

**Evidence from Hang** · weight 15 (1 instruction, 1 hand edit, 1 edit, 2 acceptances)

- [HI-01](preference-signals.md#hi-01), Hang's instruction, September 26, 2026 (weight 5). ““With an agreement tolerance of ±2, we did not detect a difference in self-consistency between scalar and binary feedback.””.
- [DW-37](reviews/discussion-writing-review.md#dw-37), accepted with Hang's edit (weight 4). “can obtain equivalent performance” became “can reach similar performance”.
- [HE-14](preference-signals.md#he-14), Hang's own edit (weight 4). “no detectable difference” became “no statistical significance”. Hang made this change on a slide of the short talk.
- [OA-605](reviews/overall-assessment-review.md#oa-605), accepted (weight 1). “The workload of giving progress has no difference from that of giving scalar feedback” became “No significant difference in workload was detected between giving progress and giving scalar feedback”.
- [OA-601](reviews/overall-assessment-review.md#oa-601), accepted (weight 1). “does not need extra workload and time” became “no significant difference in workload or completion time was detected”.

**Paper example** — [PROG, line 319](../reference_papers/Progress/Ro-MAN%202024.tex)

> We did not find any significant difference between giving scalar feedback and progress in all the dimensions of the NASA TLX results

[All source examples for this pattern](source-evidence.md#reporting-a-difference-that-was-not-detected).

### Numbers and measured comparisons

Put the measured outcome and baseline in the same sentence. Use N out of M for participant counts, specify the denominator of a percentage, and report correlation values. Keep the comparison condition, magnitude, and relevant statistical evidence when shortening a sentence. In a full sentence, join two values with compared with. Inside parentheses, against is enough.

**Reusable forms**

- [Model] predicted [values] more accurately than [baseline] under [condition].
- [Method] achieved [value A] on [metric], compared with [value B] for [baseline].
- [N] out of [M] participants [observed action].
- [Factors] showed positive associations with [measure], with correlations of [r1] and [r2], respectively.
- [Margin] was larger on [A] than on [B] (in [task], [value A] against [value B]).

**Keep the meaning.** Do not turn correlation into prediction or causation, or replace a named metric with overall quality. Preserve units and distinguish percentage points from relative percentages. Paper numbers illustrate wording, so use the current study's actual values. Hang accepted every correction that made a number agree with the chapter that reports it, such as an exact count in place of more than or over.

**Evidence from Hang** · weight 12 (2 edits, 4 acceptances)

- [DW-07](reviews/discussion-writing-review.md#dw-07), accepted with Hang's edit (weight 4). “was 11.6 for *progress* and 25.5 for scalar feedback” became “was 11.6 for *progress*, compared with 25.5 for scalar feedback”.
- [DW-11](reviews/discussion-writing-review.md#dw-11), accepted with Hang's edit (weight 4). Suggested “(in Lift, 17.1% compared with 5.6%)”. Hang's wording is “(in Lift, 17.1% against 5.6%)”.
- [DW-02](reviews/discussion-writing-review.md#dw-02), accepted (weight 1). “correlated with feedback accuracy at 0.25 and 0.16” became “showed positive associations with feedback accuracy, with correlations of 0.25 and 0.16, respectively”.
- [OA-107](reviews/overall-assessment-review.md#oa-107), accepted (weight 1). “used to collect over 5000 pieces” became “used to collect 4,655 pieces”.
- [OA-115](reviews/overall-assessment-review.md#oa-115), accepted (weight 1). “During the study, more than 18,000 pieces” became “During the study, 18,000 pieces”.
- [OA-716](reviews/overall-assessment-review.md#oa-716), accepted (weight 1). “PHIRL performed well with demonstrations of mixed quality” became “PHIRL (73) performed well with demonstrations of mixed quality”.

**Paper example** — [PROG, line 548](../reference_papers/Progress/Ro-MAN%202024.tex)

> We found that non-expert demonstrations are noisy and contain a variety of policies, even though 34 out of 40 are ultimately successful.

[All source examples for this pattern](source-evidence.md#numbers-and-measured-comparisons).

### Hypotheses and verdicts

State the expectation in plain language, give the hypothesis a stable label, and report whether the evidence supports it. Keep the verdict short once the measure and test have been explained.

**Reusable forms**

- H1. [Testable statement].
- H1 is supported.
- H3 is not supported.

**Keep the meaning.** Use supported, not proven. A hypothesis of no extra cost or no difference needs careful interpretation. Do not infer equivalence solely from a nonsignificant test. Report unsupported hypotheses as plainly as supported ones.

**Paper example** — [PROG, line 251](../reference_papers/Progress/Ro-MAN%202024.tex)

> H1. Giving progress does not require extra workload and extra time compared to giving scalar feedback.

[All source examples for this pattern](source-evidence.md#hypotheses-and-verdicts).

### Possible explanations

Give the result before its possible explanation. Use one possible reason is that, this might be because, or this may be due to when the mechanism was not tested. This is because suits an established procedural or mathematical reason.

**Reusable forms**

- One possible explanation is [hypothesis].
- This might be because [plausible mechanism].
- This might explain why [bounded observation].

**Keep the meaning.** Likely or possibly does not supply causal evidence. The phrase this explains why can overstate an untested mechanism. Make the observation referred to by this unambiguous.

**Paper example** — [SIDE, line 304](../reference_papers/Demonstration_sidetracks/main.tex)

> This is likely due to the different sub-goals of different task phases, along with a change in the control pattern for participants

[All source examples for this pattern](source-evidence.md#possible-explanations).

### Limitations and future work

Name the study design or method assumption, explain the limit it places on a claim, and identify a matching next test. A useful limitation says what cannot yet be concluded and what evidence would address it. For planned work, use Future work could, One planned step is to, and would for what the planned study does. Keep the scope of a plan general, with such as for an example source, when exact tracks, years, or counts would commit the plan to details that may change.

**Reusable forms**

- One limitation is that [specific design constraint].
- Because [design choice], [behavior] may differ in [unexamined setting].
- Future work could investigate [question] by [specific extension].
- One planned step is to [action]. Another planned step is to [action].
- These [strategies] would be compared under [shared condition].
- This would begin by [verb]-ing [sources], such as [example], and [verb]-ing [result].

**Keep the meaning.** Do not replace a scoped contribution with a generic disclaimer. A future extension is a proposed action or hypothesis, not an established improvement or a commitment to conduct the study. Hang also writes future work can consider and can be beneficial in future-work sentences, and suggestions to change them were declined. Do not insert a new limitation into a chapter. Hang declined each inserted limitation sentence in the overall assessment and accepted the one change that extended Hang's own limitation sentence with what it means.

**Evidence from Hang** · weight 29 (4 edits, 4 declines, 1 acceptance)

- [DW-32](reviews/discussion-writing-review.md#dw-32), accepted with Hang's edit (weight 4). “Future work should extend PHIRL with a selection strategy” became “Future work could extend PHIRL with a selection strategy”.
- [DW-34](reviews/discussion-writing-review.md#dw-34), accepted with Hang's edit (weight 4). “These strategies should be compared under an equal budget of human time” became “These strategies would be compared under an equal budget of human time”.
- [DW-54](reviews/discussion-writing-review.md#dw-54), accepted with Hang's edit (weight 4). Suggested “distilling the main-track papers of the ACM/IEEE International Conference on Human-Robot Interaction from 2006 to 2025”. Hang's wording is “distilling the papers from Human-Robot Interaction conferences, such as”.
- [DW-56](reviews/discussion-writing-review.md#dw-56), accepted with Hang's edit (weight 4). Suggested “two decades of HRI findings”. Hang's wording is “draw on decades of HRI findings”.
- [DW-41](reviews/discussion-writing-review.md#dw-41), declined (weight 3). Suggested “future work could extend the framework to new modalities with the approach of this dissertation”. Hang kept “future work can consider extending new modalities while using an approach similar to that of this dissertation”.
- [OA-310](reviews/overall-assessment-review.md#oa-310), declined (weight 3). Suggested “part of the improvement may come from learning how individual participants rate”.
- [OA-411](reviews/overall-assessment-review.md#oa-411), declined (weight 3). Suggested “an agreement statistic between the annotators is not reported”.
- [OA-712](reviews/overall-assessment-review.md#oa-712), declined (weight 3). Suggested “they are not the passersby whose demonstrations were studied”.
- [OA-410](reviews/overall-assessment-review.md#oa-410), accepted (weight 1). “it only used demonstrations from one task and one robot” became “one task, one robot, and one control interface. With a single interface”.

**Paper example** — [SIDE, line 364](../reference_papers/Demonstration_sidetracks/main.tex)

> One limitation of this work is that we only used demonstrations from one task and one robot.

[All source examples for this pattern](source-evidence.md#limitations-and-future-work).

### Contribution statements

State what the dissertation or chapter contributes, using the research operation, resulting method, characterization, or dataset. Connect it to a practical benefit at the strength the evidence supports.

**Reusable forms**

- The main contribution of this dissertation is [specific contribution].
- This dissertation makes the following contributions:
- An additional contribution is [dataset / method / finding].

**Keep the meaning.** Use first only where its scope is defensible. Keep a contribution distinct from an aspiration. A dataset release, empirical characterization, and performance improvement are different kinds of contribution. Hang accepted each of the four suggestions that replaced a claim of being the first work with what the chapter does, and with few studies have examined where the gap matters.

**Evidence from Hang** · weight 4 (4 acceptances)

- [OA-403](reviews/overall-assessment-review.md#oa-403), accepted (weight 1). “To the best of the author's knowledge, this is the first work that systematically characterizes” became “This chapter systematically characterizes”.
- [OA-301](reviews/overall-assessment-review.md#oa-301), accepted (weight 1). “this is the first work that systematically investigated” became “few studies have examined how human characteristics are associated with human feedback”.
- [OA-502](reviews/overall-assessment-review.md#oa-502), accepted (weight 1). “this is the first work that quantifies feedback dynamics” became “This chapter quantifies feedback dynamics”.
- [OA-503](reviews/overall-assessment-review.md#oa-503), accepted (weight 1). “STEADY is the first algorithm that enables” became “STEADY enables binary-feedback-based algorithms”.

**Paper example** — [PROG, line 149](../reference_papers/Progress/Ro-MAN%202024.tex)

> The main contribution of this work is to demonstrate that *progress* has information beyond rating and ranking, and has great potential in interactive learning.

[All source examples for this pattern](source-evidence.md#contribution-statements).

### Established dissertation terminology

Use degree of completion or degree of task completion for the progress quantity, and under-explored as a human teaching signal for the intended progress positioning. Write a codebook developed through open coding, and advantages for the RL quantity. Use binary evaluative feedback and scalar evaluative feedback for the named modalities. Use account for systematic variation in human teaching when that is the intended operation. Write agentic robotics and agentic human-robot interaction (HRI) in lower case in running text. Refer to a chapter by its label, not by a typed number.

**Reusable forms**

- Completion rate / completion percentage → degree of completion, when naming the progress quantity.
- Open-coded book → a codebook developed through open coding.
- Advantaged rewards → advantages, when referring to the RL quantity.
- Structurally resilient against [failure] → illustrates how [mechanism] can discourage [failure], when supported.
- Agentic HRI builds on agentic robotics.

**Keep the meaning.** These are context-dependent wording choices, not global replacements. A measured completion rate may still be a rate. The recorded 0 to 10 correction concerns STEADY scalar feedback. Preserve CHARM's five-point scale and the applicable progress scale. Never change a scale or scientific quantity for stylistic consistency. Keep Hang's definitions as written, such as demonstration sidetracks defined as structured imperfections in human demonstrations and the codebook's types, and ask before changing a definition so that it matches another chapter. Hang declined three such changes. Spelling of a name, such as AIRL-Pref or Gen3 Lite, was made consistent.

**Evidence from Hang** · weight 21 (1 instruction, 1 edit, 3 declines, 3 acceptances)

- [HI-02](preference-signals.md#hi-02), Hang's instruction, September 26, 2026 (weight 5). “Prefer “degree of completion” to “completion rate.””.
- [HI-02](preference-signals.md#hi-02), Hang's instruction, September 26, 2026 (weight 5). “I'd use "under-explored as a human teaching signal" everywhere except the paper title”.
- [DW-56](reviews/discussion-writing-review.md#dw-56), accepted with Hang's edit (weight 4). “(Chapters 5 and 6)” was replaced. The typed chapter numbers became chapter labels written with \autoref.
- [OA-109](reviews/overall-assessment-review.md#oa-109), declined (weight 3). Suggested “defined as non-optimal behaviors in human demonstrations”. Hang kept “defined as structured imperfections in human demonstrations”.
- [OA-402](reviews/overall-assessment-review.md#oa-402), declined (weight 3). Suggested “The non-optimal behaviors that non-experts performed while demonstrating are defined as”. Hang kept “The frequent and patterned non-optimal behaviors”.
- [OA-111](reviews/overall-assessment-review.md#oa-111), declined (weight 3). Suggested “a sequence of movements that makes no contribution to the completion of the task or harms it”. Hang kept “non-harmful control errors that often last for a very short period of time”.
- [DW-49](reviews/discussion-writing-review.md#dw-49), accepted (weight 1). “Buinding on agentic Robotics” became “Agentic HRI builds on agentic robotics”.
- [OA-110](reviews/overall-assessment-review.md#oa-110), accepted (weight 1). “A codebook was used for open coding” became “A codebook developed through open coding was used”.
- [OA-715](reviews/overall-assessment-review.md#oa-715), accepted (weight 1). “AIRLPref (IRL with both feedback and demonstrations)” became “AIRL-Pref (IRL with both feedback and demonstrations)”.

**Paper example** (historical wording to adapt using the guidance above) — [PROG, line 93](../reference_papers/Progress/Ro-MAN%202024.tex)

> In this work, we characterize and test a little-used teaching signal: *progress*, designed to represent the completion percentage of a task.

[All source examples for this pattern](source-evidence.md#established-dissertation-terminology).

### Shared references and user scales

Explain a scale through the reference states and the meaning of its endpoints. Keep the possibility of user-dependent scaling near cross-user comparisons, especially when a method compares annotation magnitudes.

**Reusable forms**

- The signal ranges from [lower] to [upper].
- A value of [endpoint] indicates [defined task state].
- Different users may scale progress differently.
- [Comparison] is made within [reference] because [scaling reason].

**Keep the meaning.** Shared endpoints do not imply identical intermediate values, objective accuracy, or numerical comparability across tasks. Has not begun, fully incomplete, and no progress has been made can differ in a formal definition, so preserve the chapter's meaning.

**Paper example** — [Progress, line 226](../reference_papers/Progress/Ro-MAN%202024.tex)

> A \textit{progress} value of 0 indicates that the task has not yet begun, while a value of 100 signifies task completion.

[All source examples for this pattern](source-evidence.md#shared-references-and-user-scales).

### Conditions attached to benefits

Keep the treatment or reference condition attached to the benefit. Name the processing method when properly handled would hide the actual operation. Distinguish a capability, a conditional intuition, and an observed result.

**Reusable forms**

- [Signal] can benefit learning when [processing condition].
- With [method], [signal] achieved [outcome] in [task].
- [Signal] would be more [property] if [design condition].

**Keep the meaning.** Do not delete when or if while tightening prose. Would cannot become does without evidence, and can does not promise performance across tasks.

**Paper example** — [STEADY, line 125](../reference_papers/STEADY/IEEEexample.tex)

> we compare scalar and binary feedback, and demonstrate that scalar feedback benefits learning when properly handled.

[All source examples for this pattern](source-evidence.md#conditions-attached-to-benefits).

### Correcting a sentence without rewording it

When a sentence that Hang wrote has a spelling or grammar error, correct the error and leave the rest of the sentence as it is. Keep the words, the sentence boundaries, the singular or plural, the modal verb, and the compound terms. If a rewording also seems useful, propose it as a separate suggestion with its own reason, so that the correction can be accepted without it. When a correction needs a new word, choose the word closest to the one Hang wrote. The same holds for slide text that Hang wrote or dictated, and for sentences that Hang edits by hand after a review. Corrections offered alone were accepted later for most of the errors whose rewording had been declined.

**Wording that Hang kept**

- This section introduces [topic] in two aspects. One is [A]. The other one is [B].
- Thus, future work can consider [verb]-ing [object] while using an approach similar to that of this dissertation.
- In addition, [change] can be beneficial.
- In human-chatbot interaction, a human and a chatbot interact in turns.
- whether the model would always benefit from [more data]
- Literature-grounded skills could allow [agent] to [use].
- When humans teach humans, people teach through [channels].

**Keep the meaning.** Keeping the wording does not mean keeping the error, so still offer the correction alone, in its smallest form. The review records each decision and the final wording, not the reason. That the rewording was the reason is a reading of what the declined versions changed. Ten of the eleven declined suggestions reworded an existing sentence, and seven of the ten were spelling or grammar items, so their corrections were declined together with the rewording. Text that an assistant drafted can be reworded more freely, as the accepted replacements under Literal wording show. Across the dissertation reviews of October 12 to 15, 2026, Hang declined 32 percent of the decided changes to passages taken from the papers and 19 percent of the changes to other passages. Among rewordings of new text in the Chapter 8 review, the rate was 9 percent. These rates count where a passage came from, not who wrote each word.

**Evidence from Hang** · weight 32 (2 edits, 7 declines, 3 acceptances)

- [DW-37](reviews/discussion-writing-review.md#dw-37), accepted with Hang's edit (weight 4). Suggested “whether the model continues to benefit from”. Hang's wording is “whether the model would always benefit from”. Hang accepted the grammar corrections in this sentence and put this phrase back.
- [DW-56](reviews/discussion-writing-review.md#dw-56), accepted with Hang's edit (weight 4). Suggested “Skills grounded in the literature could allow”. Hang's wording is “Literature-grounded skills could allow”.
- [DW-52](reviews/discussion-writing-review.md#dw-52), declined (weight 3). Suggested “In an interaction between a person and a chatbot, the two take turns”. Hang kept “In human-chatbot interaction, a human and a chatbot interact in turns”. The spelling corrections in the same suggestion were declined with it.
- [DW-25](reviews/discussion-writing-review.md#dw-25), declined (weight 3). Suggested “One group addresses”. Hang kept “One is future work that addresses”. The spelling corrections in the same suggestion were declined with it.
- [DW-26](reviews/discussion-writing-review.md#dw-26), declined (weight 3). Suggested “extending the learning framework to teaching modalities beyond evaluative feedback and demonstrations”. Hang kept “extending the learning framework to enable learning from teaching modalities beyond human evaluative feedback and human demonstrations”.
- [DW-38](reviews/discussion-writing-review.md#dw-38), declined (weight 3). Suggested “People can teach through many more channels and modalities”. Hang kept “When humans teach humans, people teach through many more channels and modalities”.
- [OA-101](reviews/overall-assessment-review.md#oa-101), declined (weight 3). Suggested “and such adaptation is usually achieved”. Hang kept “which are usually achieved”. The first sentence of the dissertation.
- [S03-S01](reviews/full-talk-wording-review.md#s03-s01), declined (weight 3). Suggested “robots need to learn from varied, imperfect teaching”. Hang kept “which means their teaching will be noisier and challenging for robots to learn”. Hang had dictated this slide line (HE-15).
- [TC-301](reviews/this-chapter-review.md#tc-301), declined (weight 3). Suggested “The related work is reviewed in \autoref{sec:bg-rlhf}”. Hang kept “The related work for this chapter is reviewed in \autoref{sec:bg-rlhf}”.
- [OA-806](reviews/overall-assessment-review.md#oa-806), accepted (weight 1). “limitations of the charpters in this dissertation or extentions” became “limitations of the chapters in this dissertation or extensions”. The corrections that DW-25 had declined, offered alone.
- [OA-810](reviews/overall-assessment-review.md#oa-810), accepted (weight 1). “interact in turns and comunicate” became “interact in turns and communicate”. One of the corrections that DW-52 had declined, offered alone.
- [S03-G01](reviews/full-talk-wording-review.md#s03-g01), accepted (weight 1). “noisier and challenging for robots to learn” became “noisier and more challenging for robots to learn from”. The grammar correction of the same line, offered alone.

**Basis.** This pattern comes from the evidence from Hang above. It has no paper example.

### This chapter as the subject

Keep This chapter as the subject of a verb that describes what the chapter itself does, such as argues, asks, analyzes, defines, focuses on, investigates, measures, builds on, and begins or completes a stage of this dissertation. Replace it when a more specific actor does the work, such as the results (The results demonstrate), a method (CHARM is proposed as), or an instrument (The codebook focuses on). Drop in this chapter where it only repeats the scope of the sentence, as in In this chapter, [parameter] is set to [value].

**Reusable forms**

- This chapter argues that [claim].
- This chapter asks whether [question].
- This chapter measures how [quantity], and examines whether [question].
- This chapter builds on these results and characterizes [signal], [description].
- The results demonstrate that [finding].
- [Method] is proposed as [description].
- In the experiments, [parameter] is set to [value].

**Keep the meaning.** Do not replace This chapter with a frame built on a noun, such as The question that follows is, the focus is, The study is based on the premise, The analysis uses, or Here, [term] is defined as. Hang declined each of these. Hang asked for this review because This chapter was used so many times, and then accepted 16 suggestions and declined 10. Hang's own later edits of two openings kept This chapter measures and This chapter builds on these results. A repeated This chapter in a chapter opening is acceptable. Whether This chapter showed should become The results of this chapter showed is undecided, since the same change was accepted once and declined once.

**Evidence from Hang** · weight 46 (1 instruction, 2 hand edits, 9 declines, 6 acceptances)

- [HI-08](preference-signals.md#hi-08), Hang's instruction, October 14, 2026 (weight 5). “"this chapter" has been used so many times, propose replacement suggestions”.
- [HE-08](preference-signals.md#he-08), Hang's own edit (weight 4). “Rather than reducing the variability of scalar feedback by reducing its information, this chapter measures” became “This chapter measures how inconsistent scalar feedback actually is”. TC-501 had proposed the approach taken here is to measure.
- [HE-09](preference-signals.md#he-09), Hang's own edit (weight 4). “This chapter builds on these results to design a signal” became “This chapter builds on these results and characterizes”. TC-602 had proposed These results motivate the design of a signal.
- [TC-305](reviews/this-chapter-review.md#tc-305), declined (weight 3). Suggested “The study is based on the premise that”. Hang kept “This chapter argues that”.
- [TC-401](reviews/this-chapter-review.md#tc-401), declined (weight 3). Suggested “The question that follows is whether”. Hang kept “This chapter asks whether”.
- [TC-403](reviews/this-chapter-review.md#tc-403), declined (weight 3). Suggested “the focus is on identifying”. Hang kept “this chapter focuses on identifying”.
- [TC-404](reviews/this-chapter-review.md#tc-404), declined (weight 3). Suggested “The analysis uses data from a public space study”. Hang kept “This chapter analyzes data from a public space study”.
- [TC-408](reviews/this-chapter-review.md#tc-408), declined (weight 3). Suggested “Here, non-optimal behaviors in human demonstrations are defined as”. Hang kept “This chapter defines non-optimal behaviors in human demonstrations as”.
- [TC-406](reviews/this-chapter-review.md#tc-406), declined (weight 3). Suggested “The premise is that”. Hang kept “The premise of this chapter is that”.
- [TC-413](reviews/this-chapter-review.md#tc-413), declined (weight 3). Suggested “One limitation of the analysis”. Hang kept “One limitation of this chapter”.
- [TC-412](reviews/this-chapter-review.md#tc-412), declined (weight 3). Suggested “defined above”. Hang kept “defined in this chapter”.
- [CP-08](reviews/connection-paragraph-review.md#cp-08), declined (weight 3). Suggested “The results of this chapter showed that the feedback non-experts give”. Hang kept “This chapter showed that the feedback non-experts give”.
- [TC-304](reviews/this-chapter-review.md#tc-304), accepted (weight 1). “This chapter demonstrates that” became “The results demonstrate that”.
- [TC-307](reviews/this-chapter-review.md#tc-307), accepted (weight 1). “this chapter proposes CHARM, a novel human feedback simulation method” became “CHARM is proposed as a novel human feedback simulation method”.
- [TC-410](reviews/this-chapter-review.md#tc-410), accepted (weight 1). “This chapter focuses on the following four types” became “The codebook focuses on the following four types”.
- [TC-506](reviews/this-chapter-review.md#tc-506), accepted (weight 1). “In this chapter, $k$ is set to $20$” became “In the experiments, $k$ is set to $20$”.
- [TC-704](reviews/this-chapter-review.md#tc-704), accepted (weight 1). “This chapter develops a reward learning framework, PHIRL,” became “PHIRL is a reward learning framework”.
- [CP-13](reviews/connection-paragraph-review.md#cp-13), accepted (weight 1). “This chapter showed that scalar feedback, once stabilized” became “The results of this chapter showed that scalar feedback, once stabilized”.

**Basis.** This pattern comes from the evidence from Hang above. It has no paper example.

### Qualifying a result

Qualify a sentence when it misstates what the evidence shows. Hang accepted this for a null result written as no difference, for a cause or intention that was not measured, for a guarantee, for a heading that claims more than its section, and for a result that one scenario established. Hang declined qualifications that narrow a positive result the chapter reports with a test, such as removing significantly from PHIRL significantly outperforms baselines or naming the one algorithm or domain of an evaluation. Hang also declined sentences added to say that evidence is weak. Offer the second kind as a question in the note of a review item, not as a change.

**Reusable forms**

- No significant difference in [measure] was detected between [A] and [B].
- [Behaviors] may be intentional.
- [Pattern] may help explain why [observation].
- A qualitative analysis illustrates how [mechanism] can discourage [examined behaviors].
- [Method] produced a more robust [object] in this scenario.

**Keep the meaning.** The counts come from the overall assessment of October 12, 2026, whose items of this kind Hang decided as 10 accepted, 1 accepted with an edit, and 9 declined. The same change to significantly outperforms was accepted in the opening of Chapter 7 and declined in Chapter 1, in a caption, and in the summary of Chapter 7. Hang's instruction of September 26, 2026 to report correlation values stands. It was accepted in Chapters 3 and 8 and declined in Chapter 1, where the suggestion also changed what was correlated. A decline is not a statement that the claim is correct, and the record of each review keeps the reason that was offered with the suggestion.

**Evidence from Hang** · weight 37 (1 instruction, 8 declines, 8 acceptances)

- [HI-01](preference-signals.md#hi-01), Hang's instruction, September 26, 2026 (weight 5). ““Robot experience and educational background showed positive associations with feedback accuracy, with correlations of 0.25 and 0.16, respectively.””.
- [OA-123](reviews/overall-assessment-review.md#oa-123), declined (weight 3). Suggested “PHIRL obtains higher returns than all four baselines”. Hang kept “PHIRL significantly outperforms IRL baselines”.
- [OA-713](reviews/overall-assessment-review.md#oa-713), declined (weight 3). Suggested “PHIRL obtains higher returns than the baselines in both domains”. Hang kept “PHIRL significantly outperforms baselines in both domains”.
- [OA-722](reviews/overall-assessment-review.md#oa-722), declined (weight 3). Suggested “PHIRL obtained higher returns than all four baselines”. Hang kept “PHIRL significantly outperformed baselines”.
- [OA-116](reviews/overall-assessment-review.md#oa-116), declined (weight 3). Suggested “an interactive reinforcement learning algorithm, TAMER, achieved higher performance”. Hang kept “interactive reinforcement learning algorithms can achieve higher performance”.
- [OA-721](reviews/overall-assessment-review.md#oa-721), declined (weight 3). Suggested “This study, conducted in the Lift domain, demonstrates”. Hang kept “This study demonstrates that PHIRL can benefit”.
- [OA-709](reviews/overall-assessment-review.md#oa-709), declined (weight 3). Suggested “PHIRL can still be applied with the remaining three alignments, although the ablation shows”. Hang kept “PHIRL can still be effective with the remaining three alignments”.
- [OA-606](reviews/overall-assessment-review.md#oa-606), declined (weight 3). Suggested “give only weak evidence for the absence of a difference”.
- [OA-108](reviews/overall-assessment-review.md#oa-108), declined (weight 3). Suggested “showed positive associations with feedback accuracy, with correlations of 0.25 and 0.16”. Hang kept “human evaluative feedback values are fairly correlated with human characteristics”.
- [OA-119](reviews/overall-assessment-review.md#oa-119), accepted (weight 1). “showed that providing *progress* to evaluate the robot's behavior does not require more workload” became “no significant difference in workload was detected between providing *progress* and providing scalar evaluative feedback”.
- [OA-408](reviews/overall-assessment-review.md#oa-408), accepted (weight 1). “are often intentional” became “may be intentional”.
- [OA-506](reviews/overall-assessment-review.md#oa-506), accepted (weight 1). “The uniqueness of the feedback pattern explains why” became “The uniqueness of the feedback pattern may help explain why”.
- [OA-710](reviews/overall-assessment-review.md#oa-710), accepted (weight 1). “the reward functions learned by PHIRL are shown to be robust to reward hacking in two representative scenarios” became “a qualitative analysis illustrates how *progress* alignment can discourage two examined reward-hacking behaviors”.
- [OA-718](reviews/overall-assessment-review.md#oa-718), accepted (weight 1). “\subsection{PHIRL Learns More Robust Reward Functions}” became “\subsection{Reward Functions in Two Reward Hacking Scenarios}”.
- [OA-719](reviews/overall-assessment-review.md#oa-719), accepted (weight 1). “PHIRL produced a more robust reward function” became “PHIRL produced a more robust reward function in this scenario”.
- [OA-305](reviews/overall-assessment-review.md#oa-305), accepted (weight 1). “are fairly correlated with feedback accuracy and feedback values” became “with correlations of 0.25 and 0.16, respectively”.
- [OA-703](reviews/overall-assessment-review.md#oa-703), accepted (weight 1). “PHIRL significantly outperforms IRL baselines” became “PHIRL obtains higher returns than all four baselines”.

**Basis.** This pattern comes from the evidence from Hang above. It has no paper example.

## Writing style

### Practical purpose

Ground motivation in what a robot needs to learn, what users can provide, and what makes the learning difficult. The recurring practical stakes are deployment beyond the lab, data requirements, and human teaching effort. Move from that requirement to the obstacle and the research response.

**Reusable forms**

- To [deployment goal], robots need to [capability].
- [Teaching source] makes [benefit] possible, but [difficulty] limits [outcome].
- The goal of this chapter is to [research action] so that [practical purpose].

**Keep the meaning.** A practical motivation is not evidence of deployment success. Preserve theoretical motivation when it is the contribution, and avoid opening every paragraph with the same purpose clause.

**Paper example** — [PROG, line 117](../reference_papers/Progress/Ro-MAN%202024.tex)

> Perfect demonstrations are hard to obtain while purely learning from human feedback requires many human labels, often obtained at significant time and expense.

[All source examples for this pattern](source-evidence.md#practical-purpose).

### Direct subjects and concrete details

State what was done, what was found, and why it matters. Use the study, method, participants, or results as the sentence subject. Open a sentence with its subject, not with a That clause. Follow an abstract claim with the task, object, count, or observation that makes it inspectable. Reuse study examples in discussion when they help explain a broader point.

**Reusable forms**

- Participants [action] during [task].
- [Method] transforms [input] into [output].
- In [study], [concrete observation] illustrates [bounded point].
- The expectation that [claim] is therefore an inference from [basis], and not a measured result.

**Keep the meaning.** Use enough nouns to make the claim clear without repeating every detail. Pronouns and shorter labels remain useful when their referents are unmistakable. Concrete detail must come from the study, not from a plausible invented scenario.

**Evidence from Hang** · weight 2 (2 acceptances)

- [DW-24](reviews/discussion-writing-review.md#dw-24), accepted (weight 1). “That *progress* alignment discounts sidetracks is therefore an inference” became “The expectation that *progress* alignment discounts sidetracks is therefore an inference”.
- [DW-02](reviews/discussion-writing-review.md#dw-02), accepted (weight 1). “Feedback accuracy was associated with who the teacher was” became “Feedback accuracy was associated with the characteristics of the teacher”.

**Paper example** — [CHARM, line 55](../reference_papers/CHARM/ROMAN%202025.tex)

> We conducted a public space study with two long-horizon tasks and 46 participants.

[All source examples for this pattern](source-evidence.md#direct-subjects-and-concrete-details).

### Describing human teaching without blame

Describe the signal or behavior precisely, then identify the relevant task demand, interface constraint, or plausible explanation. Distinguish an inefficient but useful accommodation from a harmful error when the evidence allows it.

**Reusable forms**

- When [interaction demand], users may [behavior] because [supported constraint].
- [Behavior] is inefficient relative to [reference], but can help users [purpose].

**Keep the meaning.** Do not call a person unreliable when the measured property belongs to their feedback. Constructive explanation does not require excusing errors or inferring intent. State whether a reason was measured, interpreted, or hypothesized.

**Evidence from Hang** · weight 4 (1 edit)

- [DW-18](reviews/discussion-writing-review.md#dw-18), accepted with Hang's edit (weight 4). “A human demonstrator who is unsure at such a point pauses” became “At such a step, a human demonstrator may pause”. The studies recorded the pauses and alignments, not whether a demonstrator was unsure.

**Paper example** — [RSS, line 94](../reference_papers/prospectus/RSS%20Pioneers%202026.tex)

> We found that non-expert demonstrations, while noisy, do not necessarily mean failures or errors.

[All source examples for this pattern](source-evidence.md#describing-human-teaching-without-blame).

### Explaining the mechanism

Make confidence come from an understandable computation with its input, operation, and output. Give the intuition in ordinary language and explain how the method implements it. Put the evaluation claim in a separate sentence with its task and comparison.

**Reusable forms**

- The intuition is that [relationship between known quantities].
- [Method] transforms [input] into [output] by [operation].
- This makes [information] available to [downstream process].

**Keep the meaning.** A mechanism and a measured benefit are different claims. Effective, novel, and robust do not explain the computation. An analogy should return promptly to the actual method.

**Paper example** — [STEADY, line 196](../reference_papers/STEADY/IEEEexample.tex)

> The key insight of STEADY is to use a multi-distributional model for scalar feedback,  re-normalizing noisy scalar feedback to confidence scores (i.e. more precise magnitudes) and recovering positive/negative labels.

[All source examples for this pattern](source-evidence.md#explaining-the-mechanism).

### Observation interpretation and explanation

Separate direct measurement from its interpretation and from a possible cause. Report the observation firmly within its evaluated scope. Use a qualified interpretation for what it means, and possibility language for a mechanism that was not tested.

**Reusable forms**

- In [condition], [measured object] [observed result].
- This pattern suggests that [interpretation].
- One possible explanation is [untested mechanism].

**Keep the meaning.** Do not weaken a direct observation with unnecessary may, or strengthen an association into causation. Keep participant, task, training, and evaluation conditions that materially limit the claim. Separating an observation from its interpretation does not require two sentences. Hang kept a result and its interpretation in one sentence, joined by which suggests that.

**Evidence from Hang** · weight 4 (1 edit)

- [DW-36](reviews/discussion-writing-review.md#dw-36), accepted with Hang's edit (weight 4). Suggested “This suggests that annotations differ in how informative they are”. Hang's wording is “which suggests that annotations differ in how informative they are”.

**Paper example** — [SIDE, line 327](../reference_papers/Demonstration_sidetracks/main.tex)

> This is possibly due to the requirement for control accuracy, which resulted in more alignment to get to the desired positions and more pauses for reaction.

[All source examples for this pattern](source-evidence.md#observation-interpretation-and-explanation).

### Emphasis

Use italics for progress as a technical signal and, selectively, a key intuition. Use bold for an established run-in heading or a concise takeaway where the chapter format calls for it. Quotation marks can identify informal labels, such as harmless explorations, when the label needs that status.

**Reusable forms**

- *Progress* describes [quantity].
- *The key intuition is that [relationship].*
- **[Finding or hypothesis label].** [Explanation].

**Keep the meaning.** Emphasize sparingly, because repeated bold or italic sentences compete for attention. The source library's once-per-paragraph advice is a restraint on rhetorical emphasis, not a ban on repeated formatting of a defined technical term. Follow the dissertation's existing LaTeX conventions.

**Paper example** — [PROG, line 440](../reference_papers/Progress/Ro-MAN%202024.tex)

> Participants used scalar feedback to indicate if a demonstration was clean and good, but the possibility that the errors were 'harmless explorations' or 'fixable mistakes' is not captured by scalar feedback.

[All source examples for this pattern](source-evidence.md#emphasis).

### Literal wording

Use literal verbs to state the relationship between findings, such as suggest, are consistent with, help explain, were evaluated separately, and provided. Prefer concrete scenarios to figurative summaries. If an analogy is useful, announce it and identify the correspondence to the method.

**Reusable forms**

- These findings suggest [connection].
- The results are consistent with [earlier evidence].
- [Components] were evaluated separately.
- Participants provided [annotations / feedback].
- Together, these findings suggest [connection].
- The results of [studies] are consistent with each other.
- Both approaches provide [references], but they describe different quantities.
- [Demonstrations] failed at similar kinds of steps.

**Keep the meaning.** Prefer these forms to read together, point in the same direction, link by link, by two routes, the two routes, supplied, were lost at, or a sense in which when matching this reference. Each of these replacements was accepted in the Chapter 8 review. Their absence from a limited corpus is a style observation, not a universal grammatical prohibition. Do not remove a literal contrast that carries the scientific argument.

**Evidence from Hang** · weight 18 (1 instruction, 2 edits, 5 acceptances)

- [HI-04](preference-signals.md#hi-04), Hang's instruction, October 12, 2026 (weight 5). “suggestING improvement FOR THE AI WRITING TO MAKE THEM LESS AI LIKE”.
- [DW-23](reviews/discussion-writing-review.md#dw-23), accepted with Hang's edit (weight 4). “the argument was tested link by link” became “the stages of the argument were evaluated separately”.
- [DW-06](reviews/discussion-writing-review.md#dw-06), accepted with Hang's edit (weight 4). “by two routes” became “in two ways”.
- [DW-04](reviews/discussion-writing-review.md#dw-04), accepted (weight 1). “Read together, the two studies point to three sources of structure” became “Together, these findings suggest three sources of structure”.
- [DW-15](reviews/discussion-writing-review.md#dw-15), accepted (weight 1). “point in the same direction” became “are consistent with each other”.
- [DW-09](reviews/discussion-writing-review.md#dw-09), accepted (weight 1). “The two routes supply references” became “Both approaches provide references”.
- [DW-17](reviews/discussion-writing-review.md#dw-17), accepted (weight 1). “were lost at similar kinds of points” became “failed at similar kinds of steps”.
- [DW-13](reviews/discussion-writing-review.md#dw-13), accepted (weight 1). “suggests a sense in which imperfect teaching can be used and not only tolerated” became “illustrates how imperfect teaching can be used rather than only tolerated”.

**Paper example** (the explicitly announced analogy) — [PH-INT, line 37](../reference_papers/PHIRL/introduction.tex)

> This process mimics human learning: much like a student cross-referencing answers to correct their own solutions, the method generates a potential reward function and compares it against human feedback to refine its learned rewards.

[All source examples for this pattern](source-evidence.md#literal-wording).

### Chapter openings

Open a research chapter with one sentence that places it in the three stages, such as This chapter completes the first stage of this dissertation. Then give the chapter's own introduction. State the gap in prior work, the key insight or the aim and hypothesis, what the chapter investigates or proposes, the study with its participants and task, the main findings, and what the findings are useful for. Say where the code and data are, and end the opening with the related-work pointer and the originally published as line. There is no separate Introduction heading. When revising an opening, move and cut sentences rather than writing new ones.

**Reusable forms**

- This chapter completes the [first] stage of this dissertation.
- This chapter begins the second stage of this dissertation, [stage name], by revisiting [design choice], which is [choice].
- This chapter completes the second stage of this dissertation by formalizing [signal].
- This chapter presents the final stage of this dissertation, which is to [aim]. Thus, this chapter proposes [method], [description].
- The main contributions of this chapter are [contributions].
- The related work for this chapter is reviewed in [section], and the work presented in this chapter was originally published as ``\textbf{[title]}''~\cite{[key]}.

**Keep the meaning.** This is the order Hang used when restructuring the openings of Chapters 3 to 7 on October 14 and 15, 2026, and it is a default rather than a rule. In those edits, the summary paragraph that an assistant had written at the head of Chapters 4, 5, and 7 gave way to the introduction text of the paper. Keep one statement of the aim or the contributions right after the stage sentence. Keep the study summary with its participant counts and its main result even when a later section repeats them. Hang declined cuts of each of these. A sentence that repeats one a few lines earlier, general background on learning from demonstration, and a second statement of the findings were cut.

**Evidence from Hang** · weight 66 (3 instructions, 4 hand edits, 1 edit, 9 declines, 4 acceptances)

- [HI-10](preference-signals.md#hi-10), Hang's instruction, October 15, 2026 (weight 5). “mostly focus on re-orgnizing (moving sentences around), and cut, avode creating new ones”.
- [HI-02](preference-signals.md#hi-02), Hang's instruction, September 26, 2026 (weight 5). “Reduce the feeling of repeatedly starting a new paper”.
- [HI-09](preference-signals.md#hi-09), Hang's instruction, October 15, 2026 (weight 5). “the introduction section in chapter 3 to chapter 7 are redundant with the pre-face paragraphs”.
- [HE-07](preference-signals.md#he-07), Hang's own edit (weight 4). “It analyzes demonstrations of a long-horizon manipulation task provided by 40 non-experts” became “The main contributions of this chapter are characterizing and categorizing non-optimal behaviors”.
- [HE-10](preference-signals.md#he-10), Hang's own edit (weight 4). “which leverages imperfect non-expert teaching for learning” became “which is to to learn robust reward functions by combining human demonstrations and feedback”. The aim moved into the stage sentence.
- [HE-10](preference-signals.md#he-10), Hang's own edit (weight 4). “It proposes *Progress*-Heuristicized” became “Thus, this chapter proposes *Progress*-Heuristicized”. The summary sentence gave way to the proposal sentence of the paper.
- [HE-11](preference-signals.md#he-11), Hang's own edit (weight 4). “It investigates whether the characteristics of individual teachers” became “This chapter investigates whether the characteristics of individual teachers”. Hang moved the sentence after the gap and the aim.
- [HE-13](preference-signals.md#he-13), Hang's own edit (weight 4). Twelve of the 17 cuts of the opening-overlap review were applied by hand, including both Introduction headings.
- [C6-01](reviews/opening-reorder-review.md#c6-01), accepted with Hang's edit (weight 4). Suggested “This chapter completes the second stage of this dissertation. Learning”. Hang's wording is “This chapter completes the second stage of this dissertation by formalizing progress”.
- [C5-01](reviews/opening-reorder-review.md#c5-01), declined (weight 3). Suggested “This chapter begins the second stage of this dissertation, mitigating noise in human feedback”. Hang kept “by revisiting a design choice made by many interactive reinforcement learning methods”.
- [C5-03](reviews/opening-reorder-review.md#c5-03), declined (weight 3). Suggested “evaluating a robot performing a manipulation task”. Hang kept “and the results show that scalar feedback has the potential to improve learning when properly handled”.
- [C6-03](reviews/opening-reorder-review.md#c6-03), declined (weight 3). Suggested “and one public space study”. Hang kept “in which 40 passersby provided and then evaluated their own demonstrations”.
- [C6-04](reviews/opening-reorder-review.md#c6-04), declined (weight 3). Hang kept “The validation studies covered a wide range of scenarios and involved 116 participants in total”. The suggestion cut the sentence.
- [C7-01](reviews/opening-reorder-review.md#c7-01), declined (weight 3). Hang kept “This chapter aims to learn robust reward functions”. The suggestion moved the aim after the background on reward functions.
- [C4-03](reviews/opening-reorder-review.md#c4-03), declined (weight 3). Hang kept “The main contributions of this chapter are characterizing and categorizing non-optimal behaviors in human demonstrations”. The suggestion moved the contribution statement after the procedure for identifying sidetracks.
- [C5-02](reviews/opening-reorder-review.md#c5-02), declined (weight 3). Hang kept “However, only binary feedback has been widely used in prior work”. The suggestion cut these sentences, and Hang later cut them by hand when restructuring the opening (OV-501 in HE-13).
- [C7-02](reviews/opening-reorder-review.md#c7-02), declined (weight 3). Hang kept “Prior reward learning work often relies on preference feedback”. The suggestion moved the problem with preference feedback before the proposal of PHIRL.
- [TC-405](reviews/this-chapter-review.md#tc-405), declined (weight 3). Suggested “These findings will be beneficial for future LfD algorithm development”. Hang kept “This chapter systematically characterizes non-experts' non-optimal manipulation patterns”. The suggestion deleted a sentence that repeated the contribution statement.
- [C4-02](reviews/opening-reorder-review.md#c4-02), accepted (weight 1). “In this chapter, this assumption is examined using the 40 demonstrations” was cut.
- [C4-04](reviews/opening-reorder-review.md#c4-04), accepted (weight 1). “The analysis also shows that \thingname{} are not randomly distributed” was cut.
- [C7-03](reviews/opening-reorder-review.md#c7-03), accepted (weight 1). “and a qualitative analysis illustrates how *progress* alignment can discourage two reward hacking behaviors” was cut.
- [C5-04](reviews/opening-reorder-review.md#c5-04), accepted (weight 1). “The related work is reviewed in \autoref{sec:RW}” was moved. The publication note went to the end of the opening (C5-05).

**Basis.** This pattern comes from the evidence from Hang above. It has no paper example.

### Study overview tables

Keep each cell of a study overview short and leave procedures to the chapter, with a caption that says so. Keep what a reader needs to compare the studies, which is the setting with its place, the size of each participant group, any pilot, and the word non-expert where it describes the participants. Write a cell as a phrase that reads on its own, such as Annotators watched replays of the demonstrations in simulation, rather than a clipped fragment such as Replays in simulation.

**Reusable forms**

- Public space, university atrium
- 90 crowdworkers (45 per condition); 3-expert pilot
- 40 non-expert passersby
- In person, 2 worse, 2 okay, 2 better
- The procedure of each study is described in its chapter.

**Keep the meaning.** These choices come from one table, the overview in the conclusion, where Hang accepted 18 of 19 suggestions and edited 8 of the row suggestions. Hang removed procedural details such as the controller, the sampling rate, and the scale ranges, so their absence from a cell is intended. A participant cell may keep a semicolon between two groups of people.

**Evidence from Hang** · weight 33 (8 edits, 1 acceptance)

- [CT-08](reviews/conclusion-table-review.md#ct-08), accepted with Hang's edit (weight 4). Suggested “& Public space &”. Hang's wording is “Public space, university atrium”.
- [CT-05](reviews/conclusion-table-review.md#ct-05), accepted with Hang's edit (weight 4). Suggested “& 90 crowdworkers \\”. Hang's wording is “90 crowdworkers (45 per condition); 3-expert pilot”.
- [CT-09](reviews/conclusion-table-review.md#ct-09), accepted with Hang's edit (weight 4). Suggested “& Replays in simulation &”. Hang's wording is “Annotators watched replays of the demonstrations in simulation”.
- [CT-04](reviews/conclusion-table-review.md#ct-04), accepted with Hang's edit (weight 4). Suggested “& Replays in simulation &”. Hang's wording is “public space demonstrations replayed in simulation and annotated with a codebook”.
- [CT-10](reviews/conclusion-table-review.md#ct-10), accepted with Hang's edit (weight 4). Suggested “& In person &”. Hang's wording is “In person, 2 worse, 2 okay, 2 better”.
- [CT-03](reviews/conclusion-table-review.md#ct-03), accepted with Hang's edit (weight 4). Suggested “& Public space &”. Hang's wording is “Public space, university atrium”.
- [CT-06](reviews/conclusion-table-review.md#ct-06), accepted with Hang's edit (weight 4). Suggested “& 40 crowdworkers \\”. Hang's wording is “40 crowdworkers (20 per condition)”.
- [CT-07](reviews/conclusion-table-review.md#ct-07), accepted with Hang's edit (weight 4). Suggested “& 36 crowdworkers \\”. Hang's wording is “36 crowdworkers (18 per condition)”.
- [CT-01](reviews/conclusion-table-review.md#ct-01), accepted (weight 1). “Overview of the studies conducted in this dissertation. }” became “The procedure of each study is described in its chapter”.

**Basis.** This pattern comes from the evidence from Hang above. It has no paper example.

### Adding sentences that were not asked for

Prefer moving, cutting, and correcting Hang's sentences to writing new ones. Add a sentence when Hang asks for the content, as with the short description of the success-rate figure, or when the chapter lacks a fact that its own results depend on, such as the scale on which feedback was collected or how accuracy was computed. Keep requested additions minimal.

**Reusable forms**

- In these studies, scalar feedback was collected on the same range as progress, from 0 to 100.
- The success rates of all methods are presented in [figure], where the success rate is [definition].

**Keep the meaning.** Of ten sentences or passages that assistants inserted into the chapters without being asked, Hang declined seven. They were limitations, a statement that evidence was weak, a result that Hang had asked to drop, a sentence that mapped a summary to later chapters, and a drafted subsection. The three accepted ones supplied a missing fact or were an optional draft for a subsection that Hang had listed. Additions that Hang asked for were accepted, and so were bibliography entries.

**Evidence from Hang** · weight 39 (3 instructions, 7 declines, 3 acceptances)

- [HI-10](preference-signals.md#hi-10), Hang's instruction, October 15, 2026 (weight 5). “avode creating new ones”.
- [HI-07](preference-signals.md#hi-07), Hang's instruction, October 14, 2026 (weight 5). “with a minimal text description add to dissertation”.
- [HI-19](preference-signals.md#hi-19), Hang's instruction, September 26, 2026 (weight 5). “drop it as well”.
- [OA-310](reviews/overall-assessment-review.md#oa-310), declined (weight 3). Suggested “part of the improvement may come from learning how individual participants rate”.
- [OA-411](reviews/overall-assessment-review.md#oa-411), declined (weight 3). Suggested “an agreement statistic between the annotators is not reported”.
- [OA-712](reviews/overall-assessment-review.md#oa-712), declined (weight 3). Suggested “The mixed-quality datasets are therefore used in this chapter in place of demonstrations from non-experts”.
- [OA-606](reviews/overall-assessment-review.md#oa-606), declined (weight 3). Suggested “give only weak evidence for the absence of a difference”.
- [OA-717](reviews/overall-assessment-review.md#oa-717), declined (weight 3). Suggested “removing completion shaping resulted in the largest performance drop of all terms”. Hang had asked on September 26, 2026 to drop this result, as the updated paper does.
- [CP-06](reviews/connection-paragraph-review.md#cp-06), declined (weight 3). Suggested “The chapters that follow address the three points listed above in order”.
- [DW-43](reviews/discussion-writing-review.md#dw-43), declined (weight 3). An optional subsection drafted without a note from Hang.
- [OA-603](reviews/overall-assessment-review.md#oa-603), accepted (weight 1). Accepted “scalar feedback was collected on the same range as progress, from 0 to 100”.
- [OA-306](reviews/overall-assessment-review.md#oa-306), accepted (weight 1). Accepted “The reward was discretized by partitioning its range into five equal segments”.
- [SR-02](reviews/phirl-success-rate-review.md#sr-02), accepted (weight 1). Accepted “The success rates of all methods are presented in \autoref{fig:phirl_succ_rate}”.

**Basis.** This pattern comes from the evidence from Hang above. It has no paper example.

## Sentence style

### One main job and varied sentence length

Give each sentence one main rhetorical job, while allowing a related comparison, condition, or explanation to remain attached. Use a claim followed by a contrast or explanation. Split a sentence when it reports two studies, two findings, or two requirements. Keep a result in the same sentence as the which clause that identifies or interprets it. Keep a chain of results joined by but in one sentence, and keep a numbered list of questions, findings, or premises in the one sentence that introduces it. Longer sentences are useful for a matched comparison or a coherent list, and short sentences can mark a conclusion.

**Reusable forms**

- [Claim]. However, [specific cost or boundary].
- [Modeling choice] can lead to [consequence]. [Affected methods] may therefore [specific difficulty].
- [Finding of study A] ([chapter A]). [Finding of study B] ([chapter B]).
- [Result] ([chapter]), which suggests that [bounded interpretation].

**Keep the meaning.** The Claude library reports sentences around 20 words as a corpus tendency, not a target. Do not split a condition from its claim or impose a word limit on every sentence. One job per sentence is not a reason to shorten every long sentence. In the Chapter 8 review, Hang rejoined two which clauses that had been split off and declined the split of a while contrast.

**Evidence from Hang** · weight 29 (4 edits, 4 declines, 1 acceptance)

- [DW-07](reviews/discussion-writing-review.md#dw-07), accepted with Hang's edit (weight 4). “and in the public space study the average standard deviation” became “In the public space study, the average standard deviation”. Two studies became two sentences.
- [DW-34](reviews/discussion-writing-review.md#dw-34), accepted with Hang's edit (weight 4). “a short, clear one, and any human effort needed to identify candidates” became “Any human effort needed to identify candidates”. Two requirements became two sentences.
- [DW-19](reviews/discussion-writing-review.md#dw-19), accepted with Hang's edit (weight 4). Suggested “precise contacts such as grasps. These are the steps that the magnitude term”. Hang's wording is “precise contacts such as grasps, which are the steps that the magnitude term”.
- [DW-36](reviews/discussion-writing-review.md#dw-36), accepted with Hang's edit (weight 4). Suggested “This suggests that annotations differ”. Hang's wording is “which suggests that annotations differ”.
- [DW-29](reviews/discussion-writing-review.md#dw-29), declined (weight 3). Suggested “from its users. A robot also needs to learn”. Hang kept “from the users, while robots also need to learn”.
- [CR-04](reviews/conclusion-table-review.md#cr-04), declined (weight 3). Suggested “was detected between the two. Scalar feedback processed by STEADY”. Hang kept “was detected between the two, and scalar feedback processed by STEADY”.
- [PR-001](reviews/punctuation-reduction-review.md#pr-001), declined (weight 3). Suggested “The first stage asks whether”. Hang kept “Each stage addresses one question: whether”.
- [PR-010](reviews/punctuation-reduction-review.md#pr-010), declined (weight 3). Suggested “Prior work widely uses interactive information from humans in several forms”. Hang kept “Interactive information in various forms from humans is widely used in prior work:”.
- [CR-03](reviews/conclusion-table-review.md#cr-03), accepted (weight 1). “the characteristics of the teacher, and CHARM, a model” became “the characteristics of the teacher. CHARM, a model”. Two findings became two sentences.

**Paper example** — [SIDE, line 222](../reference_papers/Demonstration_sidetracks/main.tex)

> Participants were recruited from random people walking past the experiment setup.

[All source examples for this pattern](source-evidence.md#one-main-job-and-varied-sentence-length).

### A short verdict after the evidence

After giving the numbers and the interpretation needed to judge them, a short sentence can state the outcome. The verdict should add closure rather than repeat the full result.

**Reusable forms**

- H2 is supported.
- H3 is not supported.
- The feedback is therefore uninformative under [condition].

**Keep the meaning.** Brevity must not hide the criterion or broaden the claim. Use therefore only when the preceding evidence supports the inference.

**Paper example** — [PROG, line 378](../reference_papers/Progress/Ro-MAN%202024.tex)

> H2 is supported.

[All source examples for this pattern](source-evidence.md#a-short-verdict-after-the-evidence).

### An example in a few connected sentences

Use For instance or For example to introduce one concrete case, explain what happens, and state what the case illustrates. An example can occupy one longer sentence or several shorter sentences when the reader needs to track several relations.

**Reusable forms**

- For instance, consider [task] where [condition]. In this case, [consequence]. This illustrates [distinction].
- For example, [case A] may be perceived differently from [case B], although [shared property].

**Keep the meaning.** Mark a hypothetical case as hypothetical. An invented robot episode cannot be reported as observed study data. Do not leave the reader to infer which detail supports the claim.

**Evidence from Hang** · weight 1 (1 acceptance)

- [DW-50](reviews/discussion-writing-review.md#dw-50), accepted (weight 1). “a child may provide less force and requires a lower robot height compared to an adult” became “a child may provide less force than an adult and may require the robot to hold the object lower”. The example stayed introduced by For instance, which marks it as hypothetical.

**Paper example** — [PROG, line 594](../reference_papers/Progress/Ro-MAN%202024.tex)

> For instance, one participant failed to pour the toppings into the ice cream because the grasp point was not optimal.

[All source examples for this pattern](source-evidence.md#an-example-in-a-few-connected-sentences).

### Few colons and semicolons

Use few colons and semicolons. Hang stated this preference on October 12, 2026, after the Chapter 8 review, and it takes priority over the punctuation of the papers and of earlier drafts. Before writing either mark, try to state the relation in words. A relative clause (which is to, which are) can introduce what a colon would introduce. Since or because can attach a reason, and such as or including can attach examples. Whereas, while, or but can carry a contrast that a semicolon would carry, and a second statement can be a new sentence. A colon remains suitable when a complete lead-in announces a list of several items or a term. Semicolons remain suitable between the items of a long list whose items contain commas.

**Reusable forms**

- [Design choice] recurs in [chapters], which is to [operation].
- [Claim], since [reason].
- [Statement about A], whereas [statement about B].
- [General statement], for instance, [case].
- [Statement]. [Second statement].
- [Strategy] would be compared with several [baselines]: [item A, with detail]; [item B]; and [item C].

**Keep the meaning.** This is a preference for fewer marks, not a ban, and the punctuation review of October 12, 2026 showed where the line is. Hang kept a colon in four places. The first is before a numbered or listed set of questions, findings, premises, or alternatives, such as Each stage addresses one question: whether ... The second is after The key intuition is that, before the emphasized statement of the intuition. The third is after a sentence that names a property, such as is operational or suggests the underlying reasons, before the clause that spells it out. The fourth is before a quotation. Hang accepted removing a colon after a verb or a preposition, such as are and between, joining a short list to its sentence with such as, including, namely, or by, and splitting two complete statements at a colon or semicolon, as in a chapter roadmap. Hang also accepted replacing every em dash that was reviewed, with a comma, a which clause, or a new sentence. Do not put a dash or a pair of parentheses where the colon or semicolon was, since the sentence would keep the same break. Do not join two statements with and when their relation is a reason or a contrast. Name the relation. Punctuation inside equations, citations, headings, LaTeX commands, and quoted source text is outside this preference.

**Evidence from Hang** · weight 74 (1 instruction, 10 edits, 7 declines, 8 acceptances)

- [HI-05](preference-signals.md#hi-05), Hang's instruction, October 12, 2026 (weight 5). “use less ":" and ";"”.
- [DW-16](reviews/discussion-writing-review.md#dw-16), accepted with Hang's edit (weight 4). Suggested “a design choice that recurs in the later chapters: comparing a value”. Hang's wording is “a design choice that recurs in the later chapters, which is to compare a value”.
- [DW-32](reviews/discussion-writing-review.md#dw-32), accepted with Hang's edit (weight 4). Suggested “since they may be the most informative: low-quality demonstrations can inform completion shaping”. Hang's wording is “should be prioritized for annotations, since low-quality demonstrations can inform completion shaping”.
- [DW-14](reviews/discussion-writing-review.md#dw-14), accepted with Hang's edit (weight 4). Suggested “which are not visible from any single study: differences between teachers in the magnitude of feedback”. Hang's wording is “This section describes the connections between chapters, which are not visible from any single study”. Hang removed the list that the colon introduced.
- [DW-18](reviews/discussion-writing-review.md#dw-18), accepted with Hang's edit (weight 4). “and then continues; an agent that optimizes a reward” became “before continuing, whereas an agent that optimizes a reward”.
- [DW-33](reviews/discussion-writing-review.md#dw-33), accepted with Hang's edit (weight 4). Kept “several baseline strategies: random selection”. A list of five strategies, one of which contains a comma, kept its colon and its semicolons.
- [OA-122](reviews/overall-assessment-review.md#oa-122), accepted with Hang's edit (weight 4). Suggested “The key intuition is that *reward”. Hang's wording is “The key intuition is that: *reward”. Hang accepted the lower-case reward and put the colon back.
- [CP-14](reviews/connection-paragraph-review.md#cp-14), accepted with Hang's edit (weight 4). Suggested “suggests the underlying reasons. Feedback is associated with”. Hang's wording is “suggests the underlying reasons: feedback is associated with”.
- [PR-012](reviews/punctuation-reduction-review.md#pr-012), accepted with Hang's edit (weight 4). Suggested “refers to methods that have three components, namely”. Hang's wording is “LfHF, in general, have three components, namely”. Hang also cut refers to methods that.
- [PR-017](reviews/punctuation-reduction-review.md#pr-017), accepted with Hang's edit (weight 4). Suggested “or robot behaviors. It also depends”. Hang's wording is “or robot behaviors, it also depends”. Hang chose a comma over a new sentence.
- [OA-802](reviews/overall-assessment-review.md#oa-802), accepted with Hang's edit (weight 4). Kept “have structured sources, which are the teacher's characteristics”. Which are took the place of a comma before the list, and Hang removed its third item.
- [DW-42](reviews/discussion-writing-review.md#dw-42), declined (weight 3). Suggested “complement one another: for instance, whether pauses”. Hang kept “complement one another, for instance, whether pauses”.
- [PR-005](reviews/punctuation-reduction-review.md#pr-005), declined (weight 3). Suggested “The key intuition is that *Reward”. Hang kept “The key intuition is that: *Reward”.
- [PR-007](reviews/punctuation-reduction-review.md#pr-007), declined (weight 3). Suggested “provided by *progress*. First, positive”. Hang kept “provided by *progress*: 1) positive”.
- [PR-004](reviews/punctuation-reduction-review.md#pr-004), declined (weight 3). Suggested “They also suggest that demonstration imperfections”. Hang kept “prediction accuracy; and 2) demonstration imperfections”.
- [PR-014](reviews/punctuation-reduction-review.md#pr-014), declined (weight 3). Suggested “in two major ways, namely (1)”. Hang kept “in two major ways: (1)”.
- [PR-108](reviews/punctuation-reduction-review.md#pr-108), declined (weight 3). Suggested “is operational. A person would not need”. Hang kept “is operational: a person would not need”.
- [OA-720](reviews/overall-assessment-review.md#oa-720), declined (weight 3). Suggested “the key idea of ReWiND, which is to use language instructions”. Hang kept “the key idea of ReWiND: ``use language instructions”. The colon before a quotation stayed.
- [PR-002](reviews/punctuation-reduction-review.md#pr-002), accepted (weight 1). “The six domains are: trust in robots” became “The six domains are trust in robots”.
- [PR-006](reviews/punctuation-reduction-review.md#pr-006), accepted (weight 1). “alternates between: learning” became “alternates between learning”.
- [PR-104](reviews/punctuation-reduction-review.md#pr-104), accepted (weight 1). “acts on the robot or on its data: a trained policy” became “acts on the robot or on its data, such as a trained policy”.
- [PR-015](reviews/punctuation-reduction-review.md#pr-015), accepted (weight 1). “has multiple advantages: it enables” became “has multiple advantages. It enables”.
- [PR-110](reviews/punctuation-reduction-review.md#pr-110), accepted (weight 1). “involves no interaction: the robot can assemble” became “involves no interaction. The robot can assemble”.
- [PR-008](reviews/punctuation-reduction-review.md#pr-008), accepted (weight 1). “(the background for \autoref{ch:charm}); \autoref{sec:bg-lfd}” became “(the background for \autoref{ch:charm}). \autoref{sec:bg-lfd}”.
- [DR-001](reviews/dash-reduction-review.md#dr-001), accepted (weight 1). “personality model—comprising openness” became “personality model, which comprises openness”.
- [DR-002](reviews/dash-reduction-review.md#dr-002), accepted (weight 1). “could also play a role—those with higher trust” became “could also play a role. Those with higher trust”.

**Paper example** (a colon before an announced term, the use that remains) — [PROG, line 93](../reference_papers/Progress/Ro-MAN%202024.tex)

> In this work, we characterize and test a little-used teaching signal: *progress*

[All source examples for this pattern](source-evidence.md#few-colons-and-semicolons).

### Parentheses for supporting specifics

Put a compact example, count, abbreviation, or test statistic in parentheses when the main clause remains understandable without it. Use e.g., for examples and i.e., for a restatement.

**Reusable forms**

- Participants viewed [stimuli] ([brief composition]).
- [Main result] ([test statistic and uncertainty, when reported]).

**Keep the meaning.** Keep essential scope and conditions in the sentence rather than hiding them in a long aside. Parentheses should not carry a second argument.

**Paper example** — [STEADY, line 158](../reference_papers/STEADY/IEEEexample.tex)

> Scalar feedback, on the other hand, is also naturally used in daily life (e.g., movie rating and product evaluation) but encodes information beyond that in binary feedback, such as ranking and magnitude, through a wider range of possible values.

[All source examples for this pattern](source-evidence.md#parentheses-for-supporting-specifics).

### Connectors with a clear job

Use However for a contrast, Thus or Therefore for a supported consequence, Specifically for a concrete elaboration, For instance for a case, and First, Then, or Finally for a real sequence. Additionally, Moreover, Furthermore, and In addition can introduce an added point. Put However at the start of its sentence. Also can mark an added requirement inside a sentence.

**Reusable forms**

- However, [contrast with the preceding claim].
- Specifically, [operation or example that explains the previous statement].
- Thus, [supported consequence].
- In addition, [further point of the same kind].

**Keep the meaning.** Do not rotate connectors only to avoid repetition. A connector must name the relationship that actually holds, and many sentences need none. Consequently claims that the sentence follows from the previous one. Hang replaced it with In addition where the sentence added a further difficulty.

**Evidence from Hang** · weight 12 (3 edits)

- [DW-51](reviews/discussion-writing-review.md#dw-51), accepted with Hang's edit (weight 4). Suggested “Consequently, interactions are hard to identify”. Hang's wording is “In addition, interactions are hard to identify”.
- [DW-19](reviews/discussion-writing-review.md#dw-19), accepted with Hang's edit (weight 4). “They suggest, however, that annotations” became “However, they suggest that annotations”.
- [DW-34](reviews/discussion-writing-review.md#dw-34), accepted with Hang's edit (weight 4). Suggested “would count toward that budget”. Hang's wording is “would also count toward that budget”.

**Paper example** — [SIDE, line 90](../reference_papers/Demonstration_sidetracks/main.tex)

> Thus, in this work, we focus on identifying and investigating patterns of the noise in non-expert demonstrations.

[All source examples for this pattern](source-evidence.md#connectors-with-a-clear-job).

### A roadmap with actual content

Open a substantial section with what it will explain and, when useful, the order. Use this section or this chapter as the subject. One clause is enough when the paragraphs that follow open with statements that name the items.

**Reusable forms**

- This section first defines [signal] and then introduces [hypothesis].
- This chapter examines [question] through [study or analysis].
- This section describes [the connections between chapters], which [property].

**Keep the meaning.** The roadmap should match the section's actual order. It can add information beyond the heading, but it should not list in advance the items that the next paragraphs name in their own opening statements. Hang removed such a list in the Chapter 8 review. Do not repeat a roadmap before every short subsection.

**Evidence from Hang** · weight 10 (1 edit, 1 decline, 3 acceptances)

- [DW-14](reviews/discussion-writing-review.md#dw-14), accepted with Hang's edit (weight 4). Suggested “This section describes three such connections, which are not visible from any single study: differences between teachers”. Hang's wording is “This section describes the connections between chapters, which are not visible from any single study”.
- [CP-06](reviews/connection-paragraph-review.md#cp-06), declined (weight 3). Suggested “The chapters that follow address the three points listed above in order”. A sentence that mapped the points of a summary to the later chapters was declined.
- [DW-01](reviews/discussion-writing-review.md#dw-01), accepted (weight 1). “the three questions that were asked by this dissertation” became “the three questions of this dissertation”.
- [DW-60](reviews/discussion-writing-review.md#dw-60), accepted (weight 1). “It also outlined directions for future work” became “It also outlined directions for future work, from selecting which demonstrations to annotate and learning from more teaching modalities to agentic robotics and agentic HRI”. In a summary, naming the directions was accepted.
- [CP-03](reviews/connection-paragraph-review.md#cp-03), accepted (weight 1). “Chapter 8 brings together the discussions from the preceding studies” became “Chapter 8 considers the studies together by answering the three questions of this dissertation”. An outline entry that names what the chapter does was accepted.

**Paper example** — [PROG, line 215](../reference_papers/Progress/Ro-MAN%202024.tex)

> In this section, we first define progress, and then introduce our hypothesis.

[All source examples for this pattern](source-evidence.md#a-roadmap-with-actual-content).

### Study actions leading to the analytical question

Build a study summary from setup or instrument, to participant action, to analytical purpose. Explain a design choice when it makes a comparison possible.

**Reusable forms**

- [Instrument] was designed to capture [property]. Participants provided [data] during [task]. The analysis examined [question].
- [Stimuli] were presented under [design]. This made it possible to compare [measure] across [conditions].

**Keep the meaning.** Design describes what could be studied and does not establish what was found. Use the actual participants, setting, and data rather than filling a template with numbers from another paper.

**Paper example** — [STEADY, line 277](../reference_papers/STEADY/IEEEexample.tex)

> The robot performed six trajectories twice, allowing us to detect changes in feedback by comparing the difference in feedback between the two sessions. All users saw the same trajectories, allowing us to detect variation in feedback between users on the same task with the same feedback type.

[All source examples for this pattern](source-evidence.md#study-actions-leading-to-the-analytical-question).

### An intuition leading to an operation

Use an explicit intuition when moving from a learning difficulty to a design. Explain the premise and then name the operation that implements it. Use First and Second only if there are distinct premises.

**Reusable forms**

- The key intuition is that [relationship]. [Method] uses this relationship to [operation].
- [Method] rests on two intuitions. First, [premise A]. Second, [premise B]. Based on these intuitions, [operations].

**Keep the meaning.** An intuition is a design rationale, not a demonstrated result. Match its modal strength to its status, and avoid attaching unrelated design choices to one vague intuition.

**Paper example** — [STEADY, line 661–664](../reference_papers/STEADY/IEEEexample.tex)

> Based on the key intuitions,
> STEADY re-constructs feedback distributions,
> labels scalar feedback with binary labels,
> and remaps the magnitude of the feedback in a more algorithmically useful way based on feedback statistics.

[All source examples for this pattern](source-evidence.md#an-intuition-leading-to-an-operation).

## Sentence structure

### Concession with while

Use While [accepted point], [main point] to grant a benefit or shared property before stating the limitation or distinction. Keep the focus of the sentence in the second clause. While can also follow the main clause to add a contrast or a limit, and Hang keeps such a contrast in one sentence.

**Reusable forms**

- While [A offers a benefit], [A has a relevant limitation].
- While [signals share a property], [their information differs in a specified way].
- [A] improved [outcome] in [scope], while the improvement is less than using [B].

**Keep the meaning.** Make the concession substantive, and distinguish contrastive while from temporal while if the sentence could be read both ways. A while phrase without its own subject, such as while retaining [information], stays when its subject is clear from the sentence.

**Evidence from Hang** · weight 10 (1 edit, 2 declines)

- [DW-22](reviews/discussion-writing-review.md#dw-22), accepted with Hang's edit (weight 4). Suggested “although less than human annotations did”. Hang's wording is “while the improvement is less than using human annotations”.
- [DW-29](reviews/discussion-writing-review.md#dw-29), declined (weight 3). Suggested “A robot also needs to learn to perform a complex task”. Hang kept “while robots also need to learn to perform a complex task”.
- [DW-08](reviews/discussion-writing-review.md#dw-08), declined (weight 3). Suggested “and as a signal that retains magnitude information”. Hang kept “while retaining magnitude information”.

**Paper example** — [PH-INT, line 6](../reference_papers/PHIRL/introduction.tex)

> While sparse rewards are intuitive to specify, they offer limited guidance during early exploration.

[All source examples for this pattern](source-evidence.md#concession-with-while).

### Matched factors and endpoints

Keep paired factors, endpoints, and operations at the same grammatical level. Use not only but also when adding a second factor of the same kind, and repeat technical nouns when the repetition clarifies the comparison.

**Reusable forms**

- [Outcome] is associated not only with [factor A] but also with [factor B].
- A value of [A] indicates [endpoint A], while a value of [B] indicates [endpoint B].
- The analysis examines both [noun phrase A] and [noun phrase B].

**Keep the meaning.** Use not only but also sparingly. A consequence is not an additional factor. Parallel grammar does not justify a new relationship or a change to a scale.

**Evidence from Hang** · weight 8 (2 edits)

- [DW-32](reviews/discussion-writing-review.md#dw-32), accepted with Hang's edit (weight 4). “can inform completion shaping, negative reward samples, and better data coverage” became “can inform completion shaping, provide negative reward samples, and improve data coverage”. Each item of the series now has its own verb.
- [DW-37](reviews/discussion-writing-review.md#dw-37), accepted with Hang's edit (weight 4). “and if the model would always benefit” became “and whether the model would always benefit”. The third question now opens like the first two.

**Paper example** — [CHARM, line 56](../reference_papers/CHARM/ROMAN%202025.tex)

> We found that feedback patterns are not only correlated with task statistics, such as rewards, but also correlated with participants' characteristics

[All source examples for this pattern](source-evidence.md#matched-factors-and-endpoints).

### A specific case introduced by especially

Place especially after the general statement to identify the subgroup, condition, or factor that matters most to the claim.

**Reusable forms**

- [General statement], especially [specific case].
- [Result holds within scope], especially when [condition].

**Keep the meaning.** Especially implies a meaningful emphasis or difference. Do not add it unless the context or evidence supports singling out that case.

**Paper example** — [PROG, line 105](../reference_papers/Progress/Ro-MAN%202024.tex)

> making it crucial to learn from users, especially non-expert users.

[All source examples for this pattern](source-evidence.md#a-specific-case-introduced-by-especially).

### A literal alternative

Use instead of or rather than to make an actual alternative in an assumption, behavior, or procedure clear. Name both sides concretely. A short contrast can be written as [A], not [B]. Whereas sets the behavior of one actor against that of another.

**Reusable forms**

- [Method] uses [B] rather than [A].
- Instead of [expected action], the robot [observed action].
- [Stages] were evaluated separately, not end to end.
- [Approach] could [use an existing resource], instead of [building it from scratch].
- [Actor A] may [behavior A], whereas [actor B] may [behavior B].

**Keep the meaning.** Preserve these contrasts when they carry the scientific distinction. Avoid inventing an obviously inferior alternative simply to make the chosen approach sound better.

**Evidence from Hang** · weight 13 (3 edits, 1 acceptance)

- [DW-23](reviews/discussion-writing-review.md#dw-23), accepted with Hang's edit (weight 4). Suggested “were evaluated separately and not end to end”. Hang's wording is “were evaluated separately, not end to end”.
- [DW-56](reviews/discussion-writing-review.md#dw-56), accepted with Hang's edit (weight 4). Hang added “instead of building the skill library from scratch”.
- [DW-18](reviews/discussion-writing-review.md#dw-18), accepted with Hang's edit (weight 4). “; an agent that optimizes a reward may stay there” became “whereas an agent that optimizes a reward may stay there”.
- [DW-13](reviews/discussion-writing-review.md#dw-13), accepted (weight 1). “can be used and not only tolerated” became “can be used rather than only tolerated”.

**Paper example** — [SIDE, line 73](../reference_papers/Demonstration_sidetracks/main.tex)

> We found that instead of being random and rare, demonstration sidetracks frequently appear in non-expert demonstrations across all participants

[All source examples for this pattern](source-evidence.md#a-literal-alternative).

### Purpose attached to an action

Put the purpose first when the reader needs to understand the design choice before the procedure. When the design is already the topic, attach its analytical purpose afterward.

**Reusable forms**

- To investigate [question], [data] were collected under [setting].
- [Design choice] was used to compare [measure] across [conditions].
- [Repeated observation], allowing [bounded comparison].

**Keep the meaning.** The purpose describes what the procedure enables, not its success. Avoid to prove for an empirical investigation, and ensure the subject can perform the action in the purpose clause.

**Paper example** — [STEADY, line 302](../reference_papers/STEADY/IEEEexample.tex)

> We used a relatively simple task to reduce the cognitive load on solving the task and thus reduce feedback dynamics from confusion over the task.

[All source examples for this pattern](source-evidence.md#purpose-attached-to-an-action).

### Parallel sentences for a comparison

Keep the compared objects as stable subjects and describe the same dimensions in the same order. Add a sentence that explains why the distinction matters.

**Reusable forms**

- [Signal A] provides [strength] but [limitation]. [Signal B] provides [strength] but [limitation].
- [A] describes [dimension A]. [B] describes [dimension B]. This distinction matters when [condition].

**Keep the meaning.** Do not compare an information property of A with an unrelated performance property of B without naming the change in axis. A claim that combining signals improves learning still requires evaluation evidence.

**Paper example** — [PH-ABS, line 68](../reference_papers/PHIRL/CoRL_2026_main.tex)

> Human demonstrations provide dense policy-level information but sometimes lack local precision. Human feedback presents accurate local critiques, but offers sparse evaluations rather than direct policy guidance.

[All source examples for this pattern](source-evidence.md#parallel-sentences-for-a-comparison).

### Known information leading to new information

Let the next sentence take up a quantity, object, or finding introduced in the previous one. A result can be followed by This suggests that, or by which suggests that in the same sentence, when the referent is clear. Repeat a precise noun when a pronoun or a phrase such as the resulting values would be ambiguous. Use the definite article for something the previous sentence introduced. Use plain This as the subject when it refers to the statement just made.

**Reusable forms**

- [Method] uses [object]. [Object] describes [quantity].
- [Result with its measure]. This suggests that [bounded interpretation].
- [Result with its measure], which suggests that [bounded interpretation].
- [Procedure] collects annotations. These annotations provide [reference].
- Future work could extend [method] with [a strategy]. The new [strategy] would be compared with [baselines].
- This motivates [next step].

**Keep the meaning.** This should refer to a specific observation or object, not an uncertain mixture of several clauses. A known-to-new chain is a continuity device, not a requirement to start every sentence with a pronoun.

**Evidence from Hang** · weight 17 (4 edits, 1 acceptance)

- [DW-11](reviews/discussion-writing-review.md#dw-11), accepted with Hang's edit (weight 4). “Its margin over the best baseline” became “PHIRL's margin over the best baseline”.
- [DW-20](reviews/discussion-writing-review.md#dw-20), accepted with Hang's edit (weight 4). Suggested “the resulting values carried information”. Hang's wording is “*progress* values carried information”.
- [DW-33](reviews/discussion-writing-review.md#dw-33), accepted with Hang's edit (weight 4). Suggested “A new selection strategy would be compared”. Hang's wording is “The new selection strategy would be compared”.
- [DW-19](reviews/discussion-writing-review.md#dw-19), accepted with Hang's edit (weight 4). Suggested “This possibility motivates the selection”. Hang's wording is “This motivates the selection”.
- [DW-40](reviews/discussion-writing-review.md#dw-40), accepted (weight 1). “can be expressed as constraints in the same way” became “could be expressed as constraints on the learned reward, in the way that PHIRL uses *progress*”. Nothing before the sentence had mentioned constraints, so the reference was named.

**Paper example** — [STEADY, line 668–670](../reference_papers/STEADY/IEEEexample.tex)

> In an online learning setting,
> the robot needs to learn from human feedback in real time and update its policy.
> The feedback distributions thus also need to be updated after new feedback is added.

[All source examples for this pattern](source-evidence.md#known-information-leading-to-new-information).

### Means expressed with by

Use by followed by a gerund to connect an operation or supported claim to the means that implements or establishes it. Hang writes by taking advantage of [resource] where a shorter with [resource] is possible.

**Reusable forms**

- [Method] shapes [quantity] by [operation]-ing [object].
- [Analysis] examines [relationship] by comparing [conditions].
- [Needs] can be approached by taking advantage of [resource].

**Keep the meaning.** The means must actually perform the stated operation or support the claim. Do not make a method description imply an untested performance improvement.

**Evidence from Hang** · weight 4 (1 edit)

- [DW-30](reviews/discussion-writing-review.md#dw-30), accepted with Hang's edit (weight 4). Suggested “can be approached with agentic AI”. Hang's wording is “can be approached by taking advantage”.

**Paper example** — [PH-METH, line 87](../reference_papers/PHIRL/methodology.tex)

> We improve the learned reward function by shaping it to align with *progress* annotations during reward learning.

[All source examples for this pattern](source-evidence.md#means-expressed-with-by).

### Procedural series and enumerations

Use one actor with parallel verbs when the steps form a single procedure. Use then if order matters. For separate reasons or premises, use First and Second or One is and The other one is. Give every item of a list the same grammatical form and separate the items with commas. Keep semicolons for a long in-sentence list whose items contain commas.

**Reusable forms**

- [Method] [operation A], [operation B], and then [operation C].
- First, [premise A]. Second, [premise B].
- This section introduces [topic] in two aspects. One is [aspect A]. The other one is [aspect B].
- The categories are 1) [name A], [definition A]; 2) [name B], [definition B]; and 3) [name C], [definition C].

**Keep the meaning.** Do not force three items or imply a sequence that did not occur. Keep the correct object beside each operation, and do not list a speculative benefit as a completed procedural step. One is and The other one is are Hang's own forms, in the papers and in the dissertation, and a suggestion to replace them was declined.

**Evidence from Hang** · weight 17 (2 edits, 3 declines)

- [DW-33](reviews/discussion-writing-review.md#dw-33), accepted with Hang's edit (weight 4). “preference for low-quality demonstrations, preference for demonstrations” became “selecting low-quality demonstrations; selecting the demonstrations”. Every strategy in the list now opens with selecting.
- [DW-51](reviews/discussion-writing-review.md#dw-51), accepted with Hang's edit (weight 4). “In addition, humans' internal states could also require” became “Second, the internal state of a person may also require”. First is now followed by Second.
- [DW-25](reviews/discussion-writing-review.md#dw-25), declined (weight 3). Suggested “This section describes future work in two groups. One group addresses”. Hang kept “This section introduces future work in two aspects”.
- [DW-27](reviews/discussion-writing-review.md#dw-27), declined (weight 3). Suggested “The other group builds on the work in this dissertation”. Hang kept “The other one is future work that builds on the work in this dissertation”.
- [CP-18](reviews/connection-paragraph-review.md#cp-18), declined (weight 3). Suggested “PHIRL builds on two results from the preceding chapters. First,”. Hang kept “PHIRL builds on two results from the preceding chapters: *progress* is consistent”. First and Second were declined for two results that one sentence already lists.

**Paper example** — [PHIRL, line 38](../reference_papers/PHIRL/introduction.tex)

> In PHIRL, we iteratively use an IRL algorithm to learn a reward function from demonstrations, calculate rewards over the annotated demonstrations, and then shape the learned reward function in four dimensions: temporal delta, magnitudes, potential, and completion.

[All source examples for this pattern](source-evidence.md#procedural-series-and-enumerations).

### Definitions before notation

Put the term first, explain its quantity or role in ordinary language, and then give notation, range, or reference states. Define a term where it is first needed and retain that meaning throughout the chapter.

**Reusable forms**

- [Term] describes [quantity], ranging from [endpoint A] to [endpoint B].
- [Symbol] denotes [measure] between [event A] and [event B].
- This chapter defines [phenomenon] as [term].

**Keep the meaning.** Describes and measures are not interchangeable if only one is operationally justified. A brief reminder can help later, but it must not redefine the quantity or erase a formal condition.

**Evidence from Hang** · weight 8 (2 edits)

- [DW-22](reviews/discussion-writing-review.md#dw-22), accepted with Hang's edit (weight 4). “The formative VLM study” became “The formative study with a vision-language model (VLM)”. An abbreviation last defined in an earlier chapter was spelled out at its first use in this one.
- [DW-30](reviews/discussion-writing-review.md#dw-30), accepted with Hang's edit (weight 4). “Agentic HRI” became “agentic human-robot interaction (HRI)”.

**Paper example** — [PH-METH, line 17](../reference_papers/PHIRL/methodology.tex)

> *Progress* is a signal that describes the cumulative degree of task completion, ranging from fully incomplete to fully complete.

[All source examples for this pattern](source-evidence.md#definitions-before-notation).

### Local reasons and governing conditions

Keep a reason or condition next to the claim it governs. Lead with If, When, or Given when an unqualified main clause could be misread as general. Put because or since after the operation when the operation is already the topic. Hang often attaches a reason with since, which can take the place of a colon before an explanation.

**Reusable forms**

- If [assumption], [formal consequence].
- When [evaluation condition], [bounded observation].
- For [alignment], [inputs] preferably share [reference] because [source of variation].
- [Assumption or rule], since [reason].

**Keep the meaning.** Do not turn an if assumption into a when observation. Preserve preferably, might, and other qualifiers. A reason for one alignment does not automatically restrict the whole framework. Hang changed if staying is rewarded to since staying is rewarded. That is the author's decision about the claim, and an assistant should ask before making the same kind of change.

**Evidence from Hang** · weight 12 (3 edits)

- [DW-18](reviews/discussion-writing-review.md#dw-18), accepted with Hang's edit (weight 4). Suggested “may stay there if staying is rewarded”. Hang's wording is “may stay there since staying is rewarded”.
- [DW-32](reviews/discussion-writing-review.md#dw-32), accepted with Hang's edit (weight 4). Suggested “are always annotated, since they may be the most informative: low-quality demonstrations can inform”. Hang's wording is “should be prioritized for annotations, since low-quality demonstrations can inform”.
- [DW-34](reviews/discussion-writing-review.md#dw-34), accepted with Hang's edit (weight 4). Kept “since annotating a long demonstration or an ambiguous segment takes more time”.

**Paper example** — [PHIRL, line 126](../reference_papers/PHIRL/methodology.tex)

> Note that in this condition specifically, $s_i, s_{i+1}, s_j$, and $s_{j+1}$ are preferably from the same demonstration $D$ since different users might scale \textit{progress} differently.

[All source examples for this pattern](source-evidence.md#local-reasons-and-governing-conditions).

### Complete clauses in place of elliptical endings

Write the clause in full. Give a comparison its own subject and verb instead of ending on a pro-form such as did, does not, or so. When a statement answers a question, repeat the verb instead of stopping at it can. When a trailing which clause leaves its verb to the reader, make it a sentence with its own subject.

**Reusable forms**

- [A] improved [outcome] in [scope], while the improvement is less than using [B].
- The results of [stage] indicate that it can [verb] [object] in two ways.
- The information from [signal] would be expected to matter more when [condition stated in full].

**Keep the meaning.** The full clause must keep the claim of the short form. When expanding, check the compared quantity and any limit that the short form stated, such as in two of them. A short contrast such as evaluated separately, not end to end is not an ellipsis that needs expanding. This pattern rests on three decisions in one chapter.

**Evidence from Hang** · weight 12 (3 edits)

- [DW-22](reviews/discussion-writing-review.md#dw-22), accepted with Hang's edit (weight 4). Suggested “although less than human annotations did”. Hang's wording is “while the improvement is less than using human annotations”.
- [DW-06](reviews/discussion-writing-review.md#dw-06), accepted with Hang's edit (weight 4). Suggested “indicate that it can, in two ways that act at different points”. Hang's wording is “indicate that it can act at different points in two ways”.
- [DW-12](reviews/discussion-writing-review.md#dw-12), accepted with Hang's edit (weight 4). “which should matter more when more of the demonstrated behavior does not” became “The information from *progress* would be expected to matter more when a larger portion of the demonstrated behaviors does not advance the task”.

**Basis.** This pattern comes from the evidence from Hang above. It has no paper example.

## Storytelling style

### An introduction built around a consequential assumption

Build a study introduction around the practical task and a particular assumption about human teaching. Explain what that assumption may overlook, why it matters, and the bounded research question. Then introduce the insight, the study, the main findings, and the contribution.

**Reusable forms**

- Practical stake → prior assumption → overlooked behavior → insight or question → this chapter's approach → findings → contribution.
- Prior [methods] assume [A]. In human teaching, however, [relevant constraint]. This raises the question of whether [testable question].

**Keep the meaning.** The seven moves are an organizing default, not seven mandatory paragraphs. Do not dismiss all prior work or present the chapter's later finding as already established in its motivation. Support the assumption with the cited work.

**Paper example** — [SIDE, line 302](../reference_papers/Demonstration_sidetracks/main.tex)

> One key assumption when using simple distributions to sample noise is that noise is independent from the task itself.

[All source examples for this pattern](source-evidence.md#an-introduction-built-around-a-consequential-assumption).

### A study finding leading to a method

Make the handoff explicit. The finding leaves a particular learning difficulty, an intuition addresses that difficulty, and a mechanism implements the intuition. State the main intuition before formal details when introducing the method.

**Reusable forms**

- [Finding] leaves [remaining difficulty]. This motivates [design response] that [operation].
- The intuition is that [relationship]. In [method], this is implemented by [mechanism].
- Finding → remaining problem → intuition → operation → evaluation question.

**Keep the meaning.** A study can motivate a method without validating it. Do not imply the studies used the same participants, task, or pipeline. State the main intuition clearly once, then refer back as needed rather than enforcing an arbitrary count.

**Paper example** — [STEADY, line 280](../reference_papers/STEADY/IEEEexample.tex)

> These results, and the data collected, motivate and enable the development and evaluation of our STEADY algorithm.

[All source examples for this pattern](source-evidence.md#a-study-finding-leading-to-a-method).

### Teaching a method from meaning to evaluation

Introduce an unfamiliar signal by what it means, then explain the relationship the method uses, its operations, and the evaluation question. Organize notation and losses around the quantities the intuition relates.

**Reusable forms**

- Problem → signal meaning → intuition → notation and assumptions → operations → evaluation design.
- The evaluation asks whether [method] improves [outcome] relative to [baseline] under [conditions].

**Keep the meaning.** Do not list symbols or losses before explaining their purpose. Keep successful evaluation outcomes out of the procedure itself. Use a shorter introduction when the audience already knows the signal.

**Paper example** — [PHIRL, line 34](../reference_papers/PHIRL/introduction.tex)

> \textit{Progress} describes the cumulative task completion based on the task observation.

[All source examples for this pattern](source-evidence.md#teaching-a-method-from-meaning-to-evaluation).

### The three stage dissertation arc

Connect the stages through questions and responses. The first stage is to understand structure and variation in non-expert teaching, the second is to mitigate or account for the difficulties through processing and signal design, and the third is to use complementary teaching information in a learning framework. Explain what each stage makes available to the next. Name the stages with the verbs of the title, modeling, mitigating, and leveraging, as Hang did in the section headings of Chapter 1.

**Reusable forms**

- The first stage asks [question] and establishes [bounded finding].
- The second stage addresses [remaining difficulty] by [processing or signal design].
- Building on [information or signal], the final stage examines how [sources] can inform [learning object].

**Keep the meaning.** This is a conceptual dependency, not evidence of one controlled end-to-end experiment. Preserve the dissertation's established stage names and distinguish tasks, datasets, and participant groups across chapters.

**Evidence from Hang** · weight 17 (1 instruction, 1 hand edit, 1 edit, 1 decline, 1 acceptance)

- [HI-06](preference-signals.md#hi-06), Hang's instruction, October 12, 2026 (weight 5). “use Chapter 1: "lower quality requirements for human teaching and reduce human effort in annotating"”.
- [HE-05](preference-signals.md#he-05), Hang's own edit (weight 4). “\section{Towards Richer Human Evaluative Feedback}” became “\section{Mitigating Noise for Richer Human Evaluative Feedback}”.
- [HE-05](preference-signals.md#he-05), Hang's own edit (weight 4). “\section{Noise beyond the Task}” became “\section{Modeling and Understanding Noise beyond the Task}”.
- [CP-22](reviews/connection-paragraph-review.md#cp-22), accepted with Hang's edit (weight 4). Suggested “lower quality requirements for human teaching and reduce human effort in annotating”. Hang's wording is “enable robust reward learning while reducing human effort in annotating”. Hang's own wording of the third question, in Chapter 8. Chapter 1 keeps the wording Hang chose for it.
- [OA-104](reviews/overall-assessment-review.md#oa-104), declined (weight 3). Suggested “can enable robust reward learning while reducing human effort in annotating”. Hang kept “can lower quality requirements for human teaching and reduce human effort in annotating”. A suggestion to give Chapter 1 the wording of Chapter 8 was declined.
- [CP-07](reviews/connection-paragraph-review.md#cp-07), accepted (weight 1). “This chapter begins the first stage of this dissertation: understanding” became “This chapter begins the first stage of this dissertation, which is to understand and model”.

**Paper example** — [RSS Pioneers prospectus, line 84](../reference_papers/prospectus/RSS%20Pioneers%202026.tex)

> Our first step focuses on examining human factors in human teaching robots that make human teaching noisy, where these factors are not only related to the tasks but also are intrinsic to the human teachers.

[All source examples for this pattern](source-evidence.md#the-three-stage-dissertation-arc).

### A hypothetical scenario that explains a problem

Use the shortest familiar robot scenario that makes an abstract difficulty visible. Identify the task state, action, consequence, and what the signal or method can distinguish. Return promptly to the technical point.

**Reusable forms**

- For instance, consider [hypothetical task] where [problem]. In this case, [consequence]. This illustrates [technical distinction].
- Problem state → action → consequence → relevance to the method.

**Keep the meaning.** Label hypothetical cases and analogies clearly. A few sentences usually suffice, but clarity takes priority over a fixed count. An illustrative scenario does not replace aggregate evidence.

**Paper example** — [PROG, line 616](../reference_papers/Progress/Ro-MAN%202024.tex)

> For instance, a cleaning robot gets a +1 reward every time it cleans a room. The robot, instead of cleaning one room and going to the next room, repetitively ejects dirt in a room, then cleans it, and thus achieves high rewards.

[All source examples for this pattern](source-evidence.md#a-hypothetical-scenario-that-explains-a-problem).

### Headings that name the question or finding

Use a result subsection heading that states the question answered or the supported finding. Give discussion run-in headings a concrete subject so readers can follow the argument from the outline. Give a future-work subsection a noun phrase or an -ing phrase that names the direction, and keep the technical verb that Hang uses for it. In the overall findings of Chapter 8, Hang states each finding as its italic heading, such as The imperfections in non-expert teaching are not random noise. A chapter title is the descriptive part of the paper title, without the acronym or question that opened it, and the paper title appears in bold in the originally published as line.

**Reusable forms**

- [Factor] improves [measured outcome] under [condition].
- Did participants provide consistent feedback across sessions?
- [Signal] and [specific measured property]
- Actively Sampling [Objects] to [Purpose]

**Keep the meaning.** A heading must not claim more than the section establishes. A question or subject heading is preferable when the evidence is mixed. Do not import a paper's strong headline into a more qualified dissertation result.

**Evidence from Hang** · weight 18 (3 hand edits, 1 edit, 2 acceptances)

- [DW-31](reviews/discussion-writing-review.md#dw-31), accepted with Hang's edit (weight 4). Suggested “Actively Selecting Demonstrations to Annotate”. Hang's wording is “Actively Sampling Demonstrations to Annotate”. The heading had been Actively Sample Annotations. Hang accepted the -ing form and the new object, and kept the verb sample.
- [HE-01](preference-signals.md#he-01), Hang's own edit (weight 4). “*Are the imperfections in non-expert teaching random noise?*” became “*The imperfections in non-expert teaching are not random noise.*”.
- [HE-01](preference-signals.md#he-01), Hang's own edit (weight 4). “\section{Answers to the Overarching Questions}” became “\section{Overall Findings Across Chapters}”.
- [HE-06](preference-signals.md#he-06), Hang's own edit (weight 4). “\chapter{CHARM: Considering Human Attributes for Reinforcement Modeling}” became “\chapter{Considering Human Attributes for Reinforcement Modeling}”.
- [HE-04](preference-signals.md#he-04), Hang's own edit (weight 4). “\subsection*{Agentic Human-Robot Interaction}” became “\subsection*{Agentic Human-Robot Interaction for Non-Expert Users}”.
- [HE-04](preference-signals.md#he-04), Hang's own edit (weight 4). “\subsection*{Agentic Robotics}” became “\subsection*{Human-in-the-Loop Agentic Robotics}”.
- [OA-718](reviews/overall-assessment-review.md#oa-718), accepted (weight 1). “\subsection{PHIRL Learns More Robust Reward Functions}” became “\subsection{Reward Functions in Two Reward Hacking Scenarios}”. A heading that claimed more than its section showed.
- [PT-003](reviews/paper-title-status-review.md#pt-003), accepted (weight 1). “originally published as ``CHARM:” became “originally published as ``\textbf{CHARM:”.

**Paper example** — [CHARM, line 403](../reference_papers/CHARM/ROMAN%202025.tex)

> Including Human Characteristics Improves Feedback Prediction Accuracy

[All source examples for this pattern](source-evidence.md#headings-that-name-the-question-or-finding).

### A results paragraph answering one comparison

State the hypothesis or comparison question, the condition and measure, the paired results, the uncertainty or test, and the bounded verdict. Repeat the same frame for multiple conditions before explaining what changes across them.

**Reusable forms**

- Question or hypothesis → condition and metric → paired outcomes → statistical evidence → interpretation or verdict.
- Under [condition], [A] achieved [value A], compared with [value B] for [B]. [Test statement]. These results [bounded answer].

**Keep the meaning.** Do not invent uncertainty estimates, repeated runs, or tests. Keep distinct outcomes separate. A statistically significant difference does not explain its cause, and a nonsignificant test does not establish equivalence.

**Paper example** — [CHARM, line 448](../reference_papers/CHARM/ROMAN%202025.tex)

> the model trained with only task statistics has an accuracy of 32.59\% and the model trained with task statistics and human characteristics (CHARM) has an accuracy of 55.83\%.

[All source examples for this pattern](source-evidence.md#a-results-paragraph-answering-one-comparison).

### An unexpected result and possible reasons

Name the mismatch between an expectation or earlier analysis and the observed result. Then present possible reasons as hypotheses that could be examined.

**Reusable forms**

- While [expectation or earlier result], [observed result]. One possible reason is that [hypothesis A]. Another is that [hypothesis B].

**Keep the meaning.** Do not manufacture surprise or label a result interesting without saying what the tension is. Separate nonlinear relationships, measurement limits, and other proposed explanations from tested causes.

**Paper example** — [CHARM, line 465](../reference_papers/CHARM/ROMAN%202025.tex)

> One interesting finding is that while there were no strong correlations between the selected human characteristics and human feedback values, our experiment results demonstrated that incorporating human characteristics into training leads to a significant improvement in modeling human feedback patterns.

[All source examples for this pattern](source-evidence.md#an-unexpected-result-and-possible-reasons).

### Discussion synthesis and its boundary

Start with the connection or finding to explain, select the evidence needed from the relevant studies, and state the methodological implication. Identify differences that limit comparison, then close with a specific question or next step and its practical relevance.

**Reusable forms**

- These findings suggest [shared issue]. In [study A], [evidence A]. In [study B], [evidence B]. This helps explain [design choice].
- The studies differ in [condition], so the comparison is suggestive rather than controlled.
- Connection → selected evidence → implication → boundary → next question.

**Keep the meaning.** Synthesis must add an interpretation, not repeat every chapter summary. Do not compare methods as if they shared an evaluation when they did not. End with a link to the next chapter only when that chapter addresses the named question. The cross-chapter form is a synthesis template, not a finding by itself. Help explain claims less than account for, and it is the accepted wording for a design choice that two studies on different scales make plausible.

**Evidence from Hang** · weight 9 (1 hand edit, 1 edit, 1 acceptance)

- [DW-16](reviews/discussion-writing-review.md#dw-16), accepted with Hang's edit (weight 4). “They also account for a design choice” became “They also help explain a design choice”.
- [HE-02](preference-signals.md#he-02), Hang's own edit (weight 4). “The limitations of each study are discussed in its own chapter” became “but there are a few gaps if the studies are considered together”. Hang's own lead-in to the limits of the combined evidence.
- [HE-02](preference-signals.md#he-02), Hang's own edit (weight 4). “evaluated separately, not end-to-end” became “First, the stages of the argument were evaluated separately”.
- [DW-15](reviews/discussion-writing-review.md#dw-15), accepted (weight 1). “Two studies with different participants, tasks, and scales point in the same direction” became “The results of two studies with different participants, tasks, and scales are consistent with each other”.

**Paper example** — [CHARM, line 445](../reference_papers/CHARM/ROMAN%202025.tex)

> Both models performed poorly and including human characteristics showed minimal improvement. These results are consistent with our earlier correlation analysis.

[All source examples for this pattern](source-evidence.md#discussion-synthesis-and-its-boundary).

### Related work ending with the specific difference

After explaining the relevant methods or studies, close with the concrete difference in the chapter's population, question, information, or method. Make clear why that difference is needed.

**Reusable forms**

- This chapter differs from prior work by [specific research choice].
- Prior [methods] address [scope]. This chapter examines [different bounded question].

**Keep the meaning.** A difference is not automatically an advantage. A claimed improvement in efficiency or human effort needs its own evidence. Frame it as a goal when that is all the current passage establishes.

**Paper example** — [PROG, line 202](../reference_papers/Progress/Ro-MAN%202024.tex)

> Our work differs from prior work by focusing on non-experts.

[All source examples for this pattern](source-evidence.md#related-work-ending-with-the-specific-difference).

### An observed episode in action order

For a real episode, describe the obstacle, the participant's or robot's adjustment, the outcome, and the analytical link. Keep actions by the same actor in order, then change focus when returning to the signal or measurement.

**Reusable forms**

- In one observed demonstration, [difficulty]. The participant then [adjustment], [next action], and [outcome]. [Measurement] shows [bounded relation].
- [Actor] first [action]. After [event], [actor] [response]. This sequence illustrates [pattern].

**Keep the meaning.** Use only an episode actually documented in the study. Do not infer an unreported intention, and do not treat one episode as evidence of prevalence. Invented examples retained in the source archive demonstrate syntax only.

**Paper example** — [PROG, line 595](../reference_papers/Progress/Ro-MAN%202024.tex)

> Then the participant decided to reset the arm to the initial position, demonstrated the entire task from the beginning again, and succeeded.

[All source examples for this pattern](source-evidence.md#an-observed-episode-in-action-order).

### Future work drafted from notes

When Hang's notes for a future-work subsection are written out, take each sentence from a note or from a source that Hang named, and say in the review note where a note was interpreted. Move from the starting point in the dissertation to the planned step and to how the step would work. End the paragraph on the planned step or on the mechanism. Do not add a closing sentence that restates the questions of the dissertation or explains why its findings matter for the new direction, and do not add supporting detail that the notes did not ask for.

**Reusable forms**

- Starting point in this dissertation → planned step → how the step would work → what a person still does.
- One planned step is to [action from the note]. Each [record] would include [fields from the note].
- Following [named approach], [agent] would then [action], and [objects] would be updated from [collected data].

**Keep the meaning.** This concerns sentences added beyond the notes, not the drafting itself. Hang deleted two of the three closing sentences that linked a direction back to the dissertation, and one sentence of added detail. Drafts that stayed within the notes and their sources were accepted (DW-45, DW-46). Of two optional drafts written without notes, one was accepted (DW-44) and one was declined (DW-43). A sentence in which Hang links a direction to the dissertation stays.

**Evidence from Hang** · weight 20 (1 hand edit, 3 edits, 1 decline, 1 acceptance)

- [DW-47](reviews/discussion-writing-review.md#dw-47), accepted with Hang's edit (weight 4). Hang deleted the suggested “The questions of this dissertation would apply at this level as well”.
- [DW-57](reviews/discussion-writing-review.md#dw-57), accepted with Hang's edit (weight 4). Hang deleted the suggested “Because these outcomes include the evaluations and reactions of non-experts, the imperfections studied in this dissertation would need to be accounted for when the skills are updated”.
- [DW-53](reviews/discussion-writing-review.md#dw-53), accepted with Hang's edit (weight 4). Hang deleted the suggested “The same format would be used for studies reported in papers and for the logs of new experiments”.
- [HE-03](preference-signals.md#he-03), Hang's own edit (weight 4). “non-expert teaching does not disappear. It moves to a higher level” became “non-expert teaching is still valuable”. Hang later reworded accepted text of this kind by hand.
- [HE-03](preference-signals.md#he-03), Hang's own edit (weight 4). “Human teaching would then provide a trajectory” became “Humans now provide a trajectory”.
- [DW-43](reviews/discussion-writing-review.md#dw-43), declined (weight 3). An optional subsection that was drafted without a note from Hang.
- [DW-48](reviews/discussion-writing-review.md#dw-48), accepted (weight 1). Kept “The time that a person gives could then go to the teaching that an agent cannot produce on its own”. This is the third added closing sentence, and it was accepted.

**Basis.** This pattern comes from the evidence from Hang above. It has no paper example.

## Talk and film text

These patterns are for the slides, the speaker notes, and the film of the dissertation talk. They rest on the reviews of the talk and the film and on Hang's messages about them. The chapters keep the patterns above.

### Slide text in the presenter's voice

Write slide text in few words and in the tone a presenter uses aloud, scientific but casual. Prefer a figure, chart, or video to a sentence, and leave the rest to the speaker notes. A title plainly says what the slide shows. Keep a line that Hang wrote or dictated word for word, and fix only its grammar. Shorter versions of Hang's slide text were accepted when they kept the content, and so were literal descriptions of what a curve or a method does.

**Reusable forms**

- Often occurred within 4 s of a task-phase change
- Demonstrations carry policy information, but not always optimal framewise.
- Compare under the same human time
- They give negative examples and cover more of the task.
- AI agents can plan long-horizon tasks and correct their own mistakes.
- AIRL's reward dips only a little at each drop.

**Keep the meaning.** This pattern is for the talk and the film, not for the chapters, whose impersonal voice stays. First person is normal on slides and in speaker notes. A slide line can keep a short shape that Hang wrote, such as Robots that learn from more, and from everyone. The slide guidelines of the talk hold the layout and visual rules, and this pattern holds only the wording. A joke added to the speaker notes was declined, and so were three suggestions to cut a slide or a line that repeated an earlier one.

**Evidence from Hang** · weight 82 (3 instructions, 4 hand edits, 2 edits, 10 declines, 7 acceptances, 3 notes)

- [HI-11](preference-signals.md#hi-11), Hang's instruction, September 27, 2026 (weight 5). “8. Scentific but causual tone”.
- [HI-11](preference-signals.md#hi-11), Hang's instruction, September 27, 2026 (weight 5). “2. figures are more preferred than text”.
- [HI-12](preference-signals.md#hi-12), Hang's instruction, October 17, 2026 (weight 5). “b. too many words”.
- [HI-18](preference-signals.md#hi-18), Hang's instruction, October 17, 2026 (weight 5). “improve wording for newly generated/added slides”.
- [HE-15](preference-signals.md#he-15), Hang's own edit (weight 4). Hang dictated the line which means their teaching will be noisier and harder for robots to learn, and then changed harder to challenging in it.
- [HE-16](preference-signals.md#he-16), Hang's own edit (weight 4). “every frame carries information, including the wobbles” became “demonstrations carry policy information, but not always optimal framewise”.
- [S18-W01](reviews/full-talk-wording-review.md#s18-w01), accepted with Hang's edit (weight 4). Suggested “Occurred within 4 s”. Hang's wording is “Often occurred within 4 s”.
- [W02](reviews/full-talk-review-20261019.md#w02), accepted with Hang's edit (weight 4). Suggested “with the start and the end as references”. Hang's wording is “with the start and the end states as references”. The review offered grammar fixes only, and Hang adjusted one of them.
- [HE-18](preference-signals.md#he-18), Hang's own edit (weight 4). Hang wrote “Robots belong to the world, not the lab”.
- [HE-18](preference-signals.md#he-18), Hang's own edit (weight 4). Hang wrote “scalar can outperform binary: the magnitudes carry additional information”.
- [HE-17](preference-signals.md#he-17), Hang's own edit (weight 4). Hang deleted the caption Factories · sidewalks · homes, which repeated the picture, and a band with a moral.
- [S08-W01](reviews/full-talk-wording-review.md#s08-w01), declined (weight 3). Suggested “Dense information about how to perform the task, although individual actions may be sub-optimal”. Hang kept “demonstrations carry policy information, but not always optimal framewise”.
- [S04-W01](reviews/full-talk-wording-review.md#s04-w01), declined (weight 3). Suggested “Models trained on varied demonstrations, such as these 34 successful examples, can become more robust”. Hang kept “Varied data, like these 34 successful demos, can make models more robust”.
- [P60](reviews/full-talk-review-20261019.md#p60), declined (weight 3). Suggested “Robots that learn from more people and more sources”. Hang kept “Robots that learn from more, and from everyone”.
- [S59-W01](reviews/full-talk-wording-review.md#s59-w01), declined (weight 3). Suggested “PHIRL learns a reward function from demonstrations and aligns it with progress annotations”. Hang kept “In the end, we proposed PHIRL”.
- [SL-R09](reviews/full-talk-slides45-68.md#sl-r09), accepted (weight 3). “Large VLA/WAM policies still requires high quality data” became “Large VLA/WAM models still need high-quality data”. Hang's note: “also re-orgnize it a bit”.
- [PN-R07](reviews/full-talk-pre-notes.md#pn-r07), accepted (weight 3). Hang's note: “for the right side, do not just use words, use the bar chart”. The slide merged two CHARM slides.
- [PN-R01a](reviews/full-talk-pre-notes.md#pn-r01a), accepted (weight 3). Hang's note: “I do not like the model outcome one, instead of having performance chart, showing actual video or images to demonstrate that it is better”. The suggestion was photos and a chart for the benefits of non-expert data.
- [M01](reviews/full-talk-migration.md#m01), declined (weight 3). Suggested “And when people say more than one, they usually mean two”.
- [S08-S01](reviews/full-talk-wording-review.md#s08-s01), declined (weight 3). Suggested “Sparse information about behavior quality”. Hang kept “Sparse, but more accurate: it takes less expertise to judge than to perform”.
- [S19-W01](reviews/full-talk-wording-review.md#s19-w01), declined (weight 3). Suggested “the companion panel in that figure”. Hang kept “the panel on the right shows that pauses take the biggest share of the time”.
- [S01](reviews/full-talk-review-20261019.md#s01), declined (weight 3). Suggested “Remove slide 26”. The slide repeated the procedure of the one before.
- [S02](reviews/full-talk-review-20261019.md#s02), declined (weight 3). Suggested “Keep only '18,000 ratings collected”. The list repeated the design slide before it.
- [S03](reviews/full-talk-review-20261019.md#s03), declined (weight 3). Suggested “Remove the line and its click from slide 35”. The line was repeated two slides later.
- [SL-R13](reviews/full-talk-slides45-68.md#sl-r13), accepted (weight 1). “Test it under the same budget of human time” became “Compare under the same human time”.
- [SL-R12](reviews/full-talk-slides45-68.md#sl-r12), accepted (weight 1). “They can shape completion, give negative reward samples, and widen data coverage” became “They give negative examples and cover more of the task”.
- [W04](reviews/full-talk-review-20261019.md#w04), accepted (weight 1). “AIRL keeps paying out” became “AIRL's reward dips only a little at each drop”.
- [S03-G01](reviews/full-talk-wording-review.md#s03-g01), accepted (weight 1). “noisier and challenging for robots to learn” became “noisier and more challenging for robots to learn from”.

**Basis.** This pattern comes from the evidence from Hang above. It has no paper example.

### Measured results and plain premises on slides

On a slide, report a result as it was measured, as in the dissertation. Write no significant difference or similar (n.s.) for a test that found no difference, and in this study or in a formative study where the scope matters. Keep the premise of the talk plain and direct, including a widely held view that the talk sets up in order to question it. Hang kept It is widely accepted that as that setup, and accepted removing Everyone in the field agrees and Everyone accepts this. Do not add a qualifying clause or a measure to a short caption unless the caption is wrong without it.

**Reusable forms**

- Within ±2, scalar self-agreement was similar to binary (n.s.)
- This study did not detect a difference in the effort required to give progress or scalar feedback.
- so a final-progress threshold of 90 identified every failed demonstration in this sample.
- It is widely accepted that human demonstrations are noisy and multi-policy.

**Keep the meaning.** Hang accepted measured wording for results in the wording review of October 17 and again on October 19, 2026, and declined it for premise lines and for added detail. Of the eleven fact checks of October 19, Hang declined six, such as naming the reward that progress was correlated with or saying what a percentage is a share of. The accepted ones corrected what happened in a failure scenario, a claim about effort, a label budget, and the source of the VLM result. Hang removed the number from a takeaway bullet that the review had kept. On one slide, Hang declined May be associated with for one candidate factor and accepted May limit for another. Hang declined three narrower versions of the line that none of the participants were robot experts. That line is Hang's decision about the talk, and the question raised about it is kept in the record of the review.

**Evidence from Hang** · weight 76 (1 hand edit, 3 edits, 17 declines, 7 acceptances, 1 note)

- [M09](reviews/full-talk-migration.md#m09), declined (weight 5). Hang's note: “but significance can be added tho”. The suggestion was to show the original self-agreement figure.
- [HE-14](preference-signals.md#he-14), Hang's own edit (weight 4). “no detectable difference” became “no statistical significance”.
- [F10](reviews/full-talk-review-20261019.md#f10), accepted with Hang's edit (weight 4). Suggested “STEADY reached a 4.2 higher return than binary feedback”. Hang's wording is “STEADY reached a higher return than binary feedback”.
- [S06-S01](reviews/full-talk-wording-review.md#s06-s01), accepted with Hang's edit (weight 4). Suggested “a guess can earn a point”. Hang's wording is “the expectation of guess is positive”.
- [S22-S02](reviews/full-talk-wording-review.md#s22-s02), accepted with Hang's edit (weight 4). Suggested “to avoid directly using those demographic attributes in the feedback model”. Hang's wording is “to avoid discrimination from the results”. The original line had promised that the results could never be used to discriminate.
- [S11-W02](reviews/full-talk-wording-review.md#s11-w02), declined (weight 3). Suggested “Human demonstrations can be noisy and reflect different policies”. Hang kept “It is widely accepted that human demonstrations are noisy and multi-policy”.
- [S12-W01](reviews/full-talk-wording-review.md#s12-w01), declined (weight 3). Suggested “People can demonstrate the same task in different ways…”. Hang kept “It's widely accepted that demonstrations are noisy, and everyone does the same task differently…”.
- [S12-W03](reviews/full-talk-wording-review.md#s12-w03), declined (weight 3). Suggested “Some imperfections follow patterns related to the task and the teacher”. Hang kept “Much of it has structure. We can model it, mitigate it, and leverage it”.
- [S19-S01](reviews/full-talk-wording-review.md#s19-s01), declined (weight 3). Suggested “Random noise alone does not capture these patterns”. Hang kept “Random noise injected into perfect demonstrations would not reproduce this structure”.
- [S07-S01](reviews/full-talk-wording-review.md#s07-s01), declined (weight 3). Suggested “alongside demonstrations from people with varying levels of robotics experience”. Hang kept “none of them are robot experts”.
- [S07-S02](reviews/full-talk-wording-review.md#s07-s02), declined (weight 3). Suggested “we recruited passersby in public spaces, such as a university atrium”. Hang kept “none of them were robot experts”.
- [F04](reviews/full-talk-review-20261019.md#f04), declined (weight 3). Suggested “and most of them are not robot experts”. Hang kept “and none of them are robot experts”.
- [S23-S01](reviews/full-talk-wording-review.md#s23-s01), declined (weight 3). Suggested “May be associated with greater feedback accuracy”. Hang kept “Helps people give more precise feedback”.
- [F03](reviews/full-talk-review-20261019.md#f03), declined (weight 3). Suggested “the reward that AIRL learned from these demonstrations”. Hang kept “Progress also correlated with task reward”.
- [F02](reviews/full-talk-review-20261019.md#f02), declined (weight 3). Suggested “Potential shaping mattered most in three of four settings”. Hang kept “Removing any term lowered the return”.
- [F08](reviews/full-talk-review-20261019.md#f08), declined (weight 3). Suggested “has a higher return than all of them in all four settings”. Hang kept “beats all of them in all four settings”.
- [F09](reviews/full-talk-review-20261019.md#f09), declined (weight 3). Suggested “share of moving time steps,”. Hang kept “by how many buttons or joystick axes were used at once”.
- [S53-W03](reviews/full-talk-wording-review.md#s53-w03), declined (weight 3). Suggested “— return, p < 0.001”. Hang kept “PickPlaceCan, MH - p < 0.001”.
- [W03](reviews/full-talk-review-20261019.md#w03), declined (weight 3). Suggested “Hand-craft a dense reward but tuning it takes a lot of time”. Hang kept “A dense reward for pouring sprinkles over a cake”.
- [S23-W01](reviews/full-talk-wording-review.md#s23-w01), declined (weight 3). Suggested “May encourage more candid feedback with less dialogue”. Hang kept “More candid, less dialogic feedback”.
- [S23-W02](reviews/full-talk-wording-review.md#s23-w02), declined (weight 3). Suggested “Feedback detail may vary with voice, video, or VR interfaces”. Hang kept “Voice, video, or VR changes feedback detail”.
- [F11](reviews/full-talk-review-20261019.md#f11), accepted (weight 1). “No extra effort: similar NASA-TLX workload” became “Similar effort: no significant difference in NASA-TLX workload”.
- [S38-S01](reviews/full-talk-wording-review.md#s38-s01), accepted (weight 1). “So progress is no harder to give than a score” became “This study did not detect a difference in the effort required to give progress or scalar feedback”.
- [S42-S03](reviews/full-talk-wording-review.md#s42-s03), accepted (weight 1). “so the last progress value alone caught all of the failures” became “so a final-progress threshold of 90 identified every failed demonstration in this sample”.
- [S06-W02](reviews/full-talk-wording-review.md#s06-w02), accepted (weight 1). “can clearly improve VLA models” became “can improve VLA performance”.
- [S12-W04](reviews/full-talk-wording-review.md#s12-w04), accepted (weight 1). “Everyone in the field agrees that human teaching is imperfect:” became “Human teaching can be imperfect:”.
- [S11-W01](reviews/full-talk-wording-review.md#s11-w01), accepted (weight 1). “Everyone accepts this. The question is why” became “The question is what produces these differences”.
- [S23-S03](reviews/full-talk-wording-review.md#s23-s03), accepted (weight 1). “Reduces feedback depth and quality” became “May limit feedback detail and quality”.

**Basis.** This pattern comes from the evidence from Hang above. It has no paper example.

### A motivation told as a story

Tell the motivation of a talk or a film as a short story about the problem, in the order of Hang's outline. Robots are already part of daily life, but most training data are recorded in labs, and many learning methods require clean data. For robots to be part of everyday life, they need to learn from everyone. Not everyone can provide clean data, and people teach each other through many modalities. Non-expert teaching is also more accessible, and models trained on it can be more robust in the real world. Set up the problem rather than summarizing what the dissertation already did, and do not overstate what robots can do now.

**Reusable forms**

- Most of the data that robots learn from is recorded in labs, by experts and trained operators.
- Many learning methods require clean data.
- For robots to become part of our everyday lives, they need to learn from everyone, including people who have never used a robot.
- However, not everyone can provide clean data.
- When people teach people, they do more than talk.
- Non-expert teaching, while noisy, is the teaching that robots will receive from the people they live and work with.

**Keep the meaning.** Hang rejected a draft of the film for being too specific about the dissertation's own work, and called the first motivation slides too serious, too wordy, and not illustrative. Hang asked for the outline to be followed in idea, not word for word. Each caption should say its point plainly. A noise label that appears before the scene shows why, and a reference that the audience has to decode, such as the name of a painting or a quotation from an 1874 review, were rejected or removed. The motivation slides follow benefits, then the challenge, then this work.

**Evidence from Hang** · weight 53 (5 instructions, 2 edits, 4 declines, 4 acceptances, 2 notes)

- [HI-14](preference-signals.md#hi-14), Hang's instruction, October 17, 2026 (weight 5). “robots are already in our daily life, but most of training data are produced in lab”.
- [HI-14](preference-signals.md#hi-14), Hang's instruction, October 17, 2026 (weight 5). “reject this version for: being too specific about the work that has already been done in this dissertation”.
- [HI-14](preference-signals.md#hi-14), Hang's instruction, October 17, 2026 (weight 5). “you dont need to use exact words, but get the idea”.
- [HI-13](preference-signals.md#hi-13), Hang's instruction, October 17, 2026 (weight 5). “non-expert teaching should recive attetion and is important while they are noisy”.
- [HI-12](preference-signals.md#hi-12), Hang's instruction, October 17, 2026 (weight 5). “a. the tone, too seriously”.
- [HI-15](preference-signals.md#hi-15), Hang's instruction, October 18, 2026 (weight 5). “page 4 benefits -> page 5 challenge -> page 6 our work”.
- [HI-17](preference-signals.md#hi-17), Hang's instruction, October 18, 2026 (weight 5). “i do not need the monet impression paint name in my video, use imperfection directly is good”.
- [HI-17](preference-signals.md#hi-17), Hang's instruction, October 18, 2026 (weight 5). “the noise tag at 140 s comes out of no where”.
- [DL01](reviews/impression-film-text-draft2.md#dl01), declined (weight 5). Suggested “Le papier peint à l'état embryonnaire”. Hang's note: “what is this?”.
- [VO07](reviews/impression-film-text-draft2.md#vo07), accepted with Hang's edit (weight 4). Suggested “this teaching is set aside as noise”. Hang's wording is “this teaching might too noisy”.
- [VO08](reviews/impression-film-text-draft2.md#vo08), accepted with Hang's edit (weight 4). Suggested “they do more than show”. Hang's wording is “they do more than talk”.
- [VO01](reviews/impression-film-text-draft2.md#vo01), accepted (weight 3). Hang's note: “too strong, weaker. the robots are not that capable now”. The line was Robots already clean our floors, deliver our food, and make our coffee.
- [TX01](reviews/impression-film-text-draft2.md#tx01), declined (weight 3). Suggested “Paris, April 1874”.
- [TX02](reviews/impression-film-text-draft2.md#tx02), declined (weight 3). Suggested “A preliminary drawing for a wallpaper pattern is more finished than this seascape”.
- [TX03](reviews/impression-film-text-draft2.md#tx03), declined (weight 3). Suggested “Louis Leroy, *Le Charivari*, 25 April 1874”.
- [VO04](reviews/impression-film-text-draft2.md#vo04), accepted (weight 1). Accepted “they need to learn from everyone, including people who have never used a robot”.
- [VO05](reviews/impression-film-text-draft2.md#vo05), accepted (weight 1). Accepted “However, not everyone can provide clean data”.
- [VO14](reviews/impression-film-text-draft2.md#vo14), accepted (weight 1). Accepted “Non-expert teaching, while noisy, is the teaching that robots will receive”.

**Basis.** This pattern comes from the evidence from Hang above. It has no paper example.

### Future work and the closing slide in a talk

In a talk, give future work as what the direction is and what it would make possible, and move the record of what has already been built to the speaker notes. Keep the update loop of a planned system when it explains how the direction improves with use. A closing slide states at a high level how each stage builds on the one before, one stage at a time.

**Reusable forms**

- AI agents can plan long-horizon tasks and correct their own mistakes. The same ideas can apply to human-robot interaction.
- The skills and data format could improve through use
- Knowing where the imperfections come from shows how to ask for feedback.

**Keep the meaning.** These choices come from the talk. In the chapters, future work keeps its planned-work wording, as described under Limitations and future work and Future work drafted from notes. Keep untested parts conditional, as in could improve, and do not describe a planned system as having run with users.

**Evidence from Hang** · weight 14 (1 instruction, 5 acceptances, 2 notes)

- [HI-16](preference-signals.md#hi-16), Hang's instruction, October 18, 2026 (weight 5). “8. reduce what has been done in page 66 and 67, focusing on what is agentic HRI and what are the benefits of agentic HRI”.
- [HI-16](preference-signals.md#hi-16), Hang's instruction, October 18, 2026 (weight 5). “focusing on the relationship (i.e., how each stage builds on each other) with very high level takeaways and summarizations”.
- [HI-16](preference-signals.md#hi-16), Hang's instruction, October 18, 2026 (weight 5). “6.simplify page 61 and 62 on text”.
- [SL-R18](reviews/full-talk-slides45-68.md#sl-r18), accepted (weight 3). Hang's note: “the improve with use can still keep the wikiskill style update flow”. The slide became the benefits of agentic HRI, and the counts of what was built moved to the notes.
- [SL-R19](reviews/full-talk-slides45-68.md#sl-r19), accepted (weight 3). Hang's note: “add animation to show one stage at a time”. The general takeaway became a chain in which each part leads to the next.
- [SL-R10](reviews/full-talk-slides45-68.md#sl-r10), accepted (weight 1). “agentic AI has demonstrated very strong capability in self-correction” became “AI agents can plan long-horizon tasks”.
- [S67-S01](reviews/full-talk-wording-review.md#s67-s01), accepted (weight 1). “the skills and the data format both improve with use” became “The skills and data format could improve through use”.
- [S67-W02](reviews/full-talk-wording-review.md#s67-w02), accepted (weight 1). “So far the knowledge base, the trajectories and the seed skills are built” became “No skill has yet been tested on a robot with real users”.

**Basis.** This pattern comes from the evidence from Hang above. It has no paper example.

## Scope of this reference

The two source libraries draw on CHARM, Demonstration Sidetracks, STEADY, Progress, PHIRL, and the RSS Pioneers prospectus. Five are coauthored and the prospectus is single-authored. These sources support a reference for the dissertation's manuscript voice, not attribution of every sentence to Hang personally.

The guide combines observed manuscript patterns, dissertation preferences recorded in the source libraries, reusable editorial forms, and evidence from Hang. The reviews record each decision and the final wording, and only sometimes a note from Hang, so the guidance drawn from a decision is a reading of what changed. Hang's instructions are quoted as typed, including spelling. A later instruction from Hang replaces any pattern. Some edited wording in the record still needs a check before it is used, and [review-decisions.md](review-decisions.md) lists those items.

Reviews that were still undecided on October 19, 2026 give no evidence, except where Hang applied their suggestions by hand. They are listed in [review-decisions.md](review-decisions.md#undecided-reviews).
