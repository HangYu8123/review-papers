"""Write sources/general-english-zipf.tsv, the general English word frequencies used by the vocabulary tools.

This is a one-time snapshot, so the other tools need only the Python standard library.
It needs the wordfreq package (https://github.com/rspeer/wordfreq), for example:
    py -3.12 -m pip install --target <scratch folder> wordfreq
    set PYTHONPATH=<scratch folder>
    py -3.12 writing_style_ref/tools/make_general_english.py
Zipf frequency is log10 of uses per billion words: 7 is "the", 4 is a word seen about
ten times per million words, 3 about once per million. Words at Zipf 3.0 or above are kept.
"""

from pathlib import Path
from wordfreq import top_n_list, zipf_frequency
import wordfreq

HERE = Path(__file__).resolve().parents[1]
OUT = HERE / 'sources' / 'general-english-zipf.tsv'
MIN_ZIPF = 3.0

rows = []
for w in top_n_list('en', 100000):
    z = zipf_frequency(w, 'en')
    if z < MIN_ZIPF:
        break
    if w.replace('-', '').replace("'", '').isalpha():
        rows.append((w, z))
header = [
    '# General English word frequencies (Zipf scale), from wordfreq ' + getattr(wordfreq, '__version__', ''),
    '# Source: wordfreq by Robyn Speer, data licensed CC BY-SA 4.0. Words with Zipf >= %.1f.' % MIN_ZIPF,
]
OUT.write_text('\n'.join(header + ['%s\t%.2f' % r for r in rows]) + '\n', encoding='utf-8')
print('Wrote %d words to %s' % (len(rows), OUT))
