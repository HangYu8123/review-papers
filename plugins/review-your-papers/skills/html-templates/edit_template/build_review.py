#!/usr/bin/env python3
"""Build a review folder from its items file.

    python waiting_for_review/_template/build_review.py waiting_for_review/<name>

Reads   <name>/items.txt, <name>/items/*.txt and/or <name>/items.json
        <name>/disagreements.txt   optional: a second agent's other option on existing items
Writes  <name>/suggestions.md      the list: location, original, revised, why
        <name>/review-data.js      the same list, for the page
        <name>/requests.json       the requests behind the review and which items address them
        <name>/review.html         a copy of the shared page (edit the one in _template)
        <name>/review-applied.js   created empty if missing; the apply step fills it

The .tex files are only read: to find each passage, fill in its chapter, section
and line, and see whether the change is already in the text. Run it again whenever
the items or the chapters change. Decisions are kept, because they are stored by
item id and are dropped only for an item whose text changed.

The format of items.txt is described in README.md in this folder.
"""
import argparse
import datetime
import hashlib
import json
import os
import re
import shutil
import sys
from pathlib import Path

KIT = Path(__file__).resolve().parent
sys.path.insert(0, str(KIT))
import review_lib as lib  # noqa: E402

SECTIONS = ("original", "revised", "anchor", "note", "title")
# Items of a 'mode: check' review show an image of what was read. These do not affect the hash.
CHECK_FIELDS = ("image", "image_size", "image_label", "reading_label", "original_label",
                "page_image", "page_box", "source_label")
HEAD = re.compile(r"\\(chapter|section|subsection|subsubsection)\*?\s*(?:\[[^\]]*\])?\s*\{")
LEVEL = {"chapter": 0, "section": 1, "subsection": 2, "subsubsection": 3}
NO = ("no", "false", "0", "none", "off")


# ------------------------------------------------------------------ reading items

def parse_txt(text, source):
    """items.txt: '@review', '@request ID' and '@item ID' records, 'key: value' lines, and
    raw '--- original' / '--- revised' / '--- anchor' / '--- note' / '--- title' blocks.
    A request holds its words in a '--- text' block. Requests come back in review['_requests']."""
    review, items, requests = {}, [], []
    cur, sec, buf = None, None, []
    in_request = False

    def flush():
        if cur is not None and sec is not None:
            cur[sec] = "\n".join(buf).strip("\n")

    for n, line in enumerate(text.replace("\r\n", "\n").split("\n"), 1):
        m = re.match(r"^@(item|request)\s+(\S+)\s*$", line)
        if m:
            flush()
            cur, sec, buf = {"id": m.group(2), "_src": "%s:%d" % (source, n)}, None, []
            in_request = m.group(1) == "request"
            (requests if in_request else items).append(cur)
            continue
        if re.match(r"^@review\s*$", line):
            flush()
            cur, sec, buf = review, None, []
            in_request = False
            continue
        m = re.match(r"^---\s*(%s)\s*$" % "|".join(("text",) if in_request else SECTIONS), line)
        if m and cur is not None and cur is not review:
            flush()
            sec, buf = m.group(1), []
            continue
        if sec is not None:
            buf.append(line)
            continue
        if cur is None or not line.strip() or line.lstrip().startswith("#"):
            continue
        m = re.match(r"^([^:]+?)\s*:\s*(.*)$", line)
        if not m:
            raise SystemExit("%s:%d: expected 'key: value', got: %s" % (source, n, line))
        cur[m.group(1).strip()] = m.group(2).strip()
    flush()
    if requests:
        review["_requests"] = requests
    return review, items


def load_items(folder):
    review, items, requests = {}, [], []
    jpath = folder / "items.json"
    if jpath.exists():
        data = json.loads(jpath.read_text(encoding="utf-8"))
        review.update(data.get("review") or dict((k, v) for k, v in data.items() if k not in ("items", "requests")))
        for req in data.get("requests", []):
            req = dict(req)
            req.setdefault("_src", "items.json")
            requests.append(req)
        for it in data.get("items", []):
            it = dict(it)
            it.setdefault("_src", "items.json")
            items.append(it)
    sources = [folder / "items.txt"] if (folder / "items.txt").exists() else []
    sources += sorted((folder / "items").glob("*.txt")) if (folder / "items").is_dir() else []
    for path in sources:
        rev, its = parse_txt(path.read_text(encoding="utf-8"), path.name)
        requests.extend(rev.pop("_requests", []))
        review.update(rev)
        items.extend(its)
    if not items:
        raise SystemExit("No items found. Write %s (see README.md in %s)." % (folder / "items.txt", KIT))
    if requests:
        review["_requests"] = requests
    return review, items


def resolve_requests(review, raw_items, review_id, problems):
    """The requests behind a review and, for each item, which of them it addresses.

    Kept out of the page's data on purpose: requests.json is read by the apply step only.
    An item with no 'request:' line takes the review's request when there is just one.
    'request: none' says plainly that nobody asked for this edit. In the 'items' map, an
    empty list means exactly that, and an item left out means nothing was recorded for it.
    """
    requests, known = [], set()
    for raw in review.get("_requests", []):
        rid, text = str(raw.get("id") or "").strip(), str(raw.get("text") or "").strip("\n")
        where = raw.get("_src", "")
        if not rid or not text.strip():
            raise SystemExit("%s  request %s: a request needs an id and its text in a '--- text' block" % (where, rid or "?"))
        if rid.lower() == "none":
            raise SystemExit("%s  'none' is reserved for an item with no request; give the request another id" % where)
        if rid in known:
            raise SystemExit("Two requests share the id %s" % rid)
        known.add(rid)
        record = dict((k, v) for k, v in raw.items() if not k.startswith("_"))
        record["text"] = text
        requests.append(record)
    if not requests:
        problems.append("no @request in the items file: write down the question or request this review "
                        "answers, or the change record will say 'request not recorded'")
    mapping = {}
    for raw in raw_items:
        iid, named = str(raw["id"]).strip(), raw.get("request")
        if not named:
            if len(requests) == 1:
                mapping[iid] = [requests[0]["id"]]
            elif requests:
                problems.append("%s: says no 'request:', and this review has %d requests" % (iid, len(requests)))
            continue
        ids = named if isinstance(named, list) else [r.strip() for r in str(named).split(",") if r.strip()]
        if [r.lower() for r in ids] == ["none"]:
            mapping[iid] = []
            continue
        unknown = [r for r in ids if r not in known]
        if unknown:
            problems.append("%s: 'request: %s' names a request that no @request declares" % (iid, ", ".join(unknown)))
        if len(unknown) < len(ids):     # with no valid id the item stays unmapped, not "nobody asked"
            mapping[iid] = [r for r in ids if r in known]
    return {"about": "Written by build_review.py from the items file. Read by apply_decisions.py for "
                     "change-record.md. The review page does not read it.",
            "review_id": review_id, "requests": requests, "items": mapping}


def read_disagreements(folder):
    """disagreements.txt: one '@reviewer' record, then '@disagree ID' records with 'key: value'
    lines and raw '--- revised' / '--- note' blocks. Returns (reviewer, records), or (None, [])
    when the review has no such file."""
    path = folder / lib.DISAGREEMENTS_NAME
    if not path.exists():
        return None, []
    source = path.name
    reviewer, records = {}, []
    cur, sec, buf = None, None, []

    def flush():
        if cur is not None and sec is not None:
            cur[sec] = "\n".join(buf).strip("\n")

    for n, line in enumerate(path.read_text(encoding="utf-8").replace("\r\n", "\n").split("\n"), 1):
        m = re.match(r"^@disagree\s+(\S+)\s*$", line)
        if m:
            flush()
            cur, sec, buf = {"id": m.group(1), "_src": "%s:%d" % (source, n)}, None, []
            records.append(cur)
            continue
        if re.match(r"^@reviewer\s*$", line):
            flush()
            cur, sec, buf = reviewer, None, []
            continue
        m = re.match(r"^---\s*(revised|note)\s*$", line)
        if m and cur is not None and cur is not reviewer:
            flush()
            sec, buf = m.group(1), []
            continue
        if sec is not None:
            buf.append(line)
            continue
        if cur is None or not line.strip() or line.lstrip().startswith("#"):
            continue
        m = re.match(r"^([^:]+?)\s*:\s*(.*)$", line)
        if not m:
            raise SystemExit("%s:%d: expected 'key: value', got: %s" % (source, n, line))
        cur[m.group(1).strip()] = m.group(2).strip()
    flush()
    return reviewer, records


def same_words(a, b):
    """The kit treats any run of whitespace as equal when it matches text."""
    return a.split() == b.split()


def attach_disagreements(reviewer, records, review, items, problems):
    """A second agent's other option goes on the item it disagrees with, as it['second'], so
    the page and the list show one entry with two options. The item's own hash is untouched,
    so adding a disagreement keeps the decisions already saved. Returns what the page says
    about the second agent, or None when there is no disagreements.txt."""
    if reviewer is None:
        return None
    name = lib.DISAGREEMENTS_NAME
    if str(review.get("mode", "")).lower() == "check":
        raise SystemExit("%s: a 'mode: check' review holds readings, and two options are not supported there." % name)
    by = str(reviewer.get("by") or "").strip()
    covers = str(reviewer.get("covers") or "").strip()
    if not by or not covers:
        raise SystemExit("%s: start the file with an @reviewer record that has 'by:' (who looked) and 'covers:' "
                         "('all', or the ids of the items that were looked at)." % name)
    by_id = dict((it["id"], it) for it in items)
    looked = None
    if covers.lower() != "all":
        looked = [c.strip() for c in covers.split(",") if c.strip()]
        for iid in looked:
            if iid not in by_id:
                problems.append("%s: 'covers:' names %s, which is not an item of this review" % (name, iid))
    for rec in records:
        iid, where = rec["id"], rec["_src"]

        def bad(msg):
            raise SystemExit("%s  disagreement on %s: %s" % (where, iid, msg))

        if iid not in by_id:
            bad("no item of this review has that id")
        it = by_id[iid]
        if it.get("second"):
            bad("this item already has a disagreement, and an entry shows two options at most")
        note = str(rec.get("note") or "").strip()
        if not note:
            bad("say why, in 'note:' or a '--- note' block")
        against = str(rec.get("against") or "").strip()
        if not against:
            bad("say which version was read, in 'against:'; it is the Version line of the entry in %s" % lib.MD_NAME)
        action = str(rec.get("action") or "reword").strip().lower()
        if action not in ("reword", "keep", "remove"):
            bad("'action:' must be keep or remove, or left out when '--- revised' holds another wording")
        text = rec.get("revised") or ""
        if action == "reword":
            if not text.strip():
                bad("give the other wording in a '--- revised' block, or say 'action: keep' or 'action: remove'")
            if same_words(text, it["revised"]):
                bad("this is the wording the entry already proposes, which is agreement: leave the entry out")
            if it["op"] != "insert" and same_words(text, it["original"]):
                bad("this is the original passage: say 'action: keep' instead")
        elif text.strip():
            bad("'action: %s' has no wording of its own: remove the '--- revised' block" % action)
        if action == "remove" and it["op"] != "replace":
            bad("'action: remove' only fits an entry that rewords a passage")
        it["second"] = {"action": action, "revised": text if action == "reword" else "", "note": note, "by": by,
                        "against": against, "stale": against != it["hash"],
                        "hash": hashlib.sha1(json.dumps([action, text], ensure_ascii=True).encode("ascii")).hexdigest()[:12]}
        if it["second"]["stale"]:
            problems.append("%s: the disagreement was written against an earlier version of this item (%s, now %s); "
                            "look at the item again, then update 'against:'" % (iid, against, it["hash"]))
    return {"by": by, "date": str(reviewer.get("date") or "").strip(),
            "looked_at": len(items) if looked is None else len(set(looked) | set(r["id"] for r in records)),
            "disagrees": len(records)}


def dotted(review, prefix):
    """'type.x: label' lines from items.txt, or a 'types' object from items.json."""
    out = []
    plural = review.get(prefix + "s")
    if isinstance(plural, dict):
        out += [(k, v.get("label") if isinstance(v, dict) else v) for k, v in plural.items()]
    elif isinstance(plural, list):
        out += [(g["key"], g.get("label", g["key"])) for g in plural]
    out += [(k[len(prefix) + 1:], v) for k, v in review.items() if k.startswith(prefix + ".")]
    return out


# ------------------------------------------------------------------ locations

def strip_comment(line):
    m = re.search(r"(?<!\\)%", line)
    return line[:m.start()] if m else line


def brace_arg(src, i):
    """Text inside the braces that open at src[i]."""
    depth, j = 0, i
    while j < len(src):
        c = src[j]
        if c == "\\":
            j += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return src[i + 1:j]
        j += 1
    return src[i + 1:]


def plain(tex):
    """A heading as plain text."""
    t = tex.replace("\\&", "&").replace("\\%", "%").replace("\\_", "_")
    for _ in range(4):
        t = re.sub(r"\\(?:textit|textbf|emph|texttt|textsc|mbox)\{([^{}]*)\}", r"\1", t)
    t = re.sub(r"\\[A-Za-z]+\*?(?:\{\})?", "", t)
    t = t.replace("``", u"\u201c").replace("''", u"\u201d").replace("~", " ")
    t = t.replace("{", "").replace("}", "")
    return re.sub(r"\s+", " ", t).strip()


def outline(text):
    """[(position, level, title)] for the headings of a file, comments ignored."""
    out, pos = [], 0
    for line in text.split("\n"):
        for m in HEAD.finditer(strip_comment(line)):
            out.append((pos + m.start(), LEVEL[m.group(1)], plain(brace_arg(text, pos + m.end() - 1))))
        pos += len(line) + 1
    return out


def section_path(heads, pos):
    path = {}
    for p, level, title in heads:
        if p > pos:
            break
        path[level] = title
        for deeper in [k for k in path if k > level]:
            del path[deeper]
    return [path[k] for k in sorted(path) if k > 0]


def short_title(title):
    head = title.split(":")[0].strip()
    if ":" in title and len(head) <= 40:
        return head
    return title if len(title) <= 46 else title[:44].rstrip() + u"\u2026"


def chapter_map(root):
    """Chapters in the order main.tex includes them: {file: {label, title}}, plus
    the \\label of each chapter so the page can print 'Chapter 3' for \\autoref."""
    chapters, labels = {}, {}
    main = root / "main.tex"
    if not main.exists():
        return chapters, labels
    number, letter, appendix = 0, 0, False
    for line in main.read_text(encoding="utf-8", errors="replace").splitlines():
        code = strip_comment(line)
        if re.search(r"\\appendix\b", code):
            appendix = True
        for m in re.finditer(r"\\(?:include|input)\{([^}]+)\}", code):
            rel = m.group(1).strip()
            rel = rel if rel.endswith(".tex") else rel + ".tex"
            path = root / rel
            if not path.exists():
                continue
            src = path.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n")
            heads = [h for h in outline(src) if h[1] == 0]
            if not heads:
                continue
            if appendix:
                letter += 1
                label = "Appendix %s" % chr(64 + letter)
            else:
                number += 1
                label = "Chapter %d" % number
            chapters[rel.replace("\\", "/")] = {"label": label, "title": heads[0][2]}
            lm = re.search(r"\\label\{([^}]+)\}", src[heads[0][0]:heads[0][0] + 600])
            if lm:
                labels[lm.group(1)] = label
    return chapters, labels


def find_root(folder):
    for parent in folder.parents:
        if (parent / "main.tex").exists():
            return parent
    return folder.parent.parent


# ------------------------------------------------------------------ items

def nearby(text, start, end, size=320):
    """A few lines on each side of a passage, cut at line ends, for the page's 'Nearby context'."""
    before = text[max(0, start - size):start]
    if start > size and "\n" in before:
        before = before[before.index("\n") + 1:]
    after = text[end:end + size]
    if end + size < len(text) and "\n" in after:
        after = after[:after.rindex("\n")]
    return before.strip("\n"), after.strip("\n")


def make_wrap(it, review):
    if str(it.get("markers", review.get("markers", "yes"))).lower() in NO:
        return ["", ""]
    body = it["original"] if it["op"] == "delete" else it["revised"]
    style = it.get("marker_style") or review.get("marker_style") or ("block" if "\n" in body.strip() else "inline")
    label = it.get("marker") or it["type"]
    opening, closing = "\\hang{%s start}" % label, "\\hang{%s end}" % label
    if style == "block":
        return [opening + "\n", "\n" + closing]
    return [opening + " ", " " + closing]


def enrich(raw, review, root, docs, chapters, problems, second_text=""):
    """Turn one authored item into the record the page and the apply step use."""
    src = raw.get("_src", "")
    iid = str(raw.get("id", "")).strip()

    def bad(msg):
        raise SystemExit("%s  item %s: %s" % (src, iid or "?", msg))

    if not iid:
        bad("no id")
    it = {"id": iid}
    it["type"] = str(raw.get("type") or review.get("type") or "change").strip()
    it["original"] = raw.get("original") or ""
    it["revised"] = raw.get("revised") or ""
    it["anchor"] = raw.get("anchor") or ""
    op = (raw.get("op") or "").strip().lower()
    if not op:
        op = "insert" if it["anchor"] and not it["original"] else ("delete" if not it["revised"] else "replace")
    if op not in ("replace", "insert", "delete"):
        bad("op must be replace, insert or delete")
    it["op"] = op
    if op == "insert" and not (it["anchor"] and it["revised"]):
        bad("an insert needs '--- anchor' (text already in the file) and '--- revised' (the new text)")
    if op == "replace" and not (it["original"] and it["revised"]):
        bad("a replace needs '--- original' and '--- revised'")
    if op == "delete" and not it["original"]:
        bad("a delete needs '--- original'")
    if op == "replace" and it["original"] == it["revised"]:
        bad("original and revised are the same")
    rel = str(raw.get("file") or review.get("file") or "").strip().replace("\\", "/")
    if not rel:
        bad("no file")
    it["file"] = rel
    if op == "insert":
        it["position"] = "before" if str(raw.get("position", "after")).lower() == "before" else "after"
        sep = raw.get("sep", review.get("sep"))
        it["sep"] = {"space": " ", "newline": "\n", "paragraph": "\n\n", None: "\n\n"}.get(sep, sep)
    if op == "delete":
        style = str(raw.get("delete_style") or review.get("delete_style") or "remove").lower()
        if style not in ("remove", "mark"):
            bad("delete_style must be remove or mark")
        it["delete_style"] = style
    if raw.get("marker"):
        it["marker"] = str(raw["marker"]).strip()
    # A removed passage needs no tags, but keeps them for the case where the
    # reviewer edits the deletion into a shorter version on the page.
    it["wrap"] = make_wrap(dict(raw, **it), review)
    it["title"] = raw.get("title") or ""
    it["note"] = raw.get("note") or ""
    tags = raw.get("tags") or []
    if not isinstance(tags, list):
        tags = [t.strip() for t in str(tags).split(",") if t.strip()]
    it["tags"] = tags
    # Evidence does not affect the change hash or which passage is applied.
    # Adding a comparison therefore preserves saved review decisions.
    if isinstance(raw.get("repetition"), dict):
        it["repetition"] = raw["repetition"]
    for key in CHECK_FIELDS:
        if raw.get(key):
            it[key] = raw[key]

    # Where it is in the dissertation now.
    path = root / rel
    it["line"] = int(raw["line"]) if str(raw.get("line", "")).isdigit() else None
    it["line_end"] = it["line"]
    it["state"] = "missing"
    pos = None
    if str(review.get("mode", "")).lower() == "check":
        it["state"] = "check"       # a reading of a source, not a change: there is no passage to find
    elif not path.exists():
        problems.append("%s: file not found: %s" % (iid, rel))
    else:
        if rel not in docs:
            doc = lib.Doc(path)
            docs[rel] = (doc, outline(doc.text))
        doc, heads = docs[rel]
        before, after = lib.compose(it)
        hits_after = lib.live_hits(doc.text, after) if after else []
        hits_before = lib.live_hits(doc.text, before)
        hits_second = []
        if second_text.strip() and not hits_after and not hits_before:      # the second agent's wording may be what was applied
            hits_second = lib.live_hits(doc.text, lib.compose(it, second_text)[1])
        if len(hits_after) == 1:
            it["state"], span = "in_text", hits_after[0]
        elif len(hits_before) == 1:
            it["state"], span = "proposed", hits_before[0]
        elif len(hits_before) > 1 or len(hits_after) > 1:
            it["state"], span = "ambiguous", (hits_before or hits_after)[0]
            problems.append("%s: the passage occurs %d times in %s; quote more of it so it is unique"
                            % (iid, len(hits_before or hits_after), rel))
        elif len(hits_second) == 1:
            it["state"], span = "in_text", hits_second[0]
        else:
            span = None
            problems.append("%s: the passage was not found in %s (check the wording against the file)" % (iid, rel))
        if span:
            pos = span[0]
            it["line"] = lib.line_of(doc.text, span[0])
            it["line_end"] = lib.line_of(doc.text, max(span[0], span[1] - 1))
            it["context_before"], it["context_after"] = nearby(doc.text, span[0], span[1])
    chapter = chapters.get(rel)
    if chapters and not chapter and rel.endswith(".tex") and rel != "main.tex":
        it["tags"] = it["tags"] + ["not in the compiled PDF"]
    where = raw.get("where")
    if not where:
        parts = [chapter["label"] if chapter else rel]
        if pos is not None:
            parts += section_path(docs[rel][1], pos)
        where = u" \u203a ".join(parts)
    it["where"] = where
    group = raw.get("group")
    if group:
        it["group"], it["_group_label"] = str(group), None
    else:
        it["group"] = "file:" + rel
        it["_group_label"] = (u"%s \u00b7 %s" % (chapter["label"], short_title(chapter["title"]))) if chapter else rel
    blob = json.dumps([it["type"], op, rel, it["original"], it["revised"], it["anchor"],
                       it.get("position"), it.get("sep"), it["wrap"], it.get("delete_style")], ensure_ascii=True)
    it["hash"] = hashlib.sha1(blob.encode("ascii")).hexdigest()[:12]
    return it


# ------------------------------------------------------------------ Markdown

fenced = lib.fenced


def request_section(requests):
    """The requests behind the review, word for word, for the top of the Markdown list."""
    out = ["## Requests", ""]
    for req in requests["requests"]:
        said = ", ".join(x for x in (req.get("asked"), ("by " + req["by"]) if req.get("by") else "", req.get("source")) if x)
        out.append("**%s**%s" % (req["id"], " (%s)" % said if said else ""))
        out.append("")
        out += [("> " + line) if line.strip() else ">" for line in req["text"].split("\n")]
        out.append("")
    return out


def location(it):
    if not it["line"]:
        return "`%s`" % it["file"]
    if it["line_end"] and it["line_end"] != it["line"]:
        return "`%s` lines %d-%d" % (it["file"], it["line"], it["line_end"])
    return "`%s` line %d" % (it["file"], it["line"])


STATE_TEXT = {
    "in_text": "already in the text, tagged; rejecting it restores the original",
    "missing": "passage not found when this list was built",
    "ambiguous": "passage occurs more than once; not applied until it is made unique",
}


def check_markdown(data, requests):
    """The list for a 'mode: check' review: what was read, not what would change."""
    out = ["# %s" % data["title"], ""]
    if data["description"]:
        out += [data["description"], ""]
    out += ["%d items, built %s. Open `review.html` in this folder to check each one. "
            "Nothing here edits the dissertation." % (len(data["items"]), data["generated"][:16].replace("T", " ")), ""]
    if requests["requests"]:
        out += request_section(requests)
    group = None
    labels = dict((g["key"], g["label"]) for g in data["groups"])
    for it in data["items"]:
        if it["group"] != group:
            group = it["group"]
            out += ["## %s" % labels[group], ""]
        out += ["### %s" % it["id"], ""]
        out.append("- **Location:** %s, %s" % (it["where"], it.get("source_label") or it["file"]))
        out.append("- **Kind:** %s" % data["types"][it["type"]]["label"])
        if it["note"]:
            out.append("- **Note:** %s" % " ".join(it["note"].split()))
        out.append("")
        if it.get("image"):
            out += ["![%s](%s)" % (it["id"], it["image"]), ""]
        out += ["**%s**" % it.get("reading_label", "Reading"), "", fenced(it["revised"]), "",
                "**%s**" % it.get("original_label", "Original"), "", fenced(it["original"]), ""]
    return "\n".join(out).rstrip("\n") + "\n"


def second_label(second):
    """What the second agent's option does, in words."""
    return {"keep": "leave the passage as it is", "remove": "remove the passage",
            "reword": "another wording"}[second["action"]]


def markdown(data, counts, requests):
    if data.get("mode") == "check":
        return check_markdown(data, requests)
    out = ["# %s" % data["title"], ""]
    if data["description"]:
        out += [data["description"], ""]
    out += [
        "%d items, built %s. Open `review.html` in this folder to accept or reject each one. "
        "Nothing in the dissertation changes until the apply step is run with `--write`."
        % (len(data["items"]), data["generated"][:16].replace("T", " ")),
        "",
        "| Change type | Tag written around accepted text | Items |",
        "| --- | --- | ---: |",
    ]
    for key in sorted(counts, key=lambda k: -counts[k]):
        info = data["types"][key]
        tag = "`\\hang{%s start}` ... `\\hang{%s end}`" % (info["marker"], info["marker"]) if info["tagged"] else "none"
        out.append("| %s | %s | %d |" % (info["label"], tag, counts[key]))
    out.append("")
    if requests["requests"]:
        out += request_section(requests)
    look = data.get("second_look")
    if look:
        out += ["A second agent (%s%s) looked at %d of these %d items and disagreed on %d. "
                "Those entries show two options, from `%s`."
                % (look["by"], ", " + look["date"] if look["date"] else "", look["looked_at"], len(data["items"]),
                   look["disagrees"], lib.DISAGREEMENTS_NAME), ""]
    group = None
    labels = dict((g["key"], g["label"]) for g in data["groups"])
    for it in data["items"]:
        if it["group"] != group:
            group = it["group"]
            out += ["## %s" % labels[group], ""]
        head = "### %s" % it["id"]
        if it["title"]:
            head += u" \u00b7 %s" % it["title"]
        out += [head, ""]
        out.append("- **Location:** %s, %s" % (it["where"], location(it)))
        out.append("- **Change type:** %s" % data["types"][it["type"]]["label"])
        if it["id"] in requests["items"]:
            out.append("- **Request:** %s" % (", ".join(requests["items"][it["id"]]) or "none, nobody asked for this edit"))
        if it["state"] in STATE_TEXT:
            out.append("- **Status:** %s" % STATE_TEXT[it["state"]])
        out.append("- **Version:** `%s`" % it["hash"])
        second = it.get("second")
        if second:
            out.append("- **Two options:** a second agent (%s) disagrees: %s." % (second["by"], second_label(second)))
            if second["stale"]:
                out.append("- **Status of option B:** written against an earlier version of this item (`%s`)" % second["against"])
            if it["note"]:
                out.append("- **Why option A:** %s" % " ".join(it["note"].split()))
            out.append("- **Why option B:** %s" % " ".join(second["note"].split()))
        elif it["note"]:
            out.append("- **Why:** %s" % " ".join(it["note"].split()))
        out.append("")
        rep = it.get("repetition")
        if rep:
            out += ["**Repeated-text comparison**", "",
                    "- **Match:** " + rep.get("match", ""),
                    "- **Recommended action:** " + rep.get("action", ""), "",
                    "**Repeated wording**", "", fenced(rep.get("shared", "")), ""]
            for occurrence in rep.get("occurrences", []):
                out += ["**%s:** %s, %s" % (occurrence.get("label", "Occurrence"),
                        occurrence.get("where", ""), location(occurrence)), "",
                        fenced(occurrence.get("original", "")), ""]
        first = "Option A" if second else "Revised"
        if it["op"] == "insert":
            out += ["**Inserted %s**" % it["position"], "", fenced(it["anchor"]), "", "**%s**" % ("Option A" if second else "New text"), "", fenced(it["revised"]), ""]
        elif it["op"] == "delete":
            result = "*(kept, marked for deletion)*" if it["delete_style"] == "mark" else "*(removed)*"
            out += ["**Original**", "", fenced(it["original"]), "", "**%s** %s" % (first, result), ""]
        else:
            out += ["**Original**", "", fenced(it["original"]), "", "**%s**" % first, "", fenced(it["revised"]), ""]
        if second and second["action"] == "reword":
            out += ["**Option B**", "", fenced(second["revised"]), ""]
        elif second:
            out += ["**Option B** *(%s)*" % second_label(second), ""]
    return "\n".join(out).rstrip("\n") + "\n"


# ------------------------------------------------------------------ main

def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description="Build a review folder (page, Markdown list, data) from its items.")
    ap.add_argument("folder", help="the review folder, e.g. waiting_for_review/pronoun-check")
    ap.add_argument("--root", help="dissertation folder (default: the nearest folder above that holds main.tex)")
    args = ap.parse_args()

    folder = Path(args.folder).resolve()
    if not folder.is_dir():
        raise SystemExit("Not a folder: %s" % folder)
    if folder == KIT:
        raise SystemExit("That is the template folder. Build a review folder next to it instead.")
    review, raw_items = load_items(folder)
    if args.root:
        root = Path(args.root).resolve()
    elif review.get("root"):
        root = (folder / review["root"]).resolve()
    else:
        root = find_root(folder)
    review_id = str(review.get("review_id") or folder.name)
    if not re.match(r"^[A-Za-z0-9][A-Za-z0-9._-]*$", review_id):
        raise SystemExit("The review id (the folder name) may only contain letters, digits, '.', '_' and '-': %s" % review_id)

    chapters, labels = chapter_map(root)
    docs, problems, items, seen = {}, [], [], set()
    reviewer, disagreeing = read_disagreements(folder)
    second_text = dict((rec["id"], rec.get("revised") or "") for rec in disagreeing)
    for raw in raw_items:
        it = enrich(raw, review, root, docs, chapters, problems, second_text.get(str(raw.get("id", "")).strip(), ""))
        if it["id"] in seen:
            raise SystemExit("Two items share the id %s" % it["id"])
        seen.add(it["id"])
        items.append(it)
    requests = resolve_requests(review, raw_items, review_id, problems)
    second_look = attach_disagreements(reviewer, disagreeing, review, items, problems)

    # Groups: the ones declared in the items file first, then chapters in order.
    group_label, order = {}, []
    for key, label in dotted(review, "group"):
        group_label[key] = label
        order.append(key)
    for rel in chapters:
        order.append("file:" + rel)
    for it in items:
        if it["group"] not in order:
            order.append(it["group"])
        if it["group"] not in group_label:
            group_label[it["group"]] = it["_group_label"] or it["group"]
        del it["_group_label"]
    if str(review.get("sort", "yes")).lower() not in NO:
        items.sort(key=lambda it: order.index(it["group"]))
    used = []
    for it in items:
        if it["group"] not in used:
            used.append(it["group"])

    type_label = dict(dotted(review, "type"))
    types, counts = {}, {}
    for it in items:
        counts[it["type"]] = counts.get(it["type"], 0) + 1
        info = types.setdefault(it["type"], {
            "label": type_label.get(it["type"]) or it["type"],
            "marker": it.get("marker") or it["type"],
            "tagged": False,
        })
        removed = it["op"] == "delete" and it["delete_style"] == "remove"
        info["tagged"] = info["tagged"] or (bool(it["wrap"][0]) and not removed)

    # The command shown on the page, as typed from the dissertation folder.
    base = find_root(KIT)

    def rel(path):
        return os.path.relpath(str(path), str(base)).replace("\\", "/")

    data = {
        "schema": "review-data/1",
        "review_id": review_id,
        "title": review.get("title") or review_id.replace("-", " ").replace("_", " ").capitalize(),
        "description": review.get("description") or "",
        "generated": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
        "root": os.path.relpath(str(root), str(folder)).replace("\\", "/"),
        "folder": str(folder),
        "apply_command": "python %s %s" % (rel(KIT / "apply_decisions.py"), rel(folder)),
        "types": types,
        "groups": [{"key": k, "label": group_label[k]} for k in used],
        "macros": dict(dotted(review, "macro")),
        "labels": labels,
        "items": items,
    }
    if review.get("mode"):
        data["mode"] = str(review["mode"]).lower()
    if second_look:
        data["second_look"] = second_look
    lib.write_js(folder / lib.DATA_NAME, lib.DATA_PREFIX, data,
                 "Written by build_review.py. Do not edit: change items.txt and build again.")
    lib.write_text(folder / lib.MD_NAME, markdown(data, counts, requests))
    lib.write_text(folder / lib.REQUESTS_NAME, json.dumps(requests, ensure_ascii=False, indent=1) + "\n")
    shutil.copyfile(str(KIT / lib.PAGE_NAME), str(folder / lib.PAGE_NAME))
    if not (folder / lib.APPLIED_NAME).exists():
        lib.write_js(folder / lib.APPLIED_NAME, lib.APPLIED_PREFIX,
                     {"review_id": review_id, "applied": {}, "batches": {}},
                     "Written by apply_decisions.py: which decisions are already in the dissertation.")

    states = {}
    for it in items:
        states[it["state"]] = states.get(it["state"], 0) + 1
    print("%s: %d items (%s)" % (review_id, len(items),
                                 ", ".join("%d %s" % (n, k) for k, n in sorted(counts.items()))))
    print("  not applied yet: %d   already in the text: %d   not found: %d   not unique: %d"
          % (states.get("proposed", 0), states.get("in_text", 0), states.get("missing", 0), states.get("ambiguous", 0)))
    if requests["requests"]:
        tally = ["%s (%d)" % (req["id"], sum(1 for ids in requests["items"].values() if req["id"] in ids))
                 for req in requests["requests"]]
        unasked = sum(1 for ids in requests["items"].values() if not ids)
        print("  items per request: %s%s" % (", ".join(tally), ", none (%d)" % unasked if unasked else ""))
    if second_look:
        print("  second agent: %s looked at %d of %d items and disagreed on %d"
              % (second_look["by"], second_look["looked_at"], len(items), second_look["disagrees"]))
    print("  dissertation root: %s" % root)
    for name in (lib.PAGE_NAME, lib.MD_NAME, lib.DATA_NAME, lib.REQUESTS_NAME):
        print("  wrote %s" % (folder / name))
    if problems:
        print("")
        print("Needs attention (%d):" % len(problems))
        for p in problems:
            print("  ! " + p)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
