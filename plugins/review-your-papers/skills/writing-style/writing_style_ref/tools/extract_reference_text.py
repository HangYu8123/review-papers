"""Extract the text of the reference dissertations for the technical vocabulary.

Run from the dissertation folder:  python writing_style_ref/tools/extract_reference_text.py
Add --group committee or --group lab to extract one group only.
It needs pdftotext (Poppler); Git for Windows ships one in mingw64/bin. The output, one
marked block per PDF page, is what build_vocabulary.py reads, so the PDFs are needed only
to extract the text again.

The committee dissertations (Short, Vázquez, Bobu) are read from dessertation_reference/ in the
dissertation folder, and their text goes to sources/reference-dissertations/. The recent lab
dissertations are read from vocab_corpus.LAB_DIR (the repository's dissertation_reference/, or
VOCAB_LAB_DISSERTATIONS), and their text goes to its text/ folder, outside the plugin, since
those dissertations are not redistributed with it. Each group's pdf-hashes.json records the
SHA-256 and page count of every PDF. A PDF that is missing is skipped and its text is kept.
The same command produced committee_style_ref/sources/text/, which this does not depend on.
"""

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import vocab_corpus as vc  # noqa: E402

HERE = vc.HERE
ROOT = HERE.parent
# Git's Xpdf first: the vocabulary counts were made with it, and Poppler may be first on PATH.
CANDIDATES = [r'C:\Program Files\Git\mingw64\bin\pdftotext.exe', 'pdftotext']


def find_pdftotext():
    for c in CANDIDATES:
        p = shutil.which(c)
        if p:
            return p
        if Path(c).exists():
            return c
    sys.exit('pdftotext was not found. Install Poppler or run this from Git Bash.')


def write(path, text):
    with open(str(path), 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)


def pdf_path(ref):
    return (ROOT if ref['group'] == 'committee' else vc.LAB_DIR) / ref['pdf']


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--group', choices=sorted(vc.REFERENCE_GROUPS), help='extract one group only')
    args = ap.parse_args()
    exe = find_pdftotext()
    for group in vc.REFERENCE_GROUPS:
        if args.group and group != args.group:
            continue
        out = vc.REFERENCE_TEXT if group == 'committee' else vc.LAB_TEXT
        out.mkdir(parents=True, exist_ok=True)
        hash_file = out / 'pdf-hashes.json'
        hashes = json.loads(hash_file.read_text(encoding='utf-8')) if hash_file.exists() else {}
        for name, ref in vc.REFERENCES.items():
            if ref['group'] != group:
                continue
            pdf = pdf_path(ref)
            if not pdf.exists():
                print('%-10s PDF not found, text kept: %s' % (name, pdf))
                continue
            with tempfile.TemporaryDirectory() as tmp:
                raw = Path(tmp) / 'raw.txt'
                subprocess.run([exe, '-enc', 'UTF-8', str(pdf), str(raw)], check=True, stderr=subprocess.DEVNULL)
                pages = raw.read_bytes().decode('utf-8', errors='replace').split('\f')
            if pages and not pages[-1].strip():
                pages.pop()
            lines = []
            for i, page in enumerate(pages, 1):
                lines.append('[[page %d]]' % i)
                lines.extend(page.replace('\r', '').rstrip('\n').split('\n'))
            write(out / (ref['key'] + '.txt'), vc.repair_text(name, '\n'.join(lines) + '\n'))
            hashes[ref['key']] = {'file': ref['pdf'], 'sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
                                  'pages': len(pages)}
            print('%-10s %3d pages' % (name, len(pages)))
        write(hash_file, json.dumps(hashes, indent=2) + '\n')


if __name__ == '__main__':
    main()
