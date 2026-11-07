# Hang's writing style reference

Start with [Hang's writing style reference](hangs-writing-style-reference.md). It holds 72 patterns across vocabulary, wording preference, writing style, sentence style, sentence structure, storytelling style, and talk and film text. 59 of them combine the two writing style libraries built from the papers, and 13 come from evidence from Hang. The opening quick reference is useful before drafting. The detailed entries provide forms, meaning boundaries, weighted evidence from Hang, and paper examples.

| File | Use |
| --- | --- |
| [hangs-writing-style-reference.md](hangs-writing-style-reference.md) | The complete writing reference and quick reference |
| [preference-signals.md](preference-signals.md) | Every instruction, hand edit, decline, edit, and note from Hang, with its weight, and the patterns ranked by weight |
| [review-decisions.md](review-decisions.md) | The index of the 16 imported reviews, with the record of each in `reviews/` |
| [source-evidence.md](source-evidence.md) | All retained paper excerpts, grouped by merged pattern |
| [source-map.md](source-map.md) | How all 96 original entries were combined, how differences were resolved, and what the evidence from Hang changed |
| [library.json](library.json) | The merged guidance, evidence, and weights in a structured format |
| [validation.md](validation.md) | Coverage, quotation, evidence wording, link, and preservation checks |
| [tech-vocabulary.md](tech-vocabulary.md) | Technical terms from the papers and the three reference dissertations, each with an estimate of how familiar it is to Hang, an example, and its source |
| [word-list.md](word-list.md) | Every word family the papers use, grouped by the same familiarity estimate, and the words only the reference dissertations use |
| [tech-vocabulary.json](tech-vocabulary.json) | The vocabulary and the full word list in a structured format, read by the checker |
| [vocabulary-check-chapters.md](vocabulary-check-chapters.md) | The chapters checked against the vocabulary, as an example of the checker's report |
| [sources](sources/) | Preserved original entries, library snapshots, review decisions, Hang's instructions and hand edits, general English word frequencies, and the text of the reference dissertations |

Use the guide for new dissertation prose while preserving the current passage's facts and definitions. Paper quotations illustrate wording and do not supply facts for a different study. Evidence from Hang takes priority over the paper examples, heavier evidence over lighter, and the impersonal dissertation voice takes priority over first-person source examples in the chapters.

Prepared on October 12, 2026 from the two libraries that were then in `waiting_for_review`. Revised the same day from the decisions of the Chapter 8 writing review and from Hang's request to use fewer colons and semicolons. The technical vocabulary was added on October 17, 2026 from a scan of the papers in `reference_papers/` (CHARM, Demonstration Sidetracks, PHIRL, Progress, the prospectus, and STEADY), and expanded the same day with the Short, Vázquez, and Bobu dissertations in `dessertation_reference/`, which are counted separately and never raise a familiarity tier. Revised on October 19, 2026 from 679 decisions in 16 reviews of the dissertation, the talk, and the film (496 of them by Hang), from 19 instructions in Hang's messages, and from 18 of Hang's hand edits, with more weight on declines, notes, and edits.

To rebuild after editing the guidance in `tools/authored_entries.py`, run `python writing_style_ref/tools/build_reference.py` from the dissertation folder. Then run `python writing_style_ref/tools/validate_reference.py`.

To bring in a later review, run `python writing_style_ref/tools/import_review.py <review folder>` before the review folder is removed. The folder can be in `waiting_for_review/` or in the talk's `wait_to_review/` (`../dissertation_presentation/wait_to_review/<folder>`). Add `--prefix X-` when the review's item ids repeat those of an imported review. Then cite its decisions in `tools/authored_entries.py`, or list a strong decision in `UNCITED` with its reason, and rebuild. The build stops when a decline, edit, or note is neither cited nor explained. Hang's instructions and hand edits are snapshots in `sources/hang-instructions.json` and `sources/hand-edits.json`, made by `tools/collect_hang_evidence.py`. Add a new instruction or hand edit there and rerun it before citing it.

To rebuild the technical vocabulary after adding a paper to `tools/vocab_corpus.py` or editing the term list in `tools/vocab_authored.py`, run `python writing_style_ref/tools/build_vocabulary.py`, then `build_reference.py` and `validate_reference.py`. If the reference dissertation PDFs change, run `tools/extract_reference_text.py` first. To check a draft, run `python writing_style_ref/tools/check_vocabulary.py chapters/<file>.tex`, or pass `--out <file>.md` to save the report. The example report is made with `python writing_style_ref/tools/check_vocabulary.py "chapters/*.tex" --out writing_style_ref/vocabulary-check-chapters.md`.
