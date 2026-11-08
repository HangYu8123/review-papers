"""Helpers shared by build_review.py and apply_decisions.py.

Written for the Python on PATH here (3.8), so no newer syntax.
"""
import json
import re

DATA_NAME = "review-data.js"
DATA_PREFIX = "window.REVIEW_DATA = "
APPLIED_NAME = "review-applied.js"
APPLIED_PREFIX = "window.REVIEW_APPLIED = "
LOG_NAME = "applied-log.json"
PAGE_NAME = "review.html"
MD_NAME = "suggestions.md"
REQUESTS_NAME = "requests.json"
DISAGREEMENTS_NAME = "disagreements.txt"
RECORD_NAME = "change-record.json"
RECORD_MD_NAME = "change-record.md"


def read_requests(folder):
    """The requests of a review and which items address them. The page never reads this."""
    path = folder / REQUESTS_NAME
    if not path.exists():
        return {"requests": [], "items": {}}
    return json.loads(path.read_text(encoding="utf-8"))


def fenced(text):
    fence = "```"
    while fence in text:
        fence += "`"
    return "%slatex\n%s\n%s" % (fence, text, fence)


def read_js(path, prefix):
    """Read the JSON object assigned in a one-statement .js data file."""
    text = path.read_text(encoding="utf-8")
    start = text.index(prefix) + len(prefix)
    return json.loads(text[start:].rstrip().rstrip(";"))


def write_text(path, text):
    with open(str(path), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def write_js(path, prefix, obj, comment):
    # ASCII only, so the page reads it the same way whatever encoding the browser guesses.
    body = json.dumps(obj, ensure_ascii=True, indent=1)
    write_text(path, "// %s\n%s%s;\n" % (comment, prefix, body))


def decisions_pattern(review_id):
    """File name of one saved batch: <review id>.decisions.<YYYYMMDD-HHMMSS>.json"""
    return re.compile(r"^" + re.escape(review_id) + r"\.decisions\.(\d{8}-\d{6}(?:-\d+)?)\.json$")


def autosave_name(review_id):
    """The page's working copy: every decision, in a batch or not. Never applied."""
    return "%s.autosave.json" % review_id


class Doc(object):
    """A source file held as LF text and written back with its original line endings."""

    def __init__(self, path):
        self.path = path
        raw = path.read_bytes()
        self.crlf = b"\r\n" in raw
        self.text0 = raw.decode("utf-8").replace("\r\n", "\n")
        self.text = self.text0

    @property
    def changed(self):
        return self.text != self.text0

    def render(self):
        return self.text.replace("\n", "\r\n") if self.crlf else self.text


TAG = re.compile(r"(\\hang\{[^{}]*\})")


def find_all(hay, needle):
    """Spans where needle occurs, treating any run of whitespace as equal (a
    sentence quoted on one line may be wrapped in the file) and allowing a
    \\hang{...} tag to sit against its text with or without a space."""
    if not needle or not needle.strip():
        return []
    pieces = [r"\s+".join(re.escape(word) for word in piece.split()) for piece in TAG.split(needle) if piece.strip()]
    return [(m.start(), m.end()) for m in re.finditer(r"\s*".join(pieces), hay)]


def live_hits(hay, needle):
    """find_all without the hits that start on a commented-out line."""
    out = []
    for start, end in find_all(hay, needle):
        line_start = hay.rfind("\n", 0, start) + 1
        if not hay[line_start:start].lstrip().startswith("%"):
            out.append((start, end))
    return out


def line_of(hay, pos):
    return hay.count("\n", 0, pos) + 1


def compose(item, revised=None):
    """(original, accepted): the passage as it stands in the file before the change,
    and as it stands once the change is accepted, markers included."""
    wrap = item.get("wrap") or ["", ""]
    new = item.get("revised", "") if revised is None else revised
    op = item["op"]
    if op == "insert":
        anchor = item["anchor"]
        block = wrap[0] + new + wrap[1]
        sep = item.get("sep", "\n\n")
        if item.get("position") == "before":
            return anchor, block + sep + anchor
        return anchor, anchor + sep + block
    if op == "delete":
        original = item["original"]
        if new:                                 # the reviewer kept a shorter version instead
            return original, wrap[0] + new + wrap[1]
        if item.get("delete_style") == "mark":
            return original, wrap[0] + original + wrap[1]
        return original, ""
    if not new:                                 # a second agent's option to remove the passage
        return item["original"], ""
    return item["original"], wrap[0] + new + wrap[1]
