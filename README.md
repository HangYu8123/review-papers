# review-your-papers

A plugin for Claude Code and Codex with two paper-review skills. This repository is also the marketplace that both apps install it from, and it holds everything the skills need.

| Skill | What it does |
| --- | --- |
| [advisor-review-paper](plugins/review-your-papers/skills/advisor-review-paper/SKILL.md) | Reviews a student's draft on behalf of the advisor, using Elaine Schaertl Short's advisor guide. Proposes small revisions with reasons on the editing page, where the author accepts, rejects, or edits each one before it is applied to the source. Can also write a mock reviewer report. |
| [review-paper](plugins/review-your-papers/skills/review-paper/SKILL.md) | Drafts a peer review of someone else's paper in Hang's reviewing style, on the review page with evidence under each point. Uses the editing page when asked to edit a manuscript's text. |

## Install as a plugin

Claude Code:

```
claude plugin marketplace add HangYu8123/review-your-papers
claude plugin install review-your-papers@review-your-papers
```

Codex:

```
codex plugin marketplace add HangYu8123/review-your-papers
codex plugin add review-your-papers@review-your-papers
```

The skills are then `review-your-papers:advisor-review-paper` and `review-your-papers:review-paper`, such as `/review-your-papers:review-paper` in Claude Code. Restart the app if it was running. To update, run `claude plugin marketplace update` or `codex plugin marketplace upgrade`.

## Install the skills on their own

`install.py` copies the skills into a skills folder without the plugin system, so they are invoked as `/advisor-review-paper` and `/review-paper` (`$advisor-review-paper` and `$review-paper` in Codex). Use either this or the plugin, not both. Run it with Python 3.8 or newer:

```
python install.py                 # Claude Code (~/.claude/skills) and Codex ($CODEX_HOME/skills)
python install.py --app claude    # or --app codex
```

Other options are `--dest <skills folder>`, `--skill review-paper`, `--dry-run`, `--uninstall`, and `--package dist`, which writes a zip that unpacks into a skills folder. The script replaces only folders it installed.

## Layout

```
.claude-plugin/marketplace.json        Claude Code marketplace
.agents/plugins/marketplace.json       Codex marketplace
plugins/review-your-papers/
  .claude-plugin/plugin.json           Claude Code plugin manifest
  .codex-plugin/plugin.json            Codex plugin manifest
  skills/
    advisor-review-paper/              skill, with its own style_guide_portable/
    review-paper/                      skill, with its own style_guide_portable/ and references/guideline.md
    paper-review-shared/               used by both skills; not a skill
      writing_style_ref/               Hang's full style reference (about 7 MB)
      committee_style_ref/             committee style reference (about 2 MB)
      templates/edit_template/         the editing template
      templates/review_template/       the review template
      review-tools/                    review-data.js checker and format example
install.py                             standalone installer
```

Each skill carries the portable writing style guide (about 120 KB), which is its style source for ordinary reviews. The two copies must stay identical; `install.py` warns when they differ. The full references are kept once in `paper-review-shared/`, and the skills open them only when the portable guide is not enough, such as for a disputed wording or a sentence that was reviewed before.

`review-paper` reads Hang's past reviews from `previous_reviews/previous_reviews` in the folder that holds the paper folder, when that file exists. They are not in this repository because peer reviews are confidential.

## Requirements

The paper helpers in `advisor-review-paper/scripts/` need Python 3.10 or newer. The editing template's scripts run on Python 3.8 or newer, and the review checker needs Node.js. Review folders, decisions, and outputs belong with each paper, not in the installed plugin.
