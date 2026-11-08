---
name: writing-style
description: Hang Yu's full writing style reference (72 patterns with weighted evidence from Hang's instructions, hand edits, and 16 review records, plus a 929-term technical vocabulary and a vocabulary checker) and the committee writing style reference (patterns, quotations, and measures from the Short, Vázquez, and Bobu dissertations), about 9 MB in all. Use only when the writing-style-portable guide is not enough, such as a disputed wording, a sentence that may have been reviewed before, the evidence or strength behind a preference, committee-facing or thesis-chapter conventions, checking a draft's vocabulary, or importing a finished review's decisions into the reference.
---

# Full writing style references

Two large source libraries behind the [portable writing style guide](../writing-style-portable/SKILL.md). The portable guide covers ordinary writing and reviews; open these only when it is not enough. Search them by heading or pattern name and read only the entries needed. Do not load a whole library, evidence file, or source text.

| Folder | What it is | Start with |
| --- | --- | --- |
| [writing_style_ref](writing_style_ref/README.md) | Hang's writing style reference: 72 patterns, every instruction, hand edit, and review decision from Hang with its weight, the records of 16 reviews, the technical vocabulary, and the build tools (about 7 MB) | [hangs-writing-style-reference.md](writing_style_ref/hangs-writing-style-reference.md) |
| [committee_style_ref](committee_style_ref/README.md) | The committee writing style reference: 63 patterns from three dissertations Hang named, with 282 quotations and per-writer measures (about 2 MB) | [committee-writing-style-reference.md](committee_style_ref/committee-writing-style-reference.md) |

## Which file answers which question

| Question | Read |
| --- | --- |
| A preference needs explanation or appears to conflict with the portable guide | The relevant entry in [Hang's full reference](writing_style_ref/hangs-writing-style-reference.md), then its linked evidence |
| A sentence was reviewed before, or the author disputes a wording | [Review index](writing_style_ref/review-decisions.md) and the relevant record in `writing_style_ref/reviews/` |
| How strong a preference is, or where it came from | [Preference signals](writing_style_ref/preference-signals.md) and the [source map](writing_style_ref/source-map.md) |
| Technical word choice, with examples and sources | [Technical vocabulary](writing_style_ref/tech-vocabulary.md) and the [word list](writing_style_ref/word-list.md) |
| Committee-facing clarity, study reporting, or a thesis chapter | The relevant entry in [the committee reference](committee_style_ref/committee-writing-style-reference.md) |
| Evidence of a writing pattern | [Hang's paper excerpts](writing_style_ref/source-evidence.md) or [committee excerpts](committee_style_ref/source-evidence.md); [writer profiles](committee_style_ref/writer-profiles.md) for approximate measures |

Hang's current instructions and the facts of the passage come first. Among style sources, direct evidence of Hang's choices takes priority over the portable summary, then committee examples. Do not turn a past choice about one passage into a universal substitution. The committee quotations show how those writers wrote, with their first person and punctuation; they are not text to copy, and dissertation structure does not set the style of a conference paper or a peer review.

## Tools

The two READMEs give the full build steps. The commands below run from this skill's folder.

- Check a draft's vocabulary: `python writing_style_ref/tools/check_vocabulary.py <file>.tex`, with `--out <report>.md` to save the report.
- Bring a finished review into the reference: `python writing_style_ref/tools/import_review.py <review folder>`, then cite its decisions in `writing_style_ref/tools/authored_entries.py` and rebuild with `build_reference.py` and `validate_reference.py`. This changes the reference, so ask before running it. An installed copy is replaced on the next install or plugin update, so run it on the repository's copy (`plugins/review-your-papers/skills/writing-style/`) and reinstall.

The READMEs, validation reports, and build scripts refer to Hang's dissertation folder, the original PDFs, and paper sources that are not bundled here. Those paths are provenance, not required inputs. Do not claim to have opened a PDF that is absent, and do not run the rebuild or extraction scripts as part of an ordinary review.
