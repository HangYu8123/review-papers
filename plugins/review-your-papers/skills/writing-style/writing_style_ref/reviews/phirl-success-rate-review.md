# PHIRL success-rate figure

Review `phirl-success-rate-review` of the dissertation, from `waiting_for_review/phirl-success-rate-review`. Decided between October 14, 2026 and October 14, 2026. Decisions files: `phirl-success-rate-review.decisions.20261014-095837.json`.

[All reviews](../review-decisions.md) · [Weighted signals](../preference-signals.md) · [Main reference](../hangs-writing-style-reference.md)

| Outcome | Decided by Hang | Not decided by Hang |
| --- | ---: | ---: |
| Accepted as suggested | 4 | 0 |
| Accepted with Hang's edit | 0 | 0 |
| Declined | 0 | 0 |
| Notes from Hang | 0 | |

### SR-01

**Accepted** · weight 1 · New figure · The figure and its description · Chapter 7 › Experiments and Results › PHIRL Outperforms Baselines, `chapters/phirl.tex`, line 511

Suggestion: Add the success-rate figure before the Real Robot results

New text, placed next to this passage:

~~~latex
\textbf{Real Robot}
~~~

Accepted wording:

~~~latex
% [HY created] success-rate figure moved from the PHIRL appendix (fig:succ_rate in appendix-phirl.tex)
\begin{figure*}[!t]
    \centering
    \includegraphics[width=0.95\linewidth]{Results/success_rate.png}
    \caption{Success Rates. The Y-axis indicates the success rate over 100 runs. Task success was decided by the environmental reward. When the agent has achieved success, the single-step return reward is 1. The rows and columns follow the layout of \autoref{fig:res}, with success rates in place of mean rewards. }
    \label{fig:phirl_succ_rate}
\end{figure*}
~~~

Note written with the suggestion: The figure, image path and caption are taken from the appendix (fig:succ_rate) with your caption wording kept. One sentence is added to the caption, since the figure has the same three rows and four columns as Figure fig:res and only the measure differs. The label is new (fig:phirl_succ_rate), so it cannot clash with fig:succ_rate if the appendix is put back into the build. The placement [!t] matches the other figures of the chapter ([h] in the appendix has no effect on a figure*). The figure is placed after the Simulation paragraph that describes it. Accept together with SR-02, which is the only text that refers to it. Style entry: Correcting a sentence without rewording it (your caption sentences are unchanged).

### SR-02

**Accepted** · weight 1 · New text · The figure and its description · Chapter 7 › Experiments and Results › PHIRL Outperforms Baselines, `chapters/phirl.tex`, line 507

Suggestion: Describe the success rates in the Simulation results

New text, placed next to this passage:

~~~latex
These results demonstrate that PHIRL learns effective rewards for RL agents, and is more reliable when the task horizon is longer or the demonstration quality is lower.
~~~

Accepted wording:

~~~latex
% [HY created] success rates from the figure moved from the PHIRL appendix
The success rates of all methods are presented in \autoref{fig:phirl_succ_rate}, where the success rate is the percentage of the 100 evaluation rollouts in which the task was completed.
In Lift-PH, PHIRL and all baselines except Pref reached similar success rates (83\% to 86\%).
In the other three conditions, PHIRL reached higher success rates than the best baseline, with 87\% compared with 66\% in Lift-MH, 36\% compared with 11\% in Can-PH, and 25\% compared with 14\% in Can-MH.
~~~

Note written with the suggestion: Three sentences, added to the Simulation paragraph after the summary of the return rewards and before the pointer to the repository. They give the measure and then the comparison with the baselines. In Lift-PH the success rates of PHIRL (84%), AIRL (83%), AIRL-Pref (86%) and Rank2Reward (85%) are close, and PHIRL is not the highest, so that condition is stated on its own instead of being folded into "PHIRL outperforms". The best baseline is Pref (66%) in Lift-MH, AIRL-Pref and Rank2Reward (11%) in Can-PH, and AIRL-Pref (14%) in Can-MH. No test was run on success rates, so the text says "similar" and "higher" without "significantly". Needs SR-01 for the reference. Style entries: Numbers and measured comparisons ("compared with" in a full sentence), A results paragraph answering one comparison, Reporting a difference that was not detected ("similar" for a comparison without a test).

Used in: [Adding sentences that were not asked for](../hangs-writing-style-reference.md#adding-sentences-that-were-not-asked-for).

### SR-03

**Accepted** · weight 1 · New text · Optional follow-ups · Chapter 7 › Experiments and Results › PHIRL Outperforms Baselines, `chapters/phirl.tex`, line 526

Suggestion: Optional: success rates of PHIRL-online

New text, placed next to this passage:

~~~latex
For instance, in the challenging Can-MH scenario, returns increased from $M=116.99$ to $M=147.28$ ( $p < 0.001$).
~~~

Accepted wording:

~~~latex
% [HY created] PHIRL-online success rates from the figure moved from the PHIRL appendix
In success rate (\autoref{fig:phirl_succ_rate}), PHIRL-online was higher than PHIRL in Lift-PH (95\% against 84\%), Lift-MH (90\% against 87\%), and Can-PH (49\% against 36\%), while both reached 25\% in Can-MH.
~~~

Note written with the suggestion: Optional. The figure also shows PHIRL-online, which the PHIRL vs. PHIRL-online paragraph discusses only in return rewards. One sentence is added after the Can-MH example. In Can-MH the return rose from 116.99 to 147.28, but the success rate of both methods is 25%, which a reader comparing the two figures may ask about, so the sentence states it. Reject if the paragraph should stay about rewards only. Needs SR-01 for the reference. Style entries: Numbers and measured comparisons ("against" inside parentheses), Concession with while.

### SR-04

**Accepted** · weight 1 · Follow-up to the new figure · Optional follow-ups · Chapter 7 › Experiments and Results › PHIRL Outperforms Baselines, `chapters/phirl.tex`, line 509

Suggestion: Optional: drop "success rate" from the list of results in the repository

Original:

~~~latex
More details and results, including more statistical analysis, learning curves, success rate, annotation examples, and additional domains for simulation studies, are available at \url{https://github.com/PHIRL2026}.
~~~

Accepted wording:

~~~latex
More details and results, including more statistical analysis, learning curves, annotation examples, and additional domains for simulation studies, are available at \url{https://github.com/PHIRL2026}.
~~~

Note written with the suggestion: Optional. With SR-01 and SR-02 accepted, the success rates are in the chapter, so the pointer to the repository no longer needs to list them. Only the words "success rate," are removed. Reject if the repository should still be named as a source for success rates (for example, for the additional domains). Style entry: Correcting a sentence without rewording it.
