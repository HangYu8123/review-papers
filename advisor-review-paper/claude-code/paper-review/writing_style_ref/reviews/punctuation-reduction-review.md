# Colon and semicolon reduction review

Review `punctuation-reduction-review` of the dissertation, from `waiting_for_review/punctuation-reduction-review`. Decided between October 12, 2026 and October 12, 2026. Decisions files: `punctuation-reduction-review.decisions.20261012-144004.json`, `punctuation-reduction-review.decisions.20261012-144854.json` (inferred).

[All reviews](../review-decisions.md) · [Weighted signals](../preference-signals.md) · [Main reference](../hangs-writing-style-reference.md)

| Outcome | Decided by Hang | Not decided by Hang |
| --- | ---: | ---: |
| Accepted as suggested | 16 | 76 |
| Accepted with Hang's edit | 2 | 0 |
| Declined | 7 | 16 |
| Notes from Hang | 0 | |

92 decisions in this review were not made by Hang (inferred). They are listed with the reason that was recorded for them and carry no weight.

**To check before the accepted wording is used**

- [PR-017](#pr-017). The edited wording joins two clauses with a comma (behaviors, it also depends). OA-302 changed it to but also depends, and Hang accepted.

### PR-001

**Declined** · weight 3 · Colon and semicolon reduction · Chapter 1 · Introduction · Chapter 1 › Overview, `chapters/introduction.tex`, line 56

Suggestion: Give each stage its own question

Original, which stayed:

~~~latex
Each stage addresses one question: whether the imperfections in non-expert teaching are random noise (\autoref{ch:charm} and \autoref{ch:sidetracks}); whether the inconsistency of non-expert feedback can be reduced while utilizing the magnitudes (\autoref{ch:steady} and \autoref{ch:progress}); and whether combining demonstrations and feedback can lower quality requirements for human teaching and reduce human effort in annotating(\autoref{ch:phirl}).
~~~

Declined suggestion:

~~~latex
The first stage asks whether the imperfections in non-expert teaching are random noise (\autoref{ch:charm} and \autoref{ch:sidetracks}). The second asks whether the inconsistency of non-expert feedback can be reduced while utilizing the magnitudes (\autoref{ch:steady} and \autoref{ch:progress}). The third asks whether combining demonstrations and feedback can lower quality requirements for human teaching and reduce human effort in annotating (\autoref{ch:phirl}).
~~~

Note written with the suggestion: Split the three research questions into parallel sentences. This removes the colon and two semicolons and keeps the question-to-chapter mapping.

Used in: [One main job and varied sentence length](../hangs-writing-style-reference.md#one-main-job-and-varied-sentence-length).

### PR-002

**Accepted** · weight 1 · Colon reduction · Chapter 1 · Introduction · Chapter 1 › Noise beyond the Task, `chapters/introduction.tex`, line 82

Suggestion: Remove the colon after “are”

Original:

~~~latex
The six domains are: trust in robots, robot experience, educational background, teaching experience, teaching style, and personality traits.
~~~

Accepted wording:

~~~latex
The six domains are trust in robots, robot experience, educational background, teaching experience, teaching style, and personality traits.
~~~

Note written with the suggestion: Remove the colon separating the linking verb from its complement. The six short domains remain a comma-separated list.

Used in: [Few colons and semicolons](../hangs-writing-style-reference.md#few-colons-and-semicolons).

### PR-003

**Declined by inference** · weight 0 · Colon and semicolon reduction · Chapter 1 · Introduction · Chapter 1 › Noise beyond the Task, `chapters/introduction.tex`, line 95

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-004, PR-007: Keep the numbered category definitions together, as in the declined numbered findings and premises.

Suggestion: Separate the four sidetrack definitions

Original, which stayed:

~~~latex
A codebook was used for open coding and for identifying demonstration sidetracks.  \hang{grammar start} Four types of demonstration sidetracks that participants frequently exhibited when providing demonstrations were found: 1) Pause, no input from the controller for a period of time; 2) Alignment, moving the robot back-and-forth to align the robot with a target object; 3) Exploration, controlling multiple degrees of freedom of the robot and not contributing to task completion; 4) Mistake, non-harmful control errors that often last for a very short period of time. \hang{grammar end}
~~~

Declined suggestion:

~~~latex
A codebook was used for open coding and for identifying demonstration sidetracks. Four types of demonstration sidetracks that participants frequently exhibited when providing demonstrations were found. Pause means no input from the controller for a period of time. Alignment involves moving the robot back-and-forth to align the robot with a target object. Exploration involves controlling multiple degrees of freedom of the robot without contributing to task completion. Mistake refers to non-harmful control errors that often last for a very short period of time.
~~~

Note written with the suggestion: Give each category a complete sentence rather than separating comma-heavy definitions with semicolons. Preserve all four definitions and the existing introductory sentence.

### PR-004

**Declined** · weight 3 · Semicolon reduction · Chapter 1 · Introduction · Chapter 1 › Noise beyond the Task, `chapters/introduction.tex`, line 101

Suggestion: Separate the two study conclusions

Original, which stayed:

~~~latex
\textbf{These studies suggest that 1) human evaluative feedback is associated with human characteristics, and including human characteristics in feedback prediction can improve prediction accuracy; and 2) demonstration imperfections can have systematic structure, spatially and temporally related to the task.}
~~~

Declined suggestion:

~~~latex
\textbf{These studies suggest that human evaluative feedback is associated with human characteristics, and including human characteristics in feedback prediction can improve prediction accuracy. They also suggest that demonstration imperfections can have systematic structure, spatially and temporally related to the task.}
~~~

Note written with the suggestion: Split the two conclusions at the semicolon. Keep both findings bold and retain “suggest”.

Used in: [Few colons and semicolons](../hangs-writing-style-reference.md#few-colons-and-semicolons).

### PR-005

**Declined** · weight 3 · Colon reduction · Chapter 1 · Introduction · Chapter 1 › Progress-Heuristicized Inverse Reinforcement Learning, `chapters/introduction.tex`, line 155

Suggestion: Remove the colon after “that”

Original, which stayed:

~~~latex
The key intuition is that: \textit{Reward functions learned from demonstrations should align with the progress annotations of the demonstrations.}
~~~

Declined suggestion:

~~~latex
The key intuition is that \textit{Reward functions learned from demonstrations should align with the progress annotations of the demonstrations.}
~~~

Note written with the suggestion: The that-clause already introduces the intuition; the colon is unnecessary.

Used in: [Few colons and semicolons](../hangs-writing-style-reference.md#few-colons-and-semicolons).

### PR-006

**Accepted** · weight 1 · Colon reduction · Chapter 1 · Introduction · Chapter 1 › Progress-Heuristicized Inverse Reinforcement Learning, `chapters/introduction.tex`, line 158

Suggestion: Remove the colon after “between”

Original:

~~~latex
PHIRL then alternates between: learning a reward model from all demonstrations via an IRL algorithm and aligning the model with the \textit{progress} annotations on the annotated subset.
~~~

Accepted wording:

~~~latex
PHIRL then alternates between learning a reward model from all demonstrations via an IRL algorithm and aligning the model with the \textit{progress} annotations on the annotated subset.
~~~

Note written with the suggestion: The preposition “between” directly introduces the two alternating operations.

Used in: [Few colons and semicolons](../hangs-writing-style-reference.md#few-colons-and-semicolons).

### PR-007

**Declined** · weight 3 · Colon and semicolon reduction · Chapter 1 · Introduction · Chapter 1 › Progress-Heuristicized Inverse Reinforcement Learning, `chapters/introduction.tex`, line 159

Suggestion: Separate the four progress premises

Original, which stayed:

~~~latex
\hang{grammar start} PHIRL exploits four key aspects of the information provided by \textit{progress}: 1) positive \textit{progress} indicates positive rewards; 2) larger increases in \textit{progress} indicate larger rewards; 3) high current \textit{progress} indicates high potential; 4) successful demonstrations should receive more rewards than incomplete or failed demonstrations. \hang{grammar end}
~~~

Declined suggestion:

~~~latex
PHIRL exploits four key aspects of the information provided by \textit{progress}. First, positive \textit{progress} indicates positive rewards. Second, larger increases in \textit{progress} indicate larger rewards. Third, high current \textit{progress} indicates high potential. Fourth, successful demonstrations should receive more rewards than incomplete or failed demonstrations.
~~~

Note written with the suggestion: Use parallel sentences to preserve all four alignment premises while removing the colon and three semicolons.

Used in: [Few colons and semicolons](../hangs-writing-style-reference.md#few-colons-and-semicolons).

### PR-008

**Accepted** · weight 1 · Semicolon reduction · Chapter 2 · Background · Chapter 2, `chapters/background.tex`, line 11

Suggestion: Split the chapter roadmap

Original:

~~~latex
\autoref{sec:bg-rlhf} reviews RLHF and the human characteristics that may shape feedback (the background for \autoref{ch:charm}); \autoref{sec:bg-lfd} reviews learning from demonstrations and the modeling of noisy demonstrations (\autoref{ch:sidetracks}); \autoref{sec:RW} reviews interactive reinforcement learning and feedback dynamics (\autoref{ch:steady}); \autoref{sec:bg-combine} reviews  work that combines human feedback and human demonstrations (\autoref{ch:progress}); and \autoref{sec:bg-reward} reviews reward learning from these combined forms of human teaching (\autoref{ch:phirl}).
~~~

Accepted wording:

~~~latex
\autoref{sec:bg-rlhf} reviews RLHF and the human characteristics that may shape feedback (the background for \autoref{ch:charm}). \autoref{sec:bg-lfd} reviews learning from demonstrations and the modeling of noisy demonstrations (\autoref{ch:sidetracks}). \autoref{sec:RW} reviews interactive reinforcement learning and feedback dynamics (\autoref{ch:steady}). \autoref{sec:bg-combine} reviews  work that combines human feedback and human demonstrations (\autoref{ch:progress}). \autoref{sec:bg-reward} reviews reward learning from these combined forms of human teaching (\autoref{ch:phirl}).
~~~

Note written with the suggestion: Give each background section its own sentence. Preserve the five section-to-chapter links.

Used in: [Few colons and semicolons](../hangs-writing-style-reference.md#few-colons-and-semicolons).

### PR-009

**Accepted** · weight 1 · Semicolon reduction · Chapter 2 · Background · Chapter 2 › Reinforcement Learning from Human Feedback and Human Characteristics, `chapters/background.tex`, line 27

Suggestion: Split feedback delay and its causes

Original:

~~~latex
Human feedback can be biased \cite{thomaz2006reinforcement}, unreliable\cite{faulkner2020interactive}, and inconsistent \cite{bignold2021evaluation} (see also \autoref{ch:steady}). Furthermore, human feedback is rarely instantaneous; delays can occur due to distraction \cite{kessler2019active}, or hesitation \cite{loftin2014strategy}.
~~~

Accepted wording:

~~~latex
Human feedback can be biased \cite{thomaz2006reinforcement}, unreliable\cite{faulkner2020interactive}, and inconsistent \cite{bignold2021evaluation} (see also \autoref{ch:steady}). Furthermore, human feedback is rarely instantaneous. Delays can occur due to distraction \cite{kessler2019active}, or hesitation \cite{loftin2014strategy}.
~~~

Note written with the suggestion: Separate the general observation from the possible causes of delay. Keep the citations beside their causes.

### PR-010

**Declined** · weight 3 · Colon and semicolon reduction · Chapter 2 · Background · Chapter 2 › Interactive Reinforcement Learning and Feedback Dynamics, `chapters/background.tex`, line 83

Suggestion: Separate the four uses of human information

Original, which stayed:

~~~latex
Interactive information in various forms from humans is widely used in prior work: 
as reward or feedback to shape learned policies~\cite{knox2008tamer,knox2009interactively, thomaz2005real,cederborg2015policy,griffith2013policy, yu2021active};
as signals, such as state visiting counts, prediction errors, and actions-states, to perform inverse reinforcement learning \cite{gregor2016variational,pathak2017curiosity,bellemare2016unifying,wang2020reward};
as demonstrations to enable imitation learning or behavior cloning \cite{hester2017deep, ho2016generative}; and
as preferences, which indicate preferable actions or trajectories \cite{christiano2017deep, ibarz2018reward}.
~~~

Declined suggestion:

~~~latex
Prior work widely uses interactive information from humans in several forms. Reward or feedback is used to shape learned policies~\cite{knox2008tamer,knox2009interactively, thomaz2005real,cederborg2015policy,griffith2013policy, yu2021active}. Signals, such as state visiting counts, prediction errors, and actions-states, are used to perform inverse reinforcement learning \cite{gregor2016variational,pathak2017curiosity,bellemare2016unifying,wang2020reward}. Demonstrations enable imitation learning or behavior cloning \cite{hester2017deep, ho2016generative}. Preferences indicate preferable actions or trajectories \cite{christiano2017deep, ibarz2018reward}.
~~~

Note written with the suggestion: Turn the four uses into complete sentences, keeping each group of citations with its original use.

Used in: [One main job and varied sentence length](../hangs-writing-style-reference.md#one-main-job-and-varied-sentence-length).

### PR-011

**Accepted** · weight 1 · Colon reduction · Chapter 2 · Background · Chapter 2 › Combining Human Feedback and Human Demonstrations, `chapters/background.tex`, line 119

Suggestion: Split the limitations and explanation

Original:

~~~latex
This dissertation focuses on human feedback and human demonstrations, which were introduced in \autoref{sec:bg-rlhf} and \autoref{sec:bg-lfd}. Separately, each of these approaches has significant limitations: on the one hand, inferring a policy from human feedback requires a large number of interactions \cite{knox2009interactively, arakawa2018dqn, warnell2018deep}, and on the other, error-free demonstrations are rare and expensive to obtain in the real world \cite{ravichandar2020recent}.
~~~

Accepted wording:

~~~latex
This dissertation focuses on human feedback and human demonstrations, which were introduced in \autoref{sec:bg-rlhf} and \autoref{sec:bg-lfd}. Separately, each of these approaches has significant limitations. On the one hand, inferring a policy from human feedback requires a large number of interactions \cite{knox2009interactively, arakawa2018dqn, warnell2018deep}, and on the other, error-free demonstrations are rare and expensive to obtain in the real world \cite{ravichandar2020recent}.
~~~

Note written with the suggestion: Use a period to introduce the explanation of the limitations; keep the two-sided comparison and citations.

### PR-012

**Accepted with Hang's edit** · weight 4 · Colon reduction · Chapter 2 · Background · Chapter 2 › Combining Human Feedback and Human Demonstrations, `chapters/background.tex`, line 139

Suggestion: Integrate the three components

Original:

~~~latex
LfHF, in general, refers to methods that have three components: feedback collection,  policy or reward shaping, and policy optimization.
~~~

Suggested:

~~~latex
LfHF, in general, refers to methods that have three components, namely feedback collection,  policy or reward shaping, and policy optimization.
~~~

Hang's wording:

~~~latex
LfHF, in general, have three components, namely feedback collection,  policy or reward shaping, and policy optimization.
~~~

Note written with the suggestion: Introduce the three short components with “namely”.

Used in: [Few colons and semicolons](../hangs-writing-style-reference.md#few-colons-and-semicolons).

### PR-013

**Accepted** · weight 1 · Semicolon reduction · Chapter 2 · Background · Chapter 2 › Combining Human Feedback and Human Demonstrations, `chapters/background.tex`, line 165

Suggestion: Separate the technique and instruction

Original:

~~~latex
However, learning from multiple users and learning from imperfect demonstrations are still challenging problems \cite{ravichandar2020recent}. One previous work used a technique they refer to as ``reward sketching''; in practice the annotators were instructed to provide progress \cite{cabi2019scaling}.
~~~

Accepted wording:

~~~latex
However, learning from multiple users and learning from imperfect demonstrations are still challenging problems \cite{ravichandar2020recent}. One previous work used a technique they refer to as ``reward sketching''. In practice the annotators were instructed to provide progress \cite{cabi2019scaling}.
~~~

Note written with the suggestion: Separate the name of the technique from what annotators were instructed to provide.

### PR-014

**Declined** · weight 3 · Colon reduction · Chapter 2 · Background · Chapter 2 › Reward Learning from Human Teaching, `chapters/background.tex`, line 209

Suggestion: Integrate the two learning approaches

Original, which stayed:

~~~latex
LfD generally solves the learning problem in two major ways: (1) inferring a policy \cite{hafner2023mastering, chi2023diffusion, hu2024thought, hussein2021robust}, and (2) inferring a reward function \cite{ren2024hybrid, ho2016generative, yang2024meta, fu2018learning}.
~~~

Declined suggestion:

~~~latex
LfD generally solves the learning problem in two major ways, namely (1) inferring a policy \cite{hafner2023mastering, chi2023diffusion, hu2024thought, hussein2021robust}, and (2) inferring a reward function \cite{ren2024hybrid, ho2016generative, yang2024meta, fu2018learning}.
~~~

Note written with the suggestion: Keep the numbered alternatives and their citations, using “namely” to introduce them.

Used in: [Few colons and semicolons](../hangs-writing-style-reference.md#few-colons-and-semicolons).

### PR-015

**Accepted** · weight 1 · Colon reduction · Chapter 2 · Background · Chapter 2 › Reward Learning from Human Teaching, `chapters/background.tex`, line 211

Suggestion: Separate the advantages and their explanation

Original:

~~~latex
Learning a reward function from demonstrations, while being harder, has multiple advantages: it enables the learning outcome to be transferred to new tasks \cite{Yoo_2022}, supports rapid re-optimization \cite{kim2024unifiedlinearprogrammingframework}, and can be combined with optimal control and RL machinery \cite{zhang2024improvingreinforcementlearninghuman}.
~~~

Accepted wording:

~~~latex
Learning a reward function from demonstrations, while being harder, has multiple advantages. It enables the learning outcome to be transferred to new tasks \cite{Yoo_2022}, supports rapid re-optimization \cite{kim2024unifiedlinearprogrammingframework}, and can be combined with optimal control and RL machinery \cite{zhang2024improvingreinforcementlearninghuman}.
~~~

Note written with the suggestion: Separate the claim of advantages from the sentence listing them.

Used in: [Few colons and semicolons](../hangs-writing-style-reference.md#few-colons-and-semicolons).

### PR-016

**Accepted** · weight 1 · Colon reduction · Chapter 3 · CHARM · Chapter 3, `chapters/charm.tex`, line 6

Suggestion: Integrate the stage focus

Original:

~~~latex
This chapter begins the first stage of this dissertation: understanding the imperfections in non-expert teaching that arise not only from the task or the robot, but also from the human teachers themselves.
~~~

Accepted wording:

~~~latex
This chapter begins the first stage of this dissertation by examining the imperfections in non-expert teaching that arise not only from the task or the robot, but also from the human teachers themselves.
~~~

Note written with the suggestion: Use “by examining” to connect the stage to its focus without an appositional colon.

### PR-017

**Accepted with Hang's edit** · weight 4 · Semicolon reduction · Chapter 3 · CHARM · Chapter 3 › Study Design, `chapters/charm.tex`, line 72

Suggestion: Separate the two sources of feedback variation

Original:

~~~latex
\hang{grammar start} This chapter argues that human feedback does not solely rely on tasks or robot behaviors; it also depends on the human teachers themselves. \hang{grammar end}
~~~

Suggested:

~~~latex
This chapter argues that human feedback does not solely rely on tasks or robot behaviors. It also depends on the human teachers themselves.
~~~

Hang's wording:

~~~latex
This chapter argues that human feedback does not solely rely on tasks or robot behaviors, it also depends on the human teachers themselves.
~~~

To check: The edited wording joins two clauses with a comma (behaviors, it also depends). OA-302 changed it to but also depends, and Hang accepted.

Note written with the suggestion: Make the task/teacher distinction in two complete sentences.

Used in: [Few colons and semicolons](../hangs-writing-style-reference.md#few-colons-and-semicolons).

### PR-018

**Accepted by inference** · weight 0 · Colon reduction · Chapter 3 · CHARM · Chapter 3 › Study Design › Considering Human Attributes for Reinforcement Modeling, `chapters/charm.tex`, line 133

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-002: Remove the colon between is and its reward-equation complement, extending the approved removal after a linking verb.

Suggestion: Remove the colon before the reward equation

Original:

~~~latex
For a given state $s$, action $a$, and a reward function $\mathbb{R}$, the reward of the state-action pair is:
~~~

Accepted wording:

~~~latex
For a given state $s$, action $a$, and a reward function $\mathbb{R}$, the reward of the state-action pair is
~~~

Note written with the suggestion: The displayed equation completes the predicate “is”; remove the colon between the verb and its mathematical complement. Leave the equation unchanged.

### PR-019

**Accepted by inference** · weight 0 · Colon reduction · Chapter 3 · CHARM · Chapter 3 › Study Design › Considering Human Attributes for Reinforcement Modeling, `chapters/charm.tex`, line 138

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-012, PR-104, PR-105, PR-107, PR-111: Integrate short unnumbered names, examples or activities into the existing sentence while retaining their order and scope, following the approved component and example integrations.

Suggestion: Integrate the two oracle inputs

Original:

~~~latex
The feedback oracle $\mathcal{F}$ takes two inputs: Human Characteristics $\overrightarrow{hc}$ and task statistics $\hat{r}$, and outputs the predicted human feedback $f^*$, described as $
~~~

Accepted wording:

~~~latex
The feedback oracle $\mathcal{F}$ takes two inputs, Human Characteristics $\overrightarrow{hc}$ and task statistics $\hat{r}$, and outputs the predicted human feedback $f^*$, described as $
~~~

Note written with the suggestion: Use commas to set off the two input names in this sentence. Preserve the output description and formula.

### PR-020

**Accepted by inference** · weight 0 · Colon reduction · Chapter 3 · CHARM · Chapter 3 › Study Design › Considering Human Attributes for Reinforcement Modeling, `chapters/charm.tex`, line 170

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-006: Remove the colon after given by so the mathematical expression directly completes the preposition.

Suggestion: Remove the colon after “given by”

Original:

~~~latex
be the loss for the regression task. The overall loss function is then given by:
~~~

Accepted wording:

~~~latex
be the loss for the regression task. The overall loss function is then given by
~~~

Note written with the suggestion: The displayed equation directly completes “given by”; preserve the equation and the preceding regression description.

### PR-021

**Accepted by inference** · weight 0 · Colon reduction · Chapter 3 · CHARM · Chapter 3 › Experimental Setup › Task Setup, `chapters/charm.tex`, line 184

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-012, PR-104, PR-105, PR-107, PR-111: Integrate short unnumbered names, examples or activities into the existing sentence while retaining their order and scope, following the approved component and example integrations.

Suggestion: Integrate the two experimental tasks

Original:

~~~latex
\hang{grammar start} The experiment used two tasks from mimicgen \cite{mandlekar2023mimicgen}: nut assembly and coffee preparation, as shown in \autoref{fig:robot_tasks}. \hang{grammar end}
~~~

Accepted wording:

~~~latex
The experiment used two tasks from mimicgen \cite{mandlekar2023mimicgen}, namely nut assembly and coffee preparation, as shown in \autoref{fig:robot_tasks}.
~~~

Note written with the suggestion: Use “namely” to integrate the two task names into the sentence.

### PR-022

**Accepted by inference** · weight 0 · Colon reduction · Chapter 3 · CHARM · Chapter 3 › Experimental Setup › GUI for Standardized Feedback Collection, `chapters/charm.tex`, line 191

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-012, PR-104, PR-105, PR-107, PR-111: Integrate short unnumbered names, examples or activities into the existing sentence while retaining their order and scope, following the approved component and example integrations.

Suggestion: Integrate the two GUI components

Original:

~~~latex
A graphical user interface (GUI) was developed to standardize and streamline data collection. The GUI consists of two components: the ``state window'' and the ``noticing window''. During robot execution, the state window remained continuously displayed. \hang{grammar start} Upon completion of a task, the noticing window appeared with a blinking prompt, instructing the participant to provide a rating. \hang{grammar end} This window displayed five emoji buttons labeled from ``Very Dissatisfied'' to ``Very Satisfied,'' corresponding to a five-point scale in a range of $[-2, 2]$. \hang{delete start + The latency measurement description supports the delay analysis proposed for removal.}Additionally, the system recorded the response latency as the elapsed time between the onset of the noticing window and the participant's rating submission, thereby capturing feedback delay. \hang{delete end}Once a rating was submitted, the noticing window disappeared, and the state window was reactivated for the subsequent trajectory execution. If no response was provided, the noticing window remained visible for a maximum of 5 seconds before automatically proceeding to the next trajectory.
~~~

Accepted wording:

~~~latex
A graphical user interface (GUI) was developed to standardize and streamline data collection. The GUI consists of two components, the ``state window'' and the ``noticing window''. During robot execution, the state window remained continuously displayed. \hang{grammar start} Upon completion of a task, the noticing window appeared with a blinking prompt, instructing the participant to provide a rating. \hang{grammar end} This window displayed five emoji buttons labeled from ``Very Dissatisfied'' to ``Very Satisfied,'' corresponding to a five-point scale in a range of $[-2, 2]$. \hang{delete start + The latency measurement description supports the delay analysis proposed for removal.}Additionally, the system recorded the response latency as the elapsed time between the onset of the noticing window and the participant's rating submission, thereby capturing feedback delay. \hang{delete end}Once a rating was submitted, the noticing window disappeared, and the state window was reactivated for the subsequent trajectory execution. If no response was provided, the noticing window remained visible for a maximum of 5 seconds before automatically proceeding to the next trajectory.
~~~

Note written with the suggestion: Use an appositional comma for the two GUI components; leave the other sentences and existing deletion markers intact.

### PR-023

**Accepted by inference** · weight 0 · Semicolon reduction · Chapter 3 · CHARM · Chapter 3 › Experimental Setup › Procedure, `chapters/charm.tex`, line 202

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-009, PR-011, PR-013, PR-015, PR-103, PR-106: Separate a complete claim, observation or role from its explanation or an independent clause, following the approved sentence splits without dispersing a numbered or detailed definition list.

Suggestion: Separate the prompt and timeout

Original:

~~~latex
During the experiment, the tasks were rendered on-screen while participants provided feedback via the previously described GUI. For both the nut assembly and coffee preparation tasks, each participant rated three trajectories. For each trajectory—comprising approximately 500 to 800 steps—the system recorded task statistics\hang{delete start + Avoid repeating feedback values after the remaining phrase is shortened to feedback.}, feedback values,\hang{delete end} and feedback\hang{delete start + Keep the data summary consistent with the proposed focus on feedback values.} delays\hang{delete end}. The robot paused every 30 actions to prompt for feedback via the GUI; if no response was given within 5 seconds, the system automatically proceeded to the next set of actions.
~~~

Accepted wording:

~~~latex
During the experiment, the tasks were rendered on-screen while participants provided feedback via the previously described GUI. For both the nut assembly and coffee preparation tasks, each participant rated three trajectories. For each trajectory—comprising approximately 500 to 800 steps—the system recorded task statistics\hang{delete start + Avoid repeating feedback values after the remaining phrase is shortened to feedback.}, feedback values,\hang{delete end} and feedback\hang{delete start + Keep the data summary consistent with the proposed focus on feedback values.} delays\hang{delete end}. The robot paused every 30 actions to prompt for feedback via the GUI. If no response was given within 5 seconds, the system automatically proceeded to the next set of actions.
~~~

Note written with the suggestion: Separate the feedback prompt from the timeout behavior. The earlier deletion-marked text is retained exactly.

### PR-024

**Accepted by inference** · weight 0 · Colon reduction · Chapter 3 · CHARM · Chapter 3 › Experimental Setup › Procedure, `chapters/charm.tex`, line 217

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-002: Turn the domain-order fragment into a complete sentence while keeping the short domain list, like the approved six-domain list.

Suggestion: Make the domain ordering a sentence

Original:

~~~latex
Bottom Row (2a) is the mean and standard deviation of the responses across all the questions in the human characteristic questionnaire. Each bar corresponds to one question (e.g., Q1 $\rightarrow$ “Reliability”), and each x-axis label is a word that summarizes the question. Questions from the same human characteristics domain share a common color. From left to right: Trust in Robot, Robot Experience, Education Background, Teaching Experience, Teaching Style, and Personality.
~~~

Accepted wording:

~~~latex
Bottom Row (2a) is the mean and standard deviation of the responses across all the questions in the human characteristic questionnaire. Each bar corresponds to one question (e.g., Q1 $\rightarrow$ “Reliability”), and each x-axis label is a word that summarizes the question. Questions from the same human characteristics domain share a common color. From left to right, the domains are Trust in Robot, Robot Experience, Education Background, Teaching Experience, Teaching Style, and Personality.
~~~

Note written with the suggestion: Make the domain ordering a full sentence rather than a colon-led fragment; retain all six labels.

### PR-025

**Declined by inference** · weight 0 · Colon reduction · Chapter 3 · CHARM · Chapter 3 › Results › Including Human Characteristics Improves Feedback Prediction Accuracy, `chapters/charm.tex`, line 327

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-010, PR-014: Retain the compact baseline label and its explanation; the reviews favor keeping structured alternatives together.

Suggestion: Integrate the random-prediction baseline

Original, which stayed:

~~~latex
Random prediction: the model randomly selected a feedback value (expected accuracy is 20\% and 50\%).
~~~

Declined suggestion:

~~~latex
In random prediction, the model randomly selected a feedback value (expected accuracy is 20\% and 50\%).
~~~

Note written with the suggestion: Use a sentence opening to name the baseline, keeping both expected accuracy figures.

### PR-026

**Declined by inference** · weight 0 · Colon reduction · Chapter 3 · CHARM · Chapter 3 › Results › Including Human Characteristics Improves Feedback Prediction Accuracy, `chapters/charm.tex`, line 328

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-010, PR-014: Retain the parallel baseline label and its explanation, consistently with the adjacent baseline conditions.

Suggestion: Integrate the task-statistics baseline

Original, which stayed:

~~~latex
Task statistics only: the model was trained to predict feedback values using corresponding task statistics.
~~~

Declined suggestion:

~~~latex
With task statistics only, the model was trained to predict feedback values using corresponding task statistics.
~~~

Note written with the suggestion: Name the input condition in a sentence opening.

### PR-027

**Declined by inference** · weight 0 · Colon reduction · Chapter 3 · CHARM · Chapter 3 › Results › Including Human Characteristics Improves Feedback Prediction Accuracy, `chapters/charm.tex`, line 329

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-010, PR-014: Retain the parallel CHARM condition label and its explanation, consistently with the adjacent baseline conditions.

Suggestion: Integrate the CHARM condition

Original, which stayed:

~~~latex
Human characteristics and task statistics (CHARM): the model was trained to predict feedback values using both corresponding task statistics and human characteristics.
~~~

Declined suggestion:

~~~latex
With human characteristics and task statistics (CHARM), the model was trained to predict feedback values using both corresponding task statistics and human characteristics.
~~~

Note written with the suggestion: Name the input condition in a sentence opening.

### PR-028

**Accepted by inference** · weight 0 · Colon reduction · Chapter 4 · Demonstration Sidetracks · Chapter 4, `chapters/sidetracks.tex`, line 6

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-012, PR-104, PR-105, PR-107, PR-111: Integrate short unnumbered names, examples or activities into the existing sentence while retaining their order and scope, following the approved component and example integrations.

Suggestion: Integrate the teaching modality

Original:

~~~latex
This chapter completes the first stage of this dissertation by turning from human feedback to the other form of human teaching studied here: demonstrations.
~~~

Accepted wording:

~~~latex
This chapter completes the first stage of this dissertation by turning from human feedback to the other form of human teaching studied here, demonstrations.
~~~

Note written with the suggestion: Use a comma to introduce the short appositive “demonstrations”.

### PR-029

**Accepted by inference** · weight 0 · Colon reduction · Chapter 4 · Demonstration Sidetracks · Chapter 4, `chapters/sidetracks.tex`, line 7

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-012, PR-104, PR-105, PR-107, PR-111: Integrate short unnumbered names, examples or activities into the existing sentence while retaining their order and scope, following the approved component and example integrations.

Suggestion: Integrate the four category names

Original:

~~~latex
It analyzes demonstrations of a long-horizon manipulation task provided by 40 non-experts in a public space study, and identifies four types of frequent, systematic non-optimal behaviors, termed \thingname{}: \textit{Exploration}, \textit{Mistake}, \textit{Alignment}, and \textit{Pause}.
~~~

Accepted wording:

~~~latex
It analyzes demonstrations of a long-horizon manipulation task provided by 40 non-experts in a public space study, and identifies four types of frequent, systematic non-optimal behaviors, termed \thingname{}, namely \textit{Exploration}, \textit{Mistake}, \textit{Alignment}, and \textit{Pause}.
~~~

Note written with the suggestion: Introduce the four short names with “namely”; preserve their order and styling.

### PR-030

**Accepted by inference** · weight 0 · Semicolon reduction · Chapter 4 · Demonstration Sidetracks · Chapter 4 › Introduction, `chapters/sidetracks.tex`, line 24

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-106, PR-013: Split the two complete contrast clauses while keeping the italic emphasis, like the approved teaching-continuity contrast.

Suggestion: Split the key insight

Original:

~~~latex
The key insight is that \textit{not all non-optimal behaviors from non-experts are randomly distributed errors; instead, they appear in structured ways.}
~~~

Accepted wording:

~~~latex
The key insight is that \textit{not all non-optimal behaviors from non-experts are randomly distributed errors. Instead, they appear in structured ways.}
~~~

Note written with the suggestion: Separate the contrast into two sentences while keeping the italic emphasis.

### PR-031

**Accepted by inference** · weight 0 · Semicolon reduction · Chapter 4 · Demonstration Sidetracks · Chapter 4 › Methodology, `chapters/sidetracks.tex`, line 77

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-009, PR-011, PR-013, PR-015, PR-103, PR-106: Separate a complete claim, observation or role from its explanation or an independent clause, following the approved sentence splits without dispersing a numbered or detailed definition list.

Suggestion: Separate the premise and explanation

Original:

~~~latex
However, not all imperfect behaviors are meaningless.  \hang{grammar start} The premise of this chapter is that some non-optimal behaviors are beyond noise or mistakes; they are actually performed by the demonstrators intentionally or subconsciously to provide successful demonstrations. \hang{grammar end}
~~~

Accepted wording:

~~~latex
However, not all imperfect behaviors are meaningless.  \hang{grammar start} The premise of this chapter is that some non-optimal behaviors are beyond noise or mistakes. They are actually performed by the demonstrators intentionally or subconsciously to provide successful demonstrations. \hang{grammar end}
~~~

Note written with the suggestion: Separate the premise from the explanation of intentional or subconscious behavior.

### PR-032

**Accepted by inference** · weight 0 · Semicolon reduction · Chapter 4 · Demonstration Sidetracks · Chapter 4 › Methodology › Experiment Setup, `chapters/sidetracks.tex`, line 98

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-009, PR-011, PR-013, PR-015, PR-103, PR-106: Separate a complete claim, observation or role from its explanation or an independent clause, following the approved sentence splits without dispersing a numbered or detailed definition list.

Suggestion: Separate the two study-design references

Original:

~~~latex
The demonstration data analyzed in this chapter were collected as part of the validation study for \textit{progress} in \autoref{ch:progress}. The study design is reviewed here; it is described in detail in \autoref{ch:progress}. \hang{created}
~~~

Accepted wording:

~~~latex
The demonstration data analyzed in this chapter were collected as part of the validation study for \textit{progress} in \autoref{ch:progress}. The study design is reviewed here. It is described in detail in \autoref{ch:progress}. \hang{created}
~~~

Note written with the suggestion: Give the local review and the detailed source their own sentences.

### PR-033

**Accepted by inference** · weight 0 · Colon reduction · Chapter 4 · Demonstration Sidetracks · Chapter 4 › Methodology › Experiment Setup, `chapters/sidetracks.tex`, line 103

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-012: Integrate the unnumbered task names with namely, like the accepted component list. Preserve the existing six-versus-seven count discrepancy for a separate factual correction.

Suggestion: Integrate the sub-task list; check the count

Original:

~~~latex
The task consisted of six sub-tasks: move down to jar, approach jar, grasp jar, lift jar, move to ice cream cup, approach ice cream cup, and pour.
~~~

Accepted wording:

~~~latex
The task consisted of six sub-tasks, namely move down to jar, approach jar, grasp jar, lift jar, move to ice cream cup, approach ice cream cup, and pour.
~~~

Note written with the suggestion: Use “namely” to integrate the task list. The source says six sub-tasks but lists seven; this punctuation suggestion deliberately preserves the count and list. Check the count separately.

### PR-034

**Accepted by inference** · weight 0 · Colon reduction · Chapter 4 · Demonstration Sidetracks · Chapter 4 › Methodology › Codebook › Alignment, `chapters/sidetracks.tex`, line 142

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-012, PR-104, PR-105, PR-107, PR-111: Integrate short unnumbered names, examples or activities into the existing sentence while retaining their order and scope, following the approved component and example integrations.

Suggestion: Integrate the alignment feature

Original:

~~~latex
One additional feature was used to help identify the intention of alignment: an increase in precision, meaning the robot is closer to the target after this behavior.
~~~

Accepted wording:

~~~latex
One additional feature was used to help identify the intention of alignment, namely an increase in precision, meaning the robot is closer to the target after this behavior.
~~~

Note written with the suggestion: Integrate the additional feature without changing the operational explanation of precision.

### PR-035

**Accepted by inference** · weight 0 · Colon reduction · Chapter 4 · Demonstration Sidetracks · Chapter 4 › Results › Demonstration Sidetracks are frequent in demonstrations, `chapters/sidetracks.tex`, line 194

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-009, PR-011, PR-013, PR-015, PR-103, PR-106: Separate a complete claim, observation or role from its explanation or an independent clause, following the approved sentence splits without dispersing a numbered or detailed definition list.

Suggestion: Separate prevalence and statistics

Original:

~~~latex
The data show that \thingname{} widely exist across all demonstrations: while 33 out of 40 non-expert participants successfully demonstrated the task, the average number of \thingname{} is $14.48 \pm 10.54$ per participant.
~~~

Accepted wording:

~~~latex
The data show that \thingname{} widely exist across all demonstrations. While 33 out of 40 non-expert participants successfully demonstrated the task, the average number of \thingname{} is $14.48 \pm 10.54$ per participant.
~~~

Note written with the suggestion: Separate the prevalence claim from the success count and per-participant statistic.

### PR-036

**Accepted by inference** · weight 0 · Colon reduction · Chapter 4 · Demonstration Sidetracks · Chapter 4 › Summary, `chapters/sidetracks.tex`, line 278

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-016: Connect the stage to its activities with by, like the approved by examining chapter opening.

Suggestion: Integrate the first-stage focus

Original:

~~~latex
Together with \autoref{ch:charm}, \hang{stage-name start} this chapter completes the first stage of this dissertation: understanding and modeling the imperfections in non-expert teaching. \hang{stage-name end}
~~~

Accepted wording:

~~~latex
Together with \autoref{ch:charm}, this chapter completes the first stage of this dissertation by understanding and modeling the imperfections in non-expert teaching.
~~~

Note written with the suggestion: Express the stage focus with “by” and remove the replaced stage-name annotation pair.

### PR-037

**Accepted by inference** · weight 0 · Colon reduction · Chapter 4 · Demonstration Sidetracks · Chapter 4 › Summary, `chapters/sidetracks.tex`, line 279

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-009, PR-011, PR-013, PR-015, PR-103, PR-106: Separate a complete claim, observation or role from its explanation or an independent clause, following the approved sentence splits without dispersing a numbered or detailed definition list.

Suggestion: Separate the synthesis and evidence

Original:

~~~latex
Both studies found that these imperfections can contain systematic structure: feedback values are associated with the characteristics of the teacher, and demonstration sidetracks are associated with the phases of the task, the locations of target objects, and the control interface.
~~~

Accepted wording:

~~~latex
Both studies found that these imperfections can contain systematic structure. Feedback values are associated with the characteristics of the teacher, and demonstration sidetracks are associated with the phases of the task, the locations of target objects, and the control interface.
~~~

Note written with the suggestion: Separate the synthesis from its two supporting patterns.

### PR-038

**Accepted by inference** · weight 0 · Colon reduction · Chapter 4 · Demonstration Sidetracks · Chapter 4 › Summary, `chapters/sidetracks.tex`, line 283

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-009, PR-011, PR-013, PR-015, PR-103, PR-106: Separate a complete claim, observation or role from its explanation or an independent clause, following the approved sentence splits without dispersing a numbered or detailed definition list.

Suggestion: Separate the stage handoff and chapter roles

Original:

~~~latex
The next two chapters form the second stage of this dissertation, which addresses this question: \autoref{ch:steady} measures how consistent scalar and binary feedback are and stabilizes scalar feedback with STEADY, and \autoref{ch:progress} formalizes \textit{progress}, a signal that is under-explored as a human teaching signal and is designed to be informative and consistent across non-expert users even when their demonstrations contain sidetracks. \hang{created}
~~~

Accepted wording:

~~~latex
The next two chapters form the second stage of this dissertation, which addresses this question. \autoref{ch:steady} measures how consistent scalar and binary feedback are and stabilizes scalar feedback with STEADY, and \autoref{ch:progress} formalizes \textit{progress}, a signal that is under-explored as a human teaching signal and is designed to be informative and consistent across non-expert users even when their demonstrations contain sidetracks. \hang{created}
~~~

Note written with the suggestion: Make the handoff a complete sentence, followed by the roles of the two chapters.

### PR-039

**Accepted by inference** · weight 0 · Colon reduction · Chapter 5 · From “Thumbs Up” to “10 out of 10” · Chapter 5, `chapters/steady.tex`, line 6

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-012, PR-104, PR-105, PR-107, PR-111: Integrate short unnumbered names, examples or activities into the existing sentence while retaining their order and scope, following the approved component and example integrations.

Suggestion: Integrate the binary-feedback design choice

Original:

~~~latex
This chapter begins the second stage of this dissertation, mitigating noise in human feedback, by revisiting a design choice made by many interactive reinforcement learning methods: asking human teachers for binary rather than scalar feedback.
~~~

Accepted wording:

~~~latex
This chapter begins the second stage of this dissertation, mitigating noise in human feedback, by revisiting a design choice made by many interactive reinforcement learning methods, namely asking human teachers for binary rather than scalar feedback.
~~~

Note written with the suggestion: Use “namely” to introduce the specific design choice.

### PR-040

**Accepted by inference** · weight 0 · Semicolon reduction · Chapter 5 · From “Thumbs Up” to “10 out of 10” · Chapter 5, `chapters/steady.tex`, line 8

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-009, PR-011, PR-013, PR-015, PR-103, PR-106: Separate a complete claim, observation or role from its explanation or an independent clause, following the approved sentence splits without dispersing a numbered or detailed definition list.

Suggestion: Separate the two consistency conditions

Original:

~~~latex
The study finds that scalar feedback is less self-consistent than binary feedback when exact agreement is required; with an agreement tolerance of $\pm 2$, however, no difference in self-consistency was detected between the two.
~~~

Accepted wording:

~~~latex
The study finds that scalar feedback is less self-consistent than binary feedback when exact agreement is required. With an agreement tolerance of $\pm 2$, however, no difference in self-consistency was detected between the two.
~~~

Note written with the suggestion: Separate the exact-agreement result from the tolerance-conditioned result. Keep “no difference ... was detected”.

### PR-041

**Accepted by inference** · weight 0 · Semicolon reduction · Chapter 5 · From “Thumbs Up” to “10 out of 10” · Chapter 5, `chapters/steady.tex`, line 9

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-009, PR-011, PR-013, PR-015, PR-103, PR-106: Separate a complete claim, observation or role from its explanation or an independent clause, following the approved sentence splits without dispersing a numbered or detailed definition list.

Suggestion: Separate STEADY and its evaluation

Original:

~~~latex
The chapter then introduces Stabilizing TEacher Assessment DYnamics (STEADY), a method that re-scales scalar feedback into binary labels with confidence degrees; agents trained with scalar feedback processed by STEADY obtained higher returns than agents trained with binary feedback in the evaluated task.
~~~

Accepted wording:

~~~latex
The chapter then introduces Stabilizing TEacher Assessment DYnamics (STEADY), a method that re-scales scalar feedback into binary labels with confidence degrees. Agents trained with scalar feedback processed by STEADY obtained higher returns than agents trained with binary feedback in the evaluated task.
~~~

Note written with the suggestion: Give the method definition and the evaluated performance their own sentences.

### PR-042

**Accepted by inference** · weight 0 · Colon reduction · Chapter 5 · From “Thumbs Up” to “10 out of 10” · Chapter 5, `chapters/steady.tex`, line 15

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-009, PR-011, PR-013, PR-015, PR-103, PR-106: Separate a complete claim, observation or role from its explanation or an independent clause, following the approved sentence splits without dispersing a numbered or detailed definition list.

Suggestion: Separate the concern and reasons

Original:

~~~latex
Both findings make the reliability of human feedback a concern: feedback varies with the teacher, and it is also a natural source of the additional information for evaluating demonstrations.
~~~

Accepted wording:

~~~latex
Both findings make the reliability of human feedback a concern. Feedback varies with the teacher, and it is also a natural source of the additional information for evaluating demonstrations.
~~~

Note written with the suggestion: Separate the concern from the explanation.

### PR-043

**Accepted by inference** · weight 0 · Colon reduction · Chapter 5 · From “Thumbs Up” to “10 out of 10” · Chapter 5, `chapters/steady.tex`, line 16

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-009, PR-011, PR-013, PR-015, PR-103, PR-106: Separate a complete claim, observation or role from its explanation or an independent clause, following the approved sentence splits without dispersing a numbered or detailed definition list.

Suggestion: Separate the response and example

Original:

~~~latex
A common response to this variability is to restrict what teachers can express: many interactive learning methods favor binary feedback over scalar feedback, viewing binary feedback as noise-reduced and thus more suitable for learning \cite{arzate2020survey}.
~~~

Accepted wording:

~~~latex
A common response to this variability is to restrict what teachers can express. Many interactive learning methods favor binary feedback over scalar feedback, viewing binary feedback as noise-reduced and thus more suitable for learning \cite{arzate2020survey}.
~~~

Note written with the suggestion: Separate the general response from the cited example of that response.

### PR-044

**Accepted by inference** · weight 0 · Semicolon reduction · Chapter 5 · From “Thumbs Up” to “10 out of 10” · Chapter 5 › Introduction, `chapters/steady.tex`, line 41

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-009, PR-011, PR-013, PR-015, PR-103, PR-106: Separate a complete claim, observation or role from its explanation or an independent clause, following the approved sentence splits without dispersing a numbered or detailed definition list.

Suggestion: Separate scalar-feedback difficulty and explanation

Original:

~~~latex
Scalar feedback, on the other hand, is also naturally used in daily life (e.g., movie rating and product evaluation) but encodes information beyond that in binary feedback, such as ranking and magnitude, through a wider range of possible values.  However, scalar feedback is more difficult to apply to RL; it is likely to have minor differences while evaluating the same data and is more difficult to separate into good and bad.  Furthermore, users are unlikely to scale their feedback such that it can be interpreted directly as a reward.  For example, on a scale of 10, the distance from 5 to 7 may be perceived as different from the distance from 3 to 5 although they are numerically the same.
~~~

Accepted wording:

~~~latex
Scalar feedback, on the other hand, is also naturally used in daily life (e.g., movie rating and product evaluation) but encodes information beyond that in binary feedback, such as ranking and magnitude, through a wider range of possible values.  However, scalar feedback is more difficult to apply to RL. It is likely to have minor differences while evaluating the same data and is more difficult to separate into good and bad.  Furthermore, users are unlikely to scale their feedback such that it can be interpreted directly as a reward.  For example, on a scale of 10, the distance from 5 to 7 may be perceived as different from the distance from 3 to 5 although they are numerically the same.
~~~

Note written with the suggestion: Separate application difficulty from its explanation, preserving the examples and later sentences.

### PR-045

**Accepted by inference** · weight 0 · Semicolon reduction · Chapter 5 · From “Thumbs Up” to “10 out of 10” · Chapter 5 › Methodology › Experimental Setup, `chapters/steady.tex`, line 163

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-008, PR-009: Give the independent clip properties their own sentences, like the accepted section roadmap. Counts and composition remain unchanged.

Suggestion: Separate the video-clip properties

Original:

~~~latex
There were 200 video clips in total, each 3 seconds long (about 10 minutes total) with the first 100 and second 100 clips identical to each other; each clip represented one action performed by the robot; 
clips were in sequential order of a trajectory;
each set of 100 clips consisted of six trajectories (three successes, three failures).
~~~

Accepted wording:

~~~latex
There were 200 video clips in total, each 3 seconds long (about 10 minutes total), with the first 100 and second 100 clips identical to each other. Each clip represented one action performed by the robot. Clips were in sequential order of a trajectory. Each set of 100 clips consisted of six trajectories (three successes, three failures).
~~~

Note written with the suggestion: Turn the three semicolon joins into complete sentences. Preserve the clip counts, duration, order and trajectory composition. The surrounding tense and grammar blocks remain in place.

### PR-046

**Accepted by inference** · weight 0 · Semicolon reduction · Chapter 5 · From “Thumbs Up” to “10 out of 10” · Chapter 5 › Methodology › Hypotheses, `chapters/steady.tex`, line 220

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-009, PR-011, PR-013, PR-015, PR-103, PR-106: Separate a complete claim, observation or role from its explanation or an independent clause, following the approved sentence splits without dispersing a numbered or detailed definition list.

Suggestion: Separate the heatmap unit and color key

Original:

~~~latex
\caption{Heatmaps of data collected from 90 participants. \hang{grammar start} Each block shows a piece of feedback; red is high-value and blue is low-value feedback. \hang{grammar end} The x-axis represents the video clip and each row is a user, sorted by average feedback value.
~~~

Accepted wording:

~~~latex
\caption{Heatmaps of data collected from 90 participants. \hang{grammar start} Each block shows a piece of feedback. Red is high-value and blue is low-value feedback. \hang{grammar end} The x-axis represents the video clip and each row is a user, sorted by average feedback value.
~~~

Note written with the suggestion: Separate what a block represents from the color key.

### PR-047

**Accepted by inference** · weight 0 · Semicolon reduction · Chapter 5 · From “Thumbs Up” to “10 out of 10” · Chapter 5 › User Study Results › Analysis of H3: How do scalar and binary feedback correlate with the learning algorithm's learning targets?, `chapters/steady.tex`, line 462

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-009, PR-011, PR-013, PR-015, PR-103, PR-106: Separate a complete claim, observation or role from its explanation or an independent clause, following the approved sentence splits without dispersing a numbered or detailed definition list.

Suggestion: Separate feedback use and algorithm differences

Original:

~~~latex
\hang{grammar start} To improve learning, Interactive RL uses human feedback to estimate internal elements of  RL algorithms \cite{arzate2020survey}; different Interactive RL algorithms associate feedback with a different part of the learning problem. \hang{grammar end}
~~~

Accepted wording:

~~~latex
To improve learning, Interactive RL uses human feedback to estimate internal elements of  RL algorithms \cite{arzate2020survey}. Different Interactive RL algorithms associate feedback with a different part of the learning problem.
~~~

Note written with the suggestion: Separate the general use of feedback from the difference among algorithms.

### PR-048

**Accepted by inference** · weight 0 · Colon reduction · Chapter 5 · From “Thumbs Up” to “10 out of 10” · Chapter 5 › User Study Results › Analysis of H3: How do scalar and binary feedback correlate with the learning algorithm's learning targets?, `chapters/steady.tex`, line 463

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-012, PR-104, PR-105, PR-107, PR-111: Integrate short unnumbered names, examples or activities into the existing sentence while retaining their order and scope, following the approved component and example integrations.

Suggestion: Integrate the three training targets

Original:

~~~latex
\hang{grammar start} Spearman's Rank correlation was calculated between the feedback values and the training targets used in several key Interactive RL algorithms: advantages (COACH \cite{pmlr-v70-macglashan17a}), normalized Q-values (TAMER \cite{knox2008tamer}), and action rankings (Policy Shaping \cite{griffith2013policy}), using a standard MDP formulation with states $s \in S$, actions $a \in A$, and value functions $V(s)$ and $Q(s,a)$. \hang{grammar end}
~~~

Accepted wording:

~~~latex
Spearman's Rank correlation was calculated between the feedback values and the training targets used in several key Interactive RL algorithms, namely advantages (COACH \cite{pmlr-v70-macglashan17a}), normalized Q-values (TAMER \cite{knox2008tamer}), and action rankings (Policy Shaping \cite{griffith2013policy}), using a standard MDP formulation with states $s \in S$, actions $a \in A$, and value functions $V(s)$ and $Q(s,a)$.
~~~

Note written with the suggestion: Introduce the three targets with “namely”, keeping each algorithm and citation attached to its target.

### PR-049

**Accepted by inference** · weight 0 · Colon reduction · Chapter 5 · From “Thumbs Up” to “10 out of 10” · Chapter 5 › User Study Results › Analysis of H3: How do scalar and binary feedback correlate with the learning algorithm's learning targets?, `chapters/steady.tex`, line 464

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-002, PR-006: Remove the colons between noun phrases and their inline formula complements without changing the formulas.

Suggestion: Remove two colons before inline formulas

Original:

~~~latex
The advantages were computed by using the advantage function: $A(s,a) =Q(s,a) - V(s)$. The normalized Q-values were computed based on the equation: $r = \frac{Q(s,a)}{\sum_{a_i \in A} Q(s,a_i)}$. The action ranking assigned the rank $(0, \cdots, |A|-1)$ to each action $a$ based on the magnitude of $Q(s,a)$. %In our environment, the action with the highest reward is rank 4 and the action with the lowest reward is rank 0.
~~~

Accepted wording:

~~~latex
The advantages were computed by using the advantage function $A(s,a) =Q(s,a) - V(s)$. The normalized Q-values were computed based on the equation $r = \frac{Q(s,a)}{\sum_{a_i \in A} Q(s,a_i)}$. The action ranking assigned the rank $(0, \cdots, |A|-1)$ to each action $a$ based on the magnitude of $Q(s,a)$. %In our environment, the action with the highest reward is rank 4 and the action with the lowest reward is rank 0.
~~~

Note written with the suggestion: Remove the colons between the noun phrases and the inline formulas. Preserve every symbol and the ranking definition.

### PR-050

**Declined by inference** · weight 0 · Colon reduction · Chapter 5 · From “Thumbs Up” to “10 out of 10” · Chapter 5 › Stabilizing Teacher Assessment Dynamics › STEADY, `chapters/steady.tex`, line 498

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-005, PR-007: Preserve the lead-in to the First/Second intuitions rather than rewriting a structured set of key premises.

Suggestion: Introduce the intuitions with a sentence

Original, which stayed:

~~~latex
The key intuitions are: First, human evaluations often involve associating certain qualities with certain ranges. These are subject to variation,
~~~

Declined suggestion:

~~~latex
Two key intuitions guide STEADY. First, human evaluations often involve associating certain qualities with certain ranges. These are subject to variation,
~~~

Note written with the suggestion: Introduce the already numbered intuitions with a complete sentence; the later “Second” paragraph remains unchanged.

### PR-051

**Accepted by inference** · weight 0 · Colon reduction · Chapter 5 · From “Thumbs Up” to “10 out of 10” · Chapter 5 › Stabilizing Teacher Assessment Dynamics › STEADY, `chapters/steady.tex`, line 518

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-002: Remove the colon between is and its mathematical complement, extending the approved linking-verb cleanup.

Suggestion: Remove the colon before the Wasserstein formula

Original:

~~~latex
The Wasserstein distance between the positive distributions $\phi^+$ and  the negative distribution $\phi^-$ is:
~~~

Accepted wording:

~~~latex
The Wasserstein distance between the positive distributions $\phi^+$ and  the negative distribution $\phi^-$ is
~~~

Note written with the suggestion: Let the displayed formula complete the verb “is”. The formula is unchanged.

### PR-052

**Accepted by inference** · weight 0 · Colon reduction · Chapter 5 · From “Thumbs Up” to “10 out of 10” · Chapter 5 › Stabilizing Teacher Assessment Dynamics › STEADY, `chapters/steady.tex`, line 581

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-006: Remove the colon after given by so the mathematical expression directly completes the preposition.

Suggestion: Remove the colon before the increase-weight formula

Original:

~~~latex
For feedback $\vec{f}$ and its classified distribution $\phi$, the \textit{confidence degree} of \textit{increase weight} cases is given by:
~~~

Accepted wording:

~~~latex
For feedback $\vec{f}$ and its classified distribution $\phi$, the \textit{confidence degree} of \textit{increase weight} cases is given by
~~~

Note written with the suggestion: The displayed formula directly completes “given by”.

### PR-053

**Accepted by inference** · weight 0 · Colon reduction · Chapter 5 · From “Thumbs Up” to “10 out of 10” · Chapter 5 › Stabilizing Teacher Assessment Dynamics › STEADY, `chapters/steady.tex`, line 586

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-006: Remove the colon after given by so the mathematical expression directly completes the preposition.

Suggestion: Remove the colon before the decrease-weight formula

Original:

~~~latex
In \textit{decrease weight} cases, the \textit{confidence degree} is given by:
~~~

Accepted wording:

~~~latex
In \textit{decrease weight} cases, the \textit{confidence degree} is given by
~~~

Note written with the suggestion: The displayed formula directly completes “given by”.

### PR-054

**Accepted by inference** · weight 0 · Colon reduction · Chapter 5 · From “Thumbs Up” to “10 out of 10” · Chapter 5 › Stabilizing Teacher Assessment Dynamics › STEADY, `chapters/steady.tex`, line 606

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-002: Remove the colon between is and its mathematical complement, extending the approved linking-verb cleanup.

Suggestion: Remove the colon before the multi-distribution formula

Original:

~~~latex
The distance among $m$ distributions is:
~~~

Accepted wording:

~~~latex
The distance among $m$ distributions is
~~~

Note written with the suggestion: The displayed formula directly completes “is”.

### PR-055

**Accepted by inference** · weight 0 · Colon and semicolon reduction · Chapter 5 · From “Thumbs Up” to “10 out of 10” · Chapter 5 › Stabilizing Teacher Assessment Dynamics › Scalar Feedback with STEADY › Baselines, `chapters/steady.tex`, line 628

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-012: Keep the four short, unnumbered baseline names in one comma-separated list with namely, like the accepted three-component list.

Suggestion: Use a comma-separated baseline list

Original:

~~~latex
\hang{tense start} Four baselines were compared with \textit{scalar feedback + STEADY}: Binary feedback; Raw scalar feedback; Scalar feedback with a midpoint classifier; Scalar feedback with a sliding window classifier. \hang{tense end}
~~~

Accepted wording:

~~~latex
Four baselines were compared with \textit{scalar feedback + STEADY}, namely binary feedback, raw scalar feedback, scalar feedback with a midpoint classifier, and scalar feedback with a sliding window classifier.
~~~

Note written with the suggestion: The four baseline names are short and contain no internal commas, so ordinary commas and a final “and” are sufficient.

### PR-056

**Accepted by inference** · weight 0 · Semicolon reduction · Chapter 5 · From “Thumbs Up” to “10 out of 10” · Chapter 5 › Stabilizing Teacher Assessment Dynamics › Scalar Feedback with STEADY › Model Performance, `chapters/steady.tex`, line 650

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-009, PR-011, PR-013, PR-015, PR-103, PR-106: Separate a complete claim, observation or role from its explanation or an independent clause, following the approved sentence splits without dispersing a numbered or detailed definition list.

Suggestion: Separate the return range and movement noise

Original:

~~~latex
The maximum return reward can be 14, and the minimum can be -50; because the models were tested on the real robot, randomness in the results comes from noise in robot movement.
~~~

Accepted wording:

~~~latex
The maximum return reward can be 14, and the minimum can be -50. Because the models were tested on the real robot, randomness in the results comes from noise in robot movement.
~~~

Note written with the suggestion: Separate the return range from the explanation of real-robot variation.

### PR-057

**Accepted by inference** · weight 0 · Colon reduction · Chapter 5 · From “Thumbs Up” to “10 out of 10” · Chapter 5 › Summary, `chapters/steady.tex`, line 725

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-009, PR-011, PR-013, PR-015, PR-103, PR-106: Separate a complete claim, observation or role from its explanation or an independent clause, following the approved sentence splits without dispersing a numbered or detailed definition list.

Suggestion: Split the handoff to progress

Original:

~~~latex
The next chapter completes the second stage of this dissertation by addressing this question: rather than post-processing a noisy signal, it formalizes \textit{progress}, a signal that is under-explored as a human teaching signal and gives teachers objective references, the start and the completion of the task, so that the signal is informative and consistent across non-expert users. \hang{created}
~~~

Accepted wording:

~~~latex
The next chapter completes the second stage of this dissertation by addressing this question. Rather than post-processing a noisy signal, the next chapter formalizes \textit{progress}, a signal that is under-explored as a human teaching signal and gives teachers objective references, the start and the completion of the task, so that the signal is informative and consistent across non-expert users. \hang{created}
~~~

Note written with the suggestion: Split the handoff from the next chapter’s approach and name its subject after the split.

### PR-058

**Accepted by inference** · weight 0 · Colon reduction · Chapter 6 · How Much Progress Did I Make? An Unexplored… · Chapter 6, `chapters/progress.tex`, line 10

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-011, PR-015: Separate the cross-chapter claim and supporting findings, like the accepted limitations and advantages explanations. Use the suggested adjacent spelling correction.

Suggestion: Separate the inference and preceding findings

Original:

~~~latex
The results presented in \autoref{ch:steady} show that the inconsistency of scalar feedback can be mitigated after it has been given, and the first stage of this dissertation suggests the underling reasons: feedback is shaped by the characteristics of the teacher (\autoref{ch:charm}), and non-expert demonstrations contain frequent sidetracks, behaviors that do not advance the task but are often part of how non-experts succeed at it (\autoref{ch:sidetracks}).
~~~

Accepted wording:

~~~latex
The results presented in \autoref{ch:steady} show that the inconsistency of scalar feedback can be mitigated after it has been given, and the first stage of this dissertation suggests the underlying reasons. Feedback is shaped by the characteristics of the teacher (\autoref{ch:charm}), and non-expert demonstrations contain frequent sidetracks, behaviors that do not advance the task but are often part of how non-experts succeed at it (\autoref{ch:sidetracks}).
~~~

Note written with the suggestion: Separate the cross-chapter inference from its supporting findings. Correct the adjacent “underling” typo needed for the new sentence.

### PR-059

**Accepted by inference** · weight 0 · Colon reduction · Chapter 6 · How Much Progress Did I Make? An Unexplored… · Chapter 6 › Introduction, `chapters/progress.tex`, line 41

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-009, PR-011, PR-013, PR-015, PR-103, PR-106: Separate a complete claim, observation or role from its explanation or an independent clause, following the approved sentence splits without dispersing a numbered or detailed definition list.

Suggestion: Separate the comparison problem and non-expert case

Original:

~~~latex
It also neglects the objective quality of a demonstration or a partial demonstration itself: a pair of demonstrations might both be good or both bad, making preferences difficult to provide. This is especially true for non-expert demonstrations: non-expert demonstrations can be noisy, multi-policy, and yet still succeed (as shown in \autoref{sectionVC}).
~~~

Accepted wording:

~~~latex
It also neglects the objective quality of a demonstration or a partial demonstration itself. A pair of demonstrations might both be good or both bad, making preferences difficult to provide. This is especially true for non-expert demonstrations. Non-expert demonstrations can be noisy, multi-policy, and yet still succeed (as shown in \autoref{sectionVC}).
~~~

Note written with the suggestion: Split the explanation and the non-expert case into full sentences, keeping the existing qualifiers.

### PR-060

**Accepted by inference** · weight 0 · Colon reduction · Chapter 6 · How Much Progress Did I Make? An Unexplored… · Chapter 6 › Progress, `chapters/progress.tex`, line 69

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-012, PR-104, PR-105, PR-107, PR-111: Integrate short unnumbered names, examples or activities into the existing sentence while retaining their order and scope, following the approved component and example integrations.

Suggestion: Integrate the progress signal name

Original:

~~~latex
The goal is to improve learning from human feedback with a new teaching signal: progress.
~~~

Accepted wording:

~~~latex
The goal is to improve learning from human feedback with a new teaching signal, progress.
~~~

Note written with the suggestion: Use a comma for the short appositive naming the signal.

### PR-061

**Accepted by inference** · weight 0 · Colon reduction · Chapter 6 · How Much Progress Did I Make? An Unexplored… · Chapter 6 › Progress › Progress, `chapters/progress.tex`, line 80

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-002, PR-006: Remove the colon interrupting the expectation-is-that construction so its displayed equality completes the sentence.

Suggestion: Remove the colon before the progress equality

Original:

~~~latex
A \textit{progress} value of 0 indicates that the task has not yet begun, while a value of 100 signifies task completion. \hang{grammar start} In between, the expectation is that for any given task $t$, current state $s$, any actions $a_i$ and $a_j$, and any previous states $s_i$ and $s_j$: \hang{grammar end}
~~~

Accepted wording:

~~~latex
A \textit{progress} value of 0 indicates that the task has not yet begun, while a value of 100 signifies task completion. \hang{grammar start} In between, the expectation is that for any given task $t$, current state $s$, any actions $a_i$ and $a_j$, and any previous states $s_i$ and $s_j$ \hang{grammar end}
~~~

Note written with the suggestion: The displayed equality completes “the expectation is that”; the intervening conditions do not require a colon. Leave the equality unchanged.

### PR-062

**Accepted by inference** · weight 0 · Colon reduction · Chapter 6 · How Much Progress Did I Make? An Unexplored… · Chapter 6 › Progress with non-self-provided demonstrations, `chapters/progress.tex`, line 119

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-009, PR-011, PR-013, PR-015, PR-103, PR-106: Separate a complete claim, observation or role from its explanation or an independent clause, following the approved sentence splits without dispersing a numbered or detailed definition list.

Suggestion: Separate the online studies and their purposes

Original:

~~~latex
\hang{tense start} Two online studies were conducted: Online study \RNum{1} used three simple tasks to evaluate the workload of giving progress, while online study \RNum{2} involved a long-horizon task comprising six sub-tasks and five scenarios to assess the utility of progress. \hang{tense end}
~~~

Accepted wording:

~~~latex
Two online studies were conducted. Online study \RNum{1} used three simple tasks to evaluate the workload of giving progress, while online study \RNum{2} involved a long-horizon task comprising six sub-tasks and five scenarios to assess the utility of progress.
~~~

Note written with the suggestion: Separate the study count from the description of the two studies.

### PR-063

**Declined by inference** · weight 0 · Colon reduction · Chapter 6 · How Much Progress Did I Make? An Unexplored… · Chapter 6 › Progress with non-self-provided demonstrations › Online study setups › Online study 2, `chapters/progress.tex`, line 148

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-004, PR-010, PR-014: Keep the colon introducing the long named-scenario definitions, including their internal commas.

Suggestion: Integrate the five scenarios

Original, which stayed:

~~~latex
\hang{grammar start} Five demonstrations were chosen, each representing a distinct scenario: Perfect (everything is performed flawlessly), Imperfect (the cup is dropped onto the table rather than being placed carefully), Unaware (failed to pick the stir, and spun without a stir), Corrected (failed to pick the stir but went back to pick it after a few spins), and Failure (the cup was dropped at the beginning). \hang{grammar end}
~~~

Declined suggestion:

~~~latex
Five demonstrations were chosen, each representing a distinct scenario, namely Perfect (everything is performed flawlessly), Imperfect (the cup is dropped onto the table rather than being placed carefully), Unaware (failed to pick the stir, and spun without a stir), Corrected (failed to pick the stir but went back to pick it after a few spins), and Failure (the cup was dropped at the beginning).
~~~

Note written with the suggestion: Introduce the five named scenarios with “namely”. Keep all scenario definitions unchanged.

### PR-064

**Accepted by inference** · weight 0 · Colon reduction · Chapter 6 · How Much Progress Did I Make? An Unexplored… · Chapter 6 › Progress with Self-Provided Demonstrations from Non-experts, `chapters/progress.tex`, line 336

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-006: Remove the colon between at and the URL, like the approved removal after between.

Suggestion: Remove the colon before the dataset URL

Original:

~~~latex
All data collected from the public space study were released as a dataset, along with the example scripts that read the data from files. The dataset is available at: \url{https://github.com/TeachingwithProgress/Non-Expert_Demonstrations}
~~~

Accepted wording:

~~~latex
All data collected from the public space study were released as a dataset, along with the example scripts that read the data from files. The dataset is available at \url{https://github.com/TeachingwithProgress/Non-Expert_Demonstrations}
~~~

Note written with the suggestion: The preposition “at” directly introduces the URL; leave the link unchanged.

### PR-065

**Accepted by inference** · weight 0 · Colon reduction · Chapter 6 · How Much Progress Did I Make? An Unexplored… · Chapter 6 › Progress with Self-Provided Demonstrations from Non-experts › Non-Expert Demonstrations Are Multi-Policy and Noisy, `chapters/progress.tex`, line 398

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-016, PR-107: Integrate the un-emphasized intuition in a that-clause while preserving its uncertainty, consistent with approved prose integrations.

Suggestion: Integrate the intuition about comparisons

Original:

~~~latex
This suggests that policies can be both successful and sub-optimal, which supports the intuition: assessing the quality of demonstrations by comparing is likely to lose information if there are many "good enough" policies.
~~~

Accepted wording:

~~~latex
This suggests that policies can be both successful and sub-optimal, which supports the intuition that assessing the quality of demonstrations by comparing is likely to lose information if there are many "good enough" policies.
~~~

Note written with the suggestion: Use a that-clause to state the supported intuition without changing its uncertainty.

### PR-066

**Declined by inference** · weight 0 · Colon reduction · Chapter 6 · How Much Progress Did I Make? An Unexplored… · Chapter 6 › Progress with Self-Provided Demonstrations from Non-experts › Non-Expert Demonstrations Are Multi-Policy and Noisy, `chapters/progress.tex`, line 402

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-005, PR-108: Keep the emphatic bold claim and its colon-linked explanation; the reviewed choices retained an emphasized intuition and a compact explanatory colon.

Suggestion: Connect the approximation claim to its explanation

Original, which stayed:

~~~latex
and suggests that \textbf{noisy demonstrations from partially trained agents or perfect demonstrations with injected noise are inappropriate approximations of noisy human demonstrations}: human demonstrations are ``noisy'' in a meaningful way.
~~~

Declined suggestion:

~~~latex
and suggests that \textbf{noisy demonstrations from partially trained agents or perfect demonstrations with injected noise are inappropriate approximations of noisy human demonstrations} because human demonstrations are ``noisy'' in a meaningful way.
~~~

Note written with the suggestion: Make the explanatory relationship explicit with “because”. Preserve the bold claim and the quoted term.

### PR-067

**Accepted by inference** · weight 0 · Semicolon reduction · Chapter 6 · How Much Progress Did I Make? An Unexplored… · Chapter 6 › Progress with Self-Provided Demonstrations from Non-experts › Progress indicates task completions and is more consistent across participants than scalar feedback, `chapters/progress.tex`, line 423

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-009, PR-106: Split the two complete conditional-result clauses while retaining the exact threshold, like the approved two-clause splits.

Suggestion: Separate the completion rule and alternative

Original:

~~~latex
\hang{grammar start} If progress at the last step is less than 90, the task is incomplete; otherwise, the task is completed. \hang{grammar end}
~~~

Accepted wording:

~~~latex
If progress at the last step is less than 90, the task is incomplete. Otherwise, the task is completed.
~~~

Note written with the suggestion: Use two sentences for the threshold rule and its alternative. Preserve the strict “less than 90” boundary.

### PR-068

**Accepted by inference** · weight 0 · Colon reduction · Chapter 6 · How Much Progress Did I Make? An Unexplored… · Chapter 6 › Discussion, `chapters/progress.tex`, line 469

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-012, PR-104, PR-105, PR-107, PR-111: Integrate short unnumbered names, examples or activities into the existing sentence while retaining their order and scope, following the approved component and example integrations.

Suggestion: Integrate the possible uses of progress

Original:

~~~latex
The information in \textit{progress} could be used in several ways: reward learning, identifying reward hacking, and filtering or ranking demonstrations.
~~~

Accepted wording:

~~~latex
The information in \textit{progress} could be used in several ways, including reward learning, identifying reward hacking, and filtering or ranking demonstrations.
~~~

Note written with the suggestion: Integrate the three uses with “including”, preserving their non-exhaustive framing.

### PR-069

**Accepted by inference** · weight 0 · Colon reduction · Chapter 6 · How Much Progress Did I Make? An Unexplored… · Chapter 6 › Summary, `chapters/progress.tex`, line 503

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-103, PR-011: Separate the single remaining question from its lead-in without dispersing a numbered question list, like the approved approach explanation.

Suggestion: Separate the remaining learning question

Original:

~~~latex
What this chapter did not show is how \textit{progress} can be used for learning: whether annotations on a small subset of imperfect demonstrations can improve what is learned from all of them, without requiring a human to remain in the training loop.
~~~

Accepted wording:

~~~latex
What this chapter did not show is how \textit{progress} can be used for learning. The remaining question is whether annotations on a small subset of imperfect demonstrations can improve what is learned from all of them, without requiring a human to remain in the training loop.
~~~

Note written with the suggestion: State the unresolved question separately, preserving the subset and human-effort conditions.

### PR-070

**Accepted by inference** · weight 0 · Colon reduction · Chapter 6 · How Much Progress Did I Make? An Unexplored… · Chapter 6 › Summary, `chapters/progress.tex`, line 504

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-009, PR-011, PR-013, PR-015, PR-103, PR-106: Separate a complete claim, observation or role from its explanation or an independent clause, following the approved sentence splits without dispersing a numbered or detailed definition list.

Suggestion: Split the final-stage handoff

Original:

~~~latex
The final stage of this dissertation addresses this question: the next chapter presents a reward learning framework that learns a reward function from demonstrations and aligns it with \textit{progress} annotations on those demonstrations. \hang{created}
~~~

Accepted wording:

~~~latex
The final stage of this dissertation addresses this question. The next chapter presents a reward learning framework that learns a reward function from demonstrations and aligns it with \textit{progress} annotations on those demonstrations. \hang{created}
~~~

Note written with the suggestion: Separate the final-stage handoff from the description of the next chapter.

### PR-071

**Accepted by inference** · weight 0 · Colon reduction · Chapter 7 · PHIRL · Chapter 7, `chapters/phirl.tex`, line 16

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-009, PR-011, PR-013, PR-015, PR-103, PR-106: Separate a complete claim, observation or role from its explanation or an independent clause, following the approved sentence splits without dispersing a numbered or detailed definition list.

Suggestion: Separate the preceding results and their statement

Original:

~~~latex
PHIRL builds on two results from the preceding chapters: \textit{progress} is consistent and intuitive for non-expert users (\autoref{ch:progress}), and non-expert demonstrations contain structured imperfections that do not advance the task (\autoref{ch:sidetracks}).
~~~

Accepted wording:

~~~latex
PHIRL builds on two results from the preceding chapters. \textit{progress} is consistent and intuitive for non-expert users (\autoref{ch:progress}), and non-expert demonstrations contain structured imperfections that do not advance the task (\autoref{ch:sidetracks}).
~~~

Note written with the suggestion: Separate the statement of two preceding results from the results themselves.

### PR-072

**Accepted by inference** · weight 0 · Semicolon reduction · Chapter 7 · PHIRL · Chapter 7, `chapters/phirl.tex`, line 17

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-009, PR-011, PR-013, PR-015, PR-103, PR-106: Separate a complete claim, observation or role from its explanation or an independent clause, following the approved sentence splits without dispersing a numbered or detailed definition list.

Suggestion: Separate human-engagement design and annotation

Original:

~~~latex
Furthermore, to reduce human engagement, PHIRL is designed to not ask humans to provide near-optimal demonstrations or to remain in the training loop; it asks them to annotate a small subset of existing demonstrations with \textit{progress}, and uses these annotations to shape what is learned from all of the demonstrations.
~~~

Accepted wording:

~~~latex
Furthermore, to reduce human engagement, PHIRL is designed to not ask humans to provide near-optimal demonstrations or to remain in the training loop. It asks them to annotate a small subset of existing demonstrations with \textit{progress}, and uses these annotations to shape what is learned from all of the demonstrations.
~~~

Note written with the suggestion: Separate the reduced-engagement design from the annotation procedure.

### PR-073

**Accepted by inference** · weight 0 · Semicolon reduction · Chapter 7 · PHIRL · Chapter 7, `chapters/phirl.tex`, line 19

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-009, PR-011, PR-013, PR-015, PR-103, PR-106: Separate a complete claim, observation or role from its explanation or an independent clause, following the approved sentence splits without dispersing a numbered or detailed definition list.

Suggestion: Separate related work and publication status

Original:

~~~latex
The related work for this chapter is \hang{cross-ref start} reviewed in \autoref{sec:bg-combine} and \autoref{sec:bg-reward} \hang{cross-ref end}; at the time of writing, the work presented in this chapter is in submission.
~~~

Accepted wording:

~~~latex
The related work for this chapter is \hang{cross-ref start} reviewed in \autoref{sec:bg-combine} and \autoref{sec:bg-reward} \hang{cross-ref end}. At the time of writing, the work presented in this chapter is in submission.
~~~

Note written with the suggestion: Separate the background cross-reference from the publication status. Preserve the existing cross-reference markers.

### PR-074

**Accepted by inference** · weight 0 · Colon reduction · Chapter 7 · PHIRL · Chapter 7 › Introduction, `chapters/phirl.tex`, line 63

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-009, PR-011, PR-013, PR-015, PR-103, PR-106: Separate a complete claim, observation or role from its explanation or an independent clause, following the approved sentence splits without dispersing a numbered or detailed definition list.

Suggestion: Separate the analogy from its lead-in

Original:

~~~latex
This process mimics human learning: much like a student cross-referencing answers to correct their own solutions, the method generates a potential reward function and compares it against human feedback to refine its learned rewards.
~~~

Accepted wording:

~~~latex
This process mimics human learning. Much like a student cross-referencing answers to correct their own solutions, the method generates a potential reward function and compares it against human feedback to refine its learned rewards.
~~~

Note written with the suggestion: Give the student analogy its own sentence.

### PR-075

**Accepted by inference** · weight 0 · Colon reduction · Chapter 7 · PHIRL · Chapter 7 › Introduction, `chapters/phirl.tex`, line 64

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-012, PR-104, PR-105, PR-107, PR-111: Integrate short unnumbered names, examples or activities into the existing sentence while retaining their order and scope, following the approved component and example integrations.

Suggestion: Integrate the four reward-shaping dimensions

Original:

~~~latex
PHIRL iteratively uses an IRL algorithm to learn a reward function from demonstrations, calculates rewards over the annotated demonstrations, and then shapes the learned reward function in four dimensions: temporal delta, magnitudes, potential, and completion. In addition, PHIRL is extended by integrating a fine-tuned Vision-Language Model (VLM) to provide online \textit{progress} feedback.
~~~

Accepted wording:

~~~latex
PHIRL iteratively uses an IRL algorithm to learn a reward function from demonstrations, calculates rewards over the annotated demonstrations, and then shapes the learned reward function in four dimensions, namely temporal delta, magnitudes, potential, and completion. In addition, PHIRL is extended by integrating a fine-tuned Vision-Language Model (VLM) to provide online \textit{progress} feedback.
~~~

Note written with the suggestion: Integrate the four dimension names with “namely”; preserve the VLM sentence.

### PR-076

**Declined by inference** · weight 0 · Colon reduction · Chapter 7 · PHIRL · Chapter 7 › Methodology › Reward Learning from Demonstrations, `chapters/phirl.tex`, line 166

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-005, PR-108: The lead-in already states a complete interpretation, and the colon usefully introduces its displayed mathematical specification.

Suggestion: Remove the colon before the IRL optimization

Original, which stayed:

~~~latex
If the demonstrations are assumed to be from an optimal policy $\pi^*$, the IRL problem can then be interpreted as a maximum likelihood problem:
~~~

Declined suggestion:

~~~latex
If the demonstrations are assumed to be from an optimal policy $\pi^*$, the IRL problem can then be interpreted as a maximum likelihood problem
~~~

Note written with the suggestion: Let the displayed optimization directly complete “interpreted as a maximum likelihood problem”.

### PR-077

**Declined by inference** · weight 0 · Colon reduction · Chapter 7 · PHIRL · Chapter 7 › Methodology › Reward Learning from Demonstrations, `chapters/phirl.tex`, line 175

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-005: The complete statement about the discriminator introduces a displayed definition; retain that explanatory colon.

Suggestion: Remove the colon before the discriminator definition

Original, which stayed:

~~~latex
The discriminator uses a particular $f_\theta$:
~~~

Declined suggestion:

~~~latex
The discriminator uses a particular $f_\theta$
~~~

Note written with the suggestion: Let the displayed definition complete the predicate. No formula changes.

### PR-078

**Declined by inference** · weight 0 · Colon reduction · Chapter 7 · PHIRL · Chapter 7 › Methodology › Reward Learning from Demonstrations, `chapters/phirl.tex`, line 180

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-005, PR-108: The clause already gives the interpretation under deterministic dynamics, and the colon introduces its mathematical specification.

Suggestion: Remove the colon before the advantage expression

Original, which stayed:

~~~latex
where $f_{\theta}(s, a, s')$ can be interpreted as the advantage under deterministic dynamics:
~~~

Declined suggestion:

~~~latex
where $f_{\theta}(s, a, s')$ can be interpreted as the advantage under deterministic dynamics
~~~

Note written with the suggestion: Continue the explanatory clause directly into its displayed mathematical expression.

### PR-079

**Accepted by inference** · weight 0 · Colon reduction · Chapter 7 · PHIRL · Chapter 7 › Methodology › PHIRL, `chapters/phirl.tex`, line 295

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-006: Remove the colon before the displayed sum that directly specifies the minimization, extending the approved preposition-complement cleanup.

Suggestion: Remove the colon before the combined shaping objective

Original:

~~~latex
\hang{grammar start} Given a demonstration dataset $\mathcal{D}$ and its annotated subset $\mathcal{D}_p$, a learned reward $r_\theta$ is \emph{aligned} by minimizing a sum of all shaping components: \hang{grammar end}
~~~

Accepted wording:

~~~latex
Given a demonstration dataset $\mathcal{D}$ and its annotated subset $\mathcal{D}_p$, a learned reward $r_\theta$ is \emph{aligned} by minimizing a sum of all shaping components
~~~

Note written with the suggestion: The displayed sum directly completes the minimization description.

### PR-080

**Accepted by inference** · weight 0 · Colon reduction · Chapter 7 · PHIRL · Chapter 7 › Experiments and Results › Setups, `chapters/phirl.tex`, line 386

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-009, PR-011, PR-013, PR-015, PR-103, PR-106: Separate a complete claim, observation or role from its explanation or an independent clause, following the approved sentence splits without dispersing a numbered or detailed definition list.

Suggestion: Separate the real-robot setup and participants

Original:

~~~latex
For the real robot domain, a similar setup was used: six participants were recruited (two ``worse'', two ``okay'', and two ``better'', 10 demonstrations each), and an MH dataset was constructed. \hang{update end}
~~~

Accepted wording:

~~~latex
For the real robot domain, a similar setup was used. Six participants were recruited (two ``worse'', two ``okay'', and two ``better'', 10 demonstrations each), and an MH dataset was constructed. \hang{update end}
~~~

Note written with the suggestion: Separate the setup comparison from the participant and dataset details. Preserve the closing update marker.

### PR-081

**Accepted by inference** · weight 0 · Colon reduction · Chapter 7 · PHIRL · Chapter 7 › Experiments and Results › Setups, `chapters/phirl.tex`, line 452

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-104, PR-105: Integrate the three recruitment groups with with, keeping the coordinated list and distinct roles, like approved integrations of examples and activities.

Suggestion: Integrate the three recruitment groups

Original:

~~~latex
\noindent \textbf{Data Collection} \hang{update start} Separate groups were recruited: six participants to annotate the Robomimic datasets, six participants to construct the real robot dataset, and two participants to annotate the real robot dataset.
~~~

Accepted wording:

~~~latex
\noindent \textbf{Data Collection} \hang{update start} Separate groups were recruited, with six participants to annotate the Robomimic datasets, six participants to construct the real robot dataset, and two participants to annotate the real robot dataset.
~~~

Note written with the suggestion: Use “with” to introduce the three participant groups while preserving their distinct roles and the opening update marker.

### PR-082

**Accepted by inference** · weight 0 · Colon reduction · Chapter 7 · PHIRL · Chapter 7 › Experiments and Results › Setups, `chapters/phirl.tex`, line 454

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-009, PR-011, PR-013, PR-015, PR-103, PR-106: Separate a complete claim, observation or role from its explanation or an independent clause, following the approved sentence splits without dispersing a numbered or detailed definition list.

Suggestion: Separate annotation design and instruction

Original:

~~~latex
To reduce the bias in the collected \textit{progress} annotations, no specific patterns were imposed on the \textit{progress} values: participants were only asked to provide values from 0 to 100.
~~~

Accepted wording:

~~~latex
To reduce the bias in the collected \textit{progress} annotations, no specific patterns were imposed on the \textit{progress} values. Participants were only asked to provide values from 0 to 100.
~~~

Note written with the suggestion: Separate the lack of an imposed pattern from the 0–100 instruction.

### PR-083

**Accepted by inference** · weight 0 · Colon reduction · Chapter 7 · PHIRL · Chapter 7 › Experiments and Results › PHIRL Learns More Robust Reward Functions, `chapters/phirl.tex`, line 563

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-012, PR-104, PR-105, PR-107, PR-111: Integrate short unnumbered names, examples or activities into the existing sentence while retaining their order and scope, following the approved component and example integrations.

Suggestion: Integrate the two reward-hacking scenarios

Original:

~~~latex
\hang{grammar start} During the training of PHIRL, AIRL, and PPO, two reward hacking scenarios emerged: Lift-Drop-Loop and Touch-And-Stay. \hang{grammar end}
~~~

Accepted wording:

~~~latex
During the training of PHIRL, AIRL, and PPO, two reward hacking scenarios emerged, namely Lift-Drop-Loop and Touch-And-Stay.
~~~

Note written with the suggestion: Integrate the two scenario names with “namely”.

### PR-084

**Declined by inference** · weight 0 · Colon reduction · Chapter 7 · PHIRL · Chapter 7 › Discussion and Limitations, `chapters/phirl.tex`, line 620

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-005: Keep the colon introducing the quoted key idea, analogous to the explicitly retained emphasized key intuition.

Suggestion: Integrate the ReWiND quotation

Original, which stayed:

~~~latex
It adopted the key idea of ReWiND: ``use language instructions to represent key subgoals in a task, and then combine the language instructions with a VLM to indicate task progress.''
~~~

Declined suggestion:

~~~latex
It adopted the key idea of ReWiND, namely to ``use language instructions to represent key subgoals in a task, and then combine the language instructions with a VLM to indicate task progress.''
~~~

Note written with the suggestion: Integrate the quoted idea with “namely to”; retain the quoted wording exactly.

### PR-085

**Accepted by inference** · weight 0 · Colon reduction · Chapter 7 · PHIRL · Chapter 7 › Summary, `chapters/phirl.tex`, line 699

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-009, PR-011, PR-013, PR-015, PR-103, PR-106: Separate a complete claim, observation or role from its explanation or an independent clause, following the approved sentence splits without dispersing a numbered or detailed definition list.

Suggestion: Separate the combined-teaching conclusion and explanation

Original:

~~~latex
This chapter completes the final stage of this dissertation, providing evidence that imperfect teaching can be leveraged for learning when complementary forms of teaching are combined: demonstrations provide dense but imperfect information about how to perform a task, and \textit{progress} annotations on a small subset of them indicate which of the demonstrated behaviors actually advance it.
~~~

Accepted wording:

~~~latex
This chapter completes the final stage of this dissertation, providing evidence that imperfect teaching can be leveraged for learning when complementary forms of teaching are combined. Demonstrations provide dense but imperfect information about how to perform a task, and \textit{progress} annotations on a small subset of them indicate which of the demonstrated behaviors actually advance it.
~~~

Note written with the suggestion: Separate the stage-level conclusion from the explanation of the two information sources.

### PR-086

**Accepted by inference** · weight 0 · Colon reduction · Chapter 7 · PHIRL · Chapter 7 › Summary, `chapters/phirl.tex`, line 700

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-012, PR-104, PR-105, PR-107, PR-111: Integrate short unnumbered names, examples or activities into the existing sentence while retaining their order and scope, following the approved component and example integrations.

Suggestion: Integrate the questions for the discussion

Original:

~~~latex
The next chapter steps back from the individual studies of \autoref{ch:charm} through \autoref{ch:phirl} and considers what they suggest when taken together: which lessons hold across both forms of teaching and all three stages, and where the findings stop applying.
~~~

Accepted wording:

~~~latex
The next chapter steps back from the individual studies of \autoref{ch:charm} through \autoref{ch:phirl} and considers what they suggest when taken together, including which lessons hold across both forms of teaching and all three stages, and where the findings stop applying.
~~~

Note written with the suggestion: Use “including” to integrate the two discussion questions.

### PR-087

**Declined by inference** · weight 0 · Colon reduction · Chapter 8 · Overall Discussion · Chapter 8, `chapters/discussion.tex`, line 7

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-001: Keep the roadmap and its three research questions together, analogous to the declined three-stage question rewrite.

Suggestion: Separate the roadmap and research questions

Original, which stayed:

~~~latex
\hang{style start} It first answers the three questions of this dissertation (\autoref{sec:discussion-questions}): whether the imperfections in non-expert teaching are random noise, whether the inconsistency of non-expert feedback can be reduced while utilizing the magnitudes, and whether imperfect demonstrations and feedback can be combined so that a robot learns more from both with little additional human effort. \hang{style end}
~~~

Declined suggestion:

~~~latex
It first answers the three questions of this dissertation (\autoref{sec:discussion-questions}). These questions ask whether the imperfections in non-expert teaching are random noise, whether the inconsistency of non-expert feedback can be reduced while utilizing the magnitudes, and whether imperfect demonstrations and feedback can be combined so that a robot learns more from both with little additional human effort.
~~~

Note written with the suggestion: Separate the roadmap statement from the list of questions; preserve their exact scope.

### PR-088

**Accepted by inference** · weight 0 · Colon reduction · Chapter 8 · Overall Discussion · Chapter 8 › Answers to the Overarching Questions, `chapters/discussion.tex`, line 17

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-009, PR-011, PR-013, PR-015, PR-103, PR-106: Separate a complete claim, observation or role from its explanation or an independent clause, following the approved sentence splits without dispersing a numbered or detailed definition list.

Suggestion: Separate feedback association and correlations

Original:

~~~latex
Feedback accuracy was associated with the characteristics of the teacher: robot experience and educational background showed positive associations with feedback accuracy, with correlations of 0.25 and 0.16, respectively.
~~~

Accepted wording:

~~~latex
Feedback accuracy was associated with the characteristics of the teacher. Robot experience and educational background showed positive associations with feedback accuracy, with correlations of 0.25 and 0.16, respectively.
~~~

Note written with the suggestion: Separate the overall association from the two named correlations.

### PR-089

**Accepted by inference** · weight 0 · Colon reduction · Chapter 8 · Overall Discussion · Chapter 8 › Answers to the Overarching Questions, `chapters/discussion.tex`, line 20

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-009, PR-011, PR-013, PR-015, PR-103, PR-106: Separate a complete claim, observation or role from its explanation or an independent clause, following the approved sentence splits without dispersing a numbered or detailed definition list.

Suggestion: Separate the sidetrack finding and statistics

Original:

~~~latex
\hang{style start} Demonstration sidetracks made up about 48\% of the recorded timesteps, and they were task-related: 54.7\% of them occurred within windows around changes of task phase that cover 40\% of the timesteps, and 73\% of \textit{Alignment} behaviors started and ended within 0.1\,m of a target object (\autoref{ch:sidetracks}). \hang{style end}
~~~

Accepted wording:

~~~latex
Demonstration sidetracks made up about 48\% of the recorded timesteps, and they were task-related. Specifically, 54.7\% of them occurred within windows around changes of task phase that cover 40\% of the timesteps, and 73\% of \textit{Alignment} behaviors started and ended within 0.1\,m of a target object (\autoref{ch:sidetracks}).
~~~

Note written with the suggestion: Separate the task-related finding from the two quantitative examples. Preserve the window qualifier and all percentages.

### PR-090

**Accepted by inference** · weight 0 · Colon reduction · Chapter 8 · Overall Discussion · Chapter 8 › Answers to the Overarching Questions, `chapters/discussion.tex`, line 21

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-012, PR-104, PR-105, PR-107, PR-111: Integrate short unnumbered names, examples or activities into the existing sentence while retaining their order and scope, following the approved component and example integrations.

Suggestion: Integrate the three sources of structure

Original:

~~~latex
\hang{style start} Together, these findings suggest three sources of structure: the teacher, the demands of the task at a given moment, and the channel through which the teaching is given. \hang{style end}
~~~

Accepted wording:

~~~latex
Together, these findings suggest three sources of structure, namely the teacher, the demands of the task at a given moment, and the channel through which the teaching is given.
~~~

Note written with the suggestion: Integrate the three short sources with “namely”.

### PR-091

**Accepted by inference** · weight 0 · Colon reduction · Chapter 8 · Overall Discussion · Chapter 8 › Answers to the Overarching Questions, `chapters/discussion.tex`, line 44

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-009, PR-011, PR-013, PR-015, PR-103, PR-106: Separate a complete claim, observation or role from its explanation or an independent clause, following the approved sentence splits without dispersing a numbered or detailed definition list.

Suggestion: Separate the signal distinction and definitions

Original:

~~~latex
\hang{style start} Both approaches provide references for interpreting a teacher's values, but they describe different quantities: STEADY retains a judgment of quality, whereas \textit{progress} describes completion. \hang{style end}
~~~

Accepted wording:

~~~latex
Both approaches provide references for interpreting a teacher's values, but they describe different quantities. STEADY retains a judgment of quality, whereas \textit{progress} describes completion.
~~~

Note written with the suggestion: Separate the general distinction from the meanings of quality and completion.

### PR-092

**Accepted by inference** · weight 0 · Colon reduction · Chapter 8 · Overall Discussion · Chapter 8 › Answers to the Overarching Questions, `chapters/discussion.tex`, line 60

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-009, PR-011, PR-013, PR-015, PR-103, PR-106: Separate a complete claim, observation or role from its explanation or an independent clause, following the approved sentence splits without dispersing a numbered or detailed definition list.

Suggestion: Separate the completion-evidence limit and reasons

Original:

~~~latex
The evidence for this use is limited so far: most demonstrations in the evaluated datasets were annotated as complete, and removing the completion term did not reduce performance in the way that removing the other terms did (\autoref{ch:phirl}). \hang{create end}
~~~

Accepted wording:

~~~latex
The evidence for this use is limited so far. Most demonstrations in the evaluated datasets were annotated as complete, and removing the completion term did not reduce performance in the way that removing the other terms did (\autoref{ch:phirl}). \hang{create end}
~~~

Note written with the suggestion: Separate the evidence limit from the reasons for that limit, preserving the existing closing create marker.

### PR-093

**Accepted by inference** · weight 0 · Semicolon reduction · Chapter 8 · Overall Discussion · Chapter 8 › Findings That Connect the Chapters, `chapters/discussion.tex`, line 70

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-009, PR-011, PR-013, PR-015, PR-103, PR-106: Separate a complete claim, observation or role from its explanation or an independent clause, following the approved sentence splits without dispersing a numbered or detailed definition list.

Suggestion: Separate prediction accuracy and gains

Original:

~~~latex
In \autoref{ch:charm}, a model given only task statistics predicted whether feedback was positive or negative with an accuracy of 79.35\%, but predicted its value on the five-point scale with an accuracy of 32.59\%; adding the characteristics of the teacher raised the first figure by about 8 percentage points and the second by about 23.
~~~

Accepted wording:

~~~latex
In \autoref{ch:charm}, a model given only task statistics predicted whether feedback was positive or negative with an accuracy of 79.35\%, but predicted its value on the five-point scale with an accuracy of 32.59\%. Adding the characteristics of the teacher raised the first figure by about 8 percentage points and the second by about 23.
~~~

Note written with the suggestion: Give the baseline accuracies and the gains from human characteristics their own sentences; retain all figures.

### PR-094

**Declined by inference** · weight 0 · Colon reduction · Chapter 8 · Overall Discussion · Chapter 8 › Findings That Connect the Chapters, `chapters/discussion.tex`, line 72

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-108: Preserve the compact explanation after the colon; splitting also leaves It with a less direct antecedent.

Suggestion: Separate the binary-feedback interpretation and explanation

Original, which stayed:

~~~latex
These results offer one explanation of why binary feedback appears less noisy: it removes the part of the signal in which teachers differ most from one another.
~~~

Declined suggestion:

~~~latex
These results offer one explanation of why binary feedback appears less noisy. It removes the part of the signal in which teachers differ most from one another.
~~~

Note written with the suggestion: Separate the interpretive claim from its explanation.

### PR-095

**Accepted by inference** · weight 0 · Colon reduction · Chapter 8 · Overall Discussion · Chapter 8 › Findings That Connect the Chapters, `chapters/discussion.tex`, line 79

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-009, PR-011, PR-013, PR-015, PR-103, PR-106: Separate a complete claim, observation or role from its explanation or an independent clause, following the approved sentence splits without dispersing a numbered or detailed definition list.

Suggestion: Separate the common failure pattern and cases

Original:

~~~latex
\hang{style start} Most of the failed demonstrations in the public space study failed at similar kinds of steps: the jar was not grasped, or it was dropped while it was being carried (\autoref{ch:progress}). \hang{style end}
~~~

Accepted wording:

~~~latex
Most of the failed demonstrations in the public space study failed at similar kinds of steps. The jar was not grasped, or it was dropped while it was being carried (\autoref{ch:progress}).
~~~

Note written with the suggestion: Give the two recurring failure cases their own sentence.

### PR-096

**Accepted by inference** · weight 0 · Colon reduction · Chapter 8 · Overall Discussion · Chapter 8 › Findings That Connect the Chapters, `chapters/discussion.tex`, line 96

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-009, PR-011, PR-013, PR-015, PR-103, PR-106: Separate a complete claim, observation or role from its explanation or an independent clause, following the approved sentence splits without dispersing a numbered or detailed definition list.

Suggestion: Separate the VLM interpretation and outcome

Original:

~~~latex
\hang{style start} The formative study with a vision-language model (VLM) in \autoref{ch:phirl} is consistent with this interpretation: annotations generated by the VLM improved learning in most cases, while the improvement is less than using human annotations. \hang{style end}
~~~

Accepted wording:

~~~latex
The formative study with a vision-language model (VLM) in \autoref{ch:phirl} is consistent with this interpretation. Annotations generated by the VLM improved learning in most cases, while the improvement is less than using human annotations.
~~~

Note written with the suggestion: Separate the link to the interpretation from the VLM outcome, preserving the human-annotation comparison.

### PR-097

**Accepted by inference** · weight 0 · Colon reduction · Chapter 8 · Overall Discussion · Chapter 8 › What the Combined Evidence Does Not Yet Show, `chapters/discussion.tex`, line 106

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-009, PR-011, PR-013, PR-015, PR-103, PR-106: Separate a complete claim, observation or role from its explanation or an independent clause, following the approved sentence splits without dispersing a numbered or detailed definition list.

Suggestion: Separate the experimental gap and evaluation scope

Original:

~~~latex
No experiment had the same non-experts provide demonstrations and \textit{progress} annotations and then trained a robot on both: the simulated evaluations of PHIRL used Robomimic datasets collected by other operators, and its real-robot evaluation involved six demonstrators and two annotators (\autoref{ch:phirl}).
~~~

Accepted wording:

~~~latex
No experiment had the same non-experts provide demonstrations and \textit{progress} annotations and then trained a robot on both. The simulated evaluations of PHIRL used Robomimic datasets collected by other operators, and its real-robot evaluation involved six demonstrators and two annotators (\autoref{ch:phirl}).
~~~

Note written with the suggestion: Separate the missing end-to-end experiment from the dataset and participant differences.

### PR-098

**Accepted by inference** · weight 0 · Colon reduction · Chapter 8 · Overall Discussion · Chapter 8 › Future Work, `chapters/discussion.tex`, line 119

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-012, PR-104, PR-105, PR-107, PR-111: Integrate short unnumbered names, examples or activities into the existing sentence while retaining their order and scope, following the approved component and example integrations.

Suggestion: Integrate the future-work components

Original:

~~~latex
\hang{grammar start} This direction follows directly from the findings of this dissertation: actively selecting which demonstrations to annotate, extending the learning framework to enable learning from teaching modalities beyond human evaluative feedback and human demonstrations, examining the conclusions on a larger scale,  and extending the framework to be compatible with foundation models. \hang{grammar end}
~~~

Accepted wording:

~~~latex
This direction follows directly from the findings of this dissertation and includes actively selecting which demonstrations to annotate, extending the learning framework to enable learning from teaching modalities beyond human evaluative feedback and human demonstrations, examining the conclusions on a larger scale,  and extending the framework to be compatible with foundation models.
~~~

Note written with the suggestion: Use “includes” to connect the direction to its four components. Keep the original list and its scope.

### PR-099

**Declined by inference** · weight 0 · Colon and semicolon reduction · Chapter 8 · Overall Discussion · Chapter 8 › Future Work › Actively Sampling Demonstrations to Annotate, `chapters/discussion.tex`, line 137

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-010, PR-014: Keep the coordinated comparison strategies and the context attached to the random baseline, analogous to the declined rewrite of four cited uses.

Suggestion: Shorten the baseline-strategy list

Original, which stayed:

~~~latex
\hang{grammar start} The new selection strategy would be compared with several baseline strategies: random selection, as in \autoref{ch:phirl}; selecting low-quality demonstrations; selecting the demonstrations on which the learned reward model is most uncertain; selecting the demonstrations where the learned reward disagrees most with the current estimate of \textit{progress}; and selecting the highest-quality demonstrations. \hang{grammar end}
~~~

Declined suggestion:

~~~latex
The new selection strategy would be compared with several baseline strategies. One baseline would use random selection, as in \autoref{ch:phirl}. The other baselines would select low-quality demonstrations, demonstrations on which the learned reward model is most uncertain, demonstrations where the learned reward disagrees most with the current estimate of \textit{progress}, or the highest-quality demonstrations.
~~~

Note written with the suggestion: Separate the contextualized random baseline from the four remaining alternatives. Their descriptions contain no internal commas, so a comma list with “or” replaces four semicolons without suggesting that the strategies are combined.

### PR-100

**Accepted by inference** · weight 0 · Colon reduction · Chapter 8 · Overall Discussion · Chapter 8 › Future Work › Learning from More Modalities of Human Teaching, `chapters/discussion.tex`, line 151

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-012, PR-104, PR-105, PR-107, PR-111: Integrate short unnumbered names, examples or activities into the existing sentence while retaining their order and scope, following the approved component and example integrations.

Suggestion: Integrate the three feedback types

Original:

~~~latex
This dissertation studied two forms of human teaching, demonstrations and evaluative feedback, and three types of evaluative feedback: binary feedback, scalar feedback, and \textit{progress}.
~~~

Accepted wording:

~~~latex
This dissertation studied two forms of human teaching, demonstrations and evaluative feedback, and three types of evaluative feedback, namely binary feedback, scalar feedback, and \textit{progress}.
~~~

Note written with the suggestion: Integrate the three feedback types with “namely”.

### PR-101

**Accepted by inference** · weight 0 · Colon reduction · Chapter 8 · Overall Discussion · Chapter 8 › Future Work › Learning from More Modalities of Human Teaching, `chapters/discussion.tex`, line 155

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-009, PR-011, PR-013, PR-015, PR-103, PR-106: Separate a complete claim, observation or role from its explanation or an independent clause, following the approved sentence splits without dispersing a numbered or detailed definition list.

Suggestion: Separate foundation-model capability and examples

Original:

~~~latex
Foundation models have made several of these modalities newly practical for robot learning: for example, a language model can interpret optional free-text explanations that accompany preference queries \cite{holk2024predilect}, or infer a user's hidden preferences from changes in their demonstrations and ask the user when it is uncertain \cite{peng2024preference}.
~~~

Accepted wording:

~~~latex
Foundation models have made several of these modalities newly practical for robot learning. For example, a language model can interpret optional free-text explanations that accompany preference queries \cite{holk2024predilect}, or infer a user's hidden preferences from changes in their demonstrations and ask the user when it is uncertain \cite{peng2024preference}.
~~~

Note written with the suggestion: Separate the general claim from the two cited examples.

### PR-102

**Accepted by inference** · weight 0 · Colon reduction · Chapter 8 · Overall Discussion · Chapter 8 › Future Work › Learning from More Modalities of Human Teaching, `chapters/discussion.tex`, line 156

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-009, PR-011, PR-013, PR-015, PR-103, PR-106: Separate a complete claim, observation or role from its explanation or an independent clause, following the approved sentence splits without dispersing a numbered or detailed definition list.

Suggestion: Separate the reward-constraint analogy and examples

Original:

~~~latex
\hang{style start} Other modalities could be expressed as constraints on the learned reward, in the way that PHIRL uses \textit{progress}: comparisons constrain the ordering of trajectories, natural language instructions and rubrics \cite{gunjal2025rubrics, liu2025openrubrics} constrain which features of the task matter, and gaze indicates which objects a teacher attends to \cite{saran2020understanding}. \hang{style end}
~~~

Accepted wording:

~~~latex
Other modalities could be expressed as constraints on the learned reward, in the way that PHIRL uses \textit{progress}. Comparisons constrain the ordering of trajectories, natural language instructions and rubrics \cite{gunjal2025rubrics, liu2025openrubrics} constrain which features of the task matter, and gaze indicates which objects a teacher attends to \cite{saran2020understanding}.
~~~

Note written with the suggestion: Separate the framework analogy from the modality-specific constraints and gaze information.

### PR-103

**Accepted** · weight 1 · Colon reduction · Chapter 8 · Overall Discussion · Chapter 8 › Future Work › Learning from More Modalities of Human Teaching, `chapters/discussion.tex`, line 159

Suggestion: Separate the extension and proposed approach

Original:

~~~latex
\hang{grammar start} Thus, future work can consider extending new modalities while using an approach similar to that of this dissertation: first model how non-experts actually provide a modality and then design learning methods around the resulting models rather than around idealized assumptions. \hang{grammar end}
~~~

Accepted wording:

~~~latex
Thus, future work can consider extending new modalities while using an approach similar to that of this dissertation. This approach would first model how non-experts actually provide a modality and then design learning methods around the resulting models rather than around idealized assumptions.
~~~

Note written with the suggestion: Make the proposed two-step approach a separate sentence. Keep its future-work framing.

### PR-104

**Accepted** · weight 1 · Colon reduction · Chapter 8 · Overall Discussion · Chapter 8 › Future Work › Agentic Robotics, `chapters/discussion.tex`, line 185

Suggestion: Integrate the tool examples

Original:

~~~latex
A tool in this sense is anything that acts on the robot or on its data: a trained policy, a training pipeline, an evaluator, or a setup for collecting demonstrations.
~~~

Accepted wording:

~~~latex
A tool in this sense is anything that acts on the robot or on its data, such as a trained policy, a training pipeline, an evaluator, or a setup for collecting demonstrations.
~~~

Note written with the suggestion: Use “such as” to introduce examples of tools, preserving the broad definition.

Used in: [Few colons and semicolons](../hangs-writing-style-reference.md#few-colons-and-semicolons).

### PR-105

**Accepted** · weight 1 · Colon reduction · Chapter 8 · Overall Discussion · Chapter 8 › Future Work › Agentic Robotics, `chapters/discussion.tex`, line 195

Suggestion: Integrate the human intervention points

Original:

~~~latex
A person would remain in the loop at chosen points: giving feedback on an outcome, validating a change before it is kept, or adjusting a procedure that the agent follows.
~~~

Accepted wording:

~~~latex
A person would remain in the loop at chosen points by giving feedback on an outcome, validating a change before it is kept, or adjusting a procedure that the agent follows.
~~~

Note written with the suggestion: Use “by” to connect the person’s involvement to the three actions.

### PR-106

**Accepted** · weight 1 · Semicolon reduction · Chapter 8 · Overall Discussion · Chapter 8 › Future Work › Agentic Robotics, `chapters/discussion.tex`, line 199

Suggestion: Separate continuity and the higher teaching level

Original:

~~~latex
In agentic robotics, non-expert teaching does not disappear; it moves to a higher level, as people correct plans, evaluate outcomes, and demonstrate the steps that an agent gets wrong.
~~~

Accepted wording:

~~~latex
In agentic robotics, non-expert teaching does not disappear. It moves to a higher level, as people correct plans, evaluate outcomes, and demonstrate the steps that an agent gets wrong.
~~~

Note written with the suggestion: Separate the continuity of human teaching from the change in its level.

### PR-107

**Accepted** · weight 1 · Colon reduction · Chapter 8 · Overall Discussion · Chapter 8 › Future Work › Agentic Robotics, `chapters/discussion.tex`, line 200

Suggestion: Integrate the two trajectory levels

Original:

~~~latex
Human teaching would then provide a trajectory at a different level: not only the motion of the robot, but also the execution trajectory of the agent, that is, the sequence of plans, tool calls, outcomes, and human corrections recorded while a task is carried out.
~~~

Accepted wording:

~~~latex
Human teaching would then provide a trajectory at a different level, including not only the motion of the robot, but also the execution trajectory of the agent, that is, the sequence of plans, tool calls, outcomes, and human corrections recorded while a task is carried out.
~~~

Note written with the suggestion: Use “including” to integrate the two kinds of trajectory while retaining the agent-trajectory definition.

### PR-108

**Declined** · weight 3 · Colon reduction · Chapter 8 · Overall Discussion · Chapter 8 › Future Work › Agentic Robotics, `chapters/discussion.tex`, line 204

Suggestion: Separate the benefit and explanation

Original, which stayed:

~~~latex
The expected benefit of such a loop is operational: a person would not need to stay in the loop for every round.
~~~

Declined suggestion:

~~~latex
The expected benefit of such a loop is operational. A person would not need to stay in the loop for every round.
~~~

Note written with the suggestion: Separate the benefit category from the specific reduction in continuous involvement.

Used in: [Few colons and semicolons](../hangs-writing-style-reference.md#few-colons-and-semicolons).

### PR-109

**Accepted** · weight 1 · Colon reduction · Chapter 8 · Overall Discussion · Chapter 8 › Future Work › Agentic Robotics, `chapters/discussion.tex`, line 206

Suggestion: Separate the safety boundary and requirement

Original:

~~~latex
It is a narrower claim than choosing better than a person, and it is not a claim about safety: a real robot would still need safety interlocks that are independent of the agent.
~~~

Accepted wording:

~~~latex
It is a narrower claim than choosing better than a person, and it is not a claim about safety. A real robot would still need safety interlocks that are independent of the agent.
~~~

Note written with the suggestion: Give the independent-interlock requirement its own sentence; keep the boundary on the claim.

### PR-110

**Accepted** · weight 1 · Colon reduction · Chapter 8 · Overall Discussion · Chapter 8 › Future Work › Agentic Human-Robot Interaction, `chapters/discussion.tex`, line 214

Suggestion: Separate the planning condition and explanation

Original:

~~~latex
Planning is comparatively simple for a task that involves no interaction: the robot can assemble known skills and execute them in sequence.
~~~

Accepted wording:

~~~latex
Planning is comparatively simple for a task that involves no interaction. The robot can assemble known skills and execute them in sequence.
~~~

Note written with the suggestion: Separate the condition from the explanation of sequential skill execution.

Used in: [Few colons and semicolons](../hangs-writing-style-reference.md#few-colons-and-semicolons).

### PR-111

**Accepted** · weight 1 · Colon reduction · Chapter 8 · Overall Discussion · Chapter 8 › Future Work › Agentic Human-Robot Interaction, `chapters/discussion.tex`, line 230

Suggestion: Integrate the trajectory-format fields

Original:

~~~latex
One planned step is to propose a standard data format that records an interaction as a trajectory: who did what, in which order, and with what outcome.
~~~

Accepted wording:

~~~latex
One planned step is to propose a standard data format that records an interaction as a trajectory by specifying who did what, in which order, and with what outcome.
~~~

Note written with the suggestion: Use “by specifying” to connect the proposed format to the information it would record.

### PR-112

**Accepted by inference** · weight 0 · Semicolon reduction · Chapter 9 · Conclusion · Chapter 9, `chapters/conclusion.tex`, line 6

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-008: Split the three complete stage-summary clauses while preserving their references, like the approved multi-section roadmap. This keeps the original stage wording rather than recasting research questions.

Suggestion: Separate the three-stage conclusion

Original:

~~~latex
\hang{fix start} Following the three-stage architecture introduced in \autoref{ch:introduction}, public space studies were first conducted to understand the imperfections in non-expert feedback and demonstrations \hang{cross-ref start} (\autoref{ch:charm} and \autoref{ch:sidetracks}) \hang{cross-ref end}; noise in human feedback was then examined and mitigated by stabilizing scalar feedback and formalizing \textit{progress}, a signal that is under-explored as a human teaching signal \hang{cross-ref start} (\autoref{ch:steady} and \autoref{ch:progress}) \hang{cross-ref end}; and imperfect non-expert teaching was finally leveraged with PHIRL, a reward learning framework that aligns rewards learned from demonstrations with \textit{progress} annotations (\autoref{ch:phirl}). \hang{fix end}
~~~

Accepted wording:

~~~latex
Following the three-stage architecture introduced in \autoref{ch:introduction}, public space studies were first conducted to understand the imperfections in non-expert feedback and demonstrations \hang{cross-ref start} (\autoref{ch:charm} and \autoref{ch:sidetracks}) \hang{cross-ref end}. Noise in human feedback was then examined and mitigated by stabilizing scalar feedback and formalizing \textit{progress}, a signal that is under-explored as a human teaching signal \hang{cross-ref start} (\autoref{ch:steady} and \autoref{ch:progress}) \hang{cross-ref end}. Finally, imperfect non-expert teaching was leveraged with PHIRL, a reward learning framework that aligns rewards learned from demonstrations with \textit{progress} annotations (\autoref{ch:phirl}).
~~~

Note written with the suggestion: Give each of the three stages its own sentence, retaining all study and chapter references.

### PR-113

**Accepted by inference** · weight 0 · Colon reduction · Chapter 9 · Conclusion · Chapter 9, `chapters/conclusion.tex`, line 7

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-009, PR-011, PR-013, PR-015, PR-103, PR-106: Separate a complete claim, observation or role from its explanation or an independent clause, following the approved sentence splits without dispersing a numbered or detailed definition list.

Suggestion: Separate the discussion chapter and its coverage

Original:

~~~latex
\hang{opening start} \autoref{ch:discussion} considered the studies together: it answered the three questions behind these stages, described the findings that connect the chapters, identified what the combined evidence does not yet show, and outlined directions for future work. \hang{opening end}
~~~

Accepted wording:

~~~latex
\autoref{ch:discussion} considered the studies together. It answered the three questions behind these stages, described the findings that connect the chapters, identified what the combined evidence does not yet show, and outlined directions for future work.
~~~

Note written with the suggestion: Separate the chapter’s role from the list of what it covered.

### PR-114

**Accepted by inference** · weight 0 · Colon reduction · Chapter 9 · Conclusion · Chapter 9, `chapters/conclusion.tex`, line 10

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-012, PR-104, PR-105, PR-107, PR-111: Integrate short unnumbered names, examples or activities into the existing sentence while retaining their order and scope, following the approved component and example integrations.

Suggestion: Integrate the table contents

Original:

~~~latex
\autoref{tab:study-overview} summarizes the studies conducted in this dissertation: the task used in each study, the data that were collected, how the data were collected, and the number of participants recruited.
~~~

Accepted wording:

~~~latex
\autoref{tab:study-overview} summarizes the studies conducted in this dissertation, including the task used in each study, the data that were collected, how the data were collected, and the number of participants recruited.
~~~

Note written with the suggestion: Integrate the table’s four kinds of information with “including”.

### PR-115

**Accepted by inference** · weight 0 · Colon reduction · Chapter 9 · Conclusion · Chapter 9 › Summary of Contributions, `chapters/conclusion.tex`, line 82

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-105: Use parallel by phrases for the two mitigation actions, like the approved human-intervention sentence.

Suggestion: Integrate the two mitigation approaches

Original:

~~~latex
\hang{revise start} Building on this evidence, the second stage revealed the inconsistency of non-expert feedback and  mitigated it in two ways: stabilizing feedback after it is given, and  changing what teachers are asked to give. \hang{revise end}
~~~

Accepted wording:

~~~latex
Building on this evidence, the second stage revealed the inconsistency of non-expert feedback and  mitigated it in two ways, by stabilizing feedback after it is given and by changing what teachers are asked to give.
~~~

Note written with the suggestion: Use parallel “by” phrases to introduce the two mitigation approaches.

### PR-116

**Declined by inference** · weight 0 · Colon and semicolon reduction · Chapter 9 · Conclusion · Chapter 9 › Summary of Contributions, `chapters/conclusion.tex`, line 91

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-010, PR-001: Keep the detailed release list and its chapter links; the rewrite repeats release/includes and introduces new labels for the resources.

Suggestion: Separate the released resources

Original, which stayed:

~~~latex
\hang{grammar start} In addition to these primary contributions, all the studies produced data and code that are released to the research community: the feedback and questionnaire responses of 46 participants in a public space, with the code of CHARM (\autoref{ch:charm}); the sidetrack annotations of 40 non-expert demonstrations, with the accompanying annotation interface code (\autoref{ch:sidetracks});  40 non-expert demonstrations collected from 40 passersby, with the \textit{progress} and scalar feedback that their demonstrators gave (\autoref{ch:progress}); and the implementation of PHIRL (\autoref{ch:phirl}). \hang{grammar end}
~~~

Declined suggestion:

~~~latex
In addition to these primary contributions, all the studies produced data and code that are released to the research community. The CHARM release includes the feedback and questionnaire responses of 46 participants in a public space, with the code of CHARM (\autoref{ch:charm}). The Sidetracks release includes the sidetrack annotations of 40 non-expert demonstrations, with the accompanying annotation interface code (\autoref{ch:sidetracks}). The \textit{progress} release includes 40 non-expert demonstrations collected from 40 passersby, with the \textit{progress} and scalar feedback that their demonstrators gave (\autoref{ch:progress}). The implementation of PHIRL is also released (\autoref{ch:phirl}).
~~~

Note written with the suggestion: Give each released resource its own sentence. Preserve the counts and the connection between each release and its chapter.

### PR-117

**Declined by inference** · weight 0 · Colon reduction · Chapter 9 · Conclusion · Chapter 9 › Summary of Contributions, `chapters/conclusion.tex`, line 95

Decided by an assistant (inferred), not by Hang. Recorded reason: Inferred from PR-005, PR-108: Keep the emphatic concluding claim and its closely linked implication, consistent with retaining a compact explanatory colon.

Suggestion: Separate the closing conclusion and implication

Original, which stayed:

~~~latex
By modeling the systematic structure in the imperfections of non-expert feedback and demonstrations, stabilizing and enriching the feedback signals available to non-experts, and aligning learned rewards with human \textit{progress} annotations, this dissertation demonstrates that the imperfections in non-expert teaching need not be obstacles to robot learning: they can be understood, mitigated, and even leveraged. [HY: improvement end] \hang{created}
~~~

Declined suggestion:

~~~latex
By modeling the systematic structure in the imperfections of non-expert feedback and demonstrations, stabilizing and enriching the feedback signals available to non-experts, and aligning learned rewards with human \textit{progress} annotations, this dissertation demonstrates that the imperfections in non-expert teaching need not be obstacles to robot learning. They can be understood, mitigated, and even leveraged. [HY: improvement end] \hang{created}
~~~

Note written with the suggestion: Separate the dissertation-level conclusion from the closing statement of what can be done with imperfections. Preserve the existing trailing annotations.
