# Full talk: the 12 items in full_pre_notes.txt

Review `full-talk-pre-notes` of the slides, from `../dissertation_presentation/wait_to_review/full-talk-pre-notes-review`. Decided between October 18, 2026 and October 18, 2026. Decisions files: `full-talk-pre-notes.decisions.20261018-121706.json`.

[All reviews](../review-decisions.md) · [Weighted signals](../preference-signals.md) · [Main reference](../hangs-writing-style-reference.md)

| Outcome | Decided by Hang | Not decided by Hang |
| --- | ---: | ---: |
| Accepted as suggested | 15 | 0 |
| Accepted with Hang's edit | 0 | 0 |
| Declined | 0 | 0 |
| Notes from Hang | 8 | |

### PN-R01a

**Accepted** · weight 3 · Images · Motivation (slides 4-12) · Slide 4 (stays 4)

Suggestion: Photos of non-experts giving robot data (cheaper data, wider reach)

Original:

~~~text
Our atrium study photo and the four people drawings, under 'Cheaper data and Wider reach', with your note 'Replace these two figure with many figures for data collection for non-expert users'.
~~~

Accepted wording:

~~~text
Three photos of non-experts giving robot data, from outside our own work:
- RoboCrowd: passersby lining up at a robot in a university café (ICRA 2025, photo from robocrowd.github.io).
- AR2-D2: a person records a demonstration with an iPhone app, no robot needed (CoRL 2023, photo 2 of the paper's Figure 1).
- RoboTurk: a person controls the robot with a phone (CoRL 2018, panel c of the system figure).
Heading 'Cheaper data and wider reach'. Captions: 'More than 200 café visitors gave data in two weeks (RoboCrowd).' and 'People can also teach with a phone (RoboTurk) or with an iPhone app and no robot (AR2-D2).'
Click 1 shows the café photo and the first caption, click 2 the two phone photos and the second caption. The slide keeps 4 clicks.
Notes for clicks 1-2: '[click] First, it is cheaper. RoboCrowd put a robot arm in a university café, and more than 200 visitors gave it data in two weeks. [click] Second, a wider reach. People can teach with the phone they already have, as in RoboTurk, or with an iPhone app and no robot at all, as in AR2-D2.'
~~~

Hang's note: I do not like the model outcome one, instead of having performance chart, showing actual video or images to demonstrate that it is better

Note written with the suggestion: Your note asked for many pictures of data collection by non-experts. These are real photos from the papers or project pages, and each shows a different way non-experts give data: in person in a public space, remotely with a phone, and at home with no robot. The numbers come from the RoboCrowd abstract (over 200 people, two weeks). The drawings already appear on slide 22, and item 2 reuses them and the top view on slide 5. Before posting the slides publicly, check reuse of the RoboTurk and AR2-D2 figures (arXiv default license) and of the RoboCrowd project photo (the RoboCrowd paper itself is CC BY 4.0). If you accept only one of 1a and 1b, the other half keeps its current picture and I will re-lay out the slide around it.

Used in: [Slide text in the presenter's voice](../hangs-writing-style-reference.md#slide-text-in-the-presenter-s-voice).

### PN-R01b

**Accepted** · weight 3 · Images · Motivation (slides 4-12) · Slide 4 (stays 4)

Suggestion: A VLA figure for 'More robust models'

Original:

~~~text
The top view of our 34 successful demonstrations under 'More robust models', with your note 'Find other figures (not from this paper) to show this point ( maybe VLAs?)'.
~~~

Accepted wording:

~~~text
The original Figure 8 of π0.5 (Physical Intelligence, CoRL 2025): average task progress in new homes against the number of training locations (3 to 104), next to the in-domain baseline. Caption: 'π0.5 did better in new homes when its training data came from more homes (3 to 104 locations).' It appears on click 3.
Notes for click 3: '[click] Third, more robust models. When π0.5 was trained with data from more homes, it did better in homes it had never seen. With data from 104 locations, it did about as well as a model trained on the test homes themselves.'
~~~

Hang's note: I do not like the model outcome one, instead of having performance chart, showing actual video or images to demonstrate that it is better

Note written with the suggestion: A VLA result, as your note suggested, and not from our papers. The paper says that performance improves with more training locations and that the 104-location model performs similarly to a model trained on the test homes, so the caption and notes say only that. The figure keeps its original colors. Its tick labels are small at this size, so the caption carries the point. The top view of our 34 demos moves to slide 5 (item 2). The introduction cites Ebert's thesis on diverse data for this claim. If you prefer a figure from that line of work, such as Bridge Data or DROID, add a note.

Not used in a pattern: Decisions about slide structure, figures, pictures, and animation, which the slide guidelines of the talk cover.

### PN-R02

**Accepted** · weight 3 · Layout · Motivation (slides 4-12) · Slide 5 (stays 5)

Suggestion: Fill the empty right half so 4 (benefits) leads to 5 (challenge) and 6 (our goal)

Original:

~~~text
Two sentences on the left ('It's widely accepted that demonstrations are noisy, and everyone does the same task differently…' and '…and that feedback varies from person to person.'), an empty right half, then COMMON ASSUMPTION and the navy THIS DISSERTATION box (2 clicks). The eyebrow reads 'Motivation'. The notes are a copy of slide 10's notes.
~~~

Accepted wording:

~~~text
Same words, in two columns.
- Left: the top view of the 34 successful demonstrations (from slide 4), with the demonstrations sentence under it.
- Right: the four people with the ratings Good, Excellent, Bad and Fine, with the feedback sentence under it.
- The two sentences go from 20 pt to 18 pt. COMMON ASSUMPTION and THIS DISSERTATION stay where they are, with the same two clicks.
- The eyebrow becomes 'MOTIVATION', like slides 4 and 6. The footer names the source of the top view.
Notes: '(≈40 s) Everyone in the field agrees that human teaching is imperfect. These are the paths of the 34 successful demonstrations from one of our studies, seen from above, and every one of them is different. And show the same robot to four people, and you can get four different ratings. [click] The common assumption is that this is random noise, so we average it out, keep only binary thumbs up or down, or filter the messy parts away. [click] My dissertation takes a different view: a lot of these imperfections have structure, they come from the task and from the person teaching. And if they're structured, we can model them, mitigate them, and even leverage them.'
~~~

Hang's note: for noisy demonstrations, do not use images from my paper first, try to search online and find other images from other papers

Note written with the suggestion: Slide 4 ends with 'non-expert teaching is seen as noisy and unreliable'. Slide 5 now shows what that noise looks like for demonstrations and for feedback, and THIS DISSERTATION leads into slide 6, 'Go outside the lab and learn from imperfection'. No new words on the slide. The notes now describe this slide and leave 'But why?' to slide 10, whose notes they used to repeat. The rating pills repeat slide 22 on purpose, as a first look. If you reject 1b, the top view would be on slides 4 and 5, so add a note and I will pick another picture for this slide.

Not used in a pattern: Decisions about slide structure, figures, pictures, and animation, which the slide guidelines of the talk cover.

### PN-R03

**Accepted** · weight 1 · Video · Motivation (slides 4-12) · Slide 11 (stays 11)

Suggestion: A 2-second pause in the middle demonstration

Original:

~~~text
Three looping clips of the nut assembly task. All three are trims of one 4.6 s video. The middle one plays 1.9 to 3.37 s, so it also shows 0.2 s of the third demo at the end.
~~~

Accepted wording:

~~~text
The middle clip is replaced by a new video in the same frame and the same play-with-previous slot: demo 2 only, frozen for 2.0 s at 2.3 s while the gripper closes on the nut, then it finishes and loops (3.3 s in all). There is no label on the slide.
Notes add, before '[click] Everyone accepts this.': 'And the one in the middle stops for two seconds. People often pause like this while they teach.'
~~~

Note written with the suggestion: This sets up the pause frames on slide 12. The freeze repeats one real frame of the clip, and nothing else in the video changes. Watch the timing in previews/R03_middle_video_with_pause.mp4. If you want a visible cue during the pause, such as a small 'pause' label, add a note.

### PN-R04a

**Accepted** · weight 3 · Split · Motivation (slides 4-12) · Slide 12 (stays 12)

Suggestion: Split slide 12, part 1: average the pause frames out or remove them

Original:

~~~text
Left half of 'Simple assumptions can backfire': six frames of one demonstration, the last three marked as pause frames, then 'What trains a better VLA' with the pause frames removed.
~~~

Accepted wording:

~~~text
Slide 12 keeps only the pause example, titled 'Two ways to handle pauses in demonstrations'.
- Lead: 'A common shortcut treats human imperfections, like pauses, as random noise that averages out.'
- On screen: 'What a person records', the same six frames, arrows under the three frames with input, and 'pause frames, no input' under the other three.
- Click 1, 'Average it out (keep every frame)': the six frames again, with shorter arrows under all of them. Right: 'Near the jar, the model sees moving and stopping, so it learns to slow down or stop there.'
- Click 2, 'Remove the pause frames': the six frames appear, the three pause frames fade out and leave empty slots, and full arrows wipe in under the rest. Right: 'The model only learns from frames with input. Recent VLA work found that this can clearly improve the models.'
Footer: the frames note, DART and Sasaki and Yamashina (the averaging assumption), Wu et al. and Wang et al. (VLA).
Notes: '(≈40 s) A common shortcut is to treat human imperfections as random noise that averages out. Take pauses. People pause naturally while they teach, like this participant at the jar, and these frames have no input. [click] If we average it out, we keep every frame. Near the jar, the model sees the person moving and stopping, so it learns to slow down or stop there. [click] If we remove the pause frames, the model only learns from frames where the person moved. Recent VLA work found that removing pause frames can significantly improve the models.'
~~~

Hang's note: with improvement: 1. enlarge the one is being illustrated, and smaller the others; 2. The average is not well visualized

Note written with the suggestion: You asked to compare the naive way (average out the freezing frames) with removing them. The introduction lists averaging as one of the simple assumptions (Sasaki and Yamashina) and says removing pause frames can significantly improve VLA models, since freezing frames downgrade the algorithms. 'Slow down or stop' is the plain reason averaging hurts: frames with no input pull the learned action toward zero. The arrows are a drawing of input versus no input, not data. 4b is the other half of the split.

Not used in a pattern: Decisions about slide structure, figures, pictures, and animation, which the slide guidelines of the talk cover.

### PN-R04b

**Accepted** · weight 3 · Split · Motivation (slides 4-12) · New slide 13, after slide 12

Suggestion: Split slide 12, part 2: with binary feedback, the expected score of a guess is above 0

New text, placed next to this passage:

~~~text
(no anchor)
~~~

Accepted wording:

~~~text
New slide 13, 'Binary feedback can reward guessing'.
- Lead: 'Another shortcut keeps only binary feedback, since it seems less noisy.'
- Left: the birthday question and the two answers, now tagged 'a guess' and 'honest'.
- Click 1, 'Right or wrong (binary)', expected score: Guess '03-07' 1/365 > 0, 'I don't know' 0. Caption: 'A random date is right 1 time in 365, so guessing pays.' With it, on the left: 'Kalai and colleagues argue that this is one reason language models hallucinate.'
- Click 2, 'A wrong answer costs 1 point': Guess ≈ −0.99, 'I don't know' 0. Caption: 'Now “I don't know” scores higher.'
- Click 3: 'Scalar feedback, or binary feedback with weights, can reduce this. STEADY in part 2 turns scalar feedback into binary labels with weights.' and the old takeaway 'Oversimplifying human teaching can mean more data or worse robots.'
Footer: Arzate Cruz and Igarashi, Huang, Kalai et al.
Notes: '(≈45 s) Another shortcut is to keep only binary feedback, because it seems less noisy. Language models show what this can cost. Ask a model for Adam Kalai's birthday. [click] Under right-or-wrong scoring, a guess such as 03-07 is right about one time in 365, so its expected score is 1 over 365, which is above zero. 'I don't know' always gets zero. So guessing always pays, and Kalai and colleagues argue that this is one reason language models hallucinate. [click] If a wrong answer costs one point, the expected score of the guess drops to about minus 0.99, and 'I don't know' becomes the better answer. [click] So scalar feedback, or binary feedback with weights, can reduce the problem. STEADY, in part 2, turns scalar feedback into binary labels with weights. So oversimplifying human teaching can mean that we need more data, or that we end up with worse robots.'
~~~

Hang's note: with some animation

Note written with the suggestion: Kalai et al. write that guessing when unsure maximizes the expected score under binary 0-1 scoring, and the introduction says the expected reward of guessing is higher than acknowledging uncertainty. 1/365 is the chance that a random date is right. The 'costs 1 point' row follows the paper's fix, which penalizes a mistake by t/(1−t) points for a confidence target t, so 1 point at t = 0.5. The last click links to part 2, where STEADY labels each rating as good or bad and gives it a confidence weight. Adds one slide.

Not used in a pattern: Decisions about slide structure, figures, pictures, and animation, which the slide guidelines of the talk cover.

### PN-R05

**Accepted** · weight 1 · Move · Part 1, CHARM (slides 22-30) · Slides 22 and 23 (become 23 and 24)

Suggestion: Move 'Our work includes' to slide 23; show all factors first, then the selection

Original:

~~~text
Slide 22: the clip, four people with ratings, the box 'Our work includes' with six ticks and 'Age, gender and culture were left out on purpose.' (click 1), and the question (click 2). Slide 23: twelve factors, the six measured ones framed and dark from the start, the other six grey; click 1 adds the labels and the frame.
~~~

Accepted wording:

~~~text
Slide 22: the box goes, the clip and the four people are centred, and the question keeps its click (1 click). The notes keep the first two sentences and the question.
Slide 23:
- Start: all twelve factors look the same, with no frame and no labels.
- Click 1: 'MEASURED IN CHARM' and the frame around the six we measured. The other six dim, under 'NOT MEASURED HERE'.
- Click 2: 'Age, gender and culture likely shape feedback too. We left them out on purpose, so the results cannot contribute to discrimination.'
The grid moves up 8 pt to make room.
Notes for slide 23 after the first paragraph: '[click] We measured the six on the left, the ones that describe a teacher and can be asked in a short questionnaire. The situational ones, like time pressure and cognitive load, are future work. [click] Age, gender and culture are very likely to shape feedback too. We left them out on purpose, so the results could never be used to discriminate against anyone.'
~~~

Note written with the suggestion: This is the order you asked for: all, then the selection, then why age and gender are left out. The reason follows charm.tex line 100, where these domains were excluded so that the results would not contribute to any form of discrimination. The tick list becomes the frame on slide 23 instead of a second list. The numbered circles stay as they are.

### PN-R06

**Accepted** · weight 3 · Merge · Part 1, CHARM (slides 22-30) · Slides 26 and 29 (29 becomes 28)

Suggestion: Remove slide 26 and use its figure to explain the prediction on slide 29

Original:

~~~text
Slide 26 'CHARM predicts feedback from the task and the teacher': the CHARM figure (learning with human teachers, learning with CHARM oracles), USUAL ORACLES, the navy CHARM box and the line about interpreting teaching. Slide 29: two small diagrams (task statistics only, plus teacher traits) next to the prediction chart.
~~~

Accepted wording:

~~~text
Slide 26 is removed. On slide 29 the two small diagrams are replaced by the CHARM figure, in its version without feedback delay (figures/charm/experiment_figs/first_page_no_delay.png).
- Start: 'task statistics' outlined in violet, matching the 'Task stats only' bars that are on screen.
- Click 1 (the existing build): 'human characteristics' outlined in blue, with the CHARM bars, +23 points and the p-value.
- Caption: 'Each model predicts a person's rating from task statistics (rewards). CHARM also uses the person's questionnaire answers.'
Notes: '(≈50 s) How do we predict a person's feedback? Much of robot learning is tested with simulated oracles that compute feedback from the task alone, so differences between people are ignored. CHARM is a small neural network that predicts the rating a specific person would give. Its inputs are task statistics, here the rewards of the robot's behavior, and that person's questionnaire answers. If you predict a rating from task statistics alone, you get 33 percent on the five-point scale. [click] Add who the teacher is, from their questionnaire answers, and it jumps to 56 percent; for binary, from 79 to 87. One caveat I care about: a model like this should be used to interpret teaching, for example to rescale someone's feedback, never to decide whose teaching counts. And the cross-validation mixed feedback from the same people across train and test, so generalizing to brand-new teachers is future work.'
~~~

Hang's note: i want the orignial illustration on the second one kept as well

Note written with the suggestion: One slide now shows how the rating is predicted and how well it works. The figure is the authors' own. The outlines only point at the two inputs, in the chart's colors. Task statistics are rewards from a reward function (charm.tex line 111), so the caption says so. The sentence about not deciding whose teaching counts moves from the slide to the notes; add a note if you want it on the slide. Removes one slide.

Not used in a pattern: Decisions about slide structure, figures, pictures, and animation, which the slide guidelines of the talk cover.

### PN-R07

**Accepted** · weight 3 · Merge · Part 1, CHARM (slides 22-30) · Slides 27 and 28 (become one slide 27)

Suggestion: Remove feedback delay and merge slide 27 into slide 28

Original:

~~~text
Slide 27: the original correlation figure with three groups (feedback delay, feedback accuracy, absolute difference) and a long caption. Slide 28: redrawn bars for true reward (0.56, delay −0.004), robot experience (0.25 and −0.24) and education (0.16 and −0.12), three notes, and 'None of the characteristics lined up with rating delay.'
~~~

Accepted wording:

~~~text
One slide, 'Feedback depends on who is teaching', built on the authors' figure without the delay panel (figures/charm/correlation_no_delay.pdf).
- Start: the figure and 'The dashed line is the correlation between ratings and the true reward (r = 0.563). Against it, r above 0.1 is noteworthy.'
- Click 1: the Robot Experience bars outlined with 0.25 and −0.24, the rating-accuracy note (51.8%, SD 10.9%, best 74.5%) and the absolute-difference note.
- Click 2: the Education bars outlined with 0.16 and −0.12, and 'People with more robot experience or a related education gave ratings closer to the true reward.'
Every mention of delay goes: the −0.004 row, the delay sentence, and delay in the footer and the notes. The redrawn bars are replaced by the original figure.
Notes: slide 28's notes without the delay sentences, plus 'Each bar is one characteristic domain, against two properties of the ratings: accuracy, and absolute difference from the true reward.'
~~~

Hang's note: for the right side, do not just use words, use the bar chart

Note written with the suggestion: The figures folder already has the authors' no-delay version of this figure, so nothing was cropped or redrawn. The numbers are the ones on slide 28 now, from charm.tex. The two clicks keep slide 28's order. Removes one slide.

Used in: [Slide text in the presenter's voice](../hangs-writing-style-reference.md#slide-text-in-the-presenter-s-voice).

### PN-R08

**Accepted** · weight 1 · Animation · Part 1, CHARM (slides 22-30) · Slide 30 (becomes 29)

Suggestion: Takeaways of part 1: one conclusion per click

Original:

~~~text
The two conclusions on the right already come one per click, but the two bullets on the left ('Noisy demonstrations do not mean failed demonstrations.' and 'Adding teacher characteristics into feedback prediction lifted rating prediction from 33% to 56%') and the picture are on screen from the start.
~~~

Accepted wording:

~~~text
Click 1: DEMONSTRATION SIDETRACKS and its text, the first bullet, and a thin rust outline around the Demonstration Sidetracks half of the picture.
Click 2: FEEDBACK & CHARACTERISTICS and its text, the second bullet, and the outline moves to the Feedback & Characteristics half.
The bullet box is split in two so each bullet comes with its conclusion. The wording does not change, and the slide keeps 2 clicks.
~~~

Note written with the suggestion: Each conclusion now appears with its number and its half of the picture, so nothing on the slide runs ahead of what you are saying.

### PN-R09

**Accepted** · weight 1 · Animation · Part 2 (slides 33-43) · Slide 33 (becomes 32)

Suggestion: Each part of the figure appears with its text

Original:

~~~text
The whole figure and 'The task' are on screen from the start. Clicks add 'The clips', 'Repetition', 'The scales' and the question.
~~~

Accepted wording:

~~~text
The figure is cut into four layers from the same image (same frame, pixels unchanged), and each appears with its text.
- When the slide opens, without a click: top left, the robot and one clip, with 'The task.'
- Click 1: bottom left, the two sessions of 100 clips, with 'The clips.'
- Click 2: Human Study, the first-session row (binary and scalar), with 'The scales.'
- Click 3: the second-session row and the two consistency brackets, with 'Repetition.' and the figure caption.
- Click 4: the question.
'The scales' and 'Repetition' swap places, and the notes swap the same two sentences.
~~~

Note written with the suggestion: In the figure, the second session and the 'consistency within feedback type' bracket are what show the repetition, and they sit below the first-session row, so the scales come first. It also keeps the hidden repeat as the last step before the question. If you want to keep your order, add a note and I will show the whole right half with 'Repetition' and add 'The scales' on the next click.

### PN-R10

**Accepted** · weight 3 · Chart · Part 2 (slides 33-43) · Slide 36 (becomes 35)

Suggestion: Add a scalar feedback line to the progress chart (mean 90, SD 10)

Original:

~~~text
Only the progress curve, which appears on click 1 with the PROGRESS ASKS box.
~~~

Accepted wording:

~~~text
A green scalar feedback line at 90 across all six sub-tasks, with a light band from 80 to 100 (one SD) and the label 'scalar feedback: about 90 at every step (SD 10)'. It is on screen with 'SCALAR FEEDBACK ASKS' when the slide opens, together with the axes, the sub-task names and the step images.
Click 1: the PROGRESS ASKS box, then the progress curve wipes in from the left, with a small 'progress' label. Click 2 is unchanged.
The chart picture is split into a grid layer and the curve so the curve can draw on its own.
Notes add after the scalar question: 'For a clean run like this one, scalar ratings would stay around 90 at every step, with a standard deviation of about 10, whether the robot has just started or is almost done.'
~~~

Hang's note: but for the scalar value curve, do not use a straight line, use averge 90, std 10 ( not use interval) just change the values (remove the std area as well)

Note written with the suggestion: Mean 90 and SD 10 are your numbers. Like the progress curve on this slide, the line shows the expected shape for a clean run, not study data. I drew it as a flat line with a band rather than a jagged line, because a jagged line through made-up points would look like data. Green matches the scalar color on slides 35 and 40.

Not used in a pattern: Decisions about slide structure, figures, pictures, and animation, which the slide guidelines of the talk cover.

### PN-R11A

**Accepted** · weight 1 · Color · Part 2 (slides 33-43) · Slide 39 (becomes 38)

Suggestion: Finished vs. not finished, option A: deep green and rust

Original:

~~~text
'✓ Task finished' in navy pills and '✗ Not finished' in pale blue-grey pills (C5D2E1) that almost disappear on the background.
~~~

Accepted wording:

~~~text
Finished: deep green 1F5F40 with white text. Not finished: rust 935431 with white text. Both colors are from the Monet palette.
~~~

Note written with the suggestion: Green for done and rust for not done is the most familiar pairing, and both fills now have the same weight. For red-green color blindness the two are close in lightness, so the ✓ and ✗ carry the difference. Option B avoids that. Choose one of R11A and R11B.

### PN-R11B

**Accepted** · weight 1 · Color · Part 2 (slides 33-43) · Slide 39 (becomes 38)

Suggestion: Finished vs. not finished, option B: navy and rust

Original:

~~~text
'✓ Task finished' in navy pills and '✗ Not finished' in pale blue-grey pills (C5D2E1) that almost disappear on the background.
~~~

Accepted wording:

~~~text
Finished: navy 0F284C as now, with white text. Not finished: rust 935431 with white text. Both colors are from the Monet palette.
~~~

Note written with the suggestion: Blue against orange-brown stays distinct for color blindness, and the finished pills stay as they are. Choose one of R11A and R11B.

### PN-R12

**Accepted** · weight 1 · Animation · Part 2 (slides 33-43) · Slide 43 (becomes 42)

Suggestion: Takeaways of part 2: one conclusion per click

Original:

~~~text
The two conclusions on the left already come one per click, but the three bullets on the right and the picture are on screen from the start.
~~~

Accepted wording:

~~~text
Click 1: NOISE IN HUMAN FEEDBACK and its text, the first two bullets (scalar matches binary within ±2, STEADY beat binary by 4.2 return), and an outline around the 'Noise in Human Feedback' half of the picture.
Click 2: NEW MODALITY: PROGRESS and its text, the third bullet (progress spread 11.6 vs. 25.5), and the outline moves to the 'New Modality: Progress' half.
The bullet wording does not change, and the slide keeps 2 clicks.
~~~

Note written with the suggestion: The same pattern as slide 30 (R08).
