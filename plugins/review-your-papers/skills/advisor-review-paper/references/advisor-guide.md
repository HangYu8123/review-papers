# Advisor's Paper-Writing Guide (reference for the review)

Condensed from the advisor's guide, "Dr. Short's Paper-Writing Tonic" (Elaine Schaertl Short). This is the standard the paper is reviewed against. It describes one way to write an HRI conference paper, not the only way. Use it as the source of each finding and each proposed revision, and quote or paraphrase it to explain *why* something matters. The questions under each section are checks to answer about the paper, not questions to ask the student.

Page lengths assume an 8–9 page conference format. Scale up or down for other limits.

## Contents
1. Cross-cutting principles (apply to every section)
2. Introduction
3. Background / Related Work
4. Algorithm (or computational approach)
5. Methodology / Validation (and subsections)
6. Results
7. Discussion
8. Conclusion
9. Figures and tables
10. Pet peeves (style patterns) and why
11. Editing for length
12. Timeline (for context if the student asks "is it too early/late for this?")

---

## 1. Cross-cutting principles

- **Central argument.** The paper should have a coherent chain of logic: problem → why it matters → why it's hard / what's missing in prior work → what we did → what we found → why that matters. Every section carries some link of that chain.
- **Every paragraph has a point** — usually a claim, sometimes a topic or key idea. A reader should be able to say what the paragraph is for.
- **Every section signposts.** Early in each section, tell the reader what the section covers and how it's organized, so they can follow along.
- **Length outliers.** Watch for very long sentences, very long paragraphs, and very short (1–2 sentence) paragraphs.
- **Don't over- or under-state.** "Just say what you did and make the case for why it's interesting and important."
- **Readability.** Avoid convoluted sentence structures, run-on sentences, verbed nouns, and unnecessary passive voice (sometimes passive is right — be sure it's the best way to express the idea).

Questions to draw on:
- "Which link of your argument does this section / paragraph carry?"
- "In one sentence, what is the point of this paragraph? Where is that sentence in the paragraph?"
- "After reading the first paragraph of this section, what would a reader expect the rest to contain?"
- "Is this claim stronger or weaker than your evidence supports?"

## 2. Introduction

**Purpose:** get the reader excited and summarize why the work is interesting. If the student only has time to carefully edit one section, it should be this one. Highlight the "value added": what does the paper do that others in the field should be excited about?

**Length:** ~1–1.5 single-column pages, or about one full column in two-column format. For workshop papers/abstracts, often merged with Background.

**Every introduction must answer:**
1. What is being done?
2. What is the current state of the art in the field?
3. Why is our thing new?
4. Why is our thing important?

**Typical structure:**
- **Paragraph 1 — The hook.** Convince the reader the problem is important and interesting. A vivid example of what the solution lets you do; why the problem is broadly applicable; why it's hard. Avoid "throat clearing": trite sentences obvious to anyone in the field (e.g., "Robots are becoming increasingly important in society."). Test: if the intro still makes sense with the first sentence deleted, it's probably throat-clearing.
- **Paragraph 2 — The approach.** High-level summary of the approach and its unique features (aspects others don't consider; the key insight that enables the work). Name and describe any algorithms developed.
- **Paragraph 3 — The results.** Summarize results. For a user study: statistically significant, interesting results ("We show that…"). For an algorithm: advantages over prior work ("achieves x% accuracy, an improvement of y%…" or "addresses z problem, not addressed by prior work"). Each sentence or pair of sentences should state a key contribution **and the evidence for it**.

**Revisit after writing Discussion and Conclusion** to make sure the intro highlights the interesting points made there.

Good questions:
- "Can you point to the sentence that answers each of the four questions?"
- "Read your first sentence. Would anyone in your field disagree with it or learn something from it?"
- "Where does the reader learn why this problem is *hard*?"
- "For each contribution in your results paragraph, where's the evidence right next to it?"
- "What's your key insight — the thing others don't do? Is it named?"
- "Does your intro promise anything the paper doesn't deliver, or undersell anything it does?"

Figure: ideally the first page has a figure summarizing the approach (system diagram, pipeline, photo of the core interaction); if the format disallows it, page 2.

## 3. Background / Related Work

**Purpose:** overview of relevant literature on both the human and technical side; may also justify the approach by appeal to literature (e.g., psychology literature for why a social process matters). Resist the urge to list and describe the 3–4 most relevant papers in detail.

**Length:** about the same as the intro (1–1.5 single-column pages / one column), perhaps slightly longer if the intro was short. Almost never has a figure.

**Citations:** cite anyone who might read the work; if space is tight, cite at least one paper from each relevant lab (last author).

**Typical structure:**
- **Paragraph 1 — Summary.** Name the relevant areas / approaches. After this paragraph the reader should know how the section is structured (signposting).
- **Paragraphs 2–n — One aspect of prior work each.** Can summarize papers ("Work by X et al. does a, b, c, evaluated in context y"), but must also give a high-level point ("Our work builds on the general approach of [x], [y], [z] by doing [a]"). For justification / adjacent areas (e.g., social science), a high-level summary with example citations is enough. For prior approaches to the same problem, be specific: summarize, draw connections, and say how this work improves on or contributes to the state of the art. Advisor's usual order: justifications and generally related areas first, then specific prior approaches — but flow matters most.
- **Paragraph n+1 (optional) — Another summary.** How our approach builds on / contributes to prior work.

Good questions:
- "For this paragraph, what's the high-level point — not the list of papers, but what the reader should conclude?"
- "Where does this paragraph connect back to your work?"
- "Is this section organized by idea, or by paper?"
- "Who might review this paper? Are their labs cited?"
- "Does this section establish the 'state of the art' link of your argument, and the gap your work fills?"

## 4. Algorithm (or Computational Approach)

Depending on the paper: a Methodology section; Algorithm + Validation sections; or Data Collection + Algorithm sections. Advisor's recommendation: start with just Methodology and promote the Algorithm to its own section if it gets long or complicated.

**Length:** Algorithm + Methodology/Validation/Data Collection together ≈ half the paper (≈3–4 pages of 8). Algorithm-focused papers: longer end (4–4.5 pages), especially with data collection. Human-insight papers: shorter here, longer Results.

**Tense and voice:** typically present tense. The subject of sentences is usually "the algorithm" or "our method" ("the algorithm chooses among the set of possible actions"), not "we" — first person implies a human in the loop or ad-hoc design decisions.

**Structure:**
- **Paragraph 1:** 2–3 sentence high-level summary of what the algorithm does and how (signposting).
- **Preliminaries** (optional): assumptions, notation, key ideas.
- **Problem formulation / formalization** (optional): how the problem is formalized computationally — many HRI problems can be framed multiple ways.
- **Algorithm:** high-level description *and* pseudocode. Give the algorithm a name (memorable, easier to refer to).

**Notation:** should make things clearer, not murkier — test by having someone else read it. Avoid too many decorators (subscripts, superscripts). Pick coding conventions (= assignment, multi-character names, arrays) or math conventions (← assignment, single-character names, sets) and stick with one. Sub-sections should divide the algorithm in a way that aids understanding. Go back and forth between code and written algorithm to keep them consistent.

Good questions:
- "Could a labmate who hasn't seen your code follow this? Have you asked one?"
- "Who is the subject of most sentences here?"
- "Is your notation consistent with one convention throughout?"
- "Does the opening paragraph tell the reader what the algorithm does before diving into details?"

## 5. Methodology / Validation

**Length:** see Algorithm (shared ≈ half the paper).

**Tense:** past tense preferred ("We tested…"), present acceptable — consistency is what matters.

**Paragraph 1:** 1–2 sentence high-level summary of what was done, then (for most papers) hypotheses. The summary must give enough information to understand the hypotheses. Very detailed hypotheses can get their own subsection at the end of the section or start of Results.

**Subsections (use what applies):**
- **Data Collection:** how data used to train/parameterize the model was collected (similar to Experimental Design). Can go before or after the algorithm description.
- **Algorithm** (if no top-level Algorithm section): then call the experiment section "Validation Study"; otherwise "Experimental Design."
- **Parameterization:** how parameters were derived from collected data, using the same notation as the algorithm.
- **Robot / Hardware and Software:** height, degrees of freedom, general type (humanoid?), underlying software; footnote link if open source. Goes before experiments; can be demoted to a paragraph.
- **Experimental Design / Protocol / Validation Study:** detailed enough to replicate exactly. Include: design (within/between/mixed), conditions, what participants were told, duration, ordering and counterbalancing/randomization, assignment to conditions, the space and setup, exactly what the robot said and did, anything else needed to replicate. Algorithmic papers with multiple experiments (e.g., simulation then real world): one subsection each.
- **Measures:** cite questionnaires; reproduce any self-developed questions exactly; explain derived measures (e.g., computer-vision gaze detection).
- **Data Coding:** how coding was done; how coded concepts were defined (operational definitions); percent agreement, Cohen's kappa or similar (watch for unbalanced data).
- **Participants:** can also go at the start of Results. Number, conditions seen, recruitment, demographics (usually age and gender; sometimes race and ethnicity).

Figures: a handful of informative figures, including a picture of the robot if not elsewhere. For human-subjects studies, a picture of the interaction or interaction space if not on page 1.

Good questions:
- "If another lab tried to replicate this tomorrow, what would they have to email you to ask?"
- "Can a reader understand each hypothesis from what's said before it?"
- "Is the tense consistent?"
- "How is each measure defined — could two people compute it the same way?"

## 6. Results

**Purpose:** report results of the study/validation. Graphs and tables help — readable and clear, significant comparisons labeled on graphs, key table cells in bold.

**Length:** longer than the intro, ~1.5–2.5 pages. Longer for human-insight papers, shorter for algorithm papers.

**Structure:** a subsection per major theme — a group of related hypotheses, an aspect of performance (e.g., "Complexity and Running Time"), or one experiment's results.

**Statistics:** p < 0.05 is significant. p ≤ 0.10 can be reported, with effect size to justify why it might become significant with more data. Report t-tests, ANOVAs, etc. in APA format with test statistics, e.g.: "participants rated cats in baths (M = 4.9, SD = 0.15) significantly higher than cats with paper towel tubes (M = 4.5, SD = 0.34), t(127) = 4.65, p < 0.05. This was a large effect (effect size 0.89)."

**Classifiers:** raw accuracy can mislead on unbalanced data — report other statistics (TPR, FPR, F-score) or accuracy relative to chance (e.g., one-tailed t-test).

**Graphs:** axes not cut off in odd places; labels readable; error bars; mark significant comparisons (*, **, *** for increasing significance; "." for marginal); readable for colorblind readers and black-and-white printing.

Good questions:
- "Which hypothesis does this subsection address? Does the subsection say so up front?"
- "Is each statistical result reported with the test statistic, p, and effect size?"
- "Could a reviewer read this figure printed in grayscale?"
- "Is the claim in this sentence exactly as strong as the test supports?"

## 7. Discussion

**Purpose:** wrap up and pop back up to the big picture / vision. Most flexible section.

**Length:** a bit shorter than the intro; Discussion + Conclusion ≈ 0.5–1 page.

- **Paragraph 1 — Contributions:** summarize the contribution and state, for each hypothesis, whether it was supported.
- **Paragraph 2 — Observations (optional):** interesting things that happened, participant quotes, qualitative observations.
- **Paragraph 3 — Future work:** limitations (cases the algorithm doesn't handle, study limitations) framed as future research or replication; then implications — what is this good for, what insights could readers use, where could it lead?

Good questions:
- "Is every hypothesis accounted for here?"
- "Do the limitations you name match what a skeptical reviewer would raise?"
- "Does the 'why it matters' here match what you promised in the intro?"

## 8. Conclusion

One paragraph: very short summary of what was done, closing with one sentence on the vision and long-term implications. Least likely to be read by reviewers. After writing Discussion and Conclusion, go back to the Introduction and make sure it highlights the interesting points.

Good question: "Read your last sentence. Is it about the vision of the work, or a restatement of the method?"

## 9. Figures and tables

- **Every figure supports a key idea or result.** If a figure doesn't serve a link of the argument or a key result, it may not earn its space.
- **Three questions for every figure:** What does a reader parse from it at first glance? What do they get from the details? How do those line up with the overall story/argument of the paper?
- **Readable text:** axis labels, tick labels, legends and annotations readable at printed size; nothing annoys reviewers more than unreadable graphs. If figures are shrunk to save space, enlarge the labels.
- **Color-blind-safe colors**, and readable on black-and-white printers. Don't rely on color alone; use markers, line styles, or direct labels too.
- **Graphs:** axes not cut off in weird places; error bars; significant comparisons marked (*, **, ***; "." for marginal).
- **Page 1 (or 2) figure** summarizing the approach or core interaction; a picture of the robot and of the interaction space for human-subjects studies.
- Aim for at least one float (figure, table, algorithm) per page, but no pages that are only floats.
- Figures generally at the top of the page.
- Tables: few cell walls; a double line between heading and data is fine; bold for the "best" result in a category.

## 10. Pet peeves (style patterns) and why

The advisor's personal preferences — not "errors," but things to avoid:

- **Disparaging your own work** ("simple", "minor"). Focus on strengths without exaggerating.
- **"Works" for prior papers** ("Some works have addressed…"). Use "some researchers have" or "prior work has."
- **Numeric citations as nouns** ("[1] addressed this problem"). Use "Short et al. addressed this problem [1]."
- **Gendered pronouns for participants.** Use singular "they", alternate, or avoid pronouns.
- **"We" as the subject when describing how an algorithm works.** "The algorithm learns a model," not "We learn a model."
- **"Would" when describing a study** ("the robot would take an action"). Implies a hypothetical and reads as weak. Better: "the robot took an action"; best: a specific verb ("the robot picked up the block").
- **"Utilize."** Just say "use."
- **Verbosity:** "in order to" → "to"; unnecessary adverbs ("clearly", "definitely", "extremely", "very").
- **Throat-clearing** openers (see Introduction).
- **Passive voice** where active would be clearer, especially in the intro.

## 11. Editing for length (if the paper is over the limit)

Three passes:
1. **Heavy editing** (more than a page over): drop whole paragraphs or sections — qualitative or non-significant results, long-winded justifications, text that repeats figures/tables.
2. **Cleaning up**, roughly in order: move information between tables and text; combine short paragraphs; turn lists into inline text; cut verbosity; cut short final lines of paragraphs; move floats.
3. **Kludges** (only within ~10 lines of the limit): tighten list spacing, negative vspace, smaller figures (enlarge axis labels if so). These hurt readability.

Work from beginning to end — LaTeX reflow means cuts early on can move things later.

## 12. Timeline (3-month version)

- 3–6 months before: implementation, reading, thinking, verbal iteration.
- 8–12 weeks: rough draft of intro and background.
- 6–8 weeks: rough draft of methodology (coincides with pilots for human-subjects studies).
- 3–4 weeks: rough draft of everything; ~70% done; align scope with advisor.
- 1–2 weeks: second draft; get someone else to read it; figure pipeline basically done.
- 1–2 days: final draft, ready 24–48 hours early (no later than half a work day before). Scope frozen; final read-through, trade with others, polish figures, check references.

Writing is part of research, not an afterthought — drafting often exposes weaknesses in the approach or confounds in the protocol.
