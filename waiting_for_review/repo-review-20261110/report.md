# Review of the review-your-papers repository

November 10, 2026, on the working tree of `main` at 78a5b7f plus its uncommitted changes. The review read the five skills, their references, the two page templates, and the helper scripts. It was combined with three searches of outside work (LLM peer review, imitation of a personal style and what reads as machine-written, and how skills and plugins are built) and with one count made here on fifteen field dissertations.

The suggestions are on two pages. Nothing in the plugin has been changed.

| Page | What it holds |
| --- | --- |
| `review.html` in this folder | 53 edits to existing files. Accept, reject, or reword each one, then apply. `suggestions.md` is the same list as text. |
| `../repo-review-20261110-proposals/review.html` | 12 larger changes that need new files. Accept means build it. Nothing is applied from that page. |

## 1. Assessment

**What works, and should be kept.** The repository already does the things that outside work finds most effective, and several are rare in comparable projects.

- Every review point carries its evidence, with location and quotation, and the author decides each one. Comparable review skills produce a finished report.
- The style reference is built from the author's own decisions, with a decline weighted above an acceptance. This is the kind of data that the personalization literature finds most useful (TICL, PLUME, DITTO in section 4).
- Edits are minimal by rule, and a correction is kept separate from a rewording. Language models change far more than they are asked to (17 to 20 word types against 0.6 for people on the same instruction), so this rule matters more than any other for a human tone.
- The calibration file records how earlier drafts went wrong. The asking rule for external reviews has no counterpart in the systems surveyed.
- Rules that the validation of November 8 found to be personal choices were scoped as such.

**Where it falls short of its goal.**

1. **It helps review papers, and has no workflow for writing them** (P-01). The goal names writing first. There is a style guide, but no skill that drafts or revises the author's own paper.
2. **The main use of review-paper is not allowed at several target venues** (RP-01). ICRA forbids processing a manuscript with an AI system, and HRI allows AI only to polish a review that no longer identifies the submission. The skill does not check before reading the manuscript.
3. **Human tone is handled by a word list** (WS-01, P-03, P-07). The measurable differences are grammatical and about density, and the three word lists in the repository disagree. One of them flags `crucial`, a Core word of the author's papers.
4. **The editing template still speaks of a dissertation** (TPL-01 to TPL-27). It works on any plain-text document, as the audit confirmed, but its page, messages, README, and default tags are those of one document.
5. **Nothing is tested** (P-04). The audit found four failures that a small test set would catch.
6. **The style rules are not evaluated against the decisions they came from** (P-05).

## 2. Venue rules on AI tools in reviewing

| Venue | Rule | Checked |
| --- | --- | --- |
| ICRA (IEEE RAS) | "Information or content contained in or about a manuscript under review shall not be processed through an AI system." [Reviewer page](https://www.ieee-ras.org/conferences-workshops/fully-sponsored/icra/information-for-icra-reviewers/) | In this review |
| HRI 2026 (ACM) | AI "with the sole purpose of improving the quality and readability of reviewer reports", after removing what identifies the submission. [Page](https://humanrobotinteraction.org/2026/?p=319) | In this review |
| NeurIPS 2025 | "Do not talk about or share submissions with anyone or any LLMs". [Policy](https://neurips.cc/Conferences/2025/LLM) | Research pass, at the source |
| ICML 2026 | Policy A forbids any use. Policy B forbids asking a model to summarize, evaluate, or write. 497 papers were desk-rejected. [Policy](https://icml.cc/Conferences/2026/LLM-Policy) | Research pass, at the source |
| CVPR 2026 | "You cannot share substantial content from the paper or your review with an LLM". [Guidelines](https://cvpr.thecvf.com/Conferences/2026/ReviewerGuidelines) | Research pass, at the source |
| ACL ARR | Not permitted "to use generative assistance to create the first draft". [Guidelines](https://aclrollingreview.org/reviewerguidelines) | Research pass, at the source |
| ICLR 2026 | Disclosure is mandatory. [Blog](https://blog.iclr.cc/?p=1046) | Research pass, at the source |
| CoRL 2026, RSS | CoRL from a search summary only. No RSS rule found. | Not confirmed |

## 3. Count on fifteen field dissertations

To calibrate the rules on tone, the patterns that are often named as signs of machine-written text were counted in the text of fifteen robotics and HRI dissertations (the three committee texts in the plugin and the twelve in `dissertation_reference/text`, about 800,000 words). The script is `tone_measure.py` in this folder. The text includes captions and reference lists, so the rates are approximate.

| Pattern | Dissertations that use it | Median per 10,000 words | Highest |
| --- | ---: | ---: | ---: |
| leverage | 15 | 2.89 | 7.80 |
| robust | 15 | 1.10 | 7.10 |
| serves as, stands as | 15 | 1.19 | 2.13 |
| Moreover, Furthermore, Additionally at a sentence start | 15 | 4.02 | 5.60 |
| a trailing -ing clause after a comma | 15 | 4.83 | 9.63 |
| utilize | 14 | 0.86 | 7.06 |
| em dash | 13 | 1.19 | 51.89 |
| not only … but also | 12 | 0.60 | 1.21 |
| comprehensive | 12 | 0.60 | 3.38 |
| crucial | 10 | 0.58 | 2.23 |
| plays a … role | 10 | 0.20 | 1.86 |
| underscore, showcase | 8 each | 0.12, 0.14 | 0.60, 2.35 |
| pivotal, notably, holistic | 6 each | 0.00 | 0.42, 0.63, 1.97 |
| delve, realm | 2 each | 0.00 | 0.37, 0.20 |
| it is worth noting | 2 | 0.00 | 0.29 |
| shed light | 1 | 0.00 | 0.08 |
| testament, tapestry, pave the way | 0 | 0.00 | 0.00 |

Two things follow. A short list of phrases is safe to flag on sight, since good field writing almost never has them. For the rest, including most of the words that the review checker now flags, one occurrence means nothing, and only a rate compared with the author's own tells anything. The count does not show which dissertations were written with a model's help, so it describes current field writing and not writing by people only.

## 4. Outside sources

"At the source" means the research pass read the paper or page. "Abstract" and "summary" mean only that much was read. The three items marked "in this review" were opened again and confirmed.

**LLM peer review**

- Du et al., ReviewCritique, EMNLP 2024, [arXiv:2406.16253](https://arxiv.org/abs/2406.16253), at the source. 53.2% of LLM strengths rephrase the submission, 30.49% of deficient segments are out-of-scope weaknesses, and scores do not separate accepted from rejected papers.
- AAAI-26 AI review pilot, [arXiv:2604.13940](https://arxiv.org/abs/2604.13940), at the source. Staged passes with self-critique raised recall of planted errors from 0.43 to 0.64. Nitpicking and verbosity were the main complaints.
- Thakkar et al., ICLR 2025 review feedback agent, [arXiv:2504.09737](https://arxiv.org/abs/2504.09737), at the source. 26.6% of reviewers updated their review after feedback, against 9.4%.
- SPOT, [arXiv:2505.11855](https://arxiv.org/abs/2505.11855), summary. No model found more than 21.1% of known errors.
- Li et al., Findings of ACL 2026, [arXiv:2607.22553](https://arxiv.org/abs/2607.22553), abstract. Venue guidelines helped and rubric scoring hurt.
- Lin, [arXiv:2507.06185](https://arxiv.org/abs/2507.06185), summary, and the [ICML 2026 blog](https://blog.icml.cc/?p=1167), at the source, on hidden text in manuscripts.
- [ACL ARR reviewer guidelines](https://aclrollingreview.org/reviewerguidelines), at the source, for the list of review shortcuts.
- Agarwal et al. 2021, [arXiv:2108.13264](https://arxiv.org/abs/2108.13264). Henderson et al. 2018, [arXiv:1709.06560](https://arxiv.org/abs/1709.06560). Kress-Gazit et al. 2024, [arXiv:2409.09491](https://arxiv.org/abs/2409.09491). Hoffman and Zhao 2020, [doi:10.1145/3412374](https://doi.org/10.1145/3412374). Located, not read in full.

**Personal style and tone**

- Reinhart et al., PNAS 2025, [arXiv:2410.16107](https://arxiv.org/abs/2410.16107), at the source. Rates of grammatical features in model and human text.
- Shaib et al., [arXiv:2509.19163](https://arxiv.org/abs/2509.19163), at the source. Density, relevance, and tone predict a "slop" judgment.
- Kobak et al., Science Advances 2025, [arXiv:2406.07016](https://arxiv.org/abs/2406.07016), at the source. Excess vocabulary since 2023.
- "Catch Me If You Can? Not Yet", Findings of EMNLP 2025, [arXiv:2509.14543](https://arxiv.org/abs/2509.14543), at the source. A few examples of an author help, chosen by function.
- TICL, [arXiv:2502.08972](https://arxiv.org/abs/2502.08972), and PLUME, [arXiv:2505.23815](https://arxiv.org/abs/2505.23815), at the source. Failed drafts with explanations, and rules pruned against held-out text.
- Human and LLM proofreading, [arXiv:2506.09021](https://arxiv.org/abs/2506.09021), at the source. Post-editing study, ACL 2026, [arXiv:2604.24444](https://arxiv.org/abs/2604.24444), abstract.
- [Wikipedia, Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), first part read. [humanizer](https://github.com/blader/humanizer), at the source.

**Skills and plugins**

- [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) and [plugin evaluation](https://code.claude.com/docs/en/plugin-evals), at the source.
- [Host and maintain a marketplace](https://code.claude.com/docs/en/plugins/host-marketplace), in this review, for the version rule in REPO-02 and REPO-03.
- [Pre-submission checklist](https://claude.com/docs/plugins/pre-submission-checklist), at the source.
- [RefChecker](https://github.com/markrussinovich/refchecker), [ARIS](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep), [K-Dense scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills), [Orchestra-Research AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs), at the source.

## 5. What was tested

All 53 edits were applied, with every item accepted, to a scratch copy of the plugin. A second run changed nothing.

| Check on the scratch copy | Result |
| --- | --- |
| The three JSON manifests | Valid |
| The five changed Python files, compiled on 3.8.10 | No error |
| The script of the editing page, `node --check` | No error, and no "dissertation" left in the page |
| The shipped example, rebuilt | 7 items, tags kept, since its sample defines `\hang` |
| A Markdown file, no `markers:` line, items file with a byte order mark | No tags written, edit applied |
| A `paper.tex` with and without a `\hang` definition | Tags with, none without |
| `structure_scan.py` on Python 3.8.10, on 3.12, and with a cp1252 console | Runs. Before the change it stops at import on 3.8 |
| `pdf_pages.py` on one validation paper | 69 ligatures before, 0 after. "specific" found 0 times before and 5 after |

## 6. Limits

- The code audit was cut short by a usage limit. It did not read the tools of the committee reference or most of the tools of the full reference, and it did not open either page in a browser.
- The pages were built and their script was checked for syntax. Their appearance was not looked at.
- Sources marked abstract or summary were not read in full, and each card says which.
- The dependent cards are named in their reasons: SCR-01 with SCR-02, REPO-03 with REPO-04, and TPL-27 with TPL-19 to TPL-24.
- After the TPL cards for `review.html` are applied, copy `edit_template/review.html` over `edit_template/example/review.html`, since the two must stay the same.

## 7. How to finish

1. Open `review.html` in Chrome or Edge, decide each card, and save the batch.
2. Dry run: `python plugins/review-your-papers/skills/html-templates/edit_template/apply_decisions.py waiting_for_review/repo-review-20261110 --root .`
3. Apply with `--write` once the dry run looks right.
4. Decide the proposals on the second page. Each accepted one is built as its own change.
