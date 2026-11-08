"""Extract the text of the three reference dissertations for the technical vocabulary.

Run from the dissertation folder:  python writing_style_ref/tools/extract_reference_text.py
It needs pdftotext (Poppler); Git for Windows ships one in mingw64/bin. The output, one
marked block per PDF page, goes to sources/reference-dissertations/ and is what
build_vocabulary.py reads, so the PDFs are needed only to extract the text again.
The same command produced committee_style_ref/sources/text/, which this does not depend on.
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
OUT = HERE / 'sources' / 'reference-dissertations'
PDFS = {
    'short': 'dessertation_reference/Short_2017_USC_thesis.pdf',
    'vazquez': 'dessertation_reference/Vazquez_2017_CMU_thesis.pdf',
    'bobu': 'dessertation_reference/Bobu_2023_Berkeley_EECS-2023-200.pdf',
}
CANDIDATES = ['pdftotext', r'C:\Program Files\Git\mingw64\bin\pdftotext.exe']


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


def main():
    exe = find_pdftotext()
    OUT.mkdir(parents=True, exist_ok=True)
    hashes = {}
    for key, rel in PDFS.items():
        pdf = ROOT / rel
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
        write(OUT / (key + '.txt'), '\n'.join(lines) + '\n')
        hashes[key] = {'file': rel, 'sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(), 'pages': len(pages)}
        print('%-8s %3d pages' % (key, len(pages)))
    write(OUT / 'pdf-hashes.json', json.dumps(hashes, indent=2) + '\n')


if __name__ == '__main__':
    main()
