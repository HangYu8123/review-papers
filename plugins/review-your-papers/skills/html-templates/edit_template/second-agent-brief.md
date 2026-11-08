# Brief for the second agent

Another agent built a review in `waiting_for_review/<name>/`. Hang will go through it on the review page. Your job is to read what was generated and, where you would do something differently, add your option to that entry. Hang then sees the two options on one card and chooses.

Point a fresh agent at this file and name the review, for example: "Follow `waiting_for_review/_template/second-agent-brief.md` for `waiting_for_review/reuth-suggestions-review`."

## Steps

1. **Read `<name>/suggestions.md`.** The requests are at the top. Each entry gives the location, why the change is proposed, the original, the proposed text and a Version.
2. **Check each entry against its source.** Open the `.tex` file at the given line and read the passage around it. Ask whether the edit answers the request it names, whether it is true to the chapter, and whether it fits Hang's writing. The style sources are `writing_style_ref/hangs-writing-style-reference.md` and `committee_style_ref/`.
3. **Disagree only where you would choose differently and can say why.** Nothing has to be found. Disagreeing with no entries is a fine result, and it is recorded as such.
4. **Write `<name>/disagreements.txt`** in the format below.
5. **Build:** `python waiting_for_review/_template/build_review.py waiting_for_review/<name>`. Fix what it reports.
6. **Test your options on a scratch copy** of the dissertation, not on the real one. Copy `chapters`, `figures`, `main.tex`, `references.bib`, the `.cls` and the review folder to `<scratch>/waiting_for_review/<name>`. Then run `python waiting_for_review/_template/apply_decisions.py <scratch>/waiting_for_review/<name> --accept-all --prefer-second --write`, run it again to confirm nothing changes, and compile there.
7. **Report back:** how many entries you looked at, which ones you disagreed with and why, and what you could not check.

## The file

```
@reviewer
by: Claude Sonnet 5.5
date: 2026-11-02
covers: all

@disagree C3-001
against: 24917304d123
note: Why option A falls short and what this option does about it. Shown on the card.
--- revised
The other wording, as raw LaTeX, in place of the same passage.

@disagree C3-002
against: 22cefb1f9904
action: keep
note: Why the passage should stay as it is.

@disagree C3-003
against: d2bf0f67c225
action: remove
note: Why the passage should go rather than be reworded.
```

| Line | Meaning |
| --- | --- |
| `by:` | Who looked. It is shown on the page and kept in the change record. |
| `covers:` | `all`, or the ids of the entries you looked at. This is how Hang knows that silence on an entry means you read it. Say only what you did. |
| `@disagree ID` | The entry you disagree with. Each entry takes one disagreement. |
| `against:` | The Version line of that entry in `suggestions.md`. If the entry changes later, the build and the page flag your option as out of date. |
| `note:` | Your reason, required. Use a `--- note` block if it runs over several lines. |
| `--- revised` | Your wording. No `action:` line goes with it. |
| `action: keep` | Your option is to leave the passage as it is. |
| `action: remove` | Your option is to remove the passage. This fits only an entry that rewords a passage. |

## Rules

- Do not edit `items.txt`, `items.json`, the `.tex` files or the batch files. The first agent's wording stays as written, because it is option A.
- Your wording replaces the same passage as option A, and takes the same `\hang` tags. A change that needs a wider passage belongs in a new item, so name it in your report instead.
- Keep every citation, label and number unless you have checked the change against the chapter.
- Check what Hang has already decided before you offer something. Saved decisions, including Hang's own wording under `revised_override`, are in the batch files of the folders under `waiting_for_review/legacy/`. Do not offer again what Hang declined without saying so in your note.
- `action: remove` on a sentence that fills a whole line in the middle of a paragraph leaves an empty line, and TeX then starts a new paragraph there. Look at the line in the `.tex` file first. If this applies, say so in your note, so the paragraph can be rejoined after applying.
- Write `note:` for Hang, in plain words. Say what is wrong with option A and what yours does about it, in one or two sentences.
