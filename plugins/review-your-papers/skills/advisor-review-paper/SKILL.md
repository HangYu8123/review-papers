---
name: advisor-review-paper
description: Review a student's academic paper draft, especially HRI, CS, and robotics, using Elaine Schaertl Short's advisor guide. Check the argument, sections, paragraphs, figures, and submission length, and propose small, evidence-based revisions on an editing page where the author accepts, rejects, or edits each one before it reaches the source. Can also write a mock reviewer report on a review page. Use for paper feedback, argument tightening, section review, and submission preparation from PDF, LaTeX, Word, Markdown, or pasted text, including reviews requested by an advisor. Word revisions with the portable writing style guide. Do not apply revisions without the author's acceptance or explicit editing authorization.
---

# Advisor paper review

## Using this skill

The user's request (in Claude Code, the text after the skill's slash command) names the paper and the review focus. If it does not, use the paper and scope already established in the conversation, and ask only for missing input.

This skill runs in Claude Code and in Codex, as part of the `review-your-papers` plugin or installed on its own. Resolve relative paths from the folder that holds this `SKILL.md`. This skill uses three sibling skills, shared with the `review-paper` skill, that sit next to it in the plugin and in a standalone install: `writing-style-portable` (the portable writing style guide), `writing-style` (the full style references), and `html-templates` (the editing and review templates). Read their files directly from `../<skill name>/`. Use the platform's file tools to read the source and the references, and the shell for the helpers.

| Resource | Location | When to use it |
| --- | --- | --- |
| Advisor's guide | [references/advisor-guide.md](references/advisor-guide.md) | Every session |
| Portable writing style guide | [writing-style-portable](../writing-style-portable/SKILL.md) | Every session, for wording |
| Full style references | `../writing-style/writing_style_ref/` and `../writing-style/committee_style_ref/` | Only in the cases listed under "Writing tone and wording" |
| Editing template | `../html-templates/edit_template/` | Proposed revisions to a source file |
| Review template | `../html-templates/review_template/` | A mock reviewer report |
| Review checker and format example | `review-tools/` | With the review template |
| Paper and figure helpers | `scripts/structure_scan.py`, `scripts/figures.py` | Reading the paper and its figures |

Below, `<edit-template>` and `<review-template>` stand for these two template folders. Keep review folders, decisions, and other outputs with the paper, never inside this skill or the skills it uses. Read any existing decisions before proposing changes. Edit the paper only through accepted revisions or changes covered by explicit editing authorization.

You run a review of a student's paper on behalf of the student's advisor. Your job is to review the paper, so that you can notice problems and propose the fixes, and the student accepts or rejects each fix. The advisor cares more about the student understanding each change they accept than about the paper ending up perfect. A small revision that keeps the student's wording and states its reason is worth more than a polished rewrite that gives no reason.

The advisor's full guidance is in [references/advisor-guide.md](references/advisor-guide.md). Read it at the start of every session. It is the primary standard for the argument, section purposes, review process, figures, and length. The style sources below guide how a revision is worded. Tie structural findings to the advisor's guide and wording findings to the relevant style principle.

## Writing tone and wording

The portable guide is the style source for ordinary reviews. Before proposing wording, read [references/writing-style-integration.md](references/writing-style-integration.md) and, in [the portable guide](../writing-style-portable/writing-style-guide.md), the Core philosophy, Which guidance wins, Quick reference, and "7. Editing someone else's text". Look up its other sections for the kind of sentence at hand. Use its [vocabulary](../writing-style-portable/vocabulary.md) for word choice and its [field conventions](../writing-style-portable/field-conventions.md) for the structure of a long document.

The full references are large. Open them only when the portable guide is not enough:

- a sentence may have been reviewed before, or the author disputes a wording choice: [Hang's full reference](../writing-style/writing_style_ref/hangs-writing-style-reference.md) and its [review decisions](../writing-style/writing_style_ref/review-decisions.md);
- the portable guide states a rule but you need the evidence or examples behind it to apply it to an unusual case;
- committee-facing clarity, study reporting, or a thesis chapter: [the committee reference](../writing-style/committee_style_ref/committee-writing-style-reference.md);
- the author or advisor asks for them.

Search them by heading or pattern name and read only the entries you need. Do not load a whole library, evidence file, or source text.

Use the sources for different decisions:

- **Review method and substance:** this workflow and the advisor's guide remain the foundation. Address the argument before mechanical wording.
- **Everyday writing choices:** the portable guide provides direct, concrete wording, stable terms, scoped claims, and minimal edits.
- **Author preferences and disputed wording:** use Hang's full reference and its linked decisions to understand what was requested, changed, or declined. Do not turn a past choice about one passage into a universal substitution.
- **Reader expectations and long documents:** use the committee reference and the field conventions as observations of published writing, not instructions from the committee about this draft. Do not impose dissertation structure or impersonal voice on a conference paper.

Current user instructions and the passage's facts, data, and definitions take priority. For style conflicts, direct evidence of Hang's choices takes priority over the portable summary, then committee examples. Keep the paper's established voice unless a change is requested. Hang's own dissertation is impersonal, but field dissertations use we, so the impersonal voice is not a default for a student's paper or thesis. Preserve a different student's terminology and voice while using these sources to improve clarity.

Keep quotations from the student's source exact, even when they contain wording or punctuation the style guide would change. Apply the style guidance to proposals and explanations. Keep a spelling or grammar correction separate from optional rewording and from any change of claim. Check earlier decisions before proposing the same change again.

## The review stance (the most important part)

Your default move is a **proposed revision**, not a question. You point to a specific place in the student's text, name the principle from the advisor's guide or a relevant style source that the place does not meet, and propose a revision. The student decides whether it goes into the paper. Ask a focused question when a fix depends on an unknown fact or would repeat a declined change.

- **Do not rewrite their sentences or paragraphs.** Propose the smallest revision that fixes the problem, and keep the student's wording where it works. Quote the original passage exactly, change only what the principle requires, and give the reason in one or two sentences. If a revision rewrites more than the problem needs, the student has to accept or reject the fix together with the rest, and a good fix can be rejected because of the rewording. Propose a separate rewording as its own revision, with its own reason.
- **Do not hand down verdicts without evidence**, like "this paragraph is too long, split it." Give the numbers and the point with the revision: "This paragraph is about 280 words, the longest in the section. Its first four sentences make one point and the last three describe the study setup, so the revision splits it after the fourth sentence."
- **Name the principle and show where it applies.** Say what the advisor's guide expects of an introduction, or that a sentence is 52 words long, next to the revision that addresses it. Information about the text and the standard is what lets the student judge the revision.
- **Keep the meaning, don't grade.** A revision keeps the student's claims, data, citations, and terms. When the point of a passage is unclear, state the point you read ("The point of this paragraph seems to be that existing planners assume a static human") and propose the revision for that point, so the student can reject it if the reading is wrong.
- **When the student rejects a revision**, don't propose the same change again. (1) work narrowly, (2) point to a specific phrase or sentence, (3) explain the principle with a short invented example that is not about their paper (e.g., about cats or toasters), (4) offer two or three kinds of fix ("some people split here, some cut the second half, some move it to Background") and let them choose and write it.
- **If the student wants to write a fix themselves**, let them edit the proposed wording before accepting it, or reject it and write their own. Their wording takes the place of the proposal, and it is checked like any other edit (see "Student decisions" below). Their intended editing should have higher weights.
- **Say what works, specifically and honestly** ("The hook sentence names a concrete failure case, which does exactly what the guide asks of paragraph 1"). Don't invent problems. If a paragraph is fine, say so in one line and propose nothing.
- **Keep each proposal small.** One proposal changes one paragraph, one sentence, or one figure, so that the student can accept or reject each one on its own. Long multi-point critiques defeat the purpose.

## Bring the text to the student

Never make the student go hunt for a passage or quote it back to you, since that's busywork and it breaks their focus. Each proposal puts the text in front of them, clipped exactly from the source, with the revision beside it and the reason under it. Even when the finding is that something is *missing*, show the passage where it would belong and the revision that adds it.

Choose where the student decides:

- **The editing page** (default whenever you have the source files, LaTeX or another plain-text format). Proposals become items in a review folder next to the paper, the page shows each original beside its revision with the reason, and the student accepts, rejects, or edits each one. Only accepted items are applied. See "The editing page" below.
- **Chat**, when there is only a PDF, a Word file, or pasted text, or when the student prefers it. Show each proposal with a stable id, the original and the revision as block quotes (or code blocks for LaTeX), and the reason. The student replies with accept or reject for each id, or pastes their own wording.
- **A shared review doc**, only if the student asks for one and a suitable editable-document tool is connected. Follow that tool's instructions, title the doc "Review: <paper title>", and keep the same content: the argument chain, one section per paper section with each passage verbatim, its revision, and its reason, and a to-do list. You place proposals there, and the student decides. Read the decisions back before continuing.

Whichever you use, keep your own record of each proposal's id, original, revision, reason, and decision, so you can show before and after at the end. A request for review alone does not authorize applying suggestions. Apply only accepted revisions, with the student's wording wherever they edited a proposal, and leave rejected and undecided passages as they are.

### The editing page

Read `<edit-template>/README.md` before writing the first items. It specifies `items.txt`, the page, the decision batches, and the apply step. The template was written for Hang's dissertation, so adapt its paths as follows. Its scripts run on Python 3.8 or newer.

1. **Create one review folder per session** inside the paper's root folder, for example `<paper root>/waiting_for_review/<name>/`, where `<name>` uses letters, digits, and hyphens (such as `intro-review-20261107`). The folder name is the review's id.
2. **Write `items.txt`.** Under `@review`, give `title: Review: <paper title>` and a one-sentence `description:`. Add `markers: no` unless the paper defines a `\hang` macro and the student wants each applied change tagged. Record the student's request word for word as `@request R1`. For each proposal, write an `@item` with a stable id (such as `INTRO-001`), a `type:` naming the kind of change (`argument`, `signposting`, `paragraph`, `length`, `sentence`, `wording`, `figure`, or `mechanical`), the `file:` relative to the paper root, `request:`, a `note:` that gives the reason in one or two sentences and names the principle (such as "Advisor guide, Introduction" or "Portable guide, Correct without rewording"), and the `--- original` and `--- revised` blocks. Copy the original exactly from the source, enough of it to occur once in the file. Use `--- anchor` with `--- revised` for an insertion, and `--- original` alone for a cut.
3. **Build:**
   ```bash
   python <edit-template>/build_review.py <paper root>/waiting_for_review/<name> --root <paper root>
   ```
   Fix every item it reports as missing or not unique, and build again.
4. **Open `review.html`** in that folder for the student (for example `Start-Process` in PowerShell, `open` on macOS, or `xdg-open` on Linux). The student accepts, rejects, edits the wording, or leaves a note, and clicks **Save batch**, which writes `<name>.decisions.<time>.json` to the folder (or to Downloads in browsers that cannot write to a folder).
5. **Read the decisions** from the batch files in time order, later batches winning. `revised_override` holds the student's own wording. Check that wording against the principle that prompted the proposal (see "Student decisions").
6. **Apply** with a dry run first, show the student what it would change, and run it with `--write` when the student confirms. It changes only accepted items, backs up each file, and records the changes in `change-record.md`.
   ```bash
   python <edit-template>/apply_decisions.py <paper root>/waiting_for_review/<name> --root <paper root>
   python <edit-template>/apply_decisions.py <paper root>/waiting_for_review/<name> --root <paper root> --write
   ```

Add each section's proposals to the same `items.txt` as you reach it and rebuild. Rebuilding keeps every saved decision whose item text did not change. Figure findings that are not caption edits stay in chat with their evidence. To have a second agent look over the proposals, point it at `<edit-template>/second-agent-brief.md` and the review folder; its style sources are in `../writing-style/`. Its options appear as a second choice on a card, so use them occasionally and only when needed; most cards should have one option.

### The review page (mock reviewer report)

When the student or advisor asks how reviewers would read the draft, asks for an overall assessment, or accepts your offer at wrap-up, write a mock review on the review page. It reports on the draft; it does not change it.

1. Read the header comment of `<review-template>/review.html` (its first 116 lines), which specifies `review-data.js`, and the worked example in [review-data-format.md](review-tools/review-data-format.md).
2. Copy `<review-template>/review.html` unchanged into `<paper root>/review/`, and write `<paper root>/review/review-data.js` with the five sections in order: summary, strengths, weaknesses, areas for improvement, and overall recommendation. Give every point one to five evidence objects with the location, what the paper says, and the reason. Build the `machine` from the argument chain the student confirmed in step 2 of the session flow, and mark weak links between the experiments and the contributions they support.
3. Write as a fair reviewer at the target venue: "the authors" as the subject, weaknesses that state one concern each with its location and what would resolve it, and a recommendation that uses the venue's decision options and names what would most change it. Leave out the expertise caveat that ends Hang's own peer reviews. Because the paper is the student's own, a point may explain an observation, give its likely cause, and suggest a fix, which helps the student act on it. Mark such an explanation as your reading, not a finding. (A peer review of someone else's paper asks the authors instead; see "Ask the authors, do not explain for them" in the `review-paper` skill.)
4. Check it, and fix every error. Warnings about Hang's peer-review conventions, such as the expertise caveat and explaining an observation, do not apply to a mock review.
   ```bash
   node review-tools/check_review.js <paper root>/review/review-data.js
   ```
5. Open the page for the student. A weakness the student wants to fix becomes proposals on the editing page.

## Session flow

### 1. Set up (one or two short turns)

1. Get the paper — ideally **both** the compiled PDF and the source (the .tex files or an Overleaf zip, or the .docx). The PDF shows layout, length and figures; the source gives the exact text to quote and revise, without PDF extraction artifacts, and makes it easy to carry the accepted revisions back. If they've only shared one, ask once for the other; if they don't have it, proceed with what you have. If it's a file, extract the text (see "Tools for reading the paper and figures" below), run the structure scan, and, if the paper has figures, run the figure inventory.
2. Read `references/advisor-guide.md` and the starting readings under "Writing tone and wording" above. Check any earlier decisions for the passages under review, including batch files in the paper's existing review folders.
3. **Establish the target length before anything else.** Every section target in the guide is a share of the overall length, so you can't judge whether the Background is "too long" until you know the limit. Find out:
   - the venue and paper type (full paper, short paper, late-breaking report, workshop paper, journal article, thesis chapter),
   - the page or word limit, and whether references (and appendices) count toward it,
   - the format (single- or two-column template).
   Infer what you can from the document first (a PDF's page count and layout, the LaTeX document class, a venue name on the title page), then ask only for what's missing. If the student doesn't know the limit, don't guess and move on — ask them to check the call for papers (you can help find it with web search if they name the venue). Only if it truly can't be determined, agree on an assumption with the student (e.g., "let's assume 8 pages, two-column, references excluded") and say it's an assumption.
   Then scale the guide's section targets to that length (the guide's numbers assume 8–9 pages; for a 4-page paper roughly halve them and expect merged Intro/Background and Discussion/Conclusion) and note where the draft currently stands against the limit (over, under, about right). If the paper is well over the limit, mention that the guide has an editing-for-length process and ask whether they want to address length now or after the content review — content first is usually better, since cuts are easier once each paragraph's point is clear.
4. In the same message or the next, ask how far along the draft is and whether they want to cover the whole paper or focus on particular sections (default: whole paper).
5. Choose where the student decides (see "Bring the text to the student"). With source files, create the review folder for the editing page.
6. Give a two-to-three sentence overview of how the session will go so they know what to expect (argument first, then section by section, you propose the revisions and they accept or reject each one).

### 2. The central argument (do this before any section-level review)

Students most often need help building a coherent chain of logic. Start here because every later proposal depends on it.

1. **Before reviewing any section**, read the whole paper and state its central argument as a short chain: *problem → why it matters → why it's hard / what's missing → what we did → what we found → why that matters.* One sentence per link is plenty, each with the place in the paper that states it. Show the chain to the student, ask whether it is the argument they meant to make, and record their corrections.
2. Then check that chain against the four questions every introduction must answer:
   - What is being done?
   - What is the current state of the art in the field?
   - Why is our thing new?
   - Why is our thing important?
3. Look for weak links: Does each step actually follow from the previous one? Is there a jump (e.g., "the problem matters" → "so we built X" without saying why existing work fails)? Does the claimed result actually support the claimed contribution, without over- or under-stating it? For each weak link you find, propose a revision at the place in the paper where the link is made.
4. Save the chain the student confirmed and refer back to it throughout. When reviewing a section, state which link of the argument the section carries and whether the section matches the confirmed chain. Mismatches between the chain the student confirmed and the paper they wrote are some of the most valuable things to surface.

### 3. Section-by-section review

Go through sections in the paper's order (or the order the student asked for). For each section:

1. **Orient.** Briefly say what the advisor's guide says this section is for and its rough target length (from `references/advisor-guide.md`, scaled to the paper's target length from setup), and report the section's actual length from the scan. State which link of the argument this section carries.
2. **Signposting.** Every section should tell the reader early on what it covers and how it's organized. Check whether the section's opening paragraph tells the reader what's coming. If it doesn't, note what a reader would expect the section to contain after reading the first paragraph, and propose a revision of that paragraph that matches what follows.
3. **Paragraph points.** For each key paragraph, state its point in one sentence (usually a claim, sometimes a topic or key idea). Then check:
   - Where in the paragraph is that point stated? (Ideally early — often the first sentence.)
   - Does every sentence in the paragraph serve that point?
   - How does this paragraph's point connect to the one before it and the one after it?
   If no point can be named, that's the finding. State the point the paragraph seems to be trying to make, and propose a revision that states it early, or a split, a cut, or a move.
   You don't need to visit every paragraph. Prioritize: the first paragraph of each section, paragraphs the scan flagged, and paragraphs that carry links of the central argument. Ask the student if there are any they're unsure about.
4. **Length flags.** Use the scan to find:
   - very long sentences (find where a reader would have to backtrack, and propose a split there),
   - very long paragraphs (check whether it makes more than one point, and propose a split where the second point starts),
   - very short paragraphs of one or two sentences (check whether it has a point of its own, and propose merging it with a neighbor when it has none).
   Give the numbers with each proposal. A long sentence or paragraph that makes one point needs no proposal.
5. **Section-specific questions.** Answer the questions for this section from `references/advisor-guide.md` (e.g., for the Introduction: is the first sentence throat-clearing? does paragraph 3 pair each contribution with its evidence? For Methods: could someone replicate the study from this?), and propose a revision where an answer shows a problem. Report the two or three most relevant findings rather than one for every question.
6. **Key sentences.** For a handful of important sentences (the hook, each contribution claim, topic sentences, the final sentence of the conclusion), check one sentence at a time: who or what is the subject of the sentence, what is the one thing a reviewer should take away from it, and whether the claim is stronger or weaker than the evidence. Propose a revision where a check shows a problem.
7. **Figures in this section.** When you reach a figure (or table), review it using "Reviewing figures" below, one figure at a time. If the student would rather decide on all figures in one pass at the end, do that instead.
8. **Student decisions.** The student accepts or rejects each proposal (on the editing page, in the review doc, or in chat), and can edit the wording of a proposal before accepting it. When they edit a revision, check the edit against the same principle that prompted the proposal. Accept their choice even if you'd have chosen differently, unless an edit introduces a new problem. Then say what the problem is and propose a fix for it.
9. **Close the section.** If the student deferred anything ("let's come back to that"), add it to the to-do list and move on. Don't ask them to summarize what they accepted, since the decisions are already recorded and the summary is busywork. Do keep track yourself of net length added or cut, since the paper has a fixed limit.

Pace the decisions. A full paper can produce many proposals, so show them to the student one section at a time and check in periodically ("The Intro and Background proposals are decided. Do you want to keep going, or stop here and pick up later?").

### Reviewing figures

Every figure in the paper should support some key idea or result — usually one of the links in the student's argument chain. Readers (and reviewers) often look at the figures before reading the text, so a figure has to work on its own. Review each figure in this order, answer each question from a reader's point of view, and propose a change where an answer shows a problem:

1. **First glance.** "What does a reader parse from this figure at first glance, in the first two or three seconds?" Answer as a reader who sees only the figure image, not from what you know the figure *means* (e.g., "Looking at it cold, my eye went to the red bar on the right and I read it as 'the baseline wins'"). Compare that read with what the paper needs the figure to show. That's reader information, and it's often the most useful thing you can give.
2. **The details.** "What does a reader get from the details — the axes, legend, labels, error bars, sub-panels, caption?" Is anything there that a reader needs but can't find, or that's there but nobody needs?
3. **Alignment with the story.** "How do the first-glance message and the details line up with the overall argument of the paper? Which link of your argument chain, or which key result, does this figure support?" If no link or result can be named, that's the finding. Propose cutting the figure, or say what it would need to show to support a link of the argument.
4. **Readability.** Is all text (axis labels, tick labels, legends, annotations) readable at the size it appears in the paper — not just on their monitor? A good test: is the smallest figure text at least close to the size of the caption text? For graphs: are axes cut off in odd places, are error bars shown, are significant comparisons marked?
5. **Color.** Do the colors still separate for color-blind readers and on a black-and-white printout? Don't just assert an answer. Generate the simulation panel (see "Tools for reading the paper and figures"), check each simulated version, and show the panel to the student with the finding, so they can see what it is based on. Check whether anything relies on color alone (e.g., red vs. green lines), and propose a marker shape, line style, or direct label where it does.
6. **Caption and references.** Does the caption tell the reader what to take away, not just what is plotted? Is the figure referred to in the text, near where it's discussed? (The inventory reports text references; a figure referenced zero times is worth asking about.)

Also check the set of figures as a whole: Is there a figure on page 1 or 2 that summarizes the approach or core interaction? If there's a human-subjects study, is the robot or interaction space pictured? Roughly one float per page, without pages that are only floats?

Some figures are photos or diagrams rather than plots; adapt — for a system diagram, "first glance" might be "what's the flow, and where does the reader's eye start?"

### 4. Wrap-up

1. Return to the argument chain from step 2. Check whether the Introduction and Discussion, with the accepted revisions, now match it, and ask the student whether they'd state it any differently after the review. (The guide notes the Introduction usually needs revisiting after writing the Discussion and Conclusion.)
2. Point them to their to-do list of deferred items, and the net length change if the paper is near its limit.
3. Get the accepted revisions back into the source: run the editing page's apply step, or, when the student decided in chat or a doc, offer to assemble an updated copy of the source file with the accepted revisions substituted in verbatim (with the student's wording wherever they edited a proposal). A rejected proposal leaves the original text as it was.
4. Offer a mock reviewer report on the review page, if the student has not had one.
5. Optionally give the student and the advisor a count of the decisions in each section (accepted, rejected, and edited), and the kinds of proposals the student rejected most often. This is useful for the advisor, since the rejected and edited proposals show where the student disagreed with the review. The editing page's `change-record.md` already lists the applied changes by request.

## Mechanical / style patterns

The scan also flags the advisor's pet peeves (e.g., "utilize", "in order to", "works" meaning papers, numeric citations used as nouns, "would" when describing what happened in a study, "simple"/"minor" about one's own work, first person as the subject in an algorithm section, passive voice in the introduction). Treat these as low priority. Propose them as one batch near the end of a section, after the argument-level proposals, labeled as places that match patterns the advisor asks students to watch for (on the editing page, `type: mechanical`). The reasons behind each are in the guide, so give the reason with each proposal, not just the rule. Don't let mechanical issues crowd out the bigger questions about logic, points, and signposting.

## Tools for reading the paper and figures

Resolve the helper paths relative to this skill's folder, not the current paper's folder. Keep generated scans, rendered pages, and review decisions with the paper or in a task output directory, outside the installed skill.

The helpers in `scripts/` require Python 3.10 or newer; select an available interpreter (the examples use `python3`, and on Windows `py -3.12` or `py -3.10` selects one through the Python launcher when the default `python` is older). Plain text, Markdown, and LaTeX scanning and LaTeX figure inventory use the standard library. PDF operations need Poppler's `pdftotext`, `pdfinfo`, and `pdftoppm` on PATH. In Git Bash on Windows, the `pdftotext` first on PATH is Git's Xpdf, which the scan and the figure inventory cannot use, so put a Poppler build first, such as the one in MiKTeX or in conda's `poppler` package. Word extraction needs `python-docx` or `pandoc`. Color-vision panels need Pillow and NumPy. Use available equivalent tools when a dependency is missing, state any limit on what you inspected, and continue the parts of the review that do not depend on it.

- PDF: `pdftotext -layout <file> out.txt` (or without `-layout` if columns get interleaved — check the output). Two-column PDFs can scramble paragraph order; if the text looks wrong, ask the student for the .tex or a pasted section instead.
- LaTeX: read the .tex directly; the scan understands `\section`, `\subsection`, and `\paragraph`, and strips common commands and comments.
- Word: use python-docx or `pandoc`.
- Pasted text: work from it directly.

Run the structure scan to get section lengths, paragraph/sentence statistics, and flags:

```bash
python3 <skill folder>/scripts/structure_scan.py <paper file or extracted .txt> [--json]
```

For figures, run the inventory. For a PDF it lists every figure and table with its page, caption and how often the text refers to it, and renders each page holding a figure to a PNG you can view; for LaTeX it lists captions, labels, image files and `\ref` counts:

```bash
python3 <skill folder>/scripts/figures.py inventory <paper.pdf|paper.tex> --out figure_pages
```

To let the student check color accessibility themselves, make a comparison panel (original, deuteranopia, protanopia, tritanopia, grayscale) from a figure image, rendered page, or single-figure PDF, then share it with the student (copy it to the outputs folder and present it, or describe what changes if you can't share files):

```bash
python3 <skill folder>/scripts/figures.py simulate <figure.png|figure.pdf> --out colorvision.png
```

If the paper is only pasted text, ask the student for the figure files or a PDF. If you're working from a rendered page, you can crop to the figure with PIL before simulating so the panel is easier to read.

The scan is a heuristic aid for *you* to decide where to direct attention. Its counts are approximate (especially from PDFs, where figure captions, footnotes, and headers leak in), so sanity-check anything you cite, and when you discuss a paragraph, show it rather than pointing to it. Don't dump the scan output on the student.

## Adapting

- The guide is written for HRI conference papers. For other fields or formats (journals, workshop papers, theses), keep the core principles (argument chain, the four intro questions, paragraph points, signposting, length) and adjust section expectations; ask the student what structure their venue expects. For workshop papers and abstracts, Introduction+Background and Discussion+Conclusion are often merged.
- If the paper is very early (outline or partial draft), spend most of the time on the argument chain and the intended point of each planned paragraph.
- If the student is short on time before a deadline, ask what matters most to them and prioritize the Introduction (the guide says it's the section to edit most carefully if you only have time for one), then the contribution claims.
