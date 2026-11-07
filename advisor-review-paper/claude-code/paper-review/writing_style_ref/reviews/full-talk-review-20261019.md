# Full talk: visual and text review, Oct 19

Review `full-talk-review-20261019` of the slides, from `../dissertation_presentation/wait_to_review/full-talk-review-20261019`. Decided between October 19, 2026 and October 19, 2026. Decisions files: `full-talk-review-20261019.decisions.20261019-124502.json`.

[All reviews](../review-decisions.md) · [Weighted signals](../preference-signals.md) · [Main reference](../hangs-writing-style-reference.md)

| Outcome | Decided by Hang | Not decided by Hang |
| --- | ---: | ---: |
| Accepted as suggested | 37 | 0 |
| Accepted with Hang's edit | 2 | 0 |
| Declined | 13 | 0 |
| Notes from Hang | 0 | |

5 of the 57 items had no decision when the review was imported.

### F01

**Declined** · weight 3 · Text · 1. Claims that do not match the dissertation · Slide 57

Suggestion: Real robot: 2 demos per person were annotated, not 6

Original, which stayed:

~~~text
2 annotators labeled 6 demos per person with progress
~~~

Declined suggestion:

~~~text
2 annotators labeled 2 demos per person (12 of 60) with progress
~~~

Note written with the suggestion: conclusion.tex:72-74 says 60 demonstrations, 12 of them annotated with progress, by 2 annotators. Your speaker notes on this slide already say two per person. The earlier wording review caught the same mismatch (S58-C01), but the fix only went into the separate wording copy.

Not used in a pattern: Fact, logic, equation, or caption corrections that Hang declined. They are kept so that the same correction is not offered again without new information.

### F02

**Declined** · weight 3 · Content · 1. Claims that do not match the dissertation · Slide 55

Suggestion: Ablation: removing completion shaping did not lower the return everywhere

Original, which stayed:

~~~text
Removing any term lowered the return. Potential shaping mattered in every setting, and completion shaping mattered most when demonstrations failed.

Notes: Removing any of them lowers the return; potential shaping matters in every setting, ...
~~~

Declined suggestion:

~~~text
Potential shaping mattered most in three of four settings. Completion shaping mattered most on PickPlaceCan (MH), where some demos failed, and not on Lift (PH).

Notes: Removing potential shaping lowers the return the most in three of the four settings, and the other terms matter too. Completion shaping is the exception. It matters most when some demonstrations fail, as in PickPlaceCan with mixed-quality data, and removing it did not lower the return on Lift with high-quality data.
~~~

Note written with the suggestion: phirl.tex:533-535 says the other terms gave significant decreases and 'The only exception is the completion shaping term'. The figure caption (phirl.tex:390) says removing potential shaping hurts most in three conditions and removing completion shaping hurts most in PickPlaceCan (MH). On Lift (PH), PHIRL without completion shaping scored 189.4 against 188.1 for full PHIRL, so 'removing any term lowered the return' is not true there.

Used in: [Measured results and plain premises on slides](../hangs-writing-style-reference.md#measured-results-and-plain-premises-on-slides).

### F03

**Declined** · weight 3 · Content · 1. Claims that do not match the dissertation · Slide 41

Suggestion: r = 0.83 is with the reward AIRL learned, not the task reward

Original, which stayed:

~~~text
Progress also correlated with task reward: r = 0.83 on average per participant.

Notes: Progress also correlated with the task reward, 0.83 on average.
~~~

Declined suggestion:

~~~text
Progress also correlated with the reward that AIRL learned from these demonstrations (r = 0.83 on average per participant, vs. 0.19 for scalar feedback).

Notes: Progress also correlated with the reward that AIRL learned from these demonstrations, 0.83 on average, compared with 0.19 for scalar feedback.
~~~

Note written with the suggestion: progress.tex:461-463: a reward function was trained on the public-space demonstrations with AIRL, and 'Progress was strongly correlated with the learned reward function (r = 0.83)', significantly higher than scalar feedback (r = 0.19). A committee member who knows the paper could ask which reward this is.

Used in: [Measured results and plain premises on slides](../hangs-writing-style-reference.md#measured-results-and-plain-premises-on-slides).

### F04

**Declined** · weight 3 · Content · 1. Claims that do not match the dissertation · Slide 6

Suggestion: Not every participant was a non-expert

Original, which stayed:

~~~text
We recruit participants in public spaces and through crowdsourcing, and none of them are robot experts.

Notes: ...or through crowdsourcing, and none of them were robot experts.
~~~

Declined suggestion:

~~~text
We recruit participants in public spaces and through crowdsourcing, and most of them are not robot experts.

Notes: ...or through crowdsourcing, and most of them were not robot experts.
~~~

Note written with the suggestion: You rejected two wider rewrites of this line on Oct 17 (S07-S01, S07-S02), so this only changes 'none' to 'most'. New evidence: only the ice cream study excluded people familiar with robots (progress.tex:361). CHARM did not screen, and slide 27 itself reports that people with more robot experience rated more accurately. Two of the six PHIRL real-robot demonstrators were system developers (the removed appendix, appendix-phirl.tex:314).

Used in: [Measured results and plain premises on slides](../hangs-writing-style-reference.md#measured-results-and-plain-premises-on-slides).

### F05

**Accepted** · weight 1 · Text · 1. Claims that do not match the dissertation · Slide 38

Suggestion: Failure scenario: the cup was dropped, not missed (choose one)

Original:

~~~text
Misses the cup at the very beginning
~~~

Accepted wording:

~~~text
Drops the cup at the very beginning
~~~

Note written with the suggestion: You changed 'Drops' to 'Misses' by hand on Sep 28. Everything else says drop: the figure label 'Failure: drop the cup' on slides 39 and 40, slide 39's callout ('the cup fell at the start'), the notes on 38 and 40, and progress.tex:152 ('the cup was dropped at the beginning'). If the video shows a missed grasp, reject this card and tell me, and I will change the other places instead.

### F06

**Accepted** · weight 1 · Content · 1. Claims that do not match the dissertation · Slide 52

Suggestion: PHIRL-online label budget matched the humans only in simulation

Original:

~~~text
Same label budget as the humans (400 or 600)

Notes: And we gave it the same number of labels the humans provided.
~~~

Accepted wording:

~~~text
As many labels as the humans gave (400 for PH, 600 for MH, in simulation)

Notes: In simulation, we added 400 online labels for PH and 600 for MH, matching the human annotation counts.
~~~

Note written with the suggestion: phirl.tex:510 gives the 400/600 extra labels for simulation. On the real robot PHIRL-online had 100 VLM labels against 120 human labels (removed appendix, appendix-phirl.tex:316), so 'same budget' needs 'in simulation'. The notes wording is your accepted S53-W02 from Oct 17.

### F07

**Accepted** · weight 1 · Content · 1. Claims that do not match the dissertation · Slide 63

Suggestion: The VLM result comes from a formative study with a VLM that was not fine-tuned

Original:

~~~text
A VLM's progress annotations already improved PHIRL in most cases, though less than human annotations did.

Footer: VLM figure: the formative study in the PHIRL chapter.
~~~

Accepted wording:

~~~text
In a formative study, VLM progress labels improved PHIRL in most settings, but less than human labels.

Footer: VLM panel from the PHIRL method figure. The formative study (PHIRL chapter) used Gemma 3 12B without fine-tuning.
~~~

Note written with the suggestion: phirl.tex:600-604: the formative study used Gemma 3 12B without fine-tuning and ReWiND-style prompts. The picture is the VLM-in-the-loop panel of PHIRL-online (fine-tuned), not a figure from that study, so the footer was wrong. A longer version of the sentence ran into the footer, so the fine-tuning detail goes in the footer.

### F08

**Declined** · weight 3 · Notes · 1. Claims that do not match the dissertation · Slide 54

Suggestion: PHIRL's lead on Lift with high-quality demos is small

Original, which stayed:

~~~text
Notes: PHIRL, in blue, beats all of them in all four settings, and the gap grows exactly where non-expert data hurts most: longer tasks and noisier demonstrations.
~~~

Declined suggestion:

~~~text
Notes: PHIRL, in blue, has a higher return than all of them in all four settings. On Lift with high-quality demos the gap is small, and it grows on the longer task and with noisier demonstrations.
~~~

Note written with the suggestion: The means are higher in all four settings, but on Lift (PH) PHIRL has 188 against 179 (AIRL-Pref) and 175 (Rank2Reward). The per-setting Welch tests are only in the removed appendix (appendix-phirl.tex:201), where these two comparisons were not significant (p = 0.26 and 0.124). Saying 'higher return' keeps the claim to what the bars show.

Used in: [Measured results and plain premises on slides](../hangs-writing-style-reference.md#measured-results-and-plain-premises-on-slides).

### F09

**Declined** · weight 3 · Text · 1. Claims that do not match the dissertation · Slide 19

Suggestion: Say what the 75 / 12 / 10% are shares of

Original, which stayed:

~~~text
by how many buttons or joystick axes were used at once
~~~

Declined suggestion:

~~~text
share of moving time steps, by how many buttons or joystick axes were used at once
~~~

Note written with the suggestion: sidetracks.tex:246: '75% of all timesteps only recorded a single action, whereas 12% recorded two actions and 10% recorded three actions'. The caption does not say these are time steps, so the bars could be read as shares of sidetracks or of people.

Used in: [Measured results and plain premises on slides](../hangs-writing-style-reference.md#measured-results-and-plain-premises-on-slides).

### F10

**Accepted with Hang's edit** · weight 4 · Content · 1. Claims that do not match the dissertation · Slide 42

Suggestion: Takeaway bullets: report the comparisons as measured

Original:

~~~text
Scalar matches binary self-consistency within ±2
STEADY beat binary feedback by 4.2 return
progress spread 11.6 vs. 25.5
~~~

Suggested:

~~~text
Within ±2, scalar self-agreement was similar to binary (n.s.)
STEADY reached a 4.2 higher return than binary feedback
Progress varied less across people (SD 11.6 vs. 25.5)
~~~

Hang's wording:

~~~text
Within ±2, scalar self-agreement was similar to binary (n.s.)
STEADY reached a higher return than binary feedback
Progress varied less across people (SD 11.6 vs. 25.5)
~~~

Note written with the suggestion: 'Matches' claims equivalence from a test that was not significant (p = 0.775). You made the same kind of change by hand on Sep 28 ('no detectable difference' to 'no statistical significance'). The third bullet starts lower-case and does not say what 11.6 and 25.5 are. Each bullet stays on one line, since the third one is a separate text box.

Used in: [Measured results and plain premises on slides](../hangs-writing-style-reference.md#measured-results-and-plain-premises-on-slides).

### F11

**Accepted** · weight 1 · Content · 1. Claims that do not match the dissertation · Slide 35

Suggestion: Effort: no significant difference, rather than no extra effort

Original:

~~~text
No extra effort: similar NASA-TLX workload, and 22 vs. 23 minutes to rate (online study I, n = 40).

Notes: And it costs nothing extra: in a first online study with 40 people, we found no difference in NASA-TLX workload, and rating took about 22 minutes versus 23 for scalar feedback.
~~~

Accepted wording:

~~~text
Similar effort: no significant difference in NASA-TLX workload or rating time (22 vs. 23 minutes, online study I, n = 40).

Notes: And it took similar effort. In a first online study with 40 people, we found no significant difference in NASA-TLX workload or rating time, about 22 minutes with progress and 23 with scalar feedback.
~~~

Note written with the suggestion: progress.tex:457 says 'No significant differences in workload or completion time were detected'. A test that finds no difference does not show 'no extra effort'. S03 offers the alternative of removing this line, since slide 37 covers the same study.

Used in: [Measured results and plain premises on slides](../hangs-writing-style-reference.md#measured-results-and-plain-premises-on-slides).

### V01

**Accepted** · weight 1 · Layout · 2. Visual fixes · Slide 39

Suggestion: Handwriting callouts fall back to a bold sans on 7 slides

Original:

~~~text
Caveat 20-25 pt on slides 18, 23, 28, 33, 39, 41 and 54 ('not just slips…', 'is it random noise…', '+23 points', 'within ±2…', 'look at Failure…', 'less than half!', 'PHIRL 117 vs. best baseline 36'). Caveat is not installed on this PC, so PowerPoint draws them in a bold fallback font.
~~~

Accepted wording:

~~~text
Nunito Sans bold 18 pt in the same rust color, same words and positions.
~~~

Note written with the suggestion: What you see in the renders is the fallback, not Caveat. Changing the font makes the slides look the same on every machine (D9). If you prefer the handwriting look, reject this card and install Caveat (free, SIL Open Font License) on the laptop you will present from. The proposed render of slide 23 also includes P23's new wording.

### V02

**Accepted** · weight 1 · Layout · 2. Visual fixes · Slide 36

Suggestion: Three titles and two labels in Calibri or the wrong case

Original:

~~~text
Titles on slides 14 ('Public Space Study for Data Collection') and 36 ('Progress') are Calibri 27, black, not bold. The labels 'Our Approach' (7) and 'THE Question' (10) are in mixed case. (Slide 7's title is V07.)
~~~

Accepted wording:

~~~text
Same words, in the deck's title style (Libre Baskerville bold 27 pt, navy 0F284C). Labels in capitals: 'OUR APPROACH', 'THE QUESTION'.
~~~

Note written with the suggestion: These are titles you retyped by hand on Sep 28. The theme stores no fonts, so the retyped text came out in Calibri (settings sheet, Fonts). Only the font and the case of the two labels change, not your wording. The render shows slide 36.

### V03

**Accepted** · weight 1 · Animation · 2. Visual fixes · Slide 40

Suggestion: Corrected: show 'recovers to 94.1' with the recovery click

Original:

~~~text
Click 3 shows 'Corrected. Progress dips while the robot spins without the stirrer, then recovers to 94.1.' while the curve still stops at step 13. The recovery curve only grows on click 4.
~~~

Accepted wording:

~~~text
Click 3: 'Corrected. Progress dips while the robot spins without the stirrer.'
Click 4 (with the recovery curve): a second line, 'Then it goes back for the stirrer, and progress recovers to 94.1.' Both leave with the Corrected caption on click 5. Still 5 clicks.
~~~

Note written with the suggestion: A2: show a callout only after the data it discusses. Your notes already split it this way ('[click] Corrected: progress dips ... [click] then recovers to 94 ...'). The static render shows all five stacked captions at once, as before. The click-by-click frames are in proposed/V03_steps.png.

### V04

**Declined** · weight 3 · Layout · 2. Visual fixes · Slide 16

Suggestion: Name the four sidetracks on slide 16

Original, which stayed:

~~~text
The names Exploration, Mistake, Alignment and Pause only appear as tiny italic text inside the icons.
~~~

Declined suggestion:

~~~text
Each caption starts with the name in bold: 'Exploration. Trying several degrees of freedom...', 'Mistake. ...', 'Alignment. ...', 'Pause. ...'.
~~~

Note written with the suggestion: The audience cannot read the names inside the icons from the back of the room, and slide 17 then uses the names as headings. Captions and icons stay where they are. The proposed render also includes P16's caption wording.

Not used in a pattern: Decisions about slide structure, figures, pictures, and animation, which the slide guidelines of the talk cover.

### V05

**Accepted** · weight 1 · Layout · 2. Visual fixes · Slide 51

Suggestion: Numbered circles to plain numbers

Original:

~~~text
Navy circles with white numbers on slides 15, 26, 33, 34 and 51, and 01-12 badges on slide 24.
~~~

Accepted wording:

~~~text
Plain navy numbers ('1.', '2.' ...) in the same place on 15, 26, 33, 34 and 51. On slide 24 the 01-12 numbers are removed and the factor names move left, since the order means nothing there.
~~~

Note written with the suggestion: Numbered circles and badges are on the guideline's list of generator-kit details (D4). Animations stay as they are (the circles are hidden, not deleted). The render shows slide 51.

### V06

**Accepted** · weight 1 · Layout · 2. Visual fixes · Slide 48

Suggestion: Comic labels: grammar error and 'Law of Force'

Original:

~~~text
The generated comic says 'Student validate solution with answers' and 'Teacher teaches the Law of Force at school', while the slide text says 'Newton's second law'.
~~~

Accepted wording:

~~~text
Cover the two labels with corrected ones in the comic's background color: 'Teacher teaches Newton's second law at school' and 'Student checks the answers'. The blackboard ('Law of Force (F=m·a)') is left as it is.
~~~

Note written with the suggestion: The label text is baked into the AI image, so it can only be covered or regenerated. If you prefer, reject this card and regenerate the comic with the corrected labels. The notes fix for 'law of force' is a separate card (N06).

### V07

**Accepted** · weight 1 · Layout · 2. Visual fixes · Slide 7

Suggestion: Slide 7 title in the title font needs two lines

Original:

~~~text
Learning from Both Human Feedback and Human Demonstrations (Calibri 27, black, not bold)
~~~

Accepted wording:

~~~text
Learning from human feedback and demonstrations (Libre Baskerville bold 27 pt, navy)
~~~

Note written with the suggestion: Your title, set in the deck's title font, wraps to a second line and runs into the photos. Dropping 'Both' and the second 'Human' keeps it on one line. If you want to keep every word, edit the wording here, or reject and I can set it at 23 pt instead, which fits but is smaller than the other titles.

### W01

**Accepted** · weight 1 · Text · 3. Wording and grammar · Slide 33

Suggestion: Grammar: 'for twice'

Original:

~~~text
They rated the same 100 clips for twice, without being told
~~~

Accepted wording:

~~~text
They rated the same 100 clips twice, without being told
~~~

Note written with the suggestion: Error-only fix. The rest of your wording stays.

### W02

**Accepted with Hang's edit** · weight 4 · Content · 3. Wording and grammar · Slide 36

Suggestion: Grammar in the 'What we learned' and progress boxes

Original:

~~~text
Ratings depends on the rater. Feedback values depends on both...
...that do not contribute to task completion while may not be harmful to the task completion.
Grounded with the task. It describes the task's state with start point and end point as reference.
~~~

Suggested:

~~~text
Ratings depend on the rater. Feedback values depend on both...
...that do not contribute to task completion, although they may not harm the task.
Grounded in the task. It describes the task's state, with the start and the end as references.
~~~

Hang's wording:

~~~text
Ratings depend on the rater. Feedback values depend on both...
...that do not contribute to task completion, although they may not harm the task.
Grounded in the task. It describes the task's state, with the start and the end states as references.
~~~

Note written with the suggestion: Error-only fixes (subject-verb agreement, an incomplete 'while' clause, 'grounded in', missing articles). The wording is otherwise yours.

Used in: [Slide text in the presenter's voice](../hangs-writing-style-reference.md#slide-text-in-the-presenter-s-voice).

### W03

**Declined** · weight 3 · Content · 3. Wording and grammar · Slide 47

Suggestion: First panel: say what is hard about a dense reward

Original, which stayed:

~~~text
A dense reward
for pouring sprinkles over a cake
~~~

Declined suggestion:

~~~text
Hand-craft a dense reward
but tuning it takes a lot of time
~~~

Note written with the suggestion: The other two panels name a way to get the reward and its problem ('but non-experts take sidetracks', 'but people have to stay in the loop'). The first one only names the example. Your notes already say 'hand-crafting a dense one takes a lot of tedious tuning', and the photo still shows the sprinkles and the cake.

Used in: [Measured results and plain premises on slides](../hangs-writing-style-reference.md#measured-results-and-plain-premises-on-slides).

### W04

**Accepted** · weight 1 · Text · 3. Wording and grammar · Slide 56

Suggestion: Lift-Drop-Loop text: literal wording, matching the curves

Original:

~~~text
A PPO policy trained on AIRL's reward learns to lift the block and drop it, over and over, to farm reward.
AIRL keeps paying out. PHIRL's reward falls at every drop, because progress falls.
~~~

Accepted wording:

~~~text
A PPO policy trained on AIRL's reward learned to lift the block and drop it, again and again.
AIRL's reward dips only a little at each drop. PHIRL's reward falls at every drop, because progress falls.
~~~

Note written with the suggestion: 'Farm reward' and 'keeps paying out' are figurative (writing reference, Literal wording). The new second line says what the orange curve shows, and matches your notes ('AIRL's reward dips only a little'). The paragraph build stays the same.

Used in: [Slide text in the presenter's voice](../hangs-writing-style-reference.md#slide-text-in-the-presenter-s-voice).

### W05

**Accepted** · weight 1 · Text · 3. Wording and grammar · Slide 64

Suggestion: Example: 'push less' vs. 'lifts with less force'

Original:

~~~text
Example: people differ, and a robot cannot see their needs. A child may push less and need the box held lower.
~~~

Accepted wording:

~~~text
Example: people differ, and a robot cannot see their needs. A child may lift with less force and need the box held lower.
~~~

Note written with the suggestion: The timeline below says 'lifts with less force', and the task is lifting a box.

### W06

**Accepted** · weight 1 · Text · 3. Wording and grammar · Slide 41

Suggestion: Spread across people, not disagreement

Original:

~~~text
DISAGREEMENT BETWEEN PEOPLE (AVERAGE SD)
~~~

Accepted wording:

~~~text
SPREAD ACROSS PEOPLE (AVERAGE SD)
~~~

Note written with the suggestion: Each passerby rated their own demonstration, so the SD is how much the ratings spread across people, not people disagreeing about the same clip (progress.tex:420).

### W07

**Accepted** · weight 1 · Text · 3. Wording and grammar · Slide 39

Suggestion: 'look at Failure' callout: mark the reason as a likely one

Original:

~~~text
Scalar ends at 91: the last motions looked fine. Progress ends at 23: the cup fell at the start.
~~~

Accepted wording:

~~~text
Scalar feedback ends at 91, likely because the last motions looked fine. Progress ends at 23, since the cup fell at the start.
~~~

Note written with the suggestion: Writing reference, quick reference 4: untested explanations are possibilities. The study did not ask why people gave 91. Also removes two colons (quick reference 11).

### W08

**Accepted** · weight 1 · Content · 3. Wording and grammar · Slide 60

Suggestion: Spell out VLA and WAM

Original:

~~~text
Footer: Dissertation, Chapter 8 - Future work
~~~

Accepted wording:

~~~text
Footer: VLA: vision-language-action model. WAM: world action model.
Dissertation, Chapter 8 - Future work
~~~

Note written with the suggestion: W7: explain every abbreviation where it appears. Please check that 'world action model' is what you mean by WAM. The footer puts notes first, then the source.

### W09

**Accepted** · weight 1 · Content · 3. Wording and grammar · Slide 37

Suggestion: Spell out BF

Original:

~~~text
Footer: MD, PD, TD, P, E, F: mental, physical and temporal demand, ...
~~~

Accepted wording:

~~~text
Footer: BF: Bayes factor. MD, PD, TD, P, E, F: mental, physical and temporal demand, ...
~~~

Note written with the suggestion: The slide reports BF = 0.444 and BF < 1 without saying what BF is (progress.tex:162 defines it as the Bayes factor).

### W10

**Accepted** · weight 1 · Content · 3. Wording and grammar · Slide 51

Suggestion: Completion rule: 'out-earn'

Original:

~~~text
Completion. Successful demos out-earn failed ones.
Footer: Hinge ℓ with margin m ≥ 0; a demonstration counts as failed if its final progress is below 90.
~~~

Accepted wording:

~~~text
Completion. Successful demos earn more reward than failed ones.
Footer: Hinge ℓ with margin m ≥ 0. A demonstration counts as failed if its final progress is below 90.
~~~

Note written with the suggestion: Says the actual relation instead of a figurative verb, and replaces a semicolon with a period (writing reference 11).

### N01

**Accepted** · weight 1 · Notes · 4. Speaker notes and click cues · Slide 3

Suggestion: Slide 3 has 2 clicks but 1 cue in the notes

Original:

~~~text
[click] But robots are heading into homes, ... So robots inevitably need to learn from, and adapt to, people who are not experts. There's a practical upside too: non-expert data is much cheaper to collect, and models trained on it can be more robust to the messiness of the real world.
~~~

Accepted wording:

~~~text
[click] But robots are heading into homes, ... So robots need to learn from, and adapt to, people who are not experts. [click] And their teaching will be noisier, and more challenging for robots to learn from.
~~~

Note written with the suggestion: Click 2 shows the bottom line ('...which means their teaching will be noisier...'), but the notes never say it. The 'practical upside' sentence is what slide 4 shows next, so it moves out of slide 3 (A3).

### N02

**Accepted** · weight 1 · Notes · 4. Speaker notes and click cues · Slide 10

Suggestion: Slide 10 notes are a copy of slide 5's

Original:

~~~text
(≈40 s) Everyone in the field agrees that human teaching is imperfect ... But the question is: why? [click] The common assumption is ... [click] My dissertation takes a different view ...
~~~

Accepted wording:

~~~text
(≈15 s) So human teaching is noisy, and everyone in the field accepts that. The question for this part is why. Where do these imperfections come from, and are they just random?
~~~

Note written with the suggestion: Slide 10 ('Human teaching is noisy. But why?') has no clicks, but its notes have two [click] cues and repeat slide 5 almost word for word, including 'My dissertation takes a different view'.

### N03

**Accepted** · weight 1 · Notes · 4. Speaker notes and click cues · Slide 17

Suggestion: Slide 17 has a click but no cue

Original:

~~~text
None of these breaks the task, but none of them makes progress either.
~~~

Accepted wording:

~~~text
[click] These behaviors do not directly advance task completion, although they may help the demonstrator control the robot.
~~~

Note written with the suggestion: The bottom line appears on a click. The new sentence is your accepted S16-S01 from Oct 17, which also keeps the notes in step with the slide's line.

### N04

**Accepted** · weight 1 · Notes · 4. Speaker notes and click cues · Slide 56

Suggestion: Slide 56 notes narrate Touch-and-Stay, which is not on the slide

Original:

~~~text
During training we ran into two classic reward hacks. ... because AIRL keeps rewarding the lift and never punishes the drop. ... [click] In Touch-and-Stay, a policy trained on the environment reward just pokes the can forever ... so no pay.
~~~

Accepted wording:

~~~text
During training we ran into a classic reward hack. ... because AIRL keeps rewarding the lift and barely punishes the drop. (The Touch-and-Stay paragraph and its [click] are removed.)
~~~

Note written with the suggestion: The slide has 4 clicks and the notes have 5 cues. The last cue would wait for a click that never comes. Your notes also say 'AIRL's reward dips only a little', so 'never punishes' contradicts them.

### N05

**Accepted** · weight 1 · Notes · 4. Speaker notes and click cues · Slide 49

Suggestion: Slide 49 notes explain the four rules that slide 51 explains again

Original:

~~~text
(≈60 s) ... Alignment uses four rules. Delta: ... Magnitude: ... Potential: ... And completion: a successful demo should earn more total reward than a failed one, whatever its length. Optionally, ...
~~~

Accepted wording:

~~~text
(≈40 s) ... and an alignment step that shapes that reward to agree with progress. I'll go through both steps next. Optionally, ...
~~~

Note written with the suggestion: Slides 50 and 51 walk through both steps, and 51's notes cover the same four rules. Cutting them here saves about 20 seconds.

### N06

**Accepted** · weight 1 · Notes · 4. Speaker notes and click cues · Slide 48

Suggestion: Notes say 'law of force', the slide says Newton's second law

Original:

~~~text
A teacher explains the law of force in class;
~~~

Accepted wording:

~~~text
A teacher explains Newton's second law in class;
~~~

Note written with the suggestion: You changed the slide text to Newton's second law. The notes still use the old name (the earlier wording review had the same fix, S49-W01).

### P13

**Accepted** · weight 1 · Text · 5. Accepted on Oct 17, never reached this deck · Slide 13

Suggestion: Slide 13 bottom line (S06-W05)

Original:

~~~text
Oversimplifying human teaching can mean more data or worse robots.
~~~

Accepted wording:

~~~text
Oversimplifying human teaching can increase data requirements or reduce robot performance.
~~~

Note written with the suggestion: On Oct 17 you accepted this in the wording review (batch 20261017-212326). It was applied only to the separate copy output/Hang_dissertation_full_talk_Claude_wording_applied.pptx, so this deck never got it. Accept to apply it here, or reject if you changed your mind.

### P15

**Accepted** · weight 1 · Text · 5. Accepted on Oct 17, never reached this deck · Slide 15

Suggestion: Slide 15 step 3 (S14-W02)

Original:

~~~text
One second or more without input counts as a pause. Changes of task phase were marked to study when sidetracks happen.
~~~

Accepted wording:

~~~text
At least one second without input counts as a pause. Task-phase changes were marked to study when sidetracks occurred.
~~~

Note written with the suggestion: On Oct 17 you accepted this in the wording review (batch 20261017-212326). It was applied only to the separate copy output/Hang_dissertation_full_talk_Claude_wording_applied.pptx, so this deck never got it. Accept to apply it here, or reject if you changed your mind.

### P16

**Accepted** · weight 1 · Content · 5. Accepted on Oct 17, never reached this deck · Slide 16

Suggestion: Slide 16 captions (S15-G01, S15-S01)

Original:

~~~text
A brief, harmless control error, like pushing the wrong direction
No input for a while: reacting, thinking, re-planning
~~~

Accepted wording:

~~~text
A brief, harmless control error, like pushing in the wrong direction
No control input for at least one second
~~~

Note written with the suggestion: On Oct 17 you accepted this in the wording review (batch 20261017-212326). It was applied only to the separate copy output/Hang_dissertation_full_talk_Claude_wording_applied.pptx, so this deck never got it. Accept to apply it here, or reject if you changed your mind.

### P18

**Accepted** · weight 1 · Notes · 5. Accepted on Oct 17, never reached this deck · Slide 18

Suggestion: Slide 18 notes (S17-W01, S17-S01)

Original:

~~~text
They're super noisy and multi-policy, everyone found their own way. ... That's noise with a purpose.
~~~

Accepted wording:

~~~text
The trajectories vary widely, and people found different ways to complete the task. ... These behaviors suggest that some apparent noise reflects how people check their control of the robot.
~~~

Note written with the suggestion: On Oct 17 you accepted this in the wording review (batch 20261017-212326). It was applied only to the separate copy output/Hang_dissertation_full_talk_Claude_wording_applied.pptx, so this deck never got it. Accept to apply it here, or reject if you changed your mind.

### P19

**Accepted** · weight 1 · Content · 5. Accepted on Oct 17, never reached this deck · Slide 19

Suggestion: Slide 19 captions (S18-W01, S18-W02)

Original:

~~~text
Often happened within 4 s of a sub-task change
Alignments started and ended within 0.1 m of a target: where precision matters
~~~

Accepted wording:

~~~text
Often occurred within 4 s of a task-phase change
73% of alignments started and ended within 0.1 m of a target object, where precise control was needed
~~~

Note written with the suggestion: On Oct 17 you accepted this in the wording review (batch 20261017-212326). It was applied only to the separate copy output/Hang_dissertation_full_talk_Claude_wording_applied.pptx, so this deck never got it. Accept to apply it here, or reject if you changed your mind. You had hand-written the first caption on Sep 28 and accepted this change on Oct 17.

### P21

**Accepted** · weight 1 · Text · 5. Accepted on Oct 17, never reached this deck · Slide 21

Suggestion: Slide 21 last sentence (S20-W01)

Original:

~~~text
Alignment happened more where controlling the robot required accuracy.
~~~

Accepted wording:

~~~text
Alignments were more common near target objects, where precise control was needed.
~~~

Note written with the suggestion: On Oct 17 you accepted this in the wording review (batch 20261017-212326). It was applied only to the separate copy output/Hang_dissertation_full_talk_Claude_wording_applied.pptx, so this deck never got it. Accept to apply it here, or reject if you changed your mind.

### P23

**Accepted** · weight 1 · Content · 5. Accepted on Oct 17, never reached this deck · Slide 23

Suggestion: Slide 23 question (S22-S01)

Original:

~~~text
is it random noise, or is it the teacher?

Notes: So the question is: is it noise, or is it the teacher?
~~~

Accepted wording:

~~~text
How are teacher characteristics associated with feedback?

Notes: So the question is how teacher characteristics are associated with feedback.
~~~

Note written with the suggestion: On Oct 17 you accepted this in the wording review (batch 20261017-212326). It was applied only to the separate copy output/Hang_dissertation_full_talk_Claude_wording_applied.pptx, so this deck never got it. Accept to apply it here, or reject if you changed your mind. The notes change was not part of S22-S01. It keeps the spoken question the same as the slide. The font of this line is covered by V01.

### P24

**Accepted** · weight 1 · Content · 5. Accepted on Oct 17, never reached this deck · Slide 24

Suggestion: Slide 24 factor texts and bottom line (S23-S02, S23-S03, S22-S02)

Original:

~~~text
Domain knowledge improves clarity and depth
Reduces feedback depth and quality
We left them out on purpose, so the results cannot contribute to discrimination.

Notes: ...so the results could never be used to discriminate against anyone.
~~~

Accepted wording:

~~~text
Domain knowledge may help people describe task performance
May limit feedback detail and quality
We left them out on purpose, to avoid discrimination from the results.

Notes: ...to avoid discrimination from the results.
~~~

Note written with the suggestion: On Oct 17 you accepted this in the wording review (batch 20261017-212326). It was applied only to the separate copy output/Hang_dissertation_full_talk_Claude_wording_applied.pptx, so this deck never got it. Accept to apply it here, or reject if you changed your mind. S22-S02 was for the notes. The slide's bottom line makes the same promise, so it gets the same wording here. The accepted 'Relevant domain knowledge...' ran into the next factor, so 'Relevant' is dropped.

### P32

**Accepted** · weight 1 · Content · 5. Accepted on Oct 17, never reached this deck · Slide 32

Suggestion: Slide 32 caption and facts (S33-W01, S33-G01, S33-W02)

Original:

~~~text
The robot and one clip (left), and the two groups that rated both sessions (right).
Participants were not told that the clips repeat.
The scales. Good or bad, or 0 to 10 with no negative range, so the scale does not suggest a split.
~~~

Accepted wording:

~~~text
The robot and an example clip (left), and the two participant groups that completed both rating sessions (right).
Participants were not told that the clips would repeat.
The scales. Binary good/bad or scalar 0–10. The scalar scale had no negative values, so it did not impose a positive/negative division.
~~~

Note written with the suggestion: On Oct 17 you accepted this in the wording review (batch 20261017-212326). It was applied only to the separate copy output/Hang_dissertation_full_talk_Claude_wording_applied.pptx, so this deck never got it. Accept to apply it here, or reject if you changed your mind. The bold label 'The scales.' is kept, since the slide now labels each fact. The longer scales text needs one more line, so 'Repetition.' moves down 22 pt.

### P37

**Accepted** · weight 1 · Notes · 5. Accepted on Oct 17, never reached this deck · Slide 37

Suggestion: Slide 37 notes (S38-S01)

Original:

~~~text
So progress is no harder to give than a score.
~~~

Accepted wording:

~~~text
This study did not detect a difference in the effort required to give progress or scalar feedback.
~~~

Note written with the suggestion: On Oct 17 you accepted this in the wording review (batch 20261017-212326). It was applied only to the separate copy output/Hang_dissertation_full_talk_Claude_wording_applied.pptx, so this deck never got it. Accept to apply it here, or reject if you changed your mind.

### P41

**Accepted** · weight 1 · Content · 5. Accepted on Oct 17, never reached this deck · Slide 41

Suggestion: Slide 41 title, failure line and notes (S42-W01, S42-S02, S42-S03)

Original:

~~~text
Non-experts can rate their own demonstrations well
final progress for every failed demo: all failures caught

Notes: so the last progress value alone caught all of the failures.
~~~

Accepted wording:

~~~text
Non-experts’ progress ratings reflect task completion
final progress for every failed demonstration in this study

Notes: so a final-progress threshold of 90 identified every failed demonstration in this sample.
~~~

Note written with the suggestion: On Oct 17 you accepted this in the wording review (batch 20261017-212326). It was applied only to the separate copy output/Hang_dissertation_full_talk_Claude_wording_applied.pptx, so this deck never got it. Accept to apply it here, or reject if you changed your mind.

### P58

**Accepted** · weight 1 · Content · 5. Accepted on Oct 17, never reached this deck · Slide 58

Suggestion: Slide 58 title and notes (S59-G01, S59-W03)

Original:

~~~text
Learn reward function with progress and demonstrations

Notes: With progress on just 20 percent of the demonstrations, it learned more robust rewards, with the biggest gains on long tasks and noisy demonstrations, and it held up on a real robot.
~~~

Accepted wording:

~~~text
Learn a reward function with progress and demonstrations

Notes: With progress annotations on 20 percent of demonstrations, PHIRL outperformed the baselines in simulation and on the real robot. The largest simulation gains were on the longer task and the mixed-quality dataset.
~~~

Note written with the suggestion: On Oct 17 you accepted this in the wording review (batch 20261017-212326). It was applied only to the separate copy output/Hang_dissertation_full_talk_Claude_wording_applied.pptx, so this deck never got it. Accept to apply it here, or reject if you changed your mind.

### P60

**Declined** · weight 3 · Text · 5. Accepted on Oct 17, never reached this deck · Slide 60

Suggestion: Slide 60 title (S61-W02)

Original, which stayed:

~~~text
Robots that learn from more, and from everyone
~~~

Declined suggestion:

~~~text
Robots that learn from more people and more sources
~~~

Note written with the suggestion: On Oct 17 you accepted this in the wording review (batch 20261017-212326). It was applied only to the separate copy output/Hang_dissertation_full_talk_Claude_wording_applied.pptx, so this deck never got it. Accept to apply it here, or reject if you changed your mind. Slide 60 is your own design. Only the title text changes.

Used in: [Slide text in the presenter's voice](../hangs-writing-style-reference.md#slide-text-in-the-presenter-s-voice).

### P65

**Accepted** · weight 1 · Text · 5. Accepted on Oct 17, never reached this deck · Slide 65

Suggestion: Slide 65 loop label (S67-S01)

Original:

~~~text
the skills and the data format both improve with use
~~~

Accepted wording:

~~~text
the skills and the data format could improve through use
~~~

Note written with the suggestion: On Oct 17 you accepted this in the wording review (batch 20261017-212326). It was applied only to the separate copy output/Hang_dissertation_full_talk_Claude_wording_applied.pptx, so this deck never got it. Accept to apply it here, or reject if you changed your mind. No skill has run on a robot with real users yet (your notes), so the loop is still a plan.

### S01

**Declined** · weight 3 · Structure · 6. Optional cuts and flags · Slide 26

Suggestion: Slides 25 and 26 describe the same CHARM procedure

Original, which stayed:

~~~text
Slide 25 'Measuring who is teaching' (photo, 28-item chart, 46 / 4,655 / 2) and slide 26 'What each passerby did' (questionnaire, watch, rate every 30 actions) cover the same procedure, and both notes tell it.
~~~

Declined suggestion:

~~~text
Remove slide 26. Keep slide 25, add 26's details (six trajectories from agents trained for 500, 1,000 or 2,000 epochs, the 5 s timeout) to 25's notes, and move 26's scale citations to 25's footer. The progress bar is recomputed.
~~~

Note written with the suggestion: S6: cut what repeats. Saves about 40 seconds of a talk that runs about 46 minutes at a speaking pace (6,505 words of notes). Slide 25 keeps the real photo. Not built in the proposed copy, so there is no proposed render.

Used in: [Slide text in the presenter's voice](../hangs-writing-style-reference.md#slide-text-in-the-presenter-s-voice).

### S02

**Declined** · weight 3 · Structure · 6. Optional cuts and flags · Slide 33

Suggestion: Slide 33's list repeats slide 32

Original, which stayed:

~~~text
Steps 1-3 on slide 33 (90 crowdworkers, 45 + 45, the same 100 clips twice) repeat the design slide 32 just showed.
~~~

Declined suggestion:

~~~text
Keep only '18,000 ratings collected to answer: did people agree with themselves?' and the time line, and give the chart more room.
~~~

Note written with the suggestion: W3 and S6. Your notes for 33 also retell the design. If you accept this, V05 no longer matters for slide 33. Not built in the proposed copy.

Used in: [Slide text in the presenter's voice](../hangs-writing-style-reference.md#slide-text-in-the-presenter-s-voice).

### S03

**Declined** · weight 3 · Structure · 6. Optional cuts and flags · Slide 35

Suggestion: Alternative to F11: remove the effort line from slide 35

Original, which stayed:

~~~text
Slide 35 ends with the effort result on click 2. Slide 37, two slides later, shows the same study in detail.
~~~

Declined suggestion:

~~~text
Remove the line and its click from slide 35 (and the matching notes sentence). Choose either this or F11.
~~~

Note written with the suggestion: Says the effort result once, on the slide that shows its data (37). Not built in the proposed copy.

Used in: [Slide text in the presenter's voice](../hangs-writing-style-reference.md#slide-text-in-the-presenter-s-voice).

### S04

**Declined** · weight 3 · Flag · 6. Optional cuts and flags · Slide 22

Suggestion: SpongeBob and Patrick: check before posting the slides

Original, which stayed:

~~~text
Slide 22 uses SpongeBob and Patrick cut-outs.
~~~

Declined suggestion:

~~~text
Keep them for the live talk if you like. Before a PDF of the slides is posted publicly, replace them, for example with the blue stick figure from slide 10.
~~~

Note written with the suggestion: They are Nickelodeon characters (F10, check the rights to outside images). This is a flag, not a change, so nothing is rendered.

Not used in a pattern: A flag about the rights to an image, not wording.
