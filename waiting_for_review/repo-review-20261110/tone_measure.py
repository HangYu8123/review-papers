"""Rates of patterns often named as signs of machine-written prose, in human-written field dissertations."""
import re, sys, json
from pathlib import Path
REPO = Path(sys.argv[1])
files = {}
for p in sorted((REPO / "dissertation_reference/text").glob("*.txt")):
    files[p.stem] = p
for p in sorted((REPO / "plugins/review-your-papers/skills/writing-style/committee_style_ref/sources/text").glob("*.txt")):
    files[p.stem] = p
YEAR = dict(short=2017, vazquez=2017, bobu=2023, klein=2023, birmingham=2023, tsoi=2025, shi=2026, sargent=2026, gokmen=2026,
            wong=2026, candon=2026, thompson=2026, georgiou=2026, ghose=2026, matheus=2026)
PAT = {
 "em dash": r"—",
 "delve": r"\bdelv(e|es|ed|ing)\b",
 "pivotal": r"\bpivotal\b",
 "underscore(s)": r"\bunderscor(e|es|ed|ing)\b",
 "showcase": r"\bshowcas(e|es|ed|ing)\b",
 "intricate/intricacies": r"\bintrica(te|cy|cies)\b",
 "multifaceted": r"\bmultifaceted\b",
 "landscape": r"\blandscape\b",
 "realm": r"\brealm\b",
 "testament": r"\btestament\b",
 "tapestry": r"\btapestry\b",
 "seamless(ly)": r"\bseamless(ly)?\b",
 "holistic": r"\bholistic(ally)?\b",
 "nuanced": r"\bnuanced?\b",
 "foster": r"\bfoster(s|ed|ing)?\b",
 "comprehensive": r"\bcomprehensive(ly)?\b",
 "crucial(ly)": r"\bcrucial(ly)?\b",
 "notably": r"\bnotably\b",
 "leverage": r"\bleverag(e|es|ed|ing)\b",
 "utilize": r"\butiliz(e|es|ed|ing)\b",
 "robust": r"\brobust(ly|ness)?\b",
 "novel": r"\bnovel\b",
 "paramount/plethora/myriad": r"\b(paramount|plethora|myriad)\b",
 "it is worth noting / important to note": r"\b(it is|it's) (worth noting|important to note|worth mentioning)\b",
 "plays a ... role": r"\bplay(s|ed|ing)? an? (crucial|vital|key|pivotal|significant|important|central|critical) role\b",
 "pave the way": r"\bpav(e|es|ed|ing) the way\b",
 "shed light": r"\bshed(s|ding)? light\b",
 "not only ... but also": r"\bnot only\b[^.]{0,120}\bbut also\b",
 "trailing -ing clause (, highlighting ...)": r", (highlighting|underscoring|emphasizing|showcasing|demonstrating|reflecting|ensuring|enabling|allowing|making|leading to|suggesting|indicating|resulting in|providing|offering|paving)\b",
 "  of which: , suggesting/indicating": r", (suggesting|indicating)\b",
 "  of which: , highlighting/underscoring/emphasizing/showcasing": r", (highlighting|underscoring|emphasizing|showcasing)\b",
 "serves as / stands as": r"\b(serv(e|es|ed|ing) as|stands? as)\b",
 "Moreover/Furthermore/Additionally (sentence start)": r"(?<=[.!?] )(Moreover|Furthermore|Additionally),",
 "Overall/In summary/In conclusion/Ultimately (sentence start)": r"(?<=[.!?] )(Overall|In summary|In conclusion|Ultimately|To summarize),",
 "Importantly/Notably/Crucially/Interestingly (sentence start)": r"(?<=[.!?] )(Importantly|Notably|Crucially|Interestingly|Remarkably),",
 "This highlights/underscores/demonstrates the importance": r"\bThis (highlights|underscores|emphasizes|demonstrates) the (importance|need|potential|value)\b",
 "semicolon": r";",
 "colon": r":(?!//)",
 "contraction": r"\b\w+n't\b|\b(it|that|there|we|they|I)'(s|re|ve|ll|d)\b",
}
rows = {}
tot = {}
for name, p in files.items():
    t = p.read_text(encoding="utf-8", errors="replace")
    t = re.sub(r"\[\[page \d+\]\]", " ", t)
    t = re.sub(r"\s+", " ", t)
    n = len(re.findall(r"[A-Za-z][A-Za-z'-]*", t))
    tot[name] = n
    rows[name] = {k: len(re.findall(v, t)) for k, v in PAT.items()}
names = sorted(files, key=lambda k: (YEAR.get(k, 0), k))
print("words:", {k: tot[k] for k in names})
print("%-62s %7s %7s %7s  %s" % ("pattern (per 10,000 words)", "median", "max", "docs>0", "2017 pair | 2025-26 median"))
import statistics as st
out = {}
for k in PAT:
    r = {n: rows[n][k] / tot[n] * 1e4 for n in names}
    early = [r[n] for n in names if YEAR[n] <= 2017]
    late = [r[n] for n in names if YEAR[n] >= 2025]
    out[k] = dict(median=st.median(r.values()), max=max(r.values()), docs=sum(1 for v in r.values() if v > 0), early=early, late=st.median(late), per=r)
    print("%-62s %7.2f %7.2f %4d/15  %s | %.2f" % (k, out[k]["median"], out[k]["max"], out[k]["docs"], "/".join("%.2f" % e for e in early), out[k]["late"]))
json.dump(dict(words=tot, rates=out), open(Path(sys.argv[2]), "w"), indent=1)
