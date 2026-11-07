# Guided paper review

Both versions use the advisor guide for the review process and the three bundled style collections for tone and wording. Each folder is a complete, portable skill with its own references and Python helpers.

| Version | Skill folder | Archive | Invocation after installation |
| --- | --- | --- | --- |
| Codex | [codex/paper-review](codex/paper-review/) | [paper-review.skill](codex/paper-review.skill) or [ZIP](codex/paper-review.zip) | `$paper-review` |
| Claude Code | [claude-code/paper-review](claude-code/paper-review/) | [ZIP](claude-code/paper-review.zip) | `/paper-review path/to/paper.tex` |

For Codex, copy `codex/paper-review` into your Codex skills directory (`$CODEX_HOME/skills`, or `~/.codex/skills` by default).

For Claude Code, copy `claude-code/paper-review` into `.claude/skills/` in the paper's project, or into `~/.claude/skills/` for use across projects. The result should be `.claude/skills/paper-review/SKILL.md`. Claude Code supports automatic discovery and the `/paper-review` command. See the [official Claude Code skills documentation](https://code.claude.com/docs/en/skills).

These copies have not been installed into either application's global skills directory. Review outputs and author decisions belong with the paper, outside the skill folder.

Copy the entire `paper-review` folder when installing either version so its references and helpers remain available. Each archive contains the same files as the corresponding unpacked folder.
