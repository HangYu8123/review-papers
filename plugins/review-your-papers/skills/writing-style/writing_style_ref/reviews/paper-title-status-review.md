# Original paper titles and PHIRL submission status

Review `paper-title-status-review` of the dissertation, from `waiting_for_review/paper-title-status-review`. Decided between October 14, 2026 and October 14, 2026. Decisions files: `paper-title-status-review.decisions.20261014-235838.json`.

[All reviews](../review-decisions.md) · [Weighted signals](../preference-signals.md) · [Main reference](../hangs-writing-style-reference.md)

| Outcome | Decided by Hang | Not decided by Hang |
| --- | ---: | ---: |
| Accepted as suggested | 5 | 0 |
| Accepted with Hang's edit | 1 | 0 |
| Declined | 0 | 0 |
| Notes from Hang | 0 | |

### PT-000

**Accepted** · weight 1 · Restore review annotation macro · Supporting LaTeX change · Preamble, annotation macros (after the existing Elaine macro), `main.tex`, line 39

Suggestion: Restore the annotation macro needed by the requested markers

Original:

~~~latex
\newcommand{\elaine}[1]{{\color[rgb]{0,.2,.5}{[ESS: {\it #1}]}}}
~~~

Accepted wording:

~~~latex
\newcommand{\elaine}[1]{{\color[rgb]{0,.2,.5}{[ESS: {\it #1}]}}}
% \hang{annotation-macro start}
\providecommand{\hang}[1]{{\color[rgb]{0.7,0.2,0.2}{[HY: {\it #1}]}}}
% \hang{annotation-macro end}
~~~

Note written with the suggestion: The dissertation currently has no definition of \hang. This supporting change restores its existing style from reference_papers/PHIRL/CoRL_2026_main.tex:33, using \providecommand to avoid overriding an existing definition. Accept this item when accepting any chapter revision below. If it is rejected or undecided, defer the tagged revisions unless \hang has been restored separately. The macro-definition change is bracketed by commented \hang markers because printable annotations cannot be emitted in the preamble. The chapter changes use active markers.

### PT-003

**Accepted** · weight 1 · Bold original paper title · Chapter 3 · Considering Human Attributes for Reinforceme… · Chapter 3, opening overview, original-publication sentence, `chapters/charm.tex`, line 12

Suggestion: Bold the CHARM paper title

Original:

~~~latex
The related work for this chapter is reviewed in \autoref{sec:bg-rlhf} , and the work presented in this chapter was originally published as ``CHARM: Considering Human Attributes for Reinforcement Modeling''~\cite{fang2025charmconsideringhumanattributes}.
~~~

Accepted wording:

~~~latex
The related work for this chapter is reviewed in \autoref{sec:bg-rlhf} , and the work presented in this chapter was originally published as ``\textbf{CHARM: Considering Human Attributes for Reinforcement Modeling}''~\cite{fang2025charmconsideringhumanattributes}.
~~~

Note written with the suggestion: Apply \textbf to the original paper title so it is easier to find. Preserve its wording, quotation marks, citation, and the surrounding sentence. Requires PT-000 or an existing \hang definition.

Used in: [Headings that name the question or finding](../hangs-writing-style-reference.md#headings-that-name-the-question-or-finding).

### PT-004

**Accepted** · weight 1 · Bold original paper title · Chapter 4 · Categorizing Systematic Non-Optimality in Hu… · Chapter 4, opening overview, original-publication sentence, `chapters/sidetracks.tex`, line 15

Suggestion: Bold the Demonstration Sidetracks paper title

Original:

~~~latex
The related work is reviewed in \autoref{sec:bg-lfd} , and the work presented in this chapter was originally published as ``Demonstration Sidetracks: Categorizing Systematic Non-Optimality in Human Demonstrations''~\cite{fang2025demonstrationsidetrackscategorizingsystematic}.
~~~

Accepted wording:

~~~latex
The related work is reviewed in \autoref{sec:bg-lfd} , and the work presented in this chapter was originally published as ``\textbf{Demonstration Sidetracks: Categorizing Systematic Non-Optimality in Human Demonstrations}''~\cite{fang2025demonstrationsidetrackscategorizingsystematic}.
~~~

Note written with the suggestion: Apply \textbf to the original paper title so it is easier to find. Preserve its wording, quotation marks, citation, and the surrounding sentence. Requires PT-000 or an existing \hang definition.

### PT-005

**Accepted** · weight 1 · Bold original paper title · Chapter 5 · Reconsidering Scalar Feedback in Interactive… · Chapter 5, opening overview, original-publication sentence, `chapters/steady.tex`, line 16

Suggestion: Bold the STEADY paper title

Original:

~~~latex
The related work is reviewed in \autoref{sec:RW} , and the work presented in this chapter was originally published as ``From `Thumbs Up' to `10 out of 10': Reconsidering Scalar Feedback in Interactive Reinforcement Learning''~\cite{yu2023thumbs}.
~~~

Accepted wording:

~~~latex
The related work is reviewed in \autoref{sec:RW} , and the work presented in this chapter was originally published as ``\textbf{From `Thumbs Up' to `10 out of 10': Reconsidering Scalar Feedback in Interactive Reinforcement Learning}''~\cite{yu2023thumbs}.
~~~

Note written with the suggestion: Apply \textbf to the complete original title, including its From 'Thumbs Up' to '10 out of 10' opening. Preserve its wording, quotation marks, citation, and the surrounding sentence. Requires PT-000 or an existing \hang definition.

### PT-006

**Accepted** · weight 1 · Bold original paper title · Chapter 6 · An Unexplored Human Feedback Signal for Teac… · Chapter 6, opening overview, original-publication sentence, `chapters/progress.tex`, line 15

Suggestion: Bold the Progress paper title

Original:

~~~latex
The related work for this chapter is reviewed in \autoref{sec:bg-combine} , and the work presented in this chapter was originally published as ``How Much Progress Did I Make? An Unexplored Human Feedback Signal for Teaching Robots''~\cite{yu2024much}.
~~~

Accepted wording:

~~~latex
The related work for this chapter is reviewed in \autoref{sec:bg-combine} , and the work presented in this chapter was originally published as ``\textbf{How Much Progress Did I Make? An Unexplored Human Feedback Signal for Teaching Robots}''~\cite{yu2024much}.
~~~

Note written with the suggestion: Apply \textbf to the complete original paper title so it is easier to find. Preserve its wording, quotation marks, citation, and the surrounding sentence. Requires PT-000 or an existing \hang definition.

### PT-007

**Accepted with Hang's edit** · weight 4 · Bold original paper title and update submission status · Chapter 7 · Aligning Learned Rewards with Task Progress… · Chapter 7, opening overview, submission-status sentence, `chapters/phirl.tex`, line 15

Suggestion: Add PHIRL's bold paper title and mark it submitted and under review

Original:

~~~latex
At the time of writing, the work presented in this chapter is in submission.
~~~

Suggested:

~~~latex
At the time of writing, the work presented in this chapter, titled ``\textbf{PHIRL: Aligning Learned Rewards with Task Progress for Inverse Reinforcement Learning}'', has been submitted and is under review.
~~~

Hang's wording:

~~~latex
At the time of writing, the work presented in this chapter, titled ``\textbf{PHIRL: Aligning Learned Rewards with Task Progress for Inverse Reinforcement Learning}'', has been submitted to ICRA 2027 and is under review.
~~~

Note written with the suggestion: The existing sentence does not name the paper. Add the exact title from reference_papers/PHIRL/CoRL_2026_main.tex:39 in bold, and replace 'is in submission' with 'has been submitted and is under review', as requested. The status comes from the user's instruction; no submission venue or date is inferred. The title and status are one revision of this sentence so accepted edits do not overlap. Requires PT-000 or an existing \hang definition.

Not used in a pattern: Content requests in Hang's notes or edits, about citations and the publication status rather than wording.
