# Full talk: slides 45-68 (nine requests)

Review `full-talk-slides45-68` of the slides, from `../dissertation_presentation/wait_to_review/full-talk-slides45-68-review`. Decided between October 18, 2026 and October 18, 2026. Decisions files: `full-talk-slides45-68.decisions.20261018-121028.json`.

[All reviews](../review-decisions.md) · [Weighted signals](../preference-signals.md) · [Main reference](../hangs-writing-style-reference.md)

| Outcome | Decided by Hang | Not decided by Hang |
| --- | ---: | ---: |
| Accepted as suggested | 17 | 0 |
| Accepted with Hang's edit | 0 | 0 |
| Declined | 1 | 0 |
| Notes from Hang | 4 | |

1 of the 19 items had no decision when the review was imported.

### SL-R01

**Declined** · weight 5 · Layout · Request 1 - slide 45, re-organize · Slide 45 - Whole slide

Suggestion: Group the four findings into demonstrations and feedback

Original, which stayed:

~~~text
Four columns, each with a picture, a heading and a sentence. The pictures have different sizes and sit at different heights. The STEADY box plot is 176 x 56 pt. The down arrow touches 'feedback.' at the end of column 3. One sentence at the bottom: 'This suggests inferring a reward from all the demonstrations and aligning it with progress on a few.'
~~~

Declined suggestion:

~~~text
- Two labels over the columns: DEMONSTRATIONS (columns 1-2) and FEEDBACK (columns 3-4), each with a thin line under it.
- All four pictures sit on one baseline, left-aligned with their text. The STEADY plot is as wide as its column (184 pt). Original ratios are kept.
- Headings and sentences are unchanged.
- The bottom sentence is split under the two groups, with one arrow each:
  under DEMONSTRATIONS: 'Infer a reward from all the demonstrations'
  under FEEDBACK: 'Align it with progress on a few'
- Clicks stay at 4, as in the notes: column 2, column 3 (with the FEEDBACK label), column 4, then both arrows and both halves. Notes unchanged.
~~~

Hang's note: not what i want in the original slides

Note written with the suggestion: The two halves of the conclusion come from different parts of the talk. Putting each half under the findings it comes from shows how the first two parts lead to PHIRL. The words are the same as the old sentence, minus 'This suggests'.

Not used in a pattern: Decisions about slide structure, figures, pictures, and animation, which the slide guidelines of the talk cover.

### SL-R02

**Accepted** · weight 1 · Layout · Request 2 - slide 49, re-organize and original ratios · Slide 49 - Whole slide

Suggestion: Even rows, and the robot photos at their original 3:2 ratio

Original:

~~~text
Four robot photos are squeezed: row 1 is 5.6% too wide, row 2 3.8% too wide, the row 3 demo photo 18% too narrow and the annotator photo 29% too narrow. The robot text column is 143 pt wide, so its lines wrap to four lines.
~~~

Accepted wording:

~~~text
- Three rows with equal spacing between the comic's top and bottom (photo tops at 154, 258 and 362 pt). Each row: school step - arrow - photo - robot step, with the text centred on the photo.
- Rows 1 and 2: the whole photo at its own 3:2 ratio (126 x 84 pt), no cropping.
- Row 3: the two photos are cropped, not squeezed, to fill 70 x 84 and 52 x 84 pt. The demo crop keeps the hand and the jar; the annotator crop keeps the person holding the signs.
- Robot text column 184 pt wide. Comic, wording, clicks (3) and notes unchanged.
All pictures checked after the build: displayed ratio = source ratio for every picture.
~~~

Note written with the suggestion: Fixes the stretched photos and gives the robot text room, without changing the content.

### SL-R03

**Accepted** · weight 1 · Grammar · Request 2 - slide 49, re-organize and original ratios · Slide 49 - Text 5

Suggestion: Optional grammar fix in the first school step

Original:

~~~text
The teacher explains the Newton’s second rule in class
~~~

Accepted wording:

~~~text
The teacher explains Newton’s second law in class
~~~

Note written with the suggestion: Not requested. 'the Newton's' has an extra 'the', and the comic and the notes call it the law of force, so 'law' matches them. Reject to keep the current line.

### SL-R04

**Accepted** · weight 1 · Layout · Request 3 - slide 50, remove the right side · Slide 50 - Right side (Four alignment rules)

Suggestion: Remove the four alignment rules and enlarge the figure

Original:

~~~text
Right side: 'Four alignment rules' with numbered circles 1-4 (Delta, Magnitude, Potential, Completion), shown on the slide's only click.
~~~

Accepted wording:

~~~text
- Remove the heading, the four circles and the four rule texts (13 shapes and their click).
- The PHIRL figure grows from 521 to 800 pt wide, centred, at its own ratio.
- The three captions stay word for word, spread under the figure.
- Notes: only the '[click]' before 'Delta' is removed. The spoken explanation of the four rules stays, so you can still say it if asked.
~~~

Note written with the suggestion: The slide now has no clicks, so the one [click] cue goes too.

### SL-R05

**Accepted** · weight 1 · Layout · Request 4 - slide 53, remove the results · Slide 53 - Right side (bars and legend)

Suggestion: Remove the results chart

Original:

~~~text
Right side: legend (PHIRL / PHIRL-online) and three pairs of bars (Lift PH 188.1 vs 205.1, PickPlaceCan MH 117.0 vs 147.3, real robot 73 vs 84), shown on click 1.
~~~

Accepted wording:

~~~text
- Remove the legend, labels, bars and values (19 shapes).
- The VLM-in-the-loop figure grows from 400 to 560 pt wide; the four bullets move to its right, wording unchanged.
- The bottom line stays (see R06).
- Notes: remove '[click] It helps consistently: on Lift ... from 73 to 84 pom-poms.' and change the time from (≈45 s) to (≈35 s). One click is left, for the bottom line.
~~~

Note written with the suggestion: The same values are also on slide 55 (Lift and PickPlaceCan) and slide 58 (real robot), so the talk still has them.

### SL-R06

**Accepted** · weight 1 · Layout · Request 4 - slide 53, remove the results · Slide 53 - Takeaway text

Suggestion: Also remove the bottom result line

Original:

~~~text
With no human labels, off-the-shelf Gemma 3 still improved Lift, though less than human progress.
~~~

Accepted wording:

~~~text
Remove the line and its click. Notes: remove '[click] We also tried with no human labels at all: ... though less than real human progress.' and change the time to (≈30 s). The slide then has no clicks.
~~~

Note written with the suggestion: This line is also a result, but it is not on the right side, so it is a separate choice. Accept to remove it, reject to keep it. The After image shows R05 and R06 together.

### SL-R07

**Accepted** · weight 1 · Video · Request 5 - slide 54, Lift and PickPlaceCan videos · Slide 54 - Left picture and dataset text

Suggestion: Replace the picture with four real dataset clips (2 tasks x 2 data qualities)

Original:

~~~text
A still image with three Lift frames and three PickPlaceCan frames from the paper figure, and below it 'PH: 200 demonstrations from one proficient operator' and 'MH: 300 from six operators (2 worse, 2 okay, 2 better)'.
~~~

Accepted wording:

~~~text
A 2 x 2 grid of looping videos (128 x 128 pt each, original 1:1 ratio):
- columns: PH (header '200 demos from one proficient operator') and MH (header '300 demos from six operators')
- rows: Lift and PickPlaceCan (labels turned sideways on the left)
- MH clips: one of the two 'worse' operators
The dataset text moves into the two headers. Footer gets a first line: 'Videos: playback of the robomimic PH and MH datasets (MH: one of the two “worse” operators), from the robomimic study page (robomimic.github.io/study).' The clips start with the slide; the two clicks for BASELINES and TRAINING are unchanged.
~~~

Note written with the suggestion: Found online: the robomimic study page shows playback of exactly the PH and MH datasets PHIRL used for Lift and Can (files playback_lift_se, playback_lift_mh_worse_1, playback_can_se, playback_can_mh_worse_1_trim, 512 x 512, 20 fps, 26-63 s). The grid matches the title: two tasks, two data qualities. Rights: the robomimic code is MIT licensed, but the website has no license, so credit is in the footer. Fine for the live talk; check before posting slides or a recording publicly. If you prefer clips we render ourselves from the datasets, say so in a note and I will set up robosuite in a separate Desktop folder. Choose R07 or R08.

### SL-R09

**Accepted** · weight 3 · Wording · Request 6 - slide 61, simpler text · Slide 61 - Text 25 (under 'Non-expert data for VLA/WAM')

Suggestion: Shorter VLA/WAM text

Original:

~~~text
Large VLA/WAM policies still requires high quality data (UMI, ego centric, and Dagger), while real users could produce massive meaningful data
~~~

Accepted wording:

~~~text
Large VLA/WAM models still need high-quality data (UMI, egocentric, DAgger). Real users could provide much more data.
~~~

Hang's note: also re-orgnize it a bit

Note written with the suggestion: Two short sentences. Fixes 'policies still requires', spells DAgger and egocentric the usual way, and replaces 'massive meaningful data' with a plain comparison. Style reference: complete clauses, one job per sentence.

Used in: [Slide text in the presenter's voice](../hangs-writing-style-reference.md#slide-text-in-the-presenter-s-voice).

### SL-R10

**Accepted** · weight 1 · Wording · Request 6 - slide 61, simpler text · Slide 61 - Text 28 (under 'Agentic HRI')

Suggestion: Shorter agentic HRI text, without 'very strong capability'

Original:

~~~text
For high level control, agentic AI has demonstrated very strong capability in self-correction and long-horizon task planning. This can also be applied to human-robot-interaction. 
~~~

Accepted wording:

~~~text
AI agents can plan long-horizon tasks and correct their own mistakes. The same ideas can apply to human-robot interaction.
~~~

Note written with the suggestion: 'has demonstrated very strong capability' is a strong claim for a future-work slide; 'can' says what agents do without grading it. Style reference: claim strength matches the evidence.

Used in: [Future work and the closing slide in a talk](../hangs-writing-style-reference.md#future-work-and-the-closing-slide-in-a-talk).

### SL-R11

**Accepted** · weight 1 · Notes · Request 6 - slide 61, simpler text · Slide 61 - Speaker notes

Suggestion: Optional: bring the notes in line with the middle column

Original:

~~~text
...Teaching that's easy for everyone: interfaces that reduce the control burden behind many sidetracks, showing the robot's own progress estimate so people only correct what's wrong, and including children, older adults and people with disabilities. And agentic HRI: as robots become agents, non-expert teaching moves up a level, to correcting plans and judging outcomes, and tools like CHARM, STEADY and progress can help close that loop with real people.
~~~

Accepted wording:

~~~text
...Non-expert data for VLA and WAM models: these large models still need high-quality data, collected with UMI grippers, egocentric video or DAgger, while real users could provide much more data. And agentic HRI: AI agents can already plan long-horizon tasks and correct their own mistakes, and the same ideas can apply to human-robot interaction.
~~~

Note written with the suggestion: Not requested. The notes still describe the old middle column ('Teaching that's easy for everyone'), which the slide no longer shows. The first part of the notes, up to 'the way PHIRL uses progress', stays. Reject to keep your notes as they are.

### SL-R12

**Accepted** · weight 1 · Wording · Request 6 - slide 62, simpler text · Slide 62 - Idea text

Suggestion: Shorter reason for annotating failed demonstrations first

Original:

~~~text
They can shape completion, give negative reward samples, and widen data coverage.
~~~

Accepted wording:

~~~text
They give negative examples and cover more of the task.
~~~

Note written with the suggestion: Plain words for 'negative reward samples' and 'data coverage'. 'Shape completion' moves to the notes, which already say it.

Used in: [Slide text in the presenter's voice](../hangs-writing-style-reference.md#slide-text-in-the-presenter-s-voice).

### SL-R13

**Accepted** · weight 1 · Wording · Request 6 - slide 62, simpler text · Slide 62 - Budget heading

Suggestion: Shorter comparison heading

Original:

~~~text
Test it under the same budget of human time
~~~

Accepted wording:

~~~text
Compare under the same human time
~~~

Note written with the suggestion: Same meaning in fewer words. The heading and list move up to close the gap left by the shorter text.

Used in: [Slide text in the presenter's voice](../hangs-writing-style-reference.md#slide-text-in-the-presenter-s-voice).

### SL-R14

**Accepted** · weight 1 · Wording · Request 6 - slide 62, simpler text · Slide 62 - Strategy list

Suggestion: Shorter strategy list

Original:

~~~text
- random, as in PHIRL
- low-quality first
- where the reward model is most uncertain
- where the reward disagrees most with progress
- high-quality first
~~~

Accepted wording:

~~~text
- random, as in PHIRL
- low-quality first
- most uncertain reward
- reward disagrees with progress
- high-quality first
~~~

Note written with the suggestion: Items 3 and 4 shortened; the notes keep the full description of each strategy.

### SL-R15

**Accepted** · weight 1 · Wording · Request 6 - slide 62, simpler text · Slide 62 - Budget note

Suggestion: Remove the 'Time, not label count' line

Original:

~~~text
Time, not label count: a long or unclear demonstration takes longer to annotate.
~~~

Accepted wording:

~~~text
(delete the passage)
~~~

Note written with the suggestion: The heading already says 'same human time', and the notes explain why. Its click effect goes with it; the slide keeps 3 clicks.

### SL-R16

**Accepted** · weight 1 · Delete slide · Request 7 - slide 65, remove · Slide 65 - Whole slide

Suggestion: Remove slide 65, Human-in-the-loop agentic robotics

Original:

~~~text
Slide 65 'Human-in-the-loop agentic robotics' (preprint figure, four points, 4 clicks).
~~~

Accepted wording:

~~~text
(delete the passage)
~~~

Note written with the suggestion: The deck goes from 69 to 68 slides and the progress bar is recomputed on every slide. Its one idea that the next slide needs, what an agent does (plans, calls skills, observes, revises), moves to slide 66 (R17). Slides 66, 67 and 68 become 65, 66 and 67.

### SL-R17

**Accepted** · weight 1 · Layout · Request 8 - slides 66-67, agentic HRI · Slide 66 - Whole slide and notes

Suggestion: Slide 66: what agentic HRI is, with the child example

Original:

~~~text
Lead 'People differ, and a robot cannot see their needs...', the label 'One interaction, recorded as a trajectory: who did what, in which order, with what outcome', the child/robot lanes, and 'Each record also keeps what the camera tells about the user, ... and the robot's embodiment.' 3 clicks. The notes describe the planned data format.
~~~

Accepted wording:

~~~text
Title unchanged. Top, visible from the start:
  'An agent plans a task, calls skills, observes the outcome, and revises its plan.'
  'Agentic HRI also includes the person in the robot's planning.' (bold: includes the person in the robot's planning)
Click 1: 'Example: people differ, and a robot cannot see their needs. A child may push less and need the box held lower.' with the same child/robot lanes. Click 2: outcome.
Removed: the 'recorded as a trajectory' label and the 'Each record also keeps...' line (the data format). Footer: 'An illustrative example, not collected data. ...'
Notes: '(≈40 s) Beyond this dissertation, one direction is agentic HRI. An agent plans a task, calls skills, such as policies learned from human teaching, observes the outcome, and revises its plan. Planning is comparatively simple when no people are involved. With people, users' internal states are unknown, and they differ in their preferences, needs, and capabilities. So agentic HRI also includes the person in the robot's planning. [click] For example, in a collaborative lifting task, a child may provide less force than an adult. The robot keeps its side lower and asks whether this works, [click] and the box is carried, held lower.'
~~~

Note written with the suggestion: Answers 'what is agentic HRI' with the definition from the Future Work section and keeps your example. The data-format details (work in progress) go.

### SL-R18

**Accepted** · weight 3 · Layout · Request 8 - slides 66-67, agentic HRI · Slide 67 - Whole slide and notes

Suggestion: Slide 67: benefits of agentic HRI

Original:

~~~text
'Seeding robot skills from 20 years of HRI papers': the counts 983 -> 823 -> 716 -> 51, a four-step skill-update loop, and 'So far the knowledge base, the trajectories and the seed skills are built, but no skill has run on a robot with real users yet...'. 3 clicks.
~~~

Accepted wording:

~~~text
Title 'Benefits of agentic HRI'. Four rows, each a heading, one line and a small picture already in the deck:
1. Adapts to each person - It can include the person in its planning, such as holding the box lower for a child. (child + robot cut-outs)
2. Decides when and how to ask - It can choose when and what to ask from people, and how to phrase the request. (“like this?”)
3. Starts from what HRI already knows - Seed skills can come from 20 years of HRI papers instead of a cold start. (983 HRI papers)
4. Improves with use - Interactions are recorded, and a skill changes only when outcomes improve or the user approves. (loop arrows)
Row 1 visible, rows 2-4 one click each (3 clicks). Footer keeps the HRI-paper source and WikiSkill.
Notes: '(≈40 s) What could agentic HRI offer non-expert users? First, it can adapt to each person, for example by holding the box lower for a child. [click] Second, it can decide when and what to ask from people, and how to phrase the request. [click] Third, it does not have to start from scratch. Seed skills can come from findings in 20 years of HRI papers. So far, 983 main-track papers have been condensed into 51 seed behavior skills. [click] And it can improve with use. Following the loop of WikiSkill, each interaction is recorded in a standard format, and a skill changes only when the outcomes improve or the user approves the change. No skill has run on a robot with real users yet.'
~~~

Hang's note: the improve with use can still keep the wikiskill style update flow

Note written with the suggestion: The four benefits are the ones named in the agentic HRI part of the Future Work section. 'Can' keeps them as expected benefits. The counts of what has been built move to the notes, and the notes keep 'No skill has run on a robot with real users yet'. If you prefer slides 66 and 67 merged into one, say so in a note.

Used in: [Future work and the closing slide in a talk](../hangs-writing-style-reference.md#future-work-and-the-closing-slide-in-a-talk).

### SL-R19

**Accepted** · weight 3 · Layout · Request 9 - slide 68, how the parts build on each other · Slide 68 - Whole slide and notes

Suggestion: General takeaway as a chain: each part leads to the next

Original:

~~~text
Three side-by-side columns (1. Model, 2. Mitigate, 3. Leverage) with small arrows between the pills, a heading, a sentence and a method tag each, and the bottom line 'Once modeled, imperfect teaching provides information a robot can learn from.'
~~~

Accepted wording:

~~~text
The three parts stacked top to bottom, each: pill + method tag under it | heading + one line.
1. Model - Imperfect teaching has structure. 'Sidetracks follow the task, and feedback depends on who is teaching.'
   arrow down: 'Knowing where the imperfections come from shows how to ask for feedback.'
2. Mitigate - How feedback is requested matters. 'Progress asks about the task instead of the robot, and it varied less across people.'
   arrow down: 'Progress gives a consistent signal to align a learned reward with.'
3. Leverage - Demonstrations and feedback complement each other. 'PHIRL learns from all demonstrations, failed ones included, with progress on a few.'
Bottom line unchanged. Clicks: link 1 + part 2, link 2 + part 3, bottom line (3, as before).
Notes: '... First, imperfect teaching has structure. Sidetracks follow the task, and feedback depends on who is teaching. [click] Knowing where the imperfections come from showed us how to ask for feedback. Progress asks about the task rather than the robot, and it varied less across people, even on imperfect demonstrations. [click] That consistency made progress a signal that a learned reward can be aligned with. PHIRL learns from every demonstration, failed ones included, with progress on just 20 percent of them. [click] So once we understand it, imperfect teaching is not just noise. It is information a robot can learn from.'
~~~

Hang's note: add animation to show one stage at a time

Note written with the suggestion: The two arrow lines say how each part builds on the one before, which the current slide only shows with small arrows. The headings are your current ones. The lines are shorter and higher-level (no '20%' on the slide). The links follow the Overall Discussion: teachers differ mostly in the magnitude of their feedback (Part 1), which motivated STEADY's per-teacher rescaling, and PHIRL uses changes in progress to constrain the learned reward.

Used in: [Future work and the closing slide in a talk](../hangs-writing-style-reference.md#future-work-and-the-closing-slide-in-a-talk).
