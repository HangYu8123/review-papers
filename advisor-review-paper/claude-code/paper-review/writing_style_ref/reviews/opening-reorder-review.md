# Chapter openings: sentences moved and cut (Chapters 3 to 7)

Review `opening-reorder-review` of the dissertation, from `waiting_for_review/opening-reorder-review`. Decided between October 15, 2026 and October 15, 2026. Decisions files: `opening-reorder-review.decisions.20261015-045314.json`.

[All reviews](../review-decisions.md) · [Weighted signals](../preference-signals.md) · [Main reference](../hangs-writing-style-reference.md)

| Outcome | Decided by Hang | Not decided by Hang |
| --- | ---: | ---: |
| Accepted as suggested | 8 | 0 |
| Accepted with Hang's edit | 1 | 0 |
| Declined | 9 | 0 |
| Notes from Hang | 0 | |

### C4-01

**Accepted** · weight 1 · Sentences moved · Chapter 4 · Categorizing Systematic Non-Optimality in Hu… · Chapter 4, `chapters/sidetracks.tex`, line 8

Suggestion: Let the gap lead straight into the key insight

Original:

~~~latex
However, few works have studied patterns in non-experts' behavior when giving demonstrations. Prior work often describes non-expert demonstrations using relatively simple patterns,  such as expert demonstrations with added noisy actions\cite{sasaki2020behavioral}, or expert policy mixing with random policies\cite{liu2022robust}, which fail to capture the diverse strategies or accommodation techniques non-experts use to succeed.
The results presented in \autoref{ch:charm} indicate that differences in the feedback that non-experts give are not simply random noise, but are associated with the characteristics of the teachers.
~~~

Accepted wording:

~~~latex
% [HY moved up one line, opening-reorder-review C4-01]
The results presented in \autoref{ch:charm} indicate that differences in the feedback that non-experts give are not simply random noise, but are associated with the characteristics of the teachers.
However, few works have studied patterns in non-experts' behavior when giving demonstrations. Prior work often describes non-expert demonstrations using relatively simple patterns,  such as expert demonstrations with added noisy actions\cite{sasaki2020behavioral}, or expert policy mixing with random policies\cite{liu2022robust}, which fail to capture the diverse strategies or accommodation techniques non-experts use to succeed.
~~~

Note written with the suggestion: Optional; the current order also works since your 04:28 edit. The Chapter 3 result now sits between the gap ("Prior work often describes non-expert demonstrations using relatively simple patterns, such as expert demonstrations with added noisy actions ... or expert policy mixing with random policies") and the key insight that answers it ("not all non-optimal behaviors from non-experts are randomly distributed errors. Instead, they appear in structured ways"). Moved up one line, it follows your new ending of the sentence before ("non-expert demonstrations are often viewed as noisy") with "not simply random noise"; "However, few works have studied patterns in non-experts' behavior when giving demonstrations" then contrasts what Chapter 3 found for feedback with what is missing for demonstrations, and the insight follows the gap directly. Keep the current order if you wrote "often viewed as noisy" to lead straight into "However, few works ..."; there the Chapter 3 result reads as the precedent for the insight. Both sentences are unchanged. Style reference: An introduction built around a consequential assumption (assumption, overlooked behavior, insight); Known information leading to new information.

### C4-02

**Accepted** · weight 1 · Repeated text cut · Chapter 4 · Categorizing Systematic Non-Optimality in Hu… · Chapter 4, `chapters/sidetracks.tex`, line 13

Suggestion: "This assumption" has nothing to refer to, and the data source is stated twice in a row

Original:

~~~latex
In this chapter, this assumption is examined using the 40 demonstrations from the public space study described in detail in \autoref{ch:progress}, which was originally conducted to validate the \textit{progress} signal.
~~~

Accepted wording:

~~~latex
% [HY removed] In this chapter, this assumption is examined using the 40 demonstrations from the public space study described in detail in \autoref{ch:progress}, which was originally conducted to validate the \textit{progress} signal.
~~~

Note written with the suggestion: The assumption this sentence examines ("One key assumption when using simple distributions to sample noise is that noise is independent from the task itself") is in Section 4.2.2, not in the opening, so "this assumption" points to nothing. The next sentence describes the same data again ("demonstrations of a long-horizon manipulation task provided by 40 non-experts in a public space study"), and Section 4.1.2 opens with where the data came from ("The demonstration data were collected as part of the validation study for progress in Chapter 6"), so the link to Chapter 6 is kept. After the cut the paragraph opens with "It analyzes demonstrations ...", whose "It" is "this chapter" in the last sentence of the paragraph above ("Thus, this chapter focuses on identifying and investigating patterns of the noise in non-expert demonstrations"). OV-402 removes that sentence (you declined TC-403 on it). If you accept OV-402 too, "It" has nothing to refer to, so decide the two together. The line stays as a % [HY removed] comment rather than an empty line, which would start a new paragraph.

Used in: [Chapter openings](../hangs-writing-style-reference.md#chapter-openings).

### C4-03

**Declined** · weight 3 · Sentences moved · Chapter 4 · Categorizing Systematic Non-Optimality in Hu… · Chapter 4, `chapters/sidetracks.tex`, line 15

Suggestion: Say how sidetracks were identified right after saying they were identified

Original, which stayed:

~~~latex
The main contributions of this chapter are characterizing and categorizing non-optimal behaviors in human demonstrations.
To identify \thingname{} in the collected demonstrations, a graphical interface was designed, a codebook was developed through open coding, the demonstrations were annotated by two robot experts, and the labels were cross-validated with a third expert.
~~~

Declined suggestion:

~~~latex
To identify \thingname{} in the collected demonstrations, a graphical interface was designed, a codebook was developed through open coding, the demonstrations were annotated by two robot experts, and the labels were cross-validated with a third expert.
% [HY moved down one line, opening-reorder-review C4-03]
The main contributions of this chapter are characterizing and categorizing non-optimal behaviors in human demonstrations.
~~~

Note written with the suggestion: "It analyzes demonstrations ... and identifies four types of frequent, systematic non-optimal behaviors, termed sidetracks" is followed by the contribution statement, and only then by how they were identified ("To identify sidetracks in the collected demonstrations, a graphical interface was designed ..."). Swapping the two puts "identifies" and "To identify" next to each other, and the contribution statement then leads into the findings, as in the Demonstration Sidetracks paper ("The main contributions of this work are characterizing and categorizing non-optimal behaviors in human demonstrations. We found that non-optimal behaviors are beyond random errors, and possess spatial and temporal structures."). Both sentences are unchanged. Style reference: Known information leading to new information; Contribution statements.

Used in: [Chapter openings](../hangs-writing-style-reference.md#chapter-openings).

### C4-04

**Accepted** · weight 1 · Repeated text cut · Chapter 4 · Categorizing Systematic Non-Optimality in Hu… · Chapter 4, `chapters/sidetracks.tex`, line 19

Suggestion: Two findings sentences repeat the one that opens the findings

Original:

~~~latex
The analysis also shows that \thingname{} are not randomly distributed in demonstrations.
When and where \thingname{} appeared have temporal and spatial relationships with the task.
~~~

Accepted wording:

~~~latex
% [HY removed] The analysis also shows that \thingname{} are not randomly distributed in demonstrations.
% [HY removed] When and where \thingname{} appeared have temporal and spatial relationships with the task.
~~~

Note written with the suggestion: Both repeat the sentence that opens the findings, "The findings indicate that non-optimal behaviors are beyond random errors, and possess spatial and temporal structures": "not randomly distributed" is "beyond random errors", and "temporal and spatial relationships with the task" is "spatial and temporal structures". The sentence after them gives the concrete version ("more frequently identified when the sub-goal changed or when accurate manipulation or perceptions were required"), so the findings read general claim, frequency, when and where, control interface, which is also the order of Sections 4.2.1 to 4.2.4. This is an alternative to OV-404. OV-404 was built when the opening still had a separate summary of the findings ("The analysis shows that sidetracks occur across all demonstrators ..."), which you have since removed; accepting OV-404 now would leave only the sub-goal sentence. Decide one of the two. If OV-404 is applied first, this item is not found.

Used in: [Chapter openings](../hangs-writing-style-reference.md#chapter-openings).

### C4-05

**Accepted** · weight 1 · Sentences moved · Chapter 4 · Categorizing Systematic Non-Optimality in Hu… · Chapter 4, `chapters/sidetracks.tex`, line 23

Suggestion: Keep the findings next to "These findings", and end with the repository

Original:

~~~latex
All codes and annotated data are published online at \href{https://github.com/AABL-Lab/Human-Demonstration-Sidetracks}{Demonstration-Sidetracks GitHub}.
These findings will be beneficial for future LfD algorithm development to better learn from noisy demonstrations and for oracle design to reduce the gap between in-lab datasets and real-world demonstrations.
The related work is reviewed in \autoref{sec:bg-lfd} , and the work presented in this chapter was originally published as ``\textbf{Demonstration Sidetracks: Categorizing Systematic Non-Optimality in Human Demonstrations}''~\cite{fang2025demonstrationsidetrackscategorizingsystematic}.
~~~

Accepted wording:

~~~latex
These findings will be beneficial for future LfD algorithm development to better learn from noisy demonstrations and for oracle design to reduce the gap between in-lab datasets and real-world demonstrations.
The related work is reviewed in \autoref{sec:bg-lfd} , and the work presented in this chapter was originally published as ``\textbf{Demonstration Sidetracks: Categorizing Systematic Non-Optimality in Human Demonstrations}''~\cite{fang2025demonstrationsidetrackscategorizingsystematic}.
% [HY moved from before "These findings", opening-reorder-review C4-05]
All codes and annotated data are published online at \href{https://github.com/AABL-Lab/Human-Demonstration-Sidetracks}{Demonstration-Sidetracks GitHub}.
~~~

Note written with the suggestion: The repository sentence sits between the findings and "These findings will be beneficial for future LfD algorithm development ...", so "These findings" reaches back over it. Moved to the end of the opening, the findings and their use are adjacent, and the repository follows the publication note, as the data and code sentences do in Chapter 3 ("All human feedback and human characteristic questionnaire responses, together with the code, are published online ...") and Chapter 7 ("Supplementary materials for this chapter ..."). The sentence is unchanged. ES-31 changes \href to \url in it: decide this item first, and ES-31 still applies afterwards because the sentence moves as it is. If ES-31 is applied first, this item is not found; tell me and I will rebuild it.

### C5-01

**Declined** · weight 3 · Repeated text cut · Chapter 5 · Reconsidering Scalar Feedback in Interactive… · Chapter 5, `chapters/steady.tex`, line 5

Suggestion: The design choice is named twice in the first paragraph

Original, which stayed:

~~~latex
This chapter begins the second stage of this dissertation, mitigating noise in human feedback, by revisiting a design choice made by many interactive reinforcement learning methods, which is asking human teachers for binary rather than scalar evaluative feedback.
~~~

Declined suggestion:

~~~latex
This chapter begins the second stage of this dissertation, mitigating noise in human feedback.
~~~

Note written with the suggestion: The design choice in this clause is named again later in the same paragraph, where the argument reaches it: "A common response to this variability is to restrict what teachers can express. Many interactive learning methods favor binary feedback over scalar feedback, viewing binary feedback as noise-reduced and thus more suitable for learning". Without the clause the stage sentence is as short as the one in Chapter 4 ("This chapter completes the first stage of this dissertation."), and the paragraph reaches binary feedback through the first-stage results. ES-07 rewords the next sentences but not this one, so the two are independent. Style reference: One main job and varied sentence length.

Used in: [Chapter openings](../hangs-writing-style-reference.md#chapter-openings).

### C5-02

**Declined** · weight 3 · Repeated text cut · Chapter 5 · Reconsidering Scalar Feedback in Interactive… · Chapter 5, `chapters/steady.tex`, line 20

Suggestion: Why binary feedback is favored and what it loses, said a second time

Original, which stayed:

~~~latex
However, only binary feedback has been widely used in prior work\cite{knox2008tamer,griffith2013policy,tan2020top}
since it is easy to separate into positive and negative, and limiting people to only two options can reduce noise.


Despite these advantages,
allowing \emph{only} binary feedback reduces information in the signal such as the intensity of preferences.
~~~

Declined suggestion:

~~~latex
% [HY removed] However, only binary feedback has been widely used in prior work\cite{knox2008tamer,griffith2013policy,tan2020top}
% [HY removed] since it is easy to separate into positive and negative, and limiting people to only two options can reduce noise.
% [HY removed] Despite these advantages,
% [HY removed] allowing \emph{only} binary feedback reduces information in the signal such as the intensity of preferences.
~~~

Note written with the suggestion: These sentences repeat the first paragraph, which already says why binary feedback is favored ("Many interactive learning methods favor binary feedback over scalar feedback, viewing binary feedback as noise-reduced and thus more suitable for learning") and what it loses ("However, restricting feedback in this way also discards information, such as the magnitude of a teacher's evaluation"). They are cut together because "Despite these advantages" refers to the first. The two paragraphs then merge and read: the two types of evaluative feedback, "In theory, both of these types of feedback can contain useful information", then "Scalar feedback, on the other hand, ..." and its difficulties. This is the cut OV-501 proposed; OV-501 is no longer found because you removed the commented lines between the two paragraphs. ES-43 changes a citation key in the first sentence, so it is not found if this is accepted, which is expected. knox2008tamer and griffith2013policy stay in the bibliography (cited in Chapters 1, 2 and 5); tan2020top is cited only here and leaves it, as ES-43 intends anyway.

Used in: [Chapter openings](../hangs-writing-style-reference.md#chapter-openings).

### C5-03

**Declined** · weight 3 · Repeated text cut · Chapter 5 · Reconsidering Scalar Feedback in Interactive… · Chapter 5, `chapters/steady.tex`, line 55

Suggestion: The conclusion of the study is given before its results

Original, which stayed:

~~~latex
In this chapter, a study of scalar and binary feedback was conducted with 90 online participants evaluating a robot performing a manipulation task, and the results show that scalar feedback has the potential to improve learning when properly handled.
~~~

Declined suggestion:

~~~latex
In this chapter, a study of scalar and binary feedback was conducted with 90 online participants evaluating a robot performing a manipulation task.
~~~

Note written with the suggestion: The conclusion is drawn three sentences later, after the results: "Given that these results suggest that scalar feedback is not necessarily worse for learning if the scaling problem and noise can be addressed, ...". Stated here as well, it comes before the evidence and is said twice. Without the clause the paragraph reads study, results ("human teachers can be inconsistent ...", "no significant difference was found ..."), interpretation, STEADY. Style reference: Reporting findings and interpretations; A study finding leading to a method.

Used in: [Chapter openings](../hangs-writing-style-reference.md#chapter-openings).

### C5-04

**Accepted** · weight 1 · Sentences moved · Chapter 5 · Reconsidering Scalar Feedback in Interactive… · Chapter 5, `chapters/steady.tex`, line 13

Suggestion: Move the publication note to the end of the opening (1 of 2: take it out here)

Original:

~~~latex
its inconsistency can be mitigated algorithmically.
The related work is reviewed in \autoref{sec:RW} , and the work presented in this chapter was originally published as ``\textbf{From `Thumbs Up' to `10 out of 10': Reconsidering Scalar Feedback in Interactive Reinforcement Learning}''~\cite{yu2023thumbs}.
~~~

Accepted wording:

~~~latex
its inconsistency can be mitigated algorithmically.
% [HY moved to the end of the opening, C5-05] The related work is reviewed in \autoref{sec:RW} , and the work presented in this chapter was originally published as ``\textbf{From `Thumbs Up' to `10 out of 10': Reconsidering Scalar Feedback in Interactive Reinforcement Learning}''~\cite{yu2023thumbs}.
~~~

Note written with the suggestion: Accept both C5-04 and C5-05, or neither: this one takes the sentence out, C5-05 puts it back after the last sentence of the opening. In Chapters 3, 4, 6 and 7 the related-work and publication note closes the opening, after the summary of the study. In this chapter it comes after the first paragraph, and the background on evaluative feedback, the study and STEADY follow it. You commented out the study summary that used to stand before it, so the summary of the study is now the paragraph before Figure 5.2, and the note fits after that. The sentence stays here as a comment. TC-501 rewords the sentence before; both apply in either order, because this item quotes only the unchanged end of that sentence.

Used in: [Chapter openings](../hangs-writing-style-reference.md#chapter-openings).

### C5-05

**Accepted** · weight 1 · Sentences moved · Chapter 5 · Reconsidering Scalar Feedback in Interactive… · Chapter 5, `chapters/steady.tex`, line 62

Suggestion: Move the publication note to the end of the opening (2 of 2: put it here)

New text, placed next to this passage:

~~~latex
The experiments demonstrate that models trained with \textit{scalar feedback + STEADY} outperform models trained with binary feedback on a robot learning task.
~~~

Accepted wording:

~~~latex
% [HY moved here from the end of the first paragraph, opening-reorder-review C5-04 and C5-05]
The related work is reviewed in \autoref{sec:RW} , and the work presented in this chapter was originally published as ``\textbf{From `Thumbs Up' to `10 out of 10': Reconsidering Scalar Feedback in Interactive Reinforcement Learning}''~\cite{yu2023thumbs}.
~~~

Note written with the suggestion: The second half of the move in C5-04; accept both or neither. The note follows the last result of the opening ("models trained with scalar feedback + STEADY outperform models trained with binary feedback on a robot learning task"), in the same paragraph. The sentence is unchanged.

### C6-01

**Accepted with Hang's edit** · weight 4 · Repeated text cut · Chapter 6 · An Unexplored Human Feedback Signal for Teac… · Chapter 6, `chapters/progress.tex`, line 5

Suggestion: Progress is introduced twice before the studies

Original:

~~~latex
This chapter completes the second stage of this dissertation. by formalizing \textit{progress}, a teaching signal that describes how much of a task has been completed, ranging from totally incomplete to fully complete.
Learning from Demonstration (LfD) enables robots
~~~

Suggested:

~~~latex
This chapter completes the second stage of this dissertation.
Learning from Demonstration (LfD) enables robots
~~~

Hang's wording:

~~~latex
This chapter completes the second stage of this dissertation by formalizing progress.
Learning from Demonstration (LfD) enables robots
~~~

Note written with the suggestion: Progress is introduced again at the end of the third paragraph, where the opening turns from the problem to the signal ("This chapter builds on these results and characterizes progress, a type of human feedback that is under-explored as a human teaching signal and is used to capture the completion of a task"), and defined in full at the start of Section 6.1 ("the cumulative degree of task completion based on the current observation, ranging from totally incomplete to fully complete"). The cut also removes the stray period before "by". The stage sentence then matches Chapter 4 ("This chapter completes the first stage of this dissertation."). If you would rather keep the definition here, reject this and accept C6-02, which only fixes the period. The quote runs into the next line only so that the shorter text is not mistaken for text already in the file.

Used in: [Chapter openings](../hangs-writing-style-reference.md#chapter-openings).

### C6-02

**Declined** · weight 3 · Punctuation fix · Chapter 6 · An Unexplored Human Feedback Signal for Teac… · Chapter 6, `chapters/progress.tex`, line 5

Suggestion: Only the stray period (if you keep the definition)

Original, which stayed:

~~~latex
This chapter completes the second stage of this dissertation. by formalizing \textit{progress}, a teaching signal that describes how much of a task has been completed, ranging from totally incomplete to fully complete.
~~~

Declined suggestion:

~~~latex
This chapter completes the second stage of this dissertation by formalizing \textit{progress}, a teaching signal that describes how much of a task has been completed, ranging from totally incomplete to fully complete.
~~~

Note written with the suggestion: Use this only if you reject C6-01. It removes the period before "by" and changes nothing else. If C6-01 is accepted, this item is not found, which is expected. Style reference: Correcting a sentence without rewording it.

Not used in a pattern: Superseded by another suggestion on the same text, which Hang decided instead.

### C6-03

**Declined** · weight 3 · Repeated text cut · Chapter 6 · An Unexplored Human Feedback Signal for Teac… · Chapter 6, `chapters/progress.tex`, line 36

Suggestion: The public space study is described twice in three sentences

Original, which stayed:

~~~latex
and one public space study in which 40 passersby provided and then evaluated their own demonstrations.
~~~

Declined suggestion:

~~~latex
and one public space study.
~~~

Note written with the suggestion: Two sentences later the same study is described in detail: "For the in-person study, 40 passersby were recruited to provide demonstrations in an ice cream topping-adding task ... The demonstrators then provided progress and scalar feedback on their own demonstrations." The Progress paper's version of this sentence stops at the count of studies ("We show the capability of progress through two online studies and one in-person study"). Only the end of the sentence is quoted, so this works after TC-601 (which changes "This chapter validates" to "It validates"); if this item goes first, TC-601 is not found. TC-601's reason no longer holds, because this sentence now opens a paragraph after "The intuition is that ...", where "It" would not clearly mean the chapter.

Used in: [Chapter openings](../hangs-writing-style-reference.md#chapter-openings).

### C6-04

**Declined** · weight 3 · Repeated text cut · Chapter 6 · An Unexplored Human Feedback Signal for Teac… · Chapter 6, `chapters/progress.tex`, line 69

Suggestion: The studies are summarized again after the figure

Original, which stayed:

~~~latex
The validation studies covered a wide range of scenarios and involved 116 participants in total.
~~~

Declined suggestion:

~~~latex
% [HY removed] The validation studies covered a wide range of scenarios and involved 116 participants in total.
~~~

Note written with the suggestion: The paragraph before Figure 6.1 already describes the three studies, their participants (76 crowd-sourced workers, 40 passersby) and their tasks (three simple tasks and one long-horizon task, the ice cream topping-adding task). Here the sentence separates the contribution statement from the dataset release. The total of 116 is stated only in this sentence; it is the sum of the two numbers given before the figure.

Used in: [Chapter openings](../hangs-writing-style-reference.md#chapter-openings).

### C6-05

**Accepted** · weight 1 · Repeated text cut · Chapter 6 · An Unexplored Human Feedback Signal for Teac… · Chapter 6, `chapters/progress.tex`, line 70

Suggestion: Non-expert demonstrations are multi-policy: already said in the second paragraph

Original:

~~~latex
The results also showed that non-expert demonstrations are multi-policy and sub-optimal, but sub-optimal in a meaningful way.
~~~

Accepted wording:

~~~latex
% [HY removed] The results also showed that non-expert demonstrations are multi-policy and sub-optimal, but sub-optimal in a meaningful way.
~~~

Note written with the suggestion: The second paragraph says this with a pointer to the section that shows it ("Non-expert demonstrations can be noisy, multi-policy, and yet still succeed (as shown in Section 6.3.3)"), and the third paragraph says it through Chapter 4 ("non-expert demonstrations contain frequent sidetracks, behaviors that do not advance the task but are often part of how non-experts succeed at it"; ES-10 keeps this part). The Summary keeps the finding ("The data show that non-expert demonstrations are multi-policy and mostly successful, while noisy in a meaningful way"). With C6-04 as well, the contribution statement is followed directly by the dataset release ("Finally, a dataset was released online ...").

### C7-01

**Declined** · weight 3 · Sentences moved · Chapter 7 · Aligning Learned Rewards with Task Progress… · Chapter 7, `chapters/phirl.tex`, line 6

Suggestion: Put the aim after the IRL background, where the PHIRL paper has it

Original, which stayed:

~~~latex
This chapter aims to learn robust reward functions by combining human demonstrations and feedback, while reducing human engagement.
An appropriate reward function is a crucial component for Reinforcement Learning (RL) agents to perform effectively \cite{ibrahim2024comprehensiveoverviewrewardengineering}.
While sparse rewards are intuitive to specify, they offer limited guidance during early exploration. Conversely, hand-crafted dense rewards accelerate learning, but designing them requires substantial engineering effort and tedious manual tuning \cite{xiang2024sc, ibrahim2024comprehensiveoverviewrewardengineering}.
Inverse Reinforcement Learning (IRL) offers an alternative by inferring a dense reward function directly from human demonstrations or human feedback, mitigating the need for manual reward designing.
Compared to imitation learning methods that directly map states to actions \cite{chi2024diffusionpolicyvisuomotorpolicy, zhao2023act}, IRL may require higher-quality demonstrations \cite{sasaki2020behavioral}, but the learning outcomes can be easier for post-training \cite{sun2025inversereinforcementlearningmeets} or revising \cite{hao2026rewardtransfer}.
~~~

Declined suggestion:

~~~latex
An appropriate reward function is a crucial component for Reinforcement Learning (RL) agents to perform effectively \cite{ibrahim2024comprehensiveoverviewrewardengineering}.
While sparse rewards are intuitive to specify, they offer limited guidance during early exploration. Conversely, hand-crafted dense rewards accelerate learning, but designing them requires substantial engineering effort and tedious manual tuning \cite{xiang2024sc, ibrahim2024comprehensiveoverviewrewardengineering}.
Inverse Reinforcement Learning (IRL) offers an alternative by inferring a dense reward function directly from human demonstrations or human feedback, mitigating the need for manual reward designing.
Compared to imitation learning methods that directly map states to actions \cite{chi2024diffusionpolicyvisuomotorpolicy, zhao2023act}, IRL may require higher-quality demonstrations \cite{sasaki2020behavioral}, but the learning outcomes can be easier for post-training \cite{sun2025inversereinforcementlearningmeets} or revising \cite{hao2026rewardtransfer}.
% [HY moved from after the first sentence, opening-reorder-review C7-01]
This chapter aims to learn robust reward functions by combining human demonstrations and feedback, while reducing human engagement.
~~~

Note written with the suggestion: Two "This chapter" sentences open the chapter, and the aim comes before the background it follows from. In the PHIRL paper the aim closes the IRL background ("Compared to imitation learning methods ... IRL may require higher quality demonstrations ... In this work, we aim to learn robust reward functions by combining human demonstrations and feedback, while reducing human engagement."). Moved there, it also leads into the next paragraph, which takes up its two parts in turn: feedback ("Prior reward learning work often relies on preference feedback", after C7-02) and human engagement ("human-in-the-loop teaching effort has become a more expensive resource"). This is an alternative to OV-702, which cuts the sentence. Decide this item first. If you then accept OV-702 as well, the sentence is cut at its new place, and TC-703 and ES-36 still apply to it, because the sentences move unchanged. If any of the three is applied first, this item is not found. Style reference: An introduction built around a consequential assumption (practical stake, then the chapter's approach).

Used in: [Chapter openings](../hangs-writing-style-reference.md#chapter-openings).

### C7-02

**Declined** · weight 3 · Sentences moved · Chapter 7 · Aligning Learned Rewards with Task Progress… · Chapter 7, `chapters/phirl.tex`, line 21

Suggestion: State the problems with preference feedback before proposing PHIRL

Original, which stayed:

~~~latex
Technologies and dataset-sharing communities, such as NES \cite{cabi2019scaling}, UMI \cite{chi2024universalmanipulationinterfaceinthewild}, ego-centric data \cite{kareer2025egomimic}, and Hugging Face \cite{jain2022hugging}, have made robot demonstrations significantly easier to access.
In this setting, human-in-the-loop teaching effort has become a more expensive resource than stock demonstrations.
Thus, this chapter proposes \textit{Progress}-Heuristicized Inverse Reinforcement Learning (PHIRL), a data-efficient framework that alternates between learning a reward function from demonstrations and aligning the learned reward function with \textit{progress} annotations on a subset of those demonstrations.

PHIRL builds on two results from the preceding chapters. \textit{Progress} is consistent and intuitive for non-expert users (\autoref{ch:progress}), and non-expert demonstrations contain structured imperfections that do not advance the task (\autoref{ch:sidetracks}).
Prior reward learning work often relies on preference feedback \cite{palan2019learning, ibarz2018reward, brown2019ranking}.
Forcing users to pick a preferred trajectory does not always benefit learning. For instance, consider a pick-and-place task where the robot never manages to grasp the object. In this case, all sampled trajectory clips are undesirable. The preference feedback is therefore uninformative.
~~~

Declined suggestion:

~~~latex
% [HY moved from after "PHIRL builds on two results ...", opening-reorder-review C7-02]
Prior reward learning work often relies on preference feedback \cite{palan2019learning, ibarz2018reward, brown2019ranking}.
Forcing users to pick a preferred trajectory does not always benefit learning. For instance, consider a pick-and-place task where the robot never manages to grasp the object. In this case, all sampled trajectory clips are undesirable. The preference feedback is therefore uninformative.
Technologies and dataset-sharing communities, such as NES \cite{cabi2019scaling}, UMI \cite{chi2024universalmanipulationinterfaceinthewild}, ego-centric data \cite{kareer2025egomimic}, and Hugging Face \cite{jain2022hugging}, have made robot demonstrations significantly easier to access.
In this setting, human-in-the-loop teaching effort has become a more expensive resource than stock demonstrations.
Thus, this chapter proposes \textit{Progress}-Heuristicized Inverse Reinforcement Learning (PHIRL), a data-efficient framework that alternates between learning a reward function from demonstrations and aligning the learned reward function with \textit{progress} annotations on a subset of those demonstrations.

PHIRL builds on two results from the preceding chapters. \textit{Progress} is consistent and intuitive for non-expert users (\autoref{ch:progress}), and non-expert demonstrations contain structured imperfections that do not advance the task (\autoref{ch:sidetracks}).
~~~

Note written with the suggestion: The preference-feedback problem ("Prior reward learning work often relies on preference feedback ... The preference feedback is therefore uninformative.") now comes after PHIRL has been proposed and right after "PHIRL builds on two results from the preceding chapters", so it reads as a step back. Moved before the paragraph on demonstrations being easy to access, the opening gives both gaps first (preference feedback can be uninformative; human-in-the-loop effort is now the expensive resource), then "Thus, this chapter proposes PHIRL ... progress annotations on a subset of those demonstrations", which answers both. This is the order of the PHIRL paper. The paragraph after PHIRL then holds the link to Chapters 6 and 4 and the design that reduces human engagement ("Furthermore, to reduce human engagement, PHIRL is designed to not ask humans ..."). All sentences are unchanged. Style reference: A hypothetical scenario that explains a problem (return to the technical point); An introduction built around a consequential assumption.

Used in: [Chapter openings](../hangs-writing-style-reference.md#chapter-openings).

### C7-03

**Accepted** · weight 1 · Repeated text cut · Chapter 7 · Aligning Learned Rewards with Task Progress… · Chapter 7, `chapters/phirl.tex`, line 34

Suggestion: The reward-hacking analysis is stated in two consecutive sentences

Original:

~~~latex
An evaluation on two simulated manipulation tasks and one real-robot task shows that, with only 20\% of the demonstrations annotated, PHIRL outperforms all four baselines, with the largest advantages when the task horizon is longer or the demonstration quality is lower, and a qualitative analysis illustrates how \textit{progress} alignment can discourage two reward hacking behaviors.
~~~

Accepted wording:

~~~latex
An evaluation on two simulated manipulation tasks and one real-robot task shows that, with only 20\% of the demonstrations annotated, PHIRL outperforms all four baselines, with the largest advantages when the task horizon is longer or the demonstration quality is lower.
~~~

Note written with the suggestion: The next sentence states the same result with its comparison and your measured wording: "A qualitative analysis against AIRL illustrates how progress alignment can discourage two examined reward-hacking behaviors." Cutting the clause here keeps that version and leaves this sentence with the evaluation alone. Style reference: Numbers and measured comparisons (give the comparison with the result).

Used in: [Chapter openings](../hangs-writing-style-reference.md#chapter-openings).
