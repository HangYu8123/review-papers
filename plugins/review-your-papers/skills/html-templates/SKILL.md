---
name: html-templates
description: Two HTML page templates for accept-or-reject review workflows. The editing template turns a list of proposed edits to LaTeX source files into a page where the author accepts, rejects, or rewords each one, then applies the accepted edits with a dry run first (Python 3.8+). The review template shows a peer-review report (summary, strengths, weaknesses, areas for improvement, recommendation, and an argument map) with evidence under each point and accept, edit, and reject buttons. Use when proposing edits to a document for the author to approve, or when building a review page from a review-data.js.
---

# HTML templates

The `advisor-review-paper` and `review-paper` skills use these two templates. They were moved here from Hang's dissertation and review folders, and these copies are the ones the skills use.

| Template | Use |
| --- | --- |
| [edit_template](edit_template/README.md) | Proposed edits to a source file. The author accepts, rejects, or rewords each one on a page, and `apply_decisions.py` writes the accepted ones into the source. |
| [review_template](review_template/) | A review report (summary, strengths, weaknesses, areas for improvement, recommendation, and a map of the paper's argument) with evidence under each point. The header comment of `review.html` (its first 116 lines) specifies `review-data.js`. |

## Editing template

Read [edit_template/README.md](edit_template/README.md) first. It specifies `items.txt`, the page, the decision batches, and the apply step, and `edit_template/example/` is a small review to try it on.

The template was written for Hang's dissertation, so its README describes `waiting_for_review/` in the dissertation folder. For any other document:

1. Put the review folder inside the document's root folder, such as `<root>/waiting_for_review/<name>/`.
2. Add `markers: no` under `@review` in `items.txt` unless the document defines the `\hang` macro.
3. Pass `--root <root>` to both scripts:
   ```
   python <this skill>/edit_template/build_review.py <root>/waiting_for_review/<name> --root <root>
   python <this skill>/edit_template/apply_decisions.py <root>/waiting_for_review/<name> --root <root>           # dry run
   python <this skill>/edit_template/apply_decisions.py <root>/waiting_for_review/<name> --root <root> --write   # edits the source
   ```

Apply only accepted items, and only after the author confirms the dry run. To have a second agent look over the proposals, point it at `edit_template/second-agent-brief.md` and the review folder; the style sources it names are in the `writing-style` skill. Its disagreements show as two options on a card (Accept A, Accept B, Reject both). Use them occasionally, and only when needed: each one asks the author to choose instead of giving a recommendation, so most cards should have one option.

## Review template

Copy `review_template/review.html` unchanged into the output folder, next to a `review-data.js` written to the specification in its header comment. Copy it fresh each time, since the template is the newest version of the page. The review skills each carry `review-tools/check_review.js`, which checks a `review-data.js`, and `review-tools/review-data-format.md`, a worked example of that file.

The page's Save decisions button writes `<review_id>.decisions.<timestamp>.json` into the page's own folder, next to `review-data.js`, in browsers that can write to a folder (Chrome and Edge). The first save opens a dialog with the folder's path to paste into the folder picker, and the page refuses a folder that does not hold this review's `review-data.js`. The choice is remembered for that page, so later saves write directly, and after a browser restart the browser may ask once for permission again. In other browsers, or with Download instead, the file goes to Downloads.

Keep review folders, decisions, and outputs with each document, never in this skill. An installed copy is replaced on the next install or plugin update, so make lasting changes to a template in the repository.
