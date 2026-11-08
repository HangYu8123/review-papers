# Overall assessment review

Review `overall-assessment-review` of the dissertation, from `waiting_for_review/overall-assessment-review`. Decided between October 12, 2026 and October 12, 2026. Decisions files: `overall-assessment-review.decisions.20261012-214917.json`.

[All reviews](../review-decisions.md) · [Weighted signals](../preference-signals.md) · [Main reference](../hangs-writing-style-reference.md)

| Outcome | Decided by Hang | Not decided by Hang |
| --- | ---: | ---: |
| Accepted as suggested | 70 | 0 |
| Accepted with Hang's edit | 3 | 0 |
| Declined | 29 | 0 |
| Notes from Hang | 1 | |

14 of the 116 items had no decision when the review was imported.

**To check before the accepted wording is used**

- [OA-102](#oa-102). In the edited wording, the verb of the expected rewards of guessing is higher does not agree with rewards.

### OA-101

**Declined** · weight 3 · Grammar · Chapter 1 · Introduction · Chapter 1 › Overview, `chapters/introduction.tex`, line 11

Suggestion: First sentence of the dissertation: "which are usually achieved"

Original, which stayed:

~~~latex
The importance of developing robots that can adapt to individuals has long been recognized in the field of Human-Robot Interaction (HRI) \cite{macglashan2017interactive, fischer2013impact, zafari2019you, shim2016other}, which are usually achieved through human demonstrations \cite{cui2021empathic, arakawa2018dqn, ibarz2018reward} and  human evaluative feedback \cite{10.5555/2936924.2936990, vecerik2017leveraging, ning2022learning}.
~~~

Declined suggestion:

~~~latex
The importance of developing robots that can adapt to individuals has long been recognized in the field of Human-Robot Interaction (HRI) \cite{macglashan2017interactive, fischer2013impact, zafari2019you, shim2016other}, and such adaptation is usually achieved through human demonstrations \cite{cui2021empathic, arakawa2018dqn, ibarz2018reward} and human evaluative feedback \cite{10.5555/2936924.2936990, vecerik2017leveraging, ning2022learning}.
~~~

Note written with the suggestion: "Which are" has no plural noun to refer to. What is achieved through demonstrations and feedback is the adaptation. Only the connecting words change, and the three citation groups stay where they are.

Used in: [Correcting a sentence without rewording it](../hangs-writing-style-reference.md#correcting-a-sentence-without-rewording-it).

### OA-102

**Accepted with Hang's edit** · weight 4 · Claim matched to the evidence · Chapter 1 · Introduction · Chapter 1 › Overview, `chapters/introduction.tex`, line 26

Suggestion: What Kalai et al. claim about hallucination

Original:

~~~latex
Kalai et al.\ \cite{kalai2025language} indicate that binary evaluative feedback is the major reason that causes Large Language Models (LLMs) to hallucinate, and using scalar evaluative feedback or binary evaluative feedback with weights can reduce the problem.
~~~

Suggested:

~~~latex
Kalai et al.\ \cite{kalai2025language} argue that one reason Large Language Models (LLMs) hallucinate is that binary evaluation rewards guessing over acknowledging uncertainty, and that evaluations which penalize wrong answers with weights can reduce the problem.
~~~

Hang's wording:

~~~latex
Kalai et al.\ \cite{kalai2025language} argue that one reason Large Language Models (LLMs) hallucinate is that the expected rewards of guessing is higher than acknowledging uncertainty, and that using scalar evaluative feedback or binary evaluative feedback with weights can reduce the problem.
~~~

To check: In the edited wording, the verb of the expected rewards of guessing is higher does not agree with rewards.

Note written with the suggestion: As I read the paper (arXiv 2509.04664), it argues that language models hallucinate because training and evaluation reward guessing over acknowledging uncertainty, that binary (right or wrong) grading is the reason this persists, and that scoring which penalizes wrong answers would reduce it. It does not say that binary evaluative feedback is "the major reason", and it does not propose scalar feedback. The revision keeps your point, that binary evaluation loses something, in the strength the paper supports. Please check it against the paper, since this is my reading of it.

Used in: [Word choices made in review](../hangs-writing-style-reference.md#word-choices-made-in-review).

### OA-103

**Accepted** · weight 1 · Same fact, two wordings · Chapter 1 · Introduction · Chapter 1 › Overview, `chapters/introduction.tex`, line 34

Suggestion: Third stage: "utilizing" in the text, "Leveraging" in the title

Original:

~~~latex
\textit{utilizing complementary information from human feedback and demonstrations to achieve robust and data efficient robot learning}.
~~~

Accepted wording:

~~~latex
\textit{leveraging complementary information from human feedback and demonstrations to achieve robust and data efficient robot learning}.
~~~

Note written with the suggestion: The title names the stages Modeling, Mitigating and Leveraging. The first two italic phrases of this sentence start with "modeling" and "mitigating", and the third starts with "utilizing". One word changes, so that the three stages read the same on the title page, here, and in Chapters 7 and 9 ("leverages", "leveraged").

### OA-104

**Declined** · weight 3 · Same fact, two wordings · Chapter 1 · Introduction · Chapter 1 › Overview, `chapters/introduction.tex`, line 49

Suggestion: The third question is worded two ways (Chapter 1)

Original, which stayed:

~~~latex
Each stage addresses one question: whether the imperfections in non-expert teaching are random noise (\autoref{ch:charm} and \autoref{ch:sidetracks}); whether the inconsistency of non-expert feedback can be reduced while utilizing the magnitudes (\autoref{ch:steady} and \autoref{ch:progress}); and whether combining demonstrations and feedback can lower quality requirements for human teaching and reduce human effort in annotating (\autoref{ch:phirl}).
~~~

Declined suggestion:

~~~latex
Each stage addresses one question: whether the imperfections in non-expert teaching are random noise (\autoref{ch:charm} and \autoref{ch:sidetracks}); whether the inconsistency of non-expert feedback can be reduced while utilizing the magnitudes (\autoref{ch:steady} and \autoref{ch:progress}); and whether combining demonstrations and feedback can enable robust reward learning while reducing human effort in annotating (\autoref{ch:phirl}).
~~~

Note written with the suggestion: Chapter 1 and the opening of Chapter 8 ask whether combining demonstrations and feedback "can lower quality requirements for human teaching and reduce human effort in annotating". The question printed above its answer in Section 8.1 is the wording you typed in the connection review: "Can combining demonstrations and feedback enable robust reward learning while reducing human effort in annotating?". That wording also matches the aim stated in Chapter 7 ("to learn robust reward functions ... while reducing human engagement"), so this item and OA-801 bring the other two places to it. If you prefer the Chapter 1 wording, reject both and change the italic question in Section 8.1 instead.

Used in: [The three stage dissertation arc](../hangs-writing-style-reference.md#the-three-stage-dissertation-arc).

### OA-105

**Accepted** · weight 1 · Spelling · Chapter 1 · Introduction · Chapter 1 › Overview, `chapters/introduction.tex`, line 44

Suggestion: invesigate

Original:

~~~latex
A study was conducted to invesigate the consistency of human binary evaluative feedback and human scalar evaluative feedback, and
a heuristic method, STEADY, was proposed to mitigate inconsistency in human scalar evaluative feedback.
~~~

Accepted wording:

~~~latex
A study was conducted to investigate the consistency of human binary evaluative feedback and human scalar evaluative feedback, and
a heuristic method, STEADY, was proposed to mitigate inconsistency in human scalar evaluative feedback.
~~~

Note written with the suggestion: Spelling only.

### OA-106

**Accepted** · weight 1 · Spelling · Chapter 1 · Introduction · Chapter 1 › Overview, `chapters/introduction.tex`, line 46

Suggestion: noiser

Original:

~~~latex
Results suggest that human scalar evaluative feedback, while being noiser, can be more informative for learning if the magnitude information is properly used.
~~~

Accepted wording:

~~~latex
Results suggest that human scalar evaluative feedback, while being noisier, can be more informative for learning if the magnitude information is properly used.
~~~

Note written with the suggestion: Spelling only.

### OA-107

**Accepted** · weight 1 · Same fact, two wordings · Chapter 1 · Introduction · Chapter 1 › Noise beyond the Task, `chapters/introduction.tex`, line 73

Suggestion: "over 5000 pieces" of feedback, 4,655 in Chapter 3

Original:

~~~latex
A questionnaire with six selected domains was designed and used to collect over 5000 pieces of scalar evaluative feedback from 46 participants in a public space with simulated robots.
~~~

Accepted wording:

~~~latex
A questionnaire with six selected domains was designed and used to collect 4,655 pieces of scalar evaluative feedback from 46 participants in a public space with simulated robots.
~~~

Note written with the suggestion: Chapter 3 trains and evaluates on 4,655 data points, and your notes.txt says "Check charm feedback number". This uses the Chapter 3 number. If more than 5,000 pieces were collected and some were left out, for instance the prompts that timed out after 5 seconds, keep "over 5000" here and state the exclusion in Chapter 3 instead.

Used in: [Numbers and measured comparisons](../hangs-writing-style-reference.md#numbers-and-measured-comparisons).

### OA-108

**Declined** · weight 3 · Claim matched to the evidence · Chapter 1 · Introduction · Chapter 1 › Noise beyond the Task, `chapters/introduction.tex`, line 75

Suggestion: "fairly correlated" replaced by the correlations

Original, which stayed:

~~~latex
Results indicated that human evaluative feedback values are fairly correlated with human characteristics, especially with educational background and robot experience.
~~~

Declined suggestion:

~~~latex
Results indicated that robot experience and educational background showed positive associations with feedback accuracy, with correlations of 0.25 and 0.16, respectively.
~~~

Note written with the suggestion: This is the sentence you supplied on 2026-09-26 for the same claim ("report the actual r values"), and it is the wording of the Summary of Chapter 3 and of Section 8.1. The analysis correlated the characteristics with feedback accuracy, not with feedback values. "Results indicated that" is kept.

Used in: [Qualifying a result](../hangs-writing-style-reference.md#qualifying-a-result).

### OA-109

**Declined** · weight 3 · Same fact, two wordings · Chapter 1 · Introduction · Chapter 1 › Noise beyond the Task, `chapters/introduction.tex`, line 83

Suggestion: One definition of demonstration sidetracks (Chapter 1)

Original, which stayed:

~~~latex
Demonstration Sidetracks are defined as structured imperfections in human demonstrations.
~~~

Declined suggestion:

~~~latex
Demonstration Sidetracks are defined as non-optimal behaviors in human demonstrations.
~~~

Note written with the suggestion: The dissertation defines demonstration sidetracks in three ways: "structured imperfections" (here), "frequent and patterned non-optimal behaviors" (Section 4.1), and "non-optimal behaviors in human demonstrations" (Section 4.2.1, where the term is formally defined). When the definition already says "structured" or "patterned", the main finding of Chapter 4, that these behaviors are structured, is true by definition, and a committee member can ask what an unstructured sidetrack would be. The codebook does not require a behavior to be patterned. This item, OA-402 and OA-409 use the wording of Section 4.2.1 in the other places, so that "frequent" and "structured" are findings. The next sentences of this paragraph already report them as findings.

Used in: [Established dissertation terminology](../hangs-writing-style-reference.md#established-dissertation-terminology).

### OA-110

**Accepted** · weight 1 · Same fact, two wordings · Chapter 1 · Introduction · Chapter 1 › Noise beyond the Task, `chapters/introduction.tex`, line 87

Suggestion: "A codebook was used for open coding"

Original:

~~~latex
A codebook was used for open coding and for identifying demonstration sidetracks.
~~~

Accepted wording:

~~~latex
A codebook developed through open coding was used for identifying demonstration sidetracks.
~~~

Note written with the suggestion: A codebook is the result of open coding, not its tool. "A codebook developed through open coding" is the phrase you chose on 2026-09-26, and Chapter 4 uses it.

Used in: [Established dissertation terminology](../hangs-writing-style-reference.md#established-dissertation-terminology).

### OA-111

**Declined** · weight 3 · Same fact, two wordings · Chapter 1 · Introduction · Chapter 1 › Noise beyond the Task, `chapters/introduction.tex`, line 87

Suggestion: The definition of Mistake contradicts Chapter 4

Original, which stayed:

~~~latex
Four types of demonstration sidetracks that participants frequently exhibited when providing demonstrations were found: 1) Pause, no input from the controller for a period of time; 2) Alignment, moving the robot back-and-forth to align the robot with a target object; 3) Exploration, controlling multiple degrees of freedom of the robot and not contributing to task completion; 4) Mistake, non-harmful control errors that often last for a very short period of time.
~~~

Declined suggestion:

~~~latex
Four types of demonstration sidetracks that participants frequently exhibited when providing demonstrations were found: 1) Pause, no input from the controller for a period of time; 2) Alignment, moving the robot back-and-forth to align the robot with a target object; 3) Exploration, controlling multiple degrees of freedom of the robot and not contributing to task completion; 4) Mistake, a sequence of movements that makes no contribution to the completion of the task or harms it.
~~~

Note written with the suggestion: Here a Mistake is "non-harmful". The codebook in Chapter 4 says a Mistake "makes no contribution to the completion of the task or harms it". Only the fourth entry changes, and it uses the codebook's words.

Used in: [Established dissertation terminology](../hangs-writing-style-reference.md#established-dissertation-terminology).

### OA-112

**Declined** · weight 3 · Claim matched to the evidence · Chapter 1 · Introduction · Chapter 1 › Noise beyond the Task, `chapters/introduction.tex`, line 89

Suggestion: Pauses are the weakest example of sidetracks near a change of sub-task

Original, which stayed:

~~~latex
For instance, pauses are more likely to happen when subtasks are changed from one to another, and alignments are more likely to be found around the target objects.
~~~

Declined suggestion:

~~~latex
For instance, mistakes and explorations are more likely to happen when subtasks are changed from one to another, and alignments are more likely to be found around the target objects.
~~~

Note written with the suggestion: In Chapter 4, 59% of Mistake and 52% of Exploration happened within four seconds of a change of task phase, compared with 38% of Pause. The example names the type with the lowest figure. This names the two with the highest. See assessment.md on the chance level for these figures.

Not used in a pattern: Fact, logic, equation, or caption corrections that Hang declined. They are kept so that the same correction is not offered again without new information.

### OA-113

**Accepted** · weight 1 · Citation · Chapter 1 · Introduction · Chapter 1 › Towards Richer Human Evaluative Feedback, `chapters/introduction.tex`, line 99

Suggestion: More support for "binary feedback has been used in most of the RLHF methods"

Original:

~~~latex
Thus, binary evaluative feedback has been used in most of the RLHF methods as preferences or  evaluations \cite{griffith2013policy}.
~~~

Accepted wording:

~~~latex
Thus, binary evaluative feedback has been used in most of the RLHF methods as preferences or evaluations \cite{griffith2013policy, christiano2017deep, casper2023open}.
~~~

Note written with the suggestion: Item 6 of your notes.txt asks for more citations here, including the use in post-training of language models. Both added keys are already in references.bib. Christiano et al. is the standard reference for binary preference comparisons, and Casper et al. reviews RLHF as used for language models. Casper et al. is otherwise cited only in the Chapter 2 passage that was marked for deletion.

### OA-114

**Accepted** · weight 1 · Spelling · Chapter 1 · Introduction · Chapter 1 › Towards Richer Human Evaluative Feedback, `chapters/introduction.tex`, line 101

Suggestion: benefical

Original:

~~~latex
While scalar evaluative feedback can be more effective in these cases,
many interactive learning methods still favor binary evaluative feedback and view scalar evaluative feedback as unreliable, making it benefical to quantify the degree of scalar evaluative feedback inconsistency.
~~~

Accepted wording:

~~~latex
While scalar evaluative feedback can be more effective in these cases,
many interactive learning methods still favor binary evaluative feedback and view scalar evaluative feedback as unreliable, making it beneficial to quantify the degree of scalar evaluative feedback inconsistency.
~~~

Note written with the suggestion: Spelling only.

### OA-115

**Accepted** · weight 1 · Correction · Chapter 1 · Introduction · Chapter 1 › Towards Richer Human Evaluative Feedback, `chapters/introduction.tex`, line 109

Suggestion: "more than 18,000 pieces" is exactly 18,000

Original:

~~~latex
During the study,  more than 18,000 pieces of feedback from 90 participants were collected.
~~~

Accepted wording:

~~~latex
During the study, 18,000 pieces of feedback from 90 participants were collected.
~~~

Note written with the suggestion: 90 participants each gave feedback on 200 clips, which is 18,000. The study table in Chapter 9 says "18,000 in total".

Used in: [Numbers and measured comparisons](../hangs-writing-style-reference.md#numbers-and-measured-comparisons).

### OA-116

**Declined** · weight 3 · Claim matched to the evidence · Chapter 1 · Introduction · Chapter 1 › Towards Richer Human Evaluative Feedback, `chapters/introduction.tex`, line 113

Suggestion: STEADY was evaluated with one algorithm on one task

Original, which stayed:

~~~latex
The evaluation showed that interactive reinforcement learning algorithms can achieve higher performance with well-processed scalar evaluative feedback than with binary evaluative feedback.
~~~

Declined suggestion:

~~~latex
The evaluation showed that an interactive reinforcement learning algorithm, TAMER, achieved higher performance with scalar evaluative feedback processed by STEADY than with binary evaluative feedback in the evaluated task.
~~~

Note written with the suggestion: The sentence generalizes to "interactive reinforcement learning algorithms". Chapter 5 trained TAMER agents on the button-pressing task. Chapters 8 and 9 already say "in the evaluated task".

Used in: [Qualifying a result](../hangs-writing-style-reference.md#qualifying-a-result).

### OA-117

**Declined** · weight 3 · Correction · Chapter 1 · Introduction · Chapter 1 › Towards Richer Human Evaluative Feedback, `chapters/introduction.tex`, line 118

Suggestion: "The preceding chapters show" in Chapter 1

Original, which stayed:

~~~latex
The preceding chapters show that human evaluative feedback is affected by factors beyond the teaching task itself (\autoref{ch:charm}), and that human scalar evaluative feedback can be more effective if stabilized (\autoref{ch:steady}).
~~~

Declined suggestion:

~~~latex
The studies above show that human evaluative feedback is associated with factors beyond the teaching task itself (\autoref{ch:charm}), and that human scalar evaluative feedback can be more effective if stabilized (\autoref{ch:steady}).
~~~

Note written with the suggestion: Chapter 1 has no preceding chapters. The sentence refers to the two studies described above it. "Is affected by" becomes "is associated with", since Chapter 3 reports correlations.

Not used in a pattern: Fact, logic, equation, or caption corrections that Hang declined. They are kept so that the same correction is not offered again without new information.

### OA-118

**Accepted** · weight 1 · Correction · Chapter 1 · Introduction · Chapter 1 › Towards Richer Human Evaluative Feedback, `chapters/introduction.tex`, line 119

Suggestion: "human objective measurements"

Original:

~~~latex
This motivates the formalization of a teaching signal that better captures the imperfections in human demonstrations, is less affected by human objective measurements, and is more consistent across users.
~~~

Accepted wording:

~~~latex
This motivates the formalization of a teaching signal that better captures the imperfections in human demonstrations, is less affected by human subjective measurements, and is more consistent across users.
~~~

Note written with the suggestion: I read "objective" as a slip for "subjective": the paragraph goes on to say that the start and the end of the task give users references. If you meant something else, change the word with "Edit the wording".

### OA-119

**Accepted** · weight 1 · Claim matched to the evidence · Chapter 1 · Introduction · Chapter 1 › Towards Richer Human Evaluative Feedback, `chapters/introduction.tex`, line 123

Suggestion: Workload: no difference was detected

Original:

~~~latex
A first, small-scale online study showed that providing \textit{progress} to evaluate the robot's behavior does not require more workload from users compared to scalar evaluative feedback.
~~~

Accepted wording:

~~~latex
In a first, small-scale online study, no significant difference in workload was detected between providing \textit{progress} and providing scalar evaluative feedback to evaluate the robot's behavior.
~~~

Note written with the suggestion: Chapter 6 found no significant difference (p > 0.45, Bayes factors between 0.3 and 1). That is not the same as showing that no more workload is required. Chapters 6 (opening), 8 and 9 already use "no significant difference ... was detected". Style entry: Reporting a difference that was not detected.

Used in: [Qualifying a result](../hangs-writing-style-reference.md#qualifying-a-result).

### OA-120

**Accepted** · weight 1 · Correction · Chapter 1 · Introduction · Chapter 1 › Towards Richer Human Evaluative Feedback, `chapters/introduction.tex`, line 126

Suggestion: "evaluative scalar evaluative feedback"

Original:

~~~latex
Participants were asked to provide one demonstration and then provide both evaluative scalar evaluative feedback and \textit{progress} over the demonstration replays.
~~~

Accepted wording:

~~~latex
Participants were asked to provide one demonstration and then provide both scalar evaluative feedback and \textit{progress} over the demonstration replays.
~~~

Note written with the suggestion: A word left twice by the replacement of "scalar feedback" with "scalar evaluative feedback".

### OA-121

**Accepted** · weight 1 · Correction · Chapter 1 · Introduction · Chapter 1 › Towards Richer Human Evaluative Feedback, `chapters/introduction.tex`, line 130

Suggestion: "evaluative scalar feedback" and "evaluative scalar evaluative feedback"

Original:

~~~latex
The results indicated that evaluative \textbf{scalar feedback is indeed noisier than binary evaluative feedback, but can be more effective for reinforcement learning from human evaluative feedback if properly stabilized. } Moreover, this work demonstrates the benefits of \textit{progress} for non-experts, as \textit{progress} has multiple advantages for learning from non-experts compared to evaluative scalar evaluative feedback.
~~~

Accepted wording:

~~~latex
The results indicated that \textbf{scalar evaluative feedback is indeed noisier than binary evaluative feedback, but can be more effective for reinforcement learning from human evaluative feedback if properly stabilized. } Moreover, this work demonstrates the benefits of \textit{progress} for non-experts, as \textit{progress} has multiple advantages for learning from non-experts compared to scalar evaluative feedback.
~~~

Note written with the suggestion: The same leftover as OA-120, twice in this paragraph. Nothing else changes.

### OA-122

**Accepted with Hang's edit** · weight 4 · Grammar · Chapter 1 · Introduction · Chapter 1 › Progress-Heuristicized Inverse Reinforcement Learning, `chapters/introduction.tex`, line 147

Suggestion: "is that:" followed by a capital

Original:

~~~latex
The key intuition is that: \textit{Reward functions learned from demonstrations should align with the progress annotations of the demonstrations.}
~~~

Suggested:

~~~latex
The key intuition is that \textit{reward functions learned from demonstrations should align with the progress annotations of the demonstrations.}
~~~

Hang's wording:

~~~latex
The key intuition is that: \textit{reward functions learned from demonstrations should align with the progress annotations of the demonstrations.}
~~~

Note written with the suggestion: A colon after "that" breaks the clause. Chapter 7 writes the same sentence without it ("The key intuition is that \textbf{the rewards inferred ...}").

Used in: [Few colons and semicolons](../hangs-writing-style-reference.md#few-colons-and-semicolons).

### OA-123

**Declined** · weight 3 · Claim matched to the evidence · Chapter 1 · Introduction · Chapter 1 › Progress-Heuristicized Inverse Reinforcement Learning, `chapters/introduction.tex`, line 153

Suggestion: "significantly outperforms IRL baselines" (Chapter 1)

Original, which stayed:

~~~latex
The results show that PHIRL significantly outperforms IRL baselines with only 20\% of demonstrations being annotated offline, and the online extension of PHIRL is effective with VLM-generated annotations.
~~~

Declined suggestion:

~~~latex
The results show that PHIRL obtains higher returns than all four baselines with only 20\% of demonstrations being annotated offline, and the online extension of PHIRL is effective with VLM-generated annotations.
~~~

Note written with the suggestion: Three things in Chapter 7 limit "significantly". Each condition was trained once, and the chapter says the rollouts "do not establish variability across independent training runs". The tests are over evaluation rollouts of one trained model. The statistics of an earlier version of the paper, still in a comment in phirl.tex, give p = 0.26 against AIRLPref in Lift (PH). Chapters 8 and 9 already say "obtained higher returns than all four baselines" and "outperformed four baselines". This item and OA-703, OA-713 and OA-722 use that wording in the four places that still say "significantly".

Used in: [Qualifying a result](../hangs-writing-style-reference.md#qualifying-a-result).

### OA-124

**Accepted** · weight 1 · New text · Chapter 1 · Introduction · Chapter 1 › Contributions, `chapters/introduction.tex`, line 170

Suggestion: The second contribution in the list is empty

Original:

~~~latex
\item
\item An algorithm that mitigates noise in human scalar evaluative feedback
~~~

Accepted wording:

~~~latex
\item A categorization of four types of demonstration sidetracks in non-expert demonstrations, which are \textit{Exploration}, \textit{Mistake}, \textit{Alignment}, and \textit{Pause}, with evidence that they are frequent and are associated with the task both temporally and spatially.
    \item An algorithm that mitigates noise in human scalar evaluative feedback
~~~

Note written with the suggestion: Your note "add identified four demonstration sidetracks here" was removed with the tags, and an empty \item is left, which prints a "2." with nothing after it. This fills it from the Summary of Chapter 4 ("Four categories of demonstration sidetracks and one control pattern were identified ... frequent, associate with the task both temporally and spatially"), in the form of your other entries. The next entry is quoted only so that the place is found. RB-18 proposed nearly the same text, but it quotes the removed note and can no longer be applied.

### OA-201

**Accepted** · weight 1 · Correction · Chapter 2 · Background · Chapter 2, `chapters/background.tex`, line 6

Suggestion: "literature relative to"

Original:

~~~latex
Additionally, this chapter summarizes literature relative to the core technical domains in this dissertation, including modeling human feedback dynamics, learning from non-optimal demonstrations, and reward learning methods.
~~~

Accepted wording:

~~~latex
Additionally, this chapter summarizes literature relevant to the core technical domains in this dissertation, including modeling human feedback dynamics, learning from non-optimal demonstrations, and reward learning methods.
~~~

Note written with the suggestion: The word is "relevant", as in the first sentence of the chapter ("reviews relevant literature").

### OA-202

**Accepted** · weight 1 · Correction · Chapter 2 · Background · Chapter 2 › Summary, `chapters/background.tex`, line 231

Suggestion: The second motivation starts in lower case

Original:

~~~latex
interactive learning methods prefer binary feedback.
~~~

Accepted wording:

~~~latex
Many interactive learning methods prefer binary feedback.
~~~

Note written with the suggestion: The second entry of the list starts with a lower-case word and without a subject for "prefer" that fits the other entries. "Many interactive learning methods favor binary feedback" is the wording you chose on 2026-09-26, with "prefer" kept as you wrote it here.

### OA-203

**Accepted** · weight 1 · Grammar · Chapter 2 · Background · Chapter 2 › Summary, `chapters/background.tex`, line 235

Suggestion: "does not assume that A, that B, and that C"

Original:

~~~latex
This dissertation does not assume that human feedback is consistent, that behaviors in demonstrations are always optimal or contribute to task completion, and that human-in-the-loop effort is always available.
~~~

Accepted wording:

~~~latex
This dissertation does not assume that human feedback is consistent, that behaviors in demonstrations are always optimal or contribute to task completion, or that human-in-the-loop effort is always available.
~~~

Note written with the suggestion: After "does not assume", the three things are alternatives, so the last one takes "or". One word changes.

### OA-301

**Accepted** · weight 1 · Passage you marked [HY: improvement] · Chapter 3 · CHARM · Chapter 3, `chapters/charm.tex`, line 54

Suggestion: The "first work" claim between your improvement markers (Chapter 3)

Original:

~~~latex
[HY: improvement start] While it is well-established that human feedback patterns can vary among individuals \cite{christiano2017deep} (see also \autoref{ch:steady}), to the best of the author's knowledge, this is the first work that systematically investigated how human characteristics are associated with human feedback and leveraged human characteristics to predict human teaching signals. [HY: improvement end]
~~~

Accepted wording:

~~~latex
While it is well-established that human feedback patterns can vary among individuals \cite{christiano2017deep} (see also \autoref{ch:steady}), few studies have examined how human characteristics are associated with human feedback. This chapter systematically investigates this association and leverages human characteristics to predict human teaching signals.
~~~

Note written with the suggestion: The two markers print in the PDF as plain text, so they have to go whatever you decide about the sentence. A "first work" claim invites a committee member to name a counterexample, and a commented sentence in this file already cites one study of factors beyond the task (huang2024modeling). The revision says what the chapter does and leaves the ranking out. Your words are kept, and the sentence is split at the claim. To keep the claim, use "Edit the wording" and delete only the two markers.

Used in: [Contribution statements](../hangs-writing-style-reference.md#contribution-statements).

### OA-302

**Accepted** · weight 1 · Grammar · Chapter 3 · CHARM · Chapter 3 › Study Design, `chapters/charm.tex`, line 71

Suggestion: Two clauses joined by a comma

Original:

~~~latex
This chapter argues that human feedback does not solely rely on tasks or robot behaviors, it also depends on the human teachers themselves.
~~~

Accepted wording:

~~~latex
This chapter argues that human feedback does not solely rely on tasks or robot behaviors, but also depends on the human teachers themselves.
~~~

Note written with the suggestion: The semicolon between the two clauses was replaced by a comma, which leaves two sentences run together. "But" joins them and is the usual partner of "not solely".

### OA-303

**Accepted** · weight 1 · Same fact, two wordings · Chapter 3 · CHARM · Chapter 3 › Study Design › Considering Human Attributes for Reinforcement Modeling, `chapters/charm.tex`, line 133

Suggestion: A "trajectory" is 30 state-action pairs here and 500 to 800 steps in the Procedure

Original:

~~~latex
The length of a robot trajectory was fixed to 30 state-action pairs.
The accumulative reward over a trajectory $\sigma$ can be calculated as
~~~

Accepted wording:

~~~latex
Feedback was collected on trajectory segments with a fixed length of 30 state-action pairs.
The accumulative reward over a segment $\sigma$ can be calculated as
~~~

Note written with the suggestion: Section 3.2.3 says "For each trajectory, which comprised approximately 500 to 800 steps" and "The robot paused every 30 actions to prompt for feedback". The 30 pairs are therefore the part of a trajectory that one piece of feedback covers. "Segment" is the word Chapters 6 to 8 use for such a part.

### OA-304

**Accepted** · weight 1 · Correction · Chapter 3 · CHARM · Chapter 3 › Study Design › Considering Human Attributes for Reinforcement Modeling, `chapters/charm.tex`, line 163

Suggestion: "detailed in 1": the algorithm reference prints without its name

Original:

~~~latex
The training protocol is detailed in \autoref{alg:training_protocol}.
~~~

Accepted wording:

~~~latex
The training protocol is detailed in Algorithm \autoref{alg:training_protocol}.
~~~

Note written with the suggestion: \autoref has no name for algorithms in this document, so the PDF prints "The training protocol is detailed in 1." Chapters 5 and 7 write the word in front ("Algorithm \autoref{alg:STEADY}"), and this does the same.

### OA-305

**Accepted** · weight 1 · Claim matched to the evidence · Chapter 3 · CHARM · Chapter 3 › Results, `chapters/charm.tex`, line 229

Suggestion: "fairly correlated" at the start of the Results

Original:

~~~latex
The analysis shows that robot experience and educational background are fairly correlated with feedback accuracy and feedback values.
~~~

Accepted wording:

~~~latex
The analysis shows positive associations of robot experience and educational background with feedback accuracy, with correlations of 0.25 and 0.16, respectively.
~~~

Note written with the suggestion: As OA-108. The numbers are from Section 3.3.2, and the wording is the one in the Summary of this chapter. "Feedback values" is dropped because the two measures analyzed are feedback accuracy and the absolute difference.

Used in: [Qualifying a result](../hangs-writing-style-reference.md#qualifying-a-result).

### OA-306

**Accepted** · weight 1 · Restored from your paper or comments · Chapter 3 · CHARM · Chapter 3 › Results › Collected Human Feedback and Questionnaire Responses, `chapters/charm.tex`, line 247

Suggestion: Feedback accuracy is computed against something the text does not name

New text, placed next to this passage:

~~~latex
Feedback accuracy was computed for each participant by considering \(\{-2, -1\}\) as negative, \(\{1, 2\}\) as positive, and \(\{0\}\) as neutral.
~~~

Accepted wording:

~~~latex
The reward was discretized by partitioning its range into five equal segments, corresponding to the feedback value set \(\{-2, -1, 0, 1, 2\}\), and feedback was compared with the discretized reward.
~~~

Note written with the suggestion: The text says how feedback values were grouped into negative, neutral and positive, and then reports an accuracy of 51.79%, without saying what the feedback is compared with. The sentence that says it is in a comment two lines above ("We discretized the reward by partitioning its range into five equal segments ..."). This restores it in the impersonal voice. If accuracy was computed in another way, please say so here, since every correlation in Section 3.3.2 depends on this measure.

Used in: [Adding sentences that were not asked for](../hangs-writing-style-reference.md#adding-sentences-that-were-not-asked-for).

### OA-307

**Declined** · weight 3 · Correction · Chapter 3 · CHARM · Chapter 3 › Results › Collected Human Feedback and Questionnaire Responses, `chapters/charm.tex`, line 249

Suggestion: An empty box left inside the correlation equation

Original, which stayed:

~~~latex
\approx 0.563, p < 0.001\text{\parbox[c]{1.1in}{\raggedright}}; \quad \rho_{r,\text{delay}} \approx -0.004, p = 0.769\text{}.
~~~

Declined suggestion:

~~~latex
\approx 0.563, p < 0.001; \quad \rho_{r,\text{delay}} \approx -0.004, p = 0.769.
~~~

Note written with the suggestion: When the tags were removed, the wrappers that held a deletion note inside this equation stayed behind: an empty \parbox of 1.1 inches and an empty \text{}. They print as a blank gap in the middle of the equation. This removes the two wrappers and changes no number.

Not used in a pattern: Fact, logic, equation, or caption corrections that Hang declined. They are kept so that the same correction is not offered again without new information.

### OA-308

**Declined** · weight 3 · Correction · Chapter 3 · CHARM · Chapter 3 › Results › Including Human Characteristics Improves Feedback Prediction Accuracy, `chapters/charm.tex`, line 319

Suggestion: The procedure described is repeated random splitting, not k-fold cross-validation

Original, which stayed:

~~~latex
K-fold cross-validation (here, k=10) was performed by randomly splitting the \(4655 \) data points into 90\% training and 10\% validation sets, with a new random seed every time.
~~~

Declined suggestion:

~~~latex
Ten random splits were performed, each of which randomly split the \(4655 \) data points into 90\% training and 10\% validation sets with a new random seed.
~~~

Note written with the suggestion: In k-fold cross-validation the data is divided once into k parts and each part is the validation set once. The sentence describes a new random 90/10 split with a new seed each time, which is ten repeated random splits. A committee member who works with statistics will notice the difference. If the code does divide the data once into ten folds, reject this and delete "with a new random seed every time" instead.

Not used in a pattern: Fact, logic, equation, or caption corrections that Hang declined. They are kept so that the same correction is not offered again without new information.

### OA-309

**Declined** · weight 3 · Correction · Chapter 3 · CHARM · Chapter 3 › Results › Including Human Characteristics Improves Feedback Prediction Accuracy, `chapters/charm.tex`, line 336

Suggestion: The caption says "10-fold cross-validation"

Original, which stayed:

~~~latex
Each bar represents the average accuracy across a 10-fold cross-validation.
~~~

Declined suggestion:

~~~latex
Each bar represents the average accuracy across the ten random splits.
~~~

Note written with the suggestion: Follows OA-308. Accept or reject the two together.

Not used in a pattern: Fact, logic, equation, or caption corrections that Hang declined. They are kept so that the same correction is not offered again without new information.

### OA-310

**Declined** · weight 3 · Scope or limitation stated · Chapter 3 · CHARM · Chapter 3 › Discussion, `chapters/charm.tex`, line 374

Suggestion: With a random split, the characteristics can identify the participant

New text, placed next to this passage:

~~~latex
These results show that including human characteristics improves the prediction of feedback from teachers represented in the training data, but not whether CHARM generalizes to new teachers.
~~~

Declined suggestion:

~~~latex
Because the characteristics of a participant can also identify that participant in such a split, part of the improvement may come from learning how individual participants rate.
~~~

Note written with the suggestion: This is the question I would expect first on Chapter 3. The limitation paragraph says that the same participants are in the training and validation sets. It does not say why that matters for the main result: the characteristics of each of the 46 participants form a vector that is nearly unique, so a model can use it to recognize a participant and learn how that person rates, without learning anything about the characteristics. Stating it yourself is stronger than being asked. The sentence follows the form "Because [design choice], [result] may ..." of the style entry Limitations and future work, and it adds no result.

Used in: [Limitations and future work](../hangs-writing-style-reference.md#limitations-and-future-work), [Adding sentences that were not asked for](../hangs-writing-style-reference.md#adding-sentences-that-were-not-asked-for).

### OA-401

**Accepted** · weight 1 · Correction · Chapter 4 · Demonstration Sidetracks · Chapter 4 › Introduction, `chapters/sidetracks.tex`, line 32

Suggestion: "However, Few works"

Original:

~~~latex
However, Few works have studied patterns in non-experts' behavior when giving demonstrations.
~~~

Accepted wording:

~~~latex
However, few works have studied patterns in non-experts' behavior when giving demonstrations.
~~~

Note written with the suggestion: The capital was right when "However," was marked for deletion. The mark was removed and the word stayed, so the sentence now has a capital in the middle.

### OA-402

**Declined** · weight 3 · Same fact, two wordings · Chapter 4 · Demonstration Sidetracks · Chapter 4 › Introduction, `chapters/sidetracks.tex`, line 46

Suggestion: One definition of demonstration sidetracks (Section 4.1)

Original, which stayed:

~~~latex
The frequent and patterned non-optimal behaviors that non-experts performed while demonstrating are closely defined as \textit{\thingname{}}.
~~~

Declined suggestion:

~~~latex
The non-optimal behaviors that non-experts performed while demonstrating are defined as \textit{\thingname{}}.
~~~

Note written with the suggestion: See OA-109. Section 4.2.1 defines the term as "non-optimal behaviors in human demonstrations". This sentence adds "frequent and patterned" to the definition, which makes the finding of the chapter true by definition. The two words are taken out here, and the following sentences still report that the behaviors are frequent and not randomly distributed.

Used in: [Established dissertation terminology](../hangs-writing-style-reference.md#established-dissertation-terminology).

### OA-403

**Accepted** · weight 1 · Passage you marked [HY: improvement] · Chapter 4 · Demonstration Sidetracks · Chapter 4 › Introduction, `chapters/sidetracks.tex`, line 58

Suggestion: The "first work" claim between your improvement markers (Chapter 4)

Original:

~~~latex
[HY: improvement start] To the best of the author's knowledge, this is the first work that systematically characterizes non-experts' non-optimal manipulation patterns when providing demonstrations. [HY: improvement end]
~~~

Accepted wording:

~~~latex
This chapter systematically characterizes non-experts' non-optimal manipulation patterns when providing demonstrations.
~~~

Note written with the suggestion: As OA-301. The markers print in the PDF. The paragraph before the figure already says "few works have studied patterns in non-experts' behavior when giving demonstrations", so this sentence can say what the chapter provides. To keep the claim, use "Edit the wording" and delete only the two markers.

Used in: [Contribution statements](../hangs-writing-style-reference.md#contribution-statements).

### OA-404

**Accepted** · weight 1 · Correction · Chapter 4 · Demonstration Sidetracks · Chapter 4 › Methodology › Experiment Setup, `chapters/sidetracks.tex`, line 100

Suggestion: "six sub-tasks", seven listed

Original:

~~~latex
The task consisted of six sub-tasks, namely move down to jar, approach jar, grasp jar, lift jar, move to ice cream cup, approach ice cream cup, and pour.
~~~

Accepted wording:

~~~latex
The task consisted of seven sub-tasks, namely move down to jar, approach jar, grasp jar, lift jar, move to ice cream cup, approach ice cream cup, and pour.
~~~

Note written with the suggestion: The sentence lists seven sub-tasks, and the Results list the same seven task phases. The published paper has the same sentence. If two of the listed steps are one sub-task, merge them in the list instead and keep "six".

### OA-405

**Accepted** · weight 1 · Correction · Chapter 4 · Demonstration Sidetracks · Chapter 4 › Results, `chapters/sidetracks.tex`, line 181

Suggestion: "Exploratory actions were manually annotated"

Original:

~~~latex
Exploratory actions were manually annotated by replaying 40 real-world robot demonstrations from non-expert demonstrators in simulation according to the codebook developed through open coding.
~~~

Accepted wording:

~~~latex
\ThingName{} were annotated by replaying 40 real-world robot demonstrations from non-expert demonstrators in simulation according to the codebook developed through open coding.
~~~

Note written with the suggestion: Exploration is one of the four types, and the sentence is about all of them. "Manually" is dropped because Section 4.2.5 says "All pauses were automatically annotated by a script".

### OA-406

**Accepted** · weight 1 · Same fact, two wordings · Chapter 4 · Demonstration Sidetracks · Chapter 4 › Results › Demonstration Sidetracks are frequent in demonstrations, `chapters/sidetracks.tex`, line 190

Suggestion: 33 successful demonstrations here, 34 in Chapters 1 and 6

Original:

~~~latex
While 33 out of 40 non-expert participants successfully demonstrated the task, the average number of \thingname{} is $14.48 \pm 10.54$ per participant.
~~~

Accepted wording:

~~~latex
While 34 out of 40 non-expert participants successfully demonstrated the task, the average number of \thingname{} is $14.48 \pm 10.54$ per participant.
~~~

Note written with the suggestion: Chapters 1 and 6 say that 34 of the 40 demonstrations succeeded, and Chapter 6 counts six failed demonstrations, which adds up to 40. The two published papers differ in the same way. This uses 34. If the annotators of this chapter counted one demonstration differently, keep 33 and say which criterion was used.

### OA-407

**Accepted** · weight 1 · Correction · Chapter 4 · Demonstration Sidetracks · Chapter 4 › Results › Alignment happens more when accuracy is required for controlling the robot, `chapters/sidetracks.tex`, line 224

Suggestion: "Among these, 40%": the two shares add up to the 73%

Original:

~~~latex
Among these, 40\% of \textit{Alignment} behaviors started and ended near the jars, and 33\% of all alignment behaviors happened near the ice cream cup, which was the target for the pouring task.
~~~

Accepted wording:

~~~latex
Of all \textit{Alignment} behaviors, 40\% started and ended near the jars, and 33\% happened near the ice cream cup, which was the target for the pouring task.
~~~

Note written with the suggestion: 40% and 33% add up to 73%, so they are shares of all Alignment behaviors, not of the 73%. "Among these" says the second.

### OA-408

**Accepted** · weight 1 · Claim matched to the evidence · Chapter 4 · Demonstration Sidetracks · Chapter 4 › Discussion, `chapters/sidetracks.tex`, line 248

Suggestion: "are often intentional"

Original:

~~~latex
These imperfections usually have distinct patterns, are often intentional, and are associated with the control interface, which can cause real-world human demonstrations to differ from machine-generated demonstrations.
~~~

Accepted wording:

~~~latex
These imperfections usually have distinct patterns, may be intentional, and are associated with the control interface, which can cause real-world human demonstrations to differ from machine-generated demonstrations.
~~~

Note written with the suggestion: The study recorded what demonstrators did, not what they intended. Section 4.2 itself says "intentionally or subconsciously". "May be" keeps the idea without stating a frequency that was not measured. Style entry: Describing human teaching without blame ("without attributing unmeasured motives").

Used in: [Qualifying a result](../hangs-writing-style-reference.md#qualifying-a-result).

### OA-409

**Accepted** · weight 1 · Same fact, two wordings · Chapter 4 · Demonstration Sidetracks · Chapter 4 › Discussion, `chapters/sidetracks.tex`, line 249

Suggestion: One definition of demonstration sidetracks (Discussion of Chapter 4)

Original:

~~~latex
These meaningful or patterned imperfections are defined as \thingname{}.
~~~

Accepted wording:

~~~latex
These imperfections are the \thingname{} defined in this chapter.
~~~

Note written with the suggestion: See OA-109. This sentence defines the term a third time, now as "meaningful or patterned imperfections". The revision refers to the term already defined in Section 4.2.1.

### OA-410

**Accepted** · weight 1 · Scope or limitation stated · Chapter 4 · Demonstration Sidetracks · Chapter 4 › Discussion, `chapters/sidetracks.tex`, line 262

Suggestion: One control interface

Original:

~~~latex
One limitation of this chapter is that it only used demonstrations from one task and one robot.
~~~

Accepted wording:

~~~latex
One limitation of this chapter is that it only used demonstrations from one task, one robot, and one control interface. With a single interface, the tendency to control one dimension at a time cannot be separated from the design of that interface.
~~~

Note written with the suggestion: The chapter says that the control interface "affected" how participants controlled the robot, and Chapter 8 names the interface as a source of structure. All 40 demonstrations used the same controller, so the study cannot compare interfaces. Saying so here answers the question before it is asked. Your sentence is kept and gains three words, and one sentence follows it.

Used in: [Limitations and future work](../hangs-writing-style-reference.md#limitations-and-future-work).

### OA-411

**Declined** · weight 3 · Scope or limitation stated · Chapter 4 · Demonstration Sidetracks · Chapter 4 › Discussion, `chapters/sidetracks.tex`, line 263

Suggestion: No agreement statistic for the annotations

New text, placed next to this passage:

~~~latex
Even though the task covered a range of sub-tasks, including picking, grasping, and pouring, the work would benefit from including non-manipulation tasks.
~~~

Declined suggestion:

~~~latex
In addition, the annotations were crosschecked by a third expert, but an agreement statistic between the annotators is not reported.
~~~

Note written with the suggestion: A comment from your adviser in this file asks "coder agreement?", and the text has no answer. If you have a number, for instance the portion of the first annotations that the third expert confirmed, put it in Section 4.2.5 and reject this. If not, one sentence here states the limit. It says only what the text shows: no statistic is reported.

Used in: [Limitations and future work](../hangs-writing-style-reference.md#limitations-and-future-work), [Adding sentences that were not asked for](../hangs-writing-style-reference.md#adding-sentences-that-were-not-asked-for).

### OA-501

**Accepted** · weight 1 · Correction · Chapter 5 · From “Thumbs Up” to “10 out of 10” · Chapter 5 › Introduction, `chapters/steady.tex`, line 21

Suggestion: The Introduction of Chapter 5 now opens with the same sentence twice

Original:

~~~latex
Interactive Reinforcement Learning is a method that reduces data needs and improves learning efficiency by having a human-in-the-loop providing \emph{evaluative feedback} to an agent during learning.
In interactive reinforcement learning, a human provides \emph{evaluative feedback} to an agent during learning (\autoref{sec:RW}).
~~~

Accepted wording:

~~~latex
Interactive Reinforcement Learning is a method that reduces data needs and improves learning efficiency by having a human-in-the-loop providing \emph{evaluative feedback} to an agent during learning (\autoref{sec:RW}).
~~~

Note written with the suggestion: The first sentence was marked for deletion and the second was written to replace it. The marks were removed and both stayed, so the section says the same thing twice in a row. This keeps your sentence and moves the reference to Section 2.3 into it.

### OA-502

**Accepted** · weight 1 · Passage you marked [HY: improvement] · Chapter 5 · From “Thumbs Up” to “10 out of 10” · Chapter 5 › Introduction, `chapters/steady.tex`, line 94

Suggestion: The "first work" claim between your improvement markers (Chapter 5, the study)

Original:

~~~latex
[HY: improvement start] To the best of the author's knowledge, this is the first work that quantifies feedback dynamics in binary feedback and scalar feedback, indicating that feedback dynamics within individuals and between participants should be taken into consideration while using both binary feedback and scalar feedback. [HY: improvement end]
~~~

Accepted wording:

~~~latex
This chapter quantifies feedback dynamics in binary feedback and scalar feedback, and the results indicate that feedback dynamics within individuals and between participants should be taken into consideration while using both binary feedback and scalar feedback.
~~~

Note written with the suggestion: As OA-301. The markers print in the PDF. The revision keeps your words and removes the ranking. To keep the claim, use "Edit the wording" and delete only the two markers.

Used in: [Contribution statements](../hangs-writing-style-reference.md#contribution-statements).

### OA-503

**Accepted** · weight 1 · Passage you marked [HY: improvement] · Chapter 5 · From “Thumbs Up” to “10 out of 10” · Chapter 5 › Introduction, `chapters/steady.tex`, line 95

Suggestion: The "first algorithm" claim between your improvement markers (Chapter 5, STEADY)

Original:

~~~latex
[HY: improvement start] STEADY is the first algorithm that enables binary-feedback-based algorithms to learn from
%\elaine{does it have to be positive-valued? if not i would move this thought to the end of the sentence (see next note)}
scalar rewards
%\elaine{(see previous note)}
 even when those rewards do not have a clear division into positive and negative. [HY: improvement end]
~~~

Accepted wording:

~~~latex
STEADY enables binary-feedback-based algorithms to learn from scalar rewards even when those rewards do not have a clear division into positive and negative.
~~~

Note written with the suggestion: As OA-301. The markers print in the PDF. Only "is the first algorithm that" is removed, and the rest is your sentence. The original spans two commented notes from your adviser, which are removed with it. They ask whether the rewards have to be positive-valued, and the sentence already answers that with "even when those rewards do not have a clear division into positive and negative".

Used in: [Contribution statements](../hangs-writing-style-reference.md#contribution-statements).

### OA-504

**Accepted** · weight 1 · Correction · Chapter 5 · From “Thumbs Up” to “10 out of 10” · Chapter 5 › Methodology › Online Participant Recruitment, `chapters/steady.tex`, line 170

Suggestion: "workers with backgrounds"

Original:

~~~latex
In order to reflect the feedback abilities of non-expert crowdworkers, no worker requirements were set to only collect data from top workers with AMT Masters Qualification or workers with backgrounds.
~~~

Accepted wording:

~~~latex
In order to reflect the feedback abilities of non-expert crowdworkers, no worker requirements were set to only collect data from top workers with AMT Masters Qualification or workers with relevant backgrounds.
~~~

Note written with the suggestion: A word is missing after "with". I have assumed "relevant". Change it with "Edit the wording" if you meant a specific background, such as robotics.

### OA-505

**Accepted** · weight 1 · Correction · Chapter 5 · From “Thumbs Up” to “10 out of 10” · Chapter 5 › Methodology › Hypotheses, `chapters/steady.tex`, line 190

Suggestion: The last "we" in the chapters

Original:

~~~latex
From prior work, we expect that binary feedback is noise-reduced and scalar feedback tends to be unstable, but none of the prior work has closely examined it.
~~~

Accepted wording:

~~~latex
From prior work, binary feedback is expected to be noise-reduced and scalar feedback is expected to be unstable, but none of the prior work has closely examined it.
~~~

Note written with the suggestion: This is the only first-person sentence left in Chapters 1 to 9. It follows a bold run-in head, which is probably why the pronoun review did not list it. The form is the one of H2 in the same section ("are expected to be").

Used in: [Impersonal dissertation voice](../hangs-writing-style-reference.md#impersonal-dissertation-voice).

### OA-506

**Accepted** · weight 1 · Claim matched to the evidence · Chapter 5 · From “Thumbs Up” to “10 out of 10” · Chapter 5 › Methodology › Hypotheses, `chapters/steady.tex`, line 197

Suggestion: "explains why learning from multiple people is a common issue"

Original:

~~~latex
The uniqueness of the feedback pattern explains why
learning from multiple people is a common issue in Interactive RL.
~~~

Accepted wording:

~~~latex
The uniqueness of the feedback pattern may help explain why
learning from multiple people is a common issue in Interactive RL.
~~~

Note written with the suggestion: The sentence is part of a hypothesis, stated before any result, and the study did not test learning from several people. The Discussion of this chapter says "This helps explain why". The same verb is used here.

Used in: [Qualifying a result](../hangs-writing-style-reference.md#qualifying-a-result).

### OA-601

**Accepted** · weight 1 · Claim matched to the evidence · Chapter 6 · How Much Progress Did I Make? An Unexplored… · Chapter 6 › Introduction, `chapters/progress.tex`, line 57

Suggestion: "does not need extra workload and time"

Original:

~~~latex
Furthermore, when compared to scalar feedback, progress is more consistent when demonstrations are noisy and does not need extra workload and time.
~~~

Accepted wording:

~~~latex
Furthermore, when compared to scalar feedback, progress is more consistent when demonstrations are noisy, and no significant difference in workload or completion time was detected.
~~~

Note written with the suggestion: As OA-119. The opening of this chapter and its Discussion already say that no significant difference was detected.

Used in: [Reporting a difference that was not detected](../hangs-writing-style-reference.md#reporting-a-difference-that-was-not-detected).

### OA-602

**Accepted** · weight 1 · Grammar · Chapter 6 · How Much Progress Did I Make? An Unexplored… · Chapter 6 › Progress › Hypotheses, `chapters/progress.tex`, line 94

Suggestion: "should be not hard"

Original:

~~~latex
People are expected to naturally estimate task completion in their daily lives, so progress should be not hard to give.
~~~

Accepted wording:

~~~latex
People are expected to naturally estimate task completion in their daily lives, so progress should not be hard to give.
~~~

Note written with the suggestion: Word order only.

### OA-603

**Accepted** · weight 1 · Same fact, two wordings · Chapter 6 · How Much Progress Did I Make? An Unexplored… · Chapter 6 › Progress with non-self-provided demonstrations › Online study setups, `chapters/progress.tex`, line 125

Suggestion: The scale of scalar feedback in Chapter 6 is never stated

New text, placed next to this passage:

~~~latex
The online studies first validated the workload of providing progress and verified that progress contains unique information relative to scalar feedback in a range of 0 to 100.
~~~

Accepted wording:

~~~latex
In these studies, scalar feedback was collected on the same range as progress, from 0 to 100.
~~~

Note written with the suggestion: Scalar feedback is on five points in Chapter 3 and from 0 to 10 in Chapter 5. Chapter 6 compares its standard deviation with that of progress, which only works if both use the same range, and the only hint is the end of the sentence before this one. The table of final values (95.1, 62.7, 23.1) shows that the range was 0 to 100. One sentence says it. Please also confirm that the public space study used the same range, and add the instruction that participants were given for scalar feedback if you have it.

Used in: [Adding sentences that were not asked for](../hangs-writing-style-reference.md#adding-sentences-that-were-not-asked-for).

### OA-604

**Declined** · weight 3 · Correction · Chapter 6 · How Much Progress Did I Make? An Unexplored… · Chapter 6 › Progress with non-self-provided demonstrations › Giving progress is not time-consuming and not hard, `chapters/progress.tex`, line 172

Suggestion: "Online Study One" in one caption, "Online Study II" in the next

Original, which stayed:

~~~latex
Online Study One Results.
~~~

Declined suggestion:

~~~latex
Online Study \RNum{1} Results.
~~~

Note written with the suggestion: The text and the other caption use the Roman numeral.

Not used in a pattern: Fact, logic, equation, or caption corrections that Hang declined. They are kept so that the same correction is not offered again without new information.

### OA-605

**Accepted** · weight 1 · Claim matched to the evidence · Chapter 6 · How Much Progress Did I Make? An Unexplored… · Chapter 6 › Progress with non-self-provided demonstrations › Giving progress is not time-consuming and not hard, `chapters/progress.tex`, line 172

Suggestion: Caption: "has no difference"

Original:

~~~latex
The workload of giving progress has no difference from that of giving scalar feedback.
~~~

Accepted wording:

~~~latex
No significant difference in workload was detected between giving progress and giving scalar feedback.
~~~

Note written with the suggestion: As OA-119. A caption is read on its own and is listed in the List of Figures.

Used in: [Reporting a difference that was not detected](../hangs-writing-style-reference.md#reporting-a-difference-that-was-not-detected).

### OA-606

**Declined** · weight 3 · Claim matched to the evidence · Chapter 6 · How Much Progress Did I Make? An Unexplored… · Chapter 6 › Progress with non-self-provided demonstrations › Giving progress is not time-consuming and not hard, `chapters/progress.tex`, line 167

Suggestion: H1 is a hypothesis of no difference

New text, placed next to this passage:

~~~latex
\textbf{H1} is supported.
~~~

Declined suggestion:

~~~latex
The Bayes factors, which are between 0.3 and 1, give only weak evidence for the absence of a difference.
~~~

Note written with the suggestion: H1 says that giving progress does not require extra workload or time. The evidence is a difference that was not significant, with Bayes factors between 0.3 and 1, which is weak evidence for no difference. Your verdict is kept, and one sentence says how strong the support is. Style entry: Hypotheses and verdicts ("A hypothesis of no extra cost or no difference needs careful interpretation").

Used in: [Qualifying a result](../hangs-writing-style-reference.md#qualifying-a-result), [Adding sentences that were not asked for](../hangs-writing-style-reference.md#adding-sentences-that-were-not-asked-for).

### OA-701

**Accepted** · weight 1 · Correction · Chapter 7 · PHIRL · Chapter 7, `chapters/phirl.tex`, line 13

Suggestion: A sentence that starts in lower case

Original:

~~~latex
\textit{progress} is consistent and intuitive for non-expert users (\autoref{ch:progress}), and non-expert demonstrations contain structured imperfections that do not advance the task (\autoref{ch:sidetracks}).
~~~

Accepted wording:

~~~latex
\textit{Progress} is consistent and intuitive for non-expert users (\autoref{ch:progress}), and non-expert demonstrations contain structured imperfections that do not advance the task (\autoref{ch:sidetracks}).
~~~

Note written with the suggestion: The colon before this sentence was replaced by a period, and the first word kept its lower-case letter.

### OA-702

**Accepted** · weight 1 · Claim matched to the evidence · Chapter 7 · PHIRL · Chapter 7 › Introduction, `chapters/phirl.tex`, line 42

Suggestion: "High-quality human feedback ... is more accessible"

Original:

~~~latex
High-quality human feedback, on the other hand, is more accessible and requires fewer skills.
~~~

Accepted wording:

~~~latex
Human feedback, on the other hand, is more accessible and requires fewer skills.
~~~

Note written with the suggestion: Chapters 3 and 5 report that non-expert feedback was accurate in 51.79% of cases on average and was repeated exactly in 25.2% of cases, so the dissertation's own results do not show that high-quality feedback is easy to get. What the argument needs is that feedback takes less skill than a demonstration, and the rest of the sentence says that. One word is removed.

### OA-703

**Accepted** · weight 1 · Claim matched to the evidence · Chapter 7 · PHIRL · Chapter 7 › Introduction, `chapters/phirl.tex`, line 64

Suggestion: "significantly outperforms IRL baselines" (Introduction of Chapter 7)

Original:

~~~latex
The results show that PHIRL significantly outperforms IRL baselines with only 20\% of demonstrations being annotated offline, and the online extension of PHIRL is effective with VLM-generated annotations.
~~~

Accepted wording:

~~~latex
The results show that PHIRL obtains higher returns than all four baselines with only 20\% of demonstrations being annotated offline, and the online extension of PHIRL is effective with VLM-generated annotations.
~~~

Note written with the suggestion: See OA-123 for the reason.

Used in: [Qualifying a result](../hangs-writing-style-reference.md#qualifying-a-result).

### OA-704

**Declined** · weight 3 · Correction · Chapter 7 · PHIRL · Chapter 7 › Methodology › Reward Function Shaping, `chapters/phirl.tex`, line 210

Suggestion: "a strictly increasing monotonic hinge"

Original, which stayed:

~~~latex
where $\Delta p_t = p_{t+1} - p_t$, and $\ell(\cdot,\cdot)$ is a strictly increasing monotonic hinge alignment function, where $\ell(a, b) = \max\bigl(0,\, m - \mathrm{sign}(a)\, b\bigr)$, $m \geq 0$.
~~~

Declined suggestion:

~~~latex
where $\Delta p_t = p_{t+1} - p_t$, and $\ell(\cdot,\cdot)$ is a hinge alignment loss, $\ell(a, b) = \max\bigl(0,\, m - \mathrm{sign}(a)\, b\bigr)$ with a margin $m \geq 0$, which is zero when $b$ has the sign of $a$ and a magnitude of at least $m$.
~~~

Note written with the suggestion: A hinge function is flat at zero over part of its range, so it is not strictly increasing, and this one does not increase in its second argument when the first is positive. The formula is right and the description is not. The revision says what the loss does, in the words of the formula.

Not used in a pattern: Fact, logic, equation, or caption corrections that Hang declined. They are kept so that the same correction is not offered again without new information.

### OA-705

**Accepted** · weight 1 · Correction · Chapter 7 · PHIRL · Chapter 7 › Methodology › Reward Function Shaping, `chapters/phirl.tex`, line 234

Suggestion: A demonstration is $d$, the dataset is $\mathcal{D}$

Original:

~~~latex
Note that in this condition specifically, $s_i, s_{i+1}, s_j$, and $s_{j+1}$ are preferably from the same demonstration $D$ since different users might scale \textit{progress} differently.
~~~

Accepted wording:

~~~latex
Note that in this condition specifically, $s_i, s_{i+1}, s_j$, and $s_{j+1}$ are preferably from the same demonstration $d$ since different users might scale \textit{progress} differently.
~~~

Note written with the suggestion: Section 7.2.2 writes a demonstration as $d$ and the dataset as $\mathcal{D}$. Here a single demonstration is written $D$.

### OA-706

**Accepted** · weight 1 · Citation · Chapter 7 · PHIRL · Chapter 7 › Methodology › Reward Function Shaping, `chapters/phirl.tex`, line 241

Suggestion: Potential-based shaping is cited to the wrong paper

Original:

~~~latex
The potential function $\Phi$ was introduced in \cite{ng2000algorithms}, and describes the distance between the current state and the goal state:
~~~

Accepted wording:

~~~latex
The potential function $\Phi$ was introduced in \cite{ng1999policy}, and describes, for example, the distance between the current state and the goal state:
~~~

Note written with the suggestion: The cited paper, Ng and Russell (2000), is "Algorithms for inverse reinforcement learning". The potential function and the result that it does not change the optimal policy are from Ng, Harada and Russell (1999), "Policy invariance under reward transformations". OA-B1 adds that entry to references.bib, and this item needs it. "For example" is added because the negative distance to the goal is one possible potential, not its definition, and the chapter itself sets the potential to V(s) two sentences later.

### OA-707

**Declined** · weight 3 · Correction · Chapter 7 · PHIRL · Chapter 7 › Methodology › Reward Function Shaping, `chapters/phirl.tex`, line 267

Suggestion: A missing comma in the total reward

Original, which stayed:

~~~latex
$ R_\theta(d) \;=\; \sum_{t} r_\theta\!\bigl(s_t\,s_{t+1}\bigr)$
~~~

Declined suggestion:

~~~latex
$ R_\theta(d) \;=\; \sum_{t} r_\theta\!\bigl(s_t,\,s_{t+1}\bigr)$
~~~

Note written with the suggestion: The two arguments of the reward run together. The other equations of this section write them with a comma.

Not used in a pattern: Fact, logic, equation, or caption corrections that Hang declined. They are kept so that the same correction is not offered again without new information.

### OA-709

**Declined** · weight 3 · Claim matched to the evidence · Chapter 7 · PHIRL · Chapter 7 › Methodology › PHIRL, `chapters/phirl.tex`, line 331

Suggestion: "can still be effective" without the potential term

Original, which stayed:

~~~latex
For instance, for methods without a potential component, PHIRL can still be effective with the remaining three alignments (see \autoref{sec:abl}).
~~~

Declined suggestion:

~~~latex
For instance, for methods without a potential component, PHIRL can still be applied with the remaining three alignments, although the ablation shows that removing the potential term reduces performance (see \autoref{sec:abl}).
~~~

Note written with the suggestion: The sentence points to the ablation, and the ablation says "The potential shaping component is generally influential across all conditions". In the figure, removing it gives the lowest bar in three of the four conditions. The framework can be applied without it. That it stays effective is what the ablation puts in doubt.

Used in: [Qualifying a result](../hangs-writing-style-reference.md#qualifying-a-result).

### OA-710

**Accepted** · weight 1 · Claim matched to the evidence · Chapter 7 · PHIRL · Chapter 7 › Experiments and Results, `chapters/phirl.tex`, line 360

Suggestion: "shown to be robust to reward hacking"

Original:

~~~latex
In addition, the reward functions learned by PHIRL are shown to be robust to reward hacking in two representative scenarios.
~~~

Accepted wording:

~~~latex
In addition, a qualitative analysis illustrates how \textit{progress} alignment can discourage two examined reward-hacking behaviors.
~~~

Note written with the suggestion: On 2026-09-26 you replaced "structurally resilient against two reward-hacking behaviors" with "illustrates how progress alignment can discourage two examined reward-hacking behaviors", and that wording is now in Chapter 1, in the opening, Introduction and Summary of this chapter, and in Chapter 9. This sentence, the heading of Section 7.3.4 (OA-718) and one sentence in it (OA-719) still make the stronger claim.

Used in: [Qualifying a result](../hangs-writing-style-reference.md#qualifying-a-result).

### OA-711

**Accepted** · weight 1 · Same fact, two wordings · Chapter 7 · PHIRL · Chapter 7 › Experiments and Results › Setups, `chapters/phirl.tex`, line 371

Suggestion: "Gen 3 Lite" and "Gen3 Lite"

Original:

~~~latex
For the real robot task, a Kinova Gen 3 Lite arm and an animal-brushing task were used.
~~~

Accepted wording:

~~~latex
For the real robot task, a Kinova Gen3 Lite arm and an animal-brushing task were used.
~~~

Note written with the suggestion: As OA-609.

### OA-712

**Declined** · weight 3 · Scope or limitation stated · Chapter 7 · PHIRL · Chapter 7 › Experiments and Results › Setups, `chapters/phirl.tex`, line 379

Suggestion: The demonstrators of Chapter 7 are not the non-experts of Chapters 3 to 6

New text, placed next to this passage:

~~~latex
For the real robot domain, a similar setup was used. Six participants were recruited (two ``worse'', two ``okay'', and two ``better'', 10 demonstrations each), and an MH dataset was constructed.
~~~

Declined suggestion:

~~~latex
The operators of these datasets differ in proficiency, and they are not the passersby whose demonstrations were studied in \autoref{ch:sidetracks} and \autoref{ch:progress}. The mixed-quality datasets are therefore used in this chapter in place of demonstrations from non-experts.
~~~

Note written with the suggestion: This is the question I would expect first on Chapter 7. The chapter opens by saying it "leverages imperfect non-expert teaching", and its datasets come from Robomimic operators and six recruited participants graded as worse, okay and better. Section 8.3 says so ("The simulated evaluations of PHIRL used Robomimic datasets collected by other operators"), and Chapter 7 does not. Two sentences where the datasets are introduced say what the mixed-quality data is used for. Both restate facts of this paragraph and of Section 8.3.

Used in: [Limitations and future work](../hangs-writing-style-reference.md#limitations-and-future-work), [Adding sentences that were not asked for](../hangs-writing-style-reference.md#adding-sentences-that-were-not-asked-for).

### OA-713

**Declined** · weight 3 · Claim matched to the evidence · Chapter 7 · PHIRL · Chapter 7 › Experiments and Results › Setups, `chapters/phirl.tex`, line 412

Suggestion: Caption of the results figure: "significantly outperforms"

Original, which stayed:

~~~latex
PHIRL significantly outperforms baselines in both domains, particularly when the task horizon is long or demonstration quality is low (MH).
~~~

Declined suggestion:

~~~latex
PHIRL obtains higher returns than the baselines in both domains, particularly when the task horizon is long or demonstration quality is low (MH).
~~~

Note written with the suggestion: See OA-123 for the reason. The caption is also printed in the List of Figures.

Used in: [Qualifying a result](../hangs-writing-style-reference.md#qualifying-a-result).

### OA-714

**Accepted** · weight 1 · Same fact, two wordings · Chapter 7 · PHIRL · Chapter 7 › Experiments and Results › Setups, `chapters/phirl.tex`, line 414

Suggestion: The caption on the ablation disagrees with the text and with the bars

Original:

~~~latex
Completion shaping is most critical when there are failed demonstrations, while reward shaping is most effective overall.
~~~

Accepted wording:

~~~latex
Removing completion shaping reduces performance most in PickPlaceCan (MH), while removing potential shaping reduces performance most in the other three conditions.
~~~

Note written with the suggestion: The caption says "reward shaping is most effective overall". The text says "The potential shaping component is generally influential across all conditions", and in the middle row of the figure the bar without Potential is the lowest of the ablations in Lift (PH), Lift (MH) and PickPlaceCan (PH). The caption says completion shaping is "most critical when there are failed demonstrations", and the text calls it "the only exception". The bars show both: almost no effect in three conditions, and the lowest bar in PickPlaceCan (MH). The revision states what the bars show. I read the values from the figure, so please check them against your numbers.

### OA-715

**Accepted** · weight 1 · Same fact, two wordings · Chapter 7 · PHIRL · Chapter 7 › Experiments and Results › Setups, `chapters/phirl.tex`, line 424

Suggestion: "AIRLPref" in the text, "AIRL-Pref" in both figures

Original:

~~~latex
The comparison includes four baseline methods, AIRL (IRL with no human feedback) \cite{fu2018learning}, Pref (preference-learning based IRL with no demonstrations) \cite{christiano2017deep}, AIRLPref (IRL with both feedback and demonstrations) \cite{palan2019learning}, and Rank2Reward (reward learning method with a temporally inferred progress signal) \cite{yang2024rank2rewardlearningshapedreward}.
~~~

Accepted wording:

~~~latex
The comparison includes four baseline methods, AIRL (IRL with no human feedback) \cite{fu2018learning}, Pref (preference-learning based IRL with no demonstrations) \cite{christiano2017deep}, AIRL-Pref (IRL with both feedback and demonstrations) \cite{palan2019learning}, and Rank2Reward (reward learning method with a temporally inferred progress signal) \cite{yang2024rank2rewardlearningshapedreward}.
~~~

Note written with the suggestion: The legends of the results figure and of the real-robot figure say "AIRL-Pref", and so does the real-robot paragraph. This is the only other place in the text where the method is named.

Used in: [Established dissertation terminology](../hangs-writing-style-reference.md#established-dissertation-terminology).

### OA-716

**Accepted** · weight 1 · Correction · Chapter 7 · PHIRL · Chapter 7 › Experiments and Results › PHIRL Outperforms Baselines, `chapters/phirl.tex`, line 514

Suggestion: The real-robot result gives every number except PHIRL's

Original:

~~~latex
PHIRL performed well with demonstrations of mixed quality and outperformed baselines AIRL (39), AIRL-Pref (62), Pref (58), and  Rank2Reward  (54).
~~~

Accepted wording:

~~~latex
PHIRL (73) performed well with demonstrations of mixed quality and outperformed baselines AIRL (39), AIRL-Pref (62), Pref (58), and Rank2Reward (54).
~~~

Note written with the suggestion: The sentence lists the count for each baseline and not for PHIRL. The count appears only in the next paragraph ("84 vs. 73"), and the figure shows 73. One number is added.

Used in: [Numbers and measured comparisons](../hangs-writing-style-reference.md#numbers-and-measured-comparisons).

### OA-717

**Declined** · weight 3 · Restored from your paper or comments · Chapter 7 · PHIRL · Chapter 7 › Experiments and Results › Ablation Study and Sensitivity Analysis, `chapters/phirl.tex`, line 544

Suggestion: The ablation result for PickPlaceCan (MH), which the figure still shows

New text, placed next to this passage:

~~~latex
The only exception is the completion shaping term, as in most conditions demonstrations are marked as fully completed (\textit{progress} $> 90$ for the last frame).
~~~

Declined suggestion:

~~~latex
In the PickPlaceCan (MH) condition, however, removing completion shaping resulted in the largest performance drop of all terms, from $M=116.99$ to $M=63.77$ ($p < 0.001$).
~~~

Note written with the suggestion: The shortened ablation paragraph of the updated paper says that the completion term is "the only exception", and stops. The figure, which is the same file as in the earlier paper, still shows what the earlier text reported: "in the Can-MH domain, removing completion shaping resulted in a significant performance drop: PHIRL's performance decreases from M=116.99 to M=63.7740 (p < 0.001)". That sentence is in a comment a few lines above this paragraph. It is the only measured support in the dissertation for using failed demonstrations, which Section 8.1 presents as the way imperfect teaching "can be used rather than only tolerated". A dissertation has no page limit, so the result can come back. The numbers are yours. Please confirm that they still hold for the updated experiments.

Used in: [Adding sentences that were not asked for](../hangs-writing-style-reference.md#adding-sentences-that-were-not-asked-for).

### OA-718

**Accepted** · weight 1 · Heading · Chapter 7 · PHIRL · Chapter 7 › Experiments and Results › PHIRL Learns More Robust Reward Functions, `chapters/phirl.tex`, line 553

Suggestion: A heading that claims more than its section shows

Original:

~~~latex
\subsection{PHIRL Learns More Robust Reward Functions}
~~~

Accepted wording:

~~~latex
\subsection{Reward Functions in Two Reward Hacking Scenarios} % [HY measured] was ``PHIRL Learns More Robust Reward Functions''
~~~

Note written with the suggestion: See OA-710. The section analyzes two scenarios qualitatively, and the heading says that PHIRL learns more robust reward functions. The style entry on headings says "A heading must not claim more than the section establishes". The new heading names what the section contains, and the old one is kept in a comment after it.

Used in: [Headings that name the question or finding](../hangs-writing-style-reference.md#headings-that-name-the-question-or-finding), [Qualifying a result](../hangs-writing-style-reference.md#qualifying-a-result).

### OA-719

**Accepted** · weight 1 · Claim matched to the evidence · Chapter 7 · PHIRL · Chapter 7 › Experiments and Results › PHIRL Learns More Robust Reward Functions, `chapters/phirl.tex`, line 566

Suggestion: "PHIRL produced a more robust reward function"

Original:

~~~latex
PHIRL produced a more robust reward function.
~~~

Accepted wording:

~~~latex
PHIRL produced a more robust reward function in this scenario.
~~~

Note written with the suggestion: See OA-710. Three words limit the statement to the scenario it describes.

Used in: [Qualifying a result](../hangs-writing-style-reference.md#qualifying-a-result).

### OA-720

**Declined** · weight 3 · Correction · Chapter 7 · PHIRL · Chapter 7 › Discussion and Limitations, `chapters/phirl.tex`, line 611

Suggestion: A sentence about ReWiND in quotation marks

Original, which stayed:

~~~latex
It adopted the key idea of ReWiND: ``use language instructions to represent key subgoals in a task, and then combine the language instructions with a VLM to indicate task progress.''
~~~

Declined suggestion:

~~~latex
It adopted the key idea of ReWiND, which is to use language instructions to represent key subgoals in a task, and then combine the language instructions with a VLM to indicate task progress.
~~~

Note written with the suggestion: Quotation marks say that these are the words of the ReWiND paper. If the sentence is your summary of its idea, the marks should go, and the revision does that with "which is to", the form you used in Chapter 8 in place of a colon. If it is a quotation, reject this and add the page.

Used in: [Few colons and semicolons](../hangs-writing-style-reference.md#few-colons-and-semicolons).

### OA-721

**Declined** · weight 3 · Claim matched to the evidence · Chapter 7 · PHIRL · Chapter 7 › Discussion and Limitations, `chapters/phirl.tex`, line 615

Suggestion: The formative VLM study covers the Lift domain only

Original, which stayed:

~~~latex
This study demonstrates that PHIRL can benefit from a VLM trained with general knowledge and suggests a direction for other progress-based learning algorithms.
~~~

Declined suggestion:

~~~latex
This study, conducted in the Lift domain, demonstrates that PHIRL can benefit from a VLM trained with general knowledge and suggests a direction for other progress-based learning algorithms.
~~~

Note written with the suggestion: The figure of this study has two panels, Lift (PH) and Lift (MH), and the numbers in the text are the Lift results. The sentence generalizes to PHIRL and to other algorithms without saying where it was tested.

Used in: [Qualifying a result](../hangs-writing-style-reference.md#qualifying-a-result).

### OA-722

**Declined** · weight 3 · Claim matched to the evidence · Chapter 7 · PHIRL · Chapter 7 › Summary, `chapters/phirl.tex`, line 681

Suggestion: Summary of Chapter 7: "significantly outperformed baselines"

Original, which stayed:

~~~latex
The results showed that PHIRL significantly outperformed baselines with 20\% of demonstrations being annotated before learning.
~~~

Declined suggestion:

~~~latex
The results showed that PHIRL obtained higher returns than all four baselines with 20\% of demonstrations being annotated before learning.
~~~

Note written with the suggestion: See OA-123 for the reason.

Used in: [Qualifying a result](../hangs-writing-style-reference.md#qualifying-a-result).

### OA-801

**Accepted** · weight 1 · Same fact, two wordings · Chapter 8 · Overall Discussion · Chapter 8, `chapters/discussion.tex`, line 7

Suggestion: The third question is worded two ways (opening of Chapter 8)

Original:

~~~latex
It first answers the three questions: whether the imperfections in non-expert teaching are random noise, whether the inconsistency of non-expert feedback can be reduced while utilizing the magnitudes, and whether combining demonstrations and feedback can lower quality requirements for human teaching and reduce human effort in annotating.
~~~

Accepted wording:

~~~latex
It first answers the three questions: whether the imperfections in non-expert teaching are random noise, whether the inconsistency of non-expert feedback can be reduced while utilizing the magnitudes, and whether combining demonstrations and feedback can enable robust reward learning while reducing human effort in annotating.
~~~

Note written with the suggestion: See OA-104. You edited this sentence this afternoon and kept "lower quality requirements for human teaching", while the question above its answer, 30 lines below, says "enable robust reward learning while reducing human effort in annotating". Only the third question changes here.

### OA-802

**Accepted with Hang's edit** · weight 4 · Grammar · Chapter 8 · Overall Discussion · Chapter 8 › Answers to the Overarching Questions, `chapters/discussion.tex`, line 21

Suggestion: "have structured source,"

Original:

~~~latex
Together, these findings suggest the imperfections have structured source, the teacher's characteristics, the demands of the task at a given moment, and the channel through which the teaching is given.
~~~

Suggested:

~~~latex
Together, these findings suggest the imperfections have structured sources, which are the teacher's characteristics, the demands of the task at a given moment, and the channel through which the teaching is given.
~~~

Hang's wording:

~~~latex
Together, these findings suggest the imperfections have structured sources, which are the teacher's characteristics and the demands of the task at a given moment.
~~~

Note written with the suggestion: A sentence you wrote this afternoon. The list names three sources, so the noun is plural, and "which are" introduces the list in place of the comma (the form you used for "a design choice ..., which is to" in this chapter). Your words are kept.

Used in: [Few colons and semicolons](../hangs-writing-style-reference.md#few-colons-and-semicolons).

### OA-803

**Accepted** · weight 1 · Grammar · Chapter 8 · Overall Discussion · Chapter 8 › Answers to the Overarching Questions, `chapters/discussion.tex`, line 24

Suggestion: "demonstrated two ways."

Original:

~~~latex
The results of the second stage demonstrated two ways.
~~~

Accepted wording:

~~~latex
The results of the second stage demonstrated two ways to do so.
~~~

Note written with the suggestion: A sentence you shortened this afternoon. As it stands it does not say what the two ways do. Three words connect it to the question above it.

### OA-804

**Declined** · weight 3 · Correction · Chapter 8 · Overall Discussion · Chapter 8 › Answers to the Overarching Questions, `chapters/discussion.tex`, line 31

Suggestion: "in all four imperfect scenarios significantly"

Original, which stayed:

~~~latex
When participants in the second online study rated the same imperfect demonstrations, \textit{progress} varied less across participants than scalar feedback in all four imperfect scenarios significantly.
~~~

Declined suggestion:

~~~latex
When participants in the second online study rated the same imperfect demonstrations, \textit{progress} varied less across participants than scalar feedback in all four imperfect scenarios, significantly in two of them.
~~~

Note written with the suggestion: Chapter 6 reports a significant difference in two of the four scenarios (Imperfect, p = 0.018, and Failure, p < 0.001) and p = 0.060 and p = 0.058 for the other two. The record of the Chapter 8 review lists this sentence under "To check before the accepted wording is used". Progress did vary less in all four, so that part stays, and the count is put back after "significantly".

Not used in a pattern: Fact, logic, equation, or caption corrections that Hang declined. They are kept so that the same correction is not offered again without new information.

### OA-805

**Accepted** · weight 1 · Correction · Chapter 8 · Overall Discussion · Chapter 8 › Findings That Connect the Chapters, `chapters/discussion.tex`, line 71

Suggestion: A sentence without its period

Original:

~~~latex
However, they suggest that annotations may be most informative around changes of sub-task and precise contacts such as grasps, which are the steps that the magnitude term of PHIRL is designed to reward more than simply moving closer
~~~

Accepted wording:

~~~latex
However, they suggest that annotations may be most informative around changes of sub-task and precise contacts such as grasps, which are the steps that the magnitude term of PHIRL is designed to reward more than simply moving closer.
~~~

Note written with the suggestion: The period after "moving closer" is missing, so this sentence runs into the next one. Also listed under "To check" in the record of the Chapter 8 review.

### OA-806

**Accepted** · weight 1 · Spelling · Chapter 8 · Overall Discussion · Chapter 8 › Future Work, `chapters/discussion.tex`, line 104

Suggestion: charpters, extentions

Original:

~~~latex
One is future work that addresses the limitations of the charpters in this dissertation or extentions to the work in this dissertation.
~~~

Accepted wording:

~~~latex
One is future work that addresses the limitations of the chapters in this dissertation or extensions to the work in this dissertation.
~~~

Note written with the suggestion: Spelling only. Your sentence is otherwise unchanged.

Used in: [Correcting a sentence without rewording it](../hangs-writing-style-reference.md#correcting-a-sentence-without-rewording-it).

### OA-807

**Declined** · weight 3 · Same fact, two wordings · Chapter 8 · Overall Discussion · Chapter 8 › Future Work, `chapters/discussion.tex`, line 105

Suggestion: A direction in the list that has no subsection

Original, which stayed:

~~~latex
This direction follows directly from the findings of this dissertation and includes actively selecting which demonstrations to annotate, extending the learning framework to enable learning from teaching modalities beyond human evaluative feedback and human demonstrations, examining the conclusions on a larger scale,  and extending the framework to be compatible with foundation models.
~~~

Declined suggestion:

~~~latex
This direction follows directly from the findings of this dissertation and includes actively selecting which demonstrations to annotate, extending the learning framework to enable learning from teaching modalities beyond human evaluative feedback and human demonstrations, and extending the framework to be compatible with foundation models.
~~~

Note written with the suggestion: The list names four directions, and the section has subsections for three of them. "Examining the conclusions on a larger scale" has none, and you declined the subsection that was drafted for it (DW-43). This takes the direction out of the list and changes nothing else in your sentence. Reject it if you plan to write that subsection.

Not used in a pattern: Fact, logic, equation, or caption corrections that Hang declined. They are kept so that the same correction is not offered again without new information.

### OA-808

**Accepted** · weight 1 · Spelling · Chapter 8 · Overall Discussion · Chapter 8 › Future Work, `chapters/discussion.tex`, line 109

Suggestion: scenairos, planing

Original:

~~~latex
This dissertation studied scenairos  in which robots need to learn a manipulation skill from the users, while robots also need to learn to perform a complex task by planing with learned skills and learn to interact properly with users when they already know how to perform the tasks.
~~~

Accepted wording:

~~~latex
This dissertation studied scenarios in which robots need to learn a manipulation skill from the users, while robots also need to learn to perform a complex task by planning with learned skills and learn to interact properly with users when they already know how to perform the tasks.
~~~

Note written with the suggestion: Spelling only. Your sentence is otherwise unchanged.

### OA-809

**Accepted** · weight 1 · Spelling · Chapter 8 · Overall Discussion · Chapter 8 › Future Work, `chapters/discussion.tex`, line 110

Suggestion: taking advantages of

Original:

~~~latex
Both needs can be approached by taking advantages of agentic AI, and they are described in this section as agentic robotics and agentic human-robot interaction (HRI).
~~~

Accepted wording:

~~~latex
Both needs can be approached by taking advantage of agentic AI, and they are described in this section as agentic robotics and agentic human-robot interaction (HRI).
~~~

Note written with the suggestion: The idiom is "taking advantage of", which is the form recorded for you in the style reference. One letter changes.

### OA-810

**Accepted** · weight 1 · Spelling · Chapter 8 · Overall Discussion · Chapter 8 › Future Work › Agentic Human-Robot Interaction, `chapters/discussion.tex`, line 189

Suggestion: comunicate

Original:

~~~latex
In human-chatbot interaction, a human and a chatbot interact in turns and comunicate through natural language and images.
~~~

Accepted wording:

~~~latex
In human-chatbot interaction, a human and a chatbot interact in turns and communicate through natural language and images.
~~~

Note written with the suggestion: Spelling only. Your sentence is otherwise unchanged.

Used in: [Correcting a sentence without rewording it](../hangs-writing-style-reference.md#correcting-a-sentence-without-rewording-it).

### OA-811

**Accepted** · weight 1 · Spelling · Chapter 8 · Overall Discussion · Chapter 8 › Future Work › Agentic Human-Robot Interaction, `chapters/discussion.tex`, line 190

Suggestion: hiddent varibles, Human robot interaction

Original:

~~~latex
Human robot interaction is way more complex with significantly more hiddent varibles that are hard to capture.
~~~

Accepted wording:

~~~latex
Human-robot interaction is way more complex with significantly more hidden variables that are hard to capture.
~~~

Note written with the suggestion: Spelling, and the hyphen of "human-robot interaction" as written in the rest of the chapter. "Way more complex" is left as you wrote it.

### OA-812

**Accepted** · weight 1 · Grammar · Chapter 8 · Overall Discussion · Chapter 8 › Future Work › Agentic Human-Robot Interaction, `chapters/discussion.tex`, line 197

Suggestion: "such as International Conference on Human-Robot Interaction"

Original:

~~~latex
This would begin by distilling the papers from Human-Robot Interaction conferences, such as International Conference on Human-Robot Interaction, and converting their findings into skills.
~~~

Accepted wording:

~~~latex
This would begin by distilling the papers from Human-Robot Interaction conferences, such as the International Conference on Human-Robot Interaction, and converting their findings into skills.
~~~

Note written with the suggestion: The name of a conference takes "the". One word is added to your sentence.

### OA-813

**Accepted** · weight 1 · Grammar · Chapter 8 · Overall Discussion · Chapter 8 › Future Work › Agentic Human-Robot Interaction, `chapters/discussion.tex`, line 199

Suggestion: "and use to decide"

Original:

~~~latex
Literature-grounded skills could allow an agentic robot to draw on decades of HRI findings as seed skills, and use to decide whether to ask a non-expert for a demonstration, an annotation, or a correction, how to phrase the request, and when to stop asking, instead of building the skill library from scratch.
~~~

Accepted wording:

~~~latex
Literature-grounded skills could allow an agentic robot to draw on decades of HRI findings as seed skills, and use them to decide whether to ask a non-expert for a demonstration, an annotation, or a correction, how to phrase the request, and when to stop asking, instead of building the skill library from scratch.
~~~

Note written with the suggestion: "Use" has no object. One word is added, and it refers to the seed skills named just before.

### OA-902

**Accepted** · weight 1 · Correction · Chapter 9 · Conclusion · Chapter 9 › Summary of Contributions, `chapters/conclusion.tex`, line 93

Suggestion: A stray "[HY: improvement end]" on the last page

Original:

~~~latex
they can be understood, mitigated, and even leveraged. [HY: improvement end]
Learning from humans also depends on how capable humans are at shaping a robot's behaviors.
~~~

Accepted wording:

~~~latex
they can be understood, mitigated, and even leveraged.
Learning from humans also depends on how capable humans are at shaping a robot's behaviors.
~~~

Note written with the suggestion: The marker that opened this pair is on a commented line at the end of the file, so the closing marker stands alone and prints as plain text in the closing paragraph of the dissertation. Neither sentence is changed. The following sentence is quoted only so that the place is found.

### OA-903

**Declined** · weight 5 · Correction · Chapter 9 · Conclusion · Chapter 9 › Summary of Contributions, `chapters/conclusion.tex`, line 95

Suggestion: An empty citation prints "[]"

Original, which stayed:

~~~latex
When a robot can learn only from clean demonstrations and consistent feedback, teaching it is left to trained operators or workers in data factories \cite{}, and thus the people who will live and work with the robot must either learn to teach in the way that the method expects or have their teaching set aside as noise.
~~~

Declined suggestion:

~~~latex
When a robot can learn only from clean demonstrations and consistent feedback, teaching it is left to trained operators or workers in data factories, and thus the people who will live and work with the robot must either learn to teach in the way that the method expects or have their teaching set aside as noise.
~~~

Hang's note: fill in the citations: papers or work about data farming with FastUMI and ego centric data in data factories

Note written with the suggestion: \cite{} with no key prints an empty bracket in the PDF and gives a BibTeX warning. This removes it and changes nothing else. If you have a source for "workers in data factories", put its key in with "Edit the wording". I have not added one, because I have not checked a source for it.

Not used in a pattern: Content requests in Hang's notes or edits, about citations and the publication status rather than wording.

### OA-904

**Accepted** · weight 1 · Correction · Chapter 9 · Conclusion · Chapter 9 › Summary of Contributions, `chapters/conclusion.tex`, line 97

Suggestion: The last sentence of the dissertation appears twice

Original:

~~~latex
The hope is that the studies, datasets, methods, and the learning framework presented in this dissertation will encourage future work to embrace, rather than ignore, the imperfections in non-expert human teaching.
~~~

Accepted wording:

~~~latex
(delete the passage)
~~~

Note written with the suggestion: The two sentences differ in one word: the first has "takeaways" in its list and the second, the earlier version, does not. This removes the earlier version, so the dissertation ends on the sentence with "takeaways".

### OA-002

**Accepted** · weight 1 · Correction · main.tex · main.tex, `main.tex`, line 100

Suggestion: Abstract: "Our step" is missing a word

Original:

~~~latex
Our step investigates imperfections in human evaluative feedback and human demonstrations.
~~~

Accepted wording:

~~~latex
Our first step investigates imperfections in human evaluative feedback and human demonstrations.
~~~

Note written with the suggestion: A word is missing. "Our first step" keeps your wording and matches "The second stage" and "In the third stage" later in the paragraph. RB-01 in reference-dissertation-review proposes "The first stage" for the same sentence, so decide only one of the two.

### OA-003

**Accepted** · weight 1 · Correction · main.tex · main.tex, `main.tex`, line 112

Suggestion: Abstract: "alternatively" should be "alternately"

Original:

~~~latex
In the third stage, based on the findings from previous stages, we propose a reward learning framework that alternatively learns
from human progress labels and human demonstrations.
~~~

Accepted wording:

~~~latex
In the third stage, based on the findings from previous stages, we propose a reward learning framework that alternately learns
from human progress labels and human demonstrations.
~~~

Note written with the suggestion: "Alternatively" means "as another option". The framework alternates between the two sources, which is "alternately", the word Chapter 7 uses ("alternately updating"). Only this word changes. RB-03 makes the same correction together with a change of "progress labels".

### OA-B1

**Accepted** · weight 1 · Bibliography entry · references.bib · references.bib, `references.bib`, line 1654

Suggestion: Bibliography entry for potential-based reward shaping

New text, placed next to this passage:

~~~latex
booktitle = {Icml},
  volume={1},
  number={2},
  pages={2},
  year={2000}
}
~~~

Accepted wording:

~~~latex
@inproceedings{ng1999policy,
  title = {Policy invariance under reward transformations: Theory and application to reward shaping},
  author = {Ng, Andrew Y. and Harada, Daishi and Russell, Stuart},
  booktitle = {Proceedings of the Sixteenth International Conference on Machine Learning (ICML)},
  pages = {278--287},
  year = {1999}
}
~~~

Note written with the suggestion: Needed by OA-706. Ng, Harada and Russell, "Policy invariance under reward transformations: Theory and application to reward shaping", ICML 1999, pages 278 to 287. I wrote the entry from memory of the reference, so please compare it with the paper. It is placed after the entry of the paper that is cited now. An entry that is not cited does no harm.

### OA-B2

**Accepted** · weight 1 · Bibliography entry · references.bib · references.bib, `references.bib`, line 1495

Suggestion: Your CHARM paper is cited as an arXiv preprint

Original:

~~~latex
@misc{fang2025charmconsideringhumanattributes,
      title = {CHARM: Considering Human Attributes for Reinforcement Modeling},
      author={Qidi Fang and Hang Yu and Shijie Fang and Jindan Huang and Qiuyu Chen and Reuben M. Aronson and Elaine S. Short},
      year={2025},
      eprint={2506.13079},
      archivePrefix={arXiv},
      primaryClass={cs.RO},
      url={https://arxiv.org/abs/2506.13079},
}
~~~

Accepted wording:

~~~latex
@inproceedings{fang2025charmconsideringhumanattributes,
      title = {{CHARM}: Considering Human Attributes for Reinforcement Modeling},
      author={Qidi Fang and Hang Yu and Shijie Fang and Jindan Huang and Qiuyu Chen and Reuben M. Aronson and Elaine S. Short},
      booktitle = {2025 34th IEEE International Conference on Robot and Human Interactive Communication (RO-MAN)},
      year={2025},
      organization={IEEE}
}
~~~

Note written with the suggestion: A comment in main.tex says "Ch. 3: CHARM (RO-MAN 2025)", and item 2 of your notes.txt says the papers should have venues. The entry is of type misc with an arXiv number, so the bibliography prints the paper as a preprint. This makes it a conference paper. The braces around CHARM keep the bibliography style from printing "Charm". I took the name of the proceedings from the numbering of the conference (34th in 2025). Please check it and add the pages from IEEE Xplore.

### OA-B3

**Accepted** · weight 1 · Bibliography entry · references.bib · references.bib, `references.bib`, line 1514

Suggestion: Your progress paper is cited as an arXiv preprint

Original:

~~~latex
@article{yu2024much,
  title = {How Much Progress Did I Make? An Unexplored Human Feedback Signal for Teaching Robots},
  author={Yu, Hang and Fang, Qidi and Fang, Shijie and Aronson, Reuben M and Short, Elaine Schaertl},
  journal={arXiv preprint arXiv:2407.06459},
  year={2024}
}
~~~

Accepted wording:

~~~latex
@inproceedings{yu2024much,
  title = {How Much Progress Did {I} Make? {A}n Unexplored Human Feedback Signal for Teaching Robots},
  author={Yu, Hang and Fang, Qidi and Fang, Shijie and Aronson, Reuben M and Short, Elaine Schaertl},
  booktitle = {2024 33rd IEEE International Conference on Robot and Human Interactive Communication (RO-MAN)},
  year={2024},
  organization={IEEE}
}
~~~

Note written with the suggestion: As OA-B2. A comment in main.tex says "Ch. 6: Progress (RO-MAN 2024)". The braces around "I" and "A" keep the bibliography style from printing "did i make? an unexplored". Please check the name of the proceedings (33rd in 2024) and add the pages. The Demonstration Sidetracks entry is also a preprint entry. I have left it, because I do not know where that paper appeared.
