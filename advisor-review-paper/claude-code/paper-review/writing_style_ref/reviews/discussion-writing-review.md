# Chapter 8 writing improvement review

Review `discussion-writing-review` of the dissertation, from `waiting_for_review/discussion-writing-review`. Decided between October 12, 2026 and October 12, 2026. Decisions files: `discussion-writing-review.decisions.20261012-125234.json`.

[All reviews](../review-decisions.md) · [Weighted signals](../preference-signals.md) · [Main reference](../hangs-writing-style-reference.md)

| Outcome | Decided by Hang | Not decided by Hang |
| --- | ---: | ---: |
| Accepted as suggested | 26 | 0 |
| Accepted with Hang's edit | 24 | 0 |
| Declined | 11 | 0 |
| Notes from Hang | 0 | |

**To check before the accepted wording is used**

- [DW-07](#dw-07). Chapter 6 reports p < 0.05 for two of the four imperfect scenarios (Imperfect and Failure), and p = 0.060 and p = 0.058 for the other two. The edited sentence says significantly for all four. OA-804 offered the count again, and Hang declined it.
- [DW-19](#dw-19). The first sentence of the edited wording has no period after moving closer. OA-805 added it, and Hang accepted.
- [DW-25](#dw-25). The spelling corrections in this suggestion (charpters, extentions) were declined with it. OA-806 offered them alone, and Hang accepted.
- [DW-29](#dw-29). The spelling corrections in this suggestion (scenairos, planing) were declined with it. OA-808 offered them alone, and Hang accepted.
- [DW-30](#dw-30). The idiom is taking advantage of. The edited wording has taking advantages of. OA-809 corrected it, and Hang accepted.
- [DW-35](#dw-35). The grammar corrections in this suggestion (low-quality before a noun, adding to in place of including into) were declined with it.
- [DW-52](#dw-52). The spelling corrections in this suggestion (comunicate, hiddent varibles) were declined with it. OA-810 and OA-811 offered them alone, and Hang accepted.
- [DW-54](#dw-54). The edited wording has such as International Conference, without the. OA-812 added it, and Hang accepted.
- [DW-56](#dw-56). In the edited wording, and use to decide has no object (and use them to decide). OA-813 added it, and Hang accepted.

### DW-01

**Accepted** · weight 1 · Wording (style reference) · 8 opening · Chapter 8, `chapters/discussion.tex`, line 7

Suggestion: Roadmap sentence for the first section

Original:

~~~latex
\hang{grammar start} It first answers the three questions that were asked by this dissertation: whether the imperfections in non-expert teaching are random noise, whether the inconsistency of non-expert feedback can be reduced while utilizing the magnitudes, and whether imperfect demonstrations and feedback can be combined so that a robot learns more from both with less additional human effort. \hang{grammar end}
~~~

Accepted wording:

~~~latex
It first answers the three questions of this dissertation (\autoref{sec:discussion-questions}): whether the imperfections in non-expert teaching are random noise, whether the inconsistency of non-expert feedback can be reduced while utilizing the magnitudes, and whether imperfect demonstrations and feedback can be combined so that a robot learns more from both with little additional human effort.
~~~

Note written with the suggestion: Style reference, "A roadmap with actual content". The next sentence gives a section number for the second and third sections, so the first section gets one too. "that were asked by this dissertation" becomes "of this dissertation". The third question said "less additional human effort" here and "little additional human effort" in the heading of Section 8.1; "little" is used in both now.

Used in: [A roadmap with actual content](../hangs-writing-style-reference.md#a-roadmap-with-actual-content).

### DW-02

**Accepted** · weight 1 · Wording (style reference) · 8.1 Answers to the Overarching Questions · Chapter 8 › Answers to the Overarching Questions, `chapters/discussion.tex`, line 16

Suggestion: One sentence for the correlations, one for the model

Original:

~~~latex
Feedback accuracy was associated with who the teacher was: robot experience and educational background correlated with feedback accuracy at 0.25 and 0.16, and a model that included the characteristics of the teacher predicted feedback values more accurately than a model that used task statistics alone, for teachers represented in the training data (\autoref{ch:charm}).
~~~

Accepted wording:

~~~latex
Feedback accuracy was associated with the characteristics of the teacher: robot experience and educational background showed positive associations with feedback accuracy, with correlations of 0.25 and 0.16, respectively.
A model that included these characteristics also predicted feedback values more accurately than a model that used task statistics alone, for teachers represented in the training data (\autoref{ch:charm}).
~~~

Note written with the suggestion: Style reference, "One main job" and "Numbers and measured comparisons". The sentence reported the correlations and the model comparison together. The correlation wording follows the form you gave earlier ("showed positive associations ..., with correlations of 0.25 and 0.16, respectively"). "who the teacher was" becomes "the characteristics of the teacher", the term used in the rest of the paragraph.

Used in: [Numbers and measured comparisons](../hangs-writing-style-reference.md#numbers-and-measured-comparisons), [Direct subjects and concrete details](../hangs-writing-style-reference.md#direct-subjects-and-concrete-details).

### DW-03

**Accepted** · weight 1 · Wording (style reference) · 8.1 Answers to the Overarching Questions · Chapter 8 › Answers to the Overarching Questions, `chapters/discussion.tex`, line 17

Suggestion: "tied to the task" becomes "task-related"

Original:

~~~latex
Demonstration sidetracks made up about 48\% of the recorded timesteps, and they were tied to the task: 54.7\% of them occurred within windows around changes of task phase that cover 40\% of the timesteps, and 73\% of \textit{Alignment} behaviors started and ended within 0.1\,m of a target object (\autoref{ch:sidetracks}).
~~~

Accepted wording:

~~~latex
Demonstration sidetracks made up about 48\% of the recorded timesteps, and they were task-related: 54.7\% of them occurred within windows around changes of task phase that cover 40\% of the timesteps, and 73\% of \textit{Alignment} behaviors started and ended within 0.1\,m of a target object (\autoref{ch:sidetracks}).
~~~

Note written with the suggestion: Style reference, "Imperfect teaching and structured behavior": use patterned, systematic, or task-related when the analysis establishes structure. Only these words change.

Used in: [Imperfect teaching and structured behavior](../hangs-writing-style-reference.md#imperfect-teaching-and-structured-behavior).

### DW-04

**Accepted** · weight 1 · Wording (style reference) · 8.1 Answers to the Overarching Questions · Chapter 8 › Answers to the Overarching Questions, `chapters/discussion.tex`, line 18

Suggestion: "Read together ... point to"

Original:

~~~latex
Read together, the two studies point to three sources of structure: the teacher, the demands of the task at a given moment, and the channel through which the teaching is given.
~~~

Accepted wording:

~~~latex
Together, these findings suggest three sources of structure: the teacher, the demands of the task at a given moment, and the channel through which the teaching is given.
~~~

Note written with the suggestion: Style reference, "Literal wording", which names "read together" as a phrase to replace with "These findings suggest".

Used in: [Literal wording](../hangs-writing-style-reference.md#literal-wording).

### DW-05

**Accepted** · weight 1 · Wording (style reference) · 8.1 Answers to the Overarching Questions · Chapter 8 › Answers to the Overarching Questions, `chapters/discussion.tex`, line 20

Suggestion: Which consistency was measured for which signal

Original:

~~~latex
With a controller that mapped each button or joystick to one degree of freedom, participants controlled a single dimension in 75\% of the timesteps in which the robot moved (\autoref{ch:sidetracks}), and feedback given on a binary scale, on a scalar scale, and as \textit{progress} differed in how consistent it was within and between teachers (\autoref{ch:steady}, \autoref{ch:progress}).
~~~

Accepted wording:

~~~latex
With a controller that mapped each button or joystick to one degree of freedom, participants controlled a single dimension in 75\% of the timesteps in which the robot moved (\autoref{ch:sidetracks}).
Binary and scalar evaluative feedback differed in consistency within and between teachers (\autoref{ch:steady}), and \textit{progress} and scalar evaluative feedback differed in consistency between teachers (\autoref{ch:progress}).
~~~

Note written with the suggestion: Style reference, "Accuracy consistency and robustness": name the dimension and the unit of comparison. The sentence said that all three kinds of feedback differed "within and between teachers", but Section 8.3 says that the consistency of progress was measured between teachers only. The revision says which comparison comes from which chapter, and gives demonstrations and feedback a sentence each.

Used in: [Accuracy consistency and robustness](../hangs-writing-style-reference.md#accuracy-consistency-and-robustness).

### DW-06

**Accepted with Hang's edit** · weight 4 · Wording (style reference) · 8.1 Answers to the Overarching Questions · Chapter 8 › Answers to the Overarching Questions, `chapters/discussion.tex`, line 24

Suggestion: "by two routes"

Original:

~~~latex
The second stage indicates that it can, by two routes that act at different points.
~~~

Suggested:

~~~latex
The results of the second stage indicate that it can, in two ways that act at different points.
~~~

Hang's wording:

~~~latex
The results of the second stage indicate that it can act at different points in two ways.
~~~

Note written with the suggestion: Style reference, "Literal wording", which names "by two routes". "in two ways" is the wording of Chapter 9 ("mitigated it in two ways"). The results indicate the answer, so they are the subject.

Used in: [Impersonal dissertation voice](../hangs-writing-style-reference.md#impersonal-dissertation-voice), [Literal wording](../hangs-writing-style-reference.md#literal-wording), [Complete clauses in place of elliptical endings](../hangs-writing-style-reference.md#complete-clauses-in-place-of-elliptical-endings).

### DW-07

**Accepted with Hang's edit** · weight 4 · Wording (style reference) · 8.1 Answers to the Overarching Questions · Chapter 8 › Answers to the Overarching Questions, `chapters/discussion.tex`, line 31

Suggestion: Two studies, two sentences

Original:

~~~latex
When participants in the second online study rated the same imperfect demonstrations, \textit{progress} varied less across participants than scalar feedback in all four imperfect scenarios, significantly so in two of them, and in the public space study the average standard deviation across participants was 11.6 for \textit{progress} and 25.5 for scalar feedback (\autoref{ch:progress}).
~~~

Suggested:

~~~latex
When participants in the second online study rated the same imperfect demonstrations, \textit{progress} varied less across participants than scalar feedback in all four imperfect scenarios, significantly so in two of them.
In the public space study, the average standard deviation across participants was 11.6 for \textit{progress}, compared with 25.5 for scalar feedback (\autoref{ch:progress}).
~~~

Hang's wording:

~~~latex
When participants in the second online study rated the same imperfect demonstrations, \textit{progress} varied less across participants than scalar feedback in all four imperfect scenarios significantly.
In the public space study, the average standard deviation across participants was 11.6 for \textit{progress}, compared with 25.5 for scalar feedback (\autoref{ch:progress}).
~~~

To check: Chapter 6 reports p < 0.05 for two of the four imperfect scenarios (Imperfect and Failure), and p = 0.060 and p = 0.058 for the other two. The edited sentence says significantly for all four. OA-804 offered the count again, and Hang declined it.

Note written with the suggestion: Style reference, "One main job" and "Numbers and measured comparisons" ("[value A], compared with [value B] for [baseline]"). The online study and the public space study each get a sentence. No number changes.

Used in: [Numbers and measured comparisons](../hangs-writing-style-reference.md#numbers-and-measured-comparisons), [One main job and varied sentence length](../hangs-writing-style-reference.md#one-main-job-and-varied-sentence-length).

### DW-08

**Declined** · weight 3 · Spelling and grammar · 8.1 Answers to the Overarching Questions · Chapter 8 › Answers to the Overarching Questions, `chapters/discussion.tex`, line 33

Suggestion: "while retaining" had no subject

Original, which stayed:

~~~latex
These results support \textit{progress} as a more consistent signal of task completion in the studied settings, while retaining magnitude information about how much of the task has been completed.
~~~

Declined suggestion:

~~~latex
These results support \textit{progress} as a more consistent signal of task completion in the studied settings, and as a signal that retains magnitude information about how much of the task has been completed.
~~~

Note written with the suggestion: Grammar. As written, "these results" is what retains magnitude information. The revision makes progress the signal that retains it.

Used in: [Concession with while](../hangs-writing-style-reference.md#concession-with-while).

### DW-09

**Accepted** · weight 1 · Wording (style reference) · 8.1 Answers to the Overarching Questions · Chapter 8 › Answers to the Overarching Questions, `chapters/discussion.tex`, line 35

Suggestion: "The two routes supply"

Original:

~~~latex
The two routes supply references for interpreting a teacher's values, but they describe different things: STEADY retains a judgment of quality, whereas \textit{progress} describes completion.
~~~

Accepted wording:

~~~latex
Both approaches provide references for interpreting a teacher's values, but they describe different quantities: STEADY retains a judgment of quality, whereas \textit{progress} describes completion.
~~~

Note written with the suggestion: Style reference, "Literal wording" ("routes", "supplied") and "Teachers and collection settings" (provide or give). The Summary of this chapter already says "Both approaches". "different things" becomes "different quantities".

Used in: [Literal wording](../hangs-writing-style-reference.md#literal-wording), [Word choices made in review](../hangs-writing-style-reference.md#word-choices-made-in-review).

### DW-10

**Accepted** · weight 1 · Wording (style reference) · 8.1 Answers to the Overarching Questions · Chapter 8 › Answers to the Overarching Questions, `chapters/discussion.tex`, line 41

Suggestion: "supplied" becomes "provided"

Original:

~~~latex
Because the annotations were not supplied exclusively by non-experts, these results do not yet establish the same benefit when all demonstrations and annotations are supplied by non-experts.
~~~

Accepted wording:

~~~latex
Because the annotations were not provided exclusively by non-experts, these results do not yet establish the same benefit when all demonstrations and annotations are provided by non-experts.
~~~

Note written with the suggestion: Style reference, "Literal wording", which lists "supplied", and "Teachers and collection settings": use provide or give for teaching. The same change is proposed in DW-21 and DW-58.

Used in: [Teachers and collection settings](../hangs-writing-style-reference.md#teachers-and-collection-settings).

### DW-11

**Accepted with Hang's edit** · weight 4 · Wording (style reference) · 8.1 Answers to the Overarching Questions · Chapter 8 › Answers to the Overarching Questions, `chapters/discussion.tex`, line 42

Suggestion: "Its margin" names PHIRL

Original:

~~~latex
Its margin over the best baseline was larger on the mixed-quality datasets than on the high-quality datasets (in Lift, 17.1\% against 5.6\%), and larger in the longer-horizon PickPlaceCan task than in Lift.
~~~

Suggested:

~~~latex
PHIRL's margin over the best baseline was larger on the mixed-quality datasets than on the high-quality datasets (in Lift, 17.1\% compared with 5.6\%), and larger in the longer-horizon PickPlaceCan task than in Lift.
~~~

Hang's wording:

~~~latex
PHIRL's margin over the best baseline was larger on the mixed-quality datasets than on the high-quality datasets (in Lift, 17.1\% against 5.6\%), and larger in the longer-horizon PickPlaceCan task than in Lift.
~~~

Note written with the suggestion: Style reference, "Known information leading to new information": repeat a precise noun when a pronoun would be ambiguous. After the sentence about the annotations, "Its" could refer to the benefit. "against" becomes "compared with".

Used in: [Numbers and measured comparisons](../hangs-writing-style-reference.md#numbers-and-measured-comparisons), [Known information leading to new information](../hangs-writing-style-reference.md#known-information-leading-to-new-information).

### DW-12

**Accepted with Hang's edit** · weight 4 · Wording (style reference) · 8.1 Answers to the Overarching Questions · Chapter 8 › Answers to the Overarching Questions, `chapters/discussion.tex`, line 44

Suggestion: What demonstrations and progress each provide

Original:

~~~latex
Demonstrations supply dense information about how a task can be performed, and \textit{progress} supplies sparse information about which parts of a demonstration advance the task, which should matter more when more of the demonstrated behavior does not.
~~~

Suggested:

~~~latex
Demonstrations provide dense information about how a task can be performed, while \textit{progress} provides sparse information about which parts of a demonstration advance the task.
The information from \textit{progress} would be expected to matter more when a larger share of the demonstrated behavior does not advance the task.
~~~

Hang's wording:

~~~latex
Demonstrations provide dense information about how a task can be performed, while \textit{progress} provides sparse information about which parts of a demonstration advance the task.
The information from \textit{progress} would be expected to matter more when a larger portion of the demonstrated behaviors does not advance the task.
~~~

Note written with the suggestion: Style reference, "Information dimensions" ("[Signal A] provides [dimension A], while [signal B] provides [dimension B]") and "Hedges and degree words" (would for a conditional expectation). The ending "when more of the demonstrated behavior does not" left the verb to the reader; it is now a sentence of its own.

Used in: [Information dimensions](../hangs-writing-style-reference.md#information-dimensions), [Hedges and degree words](../hangs-writing-style-reference.md#hedges-and-degree-words), [Word choices made in review](../hangs-writing-style-reference.md#word-choices-made-in-review), [Complete clauses in place of elliptical endings](../hangs-writing-style-reference.md#complete-clauses-in-place-of-elliptical-endings).

### DW-13

**Accepted** · weight 1 · Wording (style reference) · 8.1 Answers to the Overarching Questions · Chapter 8 › Answers to the Overarching Questions, `chapters/discussion.tex`, line 46

Suggestion: "suggests a sense in which"

Original:

~~~latex
The design of PHIRL also suggests a sense in which imperfect teaching can be used and not only tolerated.
~~~

Accepted wording:

~~~latex
The design of PHIRL also illustrates how imperfect teaching can be used rather than only tolerated.
~~~

Note written with the suggestion: Style reference, "Direct subjects and concrete details". "illustrates how ... can" is the form you chose for qualitative evidence ("illustrates how progress alignment can discourage").

Used in: [Literal wording](../hangs-writing-style-reference.md#literal-wording), [A literal alternative](../hangs-writing-style-reference.md#a-literal-alternative).

### DW-14

**Accepted with Hang's edit** · weight 4 · Wording (style reference) · 8.2 Findings That Connect the Chapters · Chapter 8 › Findings That Connect the Chapters, `chapters/discussion.tex`, line 54

Suggestion: Name the three connections

Original:

~~~latex
This section describes these connections, which are not visible from any single study.
~~~

Suggested:

~~~latex
This section describes three such connections, which are not visible from any single study: differences between teachers in the magnitude of feedback, difficulties at similar kinds of task steps, and the use of approximate feedback values for learning.
~~~

Hang's wording:

~~~latex
This section describes the connections between chapters, which are not visible from any single study.
~~~

Note written with the suggestion: Style reference, "A roadmap with actual content": the roadmap should add information beyond the heading. The three connections are the three italic statements that follow.

Used in: [Few colons and semicolons](../hangs-writing-style-reference.md#few-colons-and-semicolons), [A roadmap with actual content](../hangs-writing-style-reference.md#a-roadmap-with-actual-content).

### DW-15

**Accepted** · weight 1 · Wording (style reference) · 8.2 Findings That Connect the Chapters · Chapter 8 › Findings That Connect the Chapters, `chapters/discussion.tex`, line 57

Suggestion: "point in the same direction"

Original:

~~~latex
Two studies with different participants, tasks, and scales point in the same direction.
~~~

Accepted wording:

~~~latex
The results of two studies with different participants, tasks, and scales are consistent with each other.
~~~

Note written with the suggestion: Style reference, "Literal wording", which names "point in the same direction" and gives "are consistent with" in its place.

Used in: [Literal wording](../hangs-writing-style-reference.md#literal-wording), [Discussion synthesis and its boundary](../hangs-writing-style-reference.md#discussion-synthesis-and-its-boundary).

### DW-16

**Accepted with Hang's edit** · weight 4 · Wording (style reference) · 8.2 Findings That Connect the Chapters · Chapter 8 › Findings That Connect the Chapters, `chapters/discussion.tex`, line 61

Suggestion: "account for a design choice"

Original:

~~~latex
They also account for a design choice that recurs in the later chapters, which is to compare a value given by a teacher only with other values from the same teacher.
~~~

Suggested:

~~~latex
They also help explain a design choice that recurs in the later chapters: comparing a value given by a teacher only with other values from the same teacher.
~~~

Hang's wording:

~~~latex
They also help explain a design choice that recurs in the later chapters, which is to compare a value given by a teacher only with other values from the same teacher.
~~~

Note written with the suggestion: Style reference, "Discussion synthesis and its boundary" ("This helps explain [design choice]") and "A colon that introduces the point". "account for" claims more than two studies on different scales can show.

Used in: [Few colons and semicolons](../hangs-writing-style-reference.md#few-colons-and-semicolons), [Discussion synthesis and its boundary](../hangs-writing-style-reference.md#discussion-synthesis-and-its-boundary).

### DW-17

**Accepted** · weight 1 · Wording (style reference) · 8.2 Findings That Connect the Chapters · Chapter 8 › Findings That Connect the Chapters, `chapters/discussion.tex`, line 67

Suggestion: "were lost at similar kinds of points"

Original:

~~~latex
Most of the failed demonstrations in the public space study were lost at similar kinds of points, when the jar was not grasped or was dropped while it was being carried (\autoref{ch:progress}).
~~~

Accepted wording:

~~~latex
Most of the failed demonstrations in the public space study failed at similar kinds of steps: the jar was not grasped, or it was dropped while it was being carried (\autoref{ch:progress}).
~~~

Note written with the suggestion: Style reference, "Literal wording" and "A colon that introduces the point". "lost" becomes "failed", and "points" becomes "steps", the word used in the heading of this paragraph.

Used in: [Literal wording](../hangs-writing-style-reference.md#literal-wording).

### DW-18

**Accepted with Hang's edit** · weight 4 · Wording (style reference) · 8.2 Findings That Connect the Chapters · Chapter 8 › Findings That Connect the Chapters, `chapters/discussion.tex`, line 69

Suggestion: "who is unsure" is not measured

Original:

~~~latex
A human demonstrator who is unsure at such a point pauses, aligns the gripper, or tests the grasp, and then continues; an agent that optimizes a reward may stay there if staying is rewarded.
~~~

Suggested:

~~~latex
At such a step, a human demonstrator may pause, align the gripper, or test the grasp before continuing, whereas an agent that optimizes a reward may stay there if staying is rewarded.
~~~

Hang's wording:

~~~latex
At such a step, a human demonstrator may pause, align the gripper, or test the grasp before continuing, whereas an agent that optimizes a reward may stay there since staying is rewarded.
~~~

Note written with the suggestion: Style reference, "Describing human teaching without blame": do not infer an unreported intention or state. The studies recorded pauses, alignments and tests of the grasp, not whether a demonstrator was unsure, so the behaviors are kept and "may" marks them as what a demonstrator can do at such a step.

Used in: [Describing human teaching without blame](../hangs-writing-style-reference.md#describing-human-teaching-without-blame), [Few colons and semicolons](../hangs-writing-style-reference.md#few-colons-and-semicolons), [A literal alternative](../hangs-writing-style-reference.md#a-literal-alternative), [Local reasons and governing conditions](../hangs-writing-style-reference.md#local-reasons-and-governing-conditions).

### DW-19

**Accepted with Hang's edit** · weight 4 · Wording (style reference) · 8.2 Findings That Connect the Chapters · Chapter 8 › Findings That Connect the Chapters, `chapters/discussion.tex`, line 71

Suggestion: Three jobs in one sentence

Original:

~~~latex
They suggest, however, that annotations may be most informative around changes of sub-task and precise contacts such as grasps, which are the steps that the magnitude term of PHIRL is designed to reward more than simply moving closer, and they support the selection of what to annotate that is proposed as future work below.
~~~

Suggested:

~~~latex
However, they suggest that annotations may be most informative around changes of sub-task and precise contacts such as grasps.
These are the steps that the magnitude term of PHIRL is designed to reward more than simply moving closer.
This possibility motivates the selection of demonstrations to annotate that is proposed as future work in this chapter.
~~~

Hang's wording:

~~~latex
However, they suggest that annotations may be most informative around changes of sub-task and precise contacts such as grasps, which are the steps that the magnitude term of PHIRL is designed to reward more than simply moving closer
This motivates the selection of demonstrations to annotate that is proposed as future work in this chapter.
~~~

To check: The first sentence of the edited wording has no period after moving closer. OA-805 added it, and Hang accepted.

Note written with the suggestion: Style reference, "One main job" and "Reporting findings and interpretations" ("These findings motivate [specific next step]"). The sentence gave the suggestion, the link to the magnitude term, and the link to future work. Observations that were not designed as a comparison can motivate the future work; "support" said more.

Used in: [Reporting findings and interpretations](../hangs-writing-style-reference.md#reporting-findings-and-interpretations), [One main job and varied sentence length](../hangs-writing-style-reference.md#one-main-job-and-varied-sentence-length), [Connectors with a clear job](../hangs-writing-style-reference.md#connectors-with-a-clear-job), [Known information leading to new information](../hangs-writing-style-reference.md#known-information-leading-to-new-information).

### DW-20

**Accepted with Hang's edit** · weight 4 · Wording (style reference) · 8.2 Findings That Connect the Chapters · Chapter 8 › Findings That Connect the Chapters, `chapters/discussion.tex`, line 77

Suggestion: A chapter cannot collect or find

Original:

~~~latex
\hang{tense start} \autoref{ch:progress} collected \textit{progress} on a segment of a trajectory rather than on a single state, and found that the resulting values carried information about task completion despite variation between teachers. \hang{tense end}
~~~

Suggested:

~~~latex
In \autoref{ch:progress}, \textit{progress} was collected on a segment of a trajectory rather than on a single state, and the resulting values carried information about task completion despite variation between teachers.
~~~

Hang's wording:

~~~latex
In \autoref{ch:progress}, \textit{progress} was collected on a segment of a trajectory rather than on a single state. The results show that \textit{progress} values carried information about task completion despite variation between teachers.
~~~

Note written with the suggestion: Style reference, "Impersonal dissertation voice": avoid giving collection and observations to something that cannot perform them. The chapter was the subject of "collected" and "found". The tense tags around this sentence are replaced by the style tags.

Used in: [Impersonal dissertation voice](../hangs-writing-style-reference.md#impersonal-dissertation-voice), [Reporting findings and interpretations](../hangs-writing-style-reference.md#reporting-findings-and-interpretations), [Known information leading to new information](../hangs-writing-style-reference.md#known-information-leading-to-new-information).

### DW-21

**Accepted** · weight 1 · Wording (style reference) · 8.2 Findings That Connect the Chapters · Chapter 8 › Findings That Connect the Chapters, `chapters/discussion.tex`, line 79

Suggestion: "supplied" becomes "provided"

Original:

~~~latex
Its evaluations, whose annotations were not supplied exclusively by non-experts, show that learning can improve when the annotations are used in this way.
~~~

Accepted wording:

~~~latex
Its evaluations, whose annotations were not provided exclusively by non-experts, show that learning can improve when the annotations are used in this way.
~~~

Note written with the suggestion: Same change as DW-10.

### DW-22

**Accepted with Hang's edit** · weight 4 · Wording (style reference) · 8.2 Findings That Connect the Chapters · Chapter 8 › Findings That Connect the Chapters, `chapters/discussion.tex`, line 81

Suggestion: Spell out VLM

Original:

~~~latex
The formative VLM study in \autoref{ch:phirl} is consistent with this interpretation: generated annotations improved learning in most cases, although less than human annotations did.
~~~

Suggested:

~~~latex
The formative study with a vision-language model (VLM) in \autoref{ch:phirl} is consistent with this interpretation: annotations generated by the VLM improved learning in most cases, although less than human annotations did.
~~~

Hang's wording:

~~~latex
The formative study with a vision-language model (VLM) in \autoref{ch:phirl} is consistent with this interpretation: annotations generated by the VLM improved learning in most cases, while the improvement is less than using human annotations.
~~~

Note written with the suggestion: Style reference, "Definitions before notation": define a term where it is first needed. This is the only use of "VLM" in the chapter, and it was last defined in Chapter 7.

Used in: [Concession with while](../hangs-writing-style-reference.md#concession-with-while), [Definitions before notation](../hangs-writing-style-reference.md#definitions-before-notation), [Complete clauses in place of elliptical endings](../hangs-writing-style-reference.md#complete-clauses-in-place-of-elliptical-endings).

### DW-23

**Accepted with Hang's edit** · weight 4 · Wording (style reference) · 8.3 What the Combined Evidence Does Not Yet Show · Chapter 8 › What the Combined Evidence Does Not Yet Show, `chapters/discussion.tex`, line 90

Suggestion: "link by link"

Original:

~~~latex
First, the argument was tested link by link and not end to end.
~~~

Suggested:

~~~latex
First, the stages of the argument were evaluated separately and not end to end.
~~~

Hang's wording:

~~~latex
First, the stages of the argument were evaluated separately, not end to end.
~~~

Note written with the suggestion: Style reference, "Literal wording", which names "link by link" and gives "[Components] were evaluated separately" in its place.

Used in: [Literal wording](../hangs-writing-style-reference.md#literal-wording), [A literal alternative](../hangs-writing-style-reference.md#a-literal-alternative).

### DW-24

**Accepted** · weight 1 · Wording (style reference) · 8.3 What the Combined Evidence Does Not Yet Show · Chapter 8 › What the Combined Evidence Does Not Yet Show, `chapters/discussion.tex`, line 93

Suggestion: A sentence that opens with "That"

Original:

~~~latex
That \textit{progress} alignment discounts sidetracks is therefore an inference from the design of the method and from its larger advantage on mixed-quality data, and not a measured result.
~~~

Accepted wording:

~~~latex
The expectation that \textit{progress} alignment discounts sidetracks is therefore an inference from the design of the method and from its larger advantage on mixed-quality data, and not a measured result.
~~~

Note written with the suggestion: Style reference, "Direct subjects and concrete details". The sentence now opens with its subject. The meaning is the same.

Used in: [Direct subjects and concrete details](../hangs-writing-style-reference.md#direct-subjects-and-concrete-details).

### DW-25

**Declined** · weight 3 · Spelling and grammar · 8.4 Future Work: lead-in · Chapter 8 › Future Work, `chapters/discussion.tex`, line 102

Suggestion: The two groups of future work

Original, which stayed:

~~~latex
This section introduces future work in two aspects.
\hang{grammar start} One is future work that addresses the limitations of the charpters in this dissertation or extentions to the work in this dissertation. \hang{grammar end}
~~~

Declined suggestion:

~~~latex
This section describes future work in two groups.
One group addresses the limitations of the studies in this dissertation or extends them.
~~~

To check: The spelling corrections in this suggestion (charpters, extentions) were declined with it. OA-806 offered them alone, and Hang accepted.

Note written with the suggestion: Spelling ("charpters", "extentions") and grammar: "addresses the limitations ... or extentions" joined a verb phrase with a noun. "in two aspects" becomes "in two groups", since what follows is two groups of directions. The grammar tags around the second sentence are kept, now around both sentences.

Used in: [Procedural series and enumerations](../hangs-writing-style-reference.md#procedural-series-and-enumerations), [Correcting a sentence without rewording it](../hangs-writing-style-reference.md#correcting-a-sentence-without-rewording-it).

### DW-26

**Declined** · weight 3 · Wording (style reference) · 8.4 Future Work: lead-in · Chapter 8 › Future Work, `chapters/discussion.tex`, line 104

Suggestion: The list of directions

Original, which stayed:

~~~latex
\hang{grammar start} This direction follows directly from the findings of this dissertation: actively selecting which demonstrations to annotate, extending the learning framework to enable learning from teaching modalities beyond human evaluative feedback and human demonstrations, examining the conclusions on a larger scale,  and extending the framework to be compatible with foundation models. \hang{grammar end}
~~~

Declined suggestion:

~~~latex
Its directions follow directly from the findings of this dissertation: actively selecting which demonstrations to annotate, extending the learning framework to teaching modalities beyond evaluative feedback and demonstrations, examining the conclusions at a larger scale, and extending the framework to foundation models.
~~~

Note written with the suggestion: "This direction" introduced four directions. Shortened: "to enable learning from teaching modalities beyond human evaluative feedback and human demonstrations" and "to be compatible with". Decide this one together with DW-43 and DW-44: the list names "examining the conclusions on a larger scale", which has no subsection, and foundation models, whose subsection is empty. If you reject those two drafts and do not plan to write the subsections, use "Edit the wording" here to take the two directions out of the list.

Used in: [Correcting a sentence without rewording it](../hangs-writing-style-reference.md#correcting-a-sentence-without-rewording-it).

### DW-27

**Declined** · weight 3 · Wording (style reference) · 8.4 Future Work: lead-in · Chapter 8 › Future Work, `chapters/discussion.tex`, line 105

Suggestion: The second group

Original, which stayed:

~~~latex
The other one is future work that builds on the work in this dissertation but goes beyond a simple continuation.
~~~

Declined suggestion:

~~~latex
The other group builds on the work in this dissertation but goes beyond a direct continuation of it.
~~~

Note written with the suggestion: Matches DW-25 ("One group ... The other group"), and reads correctly whether or not DW-25 is accepted. "a simple continuation" becomes "a direct continuation of it".

Used in: [Procedural series and enumerations](../hangs-writing-style-reference.md#procedural-series-and-enumerations).

### DW-28

**Accepted** · weight 1 · Spelling and grammar · 8.4 Future Work: lead-in · Chapter 8 › Future Work, `chapters/discussion.tex`, line 107

Suggestion: "has the capbility of performing"

Original:

~~~latex
Two directions arise for further empowering non-expert users when the robot has the capbility of performing certain tasks.
~~~

Accepted wording:

~~~latex
Two directions arise for further empowering non-expert users once a robot is already capable of performing certain tasks.
~~~

Note written with the suggestion: Spelling ("capbility"). "when the robot has the capability of performing" becomes "once a robot is already capable of performing".

Used in: [Word choices made in review](../hangs-writing-style-reference.md#word-choices-made-in-review).

### DW-29

**Declined** · weight 3 · Spelling and grammar · 8.4 Future Work: lead-in · Chapter 8 › Future Work, `chapters/discussion.tex`, line 108

Suggestion: What the dissertation studied and what a robot also needs

Original, which stayed:

~~~latex
\hang{grammar start} This dissertation studied scenairos  in which robots need to learn a manipulation skill from the users, while robots also need to learn to perform a complex task by planing with learned skills and learn to interact properly with users when they already know how to perform the tasks. \hang{grammar end}
~~~

Declined suggestion:

~~~latex
This dissertation studied scenarios in which a robot needs to learn a manipulation skill from its users.
A robot also needs to learn to perform a complex task by planning with the skills it has learned, and to interact appropriately with users when it already knows how to perform a task.
~~~

To check: The spelling corrections in this suggestion (scenairos, planing) were declined with it. OA-808 offered them alone, and Hang accepted.

Note written with the suggestion: Spelling ("scenairos", "planing"). Style reference, "One main job": what was studied and what remains are now two sentences. "they already know how to perform the tasks" could refer to the users; it is now "it already knows how to perform a task".

Used in: [One main job and varied sentence length](../hangs-writing-style-reference.md#one-main-job-and-varied-sentence-length), [Concession with while](../hangs-writing-style-reference.md#concession-with-while).

### DW-30

**Accepted with Hang's edit** · weight 4 · Wording (style reference) · 8.4 Future Work: lead-in · Chapter 8 › Future Work, `chapters/discussion.tex`, line 109

Suggestion: Introducing agentic robotics and agentic HRI

Original:

~~~latex
\hang{grammar start} These are approached by taking advantage of agentic AI, and are formalized as Agentic Robotics and Agentic HRI. \hang{grammar end}
~~~

Suggested:

~~~latex
Both needs can be approached with agentic AI, and they are described in this section as agentic robotics and agentic human-robot interaction (HRI).
Agentic robotics provides a direction for organizing task execution and policy improvement, and agentic HRI extends this direction to decisions about how to work with and learn from people.
~~~

Hang's wording:

~~~latex
Both needs can be approached by taking advantages of agentic AI, and they are described in this section as agentic robotics and agentic human-robot interaction (HRI).
Agentic robotics provides a direction for organizing task execution and policy improvement, and agentic HRI extends this direction to decisions about how to work with and learn from people.
~~~

To check: The idiom is taking advantage of. The edited wording has taking advantages of. OA-809 corrected it, and Hang accepted.

Note written with the suggestion: Style reference, "Research actions": "formalized" promises a formal definition, which the subsections do not give, so the two directions are "described". HRI is spelled out at its first use in the chapter. The second sentence is your own wording from your edit of the earlier future-work review ("provides a direction for organizing task execution and policy improvement", "extends this direction to decisions about how to work with and learn from people"). Delete it on the page if you no longer want it.

Used in: [Research actions](../hangs-writing-style-reference.md#research-actions), [Means expressed with by](../hangs-writing-style-reference.md#means-expressed-with-by), [Definitions before notation](../hangs-writing-style-reference.md#definitions-before-notation).

### DW-31

**Accepted with Hang's edit** · weight 4 · Wording (style reference) · 8.4 Future Work: selecting annotations · Chapter 8 › Future Work › Actively Sample Annotations, `chapters/discussion.tex`, line 112

Suggestion: Subsection heading

Original:

~~~latex
\subsection*{Actively Sample Annotations}
~~~

Suggested:

~~~latex
\subsection*{Actively Selecting Demonstrations to Annotate} % [HY style] renamed from ``Actively Sample Annotations''
~~~

Hang's wording:

~~~latex
\subsection*{Actively Sampling Demonstrations to Annotate} % [HY style] renamed from ``Actively Sample Annotations''
~~~

Note written with the suggestion: Style reference, "Headings that name the question or finding". The other subsection headings are noun phrases, and the lead-in calls this direction "actively selecting which demonstrations to annotate". A heading gets a comment, not tags, as elsewhere in the chapters.

Used in: [Headings that name the question or finding](../hangs-writing-style-reference.md#headings-that-name-the-question-or-finding).

### DW-32

**Accepted with Hang's edit** · weight 4 · Spelling and grammar · 8.4 Future Work: selecting annotations · Chapter 8 › Future Work › Actively Sample Annotations, `chapters/discussion.tex`, line 115

Suggestion: The selection strategy and its starting assumption

Original:

~~~latex
\hang{grammar start} Future work should extend PHIRL with a selection strategy, while assuming that failed demonstrations are necessarily to be annotated since they are most likely to be informative: low-quality demonstrations can inform completion shaping, negative reward samples, and better data coverage. \hang{grammar end}
~~~

Suggested:

~~~latex
Future work could extend PHIRL with a selection strategy.
One starting assumption is that failed demonstrations are always annotated, since they may be the most informative: low-quality demonstrations can inform completion shaping, provide negative reward samples, and improve data coverage.
~~~

Hang's wording:

~~~latex
Future work could extend PHIRL with a selection strategy.
One starting assumption is that failed demonstrations should be prioritized for annotations, since low-quality demonstrations can inform completion shaping, provide negative reward samples, and improve data coverage.
~~~

Note written with the suggestion: Grammar: "are necessarily to be annotated", and a list that mixed a verb's object with two nouns ("inform completion shaping, negative reward samples, and better data coverage"). Style reference, "Limitations and future work" ("Future work could ...") and "Hedges and degree words": that failed demonstrations are the most informative has not been tested, and Section 8.1 says the evidence for the completion term is limited, so "most likely" becomes "may be".

Used in: [Limitations and future work](../hangs-writing-style-reference.md#limitations-and-future-work), [Few colons and semicolons](../hangs-writing-style-reference.md#few-colons-and-semicolons), [Matched factors and endpoints](../hangs-writing-style-reference.md#matched-factors-and-endpoints), [Local reasons and governing conditions](../hangs-writing-style-reference.md#local-reasons-and-governing-conditions), [Word choices made in review](../hangs-writing-style-reference.md#word-choices-made-in-review).

### DW-33

**Accepted with Hang's edit** · weight 4 · Spelling and grammar · 8.4 Future Work: selecting annotations · Chapter 8 › Future Work › Actively Sample Annotations, `chapters/discussion.tex`, line 116

Suggestion: The baseline strategies

Original:

~~~latex
\hang{grammar start}
While developing a new selection strategy,
a few baseline selection strategies should be included: random selection, as in \autoref{ch:phirl}; preference for low-quality demonstrations, preference for demonstrations  on which the learned reward model is most uncertain, preference for demonstrations where the learned reward disagrees most with the current estimate of \textit{progress}, and preference for optimal demonstrations.
\hang{grammar end}
~~~

Suggested:

~~~latex
A new selection strategy would be compared with several baseline strategies: random selection, as in \autoref{ch:phirl}; selecting low-quality demonstrations; selecting the demonstrations on which the learned reward model is most uncertain; selecting the demonstrations where the learned reward disagrees most with the current estimate of \textit{progress}; and selecting the highest-quality demonstrations.
~~~

Hang's wording:

~~~latex
The new selection strategy would be compared with several baseline strategies: random selection, as in \autoref{ch:phirl}; selecting low-quality demonstrations; selecting the demonstrations on which the learned reward model is most uncertain; selecting the demonstrations where the learned reward disagrees most with the current estimate of \textit{progress}; and selecting the highest-quality demonstrations.
~~~

Note written with the suggestion: Punctuation: the list mixed a semicolon with commas, and one item contains a comma, so every item now ends with a semicolon. Style reference, "Procedural series and enumerations": each strategy starts with "selecting". "optimal demonstrations" becomes "the highest-quality demonstrations", because the chapters describe the datasets by quality and no demonstration is shown to be optimal. Change it back on the page if "optimal" is what you mean.

Used in: [Few colons and semicolons](../hangs-writing-style-reference.md#few-colons-and-semicolons), [Known information leading to new information](../hangs-writing-style-reference.md#known-information-leading-to-new-information), [Procedural series and enumerations](../hangs-writing-style-reference.md#procedural-series-and-enumerations).

### DW-34

**Accepted with Hang's edit** · weight 4 · Wording (style reference) · 8.4 Future Work: selecting annotations · Chapter 8 › Future Work › Actively Sample Annotations, `chapters/discussion.tex`, line 121

Suggestion: The budget of human time

Original:

~~~latex
These strategies should be compared under an equal budget of human time rather than an equal number of labels, since annotating a long demonstration or an ambiguous segment takes more time than annotating a short, clear one, and any human effort needed to identify candidates, such as judging which demonstrations are of low quality, should count toward that budget.
~~~

Suggested:

~~~latex
These strategies would be compared under an equal budget of human time rather than an equal number of labels, since annotating a long demonstration or an ambiguous segment takes more time than annotating a short, clear one.
Any human effort needed to identify candidates, such as judging which demonstrations are of low quality, would count toward that budget.
~~~

Hang's wording:

~~~latex
These strategies would be compared under an equal budget of human time rather than an equal number of labels, since annotating a long demonstration or an ambiguous segment takes more time than annotating a short and clear one.
Any human effort needed to identify candidates, such as judging which demonstrations are of low quality, would also count toward that budget.
~~~

Note written with the suggestion: Style reference, "One main job": the rule for the comparison and what counts toward the budget are now two sentences. "should" becomes "would", to match DW-32 and DW-33.

Used in: [Limitations and future work](../hangs-writing-style-reference.md#limitations-and-future-work), [One main job and varied sentence length](../hangs-writing-style-reference.md#one-main-job-and-varied-sentence-length), [Connectors with a clear job](../hangs-writing-style-reference.md#connectors-with-a-clear-job), [Local reasons and governing conditions](../hangs-writing-style-reference.md#local-reasons-and-governing-conditions), [Word choices made in review](../hangs-writing-style-reference.md#word-choices-made-in-review).

### DW-35

**Declined** · weight 3 · Spelling and grammar · 8.4 Future Work: selecting annotations · Chapter 8 › Future Work › Actively Sample Annotations, `chapters/discussion.tex`, line 122

Suggestion: "including ... into the dataset can be beneficial"

Original, which stayed:

~~~latex
In addition, including more low quality demonstrations into the dataset can be beneficial.
~~~

Declined suggestion:

~~~latex
In addition, adding more low-quality demonstrations to the dataset may benefit learning.
~~~

To check: The grammar corrections in this suggestion (low-quality before a noun, adding to in place of including into) were declined with it.

Note written with the suggestion: Grammar ("including into", "low quality" before a noun). Style reference, "Hedges and degree words": no result in the dissertation shows this benefit, so "can be beneficial" becomes "may benefit learning".

Used in: [Hedges and degree words](../hangs-writing-style-reference.md#hedges-and-degree-words).

### DW-36

**Accepted with Hang's edit** · weight 4 · Wording (style reference) · 8.4 Future Work: selecting annotations · Chapter 8 › Future Work › Actively Sample Annotations, `chapters/discussion.tex`, line 123

Suggestion: The result, then what it suggests

Original:

~~~latex
Current results indicate that PHIRL's gains from additional annotations saturated at around 50\% coverage in most conditions, particularly when demonstrations were of relatively high quality (\autoref{ch:phirl}), which suggests that annotations differ in how informative they are.
~~~

Suggested:

~~~latex
PHIRL's gains from additional annotations saturated at around 50\% coverage in most conditions, particularly when demonstrations were of relatively high quality (\autoref{ch:phirl}).
This suggests that annotations differ in how informative they are.
~~~

Hang's wording:

~~~latex
Results indicate that PHIRL's gains from additional annotations saturated at around 50\% coverage in most conditions, particularly when demonstrations were of relatively high quality (\autoref{ch:phirl}), which suggests that annotations differ in how informative they are.
~~~

Note written with the suggestion: Style reference, "Observation interpretation and explanation": report the observation directly, then the interpretation with "This suggests that". "Current results indicate that" is dropped because the saturation is a reported result of Chapter 7.

Used in: [Reporting findings and interpretations](../hangs-writing-style-reference.md#reporting-findings-and-interpretations), [Observation interpretation and explanation](../hangs-writing-style-reference.md#observation-interpretation-and-explanation), [One main job and varied sentence length](../hangs-writing-style-reference.md#one-main-job-and-varied-sentence-length).

### DW-37

**Accepted with Hang's edit** · weight 4 · Spelling and grammar · 8.4 Future Work: selecting annotations · Chapter 8 › Future Work › Actively Sample Annotations, `chapters/discussion.tex`, line 124

Suggestion: What the comparison would test

Original:

~~~latex
Such a comparison would test whether PHIRL can obtain equivalent performance with less annotation effort, which kinds of demonstrations are most informative to annotate at different points in learning, and if the model would always benefit from more annotated low quality demonstrations.
~~~

Suggested:

~~~latex
Such a comparison would test whether PHIRL can reach similar performance with less annotation effort, which kinds of demonstrations are most informative to annotate at different points in learning, and whether the model continues to benefit from more annotated low-quality demonstrations.
~~~

Hang's wording:

~~~latex
Such a comparison would test whether PHIRL can reach similar performance with less annotation effort, which kinds of demonstrations are most informative to annotate at different points in learning, and whether the model would always benefit from more annotated low-quality demonstrations.
~~~

Note written with the suggestion: Grammar: "and if" becomes "and whether" to match the other two questions; "low quality" is hyphenated. Style reference, "Reporting a difference that was not detected": "equivalent performance" would need an equivalence test, so it becomes "similar performance".

Used in: [Reporting a difference that was not detected](../hangs-writing-style-reference.md#reporting-a-difference-that-was-not-detected), [Matched factors and endpoints](../hangs-writing-style-reference.md#matched-factors-and-endpoints), [Correcting a sentence without rewording it](../hangs-writing-style-reference.md#correcting-a-sentence-without-rewording-it).

### DW-38

**Declined** · weight 3 · Wording (style reference) · 8.4 Future Work: more modalities · Chapter 8 › Future Work › Learning from More Modalities of Human Teaching, `chapters/discussion.tex`, line 129

Suggestion: "When humans teach humans, people teach"

Original, which stayed:

~~~latex
When humans teach humans, people teach through many more channels and modalities, including natural language instructions and explanations \cite{goyal2019using}, physical corrections \cite{bajcsy2018learning}, gaze \cite{saran2020understanding}, gestures \cite{yanik2013gesture}, facial expressions and other implicit reactions \cite{cui2021empathic}, and comparisons between trajectories \cite{brown2019ranking, biyik2022learning}.
~~~

Declined suggestion:

~~~latex
People can teach through many more channels and modalities, including natural language instructions and explanations \cite{goyal2019using}, physical corrections \cite{bajcsy2018learning}, gaze \cite{saran2020understanding}, gestures \cite{yanik2013gesture}, facial expressions and other implicit reactions \cite{cui2021empathic}, and comparisons between trajectories \cite{brown2019ranking, biyik2022learning}.
~~~

Note written with the suggestion: The sentence named its subject twice. The cited papers are about people teaching robots, and comparisons between trajectories are not a way people teach one another, so the opening clause is dropped. Reject this if the contrast with teaching between people is the point you want to make.

Used in: [Correcting a sentence without rewording it](../hangs-writing-style-reference.md#correcting-a-sentence-without-rewording-it).

### DW-39

**Accepted** · weight 1 · Spelling and grammar · 8.4 Future Work: more modalities · Chapter 8 › Future Work › Learning from More Modalities of Human Teaching, `chapters/discussion.tex`, line 131

Suggestion: "complimentary", "intergrating"

Original:

~~~latex
\hang{grammar start} Results from PHIRL (\autoref{ch:phirl}) suggest that teaching modalities can be complimentary and strategically intergrating more teaching modalities can improve learning outcomes while possibly reducing human effort. \hang{grammar end}
~~~

Accepted wording:

~~~latex
The results of PHIRL (\autoref{ch:phirl}) suggest that teaching modalities can be complementary, and that strategically integrating more teaching modalities may improve learning outcomes while possibly reducing human effort.
~~~

Note written with the suggestion: Spelling: "complimentary" (praising) becomes "complementary", and "intergrating" becomes "integrating". A second "that" separates the two things the results suggest. Style reference, "Hedges and degree words": PHIRL combined two modalities, so the benefit of more is a possibility ("may").

Used in: [Hedges and degree words](../hangs-writing-style-reference.md#hedges-and-degree-words).

### DW-40

**Accepted** · weight 1 · Wording (style reference) · 8.4 Future Work: more modalities · Chapter 8 › Future Work › Learning from More Modalities of Human Teaching, `chapters/discussion.tex`, line 133

Suggestion: "in the same way" as what

Original:

~~~latex
Other modalities can be expressed as constraints in the same way: comparisons constrain the ordering of trajectories, natural language instructions and rubrics \cite{gunjal2025rubrics, liu2025openrubrics} constrain which features of the task matter, and gaze indicates which objects a teacher attends to \cite{saran2020understanding}.
~~~

Accepted wording:

~~~latex
Other modalities could be expressed as constraints on the learned reward, in the way that PHIRL uses \textit{progress}: comparisons constrain the ordering of trajectories, natural language instructions and rubrics \cite{gunjal2025rubrics, liu2025openrubrics} constrain which features of the task matter, and gaze indicates which objects a teacher attends to \cite{saran2020understanding}.
~~~

Note written with the suggestion: Style reference, "Known information leading to new information". Nothing in this subsection has mentioned constraints, so "in the same way" has nothing to refer to. The revision names it: the way PHIRL uses progress to constrain the learned reward (Section 8.1).

Used in: [Known information leading to new information](../hangs-writing-style-reference.md#known-information-leading-to-new-information).

### DW-41

**Declined** · weight 3 · Spelling and grammar · 8.4 Future Work: more modalities · Chapter 8 › Future Work › Learning from More Modalities of Human Teaching, `chapters/discussion.tex`, line 136

Suggestion: "extending new modalities"

Original, which stayed:

~~~latex
\hang{grammar start} Thus, future work can consider extending new modalities while using an approach similar to that of this dissertation: first model how non-experts actually provide a modality and then design learning methods around the resulting models rather than around idealized assumptions. \hang{grammar end}
~~~

Declined suggestion:

~~~latex
Thus, future work could extend the framework to new modalities with the approach of this dissertation: first model how non-experts actually provide a modality, and then design learning methods around the resulting models rather than around idealized assumptions.
~~~

Note written with the suggestion: Grammar: a modality is not extended; the framework is extended to it. "can consider extending ... while using an approach similar to that of" becomes "could extend ... with the approach of".

Used in: [Limitations and future work](../hangs-writing-style-reference.md#limitations-and-future-work).

### DW-42

**Declined** · weight 3 · Spelling and grammar · 8.4 Future Work: more modalities · Chapter 8 › Future Work › Learning from More Modalities of Human Teaching, `chapters/discussion.tex`, line 138

Suggestion: "at one time"

Original, which stayed:

~~~latex
\hang{grammar start} Collecting multiple teaching modalities at one time from the same non-expert teachers would make it possible to study how modalities relate to and complement one another, for instance, whether pauses in a demonstration coincide with shifts in gaze or with implicit evaluations. \hang{grammar end}
~~~

Declined suggestion:

~~~latex
Collecting several teaching modalities at the same time from the same non-expert teachers would make it possible to study how the modalities relate to and complement one another: for instance, whether pauses in a demonstration coincide with shifts in gaze or with implicit evaluations.
~~~

Note written with the suggestion: Grammar: "at one time" reads as "once, in the past"; "at the same time" is meant. A colon introduces the example (style reference, "A colon that introduces the point").

Used in: [Few colons and semicolons](../hangs-writing-style-reference.md#few-colons-and-semicolons).

### DW-43

**Declined** · weight 3 · New text · 8.4 Future Work: two directions with no text yet · Chapter 8 › Future Work › Non-Expert Teaching for Foundation Models, `chapters/discussion.tex`, line 141

Suggestion: Optional draft: a subsection for "examining the conclusions at a larger scale"

New text, placed next to this passage:

~~~latex
\subsection*{Non-Expert Teaching for Foundation Models}
~~~

Declined suggestion:

~~~latex
\subsection*{Evaluating the Findings End to End and at a Larger Scale} % [HY created]

\hang{create start}
Each gap identified in \autoref{sec:discussion-boundaries} corresponds to a study that could be conducted.
First, an end-to-end evaluation could have the same non-experts provide demonstrations and \textit{progress} annotations, and then train a robot on both.
Such a study would test whether the benefit of PHIRL holds when all of the teaching comes from non-experts, and whether \textit{progress} alignment discounts the sidetracks characterized in \autoref{ch:sidetracks}.
Second, the characteristics of the teacher that were associated with feedback in \autoref{ch:charm} could be used by the later methods, for instance to weight the annotations of each teacher.
Third, having teachers annotate the same behavior twice would test whether \textit{progress} is consistent within a teacher, as was tested for binary and scalar feedback in \autoref{ch:steady}.
Finally, each study covered a limited number of tasks, interfaces, and participants.
Repeating the studies with more tasks and participants, and with several training runs per condition, would show how far the findings extend beyond the studied settings.
\hang{create end}
~~~

Note written with the suggestion: Optional. The lead-in lists this direction, but the section has no subsection for it. This draft uses only what Sections 8.1 and 8.3 of this chapter already say: the three gaps, and the limits on tasks, interfaces, populations and training runs. It adds no result and no citation. It is placed before the foundation-model subsection, which is the order of the list in the lead-in. The heading carries a comment and the paragraph carries the create tags.

Used in: [Future work drafted from notes](../hangs-writing-style-reference.md#future-work-drafted-from-notes), [Adding sentences that were not asked for](../hangs-writing-style-reference.md#adding-sentences-that-were-not-asked-for).

### DW-44

**Accepted** · weight 1 · New text · 8.4 Future Work: two directions with no text yet · Chapter 8 › Future Work › Agentic Robotics, `chapters/discussion.tex`, line 146

Suggestion: Optional draft: text for "Non-Expert Teaching for Foundation Models"

New text, placed next to this passage:

~~~latex
\subsection*{Agentic Robotics}
~~~

Accepted wording:

~~~latex
The methods in this dissertation were evaluated with reward functions and policies that were trained for one task at a time.
Foundation models for robotics, such as vision-language-action (VLA) models \cite{wu2026pragmatic, wang2026qwen}, are also trained on human demonstrations, so the imperfections studied in this dissertation remain relevant to them.
For instance, removing the frames in which a demonstrator pauses can improve the performance of these models, and \textit{Pause} is one of the four types of demonstration sidetracks characterized in \autoref{ch:sidetracks}.
Future work could examine whether the other types of sidetracks affect these models as well, and whether \textit{progress} annotations can indicate which parts of a demonstration such a model should learn from.
Foundation models could also take part in the teaching.
In the formative study of \autoref{ch:phirl}, \textit{progress} annotations generated by a vision-language model improved learning in most cases, although less than human annotations did.
One direction is therefore to combine the two sources, with a model annotating most of the demonstrations and non-experts annotating the ones on which the model is least reliable.
~~~

Note written with the suggestion: Optional. The subsection has a heading and no text. This draft goes beyond the two agentic folders: it uses only statements already in the dissertation. The pause-frame result for VLA models and its two citations are from your Introduction; Pause as one of the four sidetrack types is from Chapter 4; the vision-language model result is from the formative study in Chapter 7. The two directions it proposes (do other sidetracks affect these models, and a model annotating with non-experts covering the cases where it is least reliable) are my suggestions, not results. It is inserted just above the Agentic Robotics heading, which puts it under the empty heading.

### DW-45

**Accepted** · weight 1 · New text · 8.4 Future Work: Agentic Robotics · Chapter 8 › Future Work › Agentic Robotics, `chapters/discussion.tex`, line 148

Suggestion: From code as policies to agentic robotics (your first three notes)

Original:

~~~latex
The robots in this dissertation learned a single skill at a time from human teaching.

code as policy -> agentic robotics.


learned skills + training model -> perform task.
~~~

Accepted wording:

~~~latex
The robots in this dissertation learned a single skill at a time from human teaching.
Prior work on code as policies showed that a language model can write programs that process perception outputs and call control primitives to form a robot policy \cite{liang2022codeaspolicies}.
Agentic robotics takes this idea from a single program to a loop, in which an agent plans, calls tools, observes the outcomes, and revises its plan.
A tool in this sense is anything that acts on the robot or on its data: a trained policy, a training pipeline, an evaluator, or a setup for collecting demonstrations.
A skill that was learned from human teaching would thus become a tool that an agent calls, together with other tools, to perform a longer task.
~~~

Note written with the suggestion: Replaces the scope sentence and the notes "code as policy -> agentic robotics" and "learned skills + training model -> perform task". The scope sentence is kept as it is. Code as Policies is cited with a new key (DW-61). The description of a tool is from the preprint, Section 1 commitment (ii) and Section 3.2 "Toolify every execution": a trained policy, a training pipeline, an evaluator and a data-collection rig are each a tool. The preprint uses "skill" for a written procedure and "tool" for a trained policy; this paragraph keeps "skill" for what the robot learned, as the rest of the dissertation does, and says that such a skill becomes a tool. I read "training model" as the training pipeline; correct the last sentence if you meant a trained model.

### DW-46

**Accepted** · weight 1 · New text · 8.4 Future Work: Agentic Robotics · Chapter 8 › Future Work › Agentic Robotics, `chapters/discussion.tex`, line 155

Suggestion: The loop that improves a policy, and where a person stays in it (note 4)

Original:

~~~latex
Loop engineering -> self evolve -> human in the loop feedback or validation or twist.
~~~

Accepted wording:

~~~latex
The same loop could also be used to improve the tools themselves.
Improving a robot policy currently relies on a person to interpret failures, choose what to try next, manage long training jobs, and compare noisy evaluations.
In the planned design, a language-model controller would manage this work in rounds and delegate analysis and execution to short-lived worker agents.
In each round, the controller would analyze the recorded results, choose an action such as collecting more data or retraining a policy, measure the outcome itself, and keep the new policy only when the gain exceeds a margin set by the uncertainty of the evaluation.
With the loop engineered in this way, the system could improve its own tools and procedures from one round to the next.
A person would remain in the loop at chosen points: giving feedback on an outcome, validating a change before it is kept, or adjusting a procedure that the agent follows.
~~~

Note written with the suggestion: Replaces "Loop engineering -> self evolve -> human in the loop feedback or validation or twist". Facts from the preprint: what the outer loop relies on a person for today (Section 1, first paragraph); a controller that manages the loop while disposable workers analyze and execute (Section 1, commitment i); the round Bind, Analyze, Act, Measure, Score, Commit with measurement owned by the controller (Section 3.4); promotion only when the gain exceeds 1.5 times the interval half-width (Section 3.5), written here as "a margin set by the uncertainty of the evaluation"; skills that are promoted or deprecated on recorded evidence (Section 3.2); human approval points (Section 6, Safety). Written as planned work ("In the planned design ... would"), with no result reported. I read "twist" as "tweak" and wrote "adjusting a procedure that the agent follows"; the preprint keeps the objective fixed during a run, so the adjustment is to a procedure and not to the objective.

### DW-47

**Accepted with Hang's edit** · weight 4 · New text · 8.4 Future Work: Agentic Robotics · Chapter 8 › Future Work › Agentic Robotics, `chapters/discussion.tex`, line 157

Suggestion: Non-expert teaching moves to a higher level (note 5)

Original:

~~~latex
in agebtic robotics, non-expert teaching does not disappear; it moves to a higher level, as people correct plans, evaluate outcomes, and demonstrate the steps that an agent gets wrong. \hang{grammar start} Human teaching provides a trajectory. \hang{grammar end} ( execution trajectory level trajectory)
~~~

Suggested:

~~~latex
In agentic robotics, non-expert teaching does not disappear; it moves to a higher level, as people correct plans, evaluate outcomes, and demonstrate the steps that an agent gets wrong.
Human teaching would then provide a trajectory at a different level: not only the motion of the robot, but also the execution trajectory of the agent, that is, the sequence of plans, tool calls, outcomes, and human corrections recorded while a task is carried out.
The questions of this dissertation would apply at this level as well: whether the imperfections in such teaching contain systematic structure, and which signals non-experts can give consistently.
~~~

Hang's wording:

~~~latex
In agentic robotics, non-expert teaching does not disappear; it moves to a higher level, as people correct plans, evaluate outcomes, and demonstrate the steps that an agent gets wrong.
Human teaching would then provide a trajectory at a different level: not only the motion of the robot, but also the execution trajectory of the agent, that is, the sequence of plans, tool calls, outcomes, and human corrections recorded while a task is carried out.
~~~

Note written with the suggestion: Your first sentence is kept, with "agebtic" corrected and a capital letter. "Human teaching provides a trajectory. (execution trajectory level trajectory)" is written out as I understood it: teaching would be given on, and recorded as part of, the execution trajectory of the agent (its plans, tool calls, outcomes and the corrections it received), and not only on the motion of the robot. Please check that this is what the note means. The last sentence, which asks two of the dissertation's questions again at this level, is my addition; delete it on the page if it goes too far.

Used in: [Future work drafted from notes](../hangs-writing-style-reference.md#future-work-drafted-from-notes).

### DW-48

**Accepted** · weight 1 · New text · 8.4 Future Work: Agentic Robotics · Chapter 8 › Future Work › Agentic Robotics, `chapters/discussion.tex`, line 159

Suggestion: "You don't need to stay in the loop" (note 6)

Original:

~~~latex
(bomorrow some contents from the indepent author agentic robotics paper: you dont need to stay in the loop)
~~~

Accepted wording:

~~~latex
The expected benefit of such a loop is operational: a person would not need to stay in the loop for every round.
This would be possible because each change is kept only on recorded evidence, the state of the loop can be recovered after a failure, and the measured quality of a tool expires when the tool is retrained.
It is a narrower claim than choosing better than a person, and it is not a claim about safety: a real robot would still need safety interlocks that are independent of the agent.
The time that a person gives could then go to the teaching that an agent cannot produce on its own.
~~~

Note written with the suggestion: Replaces the note to borrow from the preprint. Facts from the preprint: the title is an operational claim and not a selection claim, because promotion is evidence-gated, state is recoverable, and capability quality is derived from records (Abstract; Section 1); measured tool quality is voided when the tool is retrained (Section 3.6); "staying out of the loop is earned by control of error, not superhuman choice" (Section 7); real-robot deployment requires independent safety interlocks (Section 6, Safety). The preprint also reports that on the one lineage it measured, the loop's selections lost to taking the final checkpoint. Under the planned-work framing that result is not reported, but the paragraph is worded so that it does not claim the opposite. The last sentence is my addition.

Used in: [Future work drafted from notes](../hangs-writing-style-reference.md#future-work-drafted-from-notes).

### DW-49

**Accepted** · weight 1 · Spelling and grammar · 8.4 Future Work: Agentic HRI · Chapter 8 › Future Work › Agentic Human-Robot Interaction, `chapters/discussion.tex`, line 163

Suggestion: The opening of the subsection

Original:

~~~latex
Buinding on agentic Robotics.

Planing is easy for non-interactive tasks. The robot could simply assemble known skills and execute them in sequence.
However, for human robot interaction or collaboritive tasks, there are many challenges.
~~~

Accepted wording:

~~~latex
Agentic HRI builds on agentic robotics.
Planning is comparatively simple for a task that involves no interaction: the robot can assemble known skills and execute them in sequence.
However, tasks in which a robot interacts or collaborates with a person raise additional challenges.
~~~

Note written with the suggestion: Spelling ("Buinding", "Planing", "collaboritive") and a sentence fragment ("Buinding on agentic Robotics."), which becomes a sentence and joins the paragraph that follows. "Planning is easy" becomes "comparatively simple", since the point is the contrast with interactive tasks. "there are many challenges" becomes a sentence with the tasks as its subject.

Used in: [Established dissertation terminology](../hangs-writing-style-reference.md#established-dissertation-terminology).

### DW-50

**Accepted** · weight 1 · Spelling and grammar · 8.4 Future Work: Agentic HRI · Chapter 8 › Future Work › Agentic Human-Robot Interaction, `chapters/discussion.tex`, line 167

Suggestion: The first challenge and its example

Original:

~~~latex
First, users may have different preferences, needs, and capbilities.
\hang{grammar start} For instance, for a collaborative lifting task, a child may provide less force and requires a lower robot height compared to an adult. \hang{grammar end}
~~~

Accepted wording:

~~~latex
First, users may differ in their preferences, needs, and capabilities.
For instance, in a collaborative lifting task, a child may provide less force than an adult and may require the robot to hold the object lower.
~~~

Note written with the suggestion: Spelling ("capbilities"). Grammar in the example: "may provide ... and requires" mixed two verb forms, and "a lower robot height" becomes what the robot would do. The example stays introduced by "For instance", which marks it as hypothetical (style reference, "A hypothetical scenario that explains a problem").

Used in: [An example in a few connected sentences](../hangs-writing-style-reference.md#an-example-in-a-few-connected-sentences), [Word choices made in review](../hangs-writing-style-reference.md#word-choices-made-in-review).

### DW-51

**Accepted with Hang's edit** · weight 4 · Spelling and grammar · 8.4 Future Work: Agentic HRI · Chapter 8 › Future Work › Agentic Human-Robot Interaction, `chapters/discussion.tex`, line 169

Suggestion: The second challenge and its consequence

Original:

~~~latex
\hang{grammar start} In addition, humans' internal states could also require robot behaviors to vary. \hang{grammar end}
\hang{grammar start} These require the robot to have observations beyond objects and to include humans in its planing. \hang{grammar end}
\hang{grammar start} Consequently, this creates challenges: interactions are hard to identify and hard to record in a standard format, and thus hard to learn from. \hang{grammar end}
~~~

Suggested:

~~~latex
Second, the internal state of a person may also require the robot to vary its behavior.
Both require the robot to observe more than the objects in the task and to include the person in its planning.
Consequently, interactions are hard to identify, hard to record in a standard format, and thus hard to learn from.
~~~

Hang's wording:

~~~latex
Second, the internal state of a person may also require the robot to vary its behavior.
Both require the robot to observe more than the objects in the task and to include the person in its planning.
In addition, interactions are hard to identify, hard to record in a standard format, and thus hard to learn from.
~~~

Note written with the suggestion: Spelling ("planing"). Style reference, "Procedural series and enumerations": "First" is followed by "Second". "These require" becomes "Both require", and "this creates challenges:" is dropped because the three things that follow are the challenges.

Used in: [Connectors with a clear job](../hangs-writing-style-reference.md#connectors-with-a-clear-job), [Procedural series and enumerations](../hangs-writing-style-reference.md#procedural-series-and-enumerations).

### DW-52

**Declined** · weight 3 · Spelling and grammar · 8.4 Future Work: Agentic HRI · Chapter 8 › Future Work › Agentic Human-Robot Interaction, `chapters/discussion.tex`, line 173

Suggestion: Chatbot interaction compared with human-robot interaction

Original, which stayed:

~~~latex
\hang{grammar start} In human-chatbot interaction, a human and a chatbot interact in turns and comunicate through natural language and images. \hang{grammar end}
Human robot interaction is way more complex with significantly more hiddent varibles that are hard to capture.
~~~

Declined suggestion:

~~~latex
In an interaction between a person and a chatbot, the two take turns and communicate through natural language and images.
Human-robot interaction is considerably more complex, with many more hidden variables that are hard to capture.
~~~

To check: The spelling corrections in this suggestion (comunicate, hiddent varibles) were declined with it. OA-810 and OA-811 offered them alone, and Hang accepted.

Note written with the suggestion: Spelling ("comunicate", "hiddent varibles") and the hyphen in "human-robot interaction". "way more complex" is informal. Style reference, "Hedges and degree words": "significantly" is kept for statistical claims, so it becomes "considerably".

Used in: [Correcting a sentence without rewording it](../hangs-writing-style-reference.md#correcting-a-sentence-without-rewording-it).

### DW-53

**Accepted with Hang's edit** · weight 4 · New text · 8.4 Future Work: Agentic HRI · Chapter 8 › Future Work › Agentic Human-Robot Interaction, `chapters/discussion.tex`, line 175

Suggestion: The data format, with details from the awesome-HRI reports

Original:

~~~latex
\hang{grammar start} One planned step is to propose a standard data format for recording interactions, including user information extracted from visual input, task context, robot action, human action, and timing. \hang{grammar end} (more details in awesome HRI repo, pull it from there)
~~~

Suggested:

~~~latex
One planned step is to propose a standard data format that records an interaction as a trajectory: who did what, in which order, and with what outcome.
Each trajectory would include user information extracted from visual input, the task context, the actions of the robot and of the person, and their timing.
It would also record how the robot was controlled, the interface and modality through which the interaction took place, and the embodiment of the robot.
Fields that are inferred rather than observed would be labeled as inferred.
The same format would be used for studies reported in papers and for the logs of new experiments, so that both can be compared and learned from.
~~~

Hang's wording:

~~~latex
One planned step is to propose a standard data format that records an interaction as a trajectory: who did what, in which order, and with what outcome.
Each trajectory would include user information extracted from visual input, the task context, the actions of the robot and of the person, and their timing.
It would also record how the robot was controlled, the interface and modality through which the interaction took place, and the embodiment of the robot.
Fields that are inferred rather than observed would be labeled as inferred.
~~~

Note written with the suggestion: Replaces the note "(more details in awesome HRI repo, pull it from there)". Your five fields are kept. Added from the report: a trajectory records "who did what, in which order, with what outcome" (report, "What the repository does"); it records control mode, interface, modality and embodiment (README, "Paper trajectories", framing values); inferred fields are labelled as inferred (report, "Trajectories, not just findings"); one schema is shared by paper studies and real experiment logs (same place). Written as planned work, so no counts of what has been built are given.

Used in: [Future work drafted from notes](../hangs-writing-style-reference.md#future-work-drafted-from-notes).

### DW-54

**Accepted with Hang's edit** · weight 4 · Spelling and grammar · 8.4 Future Work: Agentic HRI · Chapter 8 › Future Work › Agentic Human-Robot Interaction, `chapters/discussion.tex`, line 177

Suggestion: The skill library

Original:

~~~latex
\hang{grammar start} Another planned step is to create an initial skill libary for HRI. \hang{tense start} This would begin by distilling papers from the main-track papers of the ACM/IEEE International Conference on Human-Robot Interaction from 2006 to 2025, and converting them to skills. \hang{tense end} \hang{grammar end}
~~~

Suggested:

~~~latex
Another planned step is to create an initial skill library for HRI.
This would begin by distilling the main-track papers of the ACM/IEEE International Conference on Human-Robot Interaction from 2006 to 2025 and converting their findings into skills.
~~~

Hang's wording:

~~~latex
Another planned step is to create an initial skill library for HRI.
This would begin by distilling the papers from Human-Robot Interaction conferences, such as International Conference on Human-Robot Interaction, and converting their findings into skills.
~~~

To check: The edited wording has such as International Conference, without the. OA-812 added it, and Hang accepted.

Note written with the suggestion: Spelling ("libary"). "distilling papers from the main-track papers" named the papers twice. "converting them to skills" becomes "converting their findings into skills", since it is the findings that become skills. The grammar and tense tags around these two sentences are replaced by one pair of grammar tags.

Used in: [Limitations and future work](../hangs-writing-style-reference.md#limitations-and-future-work).

### DW-55

**Accepted** · weight 1 · Spelling and grammar · 8.4 Future Work: Agentic HRI · Chapter 8 › Future Work › Agentic Human-Robot Interaction, `chapters/discussion.tex`, line 178

Suggestion: "The knowledge base" has not been introduced

Original:

~~~latex
\hang{tense start} The knowledge base would condense these papers into cited knowledge items and task-level study trajectories, and would use them to seed behavior skills that an agent can load when it acts, such as a skill for deciding when and how to request feedback or corrections from a human teacher. \hang{tense end}\
~~~

Accepted wording:

~~~latex
A knowledge base would condense these papers into knowledge items that cite their sources and into task-level study trajectories, and would use both to seed behavior skills that an agent can load when it acts, such as a skill for deciding when and how to request feedback or corrections from a human teacher.
~~~

Note written with the suggestion: Grammar: "The knowledge base" appears before any knowledge base is mentioned, so it becomes "A knowledge base". "cited knowledge items" can be read as items that others cite; the report says each item cites its source papers. A stray backslash after the closing tense tag is removed.

### DW-56

**Accepted with Hang's edit** · weight 4 · Wording (style reference) · 8.4 Future Work: Agentic HRI · Chapter 8 › Future Work › Agentic Human-Robot Interaction, `chapters/discussion.tex`, line 179

Suggestion: Two sentences, and chapter references in place of "Chapters 5 and 6"

Original:

~~~latex
Literature-grounded skills could allow an agentic robot to draw on two decades of HRI findings when deciding whether to ask a non-expert for a demonstration, a \textit{progress} annotation, or a correction, how to phrase the request, and when to stop asking, decisions that this dissertation suggests matter because the value of a request depends on the teacher (\autoref{ch:charm}) and on the signal requested (Chapters 5 and 6).
~~~

Suggested:

~~~latex
Skills grounded in the literature could allow an agentic robot to draw on two decades of HRI findings when deciding whether to ask a non-expert for a demonstration, a \textit{progress} annotation, or a correction, how to phrase the request, and when to stop asking.
The results of this dissertation suggest that these decisions matter, because the value of a request depends on the teacher (\autoref{ch:charm}) and on the signal requested (\autoref{ch:steady} and \autoref{ch:progress}).
~~~

Hang's wording:

~~~latex
Literature-grounded skills could allow an agentic robot to draw on decades of HRI findings as seed skills, and use to decide whether to ask a non-expert for a demonstration, an annotation, or a correction, how to phrase the request, and when to stop asking, instead of building the skill library from scratch.
The results of this dissertation suggest that these decisions matter, because the value of a request depends on the teacher (\autoref{ch:charm}) and on the signal requested (\autoref{ch:steady} and \autoref{ch:progress}).
~~~

To check: In the edited wording, and use to decide has no object (and use them to decide). OA-813 added it, and Hang accepted.

Note written with the suggestion: Style reference, "One main job": what the skills could allow, and why it matters for this dissertation, are now two sentences. "(Chapters 5 and 6)" was typed by hand and would go wrong if a chapter moved; it now uses the chapter labels, which print the same numbers.

Used in: [Limitations and future work](../hangs-writing-style-reference.md#limitations-and-future-work), [Established dissertation terminology](../hangs-writing-style-reference.md#established-dissertation-terminology), [A literal alternative](../hangs-writing-style-reference.md#a-literal-alternative), [Correcting a sentence without rewording it](../hangs-writing-style-reference.md#correcting-a-sentence-without-rewording-it).

### DW-57

**Accepted with Hang's edit** · weight 4 · New text · 8.4 Future Work: Agentic HRI · Chapter 8 › Future Work › Agentic Human-Robot Interaction, `chapters/discussion.tex`, line 180

Suggestion: The WikiSkill loop, and how it leads back to the dissertation

Original:

~~~latex
\hang{grammar start} With the wikiskill arc, human robot interaction trajectories can then be produced with a defined data format using skills, and the skills can then be updated using the collected trajectories. \hang{grammar end}
~~~

Suggested:

~~~latex
Following the loop of WikiSkill \cite{tang2026wikiskill}, an agent that uses these skills would then produce interaction trajectories in the defined data format, and the skills would be updated from the collected trajectories.
In this loop, a finding taken from a paper would enter a skill only as a hypothesis, and a new version of a skill would be kept only when observed interactions show that it leads to better outcomes.
Because these outcomes include the evaluations and reactions of non-experts, the imperfections studied in this dissertation would need to be accounted for when the skills are updated.
~~~

Hang's wording:

~~~latex
Following the loop of WikiSkill \cite{tang2026wikiskill}, an agent that uses these skills would then produce interaction trajectories in the defined data format, and the skills would be updated from the collected trajectories.
In this loop, a finding taken from a paper would enter a skill only as a hypothesis, and a new version of a skill would be kept only when observed interactions show that it leads to better outcomes.
~~~

Note written with the suggestion: Your sentence is kept as the first sentence, with WikiSkill cited (new key in DW-61; title and authors checked on arXiv:2608.27454). The second sentence is from the system architecture page: a reported study can only add a hypothesis, and a skill version changes only when observed robot-human outcomes support it ("Evidence types", "Two learning paths"). An earlier review found that the details of the refinement protocol distracted, so the noise floor and the held-out test are left out. The third sentence is my addition: the outcomes that decide a skill include ratings by people, such as rated comfort, which is where the imperfections studied in this dissertation come back. Delete it on the page if you prefer to end on the mechanism.

Used in: [Future work drafted from notes](../hangs-writing-style-reference.md#future-work-drafted-from-notes).

### DW-58

**Accepted** · weight 1 · Wording (style reference) · 8.5 Summary · Chapter 8 › Summary, `chapters/discussion.tex`, line 215

Suggestion: "supplied" becomes "provided"

Original:

~~~latex
PHIRL improved learning by combining imperfect demonstrations with \textit{progress} annotations on a subset of them, although its annotations were not supplied exclusively by non-experts.
~~~

Accepted wording:

~~~latex
PHIRL improved learning by combining imperfect demonstrations with \textit{progress} annotations on a subset of them, although its annotations were not provided exclusively by non-experts.
~~~

Note written with the suggestion: Same change as DW-10.

### DW-59

**Accepted** · weight 1 · Wording (style reference) · 8.5 Summary · Chapter 8 › Summary, `chapters/discussion.tex`, line 216

Suggestion: "feedback magnitudes deserve attention"

Original:

~~~latex
The connections across chapters suggest that feedback magnitudes deserve attention and that annotations around sub-task changes and precise contacts may be informative, while the latter remains a hypothesis for future evaluation.
~~~

Accepted wording:

~~~latex
The connections across chapters suggest that differences between teachers appear mainly in the magnitude of feedback and that annotations around sub-task changes and precise contacts may be especially informative, although the latter remains a hypothesis for future evaluation.
~~~

Note written with the suggestion: Style reference, "Value words and novelty": prefer the result to a general claim of importance. The finding of Section 8.2 is that differences between teachers appear mainly in the magnitude of feedback, so the Summary says that. "while the latter remains" becomes "although the latter remains", because the clause is a concession.

Used in: [Value words and novelty](../hangs-writing-style-reference.md#value-words-and-novelty).

### DW-60

**Accepted** · weight 1 · Wording (style reference) · 8.5 Summary · Chapter 8 › Summary, `chapters/discussion.tex`, line 218

Suggestion: Say which directions

Original:

~~~latex
It also outlined directions for future work.
~~~

Accepted wording:

~~~latex
It also outlined directions for future work, from selecting which demonstrations to annotate and learning from more teaching modalities to agentic robotics and agentic HRI.
~~~

Note written with the suggestion: Style reference, "A roadmap with actual content". Every other sentence of the Summary says what the chapter found; this one only said that directions exist. It lists the four subsections that have text now. Add the other two on the page if you accept DW-43 or DW-44.

Used in: [A roadmap with actual content](../hangs-writing-style-reference.md#a-roadmap-with-actual-content).

### DW-61

**Accepted** · weight 1 · Bibliography entry · references.bib · references.bib, `references.bib`, line 2953

Suggestion: Two bibliography entries for the agentic subsections

New text, placed next to this passage:

~~~latex
url = {https://github.com/HangYu8123/awesome-HRI}
}
~~~

Accepted wording:

~~~latex
@inproceedings{liang2022codeaspolicies,
  title = {Code as Policies: Language Model Programs for Embodied Control},
  author = {Liang, Jacky and Huang, Wenlong and Xia, Fei and Xu, Peng and Hausman, Karol and Ichter, Brian and Florence, Pete and Zeng, Andy},
  booktitle = {2023 IEEE International Conference on Robotics and Automation (ICRA)},
  year = {2023}
}

@misc{tang2026wikiskill,
  title = {{WikiSkill}: Compiling Agent Experience into Persistent Knowledge for Skill Evolution},
  author = {Tang, Liyan and Rashtchian, Cyrus and Ferng, Chun-Sung and Tomkins, Andrew and Juan, Da-Cheng and Vu, Tu},
  year = {2026},
  eprint = {2608.27454},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2608.27454}
}
~~~

Note written with the suggestion: Needed by DW-45 (Code as Policies) and DW-57 (WikiSkill). Accept it if you accept either of them; an entry that is not cited does no harm. Titles and author lists were checked on arXiv (2209.07753 and 2608.27454). Code as Policies appeared at ICRA 2023; I left out page numbers and the DOI because I did not check them. Your own preprint and the awesome-HRI repository are not cited, in keeping with the planned-work framing.
