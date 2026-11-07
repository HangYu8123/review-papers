# Source evidence for Hang's writing style reference

Examples are grouped under the same patterns as the [main reference](hangs-writing-style-reference.md). Source line numbers identify LaTeX source lines, not PDF pages. Identical file, line, and quotation records within a pattern are shown once, with all source-entry attributions. Patterns that rest only on evidence from Hang have no paper examples, and their evidence is listed in [preference-signals.md](preference-signals.md).

The v1 library preserves LaTeX excerpts. The Claude library transcribes emphasis, omits citations, and uses ellipses for omissions. The excerpts below preserve those respective representations. Quoted wording is evidence of manuscript practice, including occasional grammar, punctuation, or claims that the merged guide qualifies. It is not an instruction to reuse an outdated term, number, or claim.

The complete original entry text and metadata are retained in [source-entries.json](sources/source-entries.json). The original library texts are also preserved as [v1](sources/v1-library.md) and [Claude](sources/claude-library.md) snapshots. Their relative paths were written for the original folders.

## Teachers and collection settings

[Merged guidance](hangs-writing-style-reference.md#teachers-and-collection-settings)

**[PROG, line 105](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude VOC-01

```text
Robots have already firmly become part of our daily lives, making it crucial to learn from users, especially non-expert users.
```

**[RSS, line 26](../reference_papers/prospectus/RSS%20Pioneers%202026.tex)** — claude VOC-01

```text
However, expecting all of the users, especially those with limited experience with robots, to always provide high-quality teaching is impractical.
```

**[PROG, line 203](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude VOC-01

```text
We conducted our studies with crowd-sourced workers and random passersby.
```

**[SIDE, line 161](../reference_papers/Demonstration_sidetracks/main.tex)** — claude VOC-08

```text
The demonstrations we used in this work were collected outside the lab with random people. Our data and results can be expected to better reflect robot-in-the-wild deployments than in-lab setups.
```

**[CHARM, line 479](../reference_papers/CHARM/ROMAN%202025.tex)** — claude VOC-08

```text
We conducted our study in a public space with 46 participants who randomly passed by our setup.
```

**[RSS, line 28](../reference_papers/prospectus/RSS%20Pioneers%202026.tex)** — claude VOC-08

```text
Ignoring or oversimplifying these dynamics in teaching from non-experts can lead to a higher demand for training data or a significant decrease in robot performance.
```

**[STEADY, line 340](../reference_papers/STEADY/IEEEexample.tex)** — v1 LIB-WRD-05

```text
One group of workers was asked to give binary feedback and the other group of workers was asked to give scalar feedback. All workers received the same compensation and viewed the same content.
```

**[Progress, line 145](../reference_papers/Progress/Ro-MAN%202024.tex)** — v1 LIB-WRD-05

```text
For the in-person study, we recruit 40 passersby to provide demonstrations in an ice cream topping-adding task, shown in \autoref{page1}. The demonstrators then provide progress and scalar feedback to their own demonstrations.
```

**[RSS Pioneers prospectus, line 92](../reference_papers/prospectus/RSS%20Pioneers%202026.tex)** — v1 LIB-WRD-05

```text
We collected demonstrations from 40 non-experts with an ice cream-topping adding task.
```

## Imperfect teaching and structured behavior

[Merged guidance](hangs-writing-style-reference.md#imperfect-teaching-and-structured-behavior)

**[SIDE, line 68](../reference_papers/Demonstration_sidetracks/main.tex)** — claude VOC-02

```text
Prior work in LfD often characterizes the sub-optimalities in human demonstrations as random noise.
```

**[PROG, line 95](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude VOC-02

```text
We find that progress indicates whether the task is successfully performed, reflects the degree of task completion, identifies unproductive but harmless behaviors, and is likely to be more consistent across participants.
```

**[PROG, line 654](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude VOC-02

```text
We found that non-expert demonstrations are multi-policy and mostly successful, while noisy in a meaningful way.
```

**[Progress, line 126](../reference_papers/Progress/Ro-MAN%202024.tex)** — v1 LIB-VOC-03

```text
This is especially true for non-expert demonstrations: non-expert demonstrations can be noisy, multi-policy, and yet still succeed (we show this in \autoref{sectionVC}).
```

**[Demonstration Sidetracks, line 180](../reference_papers/Demonstration_sidetracks/main.tex)** — v1 LIB-VOC-03

```text
Non-optimal behaviors in human demonstrations are structured with patterns.
```

**[Demonstration Sidetracks, line 192](../reference_papers/Demonstration_sidetracks/main.tex)** — v1 LIB-VOC-03

```text
As a result, human demonstrations tend to be different from machine demonstrations by containing not only noisy actions but also accommodation behaviors.
```

## Teaching signals and learning quantities

[Merged guidance](hangs-writing-style-reference.md#teaching-signals-and-learning-quantities)

**[PH-ABS, line 70](../reference_papers/PHIRL/CoRL_2026_main.tex)** — claude VOC-03

```text
Specifically, we use *progress*, a feedback modality that describes cumulative task completion.
```

**[PROG, line 211](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude VOC-03

```text
Our goal is to improve learning from human feedback with a new teaching signal: progress.
```

**[STEADY, line 134](../reference_papers/STEADY/IEEEexample.tex)** — claude VOC-03

```text
both binary feedback and scalar feedback are dynamic, and
```

**[STEADY, line 144](../reference_papers/STEADY/IEEEexample.tex)** — v1 LIB-VOC-02

```text
Evaluative feedback is natural for non-experts to provide, and can take the form of either \emph{binary} feedback, in which feedback can only be either ``good'' or ``bad'', or \emph{scalar} feedback, which takes a value from a scale of values (e.g., ``1-10'', ``A-F'', or ``0-5 stars'').
```

**[PHIRL, line 17](../reference_papers/PHIRL/methodology.tex)** — v1 LIB-VOC-02

```text
\textit{Progress} is a signal that describes the cumulative degree of task completion, ranging from fully incomplete to fully complete.
```

**[PHIRL, line 87](../reference_papers/PHIRL/methodology.tex)** — v1 LIB-VOC-02

```text
We improve the learned reward function by shaping it to align with \textit{progress} annotations during reward learning.
```

## Research actions

[Merged guidance](hangs-writing-style-reference.md#research-actions)

**[CHARM, line 55](../reference_papers/CHARM/ROMAN%202025.tex)** — claude VOC-05

```text
We conducted a public space study with two long-horizon tasks and 46 participants.
```

**[SIDE, line 71](../reference_papers/Demonstration_sidetracks/main.tex)** — claude VOC-05

```text
We recreated the experimental setup in a simulation and annotated all the demonstrations.
```

**[STEADY, line 339](../reference_papers/STEADY/IEEEexample.tex)** — claude VOC-05

```text
A total of 90 AMT crowdworkers were recruited, divided evenly between two groups (45 participants per group).
```

**[CHARM, line 54](../reference_papers/CHARM/ROMAN%202025.tex)** — v1 LIB-VOC-01

```text
In this work, we designed an exploratory study investigating how human feedback patterns are associated with human characteristics.
```

**[Progress, line 93](../reference_papers/Progress/Ro-MAN%202024.tex)** — v1 LIB-VOC-01

```text
In this work, we characterize and test a little-used teaching signal: \textit{progress},  designed to represent the completion percentage of a task.
```

**[Demonstration Sidetracks, line 177](../reference_papers/Demonstration_sidetracks/main.tex)** — v1 LIB-VOC-01

```text
In this work, we conducted an exploratory analysis to investigate noisy behaviors in non-expert human demonstrations.
```

## Method operations and their objects

[Merged guidance](hangs-writing-style-reference.md#method-operations-and-their-objects)

**[PROG, line 115](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude VOC-06

```text
Demonstrations carry relatively dense and global information including policies and goals, and tend to be less accurate
```

**[PH-ABS, line 68](../reference_papers/PHIRL/CoRL_2026_main.tex)** — claude VOC-06

```text
Human demonstrations provide dense policy-level information but sometimes lack local precision.
```

**[STEADY, line 197](../reference_papers/STEADY/IEEEexample.tex)** — claude VOC-06

```text
This enables binary-feedback-based learning algorithms to learn
```

**[CHARM, line 425](../reference_papers/CHARM/ROMAN%202025.tex)** — v1 LIB-VOC-04

```text
Human characteristics and task statistics (CHARM): the model was trained to predict feedback values using both corresponding task statistics and human characteristics.
```

**[PHIRL, line 71](../reference_papers/PHIRL/CoRL_2026_main.tex)** — v1 LIB-VOC-04

```text
PHIRL iteratively infers a reward function from demonstrations via inverse reinforcement learning, calculates the learned rewards over the \textit{progress}-annotated demonstrations, and aligns the rewards with \textit{progress} annotations over four dimensions.
```

**[STEADY, line 131](../reference_papers/STEADY/IEEEexample.tex)** — v1 LIB-VOC-04

```text
STEADY re-constructs underlying positive and negative feedback distributions and re-scales scalar feedback based on feedback statistics.
```

## Information dimensions

[Merged guidance](hangs-writing-style-reference.md#information-dimensions)

**[Progress, line 114](../reference_papers/Progress/Ro-MAN%202024.tex)** — v1 LIB-VOC-05

```text
Human feedback and human demonstrations can be complementary due to the difference in human knowledge they carry.
```

**[Progress, line 115](../reference_papers/Progress/Ro-MAN%202024.tex)** — v1 LIB-VOC-05

```text
Demonstrations carry relatively dense and global information including policies and goals, and tend to be less accurate \cite{palan2019learning}.
```

**[PHIRL, line 68](../reference_papers/PHIRL/CoRL_2026_main.tex)** — v1 LIB-VOC-05

```text
Human demonstrations provide dense policy-level information but sometimes lack local precision. Human feedback presents accurate local critiques, but offers sparse evaluations rather than direct policy guidance.
```

## Accuracy consistency and robustness

[Merged guidance](hangs-writing-style-reference.md#accuracy-consistency-and-robustness)

**[STEADY, line 127](../reference_papers/STEADY/IEEEexample.tex)** — v1 LIB-VOC-06

```text
We found that when considering how consistently a participant labeled the same data, scalar feedback led to less consistency than binary feedback; however, the difference vanishes if small mismatches are allowed.
```

**[Progress, line 141](../reference_papers/Progress/Ro-MAN%202024.tex)** — v1 LIB-VOC-06

```text
We show that progress can indicate the extent of task completion, determine if a task is completed, and be robust to unproductive behaviors. Furthermore, when compared to scalar feedback, progress is more consistent when demonstrations are noisy and does not need extra workload and time.
```

**[CHARM, line 394](../reference_papers/CHARM/ROMAN%202025.tex)** — v1 LIB-VOC-06

```text
This suggests that participants with relevant educational backgrounds or greater robot experience tend to provide feedback that is more accurate in direction (e.g., positive vs. negative).
```

**[PHIRL, line 74](../reference_papers/PHIRL/CoRL_2026_main.tex)** — v1 LIB-VOC-06

```text
Analysis of reward-hacking scenarios demonstrates that PHIRL learns reliable reward functions that are robust to exploitation.
```

## Prior work and research gaps

[Merged guidance](hangs-writing-style-reference.md#prior-work-and-research-gaps)

**[SIDE, line 187](../reference_papers/Demonstration_sidetracks/main.tex)** — claude VOC-09

```text
Prior work interprets non-optimal behaviors in human demonstrations as random manipulation noise or incorrect behaviors with underlying optimal control policies
```

**[STEADY, line 249](../reference_papers/STEADY/IEEEexample.tex)** — claude VOC-09

```text
Throughout the body of prior work, there is a strong focus on using binary feedback to improve learning, with limited exploration of scalar feedback.
```

**[RSS, line 46](../reference_papers/prospectus/RSS%20Pioneers%202026.tex)** — claude VOC-09

```text
recent work suggests that oversimplifying the intricacies of human teaching can potentially cause issues
```

**[CHARM, line 53](../reference_papers/CHARM/ROMAN%202025.tex)** — claude WRD-08

```text
While much prior work acknowledged that human teachers' characteristics would affect human feedback patterns, there is little work that has closely investigated the actual effects.
```

**[SIDE, line 87](../reference_papers/Demonstration_sidetracks/main.tex)** — claude WRD-08

```text
However, there is little research on understanding and modeling non-expert demonstrations.
```

**[STEADY, line 123](../reference_papers/STEADY/IEEEexample.tex)** — claude WRD-08

```text
scalar human feedback has been used less because it is believed to be noisy and unstable.
```

**[Demonstration Sidetracks, line 187](../reference_papers/Demonstration_sidetracks/main.tex)** — v1 LIB-WRD-01

```text
Prior work interprets non-optimal behaviors in human demonstrations as random manipulation noise or incorrect behaviors with underlying optimal control policies \cite{beliaev2024inverse}\cite{beliaev2022imitation}\cite{liu2022robust}.
```

**[PHIRL, line 25](../reference_papers/PHIRL/introduction.tex)** — v1 LIB-WRD-01

```text
Prior reward learning work often relies on preference feedback \cite{palan2019learning, ibarz2018reward, brown2019ranking}.
```

## Hedges and degree words

[Merged guidance](hangs-writing-style-reference.md#hedges-and-degree-words)

**[CHARM, line 394](../reference_papers/CHARM/ROMAN%202025.tex)** — claude VOC-07

```text
This suggests that participants with relevant educational backgrounds or greater robot experience tend to provide feedback that is more accurate in direction (e.g., positive vs. negative).
```

**[STEADY, line 357](../reference_papers/STEADY/IEEEexample.tex)** — claude VOC-07

```text
From prior work, we expect that binary feedback is noise-reduced and scalar feedback tends to be unstable, but none of the prior work has closely examined it.
```

**[SIDE, line 96](../reference_papers/Demonstration_sidetracks/main.tex)** — claude VOC-07

```text
Methods that work with oracle demonstrations might not perform well with real human demonstrations.
```

## Value words and novelty

[Merged guidance](hangs-writing-style-reference.md#value-words-and-novelty)

**[STEADY, line 135](../reference_papers/STEADY/IEEEexample.tex)** — claude VOC-10

```text
scalar feedback is a promising signal for use in interactive Reinforcement Learning.
```

**[PROG, line 151](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude VOC-10

```text
Our results also showed that non-expert demonstrations are multi-policy and sub-optimal, but sub-optimal in a meaningful way.
```

**[SIDE, line 85](../reference_papers/Demonstration_sidetracks/main.tex)** — claude VOC-10

```text
One challenge in LfD is that high-quality demonstrations are hard to obtain
```

## Impersonal dissertation voice

[Merged guidance](hangs-writing-style-reference.md#impersonal-dissertation-voice)

**[CHARM, line 54](../reference_papers/CHARM/ROMAN%202025.tex)** — claude WRD-01, v1 LIB-STY-02

```text
In this work, we designed an exploratory study investigating how human feedback patterns are associated with human characteristics.
```

**[SIDE, line 177](../reference_papers/Demonstration_sidetracks/main.tex)** — claude WRD-01

```text
In this work, we conducted an exploratory analysis to investigate noisy behaviors in non-expert human demonstrations.
```

**[PH-INT, line 13](../reference_papers/PHIRL/introduction.tex)** — claude WRD-01

```text
In this work, we aim to learn robust reward functions by combining human demonstrations and feedback, while reducing human engagement.
```

**[SIDE, line 111](../reference_papers/Demonstration_sidetracks/main.tex)** — claude WRD-02

```text
Our goal is to investigate non-expert behaviors and explore the patterns of noise in non-expert demonstrations.
```

**[PH-CON, line 67](../reference_papers/PHIRL/conclusion.tex)** — claude WRD-02

```text
We believe that PHIRL is an effective framework for learning robust reward functions
```

**[PHIRL, line 71](../reference_papers/PHIRL/CoRL_2026_main.tex)** — v1 LIB-STY-02

```text
PHIRL iteratively infers a reward function from demonstrations via inverse reinforcement learning, calculates the learned rewards over the \textit{progress}-annotated demonstrations, and aligns the rewards with \textit{progress} annotations over four dimensions.
```

## Reporting findings and interpretations

[Merged guidance](hangs-writing-style-reference.md#reporting-findings-and-interpretations)

**[CHARM, line 56](../reference_papers/CHARM/ROMAN%202025.tex)** — claude VOC-04

```text
We found that feedback patterns are not only correlated with task statistics, such as rewards, but also correlated with participants' characteristics, especially robot experience and educational background.
```

**[PROG, line 413](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude VOC-04

```text
We found that progress could correctly indicate if the task is complete, while the indication of task completion was not captured by scalar feedback.
```

**[SIDE, line 306](../reference_papers/Demonstration_sidetracks/main.tex)** — claude VOC-04

```text
This further reveals that humans tend to have demonstration sidetracks near task phase change temporally.
```

**[CHARM, line 445](../reference_papers/CHARM/ROMAN%202025.tex)** — claude VOC-04

```text
These results are consistent with our earlier correlation analysis.
```

**[CHARM, line 393](../reference_papers/CHARM/ROMAN%202025.tex)** — v1 LIB-WRD-03

```text
Robot experience and educational background exhibit correlation coefficients of 0.25 and 0.16 with feedback accuracy.
```

**[CHARM, line 394](../reference_papers/CHARM/ROMAN%202025.tex)** — v1 LIB-WRD-03

```text
This suggests that participants with relevant educational backgrounds or greater robot experience tend to provide feedback that is more accurate in direction (e.g., positive vs. negative).
```

**[Demonstration Sidetracks, line 327](../reference_papers/Demonstration_sidetracks/main.tex)** — v1 LIB-WRD-03

```text
This suggests that \thingname{}, especially \textit{Alignment}, are more likely to happen when approaching a target object. This is possibly due to the requirement for control accuracy, which resulted in more alignment to get to the desired positions and more pauses for reaction.
```

## Reporting a difference that was not detected

[Merged guidance](hangs-writing-style-reference.md#reporting-a-difference-that-was-not-detected)

**[PROG, line 319](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude WRD-03

```text
We did not find any significant difference between giving scalar feedback and progress in all the dimensions of the NASA TLX results
```

**[STEADY, line 186](../reference_papers/STEADY/IEEEexample.tex)** — claude WRD-03

```text
We study the correlation of scalar and binary feedback with interactive RL training targets, and fail to find a significant difference between scalar and binary feedback, although we find that scalar feedback has more variation.
```

**[PROG, line 419](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude WRD-03

```text
there was no evidence showing that there is any difference between the other two and the Perfect case
```

## Numbers and measured comparisons

[Merged guidance](hangs-writing-style-reference.md#numbers-and-measured-comparisons)

**[PROG, line 548](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude WRD-04

```text
We found that non-expert demonstrations are noisy and contain a variety of policies, even though 34 out of 40 are ultimately successful.
```

**[STEADY, line 508](../reference_papers/STEADY/IEEEexample.tex)** — claude WRD-04

```text
we found that most participants (74 out of 90) had a bias in their feedback in the second session as compared to the first.
```

**[SIDE, line 294](../reference_papers/Demonstration_sidetracks/main.tex)** — claude WRD-04

```text
Demonstration sidetracks comprised about 48\% of the overall task's recorded timesteps.
```

**[CHARM, line 393](../reference_papers/CHARM/ROMAN%202025.tex)** — claude WRD-04

```text
Robot experience and educational background exhibit correlation coefficients of 0.25 and 0.16 with feedback accuracy.
```

**[CHARM, line 119](../reference_papers/CHARM/ROMAN%202025.tex)** — claude WRD-05, v1 LIB-WRD-02

```text
We found that models with human characteristics and task statistics (CHARM) achieved significantly higher accuracy in predicting feedback values compared to models with only task statistics.
```

**[PROG, line 440](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude WRD-05

```text
Scalar feedback, on the other hand, changed dramatically in all these cases.
```

**[PH-EXP, line 137](../reference_papers/PHIRL/experiment.tex)** — claude WRD-05

```text
These results demonstrate that PHIRL learns effective rewards for RL agents, and is more reliable when the task horizon is longer or the demonstration quality is lower.
```

**[Progress, line 623](../reference_papers/Progress/Ro-MAN%202024.tex)** — v1 LIB-WRD-02

```text
We found that progress is strongly correlated with the learned reward function ($avg_{r} = 0.83 $) and the average correlation is significantly higher ($p < 0.001$, $BF > 1000$ ) than scalar feedback ($avg_{r} = 0.19$).
```

## Hypotheses and verdicts

[Merged guidance](hangs-writing-style-reference.md#hypotheses-and-verdicts)

**[PROG, line 251](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude WRD-06

```text
H1. Giving progress does not require extra workload and extra time compared to giving scalar feedback.
```

**[STEADY, line 494](../reference_papers/STEADY/IEEEexample.tex)** — claude WRD-06

```text
If exact matches are required, binary feedback is significantly more self-consistent than scalar feedback
```

**[STEADY, line 627](../reference_papers/STEADY/IEEEexample.tex)** — claude WRD-06

```text
so H3 is not supported.
```

## Possible explanations

[Merged guidance](hangs-writing-style-reference.md#possible-explanations)

**[SIDE, line 304](../reference_papers/Demonstration_sidetracks/main.tex)** — claude WRD-07

```text
This is likely due to the different sub-goals of different task phases, along with a change in the control pattern for participants
```

**[STEADY, line 510](../reference_papers/STEADY/IEEEexample.tex)** — claude WRD-07

```text
This might be because the task is relatively simple and participants expected the robot to perform well on the task.
```

**[PH-EXP, line 207](../reference_papers/PHIRL/experiment.tex)** — claude WRD-07

```text
This reward hacking is likely caused by an imbalanced reward design and a bottleneck in the task.
```

**[STEADY, line 831](../reference_papers/STEADY/IEEEexample.tex)** — claude WRD-07

```text
This explains why learning from multiple participants is likely to be difficult and suggests that
```

## Limitations and future work

[Merged guidance](hangs-writing-style-reference.md#limitations-and-future-work)

**[SIDE, line 364](../reference_papers/Demonstration_sidetracks/main.tex)** — claude WRD-09

```text
One limitation of this work is that we only used demonstrations from one task and one robot.
```

**[STEADY, line 858](../reference_papers/STEADY/IEEEexample.tex)** — claude WRD-09, v1 LIB-STY-06

```text
Repeating the robot behaviors only once was necessary to prevent participants from becoming aware that clips were repeating, but this limits our ability to understand the full range of possible changes in feedback dynamics.
```

**[STEADY, line 859](../reference_papers/STEADY/IEEEexample.tex)** — claude WRD-09

```text
Future work could investigate longer-term changes in feedback and new methods for stabilizing dynamics over long periods of time.
```

**[CHARM, line 472](../reference_papers/CHARM/ROMAN%202025.tex)** — v1 LIB-STY-06

```text
However, the feedback delay data might not be representative for continuous interactions. Future work should further extend this work to collect feedback from both paused and un- paused conditions, improving the representativeness of the data.
```

**[PHIRL, line 19](../reference_papers/PHIRL/conclusion.tex)** — v1 LIB-STY-06

```text
Our method assumes that the task has a finite horizon or a complete status, making it unsuitable for tasks with an infinite horizon or cyclic observations, such as ant\_walk from DeepMind Control Suite \cite{tassa2018deepmind}.
```

## Contribution statements

[Merged guidance](hangs-writing-style-reference.md#contribution-statements)

**[PROG, line 149](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude WRD-10

```text
The main contribution of this work is to demonstrate that *progress* has information beyond rating and ranking, and has great potential in interactive learning.
```

**[SIDE, line 126](../reference_papers/Demonstration_sidetracks/main.tex)** — claude WRD-10

```text
To the best of our knowledge, this is the first work that systematically characterizes non-experts' non-optimal manipulation patterns when providing demonstrations.
```

**[PROG, line 96](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude WRD-10

```text
An additional contribution of our work is a dataset of 40 non-expert demonstrations from the public space study through an ice cream topping-adding task
```

## Established dissertation terminology

[Merged guidance](hangs-writing-style-reference.md#established-dissertation-terminology)

**[PROG, line 93](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude WRD-11

```text
In this work, we characterize and test a little-used teaching signal: *progress*, designed to represent the completion percentage of a task.
```

**[PROG, line 218](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude WRD-11

```text
We characterize *progress* as the accumulative task completion rate over a task based on the current observation, ranging from totally incomplete to complete fully.
```

**[SIDE, line 115](../reference_papers/Demonstration_sidetracks/main.tex)** — claude WRD-11

```text
we designed a graphical interface and an open-coded book, annotated the demonstrations with two robot experts, and cross-validated the labels with a third expert.
```

## Shared references and user scales

[Merged guidance](hangs-writing-style-reference.md#shared-references-and-user-scales)

**[Progress, line 222](../reference_papers/Progress/Ro-MAN%202024.tex)** — v1 LIB-WRD-06

```text
users can use start states and finish states as references.
```

**[Progress, line 226](../reference_papers/Progress/Ro-MAN%202024.tex)** — v1 LIB-WRD-06

```text
A \textit{progress} value of 0 indicates that the task has not yet begun, while a value of 100 signifies task completion.
```

**[PHIRL, line 126](../reference_papers/PHIRL/methodology.tex)** — v1 LIB-WRD-06

```text
Note that in this condition specifically, $s_i, s_{i+1}, s_j$, and $s_{j+1}$ are preferably from the same demonstration $D$ since different users might scale \textit{progress} differently.
```

## Conditions attached to benefits

[Merged guidance](hangs-writing-style-reference.md#conditions-attached-to-benefits)

**[STEADY, line 125](../reference_papers/STEADY/IEEEexample.tex)** — v1 LIB-WRD-04

```text
we compare scalar and binary feedback, and demonstrate that scalar feedback benefits learning when properly handled.
```

**[Progress, line 220](../reference_papers/Progress/Ro-MAN%202024.tex)** — v1 LIB-WRD-04

```text
\textit{A teaching signal would be more robust to sub-optimal demonstrations and more consistent among users if human teachers could have objective references while providing the teaching signal. }
```

## Practical purpose

[Merged guidance](hangs-writing-style-reference.md#practical-purpose)

**[CHARM, line 71](../reference_papers/CHARM/ROMAN%202025.tex)** — claude STY-05

```text
Oversimplifying human feedback patterns will introduce a lab-to-real-world discrepancy and result in a performance drop for the learning algorithms.
```

**[PH-INT, line 30](../reference_papers/PHIRL/introduction.tex)** — claude STY-05

```text
In this setting, human-in-the-loop teaching effort, rather than demonstrations, has become the more expensive resource.
```

**[PROG, line 117](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude STY-05

```text
Perfect demonstrations are hard to obtain while purely learning from human feedback requires many human labels, often obtained at significant time and expense.
```

**[RSS Pioneers prospectus, line 36](../reference_papers/prospectus/RSS%20Pioneers%202026.tex)** — v1 LIB-STY-01

```text
To integrate robots into our everyday lives, it is essential for them to learn and adapt to novices.
```

**[Progress, line 211](../reference_papers/Progress/Ro-MAN%202024.tex)** — v1 LIB-STY-01

```text
Our goal is to improve learning from human feedback with a new teaching signal: progress.
```

## Direct subjects and concrete details

[Merged guidance](hangs-writing-style-reference.md#direct-subjects-and-concrete-details)

**[CHARM, line 55](../reference_papers/CHARM/ROMAN%202025.tex)** — claude STY-01

```text
We conducted a public space study with two long-horizon tasks and 46 participants.
```

**[STEADY, line 126](../reference_papers/STEADY/IEEEexample.tex)** — claude STY-01

```text
We collected binary or scalar feedback respectively from two groups of crowdworkers on a robot task.
```

**[PH-EXP, line 189](../reference_papers/PHIRL/experiment.tex)** — claude STY-01

```text
The robot repeatedly picks up the block, lifts it, and then drops it.
```

**[PROG, line 551](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude STY-03

```text
For instance, we observed that 14 participants slightly shook the topping jar to test if the gripper firmly held the jar when picking the jar, and 17 participants poured a few toppings out first to see if the jar was right above the ice cream when pouring the toppings.
```

**[STEADY, line 158](../reference_papers/STEADY/IEEEexample.tex)** — claude STY-03

```text
For example, on a scale of 10, the distance from 5 to 7 may be perceived as different from the distance from 3 to 5 although they are numerically the same.
```

**[SIDE, line 354](../reference_papers/Demonstration_sidetracks/main.tex)** — claude STY-03

```text
For instance, in our experiment, participants controlled the robot using an Xbox controller, and each button or joystick controlled one dimension of freedom.
```

## Describing human teaching without blame

[Merged guidance](hangs-writing-style-reference.md#describing-human-teaching-without-blame)

**[SIDE, line 175](../reference_papers/Demonstration_sidetracks/main.tex)** — claude STY-02

```text
However, not all imperfect behaviors are meaningless.
```

**[RSS, line 94](../reference_papers/prospectus/RSS%20Pioneers%202026.tex)** — claude STY-02

```text
We found that non-expert demonstrations, while noisy, do not necessarily mean failures or errors.
```

**[SIDE, line 188](../reference_papers/Demonstration_sidetracks/main.tex)** — claude STY-02

```text
humans are limited by the control interface, reaction time, and perception accuracy.
```

**[RSS Pioneers prospectus, line 26](../reference_papers/prospectus/RSS%20Pioneers%202026.tex)** — v1 LIB-STY-03

```text
However, expecting all of the users, especially those with limited experience with robots, to always provide high-quality teaching is impractical.
```

**[Demonstration Sidetracks, line 188](../reference_papers/Demonstration_sidetracks/main.tex)** — v1 LIB-STY-03

```text
However, unlike trained agents or oracles, which can control all action dimensions instantly and are either provided with accurate observation or trained to reduce perception error, humans are limited by the control interface, reaction time, and perception accuracy.
```

## Explaining the mechanism

[Merged guidance](hangs-writing-style-reference.md#explaining-the-mechanism)

**[STEADY, line 196](../reference_papers/STEADY/IEEEexample.tex)** — v1 LIB-STY-04

```text
The key insight of STEADY is to use a multi-distributional model for scalar feedback,  re-normalizing noisy scalar feedback to confidence scores (i.e. more precise magnitudes) and recovering positive/negative labels.
```

**[PHIRL, line 36](../reference_papers/PHIRL/introduction.tex)** — v1 LIB-STY-04

```text
Our key intuition is that \textbf{the rewards inferred from demonstrations should be consistent with the annotations of the demonstrations.}
```

## Observation interpretation and explanation

[Merged guidance](hangs-writing-style-reference.md#observation-interpretation-and-explanation)

**[SIDE, line 327](../reference_papers/Demonstration_sidetracks/main.tex)** — claude STY-04

```text
This is possibly due to the requirement for control accuracy, which resulted in more alignment to get to the desired positions and more pauses for reaction.
```

**[STEADY, line 419](../reference_papers/STEADY/IEEEexample.tex)** — claude STY-04

```text
This suggests that asking participants to give scalar feedback did not substantially increase the participant's effort, likely because scalar feedback is common in daily life.
```

**[CHARM, line 467](../reference_papers/CHARM/ROMAN%202025.tex)** — claude STY-04

```text
One is that the relationship between human characteristics and feedback patterns might not be linear, and multiple domains of human characteristics can jointly affect human feedback.
```

**[CHARM, line 394](../reference_papers/CHARM/ROMAN%202025.tex)** — v1 LIB-STY-05

```text
This suggests that participants with relevant educational backgrounds or greater robot experience tend to provide feedback that is more accurate in direction (e.g., positive vs. negative).
```

**[Demonstration Sidetracks, line 327](../reference_papers/Demonstration_sidetracks/main.tex)** — v1 LIB-STY-05

```text
This suggests that \thingname{}, especially \textit{Alignment}, are more likely to happen when approaching a target object. This is possibly due to the requirement for control accuracy, which resulted in more alignment to get to the desired positions and more pauses for reaction.
```

## Emphasis

[Merged guidance](hangs-writing-style-reference.md#emphasis)

**[SIDE, line 349](../reference_papers/Demonstration_sidetracks/main.tex)** — claude STY-06

```text
We found that human imperfections when giving demonstrations are not just simple noise or randomly distributed.
```

**[PH-INT, line 36](../reference_papers/PHIRL/introduction.tex)** — claude STY-06

```text
Our key intuition is that the rewards inferred from demonstrations should be consistent with the annotations of the demonstrations.
```

**[PROG, line 440](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude STY-06

```text
Participants used scalar feedback to indicate if a demonstration was clean and good, but the possibility that the errors were 'harmless explorations' or 'fixable mistakes' is not captured by scalar feedback.
```

## Literal wording

[Merged guidance](hangs-writing-style-reference.md#literal-wording)

**[PH-INT, line 37](../reference_papers/PHIRL/introduction.tex)** — claude STY-07

```text
This process mimics human learning: much like a student cross-referencing answers to correct their own solutions, the method generates a potential reward function and compares it against human feedback to refine its learned rewards.
```

**[PROG, line 556](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude STY-07

```text
The most common faulty cases are similar to the Failure scenario and the Unaware scenario we used in our online study, which confirmed the validity of the design of our online study.
```

## One main job and varied sentence length

[Merged guidance](hangs-writing-style-reference.md#one-main-job-and-varied-sentence-length)

**[SIDE, line 222](../reference_papers/Demonstration_sidetracks/main.tex)** — claude SEN-01

```text
Participants were recruited from random people walking past the experiment setup.
```

**[SIDE, line 224](../reference_papers/Demonstration_sidetracks/main.tex)** — claude SEN-01

```text
22 were male, 14 were female, and 4 preferred not to say.
```

**[STEADY, line 827](../reference_papers/STEADY/IEEEexample.tex)** — claude SEN-01

```text
Scalar feedback does change more than binary feedback, but tolerating small variations removes the effect.
```

**[PHIRL, line 6](../reference_papers/PHIRL/introduction.tex)** — v1 LIB-SEN-01

```text
While sparse rewards are intuitive to specify, they offer limited guidance during early exploration. Conversely, hand-crafted dense rewards accelerate learning, but designing them requires substantial engineering effort and tedious manual tuning \cite{xiang2024sc, ibrahim2024comprehensiveoverviewrewardengineering}.
```

**[Demonstration Sidetracks, line 95–96](../reference_papers/Demonstration_sidetracks/main.tex)** — v1 LIB-SEN-01

```text
Inaccurate modeling of non-expert behaviors can result in a performance gap between experiments and real-world scenarios.
Methods that work with oracle demonstrations might not perform well with real human demonstrations.
```

## A short verdict after the evidence

[Merged guidance](hangs-writing-style-reference.md#a-short-verdict-after-the-evidence)

**[PROG, line 378](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude SEN-02

```text
H2 is supported.
```

**[STEADY, line 325](../reference_papers/STEADY/IEEEexample.tex)** — claude SEN-02

```text
All of them answered *no*.
```

**[PH-INT, line 26](../reference_papers/PHIRL/introduction.tex)** — claude SEN-02

```text
The preference feedback is therefore uninformative.
```

**[SIDE, line 223](../reference_papers/Demonstration_sidetracks/main.tex)** — claude SEN-02

```text
40 participants were recruited in total.
```

## An example in a few connected sentences

[Merged guidance](hangs-writing-style-reference.md#an-example-in-a-few-connected-sentences)

**[PROG, line 594](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude SEN-03

```text
For instance, one participant failed to pour the toppings into the ice cream because the grasp point was not optimal.
```

**[PH-INT, line 26](../reference_papers/PHIRL/introduction.tex)** — claude SEN-03

```text
For instance, consider a pick-and-place task where the robot never manages to grasp the object.
```

**[PROG, line 634](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude SEN-03

```text
For example, a demonstration with a progress of 60 at the end should be ranked lower than a demonstration with a progress of 90.
```

**[PHIRL, line 26](../reference_papers/PHIRL/introduction.tex)** — v1 LIB-SEN-02

```text
Forcing users to pick a preferred trajectory does not always benefit learning. For instance, consider a pick-and-place task where the robot never manages to grasp the object. In this case, all sampled trajectory clips are undesirable. The preference feedback is therefore uninformative.
```

**[STEADY, line 158](../reference_papers/STEADY/IEEEexample.tex)** — v1 LIB-SEN-02

```text
For example, on a scale of 10, the distance from 5 to 7 may be perceived as different from the distance from 3 to 5 although they are numerically the same.
```

## Few colons and semicolons

[Merged guidance](hangs-writing-style-reference.md#few-colons-and-semicolons)

**[PROG, line 93](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude SEN-04

```text
In this work, we characterize and test a little-used teaching signal: *progress*
```

**[RSS, line 37](../reference_papers/prospectus/RSS%20Pioneers%202026.tex)** — claude SEN-04

```text
Additionally, learning from non-experts provides practical benefits:
```

**[PROG, line 126](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude SEN-04

```text
This is especially true for non-expert demonstrations: non-expert demonstrations can be noisy, multi-policy, and yet still succeed
```

## Parentheses for supporting specifics

[Merged guidance](hangs-writing-style-reference.md#parentheses-for-supporting-specifics)

**[STEADY, line 158](../reference_papers/STEADY/IEEEexample.tex)** — claude SEN-05

```text
Scalar feedback, on the other hand, is also naturally used in daily life (e.g., movie rating and product evaluation) but encodes information beyond that in binary feedback, such as ranking and magnitude, through a wider range of possible values.
```

**[STEADY, line 321](../reference_papers/STEADY/IEEEexample.tex)** — claude SEN-05

```text
each 100 clips consisted of six trajectories (three successes, three failures).
```

**[STEADY, line 196](../reference_papers/STEADY/IEEEexample.tex)** — claude SEN-05

```text
re-normalizing noisy scalar feedback to confidence scores (i.e. more precise magnitudes) and recovering positive/negative labels.
```

## Connectors with a clear job

[Merged guidance](hangs-writing-style-reference.md#connectors-with-a-clear-job)

**[SIDE, line 90](../reference_papers/Demonstration_sidetracks/main.tex)** — claude SEN-06

```text
Thus, in this work, we focus on identifying and investigating patterns of the noise in non-expert demonstrations.
```

**[PROG, line 576](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude SEN-06

```text
Moreover, progress is significantly more consistent across participants even though their demonstrations are multiple policies and in different quality
```

**[PH-METH, line 88](../reference_papers/PHIRL/methodology.tex)** — claude SEN-06

```text
Specifically,
```

## A roadmap with actual content

[Merged guidance](hangs-writing-style-reference.md#a-roadmap-with-actual-content)

**[PROG, line 215](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude SEN-07

```text
In this section, we first define progress, and then introduce our hypothesis.
```

**[CHARM, line 316](../reference_papers/CHARM/ROMAN%202025.tex)** — claude SEN-07

```text
In this section, we first present the data we collected from 46 participants in our public space study.
```

**[SIDE, line 321](../reference_papers/Demonstration_sidetracks/main.tex)** — claude SEN-07

```text
In this subsection, we examine the spatial distribution of demonstration sidetracks.
```

## Study actions leading to the analytical question

[Merged guidance](hangs-writing-style-reference.md#study-actions-leading-to-the-analytical-question)

**[CHARM, line 115](../reference_papers/CHARM/ROMAN%202025.tex)** — v1 LIB-SEN-04

```text
We designed a questionnaire capturing six key aspects of human characteristics that are mentioned to be correlated with human feedback patterns in prior work. We conducted a public space study with 46 participants, with each participant providing feedback on a nut assembly task and a coffee preparation task. Our results indicate that while our selected human characteristics have a low correlation with feedback delay, they are fairly correlated with feedback values.
```

**[STEADY, line 274](../reference_papers/STEADY/IEEEexample.tex)** — v1 LIB-SEN-04

```text
We conducted an online user study to investigate binary and scalar feedback consistency over time and between users (\autoref{fig:bp}).
```

**[STEADY, line 275](../reference_papers/STEADY/IEEEexample.tex)** — v1 LIB-SEN-04

```text
Two groups of participants were asked to evaluate the robot's performance while the robot was completing a button-pressing task.
```

**[STEADY, line 277](../reference_papers/STEADY/IEEEexample.tex)** — v1 LIB-SEN-04

```text
The robot performed six trajectories twice, allowing us to detect changes in feedback by comparing the difference in feedback between the two sessions. All users saw the same trajectories, allowing us to detect variation in feedback between users on the same task with the same feedback type.
```

## An intuition leading to an operation

[Merged guidance](hangs-writing-style-reference.md#an-intuition-leading-to-an-operation)

**[CHARM, line 73–74](../reference_papers/CHARM/ROMAN%202025.tex)** — v1 LIB-SEN-05

```text
Our key insight is that
\textit{human feedback is not only associated with the task and the agent's performance, but also affected by human characteristics.}
```

**[STEADY, line 656–658](../reference_papers/STEADY/IEEEexample.tex)** — v1 LIB-SEN-05

```text
Our key intuitions are:
First, human evaluations often involve associating certain qualities with certain ranges. These are subject to variation,
and each range can be viewed as one distribution.
```

**[PHIRL, line 36](../reference_papers/PHIRL/introduction.tex)** — v1 LIB-SEN-05

```text
Our key intuition is that \textbf{the rewards inferred from demonstrations should be consistent with the annotations of the demonstrations.}
```

**[CHARM, line 75](../reference_papers/CHARM/ROMAN%202025.tex)** — v1 LIB-SEN-05

```text
In this work, we therefore concern ourselves with the problem of investigating the relation between human feedback patterns and human characteristics.
```

**[STEADY, line 660](../reference_papers/STEADY/IEEEexample.tex)** — v1 LIB-SEN-05

```text
Second, since some robot behaviors are more preferred than others, feedback distributions can be separated into at least two classes, preferable (positive) and non-preferable (negative).
```

**[STEADY, line 661–664](../reference_papers/STEADY/IEEEexample.tex)** — v1 LIB-SEN-05

```text
Based on the key intuitions,
STEADY re-constructs feedback distributions,
labels scalar feedback with binary labels,
and remaps the magnitude of the feedback in a more algorithmically useful way based on feedback statistics.
```

## Concession with while

[Merged guidance](hangs-writing-style-reference.md#concession-with-while)

**[PH-INT, line 6](../reference_papers/PHIRL/introduction.tex)** — claude STR-01

```text
While sparse rewards are intuitive to specify, they offer limited guidance during early exploration.
```

**[PROG, line 371](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude STR-01

```text
While scalar feedback and progress can both describe the quality of a demonstration, progress and scalar feedback focus on different information.
```

**[PROG, line 475](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude STR-01

```text
While progress can be effective in being used along with expert demonstrations,
```

## Matched factors and endpoints

[Merged guidance](hangs-writing-style-reference.md#matched-factors-and-endpoints)

**[CHARM, line 56](../reference_papers/CHARM/ROMAN%202025.tex)** — claude STR-02

```text
We found that feedback patterns are not only correlated with task statistics, such as rewards, but also correlated with participants' characteristics
```

**[RSS, line 84](../reference_papers/prospectus/RSS%20Pioneers%202026.tex)** — claude STR-02

```text
these factors are not only related to the tasks but also are intrinsic to the human teachers.
```

**[PROG, line 550](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude STR-02

```text
We also observed that the noise in the demonstrations is not only teleoperating errors but also explorations.
```

**[Progress, line 226](../reference_papers/Progress/Ro-MAN%202024.tex)** — v1 LIB-SYN-03

```text
A \textit{progress} value of 0 indicates that the task has not yet begun, while a value of 100 signifies task completion.
```

**[CHARM, line 74](../reference_papers/CHARM/ROMAN%202025.tex)** — v1 LIB-SYN-03

```text
\textit{human feedback is not only associated with the task and the agent's performance, but also affected by human characteristics.}
```

**[RSS Pioneers prospectus, line 67–69](../reference_papers/prospectus/RSS%20Pioneers%202026.tex)** — v1 LIB-SYN-03

```text
\textit{systematically modeling human factors in human feedback and human demonstrations}
and 
\textit{utilizing complementary information from multiple types of human teaching}.
```

## A specific case introduced by especially

[Merged guidance](hangs-writing-style-reference.md#a-specific-case-introduced-by-especially)

**[PROG, line 105](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude STR-03

```text
making it crucial to learn from users, especially non-expert users.
```

**[CHARM, line 56](../reference_papers/CHARM/ROMAN%202025.tex)** — claude STR-03

```text
but also correlated with participants' characteristics, especially robot experience and educational background.
```

**[PH-CON, line 21](../reference_papers/PHIRL/conclusion.tex)** — claude STR-03

```text
especially when the number of human feedback labels is limited.
```

## A literal alternative

[Merged guidance](hangs-writing-style-reference.md#a-literal-alternative)

**[SIDE, line 73](../reference_papers/Demonstration_sidetracks/main.tex)** — claude STR-04

```text
We found that instead of being random and rare, demonstration sidetracks frequently appear in non-expert demonstrations across all participants
```

**[PH-INT, line 30](../reference_papers/PHIRL/introduction.tex)** — claude STR-04

```text
In this setting, human-in-the-loop teaching effort, rather than demonstrations, has become the more expensive resource.
```

**[PROG, line 233](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude STR-04

```text
with a trajectory instead of a single state to increase reliability.
```

## Purpose attached to an action

[Merged guidance](hangs-writing-style-reference.md#purpose-attached-to-an-action)

**[STEADY, line 489](../reference_papers/STEADY/IEEEexample.tex)** — claude STR-05

```text
To answer the question of whether participants are self-consistent,
```

**[CHARM, line 104](../reference_papers/CHARM/ROMAN%202025.tex)** — claude STR-05

```text
To bridge this gap, our work focuses on investigating the impact of human characteristics on feedback patterns and exploring if incorporating these attributes can improve predicting human feedback.
```

**[STEADY, line 302](../reference_papers/STEADY/IEEEexample.tex)** — claude STR-05

```text
We used a relatively simple task to reduce the cognitive load on solving the task and thus reduce feedback dynamics from confusion over the task.
```

**[CHARM, line 163](../reference_papers/CHARM/ROMAN%202025.tex)** — v1 LIB-SYN-05

```text
To explore this, we developed a questionnaire to capture six key domains of human characteristics and conducted a public study to collect both human feedback and their characteristics.
```

**[STEADY, line 277](../reference_papers/STEADY/IEEEexample.tex)** — v1 LIB-SYN-05

```text
The robot performed six trajectories twice, allowing us to detect changes in feedback by comparing the difference in feedback between the two sessions. All users saw the same trajectories, allowing us to detect variation in feedback between users on the same task with the same feedback type.
```

## Parallel sentences for a comparison

[Merged guidance](hangs-writing-style-reference.md#parallel-sentences-for-a-comparison)

**[PH-ABS, line 68](../reference_papers/PHIRL/CoRL_2026_main.tex)** — claude STR-06, v1 LIB-SEN-03

```text
Human demonstrations provide dense policy-level information but sometimes lack local precision. Human feedback presents accurate local critiques, but offers sparse evaluations rather than direct policy guidance.
```

**[PROG, line 115](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude STR-06

```text
Human feedback carries relatively sparse and local information such as the correctness or a rating of a robot's action
```

**[PH-INT, line 6](../reference_papers/PHIRL/introduction.tex)** — claude STR-06

```text
Conversely, hand-crafted dense rewards accelerate learning, but designing them requires substantial engineering effort and tedious manual tuning
```

**[Progress, line 371](../reference_papers/Progress/Ro-MAN%202024.tex)** — v1 LIB-SEN-03

```text
While scalar feedback and progress can both describe the quality of a demonstration, progress and scalar feedback focus on different information.
```

**[Progress, line 373](../reference_papers/Progress/Ro-MAN%202024.tex)** — v1 LIB-SEN-03

```text
Progress describes the degree to what extent a task has been completed.
```

**[Progress, line 380](../reference_papers/Progress/Ro-MAN%202024.tex)** — v1 LIB-SEN-03

```text
Scalar feedback reflects the quality of a trajectory, and only a single trajectory.
```

**[CHARM, line 119](../reference_papers/CHARM/ROMAN%202025.tex)** — v1 LIB-SEN-03

```text
We found that models with human characteristics and task statistics (CHARM) achieved significantly higher accuracy in predicting feedback values compared to models with only task statistics.
```

## Known information leading to new information

[Merged guidance](hangs-writing-style-reference.md#known-information-leading-to-new-information)

**[SIDE, line 294](../reference_papers/Demonstration_sidetracks/main.tex)** — claude STR-07

```text
This suggests that, contrary to the common assumption that imperfections only take up a small part in non-expert demonstration, demonstration sidetracks are frequent and take up a large portion of the overall task demonstration.
```

**[CHARM, line 395](../reference_papers/CHARM/ROMAN%202025.tex)** — claude STR-07

```text
This indicates that participants with more robot experience or a relevant educational background also tend to provide feedback that is closer in value to the ground truth
```

**[PH-EXP, line 168](../reference_papers/PHIRL/experiment.tex)** — claude STR-07

```text
This shows that completion shaping is critical for learning when demonstrations fail.
```

**[STEADY, line 668–670](../reference_papers/STEADY/IEEEexample.tex)** — v1 LIB-SYN-07

```text
In an online learning setting,
the robot needs to learn from human feedback in real time and update its policy.
The feedback distributions thus also need to be updated after new feedback is added.
```

**[PHIRL, line 16–17](../reference_papers/PHIRL/methodology.tex)** — v1 LIB-SYN-07

```text
We use a recently-introduced human feedback form, \textit{progress} \cite{yu2025progressdidimake}, as the reference for reward function alignment. 
\textit{Progress} is a signal that describes the cumulative degree of task completion, ranging from fully incomplete to fully complete.
```

## Means expressed with by

[Merged guidance](hangs-writing-style-reference.md#means-expressed-with-by)

**[SIDE, line 302](../reference_papers/Demonstration_sidetracks/main.tex)** — claude STR-08

```text
However, we show that this assumption does not hold for actual human demonstrations by showing the relevance between demonstration sidetracks and the task's progress.
```

**[PH-METH, line 87](../reference_papers/PHIRL/methodology.tex)** — claude STR-08

```text
We improve the learned reward function by shaping it to align with *progress* annotations during reward learning.
```

**[RSS, line 90](../reference_papers/prospectus/RSS%20Pioneers%202026.tex)** — claude STR-08

```text
challenged this assumption by identifying frequent patterned imperfections in non-expert demonstrations.
```

## Procedural series and enumerations

[Merged guidance](hangs-writing-style-reference.md#procedural-series-and-enumerations)

**[STEADY, line 660](../reference_papers/STEADY/IEEEexample.tex)** — claude STR-09

```text
Second, since some robot behaviors are more preferred than others, feedback distributions can be separated into at least two classes, preferable (positive) and non-preferable (negative).
```

**[CHARM, line 468](../reference_papers/CHARM/ROMAN%202025.tex)** — claude STR-09

```text
The other one is that human characteristics are only one of the factors that affect human feedback values
```

**[RSS, line 96](../reference_papers/prospectus/RSS%20Pioneers%202026.tex)** — claude STR-09

```text
1) Pause, no input from the controller for a period of time; 2) Alignment, moving the robot back and forth to align the robot with a target object;
```

**[PHIRL, line 38](../reference_papers/PHIRL/introduction.tex)** — v1 LIB-SYN-04

```text
In PHIRL, we iteratively use an IRL algorithm to learn a reward function from demonstrations, calculate rewards over the annotated demonstrations, and then shape the learned reward function in four dimensions: temporal delta, magnitudes, potential, and completion.
```

**[Demonstration Sidetracks, line 114–115](../reference_papers/Demonstration_sidetracks/main.tex)** — v1 LIB-SYN-04

```text
To identify \thingname{} in the collected demonstrations,
 we designed a graphical interface and an open-coded book, annotated the demonstrations with two robot experts, and cross-validated the labels with a third expert.
```

## Definitions before notation

[Merged guidance](hangs-writing-style-reference.md#definitions-before-notation)

**[PH-METH, line 17](../reference_papers/PHIRL/methodology.tex)** — claude STR-10

```text
*Progress* is a signal that describes the cumulative degree of task completion, ranging from fully incomplete to fully complete.
```

**[SIDE, line 193](../reference_papers/Demonstration_sidetracks/main.tex)** — claude STR-10

```text
In this work, we define non-optimal behaviors in human demonstrations as *Demonstration Sidetracks*.
```

**[PROG, line 226](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude STR-10

```text
A *progress* value of 0 indicates that the task has not yet begun, while a value of 100 signifies task completion.
```

**[PHIRL, line 17](../reference_papers/PHIRL/methodology.tex)** — v1 LIB-SYN-01

```text
\textit{Progress} is a signal that describes the cumulative degree of task completion, ranging from fully incomplete to fully complete.
```

**[CHARM, line 174](../reference_papers/CHARM/ROMAN%202025.tex)** — v1 LIB-SYN-01

```text
We represent feedback delay as a non-negative number $D$ that denotes the time difference between the end of the robot trajectory and the moment feedback is provided.
```

## Local reasons and governing conditions

[Merged guidance](hangs-writing-style-reference.md#local-reasons-and-governing-conditions)

**[PH-METH, line 126](../reference_papers/PHIRL/methodology.tex)** — claude STR-11

```text
since different users might scale *progress* differently.
```

**[RSS, line 131](../reference_papers/prospectus/RSS%20Pioneers%202026.tex)** — claude STR-11

```text
Our final stage is to utilize human feedback to enhance learning from demonstrations, as providing accurate feedback to a policy is easier and requires less expertise.
```

**[STEADY, line 125](../reference_papers/STEADY/IEEEexample.tex)** — claude STR-11

```text
we compare scalar and binary feedback, and demonstrate that scalar feedback benefits learning when properly handled.
```

**[PHIRL, line 143](../reference_papers/PHIRL/methodology.tex)** — v1 LIB-SYN-02

```text
If a state has higher \textit{progress}, the learned potential should also be higher.
```

**[PHIRL, line 54](../reference_papers/PHIRL/methodology.tex)** — v1 LIB-SYN-02

```text
If we assume that the demonstrations are from an optimal policy $\pi^*$, we can then interpret the IRL problem as a maximum likelihood problem:
```

**[STEADY, line 494](../reference_papers/STEADY/IEEEexample.tex)** — v1 LIB-SYN-02

```text
However, when we increase the threshold of agreement, the self-consistency of scalar feedback improves, and by a threshold of $\pm 2$ the difference with binary feedback vanishes ($p = 0.775$).
```

**[STEADY, line 494](../reference_papers/STEADY/IEEEexample.tex)** — v1 LIB-SYN-02

```text
If exact matches are required, binary feedback is significantly more self-consistent than scalar feedback ($p < 0.0001$ for threshold $0$ and $\pm1$), which supports \textbf{H1}.
```

**[PHIRL, line 126](../reference_papers/PHIRL/methodology.tex)** — v1 LIB-SYN-06

```text
Note that in this condition specifically, $s_i, s_{i+1}, s_j$, and $s_{j+1}$ are preferably from the same demonstration $D$ since different users might scale \textit{progress} differently.
```

**[STEADY, line 671](../reference_papers/STEADY/IEEEexample.tex)** — v1 LIB-SYN-06

```text
Since there is no pre-labeled scalar feedback, we use a heuristic method to initialize the distributions.
```

## An introduction built around a consequential assumption

[Merged guidance](hangs-writing-style-reference.md#an-introduction-built-around-a-consequential-assumption)

**[SIDE, line 85](../reference_papers/Demonstration_sidetracks/main.tex)** — claude STO-01

```text
One challenge in LfD is that high-quality demonstrations are hard to obtain
```

**[SIDE, line 89](../reference_papers/Demonstration_sidetracks/main.tex)** — claude STO-01

```text
Our key insights are that: *not all non-optimal behaviors from non-experts are random errors and randomly distributed: instead they appear in structured ways.*
```

**[SIDE, line 127](../reference_papers/Demonstration_sidetracks/main.tex)** — claude STO-01

```text
Our work will be beneficial for future LfD algorithm development to better learn from noisy demonstrations and for oracle design to reduce the gap between in-lab datasets and real-world demonstrations.
```

**[RSS, line 89](../reference_papers/prospectus/RSS%20Pioneers%202026.tex)** — claude STO-02

```text
often assumes that non-optimal behaviors in demonstrations are random errors
```

**[SIDE, line 302](../reference_papers/Demonstration_sidetracks/main.tex)** — claude STO-02

```text
One key assumption when using simple distributions to sample noise is that noise is independent from the task itself.
```

**[SIDE, line 294](../reference_papers/Demonstration_sidetracks/main.tex)** — claude STO-02

```text
contrary to the common assumption that imperfections only take up a small part in non-expert demonstration
```

**[CHARM, line 101](../reference_papers/CHARM/ROMAN%202025.tex)** — v1 LIB-NAR-01

```text
Assuming users would consistently provide feedback only based on the task or relying on oracles to provide instant, bias-free feedback oversimplifies how humans interact with robots \cite{krening2018interaction}.
```

**[Demonstration Sidetracks, line 190](../reference_papers/Demonstration_sidetracks/main.tex)** — v1 LIB-NAR-01

```text
Intuitively, in order to complete the task while maintaining a reasonable mental workload, humans accommodate these limitations by controlling a limited degree of freedom at a time, performing redundant but harmless behaviors, or spending more time while giving demonstrations.
```

## A study finding leading to a method

[Merged guidance](hangs-writing-style-reference.md#a-study-finding-leading-to-a-method)

**[CHARM, line 73](../reference_papers/CHARM/ROMAN%202025.tex)** — claude STO-03

```text
Our key insight is that
```

**[CHARM, line 74](../reference_papers/CHARM/ROMAN%202025.tex)** — claude STO-03

```text
*human feedback is not only associated with the task and the agent's performance, but also affected by human characteristics.*
```

**[PROG, line 220](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude STO-03

```text
*A teaching signal would be more robust to sub-optimal demonstrations and more consistent among users if human teachers could have objective references while providing the teaching signal.*
```

**[STEADY, line 280](../reference_papers/STEADY/IEEEexample.tex)** — claude STO-04, v1 LIB-NAR-02

```text
These results, and the data collected, motivate and enable the development and evaluation of our STEADY algorithm.
```

**[RSS, line 117](../reference_papers/prospectus/RSS%20Pioneers%202026.tex)** — claude STO-04

```text
We were thus motivated to propose a method that dynamically rescales scalar feedback into binary feedback with confidence degrees.
```

**[STEADY, line 641](../reference_papers/STEADY/IEEEexample.tex)** — claude STO-04

```text
The user study results suggest that scalar feedback is as good as binary feedback, but noise needs to be mitigated.
```

**[Progress, line 220](../reference_papers/Progress/Ro-MAN%202024.tex)** — v1 LIB-NAR-02

```text
A teaching signal would be more robust to sub-optimal demonstrations and more consistent among users if human teachers could have objective references while providing the teaching signal.
```

**[Progress, line 222](../reference_papers/Progress/Ro-MAN%202024.tex)** — v1 LIB-NAR-02

```text
users can use start states and finish states as references.
```

## Teaching a method from meaning to evaluation

[Merged guidance](hangs-writing-style-reference.md#teaching-a-method-from-meaning-to-evaluation)

**[PHIRL, line 34](../reference_papers/PHIRL/introduction.tex)** — v1 LIB-NAR-04

```text
\textit{Progress} describes the cumulative task completion based on the task observation.
```

**[PHIRL, line 38](../reference_papers/PHIRL/introduction.tex)** — v1 LIB-NAR-04

```text
In PHIRL, we iteratively use an IRL algorithm to learn a reward function from demonstrations, calculate rewards over the annotated demonstrations, and then shape the learned reward function in four dimensions: temporal delta, magnitudes, potential, and completion.
```

**[PHIRL, line 40](../reference_papers/PHIRL/introduction.tex)** — v1 LIB-NAR-04

```text
We validate PHIRL with two robot tasks from Robosuite \cite{zhu2025robosuitemodularsimulationframework} and one real robot task with four baselines.
```

## The three stage dissertation arc

[Merged guidance](hangs-writing-style-reference.md#the-three-stage-dissertation-arc)

**[RSS, line 15](../reference_papers/prospectus/RSS%20Pioneers%202026.tex)** — claude STO-05

```text
Embracing Imperfection: Understanding, Mitigating, and Leveraging Non-expert Teaching
```

**[RSS, line 84](../reference_papers/prospectus/RSS%20Pioneers%202026.tex)** — claude STO-05

```text
Our first step focuses on examining human factors in human teaching robots that make human teaching noisy
```

**[RSS, line 131](../reference_papers/prospectus/RSS%20Pioneers%202026.tex)** — claude STO-05

```text
Our final stage is to utilize human feedback to enhance learning from demonstrations
```

**[RSS Pioneers prospectus, line 84](../reference_papers/prospectus/RSS%20Pioneers%202026.tex)** — v1 LIB-NAR-06

```text
Our first step focuses on examining human factors in human teaching robots that make human teaching noisy, where these factors are not only related to the tasks but also are intrinsic to the human teachers.
```

**[RSS Pioneers prospectus, line 107](../reference_papers/prospectus/RSS%20Pioneers%202026.tex)** — v1 LIB-NAR-06

```text
Our second step targets to improve learning from human feedback by mitigating noise in scalar feedback and proposing new feedback modality.
```

**[RSS Pioneers prospectus, line 130](../reference_papers/prospectus/RSS%20Pioneers%202026.tex)** — v1 LIB-NAR-06

```text
In the above work, we identified patterned imperfections in human feedback and demonstrations, and introduced a non-expert-friendly teaching signal \textit{progress} for evaluating demonstrations.
```

## A hypothetical scenario that explains a problem

[Merged guidance](hangs-writing-style-reference.md#a-hypothetical-scenario-that-explains-a-problem)

**[PROG, line 616](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude STO-06

```text
For instance, a cleaning robot gets a +1 reward every time it cleans a room. The robot, instead of cleaning one room and going to the next room, repetitively ejects dirt in a room, then cleans it, and thus achieves high rewards.
```

**[PH-INT, line 26](../reference_papers/PHIRL/introduction.tex)** — claude STO-06

```text
For instance, consider a pick-and-place task where the robot never manages to grasp the object. In this case, all sampled trajectory clips are undesirable.
```

**[PH-METH, line 108](../reference_papers/PHIRL/methodology.tex)** — claude STO-06

```text
Some steps, like picking up the target object, are inherently more progressive than simply moving closer.
```

**[Progress, line 594](../reference_papers/Progress/Ro-MAN%202024.tex)** — v1 LIB-NAR-03

```text
For instance, one participant failed to pour the toppings into the ice cream because the grasp point was not optimal.
```

**[Progress, line 595](../reference_papers/Progress/Ro-MAN%202024.tex)** — v1 LIB-NAR-03

```text
Then the participant decided to reset the arm to the initial position, demonstrated the entire task from the beginning again, and succeeded.
```

**[PHIRL, line 26](../reference_papers/PHIRL/introduction.tex)** — v1 LIB-NAR-03

```text
Forcing users to pick a preferred trajectory does not always benefit learning. For instance, consider a pick-and-place task where the robot never manages to grasp the object. In this case, all sampled trajectory clips are undesirable. The preference feedback is therefore uninformative.
```

## Headings that name the question or finding

[Merged guidance](hangs-writing-style-reference.md#headings-that-name-the-question-or-finding)

**[PROG, line 316](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude STO-07

```text
Giving progress is not time-consuming and not hard
```

**[CHARM, line 403](../reference_papers/CHARM/ROMAN%202025.tex)** — claude STO-07

```text
Including Human Characteristics Improves Feedback Prediction Accuracy
```

**[PH-EXP, line 127](../reference_papers/PHIRL/experiment.tex)** — claude STO-07

```text
PHIRL Outperforms Baselines
```

**[STEADY, line 485](../reference_papers/STEADY/IEEEexample.tex)** — claude STO-07

```text
Analysis of H1: Did participants give consistent feedback in the two sessions?
```

## A results paragraph answering one comparison

[Merged guidance](hangs-writing-style-reference.md#a-results-paragraph-answering-one-comparison)

**[PROG, line 240](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude STO-08

```text
We expect that people naturally estimate task completion in their daily lives, so progress should be not hard to give.
```

**[PROG, line 320](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude STO-08

```text
The average completion time is lower for progress by
```

**[PROG, line 421](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude STO-08

```text
H3 is supported.
```

**[CHARM, line 448](../reference_papers/CHARM/ROMAN%202025.tex)** — v1 LIB-NAR-05

```text
the model trained with only task statistics has an accuracy of 32.59\% and the model trained with task statistics and human characteristics (CHARM) has an accuracy of 55.83\%.
```

**[CHARM, line 454](../reference_papers/CHARM/ROMAN%202025.tex)** — v1 LIB-NAR-05

```text
Overall, our results suggest that our selected human characteristics do associate with feedback values, and including these characteristics could help the machine learning model better capture the underlining human feedback value patterns.
```

## An unexpected result and possible reasons

[Merged guidance](hangs-writing-style-reference.md#an-unexpected-result-and-possible-reasons)

**[CHARM, line 465](../reference_papers/CHARM/ROMAN%202025.tex)** — claude STO-09

```text
One interesting finding is that while there were no strong correlations between the selected human characteristics and human feedback values, our experiment results demonstrated that incorporating human characteristics into training leads to a significant improvement in modeling human feedback patterns.
```

**[CHARM, line 466](../reference_papers/CHARM/ROMAN%202025.tex)** — claude STO-09

```text
We assume this is because of two reasons.
```

## Discussion synthesis and its boundary

[Merged guidance](hangs-writing-style-reference.md#discussion-synthesis-and-its-boundary)

**[STEADY, line 827](../reference_papers/STEADY/IEEEexample.tex)** — claude STO-10

```text
The results above demonstrate that scalar feedback is not inherently worse than binary feedback as a teaching signal even without stabilization.
```

**[STEADY, line 856](../reference_papers/STEADY/IEEEexample.tex)** — claude STO-10

```text
One limitation of our work is that the experiments were relatively short-term and only repeated each clip once.
```

**[STEADY, line 863](../reference_papers/STEADY/IEEEexample.tex)** — claude STO-10

```text
Overall, our work suggests that HRI and interactive RL practitioners should give scalar feedback more attention
```

**[SIDE, line 374](../reference_papers/Demonstration_sidetracks/main.tex)** — claude STO-10

```text
We believe this work lays a foundation for bridging the gap between laboratory-based setups and real-world scenarios.
```

**[CHARM, line 445](../reference_papers/CHARM/ROMAN%202025.tex)** — v1 LIB-NAR-07

```text
Both models performed poorly and including human characteristics showed minimal improvement. These results are consistent with our earlier correlation analysis.
```

**[CHARM, line 467](../reference_papers/CHARM/ROMAN%202025.tex)** — v1 LIB-NAR-07

```text
One is that the relationship between human characteristics and feedback patterns might not be linear, and multiple domains of human characteristics can jointly affect human feedback.
```

**[STEADY, line 859](../reference_papers/STEADY/IEEEexample.tex)** — v1 LIB-NAR-07

```text
Future work could investigate longer-term changes in feedback and new methods for stabilizing dynamics over long periods of time.
```

## Related work ending with the specific difference

[Merged guidance](hangs-writing-style-reference.md#related-work-ending-with-the-specific-difference)

**[PROG, line 202](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude STO-11

```text
Our work differs from prior work by focusing on non-experts.
```

**[PH-BG, line 46](../reference_papers/PHIRL/background.tex)** — claude STO-11

```text
Our work differs from prior work by improving the data efficiency and reducing human-in-the-loop effort.
```

**[SIDE, line 159](../reference_papers/Demonstration_sidetracks/main.tex)** — claude STO-11

```text
Our work differs from prior work by recognizing that non-optimal behaviors are natural for human manipulation
```

## An observed episode in action order

[Merged guidance](hangs-writing-style-reference.md#an-observed-episode-in-action-order)

**[PROG, line 595](../reference_papers/Progress/Ro-MAN%202024.tex)** — claude STO-12

```text
Then the participant decided to reset the arm to the initial position, demonstrated the entire task from the beginning again, and succeeded.
```

**[PH-EXP, line 206](../reference_papers/PHIRL/experiment.tex)** — claude STO-12

```text
Instead of picking up the can and placing it in the target bin, the robot navigated to the can, closed the gripper, and poked the can with the gripper.
```

**[STEADY, line 324](../reference_papers/STEADY/IEEEexample.tex)** — claude STO-12

```text
we conducted a pilot study by recruiting three robot experts from a robotic lab. We asked if they were aware that all clips were repeated once.
```

**[Progress, line 594–596](../reference_papers/Progress/Ro-MAN%202024.tex)** — v1 LIB-SEN-06

```text
For instance, one participant failed to pour the toppings into the ice cream because the grasp point was not optimal. 
Then the participant decided to reset the arm to the initial position, demonstrated the entire task from the beginning again, and succeeded.
We plot the trajectory for that demonstration along with progress and scalar feedback, shown in \autoref{fig:p31}.
```
