# Chapter connection paragraph review

Review `connection-paragraph-review` of the dissertation, from `waiting_for_review/connection-paragraph-review`. Decided between October 12, 2026 and October 12, 2026. Decisions files: `connection-paragraph-review.decisions.20261012-145607.json`.

[All reviews](../review-decisions.md) · [Weighted signals](../preference-signals.md) · [Main reference](../hangs-writing-style-reference.md)

| Outcome | Decided by Hang | Not decided by Hang |
| --- | ---: | ---: |
| Accepted as suggested | 15 | 0 |
| Accepted with Hang's edit | 3 | 0 |
| Declined | 5 | 0 |
| Notes from Hang | 1 | |

### CP-01

**Accepted** · weight 1 · Connection wording · Chapter 1, roadmap sentences · Chapter 1 › Progress-Heuristicized Inverse Reinforcement Learning, `chapters/introduction.tex`, line 153

Suggestion: Chapter labels in the lead-in to PHIRL

Original:

~~~latex
Chapters 3 to chapter 6 identify patterned imperfections in human evaluative feedback and human demonstrations, and formalize \textit{progress} as a teaching signal.
~~~

Accepted wording:

~~~latex
\autoref{ch:charm} to \autoref{ch:progress} identify patterned imperfections in human evaluative feedback and human demonstrations, and formalize \textit{progress} as a teaching signal.
~~~

Note written with the suggestion: The sentence names the earlier chapters by typed numbers, and the second "chapter" is in lower case. Chapter labels replace the numbers, so they stay correct if a chapter moves (style reference, "Established dissertation terminology": refer to a chapter by its label, as in your edit of DW-56). The rest of the sentence is unchanged.

### CP-02

**Declined** · weight 3 · Connection wording · Chapter 1, roadmap sentences · Chapter 1 › Towards Richer Human Evaluative Feedback, `chapters/introduction.tex`, line 126

Suggestion: "The preceding chapters" in Chapter 1

Original, which stayed:

~~~latex
The preceding chapters show that human evaluative feedback is affected by factors beyond the teaching task itself (\autoref{ch:charm}), and that human scalar evaluative feedback can be more effective if stabilized (\autoref{ch:steady}).
~~~

Declined suggestion:

~~~latex
The studies described above show that human evaluative feedback is affected by factors beyond the teaching task itself (\autoref{ch:charm}), and that human scalar evaluative feedback can be more effective if stabilized (\autoref{ch:steady}).
~~~

Note written with the suggestion: This sentence is in Chapter 1. No chapter precedes it, and the two chapters it cites come later. "The studies described above" refers to the two summaries that Chapter 1 has just given. No other word changes.

Not used in a pattern: Fact, logic, equation, or caption corrections that Hang declined. They are kept so that the same correction is not offered again without new information.

### CP-03

**Accepted** · weight 1 · Connection wording · Chapter 1, roadmap sentences · Chapter 1 › Outline, `chapters/introduction.tex`, line 193

Suggestion: Outline entry for Chapter 8

Original:

~~~latex
Chapter 8 brings together the discussions from the preceding studies, including human factors in teaching, the use of scalar evaluative feedback and \textit{progress} for learning, and the studies' limitations and directions for further work.
~~~

Accepted wording:

~~~latex
Chapter 8 considers the studies together by answering the three questions of this dissertation, describing the findings that connect the chapters, identifying what the combined evidence does not yet show, and outlining directions for future work.
~~~

Note written with the suggestion: The entry describes Chapter 8 as it was before the chapter was rewritten. The new entry names the four parts that the chapter has now, in the words of the chapter's own opening. It stays one sentence, like the other entries and like the outline in Short's dissertation ("Chapter 3 describes ...").

Used in: [A roadmap with actual content](../hangs-writing-style-reference.md#a-roadmap-with-actual-content).

### CP-04

**Declined** · weight 5 · Spelling · Chapter 2, summary · Chapter 2 › Summary, `chapters/background.tex`, line 238

Suggestion: Capital letter at the start of a list item

Original, which stayed:

~~~latex
interactive learning methods prefer binary feedback.
~~~

Declined suggestion:

~~~latex
Interactive learning methods prefer binary feedback.
~~~

Hang's note: ignore this one

Note written with the suggestion: Capital letter only.

Not used in a pattern: Superseded by another suggestion on the same text, which Hang decided instead.

### CP-05

**Accepted** · weight 1 · Spelling · Chapter 2, summary · Chapter 2 › Summary, `chapters/background.tex`, line 239

Suggestion: "commom assuptions"

Original:

~~~latex
Methods that combine demonstrations and feedback have commom assuptions such as expert teachers, near-optimal demonstrations, or a human who remains in the training loop.
~~~

Accepted wording:

~~~latex
Methods that combine demonstrations and feedback have common assumptions such as expert teachers, near-optimal demonstrations, or a human who remains in the training loop.
~~~

Note written with the suggestion: Two spelling corrections. No other word changes.

### CP-06

**Declined** · weight 3 · Connection wording · Chapter 2, summary · Chapter 2 › Summary, `chapters/background.tex`, line 243

Suggestion: A link from the summary of Chapter 2 to the chapters that follow

New text, placed next to this passage:

~~~latex
The studies were conducted in a public space to recruit participants in non-lab settings, and the data and results can be expected to better reflect robot-in-the-wild deployments than in-lab setups. \hang{tense end}
~~~

Declined suggestion:

~~~latex
The chapters that follow address the three points listed above in order.
\autoref{ch:charm} and \autoref{ch:sidetracks} examine the first point, \autoref{ch:steady} and \autoref{ch:progress} address the second point, and \autoref{ch:phirl} addresses the third point.
~~~

Note written with the suggestion: Optional. Chapters 3 to 8 each end by pointing to the next chapter, and Chapter 2 ends without saying where its three numbered points are taken up. Short ends a chapter summary with one plain sentence of this kind ("This robot is used in a number of the studies in this dissertation work, including one of the studies of SAR target populations in Chapter 4, and the validation studies in Chapters 5, 6, 7, and 8"). The two new sentences only map the three points of this summary to the chapters, and they add no claim. They are added to the end of the last paragraph. Reject this item if the summary should end on the public space sentence.

Used in: [A roadmap with actual content](../hangs-writing-style-reference.md#a-roadmap-with-actual-content), [Adding sentences that were not asked for](../hangs-writing-style-reference.md#adding-sentences-that-were-not-asked-for).

### CP-07

**Accepted** · weight 1 · Connection wording · Chapter 3, opening and bridge · Chapter 3, `chapters/charm.tex`, line 6

Suggestion: The name of the first stage, where the stage begins

Original:

~~~latex
This chapter begins the first stage of this dissertation: understanding the imperfections in non-expert teaching that arise not only from the task or the robot, but also from the human teachers themselves.
~~~

Accepted wording:

~~~latex
This chapter begins the first stage of this dissertation, which is to understand and model the imperfections in non-expert teaching that arise not only from the task or the robot, but also from the human teachers themselves.
~~~

Note written with the suggestion: Two changes. (1) The first stage is named "understanding and modeling" at the end of Chapter 4, after your edit there, and "understanding" here. "understand and model" makes the two places agree, and it matches the title of the dissertation. (2) The colon becomes ", which is to", the form you wrote in DW-16 (style reference, "Few colons and semicolons"). PR-016 in the punctuation review changes the same sentence to "by examining the imperfections", which removes the name of the stage. Decide this item before PR-016. If you accept this item, PR-016 will report "not found" and can be left. If you reject it, PR-016 still applies.

Used in: [The three stage dissertation arc](../hangs-writing-style-reference.md#the-three-stage-dissertation-arc).

### CP-08

**Declined** · weight 3 · Connection wording · Chapter 3, opening and bridge · Chapter 3 › Summary, `chapters/charm.tex`, line 395

Suggestion: The results as the subject of "showed"

Original, which stayed:

~~~latex
This chapter showed that the feedback non-experts give to a robot is associated not only with the robot's behavior, but also with the characteristics of the teacher.
~~~

Declined suggestion:

~~~latex
The results of this chapter showed that the feedback non-experts give to a robot is associated not only with the robot's behavior, but also with the characteristics of the teacher.
~~~

Note written with the suggestion: Style reference, "Impersonal dissertation voice": a chapter can propose, examine, or present, and the results show. You made the same kind of change in DW-06, where "The second stage indicates" became "The results of the second stage indicate". Only the subject changes.

Used in: [This chapter as the subject](../hangs-writing-style-reference.md#this-chapter-as-the-subject).

### CP-09

**Accepted** · weight 1 · Connection wording · Chapter 4, opening · Chapter 4, `chapters/sidetracks.tex`, line 11

Suggestion: What Chapter 3 found, and the question that Chapter 4 takes from it

Original:

~~~latex
The results presented in \autoref{ch:charm} indicate that differences in how non-experts teach are not simply random noise, but are associated with who the teachers are.
This chapter asks whether the same holds for demonstrations.
~~~

Accepted wording:

~~~latex
The results presented in \autoref{ch:charm} indicate that differences in the feedback that non-experts give are not simply random noise, but are associated with the characteristics of the teachers.
This chapter asks whether the imperfections in non-expert demonstrations also contain systematic structure.
~~~

Note written with the suggestion: This paragraph follows Short's form for opening a chapter ("The results presented in Chapter 5 support ... In this chapter, we build on those results to ..."). Three changes keep that form and make the link exact. (1) "who the teachers are" becomes "the characteristics of the teachers", the change you accepted in DW-02. (2) Chapter 3 measured feedback, so "how non-experts teach" becomes "the feedback that non-experts give". (3) In "whether the same holds for demonstrations", "the same" refers to an association with the teacher, which this chapter does not examine. The new second sentence states the question that this chapter examines, in the words used at the end of Chapter 3 ("whether they also contain systematic structure").

### CP-10

**Accepted** · weight 1 · Connection wording · Chapter 5, opening and bridge · Chapter 5, `chapters/steady.tex`, line 14

Suggestion: What the first stage found

Original:

~~~latex
The first stage of this dissertation found that non-expert feedback is shaped by factors beyond the task, such as the characteristics of the teacher (\autoref{ch:charm}), and that non-expert demonstrations contain frequent sidetracks (\autoref{ch:sidetracks}).
~~~

Accepted wording:

~~~latex
The results of the first stage of this dissertation indicate that non-expert feedback is associated with factors beyond the task, such as the characteristics of the teacher (\autoref{ch:charm}), and that non-expert demonstrations contain frequent sidetracks (\autoref{ch:sidetracks}).
~~~

Note written with the suggestion: Two changes. (1) "The first stage of this dissertation found" becomes "The results of the first stage of this dissertation indicate", as in DW-06. (2) "is shaped by" becomes "is associated with". Chapter 3 reports associations, and Chapter 8 says that this evidence is correlational (style reference, "Numbers and measured comparisons": do not turn correlation into causation).

Used in: [Reporting findings and interpretations](../hangs-writing-style-reference.md#reporting-findings-and-interpretations).

### CP-11

**Accepted** · weight 1 · Connection wording · Chapter 5, opening and bridge · Chapter 5, `chapters/steady.tex`, line 18

Suggestion: "however" moved to the start of its sentence

Original:

~~~latex
Restricting feedback in this way, however, also discards information, such as the magnitude of a teacher's evaluation.
~~~

Accepted wording:

~~~latex
However, restricting feedback in this way also discards information, such as the magnitude of a teacher's evaluation.
~~~

Note written with the suggestion: Style reference, "Connectors with a clear job": However opens its sentence, as in your edit of DW-19. No other word changes.

### CP-12

**Accepted** · weight 1 · Connection wording · Chapter 5, opening and bridge · Chapter 5, `chapters/steady.tex`, line 19

Suggestion: The aim of the chapter stated as an aim

Original:

~~~latex
Rather than reducing the variability of scalar feedback by reducing its information, this chapter measures how inconsistent scalar feedback actually is, and shows that its inconsistency can be mitigated algorithmically.
~~~

Accepted wording:

~~~latex
Rather than reducing the variability of scalar feedback by reducing its information, this chapter measures how inconsistent scalar feedback actually is, and examines whether its inconsistency can be mitigated algorithmically.
~~~

Note written with the suggestion: This sentence ends the paragraph that motivates the chapter, and it states the outcome as a general fact ("shows that its inconsistency can be mitigated"). The paragraph above it already reports the result with its scope ("in the evaluated task"). With "examines whether", the sentence states what the chapter sets out to do (style reference, "Research actions": a chapter examines a question, and the result is reported with its evidence). Short states the aim at the same place in her chapter openings ("In this chapter, we build on those results to develop ..."). Only "shows that" changes.

### CP-13

**Accepted** · weight 1 · Connection wording · Chapter 5, opening and bridge · Chapter 5 › Summary, `chapters/steady.tex`, line 721

Suggestion: The results as the subject of "showed"

Original:

~~~latex
This chapter showed that scalar feedback, once stabilized, outperformed binary feedback in the evaluated task, and that teachers' feedback patterns remain statistically distinguishable from one another even when they evaluate identical robot behavior.
~~~

Accepted wording:

~~~latex
The results of this chapter showed that scalar feedback, once stabilized, outperformed binary feedback in the evaluated task, and that teachers' feedback patterns remain statistically distinguishable from one another even when they evaluate identical robot behavior.
~~~

Note written with the suggestion: The same change as CP-08. Only the subject changes.

Used in: [This chapter as the subject](../hangs-writing-style-reference.md#this-chapter-as-the-subject).

### CP-14

**Accepted with Hang's edit** · weight 4 · Connection wording · Chapter 6, opening and bridge · Chapter 6, `chapters/progress.tex`, line 10

Suggestion: What the earlier chapters found, as the reason for a new signal

Original:

~~~latex
The results presented in \autoref{ch:steady} show that the inconsistency of scalar feedback can be mitigated after it has been given, and the first stage of this dissertation suggests the underling reasons: feedback is shaped by the characteristics of the teacher (\autoref{ch:charm}), and non-expert demonstrations contain frequent sidetracks, behaviors that do not advance the task but are often part of how non-experts succeed at it (\autoref{ch:sidetracks}).
~~~

Suggested:

~~~latex
The results presented in \autoref{ch:steady} show that the inconsistency of scalar feedback can be mitigated after it has been given, and the first stage of this dissertation suggests the underlying reasons.
Feedback is associated with the characteristics of the teacher (\autoref{ch:charm}), and non-expert demonstrations contain frequent sidetracks, behaviors that do not advance the task but are often part of how non-experts succeed at it (\autoref{ch:sidetracks}).
~~~

Hang's wording:

~~~latex
The results presented in \autoref{ch:steady} show that the inconsistency of scalar feedback can be mitigated after it has been given, and the first stage of this dissertation suggests the underlying reasons:
feedback is associated with the characteristics of the teacher (\autoref{ch:charm}), and non-expert demonstrations contain frequent sidetracks, behaviors that do not advance the task but are often part of how non-experts succeed at it (\autoref{ch:sidetracks}).
~~~

Note written with the suggestion: Three changes. (1) "is shaped by" becomes "is associated with", as in CP-10. (2) The colon is replaced by a new sentence. (3) "underling" is corrected to "underlying". PR-058 in the punctuation review makes changes 2 and 3 only. Decide this item before PR-058. If you accept this item, PR-058 will report "not found" and can be left. If you reject it, PR-058 still applies.

Used in: [Reporting findings and interpretations](../hangs-writing-style-reference.md#reporting-findings-and-interpretations), [Few colons and semicolons](../hangs-writing-style-reference.md#few-colons-and-semicolons).

### CP-15

**Accepted** · weight 1 · Spelling · Chapter 6, opening and bridge · Chapter 6, `chapters/progress.tex`, line 11

Suggestion: "inidates"

Original:

~~~latex
Conventional evaluative feedback inidates how well a demonstration was performed rather than how much of the task it accomplished, so that a demonstration containing many sidetracks may receive a low rating even if it completed the task.
~~~

Accepted wording:

~~~latex
Conventional evaluative feedback indicates how well a demonstration was performed rather than how much of the task it accomplished, so that a demonstration containing many sidetracks may receive a low rating even if it completed the task.
~~~

Note written with the suggestion: One spelling correction. No other word changes.

### CP-16

**Accepted** · weight 1 · Connection wording · Chapter 6, opening and bridge · Chapter 6, `chapters/progress.tex`, line 13

Suggestion: The intuition stated as an expectation

Original:

~~~latex
The intuition is that giving teachers objective references, the start state and the completed state of the task, makes the signal more consistent across teachers and more robust to the imperfections in their demonstrations.
~~~

Accepted wording:

~~~latex
The intuition is that giving teachers objective references, the start state and the completed state of the task, would make the signal more consistent across teachers and more robust to the imperfections in their demonstrations.
~~~

Note written with the suggestion: Style reference, "An intuition leading to an operation": an intuition is a design rationale, and its modal strength should match its status. "makes" states the outcome as a fact before the studies are described. "would make" states it as the expectation that the studies then test. Chapter 1 states the same intuition with "could". Only this verb changes.

### CP-17

**Accepted with Hang's edit** · weight 4 · Connection wording · Chapter 6, opening and bridge · Chapter 6 › Summary, `chapters/progress.tex`, line 502

Suggestion: The result that the next chapter builds on

Original:

~~~latex
This chapter also found that \textit{progress} is strongly correlated with a reward function learned from the same demonstrations, suggesting that the two carry compatible information about the task.
~~~

Suggested:

~~~latex
The results also showed that \textit{progress} is strongly correlated with a reward function learned from the same demonstrations, which suggests that the two carry compatible information about the task.
~~~

Hang's wording:

~~~latex
The results also showed that \textit{progress} is strongly correlated with a reward function learned from the same demonstrations, suggesting that the two carry compatible information about the task.
~~~

Note written with the suggestion: Two changes. (1) "This chapter also found" becomes "The results also showed", as in CP-08. (2) "suggesting that" becomes "which suggests that", the form you wrote in DW-36 for an interpretation that follows a result in the same sentence.

Used in: [Reporting findings and interpretations](../hangs-writing-style-reference.md#reporting-findings-and-interpretations).

### CP-18

**Declined** · weight 3 · Connection wording · Chapter 7, opening and bridge · Chapter 7, `chapters/phirl.tex`, line 16

Suggestion: The two results that PHIRL builds on

Original, which stayed:

~~~latex
PHIRL builds on two results from the preceding chapters: \textit{progress} is consistent and intuitive for non-expert users (\autoref{ch:progress}), and non-expert demonstrations contain structured imperfections that do not advance the task (\autoref{ch:sidetracks}).
~~~

Declined suggestion:

~~~latex
PHIRL builds on two results from the preceding chapters.
First, \textit{progress} is consistent and intuitive for non-expert users (\autoref{ch:progress}).
Second, non-expert demonstrations contain structured imperfections that do not advance the task (\autoref{ch:sidetracks}).
~~~

Note written with the suggestion: The colon before the two results is replaced by First and Second (style reference, "Procedural series and enumerations", as in your edit of DW-51). The wording of the two results is unchanged. The paragraph already follows Short's form ("In this chapter, we build on those results to ..."). PR-071 in the punctuation review splits the same sentence at the colon, and its second sentence then begins with a lower-case "progress". Decide this item before PR-071. If you accept this item, PR-071 will report "not found" and can be left. If you reject it, PR-071 still applies.

Used in: [Procedural series and enumerations](../hangs-writing-style-reference.md#procedural-series-and-enumerations).

### CP-19

**Accepted** · weight 1 · Connection wording · Chapter 7, opening and bridge · Chapter 7 › Summary, `chapters/phirl.tex`, line 699

Suggestion: What the two forms of teaching provide

Original:

~~~latex
This chapter completes the final stage of this dissertation, providing evidence that imperfect teaching can be leveraged for learning when complementary forms of teaching are combined: demonstrations provide dense but imperfect information about how to perform a task, and \textit{progress} annotations on a small subset of them indicate which of the demonstrated behaviors actually advance it.
~~~

Accepted wording:

~~~latex
This chapter completes the final stage of this dissertation, providing evidence that imperfect teaching can be leveraged for learning when complementary forms of teaching are combined.
Demonstrations provide dense but imperfect information about how to perform a task, while \textit{progress} annotations on a small subset of them provide sparse information about which parts of a demonstration advance the task.
~~~

Note written with the suggestion: Three changes. (1) "indicate which of the demonstrated behaviors actually advance it" becomes the wording of Chapter 8 after your edit in DW-12 ("provides sparse information about which parts of a demonstration advance the task"). Progress was annotated on ten segments of each demonstration and not on individual behaviors, and Chapter 8 says that the discounting of sidetracks is an inference and not a measured result. (2) "and" becomes "while", as in DW-12. (3) The colon is replaced by a new sentence. PR-085 in the punctuation review makes change 3 only. Decide this item before PR-085. If you accept this item, PR-085 will report "not found" and can be left. If you reject it, PR-085 still applies.

### CP-20

**Accepted** · weight 1 · Connection wording · Chapter 7, opening and bridge · Chapter 7 › Summary, `chapters/phirl.tex`, line 700

Suggestion: What the next chapter does

Original:

~~~latex
The next chapter steps back from the individual studies of \autoref{ch:charm} through \autoref{ch:phirl} and considers what they suggest when taken together: which lessons hold across both forms of teaching and all three stages, and where the findings stop applying.
~~~

Accepted wording:

~~~latex
The next chapter considers the studies of \autoref{ch:charm} through \autoref{ch:phirl} together.
It answers the three questions of this dissertation, describes the findings that connect the chapters, identifies what the combined evidence does not yet show, and outlines directions for future work.
~~~

Note written with the suggestion: The sentence describes Chapter 8 as it was before the chapter was rewritten ("which lessons hold across both forms of teaching and all three stages, and where the findings stop applying"). The new text names the four parts of the chapter, as the chapter's own opening does. "steps back from" and "when taken together" are replaced by literal wording (style reference, "Literal wording", which names "read together" as a phrase to replace). PR-086 in the punctuation review removes the colon of the same sentence and keeps the old description. Decide this item before PR-086. If you accept this item, PR-086 will report "not found" and can be left. If you reject it, PR-086 still applies.

### CP-21

**Accepted** · weight 1 · Connection wording · The third question, in the wording of Chapter 1 · Chapter 8, `chapters/discussion.tex`, line 7

Suggestion: The third question in the opening of Chapter 8

Original:

~~~latex
\hang{style start} It first answers the three questions of this dissertation (\autoref{sec:discussion-questions}): whether the imperfections in non-expert teaching are random noise, whether the inconsistency of non-expert feedback can be reduced while utilizing the magnitudes, and whether imperfect demonstrations and feedback can be combined so that a robot learns more from both with little additional human effort. \hang{style end}
~~~

Accepted wording:

~~~latex
It first answers the three questions of this dissertation (\autoref{sec:discussion-questions}): whether the imperfections in non-expert teaching are random noise, whether the inconsistency of non-expert feedback can be reduced while utilizing the magnitudes, and whether combining demonstrations and feedback can lower quality requirements for human teaching and reduce human effort in annotating.
~~~

Note written with the suggestion: You chose the Chapter 1 wording of the third question. Only the third question changes here, and it now reads as in Chapter 1 ("whether combining demonstrations and feedback can lower quality requirements for human teaching and reduce human effort in annotating"). The colon before the three questions is kept. PR-087 in the punctuation review splits this sentence at the colon and has the old third question. Decide this item before PR-087. If you accept this item, PR-087 will report "not found" and can be left. If you reject it, PR-087 still applies.

### CP-22

**Accepted with Hang's edit** · weight 4 · Connection wording · The third question, in the wording of Chapter 1 · Chapter 8 › Answers to the Overarching Questions, `chapters/discussion.tex`, line 47

Suggestion: The third question above its answer in Section 8.1

Original:

~~~latex
\textit{Can imperfect demonstrations and feedback be combined so that a robot learns more from both with little additional human effort?}
~~~

Suggested:

~~~latex
\textit{Can combining demonstrations and feedback lower quality requirements for human teaching and reduce human effort in annotating?}
~~~

Hang's wording:

~~~latex
\textit{Can combining demonstrations and feedback enable robust reward learning while reducing human effort in annotating?}
~~~

Note written with the suggestion: The same question in question form, as the first two questions of this section are written. The answer below it needs no change. It reports that 20 percent of the demonstrations were annotated, which concerns the effort in annotating, and that the margin of PHIRL was larger on the mixed-quality datasets, which concerns the quality requirements. Accept this item together with CP-21, so that the opening and the section ask the same question.

Used in: [The three stage dissertation arc](../hangs-writing-style-reference.md#the-three-stage-dissertation-arc).

### CP-23

**Accepted** · weight 1 · Spelling · The third question, in the wording of Chapter 1 · Chapter 1 › Overview, `chapters/introduction.tex`, line 56

Suggestion: A missing space in the Chapter 1 sentence

Original:

~~~latex
Each stage addresses one question: whether the imperfections in non-expert teaching are random noise (\autoref{ch:charm} and \autoref{ch:sidetracks}); whether the inconsistency of non-expert feedback can be reduced while utilizing the magnitudes (\autoref{ch:steady} and \autoref{ch:progress}); and whether combining demonstrations and feedback can lower quality requirements for human teaching and reduce human effort in annotating(\autoref{ch:phirl}).
~~~

Accepted wording:

~~~latex
Each stage addresses one question: whether the imperfections in non-expert teaching are random noise (\autoref{ch:charm} and \autoref{ch:sidetracks}); whether the inconsistency of non-expert feedback can be reduced while utilizing the magnitudes (\autoref{ch:steady} and \autoref{ch:progress}); and whether combining demonstrations and feedback can lower quality requirements for human teaching and reduce human effort in annotating (\autoref{ch:phirl}).
~~~

Note written with the suggestion: One space is added before the last reference, after "annotating". No word changes, and the colon and the semicolons stay as you kept them when you rejected PR-001.
