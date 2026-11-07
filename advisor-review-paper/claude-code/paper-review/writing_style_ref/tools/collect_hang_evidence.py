"""Snapshot Hang's writing instructions (verbatim excerpts of messages) and hand edits (verbatim
lines from git and from the slide feedback log) into writing_style_ref/sources/.

    python writing_style_ref/tools/collect_hang_evidence.py

Run on October 19, 2026 to make sources/hang-instructions.json and sources/hand-edits.json.
It reads the Claude Code transcripts of the dissertation and talk projects in ~/.claude/projects,
the talk folder next to the dissertation, and the commit named in COMMIT. Each excerpt and each
needle must still be found, or the script stops. To add an instruction, add it to PICKS. To add a
hand edit, add it to CHAPTER_EDITS or SLIDE_EDITS, and check that its new text is not the wording
of a review suggestion that was applied (that belongs to the review, not to Hang's own edits)."""
import glob, json, os, re, subprocess
from pathlib import Path

DIS = Path(r'C:\Users\Hang Yu\Desktop\Dissertation')
PRES = Path(r'C:\Users\Hang Yu\Desktop\dissertation_presentation')
PROJECTS = [Path(r'C:\Users\Hang Yu\.claude\projects\C--Users-Hang-Yu-Desktop-Dissertation'),
            Path(r'C:\Users\Hang Yu\.claude\projects\C--Users-Hang-Yu-Desktop-dissertation-presentation')]
COMMIT = '3de2b82'


def text_of(content):
    if isinstance(content, str):
        return content
    return '\n'.join(c.get('text', '') for c in content or [] if isinstance(c, dict) and c.get('type') == 'text')


messages = {}
for proj in PROJECTS:
    for f in glob.glob(str(proj / '*.jsonl')):
        for line in open(f, encoding='utf-8', errors='replace'):
            try:
                e = json.loads(line)
            except Exception:
                continue
            if e.get('type') != 'user' or e.get('isSidechain') or e.get('isMeta'):
                continue
            c = e.get('message', {}).get('content')
            if isinstance(c, list) and any(isinstance(x, dict) and x.get('type') == 'tool_result' for x in c):
                continue
            t = re.sub(r'<system-reminder>.*?</system-reminder>', '', text_of(c), flags=re.S)
            t = re.sub(r'</?pasted_content[^>]*>', '', t).strip()
            if t:
                messages.setdefault(e.get('timestamp', '')[:19], (proj.name, e.get('sessionId', ''), t))

# (id, timestamp or file, project label, topic, excerpts that must occur verbatim in the message)
PICKS = [
    ('HI-01', '2026-09-26T21:54:12', 'Measured wording that Hang supplied', [
        '“mitigate these human dynamics” — [Introduction (line 54)](C:/Users/Hang Yu/Desktop/Dissertation/chapters/introduction.tex:54)“account for systematic variation in human teaching”',
        '“With an agreement tolerance of ±2, we did not detect a difference in self-consistency between scalar and binary feedback.”',
        '“Robot experience and educational background showed positive associations with feedback accuracy, with correlations of 0.25 and 0.16, respectively.”',
        '“The qualitative analysis illustrates how progress alignment can discourage two examined reward-hacking behaviors.”']),
    ('HI-02', '2026-09-26T23:16:52', 'Terminology, one dissertation, and chapter jobs', [
        'Prefer “degree of completion” to “completion rate.” “Rate” can imply speed or the proportion of successful trials.',
        "I'd use \"under-explored as a human teaching signal\" everywhere except the paper title.",
        'Write as a dissertation, not as separate papers.',
        'Reduce the feeling of repeatedly starting a new paper.',
        'Preserve the bridges and shorten repeated general motivation. End each chapter by identifying the question that remains and why the next chapter addresses it.']),
    ('HI-03', '2026-10-11T15:39:13', 'Impersonal voice', [
        'in our work -> in this work, we conducted a study -> a study was conducted,  we found that xx in results -> results suggested that, our intuition is -> the intuition is, our final step is -> the final step is']),
    ('HI-04', '2026-10-12T13:04:43', 'Writing that reads as AI-generated', [
        'suggestING improvement FOR THE AI WRITING TO MAKE THEM LESS AI LIKE']),
    ('HI-05', '2026-10-12T16:57:01', 'Colons and semicolons', ['use less ":" and ";"']),
    ('HI-06', '2026-10-12T18:41:57', "Hang's wording of the third question",
     ['use Chapter 1: "lower quality requirements for human teaching and reduce human effort in annotating"']),
    ('HI-07', '2026-10-14T13:37:55', 'Minimal added text', ['with a minimal text description add to dissertation']),
    ('HI-08', '2026-10-14T13:59:59', 'This chapter', ['"this chapter" has been used so many times, propose replacement suggestions.']),
    ('HI-09', '2026-10-15T06:28:50', 'Redundant chapter introductions',
     ['the introduction section in chapter 3 to chapter 7 are redundant with the pre-face paragraphs, can i just delete them?']),
    ('HI-10', '2026-10-15T08:07:25', 'Openings: move and cut rather than write', [
        'focus on reducing redundancy and improve smoothness of writing and logic.',
        'mostly focus on re-orgnizing (moving sentences around), and cut, avode creating new ones.']),
    ('HI-12', '2026-10-17T15:25:49', 'Motivation slides', [
        'i do not like page 3 to page 5 due to a. the tone, too seriously; b. too many words; c. not illustrative and appealling as motivation story; rework on it']),
    ('HI-13', '2026-10-17T18:05:27', 'What the motivation is about',
     ['the story should be about: non-expert teaching should recive attetion and is important while they are noisy']),
    ('HI-14', '2026-10-17T21:59:29', 'The motivation story', [
        'reject this version for: being too specific about the work that has already been done in this dissertation rather than setting up the problem and illustrate about motivation.',
        'robots are already in our daily life, but most of training data are produced in lab, and many learning methods require clean data -> if we want robots to actually be part of our day to day life, they need to learn from everyone (key motivation) -> however, not everyone can provide clean data -> in addition, human teaching human use multiple modalities(what is insufficent, i.e., challenge)  and  non-expert data is more accessible (merits of using non expert data) -> it will make the trained model more robust to real world ( merits of out come)',
        "you dont need to use exact words, but get the idea."]),
    ('HI-15', '2026-10-18T15:03:33', 'From benefits to challenge to this work', [
        'rework and reshpae page 5 to connect to our work ( page 4 benefits -> page 5 challenge -> page 6 our work). It is almost there, just do light twist and re-orgnize the page',
        'the example shows that expection of guess is > 0 thus LLM tends to hallucinate.']),
    ('HI-16', '2026-10-18T15:14:11', 'Future work and the closing slide', [
        '6.simplify page 61 and 62 on text',
        '8. reduce what has been done in page 66 and 67, focusing on what is agentic HRI and what are the benefits of agentic HRI',
        '9. improve page 68, focusing on the relationship (i.e., how each stage builds on each other) with very high level takeaways and summarizations']),
    ('HI-17', '2026-10-18T17:39:05', 'Film captions', [
        '5. for the word at 80s, it should sth like, all these relies on data from recorded in the lab or data farms',
        '6. for caption at 118scond, it could change from need -> could, and thus to be constrast to they need to be in data farm',
        '7. the noise tag at 140 s comes out of no where, while i know the meaning is that these teachings contain noise, but they did not get expressed well in the video.',
        '10. i do not need the monet impression paint name in my video, use imperfection directly is good.']),
    ('HI-18', '2026-10-17T13:56:11', 'The reference is used for slide wording', [
        '5. improve wording for newly generated/added slides ( between the newest version and C:\\Users\\Hang Yu\\Desktop\\dissertation_presentation\\Hang_dissertation_talk_Claude.pptx) using C:\\Users\\Hang Yu\\Desktop\\dissertation_presentation\\writing_style_ref']),
]

PICKS.append(('HI-19', '2026-09-26T22:12:37', 'A result Hang asked to drop', [
    'The paper drops the Can-MH result for removing completion shaping (116.99 → 63.77). drop it as well.']))

instructions = []
for hid, ts, topic, excerpts in PICKS:
    proj, sess, text = messages[ts]
    for x in excerpts:
        assert x in text, (hid, x[:60])
    instructions.append(dict(id=hid, date=ts[:10], time=ts[11:16] + ' UTC', session=sess,
                             project='dissertation' if proj.endswith('Dissertation') else 'presentation',
                             topic=topic, source='message', excerpts=excerpts))

pref = (PRES / 'reference_templates' / 'ppt_preference.md').read_text(encoding='utf-8')
ex11 = ['2. figures are more preferred than text.', '8. Scentific but causual tone.', '9. goal is to keep the listeners engage.']
assert all(x in pref for x in ex11)
instructions.append(dict(id='HI-11', date='2026-09-27', time='', session='', project='presentation',
                         topic='Slide preferences Hang wrote before the first slide session', source='file',
                         file='dissertation_presentation/reference_templates/ppt_preference.md', excerpts=ex11))
instructions.sort(key=lambda h: h['id'])


def git_show(path):
    return subprocess.run(['git', '-C', str(DIS), 'show', COMMIT + ':' + path], capture_output=True,
                          text=True, encoding='utf-8').stdout


def lines_with(text, needle):
    out = [ln.strip() for ln in text.splitlines() if needle in ln]
    assert out, needle
    return out[0]


# (id, file, topic, [(before needle, after needle)], note)
CHAPTER_EDITS = [
    ('HE-01', 'chapters/discussion.tex', 'The overall findings stated as answers', [
        ('\\section{Answers to the Overarching Questions}', '\\section{Overall Findings Across Chapters}'),
        ('\\textit{Are the imperfections in non-expert teaching random noise?}', '\\textit{The imperfections in non-expert teaching are not random noise.}'),
        ('\\textit{Can the inconsistency of non-expert feedback be reduced while utilizing the magnitudes?}', '\\textit{The inconsistency of non-expert feedback  can be reduced while utilizing the magnitudes.}'),
        ('\\textit{Can combining demonstrations and feedback enable robust reward learning', '\\textit{Combining demonstrations and feedback can help to enable robust reward learning'),
        ('Then it describes the findings that connect the chapters', 'It first describes the findings that emerges when considering the all chapters together')],
     'The section on the three questions was renamed, each question heading became the finding, and the answer sentences under them were removed. The separate section on findings that connect the chapters was removed as a heading.'),
    ('HE-02', 'chapters/discussion.tex', 'Lead-in to the limits of the combined evidence', [
        ('The limitations of each study are discussed in its own chapter.', 'The limitations of each study are already discussed in its own chapter, but there are a few gaps if the studies are considered together.'),
        ('First, the stages of the argument were evaluated separately, not end-to-end.', 'First, the stages of the argument were evaluated separately.')], ''),
    ('HE-03', 'chapters/discussion.tex', 'Agentic robotics, reworded by Hang', [
        ('In agentic robotics, non-expert teaching does not disappear.', 'In agentic robotics, non-expert teaching is still valuable, as people correct plans'),
        ('Human teaching would then provide a trajectory at a different level', 'Humans now provide a trajectory at a different level')],
     'Hang reworded text that had been accepted from the Chapter 8 and punctuation reviews.'),
    ('HE-04', 'chapters/discussion.tex', 'Future-work subsection headings', [
        ('\\subsection*{Agentic Robotics}', '\\subsection*{Human-in-the-Loop Agentic Robotics}'),
        ('\\subsection*{Agentic Human-Robot Interaction}', '\\subsection*{Agentic Human-Robot Interaction for Non-Expert Users}')], ''),
    ('HE-05', 'chapters/introduction.tex', 'Section headings for the three stages', [
        ('\\section{Noise beyond the Task}', '\\section{Modeling and Understanding Noise beyond the Task}'),
        ('\\section{Towards Richer Human Evaluative Feedback}', '\\section{Mitigating Noise for Richer Human Evaluative Feedback}'),
        ('\\section{\\textit{Progress}-Heuristicized Inverse Reinforcement Learning}', '\\section{Leveraging Human Feedback and Demonstrations for Reward Learning}')], ''),
    ('HE-06', 'chapters/*.tex', 'Chapter titles without the paper prefix', [], ''),
    ('HE-07', 'chapters/sidetracks.tex', 'Opening of Chapter 4', [
        ('This chapter completes the first stage of this dissertation by turning from human feedback', 'This chapter completes the first stage of this dissertation.'),
        ('It analyzes demonstrations of a long-horizon manipulation task provided by 40 non-experts in a public space study, and identifies four types', 'The main contributions of this chapter are characterizing and categorizing non-optimal behaviors in human demonstrations.')],
     'The summary paragraph that opened the chapter was replaced by the stage sentence, the contribution statement, and the introduction text of the paper, which now follows them.'),
    ('HE-08', 'chapters/steady.tex', 'Opening of Chapter 5', [
        ('It presents an online study in which 90 crowdworkers gave either binary or scalar feedback', 'Evaluative feedback is natural for non-experts to provide'),
        ('Rather than reducing the variability of scalar feedback by reducing its information, this chapter measures', 'This chapter measures how inconsistent scalar feedback actually is, and examines whether its inconsistency can be mitigated algorithmically.')],
     'The summary sentences after the stage sentence were removed, and the paper\'s first sentences about interactive reinforcement learning moved up. Hang also made the change of TC-501 in the review of this chapter by hand, with This chapter kept as the subject.'),
    ('HE-09', 'chapters/progress.tex', 'Opening of Chapter 6', [
        ('This chapter builds on these results to design a signal that focuses on task completion.', 'This chapter builds on these results  and characterizes \\textit{progress}, a type of human feedback that is under-explored as a human teaching signal'),
        ('and the first stage of this dissertation suggests the underlying reasons:', 'and the first stage of this dissertation suggests:')],
     'TC-602 had proposed These results motivate the design of a signal. Hang kept This chapter and moved in the sentence of the paper that characterizes progress.'),
    ('HE-10', 'chapters/phirl.tex', 'Opening of Chapter 7', [
        ('This chapter presents the final stage of this dissertation, which leverages imperfect non-expert teaching for learning.', 'This chapter presents the final stage of this dissertation, which is to to learn robust reward functions by combining human demonstrations and feedback, while reducing human engagement.'),
        ('It proposes \\textit{Progress}-Heuristicized Inverse Reinforcement Learning (PHIRL)', 'Thus, this chapter proposes \\textit{Progress}-Heuristicized Inverse Reinforcement Learning (PHIRL)')],
     'The aim moved into the stage sentence, and the proposal follows it with Thus. The doubled to in which is to to learn is in the file as of October 19, 2026.'),
    ('HE-11', 'chapters/charm.tex', 'Opening of Chapter 3', [
        ('It investigates whether the characteristics of individual teachers are associated with the values of the scalar feedback they give to a robot.', 'This chapter investigates whether the characteristics of individual teachers are associated with the values of the scalar feedback they give to a robot.')],
     'Hang reordered the opening. The gap in prior work now opens the chapter, followed by the aim and hypothesis (in the wording of TC-302, accepted), what the chapter investigates, the study, the results, and what the results are good for.'),
    ('HE-12', 'chapters/introduction.tex', 'Where the studies were conducted', [
        ('Moreover, the studies in this dissertation were mostly conducted in a public space, and can be expected', 'Moreover, the studies in this dissertation were mostly conducted in non-lab settings, and thus can be expected'),
        ('All the data collected and the annotations made in the studies of this dissertation are available online.', 'are available online along with the implementations of the algorithms and data annotation interfaces.')], ''),
]

TITLE_FILES = ['charm', 'sidetracks', 'steady', 'progress', 'phirl']
hand = []
for hid, path, topic, pairs, note in CHAPTER_EDITS:
    changes = []
    if hid == 'HE-06':
        for name in TITLE_FILES:
            p = 'chapters/%s.tex' % name
            old = git_show(p)
            new = (DIS / p).read_text(encoding='utf-8')
            b = lines_with(old, '\\chapter{')
            a = lines_with(new, '\\chapter{')
            assert a != b
            changes.append(dict(file=p, before=b, after=a))
    else:
        old = git_show(path)
        new = (DIS / path).read_text(encoding='utf-8')
        for b_needle, a_needle in pairs:
            b = lines_with(old, b_needle)
            a = lines_with(new, a_needle)
            changes.append(dict(file=path, before=b, after=a))
    hand.append(dict(id=hid, topic=topic, origin='chapter edit', where='dissertation',
                     dated='between the commit of October 14, 2026 (%s) and October 15, 2026' % COMMIT,
                     changes=changes, note=note))

# Opening-overlap review: applied by hand without a decisions file.
hand.append(dict(id='HE-13', topic='Opening-overlap review applied by hand', origin='review applied by hand',
                 where='dissertation', dated='October 15, 2026',
                 changes=[], applied=['OV-301', 'OV-401', 'OV-403', 'OV-404', 'OV-501', 'OV-601', 'OV-602', 'OV-604',
                                      'OV-701', 'OV-702', 'OV-703', 'OV-705'],
                 not_applied=['OV-402', 'OV-405', 'OV-502', 'OV-603', 'OV-704'],
                 note='No decisions were saved for this review. On October 19, 2026 the chapters held the suggested text of 12 items (11 cuts and one trim) and the original text of 5. OV-402 had been withdrawn because the opening-reorder review was applied first.'))

log = (PRES / 'guidelines' / 'feedback_log.md').read_text(encoding='utf-8')
SLIDE_EDITS = [
    ('HE-14', 'Measured wording on slides', [
        ('"no detectable difference"', '"no statistical significance"'), ('"same NASA-TLX"', '"similar NASA-TLX"')],
     'September 27 to 28, 2026'),
    ('HE-15', 'A dictated line kept word for word', [
        ('which means their teaching will be noisier and harder for robots to learn', '"harder" → "challenging" in the line Claude had just added')],
     'September 28, 2026'),
    ('HE-16', "Hang's rewrite of the demonstration caption", [
        ('"every frame carries information, including the wobbles."', '"demonstrations carry policy information, but not always optimal framewise."')],
     'September 28, 2026'),
    ('HE-17', 'Captions and bands deleted', [
        ('Deleted the caption "Factories · sidewalks · homes"', ''), ('Deleted the band "Not random noise: sidetracks depend on the sub-task..."', '')],
     'September 28, 2026'),
    ('HE-18', 'Titles and captions Hang wrote', [
        ('', '"Robots belong to the world, not the lab."'), ('"A new teaching signal" → "Progress"', ''),
        ('', '"Often happened within 4 s of a sub-task change"'), ('', '"scalar can outperform binary: the magnitudes carry additional information."')],
     'September 27 to 28, 2026'),
]
for hid, topic, pairs, dated in SLIDE_EDITS:
    changes = []
    for b, a in pairs:
        assert (not b or b in log) and (not a or a in log), (hid, b, a)
        changes.append(dict(file='dissertation_presentation/guidelines/feedback_log.md', before=b, after=a))
    hand.append(dict(id=hid, topic=topic, origin='slide edit recorded in feedback_log.md', where='slides',
                     dated=dated, changes=changes,
                     note='Recorded by an assistant that compared the saved versions of the short talk. The quotation marks are those of the log.'))

out = DIS / 'writing_style_ref' / 'sources'
(out / 'hang-instructions.json').write_text(json.dumps(
    {'schema': 'hang-instructions/1', 'collected': '2026-10-19',
     'note': 'Verbatim excerpts of messages Hang typed in Claude Code sessions for the dissertation and the dissertation talk, and of one preferences file Hang wrote. Text pasted from other reviewers is not included.',
     'instructions': instructions}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(out / 'hand-edits.json').write_text(json.dumps(
    {'schema': 'hang-hand-edits/1', 'collected': '2026-10-19', 'commit': COMMIT,
     'note': 'Edits Hang made by hand. Chapter edits compare the commit of October 14, 2026 with the chapter files of October 19, 2026, and were checked so that each is not the wording of a review suggestion. Slide edits are quoted from the feedback log of the talk.',
     'edits': hand}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(instructions), 'instructions,', len(hand), 'hand edits')
for h in hand:
    for c in h['changes']:
        print(h['id'], '|', c['before'][:110], '=>', c['after'][:110])
