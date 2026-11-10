"""Extract the text of the three dissertations, one marked block per PDF page.

Run from the dissertation folder:

    python committee_style_ref/tools/extract_text.py

It needs the pdftotext that Git for Windows ships in mingw64/bin, which is
Xpdf 4.00, not Poppler. Xpdf writes each paragraph on one line, and the counts
in common.py keep only lines of 20 words or more, so Poppler's pdftotext gives
different measures (for Bobu, 7,772 words and a mean sentence of 15.9 words
instead of 32,861 and 22.8). The output goes to committee_style_ref/sources/text/
and is what the build and the validation read, so the PDFs are only needed when
the text is extracted again.
"""
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parent
PDF_DIR = ROOT / 'dessertation_reference'
PDFS = {
    'short': 'Short_2017_USC_thesis.pdf',
    'vazquez': 'Vazquez_2017_CMU_thesis.pdf',
    'bobu': 'Bobu_2023_Berkeley_EECS-2023-200.pdf',
}
# Git's Xpdf first: the counts depend on it (see the docstring), and Poppler may be first on PATH.
CANDIDATES = [r'C:\Program Files\Git\mingw64\bin\pdftotext.exe', 'pdftotext']


def find_pdftotext():
    for c in CANDIDATES:
        p = shutil.which(c)
        if p:
            return p
        if Path(c).exists():
            return c
    sys.exit('pdftotext was not found. Install Poppler or run this from Git Bash.')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(path, text):
    with open(str(path), 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)


def main():
    exe = find_pdftotext()
    out_dir = HERE / 'sources' / 'text'
    out_dir.mkdir(parents=True, exist_ok=True)
    hashes = {}
    for key, name in PDFS.items():
        pdf = PDF_DIR / name
        with tempfile.TemporaryDirectory() as tmp:
            raw = Path(tmp) / 'raw.txt'
            subprocess.run([exe, '-enc', 'UTF-8', str(pdf), str(raw)], check=True,
                           stderr=subprocess.DEVNULL)
            pages = raw.read_bytes().decode('utf-8', errors='replace').split('\f')
        if pages and not pages[-1].strip():
            pages.pop()
        lines = []
        for i, page in enumerate(pages, 1):
            lines.append('[[page %d]]' % i)
            lines.extend(page.replace('\r', '').rstrip('\n').split('\n'))
        write(out_dir / (key + '.txt'), '\n'.join(lines) + '\n')
        hashes[key] = dict(file='dessertation_reference/' + name, sha256=sha(pdf), pages=len(pages))
        print('%-8s %3d pages' % (key, len(pages)))
    write(HERE / 'sources' / 'pdf-hashes.json', json.dumps(hashes, indent=2) + '\n')


if __name__ == '__main__':
    main()
