#!/usr/bin/env python3
"""Install the review skills on their own, without the plugin system.

    python install.py                          both apps
    python install.py --app claude             Claude Code only (~/.claude/skills)
    python install.py --app codex              Codex only ($CODEX_HOME/skills, by default ~/.codex/skills)
    python install.py --dest <skills folder>   any skills folder, such as <project>/.claude/skills
    python install.py --skill review-paper     one skill (the shared folder is always installed)
    python install.py --uninstall              remove what this script installed
    python install.py --dry-run                show what would happen
    python install.py --package dist           write dist/review-your-papers-skills.zip to unpack into a skills folder

To install the skills as a plugin from the marketplace instead, see README.md. Use one way or
the other, since both together list each skill twice.

Each skills folder receives advisor-review-paper/, review-paper/, and paper-review-shared/
side by side, since both skills read ../paper-review-shared/. An installed folder is replaced
only if this script installed it, which it records in a marker file. Runs on Python 3.8 or newer.
"""
import argparse
import datetime
import json
import os
import shutil
import stat
import subprocess
import sys
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parent
SOURCE = REPO / "plugins" / "review-your-papers" / "skills"
SKILLS = ["advisor-review-paper", "review-paper"]
SHARED = "paper-review-shared"
MARKER = ".installed-by-review-your-papers.json"
IGNORE = shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store", MARKER)
IGNORED_NAMES = {"__pycache__", ".DS_Store", MARKER}


def claude_skills_dir():
    base = os.environ.get("CLAUDE_CONFIG_DIR")
    return (Path(base) if base else Path.home() / ".claude") / "skills"


def codex_skills_dir():
    base = os.environ.get("CODEX_HOME")
    return (Path(base) if base else Path.home() / ".codex") / "skills"


def is_link(path):
    """True for a symbolic link, or a junction or other reparse point on Windows."""
    if os.path.islink(str(path)):
        return True
    if os.name == "nt":
        try:
            st = os.lstat(str(path))
        except OSError:
            return False
        return bool(getattr(st, "st_file_attributes", 0) & stat.FILE_ATTRIBUTE_REPARSE_POINT)
    return False


def git_commit():
    try:
        out = subprocess.run(["git", "-C", str(REPO), "rev-parse", "--short", "HEAD"],
                             stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, check=True)
        return out.stdout.decode().strip()
    except (OSError, subprocess.CalledProcessError):
        return ""


def check_sources(names):
    for name in names:
        src = SOURCE / name
        if not src.is_dir():
            raise SystemExit("Missing source folder: %s" % src)
        if name in SKILLS and not (src / "SKILL.md").is_file():
            raise SystemExit("Missing %s" % (src / "SKILL.md"))


def files_of(folder):
    return {p.relative_to(folder).as_posix(): p.read_bytes() for p in folder.rglob("*") if p.is_file()}


def check_portable_guides():
    """Each skill carries its own copy of the portable guide. Warn if the copies differ."""
    copies = [SOURCE / s / "style_guide_portable" for s in SKILLS]
    first = files_of(copies[0])
    for other in copies[1:]:
        if files_of(other) != first:
            print("Warning: %s differs from %s. Keep the copies of the portable guide the same."
                  % (other.relative_to(REPO), copies[0].relative_to(REPO)))


def owned(dest):
    return (dest / MARKER).is_file()


def refuse_reason(dest, force):
    if is_link(dest):
        return "it is a link or junction; remove it yourself first"
    if dest.exists() and not dest.is_dir():
        return "it is a file"
    if dest.exists() and not owned(dest) and not force:
        return "it was not installed by this script (use --force to replace it)"
    return ""


def install_one(src, dest, dry_run, force, commit):
    reason = refuse_reason(dest, force)
    if reason:
        print("  skipped %s: %s" % (dest, reason))
        return False
    action = "replace" if dest.exists() else "install"
    print("  %s %s" % (action, dest))
    if dry_run:
        return True
    tmp = dest.parent / (".%s.tmp-%d" % (dest.name, os.getpid()))
    if tmp.exists():
        shutil.rmtree(str(tmp))
    shutil.copytree(str(src), str(tmp), ignore=IGNORE)
    marker = {
        "source": str(REPO),
        "commit": commit,
        "installed_at": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
    }
    (tmp / MARKER).write_text(json.dumps(marker, indent=1) + "\n", encoding="utf-8")
    if dest.exists():
        shutil.rmtree(str(dest))
    os.rename(str(tmp), str(dest))
    return True


def uninstall_one(dest, dry_run):
    if not dest.exists() and not is_link(dest):
        return
    if is_link(dest) or not owned(dest):
        print("  left %s: it was not installed by this script" % dest)
        return
    print("  remove %s" % dest)
    if not dry_run:
        shutil.rmtree(str(dest))


def package(out_dir, names):
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "review-your-papers-skills.zip"
    count = 0
    with zipfile.ZipFile(str(out), "w", zipfile.ZIP_DEFLATED) as zf:
        for name in names:
            for root, dirs, files in os.walk(str(SOURCE / name)):
                dirs[:] = sorted(d for d in dirs if d not in IGNORED_NAMES)
                for f in sorted(files):
                    if f in IGNORED_NAMES or f.endswith(".pyc"):
                        continue
                    path = Path(root) / f
                    zf.write(str(path), path.relative_to(SOURCE).as_posix())
                    count += 1
    print("Wrote %s (%d files, %.1f MB)" % (out, count, out.stat().st_size / 1e6))
    print("Unpack it into a skills folder so the three folders sit side by side.")


def main():
    ap = argparse.ArgumentParser(description="Install the review skills for Claude Code and Codex.")
    ap.add_argument("--app", choices=["claude", "codex", "both"], default="both",
                    help="which app's personal skills folder to install into (default: both)")
    ap.add_argument("--dest", action="append", default=[],
                    help="install into this skills folder instead (repeatable)")
    ap.add_argument("--skill", action="append", choices=SKILLS, default=[],
                    help="install only this skill (repeatable; default: both)")
    ap.add_argument("--uninstall", action="store_true", help="remove the installed folders")
    ap.add_argument("--force", action="store_true",
                    help="replace a folder of the same name that this script did not install")
    ap.add_argument("--dry-run", action="store_true", help="show what would happen without changing anything")
    ap.add_argument("--package", metavar="DIR", help="write a zip of the skills and the shared folder to DIR")
    args = ap.parse_args()

    names = (args.skill or SKILLS) + [SHARED]
    check_sources(names)
    check_portable_guides()

    if args.package:
        package(Path(args.package).resolve(), names)
        return 0

    if args.dest:
        targets = [Path(d).expanduser().resolve() for d in args.dest]
    else:
        targets = []
        if args.app in ("claude", "both"):
            targets.append(claude_skills_dir())
        if args.app in ("codex", "both"):
            targets.append(codex_skills_dir())

    commit = git_commit()
    failed = False
    for skills_dir in targets:
        print("%s%s:" % (skills_dir, " (dry run)" if args.dry_run else ""))
        if args.uninstall:
            for name in names:
                uninstall_one(skills_dir / name, args.dry_run)
            continue
        if not args.dry_run:
            skills_dir.mkdir(parents=True, exist_ok=True)
        for name in names:
            if not install_one(SOURCE / name, skills_dir / name, args.dry_run, args.force, commit):
                failed = True

    if not args.uninstall and not failed:
        skills = [n for n in names if n in SKILLS]
        print("")
        print("Installed as standalone skills.")
        print("Claude Code: %s" % ", ".join("/" + n for n in skills))
        print("Codex:       %s" % ", ".join("$" + n for n in skills))
        print("Restart the app if it is running, so it finds the new skills.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
