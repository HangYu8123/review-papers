#!/usr/bin/env python3
"""Apply the decisions saved by a review page to the dissertation.

    python waiting_for_review/_template/apply_decisions.py waiting_for_review/<name>
    python waiting_for_review/_template/apply_decisions.py waiting_for_review/<name> --write

The first form is a dry run: it lists what would change. --write edits the files.

Decisions are the batch files the page saves next to itself, one per batch:
    <name>/<name>.decisions.<YYYYMMDD-HHMMSS>.json
Every batch is read in time order and the latest decision for an item wins, so
this can be run after each batch: what is already in place is recognised and left
alone. A batch that the browser put in Downloads is found there and moved in.

  accepted   the passage becomes the revised text, inside \\hang{<type> start} ... \\hang{<type> end}
             (on an entry with two options, the option that was chosen)
  rejected   the passage is left as the original, or put back if the change was already in the text
  undecided  left as it is

Safety: a passage is changed only when it is found exactly once (differences in
line wrapping aside). Anything else is reported and skipped. Each file is copied
to <name>/backups/<time>/ before it is written.

Record: each run with --write adds what it changed to <name>/change-record.json and
rewrites <name>/change-record.md, which lists every change under the request it was
made for (from requests.json, written by the build).

  --batch ID      use only this batch (repeatable); default is every batch
  --accept-all    treat every item as accepted and ignore the batch files (for testing)
  --prefer-second with --accept-all, take the second agent's option wherever an item has one
  --root PATH     dissertation folder, if it is not the one recorded when the review was built
"""
import argparse
import datetime
import json
import re
import shutil
import sys
from pathlib import Path

KIT = Path(__file__).resolve().parent
sys.path.insert(0, str(KIT))
import review_lib as lib  # noqa: E402


def find_batches(folder, review_id):
    """{batch id: path}, from the review folder and, for strays, from Downloads."""
    pattern = lib.decisions_pattern(review_id)
    loose = re.compile(pattern.pattern[:-len(r"\.json$")] + r"(?: \(\d+\))?\.json$")
    found, strays = {}, []
    for path in sorted(folder.iterdir()):
        m = pattern.match(path.name)
        if m and path.is_file():
            found[m.group(1)] = path
    downloads = Path.home() / "Downloads"
    if downloads.is_dir():
        for path in sorted(downloads.iterdir()):
            m = loose.match(path.name)
            if m and path.is_file() and m.group(1) not in found:
                found[m.group(1)] = path
                strays.append((m.group(1), path))
    return found, strays


def unbatched(folder, review_id, by_id, latest):
    """Lines to print about decisions the page holds that are in no batch yet. The page
    keeps its working state in <review>.autosave.json; only batches are applied, so say
    when the two differ rather than pass over those decisions in silence."""
    path = folder / lib.autosave_name(review_id)
    if not path.exists():
        return []
    try:
        auto = json.loads(path.read_text(encoding="utf-8"))
    except ValueError:
        return []
    decisions = auto.get("decisions") or {}
    loose = []
    for item_id in auto.get("not_in_a_batch") or []:
        if item_id not in by_id:
            continue
        mine, row = decisions.get(item_id) or {}, latest.get(item_id) or {}
        same = ((mine.get("status") or "undecided") == row.get("status", "undecided")
                and mine.get("override") == row.get("revised_override")
                and mine.get("override_b") == row.get("second_override")
                and mine.get("option") == row.get("option")
                and (mine.get("comment") or "") == (row.get("comment") or ""))
        if not same:
            loose.append(item_id)
    if not loose:
        return []
    when = str(auto.get("updated_at", ""))[:16].replace("T", " ")
    return ["",
            "Not in a batch yet: %d decision(s) made on the page (autosaved %s): %s" % (len(loose), when, ", ".join(loose)),
            "The page keeps them, but they are not applied until Save batch is clicked there."]


# ------------------------------------------------------------------ the change record

IN_TEXT = ("applied", "in_place")
NO_REQUEST_HEADING = {
    "none": ("No request", "Nobody asked for these edits. The reason on each edit is the whole of their purpose."),
    "not recorded": ("Request not recorded", "This review was built without a request for these items. "
                                             "The reason on each edit is the only purpose on record."),
}


def purpose_of(item_id, requests):
    """(the requests an item addresses, and when there are none, why the record has none)."""
    ids = requests["items"].get(item_id)
    if ids is None:
        return [], "not recorded"
    by_id = dict((r["id"], r) for r in requests["requests"])
    found = [by_id[i] for i in ids if i in by_id]
    return found, "" if found else "none"


def purpose_counts(events):
    """'R1 (3), not recorded (1)': how many changes in these events serve each request."""
    counts = {}
    for ev in events:
        if ev["result"] != "unchanged":
            for label in [r["id"] for r in ev["requests"]] or [ev["no_request"]]:
                counts[label] = counts.get(label, 0) + 1
    return ", ".join("%s (%d)" % pair for pair in counts.items())


def stamp_text(iso):
    return str(iso or "")[:16].replace("T", " ")


OPTION_NAME = {"A": "option A, as first proposed", "B": "option B, from the second agent", "neither": "neither option"}


def options_lines(ev):
    """The lines of a change-record entry about an item that showed two options."""
    opt = ev.get("options")
    if not opt:
        return []
    out = ["- **Two options:** chose %s (second agent: %s)." % (OPTION_NAME[opt["chosen"]], opt["by"])]
    if opt["chosen"] != "B":
        out.append("- **Why the second agent disagreed:** %s" % " ".join(opt["b_why"].split()))
    if opt["chosen"] == "B" and opt["a_why"]:
        out.append("- **Why option A was proposed:** %s" % " ".join(opt["a_why"].split()))
    return out


def render_entry(ev):
    head = "### %s" % ev["id"]
    if ev.get("title"):
        head += u" · %s" % ev["title"]
    line = " line %d" % ev["line"] if ev.get("line") else ""
    mine = " (your wording)" if ev.get("your_wording") else ""
    when = "%s, batch %s" % (stamp_text(ev["applied_at"]), ev["batch"])
    out = [head, "", "- **Location:** %s, `%s`%s" % (ev["where"], ev["file"], line),
           "- **Change:** %s%s" % (ev["action"], mine)]
    if ev["result"] in ("applied", "reverted") and ev.get("backup"):
        when += "; the file as it was is in `backups/%s/`" % ev["backup"]
    out.append("- **Applied:** %s" % when)
    if ev.get("why"):
        out.append("- **Why this edit:** %s" % " ".join(ev["why"].split()))
    out += options_lines(ev)
    if ev.get("your_note"):
        out.append("- **Your note:** %s" % " ".join(ev["your_note"].split()))
    out += ["", "**Before**", "", lib.fenced(ev["before"]) if ev["before"] else "*(nothing)*", "",
            "**After**", "", lib.fenced(ev["after"]) if ev["after"] else "*(removed)*", ""]
    if ev.get("options") and ev["options"].get("not_used"):
        out += ["**The option not used**", "", lib.fenced(ev["options"]["not_used"]), ""]
    return out


def render_record(record, requests, item_ids):
    """change-record.md: one section per request, holding the changes made for it."""
    order, sections = [], {}

    def section(req, why=""):
        key = (req["id"], req["text"]) if req else ("", why)
        if key not in sections:
            sections[key] = {"request": req, "why": why, "events": [], "waiting": 0}
            order.append(key)
        return sections[key]

    for req in requests["requests"]:
        section(req)
    latest = {}
    for ev in record["events"]:
        latest[ev["id"]] = ev
        for sec in [section(r) for r in ev["requests"]] or [section(None, ev["no_request"])]:
            sec["events"].append(ev)
    for item_id in item_ids:
        if item_id not in latest:
            reqs, why = purpose_of(item_id, requests)
            for sec in [section(r) for r in reqs] or [section(None, why)]:
                sec["waiting"] += 1
    order.sort(key=lambda key: key[0] == "")        # requests first, the rest after them

    out = ["# Change record: %s" % record["title"], "",
           "What this review changed in the dissertation, listed under the request each change was made for. "
           "`apply_decisions.py --write` updates this file. The same record, as data, is in `%s`." % lib.RECORD_NAME, "",
           "| Request | In the text now | Rejected | Not decided or not applied |", "| --- | ---: | ---: | ---: |"]
    for key in order:
        sec = sections[key]
        ids = set(ev["id"] for ev in sec["events"])
        in_text = sum(1 for i in ids if latest[i]["result"] in IN_TEXT)
        label = sec["request"]["id"] if sec["request"] else NO_REQUEST_HEADING[sec["why"]][0]
        out.append("| %s | %d | %d | %d |" % (label, in_text, len(ids) - in_text, sec["waiting"]))
    out.append("")
    shown = {}      # an edit made for two requests is written out under the first of them
    for key in order:
        sec, req = sections[key], sections[key]["request"]
        if req:
            out += ["## %s" % req["id"], ""]
            out += [("> " + line) if line.strip() else ">" for line in req["text"].split("\n")]
            said = ", ".join(x for x in (req.get("asked"), ("by " + req["by"]) if req.get("by") else "", req.get("source")) if x)
            out += ["", "Asked: %s." % said, ""] if said else [""]
        else:
            out += ["## %s" % NO_REQUEST_HEADING[sec["why"]][0], "", NO_REQUEST_HEADING[sec["why"]][1], ""]
        changes = [ev for ev in sec["events"] if ev["result"] != "unchanged"]
        declined = [ev for ev in sec["events"] if ev["result"] == "unchanged"]
        if not changes and not declined:
            out += ["Nothing applied for this request yet.", ""]
        for ev in changes:
            mark = (ev["id"], ev["applied_at"], ev["action"])
            if mark in shown:
                out += ["### %s" % ev["id"], "", "See %s: %s." % (shown[mark], ev["action"]), ""]
            else:
                shown[mark] = key[0] or NO_REQUEST_HEADING[sec["why"]][0]
                out += render_entry(ev)
        if declined:
            out += ["### Rejected, text left as it was", ""]
            for ev in declined:
                title = u" · %s" % ev["title"] if ev.get("title") else ""
                why = ": %s" % " ".join(ev["why"].split()) if ev.get("why") else ""
                mine = " Your note: %s" % " ".join(ev["your_note"].split()) if ev.get("your_note") else ""
                both = " Two options: chose %s (second agent: %s)." % (OPTION_NAME[ev["options"]["chosen"]], ev["options"]["by"]) if ev.get("options") else ""
                out.append("- **%s**%s%s%s%s" % (ev["id"], title, why, both, mine))
            out.append("")
    return "\n".join(out).rstrip("\n") + "\n"


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description="Apply saved review decisions to the dissertation.")
    ap.add_argument("folder", help="the review folder, e.g. waiting_for_review/pronoun-check")
    ap.add_argument("--write", action="store_true", help="edit the files (default is a dry run)")
    ap.add_argument("--batch", action="append", default=[], help="use only this batch id (repeatable)")
    ap.add_argument("--accept-all", action="store_true", help="treat every item as accepted (testing)")
    ap.add_argument("--prefer-second", action="store_true", help="with --accept-all, take the second agent's option wherever there is one")
    ap.add_argument("--root", help="dissertation folder")
    args = ap.parse_args()
    if args.prefer_second and not args.accept_all:
        ap.error("--prefer-second only goes with --accept-all; otherwise the batches say which option was chosen")

    folder = Path(args.folder).resolve()
    if not (folder / lib.DATA_NAME).exists():
        raise SystemExit("No %s in %s. Build the review first." % (lib.DATA_NAME, folder))
    data = lib.read_js(folder / lib.DATA_NAME, lib.DATA_PREFIX)
    review_id = data["review_id"]
    if data.get("mode") == "check":
        print("%s only checks readings, so there is nothing to apply and no file was changed." % review_id)
        print("The decisions are in the batch files next to the page.")
        return 0
    root = Path(args.root).resolve() if args.root else (folder / data["root"]).resolve()
    items = data["items"]
    by_id = dict((it["id"], it) for it in items)
    now = datetime.datetime.now()
    stamp = now.strftime("%Y%m%d-%H%M%S")
    now_iso = now.astimezone().isoformat(timespec="seconds")

    log_path = folder / lib.LOG_NAME
    log = json.loads(log_path.read_text(encoding="utf-8")) if log_path.exists() else {"items": {}, "batches": {}}
    requests = lib.read_requests(folder)
    record_path = folder / lib.RECORD_NAME
    record = json.loads(record_path.read_text(encoding="utf-8")) if record_path.exists() else {
        "about": "Written by apply_decisions.py: every change this review made, with the request it was made for.",
        "review_id": review_id, "title": data["title"], "events": []}

    # ---- decisions: every batch in time order, the latest row for an item wins
    final, used, strays, superseded, latest = {}, [], [], {}, {}
    if args.accept_all:
        print("Treating all %d items as accepted (--accept-all)." % len(items))
        for it in items:
            row = {"id": it["id"], "status": "accepted", "hash": it["hash"], "_batch": "accept-all"}
            second = it.get("second")
            if second:
                row["second_hash"] = second["hash"]
                if args.prefer_second and second["action"] == "keep":
                    row["status"] = "rejected"
                elif args.prefer_second:
                    row["option"] = "second"
            final[it["id"]] = row
    else:
        found, strays = find_batches(folder, review_id)
        wanted = sorted(found) if not args.batch else [b for b in sorted(found) if b in args.batch]
        missing = [b for b in args.batch if b not in found]
        if missing:
            raise SystemExit("No such batch: %s. Batches here: %s" % (", ".join(missing), ", ".join(sorted(found)) or "none"))
        if not wanted:
            print("No saved batch yet. Open %s, decide some items and click Save batch." % (folder / lib.PAGE_NAME))
            for line in unbatched(folder, review_id, by_id, {}):
                print(line)
            return 2
        newest = {}     # item id -> the last batch that decides it, selected or not
        for batch_id in sorted(found):
            payload = json.loads(found[batch_id].read_text(encoding="utf-8"))
            if payload.get("review_id") != review_id:
                print("  ignoring %s: it belongs to review %r" % (found[batch_id].name, payload.get("review_id")))
                continue
            rows = payload.get("decisions", [])
            for row in rows:
                newest[row["id"]] = batch_id
                latest[row["id"]] = row
            if batch_id not in wanted:
                continue
            used.append((batch_id, found[batch_id], rows))
            for row in rows:
                row = dict(row)
                row["_batch"] = batch_id
                final[row["id"]] = row
            print("Batch %s  saved %s  %d decision(s)  %s" % (batch_id, str(payload.get("saved_at", ""))[:16].replace("T", " "),
                                                           len(rows), found[batch_id].name))
        # An older batch applied on its own must not undo what a later batch decided.
        for item_id in sorted(final):
            if newest[item_id] != final[item_id]["_batch"]:
                superseded[item_id] = newest[item_id]
        for batch_id, path in strays:
            print("  %s is in Downloads; %s" % (path.name, "moving it into the review folder" if args.write
                                                else "it is moved into the review folder with --write"))
        unknown = sorted(k for k in final if k not in by_id)
        if unknown:
            print("  ignoring %d decision(s) for items no longer in the review: %s" % (len(unknown), ", ".join(unknown)))
    print("")

    docs = {}

    def doc_for(rel):
        if rel not in docs:
            path = (root / rel).resolve()
            if root not in path.parents or not path.exists():
                return None
            docs[rel] = lib.Doc(path)
        return docs[rel]

    report, new_entries, events = [], {}, {}

    def note(item_id, kind, msg):
        report.append((item_id, kind, msg))

    for it in items:
        row = final.get(it["id"])
        status = row.get("status") if row else None
        entry = log["items"].get(it["id"])
        if it["id"] in superseded:
            note(it["id"], "skip", "decided again in the later batch %s, which is not part of this run; left as it is"
                 % superseded[it["id"]])
            continue
        if status not in ("accepted", "rejected"):
            if row and entry and entry.get("result") in ("applied", "in_place"):
                note(it["id"], "open", "decision cleared after the change was applied; the text is left as it is")
            continue
        if row.get("hash") and row["hash"] != it["hash"]:
            note(it["id"], "skip", "the suggestion was rebuilt after this decision was made; decide it again on the page")
            continue
        doc = doc_for(it["file"])
        if doc is None:
            note(it["id"], "skip", "file not found under the dissertation folder: %s" % it["file"])
            continue
        second = it.get("second")
        on_second = status == "accepted" and row.get("option") == "second"
        if row.get("option") == "second" and (not second or row.get("second_hash") != second["hash"]):
            note(it["id"], "skip", "the second agent's option %s after this decision was made; decide it again on the page"
                 % ("changed" if second else "was withdrawn"))
            continue
        if second and row.get("second_hash") != second["hash"]:
            note(it["id"], "warn", "decided before the second agent's disagreement was %s; the decision stands unless it is made again on the page"
                 % ("added" if not row.get("second_hash") else "changed"))
        field = "second_override" if on_second else "revised_override"
        override = row.get(field) if isinstance(row.get(field), str) else None
        mine_wording = override is not None
        if on_second and override is None:
            override = second["revised"]      # its wording, or nothing when it removes the passage
        original, accepted = lib.compose(it, override)
        kept_original = entry.get("original") if entry else None
        target = accepted if status == "accepted" else (kept_original if kept_original is not None else original)
        mine = " (your wording)" if mine_wording and status == "accepted" else ""

        # Which form of the passage is in the file now? Longest first, because an
        # inserted or tagged passage still contains its original.
        pool = []
        other = lib.compose(it, second["revised"])[1] if second and second["revised"] else None
        for cand in (target, entry.get("text") if entry else None, accepted, lib.compose(it)[1], other, original, kept_original):
            if cand and cand not in pool:
                pool.append(cand)
        pool.sort(key=len, reverse=True)
        current, hits = None, []
        for cand in pool:
            hits = lib.live_hits(doc.text, cand)
            if hits:
                current = cand
                break

        result, before, action, line = None, target, "", None
        if current is None:
            removed = entry and entry.get("text") == "" and entry.get("ctx")
            if target == "" and entry and entry.get("status") == "accepted":
                note(it["id"], "done", "%s  already removed" % it["file"])
                result = "in_place"
            elif target and removed:
                joined = entry["ctx"][0] + entry["ctx"][1]
                at = doc.text.find(joined)
                if joined and at >= 0 and doc.text.find(joined, at + 1) < 0:
                    cut = at + len(entry["ctx"][0])
                    doc.text = doc.text[:cut] + target + doc.text[cut:]
                    line = lib.line_of(doc.text, cut)
                    if status == "rejected":
                        note(it["id"], "revert", "%s:%d  removed passage put back" % (it["file"], line))
                        result, before, action = "reverted", "", "removed passage put back"
                    else:       # another option was chosen after this one removed the passage
                        note(it["id"], "apply", "%s:%d  written where the passage was removed%s" % (it["file"], line, mine))
                        result, before, action = "applied", "", "written where the passage was removed"
                    entry = dict(entry, text=target, ctx=None)
                else:
                    note(it["id"], "skip", "the text around the removed passage has changed; restore it by hand from backups/%s"
                         % entry.get("backup", ""))
            else:
                note(it["id"], "skip", "%s  the passage was not found (it changed since the review was built); "
                                       "build the review again and decide this item again" % it["file"])
        elif len(hits) > 1:
            note(it["id"], "skip", "%s  the passage occurs %d times; not applied" % (it["file"], len(hits)))
        elif current == target:
            line = lib.line_of(doc.text, hits[0][0])
            if status == "accepted":
                note(it["id"], "done", "%s:%d  already in place" % (it["file"], line))
                result, action = "in_place", "already in the text when accepted"
                before = kept_original if kept_original is not None else original
            else:
                note(it["id"], "reject", "left as the original")
                result, action = "unchanged", "left as the original"
        else:
            start, end = hits[0]
            if target == "":
                # A removed sentence takes the space before it along when nothing follows on the line.
                while start > 0 and doc.text[start - 1] in " \t" and (end == len(doc.text) or doc.text[end] in " \t\n"):
                    start -= 1
            was = doc.text[start:end]
            ctx = [doc.text[max(0, start - 160):start], doc.text[end:end + 160]]
            doc.text = doc.text[:start] + target + doc.text[end:]
            line = lib.line_of(doc.text, start)
            before = was
            if status == "accepted":
                what = "removed" if target == "" else "inserted" if it["op"] == "insert" else \
                    "marked for deletion" if it["op"] == "delete" and override is None else "replaced"
                note(it["id"], "apply", "%s:%d  %s%s" % (it["file"], line, what, mine))
                result, action = "applied", what
            else:
                note(it["id"], "revert", "%s:%d  put back the original" % (it["file"], line))
                result, action = "reverted", "put back the original"
            fresh = dict(entry or {})
            if kept_original is None and current in (original, lib.compose(it)[0]):
                fresh["original"] = was          # the exact text from the file, to restore on a later reject
            fresh["ctx"] = ctx if target == "" else None
            fresh["text"] = target
            entry = fresh
        settled = result in ("in_place", "unchanged") and entry and entry.get("status") == status
        if result and not settled:      # a settled item keeps the record of when it was applied
            fresh = dict(entry or {})
            fresh.update({"status": status, "result": result, "at": now_iso, "batch": row["_batch"],
                          "file": it["file"], "backup": stamp if result in ("applied", "reverted") else fresh.get("backup", "")})
            fresh.setdefault("text", target)
            if second:
                fresh["option"] = "second" if on_second else "first"
            new_entries[it["id"]] = fresh
            reqs, no_request = purpose_of(it["id"], requests)
            chosen = None
            if second:
                chosen = "B" if on_second or (status == "rejected" and second["action"] == "keep") else \
                    "A" if status == "accepted" else "neither"
            events[it["id"]] = {
                "id": it["id"], "title": it.get("title") or "", "type": it["type"],
                "file": it["file"], "line": line, "where": it.get("where") or it["file"],
                "decision": status, "result": result, "action": action,
                "before": before, "after": target,
                "your_wording": mine_wording and status == "accepted",
                "requests": reqs, "no_request": no_request,
                "why": (second["note"] if chosen == "B" else it.get("note")) or "", "your_note": row.get("comment") or "",
                "batch": row["_batch"], "decided_at": row.get("decided_at") or "", "applied_at": now_iso,
                "backup": stamp if result in ("applied", "reverted") else "",
            }
            if second:
                not_used = {"A": second["revised"], "B": it["revised"]}.get(chosen, "")
                events[it["id"]]["options"] = {"chosen": chosen, "by": second["by"], "action": second["action"],
                                               "a_why": it.get("note") or "", "b_why": second["note"], "not_used": not_used}

    # Later items in this run may have moved a passage: say where it ended up.
    for ev in events.values():
        hits = lib.live_hits(docs[ev["file"]].text, ev["after"]) if ev["after"] else []
        if hits:
            ev["line"] = lib.line_of(docs[ev["file"]].text, hits[0][0])

    # ---- report
    label = {"apply": "APPLY " if args.write else "WOULD ", "revert": "REVERT" if args.write else "WOULD ",
             "done": "DONE  ", "skip": "SKIP  ", "reject": "reject", "open": "open  ", "warn": "NOTE  "}
    width = max([len(r[0]) for r in report] + [4])
    for item_id, kind, msg in report:
        print("  %s %s  %s" % (label[kind], item_id.ljust(width), msg))
    decided = sum(1 for r in final.values() if r.get("status") in ("accepted", "rejected") and r["id"] in by_id)
    print("")
    print("%d of %d items decided; %d still open." % (decided, len(items), len(items) - decided))
    if not args.accept_all:
        for line in unbatched(folder, review_id, by_id, latest):
            print(line)
    notes = [(r["id"], r["comment"]) for r in final.values() if r.get("comment") and r["id"] in by_id]
    if notes:
        print("")
        print("Notes left on the page:")
        for item_id, text in notes:
            print("  %s (%s): %s" % (item_id, final[item_id].get("status", "undecided"), " ".join(text.split())))

    changed = [d for d in docs.values() if d.changed]
    n_change = sum(1 for r in report if r[1] in ("apply", "revert"))
    n_skip = sum(1 for r in report if r[1] == "skip")
    print("")
    if not args.write:
        if changed:
            print("Dry run: %d change(s) in %d file(s)%s. Run again with --write to edit the files."
                  % (n_change, len(changed), (", %d skipped" % n_skip) if n_skip else ""))
        else:
            print("Dry run: nothing to change%s." % ((", %d skipped (see above)" % n_skip) if n_skip else ""))
        if purpose_counts(events.values()):
            print("With --write, %s records these changes under: %s." % (lib.RECORD_MD_NAME, purpose_counts(events.values())))
        return 0

    backup_dir = folder / "backups" / stamp
    for d in changed:
        rel = d.path.relative_to(root)
        dest = backup_dir / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(str(d.path), str(dest))
        new_text = d.render()
        stray = sorted(set(c for c in new_text if ord(c) < 32 and c not in "\t\n\r") - set(d.text0))
        if stray:
            print("  NOT WRITTEN %s: the new text contains control characters %s" % (rel, [hex(ord(c)) for c in stray]))
            for item_id, entry in list(new_entries.items()):
                if entry["file"] == str(rel).replace("\\", "/"):
                    del new_entries[item_id]
            continue
        d.path.write_bytes(new_text.encode("utf-8"))
        print("  wrote %s" % rel)
    for batch_id, path in strays:
        shutil.move(str(path), str(folder / ("%s.decisions.%s.json" % (review_id, batch_id))))
    if changed:
        lib.write_text(backup_dir / "apply-log.txt", "\n".join("%s\t%s\t%s" % r for r in report) + "\n")

    # ---- the record of what changed and why. Before the log: if this fails, the next
    # run still sees these items as new and records them.
    recorded = [events[item_id] for item_id in events if item_id in new_entries]
    if recorded or record["events"]:
        record["title"] = data["title"]
        record["events"].extend(recorded)
        lib.write_text(record_path, json.dumps(record, ensure_ascii=False, indent=1) + "\n")
        lib.write_text(folder / lib.RECORD_MD_NAME, render_record(record, requests, [it["id"] for it in items]))

    # ---- remember what is in place, for later runs and for the page
    log["items"].update(new_entries)
    skipped = set(r[0] for r in report if r[1] == "skip")
    for batch_id, _path, rows in used:
        ids = [row["id"] for row in rows if row["id"] in by_id]
        first = log["batches"].get(batch_id, {}).get("at", now_iso)
        log["batches"][batch_id] = {"at": first, "decisions": len(ids),
                                    "skipped": len([i for i in ids if i in skipped and final[i]["_batch"] == batch_id])}
    lib.write_text(log_path, json.dumps(log, ensure_ascii=True, indent=1) + "\n")
    page = {"review_id": review_id, "updated": now_iso, "batches": log["batches"],
            "applied": dict((k, dict({"status": v["status"], "result": v["result"], "at": v["at"], "batch": v["batch"]},
                                     **({"option": v["option"]} if v.get("option") else {})))
                            for k, v in log["items"].items())}
    lib.write_js(folder / lib.APPLIED_NAME, lib.APPLIED_PREFIX, page,
                 "Written by apply_decisions.py: which decisions are already in the dissertation.")
    print("")
    if changed:
        print("Done: %d change(s)%s. Originals are in %s" % (n_change, (", %d skipped" % n_skip) if n_skip else "",
                                                             backup_dir.relative_to(folder)))
        print("Recompile main.tex to see the green [HY: ... start] and [HY: ... end] tags.")
    else:
        print("Nothing to change%s." % ((", %d skipped (see above)" % n_skip) if n_skip else ""))
    if purpose_counts(recorded):
        print("Recorded in %s under: %s." % (lib.RECORD_MD_NAME, purpose_counts(recorded)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
