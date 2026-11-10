#!/usr/bin/env python3
"""Figure helper for the paper self-review coach.

Two modes:

  figures.py inventory PAPER [--out DIR]
      List the figures (and tables) in a paper with their captions, page (PDF)
      or image files (LaTeX), and how many times the text refers to each.
      For PDFs, renders every page that holds a figure to DIR/page-NN.png so
      the coach can look at it.

  figures.py simulate IMAGE [--out FILE]
      Make one comparison panel: original, deuteranopia, protanopia,
      tritanopia (Machado et al. 2009, full severity) and grayscale. Useful for
      the *student* to look at and judge whether their colors still separate.
"""
import argparse, re, subprocess, sys
from pathlib import Path

# Numbers such as 3, 4.1 (numbered within a chapter or section), and A.3 (appendices)
CAP = re.compile(r"^\s*(Figure|Fig\.|Table)\s+([A-Z]?\.?\d+(?:\.\d+)*)\s*[:.](?!\d)\s*(.*)", re.I)


def pdf_pages(path):
    out = subprocess.run(["pdfinfo", str(path)], capture_output=True, text=True).stdout
    m = re.search(r"Pages:\s+(\d+)", out)
    return int(m.group(1)) if m else 0


sys.path.insert(0, str(Path(__file__).parent))
from structure_scan import pdf_text  # column-aware extraction


def page_text(path, p):
    return pdf_text(Path(path), page=p, keep_small=True)


def inventory_pdf(path, out):
    out.mkdir(parents=True, exist_ok=True)
    n = pdf_pages(path)
    texts = {p: page_text(path, p) for p in range(1, n + 1)}
    full = "\n".join(texts.values())
    items = []
    for p, t in texts.items():
        lines = t.splitlines()
        for i, line in enumerate(lines):
            m = CAP.match(line)
            if not m:
                continue
            # caption continues until a blank line
            cap = [m.group(3)] if m.group(3).strip() else []
            rest = lines[i + 1:]
            if not cap:  # IEEE style: "Fig. 1." on its own line, caption after a blank
                while rest and not rest[0].strip():
                    rest = rest[1:]
            for nxt in rest:
                if not nxt.strip():
                    break
                cap.append(nxt.strip())
            kind = "Table" if m.group(1).lower().startswith("tab") else "Figure"
            items.append({"kind": kind, "num": m.group(2).upper(), "page": p,
                          "caption": " ".join(cap)})
    seen, uniq = set(), []
    for it in items:
        k = (it["kind"], it["num"])
        if k not in seen:
            seen.add(k); uniq.append(it)
    for it in uniq:
        num = re.escape(it["num"]) + r"(?!\.?\d)"  # Figure 4 does not count Figure 4.1
        if it["kind"] == "Figure":
            pat = r"\b(Figure|Fig\.)\s*" + num
        else:
            pat = r"\bTable\s*" + num
        it["text_refs"] = max(0, len(re.findall(pat, full, re.I)) - 1)  # minus caption
    pages = sorted({it["page"] for it in uniq})
    for p in pages:
        subprocess.run(["pdftoppm", "-f", str(p), "-l", str(p), "-r", "110", "-png",
                        "-singlefile", str(path), str(out / f"page-{p:02d}")])
    return uniq, [out / f"page-{p:02d}.png" for p in pages]


def inventory_tex(path):
    t = path.read_text(encoding="utf-8", errors="replace")
    t = re.sub(r"(?<!\\)%.*", "", t)
    items = []
    for k, m in enumerate(re.finditer(r"\\begin\{(figure\*?|table\*?)\}(.*?)\\end\{\1\}", t, re.S), 1):
        body = m.group(2)
        cap = re.search(r"\\caption(?:\[[^\]]*\])?\{((?:[^{}]|\{[^{}]*\})*)\}", body)
        labels = re.findall(r"\\label\{([^}]*)\}", body)
        imgs = re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}", body)
        refs = sum(len(re.findall(r"\\(?:auto|c|C)?ref\{%s\}" % re.escape(l), t)) for l in labels)
        files = []
        for im in imgs:
            cands = [path.parent / im] + [path.parent / (im + e) for e in (".pdf", ".png", ".jpg", ".jpeg", ".eps")]
            hit = next((c for c in cands if c.exists()), None)
            files.append(str(hit) if hit else im + " (not found next to .tex)")
        items.append({"kind": "Table" if m.group(1).startswith("table") else "Figure",
                      "num": k, "labels": labels, "caption": cap.group(1) if cap else "(no caption)",
                      "images": files, "text_refs": refs})
    return items


# Machado, Oliveira & Fernandes (2009), severity 1.0, applied in linear RGB.
CVD = {
    "deuteranopia": [[0.367322, 0.860646, -0.227968], [0.280085, 0.672501, 0.047413], [-0.011820, 0.042940, 0.968881]],
    "protanopia":   [[0.152286, 1.052583, -0.204868], [0.114503, 0.786281, 0.099216], [-0.003882, -0.048116, 1.051998]],
    "tritanopia":   [[1.255528, -0.076749, -0.178779], [-0.078411, 0.930809, 0.147602], [0.004733, 0.691367, 0.303900]],
}


def simulate(img_path, out_path):
    import numpy as np
    from PIL import Image, ImageDraw
    if str(img_path).lower().endswith(".pdf"):
        tmp = Path(out_path).with_suffix("")
        subprocess.run(["pdftoppm", "-r", "150", "-png", "-singlefile", str(img_path), str(tmp)])
        img_path = str(tmp) + ".png"
    im = Image.open(img_path).convert("RGB")
    if im.width > 900:
        im = im.resize((900, int(im.height * 900 / im.width)))
    a = np.asarray(im).astype(np.float64) / 255
    lin = np.where(a <= 0.04045, a / 12.92, ((a + 0.055) / 1.055) ** 2.4)
    panels = [("original", im)]
    for name, M in CVD.items():
        s = np.clip(lin @ np.array(M).T, 0, 1)
        srgb = np.where(s <= 0.0031308, s * 12.92, 1.055 * s ** (1 / 2.4) - 0.055)
        panels.append((name, Image.fromarray((srgb * 255).round().astype("uint8"))))
    panels.append(("grayscale", im.convert("L").convert("RGB")))
    w, h, pad = im.width, im.height, 28
    cols = 2
    rows = (len(panels) + 1) // cols
    sheet = Image.new("RGB", (cols * w, rows * (h + pad)), "white")
    d = ImageDraw.Draw(sheet)
    try:
        from PIL import ImageFont
        font = ImageFont.load_default(size=20)
    except Exception:
        font = None
    for i, (name, p) in enumerate(panels):
        x, y = (i % cols) * w, (i // cols) * (h + pad)
        d.text((x + 8, y + 3), name, fill="black", font=font)
        sheet.paste(p, (x, y + pad))
    sheet.save(out_path)
    return out_path


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    a1 = sub.add_parser("inventory"); a1.add_argument("paper"); a1.add_argument("--out", default="figure_pages")
    a2 = sub.add_parser("simulate"); a2.add_argument("image"); a2.add_argument("--out", default=None)
    a = ap.parse_args()
    if a.cmd == "inventory":
        p = Path(a.paper)
        if p.suffix.lower() == ".pdf":
            items, pages = inventory_pdf(p, Path(a.out))
        elif p.suffix.lower() == ".tex":
            items, pages = inventory_tex(p), []
        else:
            sys.exit("inventory supports .pdf and .tex; for other formats ask the student for the figure files")
        for it in items:
            where = f"p.{it['page']}" if "page" in it else ", ".join(it.get("images", [])) or "-"
            print(f"{it['kind']} {it['num']} [{where}] referenced in text {it['text_refs']}x")
            print(f"    caption: {it['caption'][:300]}")
        if pages:
            print("\nRendered pages:", *map(str, pages), sep="\n  ")
    else:
        out = a.out or str(Path(a.image).with_suffix("")) + "_colorvision.png"
        print(simulate(a.image, out))
