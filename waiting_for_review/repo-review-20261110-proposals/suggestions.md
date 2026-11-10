# Review: larger proposals for the review-your-papers repository

Twelve changes that need new files or touch several files, so they cannot be applied as passage edits. Accept means build it, reject means leave it, and a note or an edit to the proposal changes what is built. Nothing is applied from this page. The passage edits are on the first page, repo-review-20261110, and report.md there has the assessment and the links.

12 items, built 2026-11-10 05:21. Open `review.html` in this folder to check each one. Nothing here edits the dissertation.

## Requests

**R1** (2026-11-10, by Hang)

> review and propose suggestions for this repo (suggestions in html template). this repo is to help me writing papers and review papers in Hang Yu's style while remaining high quality, human tone, and personal style. combine with SOTA papers, methods, repos, and reports to propose suggestions. this repo should be general rather than only work for my dissertation or just one work.

## Writing in Hang's style

### P-01

- **Location:** plugins/review-your-papers/skills/, plugins/review-your-papers/skills/
- **Kind:** Proposal
- **Note:** This is the largest gap against the goal of the repository, which names writing before reviewing. Retrieving the author's own passages improved personalized generation by 12 to 24% on LaMP (arXiv:2304.11406, from a summary). Five examples of an author beat none on every dataset, more than five added little, and examples chosen for similar content hurt (Findings of EMNLP 2025, arXiv:2509.14543, read at the source), so step 4 picks by the kind of passage. Rules and examples together beat examples alone by up to 9% (PLUME, arXiv:2505.23815, read at the source). Step 3 follows a 2026 study in which drafts post-edited from a model stayed closer to the model's style than to the writer's own (arXiv:2604.24444, abstract only).

**Proposal**

```latex
Add skills/write-paper/SKILL.md for drafting and revising Hang's own text: a conference or journal paper, a thesis chapter, an abstract, a response to reviewers.
1. Collect the facts first. Claims, numbers, and citations come from the author's notes, result files, and source. A missing fact is marked for the author and never filled in.
2. Agree on the argument chain with the author before any prose, as the advisor skill does.
3. Start from the author's own text wherever there is some, and draft new text only where asked.
4. Before drafting a passage, read the guide's rules for that kind of passage and two or three of the author's own passages of the same kind (P-06).
5. Check the draft with the scripts (P-03) and against the paper's term sheet (P-07).
6. Show every change on the editing page, and apply only what is accepted.
7. Offer to import the decisions into the style reference.
```

**Now**

```latex
The plugin has two review skills and three skills they use, and its description is "Two paper-review skills and the three skills they use". The style guide says it is for drafting and revising, but it is a reference of rules. No skill gives a workflow for the author's own paper. The only route to edits on one's own draft is the last section of review-paper.
```

### P-06

- **Location:** plugins/review-your-papers/skills/writing-style-portable/, plugins/review-your-papers/skills/writing-style-portable/
- **Kind:** Proposal
- **Note:** Five examples of an author beat none on every dataset, and going from 2 to 10 barely helped (arXiv:2509.14543, read at the source), so a small file is enough. Examples chosen for similar content lowered attribution accuracy from 69.3 to 36.0 on one dataset, so grouping by function matters. Rules and examples together beat examples alone (PLUME). In one 2026 comparison, a described style profile and few-shot examples both scored below the level of a different author on an authorship model (arXiv:2608.19746, one author, small local models), which is a reason to keep the human edit pass whatever is added.

**Proposal**

```latex
Add writing-style-portable/exemplars.md with about 25 short passages from Hang's six published papers, grouped by what the passage does: a gap statement, a contribution list, the intuition of a method, a results paragraph, an unexpected result, a limitation, the close of a related-work passage, an abstract. Choose them by function and not by topic, and read two or three before drafting a passage of that kind. Add the triples from P-05 as examples of what was declined.
```

**Now**

```latex
The portable guide was condensed by removing the quotations from the author's papers. It keeps the rules and short before-and-after pairs. An agent drafting a results paragraph sees the rule for one, and no complete paragraph that Hang wrote.
```

### P-07

- **Location:** plugins/review-your-papers/skills/writing-style-portable/vocabulary.md, plugins/review-your-papers/skills/writing-style-portable/vocabulary.md
- **Kind:** Proposal
- **Note:** Kobak et al. (Science Advances 2025, arXiv:2406.07016, read at the source) derived 454 excess words from frequency before and after 2023, which is the sound way to build such a list. The count for this review supports the rebuild: delve, realm, testament, pave the way, and it is worth noting appear in two or fewer of fifteen dissertations, while crucial appears in ten, showcase and underscore in eight, and leverage in all fifteen.

**Proposal**

```latex
Split the file into vocabulary-general.md, with the research-writing words, the words to watch, the phrases replaced in review, and the rule for fixed meanings, which is always read, and one file per research area, which is read when the paper is in that area.
Add a helper that lists the defined terms and acronyms of a new paper from its source, as the start of that paper's term sheet (WS-03).
Keep the words to watch in one data file that the checker and the scan read. Rebuild it from counts: a word stays on the list only when Hang's papers and the field dissertations almost never use it.
```

**Now**

```latex
vocabulary.md is the largest file of the portable skill, and most of it lists the terms of six studies on learning from human feedback. For a paper on another topic these lists are read and not used.
The words to watch exist in three places that disagree: Part 3 of vocabulary.md (about 70 words), AI_WORDS in check_review.js (15 patterns, among them crucial and notably), and PET_PEEVES in structure_scan.py.
```

### P-08

- **Location:** plugins/review-your-papers/skills/writing-style-portable/writing-style-guide.md, plugins/review-your-papers/skills/writing-style-portable/writing-style-guide.md
- **Kind:** Proposal
- **Note:** These are the passages a reviewer reads first, and a response to reviewers is a kind of writing the plugin does not handle at all. The advisor's guide has a standard for captions, but it is the advisor's standard and not a record of Hang's choices. Widom's five questions for an introduction and Mensh and Kording's context, content, conclusion structure can serve as a check on the result, not as its source.

**Proposal**

```latex
Collect the evidence in the same way as for the existing patterns: the abstracts, titles, and captions of the six papers, and Hang's past responses to reviewers if Hang provides them. Write the four sections from that evidence, and show them on the editing page before they enter the guide. No rule is written from outside sources alone.
```

**Now**

```latex
Neither the portable guide nor the full reference has a pattern for an abstract, a title, a figure caption, or a response to reviewers. Both files were searched for these words. The guide covers introductions, openings, results, discussion, related work, endings, tables, and slides.
```

## Checks by script

### P-02

- **Location:** review-paper/review-tools/check_review.js, review-paper/review-tools/check_review.js
- **Kind:** Proposal
- **Note:** The audit ran the checker on fixtures: a quote that is not in the paper, a placeholder id, and an 8-word summary all passed with exit code 0. A false quote is the error the skill calls most costly, and it is the one check a script can do exactly. A warning that the instructions say to ignore teaches the agent to ignore warnings. The count warning works against RP-03.

**Proposal**

```latex
Keep one copy in html-templates/review_template/, next to the page whose data it checks, and call it from both skills.
Add --paper paper.txt: find every quoted span of each evidence text in the paper text, after normalizing spaces, hyphens at line ends, quotation marks, and ligatures, and report the ones that are not found.
Add a review_kind field (external, own, mock) that switches the rules for external reviews on and off.
Read the words to watch from one file in writing-style-portable (P-07).
Turn the warning for fewer than two weaknesses into a note that says the range is not a target.
Report a placeholder id as an error.
```

**Now**

```latex
check_review.js exists in two copies that must stay the same. They are the same today, and only a warning in install.py guards them.
It does not read the paper, so the first item of the calibration checklist, that each quote appears in paper.txt word for word, is checked by hand.
It warns about a missing not-an-expert line on a mock review, a warning the advisor skill tells the agent to ignore.
It warns that crucial "reads as AI-written", although crucial is a Core word of Hang's papers and 10 of the 15 field dissertations use it.
It warns when a review has fewer than two weaknesses.
It accepts a placeholder review_id such as [unique-paper-review-id], and it notes references only above six where the rule is one to five.
```

### P-03

- **Location:** plugins/review-your-papers/skills/writing-style-portable/, plugins/review-your-papers/skills/writing-style-portable/
- **Kind:** Proposal
- **Note:** GPT-4o writes present-participle clauses at 5.3 times the human rate and nominalizations at 2.1 times (Reinhart et al., PNAS 2025, read at the source), which a word list cannot see. Models keep writing em dashes when told not to, from 0 to 9.1 per 1,000 words by model (arXiv:2603.27006, abstract only), so a rule the author cares about needs a count. LLMs given a proofreading instruction changed 17 to 20 word types where people changed 0.6 (arXiv:2506.09021, read at the source), which is what mode 2 measures. A benchmark by the author of one such tool found that generic anti-slop linters add little on current models (hackernoon, October 2026), so the comparison is with Hang's own rates and not with a general list. The count on fifteen dissertations in report.md shows which patterns are safe to flag.

**Proposal**

```latex
Add writing-style-portable/scripts/style_check.py for .tex, .md, and .txt.
Mode 1, a draft: report per 1,000 words, next to the author's own rate and the field range in field-conventions.md, the em dashes, colons, semicolons, sentence length and the share over 35 words, first person, hedges, the words that field writing almost never uses, trailing comment clauses, not only … but also, nouns made from verbs, and repeated sentence openers.
Mode 2, an items file: compare each proposed edit with its original and report a number, unit, citation, or hedge that changed, and the share of words changed.
The output is a report for the agent, and nothing is rewritten.
```

**Now**

```latex
The style rules are enforced by the agent reading the guide. The only style code is inside check_review.js, which reads review text only, and check_vocabulary.py, which checks vocabulary and is documented with paths from the dissertation folder. committee_style_ref/tools/profile_draft.py already computes the field measures, but only for the compiled dissertation.
```

### P-10

- **Location:** plugins/review-your-papers/skills/, plugins/review-your-papers/skills/
- **Kind:** Proposal
- **Note:** RefChecker (github.com/markrussinovich/refchecker) checks these four sources and gives three verdicts, and ARIS (github.com/wanshuiyin/Auto-claude-code-research-in-sleep) keeps a "verify_pending" state so that a failed lookup is not read as a made-up reference. The ml-paper-writing skill of Orchestra-Research is built around never writing a reference from memory. The advisor's guide already asks for a reference check in the last days before a deadline.

**Proposal**

```latex
Add a helper, used by write-paper (P-01) and by advisor-review-paper at wrap-up, that looks up each .bib entry by title in Crossref, DBLP, Semantic Scholar, or OpenAlex. It reports an entry that is not found, or whose authors, year, or venue differ, and reports "could not check" when a service does not answer. Only the bibliographic strings leave the machine. For a manuscript under review it runs only when the venue's rule allows it.
```

**Now**

```latex
Nothing checks the reference list of a paper that is being written or reviewed. A reference that does not exist, or that has the wrong authors or year, is the most visible mark of text drafted with a language model.
```

### P-11

- **Location:** plugins/review-your-papers/skills/review-paper/scripts/pdf_pages.py, plugins/review-your-papers/skills/review-paper/scripts/pdf_pages.py
- **Kind:** Proposal
- **Note:** This is the script side of RP-02. Simple injections moved model reviews to acceptance in the studies the research pass found (arXiv:2509.10248 and arXiv:2508.20863, from summaries), and attacks that evade a text filter exist (arXiv:2605.05271, from a summary), so the list helps and does not guarantee anything.

**Proposal**

```latex
After extraction, list the sentences that address a reviewer or a language model, such as "ignore previous instructions", "as a language model", "give a positive review", or "include the phrase", with their pages. Where an OCR tool is installed, compare the text of each page with the OCR of its rendered image and list what only the text layer has. Print the list as findings for Hang.
```

**Now**

```latex
pdf_pages.py writes all the text it extracts, visible or not, and the agent reads it as the paper.
```

## Tests and evaluation

### P-04

- **Location:** repository root, repository root
- **Kind:** Proposal
- **Note:** Anthropic's skill authoring guide says "Create evaluations BEFORE writing extensive documentation" and asks for at least three (read at the source by the research pass). The audit found four failures that a test of this size catches: the byte order mark, the markers default, the root fallback, and Python 3.8. `claude plugin eval` runs each case with and without the plugin and reports the difference. Each run is a billed model call, so the evals belong in a manual workflow and the tests in CI.

**Proposal**

```latex
tests/, standard library only:
- build edit_template/example and compare with the committed suggestions.md and review-data.js;
- apply every item twice, where the second run must change nothing;
- a Markdown document, an items file with a byte order mark, and a paper.tex without main.tex;
- check_review.js on one good and one bad review-data.js;
- the identical-copies check.
A GitHub Actions workflow that runs them on Windows, macOS, and Linux with `claude plugin validate --strict`.
evals/ for `claude plugin eval`, with at least three cases per skill, including prompts that should start the other review skill.
```

**Now**

```latex
There is no test, fixture runner, evaluation, or CI configuration. Every change so far was checked by hand in a scratch copy, in the validation of November 8 and in this review. Three sets of files must stay identical (the two review-tools folders, review.html and example/review.html, the dissertation texts stored twice), and one of them is guarded by a warning.
```

### P-05

- **Location:** plugins/review-your-papers/skills/writing-style/writing_style_ref/sources/review-decisions.json, plugins/review-your-papers/skills/writing-style/writing_style_ref/sources/review-decisions.json
- **Kind:** Proposal
- **Note:** The decision log is the most valuable data in the repository, and it is the kind that the personalization literature finds most useful. TICL (Findings of NAACL 2025, arXiv:2502.08972, read at the source) adds the model's own failed drafts with an explanation of how they differ from the author's text, and the explanations were its largest gain. PLUME (read at the source) checks each inferred rule against held-out text of the author and prunes the ones that fail, and beats the earlier method by 33%. Writers rate post-edited model text as their own style when it is not (arXiv:2604.24444, abstract only), so decisions are a better measure than asking. The research pass found no published protocol for this, so the first version should be small.

**Proposal**

```latex
Hold out the decisions of the latest reviews. For each original passage in them, have the skill propose an edit with the current guide and without it, and compare with what Hang decided: a declined change is not proposed again, an accepted wording is matched, and Hang's own rewording is approached. Report the rates with each release of the guide.
Store "proposal, Hang's version, why" from the edited and declined items as examples for P-06.
```

**Now**

```latex
The reference records Hang's decision on several hundred proposed edits, with weights (review-decisions.json, about 15,000 lines). The decisions are used to write rules. They are not used to test whether a change to the guide produces proposals that Hang accepts more often.
```

## Repository and packaging

### P-09

- **Location:** plugins/review-your-papers/skills/writing-style/, plugins/review-your-papers/skills/writing-style/
- **Kind:** Proposal
- **Note:** Anthropic's pre-submission checklist (read at the source by the research pass) blocks a plugin without a LICENSE file or license key, stops validation above 5 MiB for one file, and holds for a reviewer any text file over 256 KiB and any plugin with more than 512 files. Whether the full texts may be redistributed depends on each dissertation's terms, which this review did not check, so it is raised as a question.

**Proposal**

```latex
Store the dissertation texts once, or keep only the measures and the quoted excerpts and leave the full texts out of the public repository.
Before a directory submission, move sources/ and the review records out of the installed skill into a folder outside plugins/.
Add a license. The choice is Hang's.
```

**Now**

```latex
writing-style is 9.9 MB of the 11.0 MB that git tracks. The texts of three dissertations are stored twice, 2.7 MB in total. tech-vocabulary.json is 2.3 MB and review-decisions.json 1.0 MB. The skill tells agents not to load these files.
The repository has no LICENSE file and no license field in plugin.json.
The full texts of three other authors' dissertations are in a public repository.
```

### P-12

- **Location:** plugins/review-your-papers/skills/, plugins/review-your-papers/skills/
- **Kind:** Proposal
- **Note:** Anthropic's guide says: "For reference files longer than 100 lines, include a table of contents at the top", since the model may read only the head of a long file, and "Keep references one level deep from SKILL.md". The Claude Code documentation describes user-invocable: false as "for background knowledge users shouldn't invoke directly". Both were read at the source by the research pass.

**Proposal**

```latex
Add a contents list at the top of the three files.
Set user-invocable: false on html-templates and writing-style, so that the command list shows the skills a person starts.
Keep the ../<skill>/ paths, since Codex documents no path variable, and say in the compatibility field of each review skill that the five skills install together.
```

**Now**

```latex
writing-style-guide.md (497 lines), vocabulary.md (356), and field-conventions.md (182) have no contents list. calibration.md and advisor-guide.md have one.
html-templates and writing-style are read by the other skills, and they are also offered to the user as commands.
The five descriptions are between 581 and 719 characters, inside the limit of 1,024.
```
