# Measures for each writer

These are the measures that the [main reference](committee-writing-style-reference.md) cites. Rates are per 1,000 words unless a row says count or percent.

| Measure | Short | Vázquez | Bobu | Hang's draft |
| --- | --- | --- | --- | --- |
| Paragraphs measured | 476 | 490 | 445 | 340 |
| Words measured | 35,300 | 33,376 | 32,861 | 29,421 |
| Sentences measured | 1,389 | 1,719 | 1,478 | 1,471 |
| Mean words per sentence | 26.1 | 20.3 | 22.8 | 20.7 |
| Median words per sentence | 24 | 19 | 22 | 19 |
| Sentences of 12 words or fewer (%) | 14 | 19 | 17 | 23 |
| Sentences of 35 words or more (%) | 22 | 6 | 13 | 10 |
| We, our, us | 6.7 | 18.0 | 25.7 | 0.0 |
| Colons | 5.3 | 3.1 | 6.1 | 3.6 |
| Semicolons | 2.3 | 0.7 | 1.1 | 0.9 |
| Question marks | 0.4 | 0.2 | 0.5 | 0.1 |
| Contractions | 0.3 | 0.2 | 0.9 | 0.0 |
| Suggest and its forms | 1.2 | 1.3 | 0.7 | 1.2 |
| May | 0.8 | 0.9 | 1.9 | 1.1 |
| Might | 1.0 | 0.2 | 1.0 | 0.3 |
| Could | 0.7 | 1.9 | 1.2 | 1.2 |
| Can | 2.9 | 4.3 | 5.0 | 5.8 |
| Likely | 0.3 | 0.6 | 0.3 | 0.5 |
| Tend and its forms | 0.0 | 0.7 | 0.2 | 0.3 |
| Enable and its forms | 1.2 | 0.9 | 1.4 | 0.5 |
| Leverage and its forms | 0.2 | 0.4 | 0.4 | 0.4 |
| This dissertation (count) | 31 | 21 | 5 | 55 |
| This thesis (count) | 0 | 0 | 7 | 0 |
| This work (count) | 55 | 26 | 3 | 7 |
| This chapter (count) | 21 | 9 | 18 | 67 |

## Sentence openers

The number of sentences that begin with the word or phrase followed by a comma.

| Opener | Short | Vázquez | Bobu | Hang's draft |
| --- | --- | --- | --- | --- |
| However | 21 | 21 | 31 | 25 |
| Additionally | 24 | 0 | 2 | 8 |
| Finally | 20 | 16 | 4 | 6 |
| Lastly | 0 | 1 | 15 | 1 |
| For example | 5 | 38 | 12 | 4 |
| For instance | 0 | 2 | 8 | 13 |
| In general | 1 | 20 | 0 | 0 |
| In particular | 0 | 16 | 2 | 1 |
| Moreover | 0 | 15 | 9 | 11 |
| Furthermore | 4 | 11 | 5 | 7 |
| In addition | 0 | 8 | 1 | 10 |
| Unfortunately | 0 | 1 | 15 | 0 |
| Interestingly | 0 | 7 | 0 | 0 |
| Thus | 0 | 6 | 9 | 10 |
| Therefore | 3 | 0 | 0 | 1 |
| First | 1 | 14 | 5 | 3 |
| Second | 1 | 9 | 3 | 3 |
| Third | 0 | 2 | 2 | 1 |
| Overall | 1 | 4 | 8 | 2 |
| Instead | 0 | 0 | 8 | 2 |
| Nonetheless | 0 | 4 | 1 | 0 |

## How the measures were counted

The text of each PDF was extracted with pdftotext, one block for each page. Only the numbered chapters were measured, which are PDF pages 19 to 189 for Short, 8 to 90 for Vázquez, and 15 to 199 for Bobu. Running heads and page numbers were removed. A line counts as prose when it has at least 20 words, which leaves out headings, captions that are short, table cells, and most equations. Lines with symbols that the extraction could not read were left out, and this removes much of the mathematics in Bobu.

Sentences were split at a period, question mark, or exclamation mark that is followed by a capital letter, after common abbreviations such as e.g., i.e., et al., Fig., and Sec. were protected. Sentences of fewer than three words were dropped. A colon between two digits was not counted. Contractions include those inside quoted speech of participants.

Hang's draft was measured from main.pdf as compiled on October 12, 2026, pages 20 to 142, after 8 review markers were removed from the text. The snapshot is in [sources/draft-profile.json](sources/draft-profile.json). Run `python committee_style_ref/tools/profile_draft.py` and then the build to refresh it.

Short cites with author and year in parentheses, and Vázquez and Bobu cite with numbers in square brackets. Citations are part of the measured text, so Short's sentences are slightly longer for that reason alone. The measures are approximate and are meant for comparison between the writers.
