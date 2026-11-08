# Explanatory dash reduction review

Review `dash-reduction-review` of the dissertation, from `waiting_for_review/dash-reduction-review`. Decided between October 12, 2026 and October 12, 2026. Decisions files: `dash-reduction-review.decisions.20261012-152407.json`.

[All reviews](../review-decisions.md) · [Weighted signals](../preference-signals.md) · [Main reference](../hangs-writing-style-reference.md)

| Outcome | Decided by Hang | Not decided by Hang |
| --- | ---: | ---: |
| Accepted as suggested | 6 | 0 |
| Accepted with Hang's edit | 0 | 0 |
| Declined | 0 | 0 |
| Notes from Hang | 0 | |

### DR-001

**Accepted** · weight 1 · Explanatory dash reduction · Chapter 2 · Background · Chapter 2 > Section 2.1 Reinforcement Learning from Human Feedback and Human Characteristics > Human Characteristics and Human Feedback Patterns, `chapters/background.tex`, line 34

Suggestion: Big Five trait list

Original:

~~~latex
The widely used Big Five personality model—comprising openness, conscientiousness, extraversion, agreeableness, and neuroticism—captures these traits \cite{soldz1999big}.
~~~

Accepted wording:

~~~latex
The widely used Big Five personality model, which comprises openness, conscientiousness, extraversion, agreeableness, and neuroticism, captures these traits \cite{soldz1999big}.
~~~

Note written with the suggestion: Replace the paired explanatory dashes with a which clause. Preserve the five traits and the citation.

Used in: [Few colons and semicolons](../hangs-writing-style-reference.md#few-colons-and-semicolons).

### DR-002

**Accepted** · weight 1 · Explanatory dash reduction · Chapter 2 · Background · Chapter 2 > Section 2.1 Reinforcement Learning from Human Feedback and Human Characteristics > Human Characteristics and Human Feedback Patterns, `chapters/background.tex`, line 37

Suggestion: Trust and forgiveness of robot errors

Original:

~~~latex
Trust in robots could also play a role—those with higher trust may be more forgiving of robot errors \cite{karli2023if}, resulting in biased feedback.
~~~

Accepted wording:

~~~latex
Trust in robots could also play a role. Those with higher trust may be more forgiving of robot errors \cite{karli2023if}, resulting in biased feedback.
~~~

Note written with the suggestion: Give the explanation its own sentence. Keep could and may, the citation, and the interpretation about biased feedback. Existing grammar markers surround this passage in the source and remain in place.

Used in: [Few colons and semicolons](../hangs-writing-style-reference.md#few-colons-and-semicolons).

### DR-003

**Accepted** · weight 1 · Explanatory dash reduction · Chapter 3 · CHARM · Chapter 3 > Section 3.1 Study Design > Section 3.1.2 Questionnaire > Teaching Style item, `chapters/charm.tex`, line 116

Suggestion: How participants answered teaching-style questions

Original:

~~~latex
Eight questions were adapted from \cite{ertesvaag2011measuring} to capture participants' teaching styles in classroom scenarios—drawing on their actual teaching experiences when available or assuming their approach otherwise—with a focus on relationship building, routine setting, care, praise, and behavior monitoring.
~~~

Accepted wording:

~~~latex
Eight questions were adapted from \cite{ertesvaag2011measuring} to capture participants' teaching styles in classroom scenarios, with a focus on relationship building, routine setting, care, praise, and behavior monitoring. When answering these questions, participants drew on their actual teaching experiences when available or assumed their approach otherwise.
~~~

Note written with the suggestion: Move the explanatory aside into a separate sentence that names participants as the respondents. Keep the number of questions, citation, classroom context, and all five areas of focus. The source's item command and bold label remain in place.

### DR-004

**Accepted** · weight 1 · Explanatory dash reduction · Chapter 3 · CHARM · Chapter 3 > Section 3.2 Experimental Setup > Section 3.2.3 Procedure, `chapters/charm.tex`, line 202

Suggestion: Number of steps per trajectory

Original:

~~~latex
For each trajectory—comprising approximately 500 to 800 steps—the system recorded task statistics\hang{delete start + Avoid repeating feedback values after the remaining phrase is shortened to feedback.}, feedback values,\hang{delete end} and feedback\hang{delete start + Keep the data summary consistent with the proposed focus on feedback values.} delays\hang{delete end}.
~~~

Accepted wording:

~~~latex
For each trajectory, which comprised approximately 500 to 800 steps, the system recorded task statistics\hang{delete start + Avoid repeating feedback values after the remaining phrase is shortened to feedback.}, feedback values,\hang{delete end} and feedback\hang{delete start + Keep the data summary consistent with the proposed focus on feedback values.} delays\hang{delete end}.
~~~

Note written with the suggestion: Integrate the trajectory-length explanation with which comprised. Keep the approximate range of 500 to 800 steps and all recorded quantities. Existing deletion annotations are preserved exactly, so this suggestion does not resolve that separate review.

### DR-005

**Accepted** · weight 1 · Explanatory dash reduction · Chapter 3 · CHARM · Chapter 3 > Section 3.3 Results > Section 3.3.2 Correlations between Human Feedback Pattern and Human Characteristics, `chapters/charm.tex`, line 288

Suggestion: Which feedback patterns are analyzed

Original:

~~~latex
This subsection analyzes the correlation between human characteristics and feedback patterns—namely, feedback values\hang{delete start + Keep the subsection scope consistent with the proposed removal of delay analysis.} and delays\hang{delete end}.
~~~

Accepted wording:

~~~latex
This subsection analyzes the correlation between human characteristics and feedback patterns in terms of feedback values\hang{delete start + Keep the subsection scope consistent with the proposed removal of delay analysis.} and delays\hang{delete end}.
~~~

Note written with the suggestion: Replace the dash and namely with in terms of, making the explanatory relationship part of the sentence. The existing proposed deletion of and delays remains marked exactly as it is.

### DR-006

**Accepted** · weight 1 · Explanatory dash reduction · Chapter 4 · Demonstration Sidetracks · Chapter 4 > Section 4.1 Introduction > Figure caption (label pipeline), `chapters/sidetracks.tex`, line 70

Suggestion: Four sidetrack types in the figure caption

Original:

~~~latex
The \thingname{} -- \textit{Exploration}, \textit{Mistake}, \textit{Alignment}, and \textit{Pause} -- are illustrated on the right side of the figure.
~~~

Accepted wording:

~~~latex
The four types of \thingname{} illustrated on the right side of the figure are \textit{Exploration}, \textit{Mistake}, \textit{Alignment}, and \textit{Pause}.
~~~

Note written with the suggestion: Make the explanatory list the main statement of the sentence. Keep all four types, their italics, the sidetracks macro, and the reference to the right side of the figure. The caption structure and the other caption sentences remain in place.
