#!/usr/bin/env python3
"""Heuristic structure scan of a paper draft, for the coach's use.

Reports per-section word counts, paragraph and sentence statistics, length
outliers (long sentences, long paragraphs, short paragraphs), and matches for
the advisor's style "pet peeves". Accepts .tex, .md, .txt, .pdf, .docx.

Usage: structure_scan.py PAPER [--json] [--long-sentence N] [--long-para N]
"""
import argparse, json, re, subprocess, sys
from pathlib import Path

LONG_SENTENCE = 40   # words
LONG_PARA = 200      # words
SHORT_PARA_SENTS = 2 # sentences or fewer

KNOWN_SECTIONS = [
    "abstract", "introduction", "background", "related work", "algorithm",
    "approach", "method", "methods", "methodology", "validation", "system design",
    "data collection", "experimental design", "experiment", "experiments",
    "study design", "evaluation", "results", "discussion", "conclusion",
    "conclusions", "limitations", "future work", "acknowledgments", "acknowledgment",
    "acknowledgements", "references", "appendix",
]

PET_PEEVES = [
    (r"\butili[sz](e|es|ed|ing|ation)\b", "'utilize' (advisor prefers 'use')"),
    (r"\bin order to\b", "'in order to' (could be 'to')"),
    (r"\b(clearly|definitely|extremely|very|obviously)\b", "intensifier adverb"),
    (r"\b(simple|minor|small)\s+(contribution|approach|method|change|extension|modification)", "possibly disparaging own work"),
    (r"\b(some|several|many|these|other|prior|previous|recent|existing)\s+works\b", "'works' meaning papers"),
    (r"(^|(?<!\bal)[.;:]\s+)\[\d+(?:[,\u2013-]\s*\d+)*\]\s+(show|shows|showed|demonstrate|demonstrated|propose|proposed|found|present|presented|use|used|address|addressed)", "numeric citation used as a noun"),
    (r"\\cite[pt]?\{[^}]*\}\s+(show|shows|showed|demonstrate|demonstrated|propose|proposed|found|present|presented|address|addressed)\b", "citation possibly used as a noun"),
    (r"\b(robot|participant|participants|agent|system|user|users)\s+would\b", "'would' describing what happened"),
    (r"\b(he or she|he/she|his or her|his/her|s/he)\b", "gendered pronoun construction (advisor prefers singular 'they')"),
]
PASSIVE = re.compile(r"\b(is|are|was|were|be|been|being)\s+(\w+ly\s+)?\w+(ed|en)\b", re.I)
FIRST_PERSON = re.compile(r"\bwe\b", re.I)


def read_text(path: Path) -> tuple[str, str]:
    suf = path.suffix.lower()
    if suf == ".pdf":
        return pdf_text(path), "pdf"
    if suf == ".docx":
        try:
            import docx  # type: ignore
            d = docx.Document(str(path))
            parts = []
            for p in d.paragraphs:
                style = (p.style.name or "").lower()
                if style.startswith("heading"):
                    parts.append("\n## " + p.text.strip() + "\n")
                else:
                    parts.append(p.text)
            return "\n\n".join(parts), "md"
        except ImportError:
            out = subprocess.run(["pandoc", str(path), "-t", "markdown"], capture_output=True, text=True)
            return out.stdout, "md"
    txt = path.read_text(encoding="utf-8", errors="replace")
    if suf == ".tex":
        return txt, "tex"
    if suf in (".md", ".markdown"):
        return txt, "md"
    return txt, "txt"


def pdf_text(path: Path, page: int | None = None, keep_small: bool = False) -> str:
    """Extract PDF text in reading order with paragraph breaks.

    Uses pdftotext's word bounding boxes so that (1) two-column templates
    (IEEE/ACM) are read left column then right column instead of interleaved,
    and (2) paragraph breaks are recovered from first-line indents and
    vertical gaps, which plain pdftotext output loses.
    """
    import html
    rng = ["-f", str(page), "-l", str(page)] if page else []
    res = subprocess.run(["pdftotext", *rng, "-bbox-layout", str(path), "-"], capture_output=True, text=True)
    if res.returncode != 0 or "<page" not in res.stdout:
        # Git for Windows ships Xpdf's pdftotext, which has no -bbox-layout and exits with its usage text.
        sys.exit(f"pdftotext -bbox-layout failed on {path} (exit {res.returncode}). The scan needs Poppler's "
                 "pdftotext, such as the one in MiKTeX or in conda's poppler package, first on PATH.")
    bb = res.stdout
    out_pages = []
    for page in re.findall(r"<page (.*?)</page>", bb, re.S):
        m = re.match(r'width="([\d.]+)" height="([\d.]+)"', page)
        w, h = float(m.group(1)), float(m.group(2))
        lines = []
        for lm in re.finditer(r'<line xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</line>', page, re.S):
            words = [html.unescape(x) for x in re.findall(r"<word[^>]*>(.*?)</word>", lm.group(5), re.S)]
            text = " ".join(words).strip()
            y0 = float(lm.group(2))
            if not text or (re.fullmatch(r"\d{1,4}", text) and y0 > 0.85 * h) or text.startswith("Authorized licensed use limited to"):
                continue
            lines.append([float(lm.group(1)), float(lm.group(2)), float(lm.group(3)), float(lm.group(4)), text])
        if not lines:
            continue
        mid = w / 2
        cross = [l for l in lines if l[0] < mid - 5 and l[2] > mid + 5]
        two_col = len(cross) / len(lines) < 0.15
        if two_col:
            colines = [l for l in lines if not (l[0] < mid - 5 and l[2] > mid + 5)]
            right = [l for l in colines if l[0] >= mid - 5]
            top = min(l[1] for l in right) if right else (min(l[1] for l in colines) if colines else 0)
            head = sorted([l for l in cross if l[1] < top], key=lambda l: l[1])
            rest = sorted([l for l in cross if l[1] >= top], key=lambda l: l[1])
            cols = [head,
                    sorted([l for l in colines if l[2] <= mid + 5], key=lambda l: (l[1], l[0])),
                    sorted([l for l in colines if l[0] >= mid - 5 and l[2] > mid + 5], key=lambda l: (l[1], l[0])),
                    rest]
        else:
            cols = [sorted(lines, key=lambda l: (l[1], l[0]))]
        hs = sorted(l[3] - l[1] for l in lines)
        body_h = hs[len(hs) // 2]
        page_parts = []
        for col in cols:
            # drop small-print lines (footnotes, captions, affiliations, table cells)
            if not keep_small:
                col = [l for l in col if (l[3] - l[1]) >= 0.85 * body_h]
            if not col:
                continue
            xs = sorted(round(l[0]) for l in col)
            margin = max(set(xs), key=xs.count)
            gaps = [b[1] - a[3] for a, b in zip(col, col[1:]) if 0 <= b[1] - a[3] < 20]
            gaps.sort()
            med = gaps[len(gaps) // 2] if gaps else 2
            buf = []
            prev = None
            for l in col:
                brk = prev is None or (l[1] - prev[3]) > med + 3 or l[0] > margin + 4 or l[1] < prev[1]
                if brk and buf:
                    buf.append("")
                buf.append(l[4])
                prev = l
            page_parts.append("\n".join(buf))
        out_pages.append("\n\n".join(page_parts))
    return "\n\n".join(out_pages)


ROMAN = re.compile(r"^(I|II|III|IV|V|VI|VII|VIII|IX|X)\.\s+([A-Z])\s?([A-Z][A-Z \-]*)$")
LETTER_SUB = re.compile(r"^([A-H])\.\s+([A-Z][\w\-]*(?:[ ,:\-]+[\w\-]+){0,8})$")


def clean_tex(t: str) -> str:
    t = re.sub(r"(?<!\\)%.*", "", t)
    m = re.search(r"\\begin\{document\}", t)
    if m:
        t = t[m.end():]
    t = re.sub(r"\\end\{document\}.*", "", t, flags=re.S)
    for env in ["figure", "figure\\*", "table", "table\\*", "algorithm", "algorithmic",
                "equation", "equation\\*", "align", "align\\*", "tabular", "comment"]:
        t = re.sub(r"\\begin\{%s\}.*?\\end\{%s\}" % (env, env), "\n\n", t, flags=re.S)
    t = re.sub(r"\\(sub)*section\*?\{([^}]*)\}", lambda m: "\n\n#" + ("#" * m.group(0).count("sub")) + " " + m.group(2) + "\n\n", t)
    t = re.sub(r"\\paragraph\*?\{([^}]*)\}", r"\n\n\1. ", t)
    t = re.sub(r"\\(cite[pt]?|citeauthor|mycite)\{[^}]*\}", "[CIT]", t)
    t = re.sub(r"\\(ref|eqref|autoref|cref|Cref|label)\{[^}]*\}", "X", t)
    t = re.sub(r"\\(textbf|textit|emph|texttt|underline|textsc)\{([^}]*)\}", r"\2", t)
    t = re.sub(r"\\item\s*", "\n\n- ", t)
    t = re.sub(r"\\begin\{[^}]*\}|\\end\{[^}]*\}", "\n\n", t)
    t = re.sub(r"\$[^$]*\$", "X", t)
    t = re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?(\{[^}]*\})?", " ", t)
    t = t.replace("~", " ").replace("``", '"').replace("''", '"')
    return t


def heading_of(line: str, mode: str):
    s = line.strip()
    if s.isupper():
        s = re.sub(r"\b([A-Z]) (?=[A-Z]{2,}\b)", r"\1", s)  # small caps split: "R ESULTS"
    m = re.match(r"^(#{1,6})\s+(.+)$", s)
    if m:
        return len(m.group(1)), m.group(2).strip()
    if mode in ("pdf", "txt"):
        m = ROMAN.match(s)
        if m:
            return 1, f"{m.group(1)}. {(m.group(2) + m.group(3)).title()}"
        if heading_of.roman_doc:
            m = LETTER_SUB.match(s)
            if m and not s.endswith((",", ";")):
                return 2, s
        m = re.match(r"^(\d+(?:\.\d+)*)\.?\s+([A-Z][^.]{1,70})$", s)
        if heading_of.roman_doc:
            m = None  # IEEE-style docs: numbered lines are footnotes/affiliations
        if m and len(m.group(2).split()) <= 9 and not s.endswith((",", ";")):
            return m.group(1).count(".") + 1, f"{m.group(1)} {m.group(2)}"
        low = s.lower().rstrip(":")
        if low in KNOWN_SECTIONS or (low.startswith("appendix") and len(s.split()) <= 12
                                     and not re.search(r"\)\.?\s|\.$", s)):
            return 1, s
    return None


heading_of.roman_doc = False


FUNCTION_WORDS = {"the", "of", "and", "to", "in", "a", "is", "that", "for", "with", "on", "as", "by",
                  "are", "was", "were", "this", "from", "an", "be", "or", "not", "which", "than", "each"}


def is_pdf_artifact(p: str) -> bool:
    """Text that a PDF puts between paragraphs: running heads, contents leaders, reference entries, table cells."""
    words = p.split()
    if re.search(r"(?:\.\s?){5,}", p):        # leaders in a table of contents or list of figures
        return True
    if p.isupper() and len(words) < 15:         # running heads such as "CHAPTER 3. METHOD"
        return True
    if re.match(r"^\[\d+\]\s+[A-Z]", p):       # an entry of a reference list
        return True
    # Table cells, axis ticks, code, and equations have few words and almost no function words.
    # A results paragraph full of statistics still has its "the", "of", and "and".
    prose = sum(1 for w in words if re.fullmatch(r"[(\"\u201c]?[A-Za-z][a-z'\u2019-]+[.,;:)\"\u201d]*", w))
    glue = sum(1 for w in words if w.lower().strip(".,;:()") in FUNCTION_WORDS)
    return prose < 0.4 * len(words) and glue < 0.1 * len(words)


def split_paragraphs(body: str, mode: str):
    if mode == "pdf":
        # pdftotext separates paragraphs inconsistently; use blank lines and
        # lines ending a sentence followed by an indented/capitalized start.
        body = re.sub(r"-\n(?=[a-z])", "", body)
    paras = [re.sub(r"\s+", " ", p).strip() for p in re.split(r"\n\s*\n", body)]
    if mode == "pdf":
        # a paragraph that starts lowercase continues across a column or page break
        merged = []
        for p in paras:
            if merged and p[:1].islower():
                merged[-1] += " " + p
            else:
                merged.append(p)
        paras = merged
    return [p for p in paras if len(p.split()) >= 4 and not re.fullmatch(r"[\d\s.]+", p)
            and not re.match(r"^(Figure|Fig\.|Table|Algorithm)\s+[A-Z]?\.?\d+(\.\d+)*[:.]", p)
            and not (mode == "pdf" and is_pdf_artifact(p))
            and not (mode == "pdf" and len(p.split()) < 15 and re.search(
                r"@|^\*?\d+\s*Corresponding|^\*This work|^\d+\s*\D*(University|Institute|College|School|Department|Laborator)", p))]


SENT_SPLIT = re.compile(r"(?<!\bet al\.)(?<!\be\.g\.)(?<!\bi\.e\.)(?<!\bvs\.)(?<!\bFig\.)(?<!\bEq\.)(?<!\bSec\.)(?<=[.!?])[\"')\]]?\s+(?=[A-Z\[\"(])")


def sentences(p: str):
    return [s.strip() for s in SENT_SPLIT.split(p) if s.strip()]


def wc(s: str) -> int:
    return len(re.findall(r"[A-Za-z0-9][\w'\-]*", s))


def snippet(s: str, n=10) -> str:
    w = s.split()
    return " ".join(w[:n]) + (" …" if len(w) > n else "")


def scan(path: Path, long_sent: int, long_para: int):
    raw, mode = read_text(path)
    if mode == "tex":
        raw = clean_tex(raw)
        mode = "md"
    sections, cur = [], {"level": 1, "title": "(front matter)", "lines": []}
    lines = raw.splitlines()
    heading_of.roman_doc = mode in ("pdf", "txt") and sum(bool(ROMAN.match(l.strip())) for l in lines) >= 2
    if mode in ("pdf", "txt"):
        # pdftotext sometimes puts a section number alone on its own line
        merged, i = [], 0
        while i < len(lines):
            if re.fullmatch(r"\s*\d+(\.\d+)*\s*", lines[i]) and i + 2 < len(lines):
                j = i + 1
                while j < len(lines) and not lines[j].strip():
                    j += 1
                if j < len(lines) and heading_of(lines[i].strip() + " " + lines[j].strip(), mode):
                    merged.append(lines[i].strip() + " " + lines[j].strip()); i = j + 1; continue
            merged.append(lines[i]); i += 1
        lines = merged
    last_num = 0
    for line in lines:
        h = heading_of(line, mode)
        if h and mode in ("pdf", "txt"):
            m = re.match(r"^(\d+)", h[1])
            if m:
                n = int(m.group(1))
                # numbered headings must follow in sequence; anything else is a
                # table cell, footnote, or page number that looks like a heading
                if not (n == last_num or n == last_num + 1):
                    h = None
                else:
                    last_num = n
        if h and mode == "pdf" and h[0] == cur["level"] and h[1] == cur["title"]:
            continue  # a PDF running head repeats the current heading
        if h:
            sections.append(cur)
            cur = {"level": h[0], "title": h[1], "lines": []}
        else:
            cur["lines"].append(line)
    sections.append(cur)

    report = []
    in_refs = False
    for sec in sections:
        tl = sec["title"].lower().strip(" .0123456789ivx")
        if tl in ("references", "bibliography", "works cited"):
            in_refs = True
        elif sec["level"] == 1 and tl and not tl.startswith("appendix"):
            pass
        if in_refs and not tl.startswith("appendix"):
            continue  # reference list: not prose
        in_refs = False
        paras = split_paragraphs("\n".join(sec["lines"]), mode)
        if not paras:
            if sec["title"] != "(front matter)":
                report.append({"section": sec["title"], "level": sec["level"], "words": 0,
                               "paragraphs": 0, "mean_para_words": 0, "first_paragraph": "",
                               "paragraphs_detail": [], "flags": []})
            continue
        title_low = sec["title"].lower()
        is_algo = any(k in title_low for k in ("algorithm", "approach", "formulation", "preliminar"))
        is_intro = "introduction" in title_low
        pinfo, flags = [], []
        for i, p in enumerate(paras, 1):
            ss = sentences(p)
            w = wc(p)
            pinfo.append({"n": i, "words": w, "sentences": len(ss), "start": snippet(p)})
            if w > long_para:
                flags.append({"type": "long_paragraph", "para": i, "words": w, "start": snippet(p)})
            # In extracted text, a fragment without end punctuation is a heading, label, or list item.
            ends = mode not in ("pdf", "txt") or re.search(r"[.?!][\"'\u201d)\]]?$", p)
            if len(ss) <= SHORT_PARA_SENTS and not p.startswith("- ") and w < 60 and ends:
                flags.append({"type": "short_paragraph", "para": i, "sentences": len(ss), "words": w, "start": snippet(p)})
            for s in ss:
                sw = wc(s)
                if sw > long_sent:
                    flags.append({"type": "long_sentence", "para": i, "words": sw, "start": snippet(s, 14)})
                for pat, label in PET_PEEVES:
                    m = re.search(pat, s, re.I)
                    if m:
                        flags.append({"type": "style", "para": i, "pattern": label, "match": m.group(0).strip(), "sentence": snippet(s, 16)})
                if is_algo and re.match(r"^\s*we\b", s, re.I):
                    flags.append({"type": "style", "para": i, "pattern": "'we' as subject in algorithm section", "sentence": snippet(s, 16)})
                if is_intro and PASSIVE.search(s):
                    flags.append({"type": "style", "para": i, "pattern": "possible passive voice in intro", "match": PASSIVE.search(s).group(0), "sentence": snippet(s, 16)})
        words = [x["words"] for x in pinfo]
        report.append({
            "section": sec["title"], "level": sec["level"],
            "words": sum(words), "paragraphs": len(paras),
            "mean_para_words": round(sum(words) / len(words), 1),
            "first_paragraph": paras[0][:400],
            "paragraphs_detail": pinfo, "flags": flags,
        })
    return report


def print_human(report, pages=None):
    total = sum(s["words"] for s in report)
    if pages:
        print(f"PDF page count (including references/appendices): {pages}")
    print(f"Approximate total words: {total}  (single-column page ≈ 500–600 words; two-column ≈ 800–1000)\n")
    for s in report:
        ind = "  " * (s["level"] - 1)
        print(f"{ind}== {s['section']} — {s['words']} words, {s['paragraphs']} paragraphs (mean {s['mean_para_words']} words/para)")
        if s["first_paragraph"]:
            print(f"{ind}   opens: {snippet(s['first_paragraph'], 20)}")
        by = {}
        for f in s["flags"]:
            by.setdefault(f["type"], []).append(f)
        for t in ("long_paragraph", "short_paragraph", "long_sentence", "style"):
            for f in by.get(t, []):
                if t == "long_paragraph":
                    print(f"{ind}   [long paragraph] ¶{f['para']} {f['words']}w: \"{f['start']}\"")
                elif t == "short_paragraph":
                    print(f"{ind}   [short paragraph] ¶{f['para']} {f['sentences']} sent/{f['words']}w: \"{f['start']}\"")
                elif t == "long_sentence":
                    print(f"{ind}   [long sentence] ¶{f['para']} {f['words']}w: \"{f['start']}\"")
                else:
                    print(f"{ind}   [style: {f['pattern']}] ¶{f['para']}: \"{f['sentence']}\"")
        print()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("paper")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--long-sentence", type=int, default=LONG_SENTENCE)
    ap.add_argument("--long-para", type=int, default=LONG_PARA)
    a = ap.parse_args()
    rep = scan(Path(a.paper), a.long_sentence, a.long_para)
    if a.json:
        json.dump(rep, sys.stdout, indent=2)
    else:
        pages = None
        if a.paper.lower().endswith(".pdf"):
            info = subprocess.run(["pdfinfo", a.paper], capture_output=True, text=True).stdout
            m = re.search(r"Pages:\s+(\d+)", info)
            pages = int(m.group(1)) if m else None
        print_human(rep, pages)
