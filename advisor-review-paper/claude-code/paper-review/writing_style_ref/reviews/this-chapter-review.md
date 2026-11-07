# Fewer "this chapter"

Review `this-chapter-review` of the dissertation, from `waiting_for_review/this-chapter-review`. Decided between October 14, 2026 and October 14, 2026. Decisions files: `this-chapter-review.decisions.20261014-225021.json`.

[All reviews](../review-decisions.md) · [Weighted signals](../preference-signals.md) · [Main reference](../hangs-writing-style-reference.md)

| Outcome | Decided by Hang | Not decided by Hang |
| --- | ---: | ---: |
| Accepted as suggested | 16 | 0 |
| Accepted with Hang's edit | 0 | 0 |
| Declined | 10 | 0 |
| Notes from Hang | 0 | |

24 of the 50 items had no decision when the review was imported.

### TC-201

**Accepted** · weight 1 · Concrete subject · Chapter 2 · Background · Chapter 2, `chapters/background.tex`, line 6

Original:

~~~latex
Additionally, this chapter summarizes literature relevant to the core technical domains in this dissertation, including modeling human feedback dynamics, learning from non-optimal demonstrations, and reward learning methods.
~~~

Accepted wording:

~~~latex
Additionally, it summarizes literature relevant to the core technical domains in this dissertation, including modeling human feedback dynamics, learning from non-optimal demonstrations, and reward learning methods.
~~~

Note written with the suggestion: The sentence before begins "This chapter reviews". The second sentence can take "it". Style entry: Known information leading to new information.

### TC-301

**Declined** · weight 3 · Phrase dropped · Chapter 3 · CHARM · Chapter 3, `chapters/charm.tex`, line 12

Original, which stayed:

~~~latex
The related work for this chapter is reviewed in \autoref{sec:bg-rlhf} , and the work presented in this chapter was originally published as ``CHARM: Considering Human Attributes for Reinforcement Modeling''~\cite{fang2025charmconsideringhumanattributes}.
~~~

Declined suggestion:

~~~latex
The related work is reviewed in \autoref{sec:bg-rlhf} , and the work presented in this chapter was originally published as ``CHARM: Considering Human Attributes for Reinforcement Modeling''~\cite{fang2025charmconsideringhumanattributes}.
~~~

Note written with the suggestion: The sentence used "this chapter" twice. It sits in the chapter's opening paragraphs, so "The related work" is already scoped. The "originally published as" part is unchanged (it keeps one "this chapter"). The space before the comma is left as it is.

Used in: [Correcting a sentence without rewording it](../hangs-writing-style-reference.md#correcting-a-sentence-without-rewording-it).

### TC-302

**Accepted** · weight 1 · Concrete subject · Chapter 3 · CHARM · Chapter 3, `chapters/charm.tex`, line 44

Original:

~~~latex
This chapter aims to investigate how human characteristics are associated with human feedback patterns and proposes that human feedback values would be more accurately predicted if human characteristics are taken into account.
~~~

Accepted wording:

~~~latex
The aim is to investigate how human characteristics are associated with human feedback patterns, and the hypothesis is that human feedback values would be more accurately predicted if human characteristics are taken into account.
~~~

Note written with the suggestion: "proposes that ... would be more accurately predicted" states a hypothesis that the evaluation then tests, so it is named as one. Style entries: Hypotheses and verdicts, Impersonal dissertation voice. To keep "proposes", edit to "The study investigates how ... and proposes that ...".

### TC-303

**Accepted** · weight 1 · Concrete subject · Chapter 3 · CHARM · Chapter 3, `chapters/charm.tex`, line 48

Original:

~~~latex
In addition, this chapter proposes a novel method for training a human feedback predictor CHARM, Considering Human Attributes for Reinforcement Modeling.
~~~

Accepted wording:

~~~latex
In addition, a novel method for training a human feedback predictor, CHARM (Considering Human Attributes for Reinforcement Modeling), is proposed.
~~~

Note written with the suggestion: The method becomes the subject. In the original it is unclear whether CHARM names the method or the predictor. Section 3.1.3 calls CHARM the method, so the name is placed next to "method". Style entry: Impersonal dissertation voice.

### TC-304

**Accepted** · weight 1 · Concrete subject · Chapter 3 · CHARM · Chapter 3, `chapters/charm.tex`, line 53

Original:

~~~latex
This chapter demonstrates that feedback delay has little correlation with the selected human characteristics, while there is a pronounced correlation between feedback values and selected human characteristics.
~~~

Accepted wording:

~~~latex
The results demonstrate that feedback delay has little correlation with the selected human characteristics, while there is a pronounced correlation between feedback values and selected human characteristics.
~~~

Note written with the suggestion: A chapter does not find results, so the results are the subject. "demonstrate" is kept so the claim keeps its strength. Style entry: Impersonal dissertation voice ("A chapter can propose, examine, or present, but it does not ... find results"). The next sentence keeps "This chapter systematically investigates this association", which answers the "few studies have examined" before it.

Used in: [This chapter as the subject](../hangs-writing-style-reference.md#this-chapter-as-the-subject).

### TC-305

**Declined** · weight 3 · Concrete subject · Chapter 3 · CHARM · Chapter 3 › Study Design, `chapters/charm.tex`, line 71

Original, which stayed:

~~~latex
This chapter argues that human feedback does not solely rely on tasks or robot behaviors, but also depends on the human teachers themselves.
~~~

Declined suggestion:

~~~latex
The study is based on the premise that human feedback does not solely rely on tasks or robot behaviors, but also depends on the human teachers themselves.
~~~

Note written with the suggestion: The claim is the premise of the study design, and the next sentence ("To explore this, a questionnaire was developed ... and a public study was conducted") follows from it. Style entry: Study actions leading to the analytical question.

Used in: [This chapter as the subject](../hangs-writing-style-reference.md#this-chapter-as-the-subject).

### TC-306

**Accepted** · weight 1 · Concrete subject · Chapter 3 · CHARM · Chapter 3 › Study Design › Human Feedback pattern, `chapters/charm.tex`, line 81

Original:

~~~latex
Thus, in this chapter, human feedback patterns are represented using scalar feedback and delays.
~~~

Accepted wording:

~~~latex
Thus, in this study, human feedback patterns are represented using scalar feedback and delays.
~~~

Note written with the suggestion: The scope is kept, since it says how feedback is represented in this study as opposed to in general. Chapter 3 reports one study, so "this study" covers the same ground.

### TC-307

**Accepted** · weight 1 · Concrete subject · Chapter 3 · CHARM · Chapter 3 › Study Design › Considering Human Attributes for Reinforcement Modeling, `chapters/charm.tex`, line 128

Original:

~~~latex
To further investigate the non-linear relationship between human characteristics and human feedback and to simulate feedback more realistically, this chapter proposes CHARM, a novel human feedback simulation method shown in \autoref{fig:oracle_overview}.
~~~

Accepted wording:

~~~latex
To further investigate the non-linear relationship between human characteristics and human feedback and to simulate feedback more realistically, CHARM is proposed as a novel human feedback simulation method, shown in \autoref{fig:oracle_overview}.
~~~

Note written with the suggestion: The method becomes the subject. Style entry: Impersonal dissertation voice. CHARM was first named as a proposal in the introduction (TC-303), so this sentence in the method section can name it directly.

Used in: [This chapter as the subject](../hangs-writing-style-reference.md#this-chapter-as-the-subject).

### TC-401

**Declined** · weight 3 · Concrete subject · Chapter 4 · Demonstration Sidetracks · Chapter 4, `chapters/sidetracks.tex`, line 10

Original, which stayed:

~~~latex
This chapter asks whether the imperfections in non-expert demonstrations also contain systematic structure.
~~~

Declined suggestion:

~~~latex
The question that follows is whether the imperfections in non-expert demonstrations also contain systematic structure.
~~~

Note written with the suggestion: The sentence before gives the result of Chapter 3, and this one names the question it raises. The opening paragraph just above already begins "This chapter completes the first stage". Style entry: Known information leading to new information.

Used in: [This chapter as the subject](../hangs-writing-style-reference.md#this-chapter-as-the-subject).

### TC-402

**Accepted** · weight 1 · Phrase dropped · Chapter 4 · Demonstration Sidetracks · Chapter 4, `chapters/sidetracks.tex`, line 15

Original:

~~~latex
The related work for this chapter is reviewed in \autoref{sec:bg-lfd} , and the work presented in this chapter was originally published as ``Demonstration Sidetracks: Categorizing Systematic Non-Optimality in Human Demonstrations''~\cite{fang2025demonstrationsidetrackscategorizingsystematic}.
~~~

Accepted wording:

~~~latex
The related work is reviewed in \autoref{sec:bg-lfd} , and the work presented in this chapter was originally published as ``Demonstration Sidetracks: Categorizing Systematic Non-Optimality in Human Demonstrations''~\cite{fang2025demonstrationsidetrackscategorizingsystematic}.
~~~

Note written with the suggestion: As TC-301. The "originally published as" part keeps its "this chapter".

### TC-403

**Declined** · weight 3 · Phrase dropped · Chapter 4 · Demonstration Sidetracks · Chapter 4 › Introduction, `chapters/sidetracks.tex`, line 23

Original, which stayed:

~~~latex
Thus, this chapter focuses on identifying and investigating patterns of the noise in non-expert demonstrations.
~~~

Declined suggestion:

~~~latex
Thus, the focus is on identifying and investigating patterns of the noise in non-expert demonstrations.
~~~

Note written with the suggestion: The sentence follows "The key insight is that ...", and "Thus" already ties the focus to it.

Used in: [This chapter as the subject](../hangs-writing-style-reference.md#this-chapter-as-the-subject).

### TC-404

**Declined** · weight 3 · Concrete subject · Chapter 4 · Demonstration Sidetracks · Chapter 4 › Introduction, `chapters/sidetracks.tex`, line 45

Original, which stayed:

~~~latex
This chapter analyzes data from a public space study with 40 non-expert demonstrators with a long-horizon task, collected in the study of \autoref{ch:progress}, which was originally conducted to validate \textit{progress}.
~~~

Declined suggestion:

~~~latex
The analysis uses data from a public space study with 40 non-expert demonstrators with a long-horizon task, collected in the study of \autoref{ch:progress}, which was originally conducted to validate \textit{progress}.
~~~

Note written with the suggestion: The analysis is what uses the data. The rest of the sentence is unchanged. Style entry: Research actions.

Used in: [This chapter as the subject](../hangs-writing-style-reference.md#this-chapter-as-the-subject).

### TC-405

**Declined** · weight 3 · Repeated sentence removed · Chapter 4 · Demonstration Sidetracks · Chapter 4 › Introduction, `chapters/sidetracks.tex`, line 56

Original, which stayed:

~~~latex
The findings indicate that non-optimal behaviors are beyond random errors, and possess spatial and temporal structures.
% \elaine{put a summary of results here}
This chapter systematically characterizes non-experts' non-optimal manipulation patterns when providing demonstrations.
These findings will be beneficial for future LfD algorithm development to better learn from noisy demonstrations and for oracle design to reduce the gap between in-lab datasets and real-world demonstrations.
~~~

Declined suggestion:

~~~latex
The findings indicate that non-optimal behaviors are beyond random errors, and possess spatial and temporal structures.
% \elaine{put a summary of results here}
These findings will be beneficial for future LfD algorithm development to better learn from noisy demonstrations and for oracle design to reduce the gap between in-lab datasets and real-world demonstrations.
~~~

Note written with the suggestion: This sentence repeats "The main contributions of this chapter are characterizing and categorizing non-optimal behaviors in human demonstrations" from three lines above, which is kept. Without it, "These findings will be beneficial" follows "The findings indicate that ...", which it refers to. The two neighbouring lines (and the \elaine comment between them) are quoted unchanged so that no blank line is left behind. To keep a reworded version instead, edit the wording, for instance "The analysis systematically characterizes ...".

Used in: [Chapter openings](../hangs-writing-style-reference.md#chapter-openings).

### TC-406

**Declined** · weight 3 · Phrase dropped · Chapter 4 · Demonstration Sidetracks · Chapter 4 › Methodology, `chapters/sidetracks.tex`, line 74

Original, which stayed:

~~~latex
The premise of this chapter is that some non-optimal behaviors are beyond noise or mistakes.
~~~

Declined suggestion:

~~~latex
The premise is that some non-optimal behaviors are beyond noise or mistakes.
~~~

Note written with the suggestion: The Methodology section opens with this premise, so its scope is clear without the phrase. "The key insight is as follows" comes three lines later and is unchanged.

Used in: [This chapter as the subject](../hangs-writing-style-reference.md#this-chapter-as-the-subject).

### TC-407

**Accepted** · weight 1 · Concrete subject · Chapter 4 · Demonstration Sidetracks · Chapter 4 › Methodology, `chapters/sidetracks.tex`, line 76

Original:

~~~latex
This chapter presents an exploratory analysis to investigate noisy behaviors in non-expert human demonstrations.
~~~

Accepted wording:

~~~latex
An exploratory analysis was conducted to investigate noisy behaviors in non-expert human demonstrations.
~~~

Note written with the suggestion: A procedural passive, since the procedure is what the sentence reports. Style entry: Impersonal dissertation voice ("Use procedural passives when the procedure or data deserves emphasis").

### TC-408

**Declined** · weight 3 · Phrase dropped · Chapter 4 · Demonstration Sidetracks · Chapter 4 › Methodology › , `chapters/sidetracks.tex`, line 92

Original, which stayed:

~~~latex
This chapter defines non-optimal behaviors in human demonstrations as \textit{\ThingName{}}.
~~~

Declined suggestion:

~~~latex
Here, non-optimal behaviors in human demonstrations are defined as \textit{\ThingName{}}.
~~~

Note written with the suggestion: "Here" keeps the sense that the term is introduced at this point. Style entry: Definitions before notation ("This chapter defines [phenomenon] as [term]" is the form in the reference; this is the third definition of the term in the chapter, after the opening paragraph and the Introduction).

Used in: [This chapter as the subject](../hangs-writing-style-reference.md#this-chapter-as-the-subject).

### TC-409

**Accepted** · weight 1 · Phrase dropped · Chapter 4 · Demonstration Sidetracks · Chapter 4 › Methodology › Experiment Setup, `chapters/sidetracks.tex`, line 95

Original:

~~~latex
The demonstration data analyzed in this chapter were collected as part of the validation study for \textit{progress} in \autoref{ch:progress}.
~~~

Accepted wording:

~~~latex
The demonstration data were collected as part of the validation study for \textit{progress} in \autoref{ch:progress}.
~~~

Note written with the suggestion: The data of this chapter are the only data the sentence can mean. The next sentence ("The study design is reviewed here") is unchanged.

### TC-410

**Accepted** · weight 1 · Concrete subject · Chapter 4 · Demonstration Sidetracks · Chapter 4 › Methodology › Codebook, `chapters/sidetracks.tex`, line 133

Original:

~~~latex
This chapter focuses on the following four types of \thingname{}:
~~~

Accepted wording:

~~~latex
The codebook focuses on the following four types of \thingname{}:
~~~

Note written with the suggestion: The sentence sits under the heading "Codebook", and the four definitions that follow are the codebook's entries. "focuses on" is kept, since it allows that other kinds of sidetracks exist.

Used in: [This chapter as the subject](../hangs-writing-style-reference.md#this-chapter-as-the-subject).

### TC-411

**Accepted** · weight 1 · Concrete subject · Chapter 4 · Demonstration Sidetracks · Chapter 4 › Methodology › Codebook › Alignment, `chapters/sidetracks.tex`, line 143

Original:

~~~latex
In addition to \thingname{}, this chapter also considers one control pattern:
~~~

Accepted wording:

~~~latex
In addition to \thingname{}, one control pattern is also considered:
~~~

Note written with the suggestion: One-dimension control was measured from the number of actions per timestep (Section "Effect of Control Interface"), not annotated with the codebook, so the codebook is not named as its source.

### TC-412

**Declined** · weight 3 · Pointer made specific · Chapter 4 · Demonstration Sidetracks · Chapter 4 › Discussion, `chapters/sidetracks.tex`, line 249

Original, which stayed:

~~~latex
These imperfections are the \thingname{} defined in this chapter.
~~~

Declined suggestion:

~~~latex
These imperfections are the \thingname{} defined above.
~~~

Note written with the suggestion: The term is defined in the Introduction and in Section "Demonstration Sidetracks" of the Methodology, both above this Discussion. The section has no label, so "above" is used instead of a reference.

Used in: [This chapter as the subject](../hangs-writing-style-reference.md#this-chapter-as-the-subject).

### TC-413

**Declined** · weight 3 · Concrete subject · Chapter 4 · Demonstration Sidetracks · Chapter 4 › Discussion, `chapters/sidetracks.tex`, line 262

Original, which stayed:

~~~latex
One limitation of this chapter is that it only used demonstrations from one task, one robot, and one control interface.
~~~

Declined suggestion:

~~~latex
One limitation of the analysis is that it only used demonstrations from one task, one robot, and one control interface.
~~~

Note written with the suggestion: The limitation is about the data the analysis used. Style entry: Limitations and future work.

Used in: [This chapter as the subject](../hangs-writing-style-reference.md#this-chapter-as-the-subject).

### TC-502

**Accepted** · weight 1 · Phrase dropped · Chapter 5 · From “Thumbs Up” to “10 out of 10” · Chapter 5, `chapters/steady.tex`, line 16

Original:

~~~latex
The related work for this chapter is reviewed in \autoref{sec:RW} , and the work presented in this chapter was originally published as ``From `Thumbs Up' to `10 out of 10': Reconsidering Scalar Feedback in Interactive Reinforcement Learning''~\cite{yu2023thumbs}.
~~~

Accepted wording:

~~~latex
The related work is reviewed in \autoref{sec:RW} , and the work presented in this chapter was originally published as ``From `Thumbs Up' to `10 out of 10': Reconsidering Scalar Feedback in Interactive Reinforcement Learning''~\cite{yu2023thumbs}.
~~~

Note written with the suggestion: As TC-301. The "originally published as" part keeps its "this chapter".

### TC-503

**Accepted** · weight 1 · Concrete subject · Chapter 5 · From “Thumbs Up” to “10 out of 10” · Chapter 5 › Introduction, `chapters/steady.tex`, line 61

Original:

~~~latex
This chapter presents a study of scalar and binary feedback with 90 online participants evaluating a robot performing a manipulation task, and shows that scalar feedback has the potential to improve learning when properly handled.
~~~

Accepted wording:

~~~latex
A study of scalar and binary feedback was conducted with 90 online participants evaluating a robot performing a manipulation task, and the results show that scalar feedback has the potential to improve learning when properly handled.
~~~

Note written with the suggestion: A chapter does not find results, so the study is reported with a passive and its results are the subject of "show". Style entry: Impersonal dissertation voice ("[Chapter] collected [data] and found [result] → In [chapter], [data] was collected. The results show that [result]"). The next sentence ("The study shows that human teachers can be inconsistent ...") is unchanged.

### TC-506

**Accepted** · weight 1 · Concrete subject · Chapter 5 · From “Thumbs Up” to “10 out of 10” · Chapter 5 › Stabilizing Teacher Assessment Dynamics › STEADY, `chapters/steady.tex`, line 468

Original:

~~~latex
In this chapter, $k$ is set to $20$.
~~~

Accepted wording:

~~~latex
In the experiments, $k$ is set to $20$.
~~~

Note written with the suggestion: The value of $k$ is a setting of the experiments, which is what "in this chapter" meant. The comment after the sentence on the same line is left in place.

Used in: [This chapter as the subject](../hangs-writing-style-reference.md#this-chapter-as-the-subject).

### TC-704

**Accepted** · weight 1 · Concrete subject · Chapter 7 · PHIRL · Chapter 7 › Methodology, `chapters/phirl.tex`, line 112

Original:

~~~latex
This chapter develops a reward learning framework, PHIRL, that aligns machine-learned information with human knowledge on the same demonstration dataset.
PHIRL is built on the key insight that \textbf{rewards inferred from a set of demonstrations should be consistent with the feedback on the same set of demonstrations.}
~~~

Accepted wording:

~~~latex
PHIRL is a reward learning framework that aligns machine-learned information with human knowledge on the same demonstration dataset.
It is built on the key insight that \textbf{rewards inferred from a set of demonstrations should be consistent with the feedback on the same set of demonstrations.}
~~~

Note written with the suggestion: The Introduction already says "This chapter mitigates these gaps by proposing a data-efficient reward learning framework, PHIRL", which is kept. Here, at the start of the method, PHIRL is the subject, and the next sentence takes "It" so that two sentences do not both begin with "PHIRL".

Used in: [This chapter as the subject](../hangs-writing-style-reference.md#this-chapter-as-the-subject).

### TC-707

**Accepted** · weight 1 · Phrase dropped · Chapter 7 · PHIRL · Chapter 7 › Methodology › Reward Function Shaping, `chapters/phirl.tex`, line 267

Original:

~~~latex
that did not complete the task (in this chapter, \textit{progress} $< 90$ at the end) , no matter the horizon of the demonstrations.
~~~

Accepted wording:

~~~latex
that did not complete the task (\textit{progress} $< 90$ at the end) , no matter the horizon of the demonstrations.
~~~

Note written with the suggestion: The parentheses give the threshold that defines a failed demonstration, and they read as that definition without the phrase. The space before the comma after the parenthesis is left as it is.
