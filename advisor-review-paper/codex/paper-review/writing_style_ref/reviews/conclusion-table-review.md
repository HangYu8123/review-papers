# Conclusion table and readability review

Review `conclusion-table-review` of the dissertation, from `waiting_for_review/conclusion-table-review`. Decided between October 12, 2026 and October 12, 2026. Decisions files: `conclusion-table-review.decisions.20261012-200639.json`.

[All reviews](../review-decisions.md) · [Weighted signals](../preference-signals.md) · [Main reference](../hangs-writing-style-reference.md)

| Outcome | Decided by Hang | Not decided by Hang |
| --- | ---: | ---: |
| Accepted as suggested | 10 | 0 |
| Accepted with Hang's edit | 8 | 0 |
| Declined | 1 | 0 |
| Notes from Hang | 0 | |

### CT-01

**Accepted** · weight 1 · Table simplification · Table 9.1, overview of the studies · Chapter 9, `chapters/conclusion.tex`, line 14

Suggestion: Caption says where the procedures are

Original:

~~~latex
\caption[Overview of the studies conducted in this dissertation]{Overview of the studies conducted in this dissertation. }
    \label{tab:study-overview}
~~~

Accepted wording:

~~~latex
\caption[Overview of the studies conducted in this dissertation]{Overview of the studies conducted in this dissertation. The procedure of each study is described in its chapter.}
    \label{tab:study-overview}
    \vspace{0.5em}
~~~

Note written with the suggestion: The rows below drop procedure details, so the caption says where a reader finds them. The space before the closing brace of the caption is removed. \vspace{0.5em} puts a small gap between the caption and the top rule. In the current PDF the caption sits directly on the rule.

Used in: [Study overview tables](../hangs-writing-style-reference.md#study-overview-tables).

### CT-02

**Accepted** · weight 1 · Table simplification · Table 9.1, overview of the studies · Chapter 9, `chapters/conclusion.tex`, line 20

Suggestion: Fourth column becomes "Setting"

Original:

~~~latex
\textbf{Study} & \textbf{Task} & \textbf{Data collected} & \textbf{How data were collected} & \textbf{Participants} \\
~~~

Accepted wording:

~~~latex
\textbf{Study} & \textbf{Task} & \textbf{Data collected} & \textbf{Setting} & \textbf{Participants} \\
~~~

Note written with the suggestion: With the procedure details removed in the rows, the fourth column says where each study took place, which is a public space, online, replays in simulation, or in person. A reader can then check the claim of Section 9.1, "studies conducted mostly outside the laboratory (Table 9.1)", from one column. Style entry: Teachers and collection settings ("Describe the recruitment setting when it affects interpretation, such as a public space, passersby, crowdworkers, or an online study"). If you keep the long cells in most rows, keep this header as it is. CT-12 changes the sentence that introduces the table to match.

### CT-03

**Accepted with Hang's edit** · weight 4 · Table simplification · Table 9.1, overview of the studies · Chapter 9, `chapters/conclusion.tex`, line 22

Suggestion: Row 1, CHARM study (Chapter 3)

Original:

~~~latex
Ch.~\ref{ch:charm}: CHARM study
        & Nut assembly and coffee preparation (simulated robot)
        & Human characteristics questionnaire (six domains); five-point scalar evaluative feedback on robot trajectories
        & In person, university atrium; simulated robot on a screen; feedback via a GUI every 30 actions
        & 46 passersby \\
~~~

Suggested:

~~~latex
Ch.~\ref{ch:charm}: CHARM study
        & Nut assembly and coffee preparation (simulated robot)
        & Human characteristics questionnaire and scalar evaluative feedback on robot trajectories
        & Public space
        & 46 passersby \\
~~~

Hang's wording:

~~~latex
Ch.~\ref{ch:charm}: CHARM study
        & Nut assembly and coffee preparation (simulated robot)
        & Human characteristics questionnaire and scalar evaluative feedback on robot trajectories
        & Public space, university atrium
        & 46 passersby \\
~~~

Note written with the suggestion: Removed: "(six domains)", "five-point", and the procedure in the fourth cell, which becomes "Public space", the term that Chapter 3 and this chapter use for the study. Chapter 3 states all of the removed details (the six domains of the questionnaire, the five-point scale, the tasks rendered on a screen, and the GUI that prompted for feedback every 30 actions). The three semicolons go with them (style entry: Few colons and semicolons).

Used in: [Study overview tables](../hangs-writing-style-reference.md#study-overview-tables).

### CT-04

**Accepted with Hang's edit** · weight 4 · Table simplification · Table 9.1, overview of the studies · Chapter 9, `chapters/conclusion.tex`, line 28

Suggestion: Row 2, Sidetracks analysis (Chapter 4)

Original:

~~~latex
Ch.~\ref{ch:sidetracks}: Sidetracks analysis
        & Ice cream topping (Kinova Gen3 Lite, Xbox controller)
        & Annotations of four sidetrack types, task phases, and control patterns
        & Ch.~\ref{ch:progress} public space demonstrations replayed in simulation and annotated with a codebook developed through open coding
        & 40 demonstrators (from Ch.~\ref{ch:progress}); 3 expert annotators \\
~~~

Suggested:

~~~latex
Ch.~\ref{ch:sidetracks}: Sidetracks analysis
        & Ice cream topping (Kinova Gen3 Lite)
        & Annotations of four sidetrack types, task phases, and control patterns on the 40 demonstrations of Ch.~\ref{ch:progress}
        & Replays in simulation
        & 3 expert annotators \\
~~~

Hang's wording:

~~~latex
Ch.~\ref{ch:sidetracks}: Sidetracks analysis
        & Ice cream topping (Kinova Gen3 Lite)
        & Annotations of four sidetrack types, task phases, and control patterns on the 40 demonstrations of Ch.~\ref{ch:progress}
        &  public space demonstrations replayed in simulation and annotated with a codebook
        & 3 expert annotators \\
~~~

Note written with the suggestion: The source of the demonstrations moves from the fourth cell into the data ("on the 40 demonstrations of Ch. 6"). "40 demonstrators (from Ch. 6)" is therefore no longer listed under Participants, which now gives only the people who took part in this analysis. Row 6 says that these demonstrations come from the public space study. Removed: "Xbox controller" (stated in Chapters 4 and 6) and "annotated with a codebook developed through open coding" (stated in Chapter 4). "Replays in simulation" is the same wording as in Row 7.

Used in: [Study overview tables](../hangs-writing-style-reference.md#study-overview-tables).

### CT-05

**Accepted with Hang's edit** · weight 4 · Table simplification · Table 9.1, overview of the studies · Chapter 9, `chapters/conclusion.tex`, line 34

Suggestion: Row 3, scalar vs. binary evaluative feedback (Chapter 5)

Original:

~~~latex
Ch.~\ref{ch:steady}: Scalar vs.\ binary evaluative feedback
        & Button pressing (Kinova Jaco arm)
        & Binary (good/bad) or scalar (0--10) feedback on 100 robot video clips, each shown twice (18,000 in total)
        & Online (Amazon Mechanical Turk); robot videos; between-subjects: binary vs.\ scalar
        & 90 crowdworkers (45 per condition); 3-expert pilot \\
~~~

Suggested:

~~~latex
Ch.~\ref{ch:steady}: Scalar vs.\ binary evaluative feedback
        & Button pressing (Kinova Jaco arm)
        & Binary or scalar feedback on 100 robot video clips, each shown twice
        & Online (Amazon Mechanical Turk)
        & 90 crowdworkers \\
~~~

Hang's wording:

~~~latex
Ch.~\ref{ch:steady}: Scalar vs.\ binary evaluative feedback
        & Button pressing (Kinova Jaco arm)
        & Binary or scalar feedback on 100 robot video clips, each shown twice
        & Online (Amazon Mechanical Turk)
        & 90 crowdworkers (45 per condition); 3-expert pilot \\
~~~

Note written with the suggestion: Removed: "(good/bad)", "(0--10)", "(18,000 in total)", "robot videos; between-subjects: binary vs. scalar", "(45 per condition)" and "3-expert pilot". Chapter 5 states the two scales, the two groups of 45, and the pilot with three robot experts. "Binary or scalar" already says that a participant gave one of the two. The total of 18,000 is not stated in Chapter 5. Chapter 1 has it ("more than 18,000 pieces of feedback from 90 participants"). "100 robot video clips, each shown twice" is kept, because the repetition is what the self-consistency result of this chapter rests on.

Used in: [Study overview tables](../hangs-writing-style-reference.md#study-overview-tables).

### CT-06

**Accepted with Hang's edit** · weight 4 · Table simplification · Table 9.1, overview of the studies · Chapter 9, `chapters/conclusion.tex`, line 40

Suggestion: Row 4, progress online study I (Chapter 6)

Original:

~~~latex
Ch.~\ref{ch:progress}: \textit{Progress} online study I
        & Reaching, pouring, and spinning
        & \textit{Progress} (0--100) or scalar evaluative feedback, 10 per task; NASA-TLX workload; completion time
        & Online (Amazon Mechanical Turk); expert demonstration videos; between-subjects
        & 40 crowdworkers (20 per condition) \\
~~~

Suggested:

~~~latex
Ch.~\ref{ch:progress}: \textit{Progress} online study I
        & Reaching, pouring, and spinning
        & \textit{Progress} or scalar evaluative feedback on demonstration videos, workload, and completion time
        & Online (Amazon Mechanical Turk)
        & 40 crowdworkers \\
~~~

Hang's wording:

~~~latex
Ch.~\ref{ch:progress}: \textit{Progress} online study I
        & Reaching, pouring, and spinning
        & \textit{Progress} or scalar evaluative feedback on demonstration videos, workload, and completion time
        & Online (Amazon Mechanical Turk)
        & 40 crowdworkers (20 per condition)\\
~~~

Note written with the suggestion: Removed: "(0--100)", "10 per task", "NASA-TLX", "expert", "between-subjects" and "(20 per condition)". "Demonstration videos" moves from the fourth cell into the data, in the same words as in Row 5. Chapter 6 states all of the removed details. "Workload" is the word that this chapter uses for the result below ("No significant difference in workload or completion time").

Used in: [Study overview tables](../hangs-writing-style-reference.md#study-overview-tables).

### CT-07

**Accepted with Hang's edit** · weight 4 · Table simplification · Table 9.1, overview of the studies · Chapter 9, `chapters/conclusion.tex`, line 46

Suggestion: Row 5, progress online study II (Chapter 6)

Original:

~~~latex
Ch.~\ref{ch:progress}: \textit{Progress} online study II
        & Tea steeping (six sub-tasks), five success and failure scenarios
        & \textit{Progress} or scalar evaluative feedback, 15 per scenario (20 in Corrected)
        & Online (Prolific); demonstration videos; between-subjects
        & 36 crowdworkers (18 per condition; all analyzed) \\
~~~

Suggested:

~~~latex
Ch.~\ref{ch:progress}: \textit{Progress} online study II
        & Tea steeping in five scenarios
        & \textit{Progress} or scalar evaluative feedback on demonstration videos
        & Online (Prolific)
        & 36 crowdworkers \\
~~~

Hang's wording:

~~~latex
Ch.~\ref{ch:progress}: \textit{Progress} online study II
        & Tea steeping in five scenarios
        & \textit{Progress} or scalar evaluative feedback on demonstration videos
        & Online (Prolific)
        & 36 crowdworkers (18 per condition) \\
~~~

Note written with the suggestion: Removed: "(six sub-tasks)", "success and failure", "15 per scenario (20 in Corrected)", "between-subjects" and "(18 per condition; all analyzed)". "Demonstration videos" moves from the fourth cell into the data. Chapter 6 states the six sub-tasks, names the five scenarios (Perfect, Imperfect, Unaware, Corrected and Failure), and gives the number of annotations per scenario and the two groups of 18. I did not find "all analyzed" stated in Chapter 6.

Used in: [Study overview tables](../hangs-writing-style-reference.md#study-overview-tables).

### CT-08

**Accepted with Hang's edit** · weight 4 · Table simplification · Table 9.1, overview of the studies · Chapter 9, `chapters/conclusion.tex`, line 52

Suggestion: Row 6, progress public space study (Chapter 6)

Original:

~~~latex
Ch.~\ref{ch:progress}: \textit{Progress} public space study
        & Ice cream topping (Kinova Gen3 Lite, Xbox controller)
        & One demonstration each (recorded at 5\,Hz); \textit{progress} and scalar evaluative feedback at 10 points on a replay of it
        & In person, university atrium; people familiar with robots excluded; up to 3 min of practice, one attempt
        & 40 passersby \\
~~~

Suggested:

~~~latex
Ch.~\ref{ch:progress}: \textit{Progress} public space study
        & Ice cream topping (Kinova Gen3 Lite)
        & One demonstration each, with \textit{progress} and scalar evaluative feedback on a replay of it
        & Public space
        & 40 passersby \\
~~~

Hang's wording:

~~~latex
Ch.~\ref{ch:progress}: \textit{Progress} public space study
        & Ice cream topping (Kinova Gen3 Lite)
        & One demonstration each, with \textit{progress} and scalar evaluative feedback on a replay of it
        & Public space, university atrium
        & 40 non-expert passersby \\
~~~

Note written with the suggestion: Removed: "Xbox controller", "(recorded at 5 Hz)", "at 10 points", and the procedure in the fourth cell (the university atrium, the exclusion of people familiar with robots, up to 3 minutes of practice, one attempt), which becomes "Public space" as in Row 1. Chapter 6 states all of them. One thing to check, which I did not change: this row gives 40 passersby for the demonstrations and for the feedback, and Chapter 6 says "Progress and scalar feedback were collected from 34 participants (two participants' progress and scalar feedback were excluded ...)".

Used in: [Teachers and collection settings](../hangs-writing-style-reference.md#teachers-and-collection-settings), [Study overview tables](../hangs-writing-style-reference.md#study-overview-tables).

### CT-09

**Accepted with Hang's edit** · weight 4 · Table simplification · Table 9.1, overview of the studies · Chapter 9, `chapters/conclusion.tex`, line 58

Suggestion: Row 7, PHIRL annotation study (Chapter 7)

Original:

~~~latex
Ch.~\ref{ch:phirl}: PHIRL annotation study
        & Lift and PickPlaceCan (Robomimic PH and MH datasets)
        & \textit{Progress} (0--100) on 10 segments per demonstration; 20\% of demonstrations used by default
        & Annotators watched replays of the demonstrations in simulation
        & 6 annotators \\
~~~

Suggested:

~~~latex
Ch.~\ref{ch:phirl}: PHIRL annotation study
        & Lift and PickPlaceCan
        & \textit{Progress} on 10 segments per Robomimic demonstration
        & Replays in simulation
        & 6 annotators \\
~~~

Hang's wording:

~~~latex
Ch.~\ref{ch:phirl}: PHIRL annotation study
        & Lift and PickPlaceCan
        & \textit{Progress} on 10 segments per Robomimic demonstration
        & Annotators watched replays of the demonstrations in simulation
        & 6 non-expert annotators \\
~~~

Note written with the suggestion: Removed: "PH and MH", which this chapter does not define, "(0--100)", and "20\% of demonstrations used by default", which the paragraph on the third stage states ("With 20\% of the demonstrations annotated"). "Robomimic" moves from the task cell into the data, since it names the datasets that were annotated. "Annotators watched replays of the demonstrations in simulation" becomes "Replays in simulation", as in Row 2. That the annotators watched replays is otherwise stated only in the PHIRL appendix, which main.tex does not include at the moment, so the table keeps it.

Used in: [Teachers and collection settings](../hangs-writing-style-reference.md#teachers-and-collection-settings), [Study overview tables](../hangs-writing-style-reference.md#study-overview-tables).

### CT-10

**Accepted with Hang's edit** · weight 4 · Table simplification · Table 9.1, overview of the studies · Chapter 9, `chapters/conclusion.tex`, line 64

Suggestion: Row 8, PHIRL real-robot study (Chapter 7)

Original:

~~~latex
Ch.~\ref{ch:phirl}: PHIRL real-robot study
        & Animal brushing (pom-poms off a stuffed animal; Kinova Gen3 Lite)
        & 10 demonstrations per participant (60 in total); \textit{progress} on 2 demonstrations per participant (120 labels)
        & In person with a real robot; demonstrators at three proficiency levels; 5 min of practice
        & 6 demonstrators; 2 annotators \\
~~~

Suggested:

~~~latex
Ch.~\ref{ch:phirl}: PHIRL real-robot study
        & Animal brushing (Kinova Gen3 Lite)
        & 60 demonstrations, 12 of them annotated with \textit{progress}
        & In person
        & 6 demonstrators and 2 annotators \\
~~~

Hang's wording:

~~~latex
Ch.~\ref{ch:phirl}: PHIRL real-robot study
        & Animal brushing (Kinova Gen3 Lite)
        & 60 demonstrations, 12 of them annotated with \textit{progress}
        & In person, 2 worse, 2 okay, 2 better
        & 6 demonstrators and 2 annotators \\
~~~

Note written with the suggestion: The data cell gives the two totals in place of the counts per participant. 60 is the "(60 in total)" of the current cell. 12 is "2 demonstrations per participant" for the 6 demonstrators, which is also the 120 labels at 10 segments per demonstration. Please check that 12 is the number you mean. Removed: "pom-poms off a stuffed animal", "(120 labels)", "with a real robot", "demonstrators at three proficiency levels" and "5 min of practice". Chapter 7 states the pom-poms and the three levels. The name of the study and the task cell already say that the robot is real. I did not find the 5 minutes of practice in Chapter 7, so with this change it would not be stated anywhere. To keep it, put it back with "Edit the wording", or add it to the Data Collection paragraph of Chapter 7.

Used in: [Study overview tables](../hangs-writing-style-reference.md#study-overview-tables).

### CT-11

**Accepted** · weight 1 · Table simplification · Table 9.1, overview of the studies · Chapter 9, `chapters/conclusion.tex`, line 18

Suggestion: Column widths for the shorter cells (decide after the rows)

Original:

~~~latex
\begin{tabularx}{\textwidth}{@{}>{\raggedright\arraybackslash}p{2.2cm}>{\raggedright\arraybackslash}p{2.8cm}>{\raggedright\arraybackslash}X>{\raggedright\arraybackslash}X>{\raggedright\arraybackslash}p{2.3cm}@{}}
~~~

Accepted wording:

~~~latex
\begin{tabularx}{\textwidth}{@{}>{\raggedright\arraybackslash}p{2.5cm}>{\raggedright\arraybackslash}p{2.8cm}>{\raggedright\arraybackslash}X>{\raggedright\arraybackslash}p{2.6cm}>{\raggedright\arraybackslash}p{2.4cm}@{}}
~~~

Note written with the suggestion: Decide this one last. The widths are Study 2.5 cm (was 2.2), Task 2.8 cm (unchanged), Setting 2.6 cm (was about 4.0), Participants 2.4 cm (was 2.3), and "Data collected" takes the rest, about 5.1 cm (was about 4.0). With all rows accepted, the table is about 4.9 inches tall with these widths, compared with 7.4 inches now, and no row is longer than three lines. Accept this only if you accept most of the rows. I compiled it with the current rows as well, and the narrower fourth column then makes the table too long for the page (LaTeX reports "Float too large for page by 61.9pt"). The rows also work without this item, with a wider fourth column that stays mostly empty.

### CT-12

**Accepted** · weight 1 · Table simplification · Table 9.1, overview of the studies · Chapter 9, `chapters/conclusion.tex`, line 10

Suggestion: The sentence that introduces the table names the new column

Original:

~~~latex
\autoref{tab:study-overview} summarizes the studies conducted in this dissertation, including the task used in each study, the data that were collected, how the data were collected, and the number of participants recruited.
~~~

Accepted wording:

~~~latex
\autoref{tab:study-overview} summarizes the studies conducted in this dissertation, including the task used in each study, the data that were collected, the setting in which they were collected, and the number of participants recruited.
~~~

Note written with the suggestion: Needed only if you accept CT-02. The sentence lists the columns of the table, and "how the data were collected" was the old header of the fourth column. Nothing else in the sentence is changed.

### CR-01

**Accepted** · weight 1 · Correction · Sentences of the chapter · Chapter 9, `chapters/conclusion.tex`, line 6

Suggestion: A space before the period, twice

Original:

~~~latex
Following the three-stage architecture introduced in \autoref{ch:introduction}, public space studies were first conducted to understand the imperfections in non-expert feedback and demonstrations (\autoref{ch:charm} and \autoref{ch:sidetracks}) . Noise in human feedback was then examined and mitigated by stabilizing scalar feedback and formalizing \textit{progress}, a signal that is under-explored as a human teaching signal (\autoref{ch:steady} and \autoref{ch:progress}) .
~~~

Accepted wording:

~~~latex
Following the three-stage architecture introduced in \autoref{ch:introduction}, public space studies were first conducted to understand the imperfections in non-expert feedback and demonstrations (\autoref{ch:charm} and \autoref{ch:sidetracks}). Noise in human feedback was then examined and mitigated by stabilizing scalar feedback and formalizing \textit{progress}, a signal that is under-explored as a human teaching signal (\autoref{ch:steady} and \autoref{ch:progress}).
~~~

Note written with the suggestion: "(Chapter 3 and Chapter 4) ." and "(Chapter 5 and Chapter 6) ." each have a space between the closing parenthesis and the period, and it prints in the PDF. The two spaces are removed. No word is changed.

### CR-02

**Accepted** · weight 1 · Correction · Sentences of the chapter · Chapter 9 › Summary of Contributions, `chapters/conclusion.tex`, line 75

Suggestion: "and supported by" has no verb

Original:

~~~latex
The main contribution of this dissertation is a systematic approach to improving robot learning from non-experts, with three stages of work that build on one another and supported by studies conducted mostly outside the laboratory (\autoref{tab:study-overview}).
~~~

Accepted wording:

~~~latex
The main contribution of this dissertation is a systematic approach to improving robot learning from non-experts, with three stages of work that build on one another and are supported by studies conducted mostly outside the laboratory (\autoref{tab:study-overview}).
~~~

Note written with the suggestion: "With three stages of work that build on one another and supported by studies" joins a clause to a participle, so a reader has to go back to find what "supported" belongs to. Adding "are" gives the stages two verbs, "build on one another" and "are supported by". One word is added (style entries: Correcting a sentence without rewording it; Matched factors and endpoints). This makes the stages the subject of "supported". If you mean the approach, type "and that is supported by" with "Edit the wording".

### CR-03

**Accepted** · weight 1 · Readability · Sentences of the chapter · Chapter 9 › Summary of Contributions, `chapters/conclusion.tex`, line 78

Suggestion: Two findings of Chapter 3 in one sentence

Original:

~~~latex
In a public space study with 46 participants, feedback values were associated with the characteristics of the teacher, and CHARM, a model that includes these characteristics, predicted feedback values significantly more accurately than a model that uses task statistics alone (\autoref{ch:charm}).
~~~

Accepted wording:

~~~latex
In a public space study with 46 participants, feedback values were associated with the characteristics of the teacher. CHARM, a model that includes these characteristics, predicted feedback values significantly more accurately than a model that uses task statistics alone (\autoref{ch:charm}).
~~~

Note written with the suggestion: The sentence reports the association with the characteristics of the teacher and the accuracy of CHARM, and the second finding carries an inserted definition ("a model that includes these characteristics"). It is split at ", and". No word is changed. The chapter reference stays at the end of the second sentence. Style entry: One main job and varied sentence length ("Split a sentence when it reports two studies, two findings, or two requirements"), as in your edit of DW-07.

Used in: [One main job and varied sentence length](../hangs-writing-style-reference.md#one-main-job-and-varied-sentence-length).

### CR-04

**Declined** · weight 3 · Readability · Sentences of the chapter · Chapter 9 › Summary of Contributions, `chapters/conclusion.tex`, line 83

Suggestion: The learning result of STEADY as its own sentence

Original, which stayed:

~~~latex
Scalar feedback was less self-consistent than binary feedback when exact agreement was required, but with an agreement tolerance of $\pm 2$, no difference in self-consistency was detected between the two, and scalar feedback processed by STEADY led to better learning than binary feedback in the evaluated task (\autoref{ch:steady}).
~~~

Declined suggestion:

~~~latex
Scalar feedback was less self-consistent than binary feedback when exact agreement was required, but with an agreement tolerance of $\pm 2$, no difference in self-consistency was detected between the two. Scalar feedback processed by STEADY led to better learning than binary feedback in the evaluated task (\autoref{ch:steady}).
~~~

Note written with the suggestion: The sentence has three clauses, which are the comparison under exact agreement, the comparison with a tolerance of 2, and the learning result of STEADY. The first two belong together, because "but" sets one against the other. The learning result is a different finding, so it becomes its own sentence. Only ", and" is removed. Style entry: One main job and varied sentence length.

Used in: [One main job and varied sentence length](../hangs-writing-style-reference.md#one-main-job-and-varied-sentence-length).

### CR-05

**Accepted** · weight 1 · Correction · Sentences of the chapter · Chapter 9 › Summary of Contributions, `chapters/conclusion.tex`, line 86

Suggestion: "progress" in italics

Original:

~~~latex
The third stage built on both earlier stages to leverage imperfect teaching for learning by using a progress signal to compensate for the imperfections in demonstrations.
~~~

Accepted wording:

~~~latex
The third stage built on both earlier stages to leverage imperfect teaching for learning by using a \textit{progress} signal to compensate for the imperfections in demonstrations.
~~~

Note written with the suggestion: Everywhere else in this chapter "progress" is in italics when it names the signal, and here it is not (style entry: Teaching signals and learning quantities, "Italicize progress when it names the signal"). Only the italics are added.

### CR-06

**Accepted** · weight 1 · Correction · Sentences of the chapter · Chapter 9 › Summary of Contributions, `chapters/conclusion.tex`, line 88

Suggestion: "a longer-horizon"

Original:

~~~latex
With 20\% of the demonstrations annotated, it outperformed four baselines in two simulated tasks and one real-robot task, with its largest advantages in the  simulated task with a longer-horizon and on the mixed-quality datasets.
~~~

Accepted wording:

~~~latex
With 20\% of the demonstrations annotated, it outperformed four baselines in two simulated tasks and one real-robot task, with its largest advantages in the simulated task with a longer horizon and on the mixed-quality datasets.
~~~

Note written with the suggestion: The hyphenated form is the adjective ("a longer-horizon task"). After "with a" the noun is needed, which is "a longer horizon". The double space after "in the" is removed as well. Nothing else is changed.

### CR-07

**Accepted** · weight 1 · Correction · Sentences of the chapter · Chapter 9 › Summary of Contributions, `chapters/conclusion.tex`, line 91

Suggestion: "the data was" next to "the data were"

Original:

~~~latex
Since the data was mostly collected outside the laboratory, it may better reflect the teaching that can be expected in real-world deployments than typical expert or in-lab datasets.
~~~

Accepted wording:

~~~latex
Since the data were mostly collected outside the laboratory, they may better reflect the teaching that can be expected in real-world deployments than typical expert or in-lab datasets.
~~~

Note written with the suggestion: The chapter writes "the data that were collected" and "how the data were collected" in the sentence that introduces the table, and "the data was" here. This makes the third use plural too, with "were" and "they". Reject it if you prefer the singular in this sentence.
