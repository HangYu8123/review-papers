"""Measure Hang's current draft with the same counts as the three dissertations.

Run from the dissertation folder after main.pdf has been compiled:

    python committee_style_ref/tools/profile_draft.py

The result is a dated snapshot in sources/draft-profile.json. The build reads
the snapshot, so the reference does not change each time the draft does.
"""
import datetime
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as C
from extract_text import find_pdftotext, write

MARKER = re.compile(r'\[HY:[^\]]{0,120}\]')


def first_line(page):
    for line in page.split('\n'):
        if line.strip():
            return line.strip()
    return ''


def main():
    pdf = C.ROOT / 'main.pdf'
    with tempfile.TemporaryDirectory() as tmp:
        raw = Path(tmp) / 'raw.txt'
        subprocess.run([find_pdftotext(), '-enc', 'UTF-8', str(pdf), str(raw)], check=True,
                       stderr=subprocess.DEVNULL)
        pages = raw.read_bytes().decode('utf-8', errors='replace').split('\f')
    start = end = None
    for i, page in enumerate(pages, 1):
        head = first_line(page)
        if start is None and re.match(r'Chapter 1\b', head):
            start = i
        if start is not None and end is None and head.startswith('Bibliography'):
            end = i - 1
    if start is None or end is None:
        sys.exit('Could not find Chapter 1 and the Bibliography in main.pdf.')
    paragraphs = []
    markers = 0
    for page in pages[start - 1:end]:
        markers += len(MARKER.findall(page))
        text = MARKER.sub(' ', page)
        lines = [re.sub(r'\s+', ' ', line).strip() for line in text.split('\n')]
        paragraphs.extend(C.paragraphs_of([line for line in lines if line and not line.isdigit()]))
    out = C.measure(paragraphs)
    out.update(date=datetime.date.today().isoformat(), file='main.pdf',
               sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(),
               body=[start, end], review_markers_removed=markers)
    write(C.HERE / 'sources' / 'draft-profile.json', json.dumps(out, indent=2) + '\n')
    print('main.pdf pages %d to %d, %d words, mean sentence %.1f words' % (start, end, out['words'], out['sent_mean']))


if __name__ == '__main__':
    main()
