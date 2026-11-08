# Full talk: more from the old talk

Review `full-talk-migration` of the slides, from `../dissertation_presentation/wait_to_review/full-talk-migration-review`. Decided between October 17, 2026 and October 17, 2026. Decisions files: `full-talk-migration.decisions.20261017-184132.json`.

[All reviews](../review-decisions.md) · [Weighted signals](../preference-signals.md) · [Main reference](../hangs-writing-style-reference.md)

| Outcome | Decided by Hang | Not decided by Hang |
| --- | ---: | ---: |
| Accepted as suggested | 6 | 0 |
| Accepted with Hang's edit | 0 | 0 |
| Declined | 11 | 0 |
| Notes from Hang | 2 | |

### M01

**Declined** · weight 3 · Notes · Motivation and the question (7-12) · Slide 7 - speaker notes

Suggestion: Bridge into slide 8 with the old 'more than one' line

Original, which stayed:

~~~text
[click] So messy, real teachers are the setting here, not the exception.
~~~

Declined suggestion:

~~~text
[click] So messy, real teachers are the setting here, not the exception. And when people say more than one, they usually mean two.
~~~

Note written with the suggestion: The old talk ended the notes of its 'Our Goal' slide (old 6) with this line. It is a small casual moment, and it sets up slide 8, which opens with the two ways people teach robots. Notes only, the slide does not change.

Used in: [Slide text in the presenter's voice](../hangs-writing-style-reference.md#slide-text-in-the-presenter-s-voice).

### M02

**Accepted** · weight 1 · Animation · Motivation and the question (7-12) · Slide 8

Suggestion: Bring back the chain link between the two photos

Original:

~~~text
Both photos, both captions and the bottom line appear together. The slide has no clicks.
~~~

Accepted wording:

~~~text
The two photos and their captions appear first. On one click, the chain-link icon from old slide 8 appears between the photos, together with the bottom line 'Together they reduce the data need for feedback and relax the quality bar for demonstrations' (wording unchanged). One [click] is added to the notes before 'Prior work, for example Palan and colleagues'.
~~~

Note written with the suggestion: In the old talk (slides 7 and 8) the link appearing between the photos was the moment that introduced combining feedback and demonstrations. The current slide says it in text only. The icon is the old talk's own image.

### M03

**Declined** · weight 3 · New slide · Motivation and the question (7-12) · New slide 12, after 'One task, many ways to demonstrate it'

Suggestion: Add the feedback half of the question (old slide 11)

New text, placed next to this passage:

~~~text
(no anchor)
~~~

Declined suggestion:

~~~text
New slide 12 'One clip, four different ratings' (label THE QUESTION), adapted from old slide 11.
- Left: the frame of the nut assembly clip used on slide 11.
- Right: the four people with the bubbles Good, Excellent, Bad and Fine, appearing one by one.
- Bottom line, matching slide 11: 'It is widely accepted that human feedback varies from person to person.'
- Notes: 'It is also widely accepted that feedback varies from person to person. Show the same clip to four people, and you can get four different answers.'
~~~

Note written with the suggestion: The old talk set up the question in three beats: demonstrations vary (old 10), feedback varies (old 11), why? (old 12). The current deck has the first and the third, and the feedback half only comes back on slide 22. Slide 22 keeps its copy of the four people, which then works as a callback. Add a note if you would rather drop them from slide 22. Adds one slide.

Not used in a pattern: Decisions about slide structure, figures, pictures, and animation, which the slide guidelines of the talk cover.

### M04

**Declined** · weight 3 · Animation · Motivation and the question (7-12) · Slide 12

Suggestion: Make slide 12 the old picture-only 'Why?' pause

Original, which stayed:

~~~text
Two lines restate slides 11 and 12 ('It's widely accepted that demonstrations are noisy...', '...and that feedback varies from person to person.'), then 'COMMON ASSUMPTION: It's random noise...' and a navy box 'THIS DISSERTATION: Much of it has structure...'. Two clicks.
~~~

Declined suggestion:

~~~text
Keep the label and title ('THE Question', 'Human teaching is noisy. But why?') and the 'Why?' drawing with the shrugging figure, larger and centred as on old slide 12. Remove the four text blocks and the navy box, and remove the two [click] cues from the notes. The notes keep the spoken common assumption and the dissertation's view.
~~~

Note written with the suggestion: Old slide 12 was a pause with only the drawing, after the two examples. The text on the current slide repeats slides 11 and 6 ('Simple assumptions can backfire'), and the navy box is the kind of card the guidelines warn about (D4, D5). Depends on M03, since without it nothing on screen mentions feedback before 'why?'.

Not used in a pattern: Decisions about slide structure, figures, pictures, and animation, which the slide guidelines of the talk cover.

### M05

**Accepted** · weight 1 · Text · Part 1, model (13-28) · Slide 13

Suggestion: Label the four steps of the ice cream task

Original:

~~~text
The 'Ice Cream Topping Adding Task' strip shows four robot drawings with no labels.
~~~

Accepted wording:

~~~text
A short caption under each drawing, from old slide 14:
'Teleoperate with an Xbox controller' / 'Pick up a topping jar' / 'Move to the ice cream' / 'Pour the toppings'
~~~

Note written with the suggestion: Old slide 14 labelled each step, which shows what a successful demonstration is without extra text (notes.txt item 1 asks for the success criterion). The rest of the slide stays.

### M06

**Declined** · weight 3 · Reorder · Part 1, model (13-28) · Slides 13-17

Suggestion: Show 'What we actually collected' right after the setup

Original, which stayed:

~~~text
Slide 13 already reveals '34 / 40 succeeded on their first and only try'. The trajectory animation comes four slides later (slide 17 'Successful, but far from optimal'), after the codebook and the four examples.
~~~

Declined suggestion:

~~~text
Follow the old order (old 14, then old 15).
1. Slide 13 ends with 'One attempt each, no retries'. Its notes add: 'Since the task is easy, we expected similar paths and a few failures.'
2. New slide 14 'What we actually collected' (old 15 title): the trajectory animation from slide 17, larger. After it plays, one line per click: 'Many different policies', 'Noisy', '34 of 40 succeeded on their first and only try'. Footer, from the progress chapter: 'Five of the six failed demos: 3 dropped the jar on the way to the ice cream, 2 did not pick it up.'
3. Slide 17 keeps its title and numbers (48%, 14.5, not just slips...) and shows the last frame of the animation as a still, since the paths were already shown.
~~~

Note written with the suggestion: In the old talk the paths were the surprise right after the setup, so the audience sees the mess before it is explained. The failure reasons are from progress.tex ('Non-Expert Demonstrations Are Multi-Policy and Noisy'), which does not say why the sixth demo failed. Left out: the old notes' line that no learning algorithm, including Diffusion Policy, could learn from these demos, since the dissertation does not report it. Adds one slide.

Not used in a pattern: Decisions about slide structure, figures, pictures, and animation, which the slide guidelines of the talk cover.

### M07

**Declined** · weight 3 · Animation · Part 1, model (13-28) · Slides 19-20

Suggestion: Merge slides 19 and 20 into the old 'not randomly distributed' build

Original, which stayed:

~~~text
Slide 19 shows the frequency and timing panels over two clicks. Slide 20 shows the alignment 3D panel on its own.
~~~

Declined suggestion:

~~~text
One slide 'Sidetracks are not randomly distributed' (old 18-20 title) with the three original panels in the old layout: frequency (top left), timing (bottom left), alignment positions (right). Each click brightens one panel and its caption and fades the other two.
1. 'All 40 demonstrators took sidetracks (14.5 ± 10.5 per demonstration).'
2. '54.7% of sidetracks happened in windows around task-phase changes, which cover 40% of the time steps.'
3. '73% of alignments started and ended within 0.1 m of a target object.'
The line 'Random noise injected into perfect demonstrations would not reproduce this structure.' stays as the last click. Slide 20 is removed.
~~~

Note written with the suggestion: The old talk made one point from three original figures on one slide, so the findings read as one argument. The figures stay unchanged, only their opacity changes between clicks. Removes one slide. Slide 18 (the redrawn WHEN / WHERE / HOW summary) then overlaps with this slide. Add a note if you also want slide 18 dropped.

Not used in a pattern: Decisions about slide structure, figures, pictures, and animation, which the slide guidelines of the talk cover.

### M08

**Declined** · weight 5 · Original figure · Part 1, model (13-28) · Slide 28

Suggestion: Use the original CHARM accuracy figure and the two prediction diagrams

Original, which stayed:

~~~text
The right chart ('How well can a model predict each person's rating?') is redrawn from rectangles: Random 20% / 50%, Task stats only 32.6% / 79.4%, + teacher traits 55.8% / 87.0%.
~~~

Declined suggestion:

~~~text
Put the original figure from old slide 27 (Random, task statistics only, CHARM, for five-point and binary, with *** marks) in its place at its original ratio (also in Dissertation/figures/charm/feedback_accuracy_comparison.pdf). Above it, the two small diagrams from old slide 27: 'Predict with task statistics only' (the clip) and 'Predict with task statistics and attributes' (the clip with the person and questionnaire), each pointing to 'Feedback'. Keep '+23 points' and 'Both gains p < 0.001 (paired t-tests, 10-fold CV)', and keep two clicks.
~~~

Hang's note: current 28 could be separate into 2 tho. fill in a bit more results for correlation.  and for the right side (second slide), the original illustration of how predicition works can come in.

Note written with the suggestion: The old talk used the paper's figure, and the guidelines prefer original figures to charts redrawn from shapes (F1, D4). The two diagrams show what adding the teacher means. The figure has no value labels, so the numbers would be said aloud or kept as a small caption. The left chart is unchanged.

Not used in a pattern: Decisions about slide structure, figures, pictures, and animation, which the slide guidelines of the talk cover.

### M09

**Declined** · weight 5 · Original figure · Part 2, mitigate (33-40) · Slide 33

Suggestion: Use the original self-agreement figure

Original, which stayed:

~~~text
Self-agreement bars are redrawn from rectangles (76.3%, 25.2%, 58.2%, 77.7%) and appear over four clicks.
~~~

Declined suggestion:

~~~text
Use the original consistency figure from old slide 31 (box and violin plots for Binary, Scalar ±0, ±1 and ±2, with the significance brackets). Keep the four clicks by uncovering one plot at a time with background-coloured masks, and keep the four percentages as small labels above the plots.
~~~

Hang's note: but significance can be added tho

Note written with the suggestion: Same reason as M08. The original also shows the spread across participants, which the bars hide, and 'within ±2: no statistical significance' is the 'ns' bracket in the figure.

Used in: [Measured results and plain premises on slides](../hangs-writing-style-reference.md#measured-results-and-plain-premises-on-slides).

### M10

**Declined** · weight 3 · Reorder · Part 2, mitigate (33-40) · Slides 35-36

Suggestion: Motivate progress before defining it (swap slides 35 and 36)

Original, which stayed:

~~~text
Slide 35 ('Progress: how much of the task is done?', the scalar vs. progress question and the expected curve) comes before slide 36 ('Progress', which starts with WHAT WE LEARNED SO FAR).
~~~

Declined suggestion:

~~~text
Swap slides 35 and 36. The talk then follows the old order (old 33, then 34): the three things learned so far, progress as the answer, and then how its question differs from scalar feedback. Slide 35's notes already open with 'The difference is in the question', which reads as a follow-up.
~~~

Note written with the suggestion: The old talk opened this part with the three problems (old 33 'New Teaching Modality') and only then introduced progress, so progress arrives as an answer. Today it is defined on 35 and motivated on 36. No content changes.

Not used in a pattern: Decisions about slide structure, figures, pictures, and animation, which the slide guidelines of the talk cover.

### M11

**Accepted** · weight 1 · Animation · Part 2, mitigate (33-40) · Slide 36

Suggestion: Pair each problem with its answer, one click at a time

Original:

~~~text
Two clicks. Click 1 shows the three 'what we learned' columns. Click 2 shows the definition, the three dog drawings and all three rust boxes at once.
~~~

Accepted wording:

~~~text
Five clicks, as in old slides 33-37.
1. The three columns.
2. The definition and the three dog drawings.
3-5. One pair at a time: 'Direction, not scale' with 'Informative', then 'Ratings depends on the rater' with 'Grounded with the task', then 'Detours' with 'No progress, no penalty'. The current pair stays dark, and the other columns and boxes fade to about 35%.
Three [click] cues go into the notes, before 'The changes in progress carry the direction', 'It's grounded in the state of the task' and 'And a harmless but unproductive move'.
~~~

Note written with the suggestion: The old build matched each problem to the property of progress that answers it, which is the reasoning behind progress. The arrows on the current slide show the pairing, but all three answers appear at once. Text and layout stay as they are.

### M12

**Accepted** · weight 1 · Animation · Part 2, mitigate (33-40) · Slide 40

Suggestion: Show each scenario's video frame with its curves

Original:

~~~text
Five clicks grow one scenario's curves at a time. The sentences on the right add up into a list of five, and the slide shows no frame from the videos.
~~~

Accepted wording:

~~~text
Add the matching video frame from old slides 39-43 (the same frames as on slide 38) at the top right, and swap it on each click together with the curves. Below it, show only the current scenario's sentence, so each click fades out the previous sentence as the curves already do. Still five clicks, and the notes stay as they are.
~~~

Note written with the suggestion: In the old talk each scenario had its own slide with a frame of the robot at that moment (for example the dropped cup), so people could see what was being rated. The current build already fades curves, and the frame and single sentence follow the same pattern.

### M13

**Accepted** · weight 1 · Animation · Part 3, leverage (47-57) · Slide 47

Suggestion: Tell the reward problem one picture and one line at a time

Original:

~~~text
Three photos, each with a heading and a 17-20 word paragraph ('Sparse rewards provide little guidance...', 'Inverse RL infers the reward...', 'Combining feedback and demonstrations...'), over three clicks.
~~~

Accepted wording:

~~~text
Keep the photos, headings and clicks, and cut each paragraph to one line, close to old slides 51-55:
- 'A dense reward' / 'for pouring sprinkles over a cake'
- 'Learn it from demonstrations' / 'but non-experts take sidetracks'
- 'Add human feedback' / 'but people have to stay in the loop'
On the last photo, add the old talk's circular arrows (old 55) on the same click as its caption. The paragraph detail stays in the notes, which already say it.
~~~

Note written with the suggestion: The old talk told this problem with one picture and one sentence per click, ending on the loop arrows over the feedback photo. The current slide has the same pictures and clicks, but about 60 words of paragraph text.

### M14

**Accepted** · weight 1 · Animation · Part 3, leverage (47-57) · Slide 48

Suggestion: Build the robot side of the intuition from our own photos

Original:

~~~text
Three rust text boxes: 'People demonstrate the task', 'The robot infers a reward from all the demonstrations (inverse RL)', 'It aligns that reward with progress labels on a few annotated demos, and repeats'.
~~~

Accepted wording:

~~~text
Replace the three rust boxes with the photos from old slides 59-61, one per comic row, each with the current box text as a plain caption.
1. The demonstration photo (a hand guiding the gripper with the sprinkles jar).
2. The robot at the cake with the circular arrows.
3. The person holding the rating paddles next to the demonstration photo (the labels as the answer key).
Same three clicks.
~~~

Note written with the suggestion: The old talk built the robot side from photos of our own robot, so the school story lands on a real setup. The rust boxes are the card style the guidelines warn about (D4, D5). The old 3D reward plot is left out, since it looks like data but does not come from a study.

### M15

**Declined** · weight 3 · Animation · Part 3, leverage (47-57) · Slide 49

Suggestion: Show the PHIRL figure large and reveal it region by region

Original, which stayed:

~~~text
The PHIRL figure takes about a third of the slide, next to three captions and a numbered list of the four alignment rules (one click).
~~~

Declined suggestion:

~~~text
The figure fills most of the slide and is revealed in the order the method runs, as in old slides 63-66, one line per click:
1. Demonstrations - 'Collect demonstrations, and label 20% of them with progress.'
2. Adversarial reward learning - 'Learn a reward with AIRL.'
3. Reward shaping with progress - 'Align the reward with progress, using four rules.'
4. VLM in the loop - 'PHIRL-online: a fine-tuned VLM labels the robot's rollouts.'
Regions not yet shown sit under background-coloured masks. The four-rule list moves out, since slide 51 shows the rules with their equations. The notes get four [click] cues at the matching sentences.
~~~

Note written with the suggestion: The old talk walked through the figure in the order the method runs. Slides 50-52 then zoom into the same regions, so each part is seen first in context and then in detail. The figure itself is unchanged.

Not used in a pattern: Decisions about slide structure, figures, pictures, and animation, which the slide guidelines of the talk cover.

### M16

**Declined** · weight 3 · Original figure · Part 3, leverage (47-57) · Slide 54

Suggestion: Use the original simulation results figure

Original, which stayed:

~~~text
Four groups of bars redrawn from rectangles with values (205, 188, 170...), two clicks, and the callout 'PHIRL 117 vs. best baseline 36'.
~~~

Declined suggestion:

~~~text
Use the original performance comparison figure from old slide 68 (top row of Dissertation/figures/phirl/Results/Results.png) at its original ratio. Keep the two clicks by masking the PHIRL and PHIRL-online bars in each group and uncovering them in turn, and keep 'PHIRL 117 vs. best baseline 36' as a callout after the figure.
~~~

Note written with the suggestion: Same reason as M08. Slide 55 already shows rows 2 and 3 of the same original figure, so this makes the two slides match. The original has error bars, which the redrawn bars do not show. The other values would no longer be printed, so the callout carries the number the notes stress.

Not used in a pattern: Decisions about slide structure, figures, pictures, and animation, which the slide guidelines of the talk cover.

### M17

**Declined** · weight 3 · Original figure · Part 3, leverage (47-57) · Slide 57

Suggestion: Use the original real-robot chart

Original, which stayed:

~~~text
Horizontal bars redrawn from rectangles (84, 73, 62, 58, 54, 39), one click.
~~~

Declined suggestion:

~~~text
Use the original real-robot bar chart from old slide 72 (Dissertation/figures/phirl/Results/real_robot_results.png) at its original ratio, in place of the redrawn bars. Keep the title, photos and caption, and the one click.
~~~

Note written with the suggestion: Same reason as M08. The original chart already prints the values above the bars.

Not used in a pattern: Decisions about slide structure, figures, pictures, and animation, which the slide guidelines of the talk cover.
