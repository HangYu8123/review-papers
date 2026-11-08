# Writing style library, initial version (proposed)

A library of how Hang Yu's papers are written: the words, the phrasings, the sentence shapes and the ways of telling the story. It is meant to be looked up while writing or revising the dissertation, so that new text sounds like the papers.

Every entry is a proposal. Decide each one in `review.html` in this folder: accept keeps the entry, reject removes it, and "Edit the wording" changes it. Nothing here has been applied to the dissertation.

## How to read an entry

- **In the papers** lists the forms that occur, with approximate counts over the six papers in parentheses.
- **Examples** are quoted from the paper sources. `[CHARM:56]` means line 56 of the CHARM source file (table below). Citations are left out, `…` marks words left out, and *italics* stand for `\textit{}`.
- **Form** is the reusable shape, with slots in square brackets.
- **In the dissertation** is the form proposed for the dissertation. It differs from the paper form where Hang has already chosen a different wording (impersonal voice, measured claims, settled terms).
- **Shown in** names a proposed change in the dissertation that uses the entry (the `APP` items on the review page).

## Sources

| Key | Paper | File under `reference_papers/` |
| --- | --- | --- |
| CHARM | CHARM (RO-MAN 2025) | `CHARM/ROMAN 2025.tex` |
| SIDE | Demonstration Sidetracks | `Demonstration_sidetracks/main.tex` |
| STEADY | Scalar vs. binary feedback and STEADY | `STEADY/IEEEexample.tex` |
| PROG | Progress (RO-MAN 2024) | `Progress/Ro-MAN 2024.tex` |
| PH-ABS, PH-INT, PH-BG, PH-METH, PH-EXP, PH-CON | PHIRL (CoRL 2026 submission) | `PHIRL/CoRL_2026_main.tex`, `introduction.tex`, `background.tex`, `methodology.tex`, `experiment.tex`, `conclusion.tex` |
| RSS | RSS Pioneers 2026 prospectus (single author) | `prospectus/RSS Pioneers 2026.tex` |

Counts come from the running text of these files, about 23,600 words and about 1,000 sentences. Comments, figures, tables and equations were left out. They are approximate and are given to show which form is the usual one, not as targets.

All papers except the prospectus have co-authors, so the library describes the voice of the papers, which is the voice the dissertation chapters started from. Slips of grammar in the papers are not part of the library.

## The voice in one paragraph

The papers state what was done, what was found and why it matters, in that order and in plain words. A sentence usually starts with its subject ("We" opens about one sentence in five) and has about 20 words. The usual connectors are "However,", "Thus,", "Moreover,", "For instance," and "To …,". Claims about observations are firm ("We found that"), and claims about reasons are tentative ("This is likely due to"). The argument almost always runs the same way: prior work makes a simplifying assumption about human teaching, a study with non-experts shows what the assumption misses, a key insight is stated in one italic sentence, and a method follows from it. Imperfect teaching is described as something with structure and reasons, never as a fault of the teacher.

## Vocabulary

### VOC-01 · The people who teach the robot

**Use for.** Naming the human side of teaching.

**In the papers.**

- "non-experts", "non-expert users", "non-expert demonstrators", "non-expert participants" (about 78, the default noun)

- "human teachers" for statements about teaching in general

- "participants" inside a study; "demonstrators" for those who gave demonstrations

- "crowdworkers", "crowd-sourced workers" for online studies

- "passersby", "random people who walked by our study setups" for public space studies

- "everyday users"; rare: "novices" (1), "naive users" (1)

**Examples.**

- [PROG:105] "Robots have already firmly become part of our daily lives, making it crucial to learn from users, especially non-expert users."

- [RSS:26] "However, expecting all of the users, especially those with limited experience with robots, to always provide high-quality teaching is impractical."

- [PROG:203] "We conducted our studies with crowd-sourced workers and random passersby."

**In the dissertation.** "non-experts" as the default; "participants" inside a study; "human teachers" for general statements. "Non-expert" describes experience with robots, not ability.

### VOC-02 · Words for imperfect teaching

**Use for.** Describing what is wrong, or only apparently wrong, with demonstrations and feedback.

**In the papers.**

- "imperfections" (about 30), the umbrella noun

- "noisy", "noise" (about 54)

- "sub-optimal" (23, with a hyphen) for demonstrations and policies; "non-optimal behaviors" (19) for single behaviors inside a demonstration

- "inconsistent", "unstable" for feedback

- "patterned imperfections", "structured", "systematic patterns"

- "unproductive but harmless behaviors", "multi-policy", "noisy in a meaningful way"

**Examples.**

- [SIDE:68] "Prior work in LfD often characterizes the sub-optimalities in human demonstrations as random noise."

- [PROG:95] "We find that progress indicates whether the task is successfully performed, reflects the degree of task completion, identifies unproductive but harmless behaviors, and is likely to be more consistent across participants."

- [PROG:654] "We found that non-expert demonstrations are multi-policy and mostly successful, while noisy in a meaningful way."

**In the dissertation.** The same nouns. For the claim about structure: "can contain systematic structure". "Failure" only for a demonstration that did not complete the task.

### VOC-03 · Names of the teaching signals

**Use for.** Referring to demonstrations, feedback and *progress* without drifting between names.

**In the papers.**

- "human demonstrations", "human feedback", "evaluative feedback"

- "binary feedback", "scalar feedback"

- "*progress*", in italics whenever it is the signal

- "teaching signal" (about 14); "feedback modality" (PHIRL and the prospectus)

- "human teaching" as the umbrella for all of them

- "*progress* annotations", "*progress* labels" for the collected values

**Examples.**

- [PH-ABS:70] "Specifically, we use *progress*, a feedback modality that describes cumulative task completion."

- [PROG:211] "Our goal is to improve learning from human feedback with a new teaching signal: progress."

- [STEADY:134] "both binary feedback and scalar feedback are dynamic, and"

**In the dissertation.** "binary evaluative feedback" and "scalar evaluative feedback"; "*progress*, a signal that is under-explored as a human teaching signal". One name per signal: no "rating" or "score" for variety.

### VOC-04 · Verbs that report a finding

**Use for.** The sentence that says what a study, an analysis or an experiment showed. This entry answers the request for more alternatives to "results show / indicate / suggest that".

**In the papers.**

- "We found that …" (30)

- "We show that …", "We showed that …" (21)

- "Results show / indicate / suggest / demonstrate that …", with "Our" or "The" in front (18)

- "We demonstrate that …", "We demonstrated that …" (8)

- "This suggests that …" (5)

- "We observed that …" (4); "We did not find …" (4)

- once each: "This indicates that", "This further reveals that", "This shows that", "This highlights", "This explains why", "which confirmed", "Our results confirmed", "These results are consistent with"

**Examples.**

- [CHARM:56] "We found that feedback patterns are not only correlated with task statistics, such as rewards, but also correlated with participants' characteristics, especially robot experience and educational background."

- [PROG:413] "We found that progress could correctly indicate if the task is complete, while the indication of task completion was not captured by scalar feedback."

- [SIDE:306] "This further reveals that humans tend to have demonstration sidetracks near task phase change temporally."

- [CHARM:445] "These results are consistent with our earlier correlation analysis."

**In the dissertation.** The subject changes and the verb stays.

- "Results indicated that …", "The results showed that …", "The results suggest that …"

- "The analysis found that …", "The study showed that …", "The evaluation showed that …"

- "This suggests that …", "This indicates that …", "This further reveals that …", "This explains why …"

- "These results are consistent with …"

- "No significant difference was found …"

- the method or the participants as subject, with no reporting verb: "STEADY achieved …", "34 out of 40 participants provided …"

- "As shown in [figure], …"

**Keep in mind.** "found" and "showed" for an observation; "suggests" and "indicates" for a reading of it; "demonstrates" when the evidence is a direct test; "confirmed" when it repeats an earlier result.

**Shown in.** APP-01, APP-02.

### VOC-05 · Verbs for what the researcher did

**Use for.** Method and procedure sentences.

**In the papers.**

- "conducted" a study; "recruited" participants; "collected" data, feedback, demonstrations

- "designed" a questionnaire, an interface, a study; "developed" a GUI

- "annotated" demonstrations; "analyzed"; "calculated" or "computed" a correlation

- "trained" models; "validated" a design; "evaluated" a method

- "investigated", "examined", "characterized", "identified", "defined"

- "propose", "present", "introduce" a method; "released", "published" data

**Examples.**

- [CHARM:55] "We conducted a public space study with two long-horizon tasks and 46 participants."

- [SIDE:71] "We recreated the experimental setup in a simulation and annotated all the demonstrations."

- [STEADY:339] "A total of 90 AMT crowdworkers were recruited, divided evenly between two groups (45 participants per group)."

**In the dissertation.** The same verb in the passive, or with the study as subject: "A public space study was conducted with …", "… were recruited", "… were collected". "Investigate" for an open question, "validate" for a check of a design, "evaluate" for performance.

### VOC-06 · Verbs for what a method, a signal or a person does

**Use for.** Saying what something contributes.

**In the papers.**

- a method "enables" (14), "allows" (18), "improves", "reduces", "mitigates" (12), "leverages" (13; "utilizes" 5), "aligns", "shapes", "infers", "re-scales", "re-constructs", "outperforms"

- a signal "provides", "carries", "contains", "encodes", "describes", "indicates", "reflects", "captures", "represents"

- a person "provides" or "gives" feedback, demonstrations and annotations

**Examples.**

- [PROG:115] "Demonstrations carry relatively dense and global information including policies and goals, and tend to be less accurate"

- [PH-ABS:68] "Human demonstrations provide dense policy-level information but sometimes lack local precision."

- [STEADY:197] "This enables binary-feedback-based learning algorithms to learn"

**In the dissertation.** The same verbs. People "provide" or "give" teaching; "supply" never occurs in the papers.

**Shown in.** APP-03.

### VOC-07 · Hedges and degree words

**Use for.** Setting how strong a claim is.

**In the papers.**

- "can" (about 115), the default for a capability or a possibility

- "could" (22) and "would" (19) for expectations and hypotheses

- "may" (17) and "might" (10) for possible explanations

- "likely" (12), "tend to" (9)

- "relatively", "fairly", "largely", "closely" ("closely investigated", "closely examined", "closely defined"), "especially" (15), "indeed"

- "significantly" (about 47)

**Examples.**

- [CHARM:394] "This suggests that participants with relevant educational backgrounds or greater robot experience tend to provide feedback that is more accurate in direction (e.g., positive vs. negative)."

- [STEADY:357] "From prior work, we expect that binary feedback is noise-reduced and scalar feedback tends to be unstable, but none of the prior work has closely examined it."

- [SIDE:96] "Methods that work with oracle demonstrations might not perform well with real human demonstrations."

**In the dissertation.** The same set. "significantly" only next to a statistical test. Instead of "fairly correlated", the value of the correlation.

### VOC-08 · Words for the setting and the gap

**Use for.** Saying where the data came from and why that matters.

**In the papers.**

- "public space study" (18); "non-lab setting"; "outside the lab"

- "in the wild"; "real-world scenarios", "real-world deployments" (15)

- "random people who walked by our study setups"; "passersby"

- "the gap between …"; "oversimplify" (6); "lab-to-real-world"

**Examples.**

- [SIDE:161] "The demonstrations we used in this work were collected outside the lab with random people. Our data and results can be expected to better reflect robot-in-the-wild deployments than in-lab setups."

- [CHARM:479] "We conducted our study in a public space with 46 participants who randomly passed by our setup."

- [RSS:28] "Ignoring or oversimplifying these dynamics in teaching from non-experts can lead to a higher demand for training data or a significant decrease in robot performance."

**In the dissertation.** The same phrases. They carry the practical argument of the dissertation, so they stay literal.

### VOC-09 · Words for earlier research

**Use for.** Referring to the literature.

**In the papers.**

- "prior work" (27), the default

- "previous work" (7); "recent work", "more recent work" (6)

- "much prior work", "most prior work", "the body of prior work"

- "few studies", "little work", "little research"

**Examples.**

- [SIDE:187] "Prior work interprets non-optimal behaviors in human demonstrations as random manipulation noise or incorrect behaviors with underlying optimal control policies"

- [STEADY:249] "Throughout the body of prior work, there is a strong focus on using binary feedback to improve learning, with limited exploration of scalar feedback."

- [RSS:46] "recent work suggests that oversimplifying the intricacies of human teaching can potentially cause issues"

**In the dissertation.** "prior work" for other people's research. Hang's own earlier studies are referred to as chapters, not as "our previous work".

### VOC-10 · Value words, used sparingly

**Use for.** The few places where the text says that something is good or important.

**In the papers.**

- "crucial", "essential", "promising"

- "effective" (16), "robust" (21)

- "novel" (11)

- "informative", "information-rich", "worth more attention"

**Examples.**

- [STEADY:135] "scalar feedback is a promising signal for use in interactive Reinforcement Learning."

- [PROG:151] "Our results also showed that non-expert demonstrations are multi-policy and sub-optimal, but sub-optimal in a meaningful way."

- [SIDE:85] "One challenge in LfD is that high-quality demonstrations are hard to obtain"

**In the dissertation.** One value word per claim, next to the result that supports it. For *progress*: "under-explored as a human teaching signal" in place of "novel". "robust" says robust to what.

## Wording preference

### WRD-01 · "In this work" becomes "In this chapter" or "This dissertation"

**In the papers.** "In this work, we …" (33); "In this paper" (2).

**Examples.**

- [CHARM:54] "In this work, we designed an exploratory study investigating how human feedback patterns are associated with human characteristics."

- [SIDE:177] "In this work, we conducted an exploratory analysis to investigate noisy behaviors in non-expert human demonstrations."

- [PH-INT:13] "In this work, we aim to learn robust reward functions by combining human demonstrations and feedback, while reducing human engagement."

**In the dissertation.**

- inside a study chapter: "In this chapter, …", "This chapter …"

- in the Introduction, the Discussion and the Conclusion: "This dissertation …"

- for one study seen from another chapter: "The study in [chapter] …"

**Shown in.** APP-05.

### WRD-02 · First person becomes impersonal

**In the papers.** "We" opens about 204 sentences and "Our" about 41.

**In the dissertation.** The pairs below start from Hang's own examples.

- we conducted a study → a study was conducted

- we collected, we recruited → … were collected, … were recruited

- we found that → results suggested that; the analysis found that

- we show that → the results show that; this chapter shows that

- we propose X, we present X → this chapter proposes X; X is proposed

- our key insight is that → the key insight is that

- our intuition is that → the intuition is that

- our goal is to → the goal is to

- our results → the results

- our work differs from prior work by → this chapter differs from prior work by

- we expect that → [X] is expected to

- we believe that → the claim itself, with "may" or "can"

- we did not find → no … was found

**Examples.**

- [SIDE:111] "Our goal is to investigate non-expert behaviors and explore the patterns of noise in non-expert demonstrations."

- [PH-CON:67] "We believe that PHIRL is an effective framework for learning robust reward functions"

**Keep in mind.** A named subject often reads better than a passive: "STEADY re-constructs …", "Participants were asked to …", "The study in [chapter] examined …".

### WRD-03 · A result that was not significant

**In the papers.**

- "we did not find any significant difference between …"

- "fail to find a significant difference"

- "there was no evidence showing that there is any difference"

- "no significance has been found"; "H3 is not supported"

**Examples.**

- [PROG:319] "We did not find any significant difference between giving scalar feedback and progress in all the dimensions of the NASA TLX results"

- [STEADY:186] "We study the correlation of scalar and binary feedback with interactive RL training targets, and fail to find a significant difference between scalar and binary feedback, although we find that scalar feedback has more variation."

- [PROG:419] "there was no evidence showing that there is any difference between the other two and the Perfect case"

**In the dissertation.** "no difference in … was detected between … and …"; "no significant difference was found". Two paper wordings are left behind because they claim more than the test shows: "the difference vanishes" and "scalar feedback is as good as binary feedback".

### WRD-04 · Numbers in a result sentence

**In the papers.**

- "N out of M" for counts of people

- a percentage together with what it is a percentage of

- "on average", "about", "approximately"

- the statistical test in parentheses at the end of the clause

- a difference with its size: "5.6\% and 17.1\% higher than the best baseline"

**Examples.**

- [PROG:548] "We found that non-expert demonstrations are noisy and contain a variety of policies, even though 34 out of 40 are ultimately successful."

- [STEADY:508] "we found that most participants (74 out of 90) had a bias in their feedback in the second session as compared to the first."

- [SIDE:294] "Demonstration sidetracks comprised about 48\% of the overall task's recorded timesteps."

- [CHARM:393] "Robot experience and educational background exhibit correlation coefficients of 0.25 and 0.16 with feedback accuracy."

**In the dissertation.** The same. A correlation is given with its value, not as "relatively high".

### WRD-05 · Comparing two things

**In the papers.**

- "compared to" (14)

- "more … than", "higher than", "significantly outperforms"

- "while" between the two sides of a result

- "on the other hand" (3), "as opposed to"

**Examples.**

- [CHARM:119] "We found that models with human characteristics and task statistics (CHARM) achieved significantly higher accuracy in predicting feedback values compared to models with only task statistics."

- [PROG:440] "Scalar feedback, on the other hand, changed dramatically in all these cases."

- [PH-EXP:137] "These results demonstrate that PHIRL learns effective rewards for RL agents, and is more reliable when the task horizon is longer or the demonstration quality is lower."

**In the dissertation.** Both sides and the measure are named in the same sentence.

### WRD-06 · Hypotheses and their verdicts

**In the papers.**

- "We expect that …"; "We hypothesize:"

- a bold "H1." followed by the statement in the present tense

- "H1 is supported."; "which supports H1"; "supporting H2"; "so H3 is not supported"

**Examples.**

- [PROG:251] "H1. Giving progress does not require extra workload and extra time compared to giving scalar feedback."

- [STEADY:494] "If exact matches are required, binary feedback is significantly more self-consistent than scalar feedback"

- [STEADY:627] "so H3 is not supported."

**In the dissertation.** The same wording. "is supported", never "is proven".

### WRD-07 · A possible cause

**In the papers.**

- "This is likely due to …"; "This is possibly due to …"

- "This might be because …"; "…, likely because …"

- "This … is likely caused by …"

- "We assume this is because of two reasons. One is that … The other one is that …"

- when the mechanism is known: "This is because …"

**Examples.**

- [SIDE:304] "This is likely due to the different sub-goals of different task phases, along with a change in the control pattern for participants"

- [STEADY:510] "This might be because the task is relatively simple and participants expected the robot to perform well on the task."

- [PH-EXP:207] "This reward hacking is likely caused by an imbalanced reward design and a bottleneck in the task."

- [STEADY:831] "This explains why learning from multiple participants is likely to be difficult and suggests that"

**In the dissertation.** "This is likely due to …"; "This might be because …"; "This might explain why …"; "One possible reason is that …".

**Shown in.** APP-04.

### WRD-08 · Naming what prior work has not done

**In the papers.**

- "there is little work that has closely investigated …"

- "there is little research on …"; "there is less work on investigating the reasons"

- "few studies have explicitly considered …"

- "has been used less because …"; "is less used since …"

- "none of the prior work has closely examined it"

- "is still relatively rare"; "with limited exploration of …"

**Examples.**

- [CHARM:53] "While much prior work acknowledged that human teachers' characteristics would affect human feedback patterns, there is little work that has closely investigated the actual effects."

- [SIDE:87] "However, there is little research on understanding and modeling non-expert demonstrations."

- [STEADY:123] "scalar human feedback has been used less because it is believed to be noisy and unstable."

**In the dissertation.** The same forms. The sentence names what is missing; it does not only say that a gap exists.

**Shown in.** APP-12.

### WRD-09 · Limitations and future work

**In the papers.**

- "One limitation of this work is that …" (CHARM, Sidetracks, STEADY)

- "We acknowledge several limitations in our work:"

- "Future work should …"; "Future work could …"

- "For future work, we will …"; "A key area for future work is to …"

**Examples.**

- [SIDE:364] "One limitation of this work is that we only used demonstrations from one task and one robot."

- [STEADY:858] "Repeating the robot behaviors only once was necessary to prevent participants from becoming aware that clips were repeating, but this limits our ability to understand the full range of possible changes in feedback dynamics."

- [STEADY:859] "Future work could investigate longer-term changes in feedback and new methods for stabilizing dynamics over long periods of time."

**In the dissertation.** "One limitation of this chapter is that …"; "One limitation is that …"; "Future work should …" or "could …"; "One direction for future work is to …".

**Shown in.** APP-06.

### WRD-10 · Stating a contribution

**In the papers.**

- "The main contribution of this work is to …"; "The main contributions of this work are …"

- "An additional contribution of our work is …"

- "To the best of our knowledge, this is the first work that …" (CHARM, Sidetracks, STEADY)

**Examples.**

- [PROG:149] "The main contribution of this work is to demonstrate that *progress* has information beyond rating and ranking, and has great potential in interactive learning."

- [SIDE:126] "To the best of our knowledge, this is the first work that systematically characterizes non-experts' non-optimal manipulation patterns when providing demonstrations."

- [PROG:96] "An additional contribution of our work is a dataset of 40 non-expert demonstrations from the public space study through an ice cream topping-adding task"

**In the dissertation.** "The main contribution of this dissertation is …"; "This dissertation makes the following contributions:". The "first work" claim only where it can be defended.

### WRD-11 · Terms already settled for the dissertation

**Use for.** Places where the paper wording was replaced on Hang's instruction. The dissertation wording wins.

- "completion rate", "completion percentage" → "degree of completion"

- "novel teaching signal", "little-used", "less-explored", "recently-introduced" → "under-explored as a human teaching signal"

- "the difference vanishes" → "no difference … was detected"

- "relatively high correlations", "fairly correlated" → the correlation values

- "open-coded book" → "a codebook developed through open coding"

- "advantaged rewards" → "advantages"

- "binary feedback", "scalar feedback" → "binary evaluative feedback", "scalar evaluative feedback"

- "structurally resilient against" → "illustrates how … can discourage"

- scalar scale "1 to 10" → "0 to 10"

- "mitigate these human dynamics" → "account for systematic variation in human teaching"

**Examples of the paper wording.**

- [PROG:93] "In this work, we characterize and test a little-used teaching signal: *progress*, designed to represent the completion percentage of a task."

- [PROG:218] "We characterize *progress* as the accumulative task completion rate over a task based on the current observation, ranging from totally incomplete to complete fully."

- [SIDE:115] "we designed a graphical interface and an open-coded book, annotated the demonstrations with two robot experts, and cross-validated the labels with a third expert."

## Writing style

### STY-01 · Say what was done, what was found and why it matters

**In the papers.** Subject first, an active research verb, then the object. "We" opens about one sentence in five.

**Examples.**

- [CHARM:55] "We conducted a public space study with two long-horizon tasks and 46 participants."

- [STEADY:126] "We collected binary or scalar feedback respectively from two groups of crowdworkers on a robot task."

- [PH-EXP:189] "The robot repeatedly picks up the block, lifts it, and then drops it."

**In the dissertation.** The same directness without the pronoun. The study, the method, the participants or the results are the subject. A statement is written in full, with its own nouns, so it can be read without the sentence before it.

**Shown in.** APP-08, APP-12.

### STY-02 · Imperfect teaching is described, not blamed

**In the papers.** An imperfection is a property of the signal, and it has a reason: the control interface, reaction time, perception, the scale that was offered.

**Examples.**

- [SIDE:175] "However, not all imperfect behaviors are meaningless."

- [RSS:94] "We found that non-expert demonstrations, while noisy, do not necessarily mean failures or errors."

- [SIDE:188] "humans are limited by the control interface, reaction time, and perception accuracy."

**In the dissertation.** The same stance. The teacher is never the fault; words such as "poor" or "careless" do not occur.

### STY-03 · Concrete tasks, objects and numbers

**In the papers.** An abstract claim is followed by the task, the object or the number that shows it.

**Examples.**

- [PROG:551] "For instance, we observed that 14 participants slightly shook the topping jar to test if the gripper firmly held the jar when picking the jar, and 17 participants poured a few toppings out first to see if the jar was right above the ice cream when pouring the toppings."

- [STEADY:158] "For example, on a scale of 10, the distance from 5 to 7 may be perceived as different from the distance from 3 to 5 although they are numerically the same."

- [SIDE:354] "For instance, in our experiment, participants controlled the robot using an Xbox controller, and each button or joystick controlled one dimension of freedom."

**In the dissertation.** The same. The Discussion and the Conclusion reuse the concrete cases of the study chapters when they make a general point.

**Shown in.** APP-14.

### STY-04 · Firm about observations, tentative about reasons

**In the papers.** What was measured is stated plainly. Why it happened is marked as a possibility.

**Examples.**

- [SIDE:327] "This is possibly due to the requirement for control accuracy, which resulted in more alignment to get to the desired positions and more pauses for reaction."

- [STEADY:419] "This suggests that asking participants to give scalar feedback did not substantially increase the participant's effort, likely because scalar feedback is common in daily life."

- [CHARM:467] "One is that the relationship between human characteristics and feedback patterns might not be linear, and multiple domains of human characteristics can jointly affect human feedback."

**In the dissertation.** The observation with its number; the reason with "likely", "might" or "possibly".

### STY-05 · The practical stake: the lab and the real world, data cost, human effort

**In the papers.** Motivation and conclusions return to three practical stakes.

**Examples.**

- [CHARM:71] "Oversimplifying human feedback patterns will introduce a lab-to-real-world discrepancy and result in a performance drop for the learning algorithms."

- [PH-INT:30] "In this setting, human-in-the-loop teaching effort, rather than demonstrations, has become the more expensive resource."

- [PROG:117] "Perfect demonstrations are hard to obtain while purely learning from human feedback requires many human labels, often obtained at significant time and expense."

**In the dissertation.** The same three stakes in place of general statements of importance.

### STY-06 · Emphasis: italics for the term and the key sentence, bold for the take-away

**In the papers.**

- italics for a defined term (*progress*, *confidence degree*, *Alignment*) and for the key-insight sentence

- bold for run-in headings and for one take-away sentence

- quotation marks for informal labels: 'good enough', 'safer', 'harmless explorations'

**Examples.**

- [SIDE:349] "We found that human imperfections when giving demonstrations are not just simple noise or randomly distributed."

- [PH-INT:36] "Our key intuition is that the rewards inferred from demonstrations should be consistent with the annotations of the demonstrations."

- [PROG:440] "Participants used scalar feedback to indicate if a demonstration was clean and good, but the possibility that the errors were 'harmless explorations' or 'fixable mistakes' is not captured by scalar feedback."

**In the dissertation.** The same three devices, each at most once in a paragraph.

### STY-07 · Literal wording, no figures of speech

**In the papers.** Things are explained with literal verbs and with small scenarios (STO-06). The one analogy is announced as an analogy.

**Examples.**

- [PH-INT:37] "This process mimics human learning: much like a student cross-referencing answers to correct their own solutions, the method generates a potential reward function and compares it against human feedback to refine its learned rewards."

- [PROG:556] "The most common faulty cases are similar to the Failure scenario and the Unaware scenario we used in our online study, which confirmed the validity of the design of our online study."

**In the dissertation.** These expressions in the Overall Discussion do not occur in any of the six papers: "read together", "point to", "point in the same direction", "link by link", "by two routes", "supplied". The literal counterparts from the papers are "suggest", "are consistent with", "was evaluated separately", "in two ways", "provided".

**Shown in.** APP-01, APP-02, APP-03, APP-07.

## Sentence style

### SEN-01 · About 20 words, one job per sentence

**In the papers.** The middle sentence has about 20 words (18 to 25 depending on the paper), and half of all sentences have between about 14 and 28. A long sentence carries a list or a two-sided comparison. A new job (a reason, a limit, a consequence) starts a new sentence with "This", "Thus," or "However,".

**Examples.**

- [SIDE:222] "Participants were recruited from random people walking past the experiment setup."

- [SIDE:224] "22 were male, 14 were female, and 4 preferred not to say."

- [STEADY:827] "Scalar feedback does change more than binary feedback, but tolerating small variations removes the effect."

**In the dissertation.** A sentence that reports, qualifies and concludes at once is split where the job changes.

**Shown in.** APP-09.

### SEN-02 · The short verdict sentence

**In the papers.** After the numbers, a sentence of three to eight words gives the verdict.

**Examples.**

- [PROG:378] "H2 is supported."

- [STEADY:325] "All of them answered *no*."

- [PH-INT:26] "The preference feedback is therefore uninformative."

- [SIDE:223] "40 participants were recruited in total."

**In the dissertation.** The same, after a result with numbers.

### SEN-03 · The example sentence

**In the papers.** "For instance," (9) is more common than "For example," (3). It introduces one concrete case with a task, a person or a number.

**Examples.**

- [PROG:594] "For instance, one participant failed to pour the toppings into the ice cream because the grasp point was not optimal."

- [PH-INT:26] "For instance, consider a pick-and-place task where the robot never manages to grasp the object."

- [PROG:634] "For example, a demonstration with a progress of 60 at the end should be ranked lower than a demonstration with a progress of 90."

**In the dissertation.** "For instance, …" with one case per claim.

**Shown in.** APP-14.

### SEN-04 · The colon that announces

**In the papers.** A colon introduces the key sentence, a list of benefits, or the specific thing that was just named.

**Examples.**

- [PROG:93] "In this work, we characterize and test a little-used teaching signal: *progress*"

- [RSS:37] "Additionally, learning from non-experts provides practical benefits:"

- [PROG:126] "This is especially true for non-expert demonstrations: non-expert demonstrations can be noisy, multi-policy, and yet still succeed"

**In the dissertation.** The same. What follows the colon is the point of the sentence.

**Shown in.** APP-13.

### SEN-05 · Specifics in parentheses

**In the papers.** Examples, counts, conditions and statistics go in parentheses, so the main clause stays easy to read.

**Examples.**

- [STEADY:158] "Scalar feedback, on the other hand, is also naturally used in daily life (e.g., movie rating and product evaluation) but encodes information beyond that in binary feedback, such as ranking and magnitude, through a wider range of possible values."

- [STEADY:321] "each 100 clips consisted of six trajectories (three successes, three failures)."

- [STEADY:196] "re-normalizing noisy scalar feedback to confidence scores (i.e. more precise magnitudes) and recovering positive/negative labels."

**In the dissertation.** The same, with "e.g.," and "i.e.," inside the parentheses.

### SEN-06 · How sentences open

**In the papers.** Counts of sentence openers:

- "To + verb …," (24)

- "However," (21)

- "While …," (10)

- "Additionally," (9); "Moreover," (9); "Furthermore," (8); "In addition," (7)

- "For instance," (9)

- "Thus," (8); "Therefore," (1)

- "Specifically," (5); "Despite …," (5); "Since …," (4)

- also: "Overall,", "Finally,", "Then", "Instead,", "Rather,", "Conversely,", "Consequently,", "In contrast to …,"

**Examples.**

- [SIDE:90] "Thus, in this work, we focus on identifying and investigating patterns of the noise in non-expert demonstrations."

- [PROG:576] "Moreover, progress is significantly more consistent across participants even though their demonstrations are multiple policies and in different quality"

- [PH-METH:88] "Specifically,"

**In the dissertation.** The same set. "Thus," for a consequence. The four additive openers are used interchangeably in the papers, so they can alternate within a paragraph.

**Shown in.** APP-09, APP-10.

### SEN-07 · The roadmap sentence

**In the papers.** A section opens by saying what it does, in order.

**Examples.**

- [PROG:215] "In this section, we first define progress, and then introduce our hypothesis."

- [CHARM:316] "In this section, we first present the data we collected from 46 participants in our public space study."

- [SIDE:321] "In this subsection, we examine the spatial distribution of demonstration sidetracks."

**In the dissertation.** "This section first defines …, and then introduces …"; "This chapter first …".

## Sentence structure

### STR-01 · "While A, B": grant something, then make the point

**In the papers.** "while" about 52 times, 10 of them at the start of a sentence.

**Examples.**

- [PH-INT:6] "While sparse rewards are intuitive to specify, they offer limited guidance during early exploration."

- [PROG:371] "While scalar feedback and progress can both describe the quality of a demonstration, progress and scalar feedback focus on different information."

- [PROG:475] "While progress can be effective in being used along with expert demonstrations,"

**Form.** While [what is true or accepted], [the limit, or what this work adds].

**In the dissertation.** The same. The point of the sentence is in the second clause.

### STR-02 · "not only A but also B"

**In the papers.** About 10 times, usually for the central claim that teaching depends on more than the task.

**Examples.**

- [CHARM:56] "We found that feedback patterns are not only correlated with task statistics, such as rewards, but also correlated with participants' characteristics"

- [RSS:84] "these factors are not only related to the tasks but also are intrinsic to the human teachers."

- [PROG:550] "We also observed that the noise in the demonstrations is not only teleoperating errors but also explorations."

**Form.** [X] is not only [the expected factor] but also [the factor this work adds].

**In the dissertation.** At most once in a paragraph, with both parts in the same grammatical form.

### STR-03 · ", especially B" at the end

**In the papers.** About 15 times. A general statement, then the case that matters most.

**Examples.**

- [PROG:105] "making it crucial to learn from users, especially non-expert users."

- [CHARM:56] "but also correlated with participants' characteristics, especially robot experience and educational background."

- [PH-CON:21] "especially when the number of human feedback labels is limited."

**Form.** [general statement], especially [the specific case].

**In the dissertation.** The same.

### STR-04 · "instead of" and "rather than"

**In the papers.** "instead of" (11), "rather than" (7), and "Rather," or "Instead," at the start of a sentence. The sentence says what something is by first saying what it is not.

**Examples.**

- [SIDE:73] "We found that instead of being random and rare, demonstration sidetracks frequently appear in non-expert demonstrations across all participants"

- [PH-INT:30] "In this setting, human-in-the-loop teaching effort, rather than demonstrations, has become the more expensive resource."

- [PROG:233] "with a trajectory instead of a single state to increase reliability."

**Form.** [X] [verb] [B] rather than [A]. Instead of [A], [X] [verb] [B].

**In the dissertation.** The same.

**Shown in.** APP-07.

### STR-05 · Purpose first: "To …, …"

**In the papers.** About 24 sentences open with "To + verb". The reason for a design choice comes before the choice.

**Examples.**

- [STEADY:489] "To answer the question of whether participants are self-consistent,"

- [CHARM:104] "To bridge this gap, our work focuses on investigating the impact of human characteristics on feedback patterns and exploring if incorporating these attributes can improve predicting human feedback."

- [STEADY:302] "We used a relatively simple task to reduce the cognitive load on solving the task and thus reduce feedback dynamics from confusion over the task."

**Form.** To [goal], [action]. Or at the end: [action] to [goal].

**In the dissertation.** "To [goal], [a named subject or a passive] …".

### STR-06 · Two parallel sentences for a contrast

**In the papers.** Two things are contrasted in two sentences with the same build.

**Examples.**

- [PH-ABS:68] "Human demonstrations provide dense policy-level information but sometimes lack local precision. Human feedback presents accurate local critiques, but offers sparse evaluations rather than direct policy guidance."

- [PROG:115] "Human feedback carries relatively sparse and local information such as the correctness or a rating of a robot's action"

- [PH-INT:6] "Conversely, hand-crafted dense rewards accelerate learning, but designing them requires substantial engineering effort and tedious manual tuning"

**Form.** [A] provides [strength] but [weakness]. [B] provides [strength], but [weakness].

**In the dissertation.** The same order of parts on both sides.

### STR-07 · A number sentence, then "This suggests that …"

**In the papers.** "This" opens about 32 sentences: "This suggests that", "This indicates that", "This is likely due to", "This allows us to", "This explains why", "This highlights".

**Examples.**

- [SIDE:294] "This suggests that, contrary to the common assumption that imperfections only take up a small part in non-expert demonstration, demonstration sidetracks are frequent and take up a large portion of the overall task demonstration."

- [CHARM:395] "This indicates that participants with more robot experience or a relevant educational background also tend to provide feedback that is closer in value to the ground truth"

- [PH-EXP:168] "This shows that completion shaping is critical for learning when demonstrations fail."

**Form.** [Result with numbers]. This suggests that [what it means].

**In the dissertation.** The same. "This" points to the sentence just before. The sentence starts with its subject; a clause as the subject ("That X does Y is …") does not occur in the papers.

**Shown in.** APP-11.

### STR-08 · "by + -ing": how something is done or shown

**Examples.**

- [SIDE:302] "However, we show that this assumption does not hold for actual human demonstrations by showing the relevance between demonstration sidetracks and the task's progress."

- [PH-METH:87] "We improve the learned reward function by shaping it to align with *progress* annotations during reward learning."

- [RSS:90] "challenged this assumption by identifying frequent patterned imperfections in non-expert demonstrations."

**Form.** [Claim or goal] by [verb]-ing [the means].

**In the dissertation.** The same.

### STR-09 · Lists and enumerations

**In the papers.**

- "First, … Second, …"

- "One is that … The other one is that …"

- a numbered list inside the sentence: "1) … 2) … 3) … 4) …"

- three items in a series, the usual length of a list

**Examples.**

- [STEADY:660] "Second, since some robot behaviors are more preferred than others, feedback distributions can be separated into at least two classes, preferable (positive) and non-preferable (negative)."

- [CHARM:468] "The other one is that human characteristics are only one of the factors that affect human feedback values"

- [RSS:96] "1) Pause, no input from the controller for a period of time; 2) Alignment, moving the robot back and forth to align the robot with a target object;"

**In the dissertation.** "First, … Second, … Third, …"; "One is … The other is …"; numbered lists inside the sentence, separated by semicolons.

### STR-10 · Defining a term

**In the papers.**

- "[Term] is a signal that describes …, ranging from … to …"

- "We define … as [term]"; "We characterize [term] as …"

- "…, which we refer to as the [term]"

- "A value of 0 indicates …, while a value of 100 signifies …"

**Examples.**

- [PH-METH:17] "*Progress* is a signal that describes the cumulative degree of task completion, ranging from fully incomplete to fully complete."

- [SIDE:193] "In this work, we define non-optimal behaviors in human demonstrations as *Demonstration Sidetracks*."

- [PROG:226] "A *progress* value of 0 indicates that the task has not yet begun, while a value of 100 signifies task completion."

**In the dissertation.** "[Term] is defined as …"; "This chapter defines … as [term]". The definition comes once, where the term is first needed.

### STR-11 · The reason or the condition at the end

**In the papers.** "… since …", "… because …", "…, as …", "… when properly handled", "… if …", "… even though …".

**Examples.**

- [PH-METH:126] "since different users might scale *progress* differently."

- [RSS:131] "Our final stage is to utilize human feedback to enhance learning from demonstrations, as providing accurate feedback to a policy is easier and requires less expertise."

- [STEADY:125] "we compare scalar and binary feedback, and demonstrate that scalar feedback benefits learning when properly handled."

**Form.** [Claim] since [reason]. [Claim] when [condition].

**In the dissertation.** The same. The condition stays attached to the claim it limits.

## Storytelling style

### STO-01 · The introduction in seven moves

**In the papers.** CHARM, Sidetracks, STEADY and Progress open the same way.

- 1. why the topic matters in practice

- 2. what prior work does or assumes

- 3. what that misses, introduced with "However,"

- 4. the key insight, in italics

- 5. "In this work, we …"

- 6. what was done and what was found, with the numbers

- 7. the contribution and its practical benefit

**Examples.**

- [SIDE:85] "One challenge in LfD is that high-quality demonstrations are hard to obtain"

- [SIDE:89] "Our key insights are that: *not all non-optimal behaviors from non-experts are random errors and randomly distributed: instead they appear in structured ways.*"

- [SIDE:127] "Our work will be beneficial for future LfD algorithm development to better learn from noisy demonstrations and for oracle design to reduce the gap between in-lab datasets and real-world demonstrations."

**In the dissertation.** Each study chapter keeps the seven moves; move 5 becomes "This chapter …".

### STO-02 · Challenge a simplifying assumption

**In the papers.** The argument starts from an assumption that prior work makes about human teaching, and shows with data that it does not hold for non-experts.

**Examples.**

- [RSS:89] "often assumes that non-optimal behaviors in demonstrations are random errors"

- [SIDE:302] "One key assumption when using simple distributions to sample noise is that noise is independent from the task itself."

- [SIDE:294] "contrary to the common assumption that imperfections only take up a small part in non-expert demonstration"

**Form.** Prior work assumes [A]. [What was measured]. This suggests that [A] does not hold for real non-expert teaching.

**In the dissertation.** The same. The assumption is named before the evidence against it.

### STO-03 · The key insight comes before the method

**In the papers.** One sentence, set in italics or bold, before any formalism: "Our key insight is that …" (CHARM, Sidetracks, PHIRL), "The key insight of STEADY is to …", "Our key intuitions are:", "Our intuition is that:" (Progress, the prospectus).

**Examples.**

- [CHARM:73] "Our key insight is that"

- [CHARM:74] "*human feedback is not only associated with the task and the agent's performance, but also affected by human characteristics.*"

- [PROG:220] "*A teaching signal would be more robust to sub-optimal demonstrations and more consistent among users if human teachers could have objective references while providing the teaching signal.*"

**In the dissertation.** "The key insight is that …" or "The intuition is that: …", once in a chapter and before the first equation.

### STO-04 · A human study motivates the method

**In the papers.** The method is presented as the answer to what the study found.

**Examples.**

- [STEADY:280] "These results, and the data collected, motivate and enable the development and evaluation of our STEADY algorithm."

- [RSS:117] "We were thus motivated to propose a method that dynamically rescales scalar feedback into binary feedback with confidence degrees."

- [STEADY:641] "The user study results suggest that scalar feedback is as good as binary feedback, but noise needs to be mitigated."

**Form.** [Finding]. This motivated [method], which [what it does]. Or: Based on [finding], [method] [does what].

**In the dissertation.** The same hand-off between the study and the method, and between one chapter and the next.

**Shown in.** APP-13.

### STO-05 · The three-stage arc: understand, mitigate, leverage

**In the papers.** The prospectus tells the whole research as three steps, each with its question.

**Examples.**

- [RSS:15] "Embracing Imperfection: Understanding, Mitigating, and Leveraging Non-expert Teaching"

- [RSS:84] "Our first step focuses on examining human factors in human teaching robots that make human teaching noisy"

- [RSS:131] "Our final stage is to utilize human feedback to enhance learning from demonstrations"

**In the dissertation.** "The first stage …", "The second stage …", "The final stage …". Each stage answers one question and ends by naming what the next stage needs.

### STO-06 · A small everyday scenario makes the problem visible

**In the papers.** A problem is shown with a short, familiar case before it is formalized.

**Examples.**

- [PROG:616] "For instance, a cleaning robot gets a +1 reward every time it cleans a room. The robot, instead of cleaning one room and going to the next room, repetitively ejects dirt in a room, then cleans it, and thus achieves high rewards."

- [PH-INT:26] "For instance, consider a pick-and-place task where the robot never manages to grasp the object. In this case, all sampled trajectory clips are undesirable."

- [PH-METH:108] "Some steps, like picking up the target object, are inherently more progressive than simply moving closer."

**Form.** For instance, consider [a familiar task] where [what goes wrong]. In this case, [the consequence].

**In the dissertation.** One scenario for a problem, three sentences at most, then back to the method.

### STO-07 · The heading states the finding

**In the papers.** Result subsections are titled with the finding, or with the question they answer.

**Examples.**

- [PROG:316] "Giving progress is not time-consuming and not hard"

- [CHARM:403] "Including Human Characteristics Improves Feedback Prediction Accuracy"

- [PH-EXP:127] "PHIRL Outperforms Baselines"

- [STEADY:485] "Analysis of H1: Did participants give consistent feedback in the two sessions?"

**In the dissertation.** The same for result subsections and for the run-in headings of the Overall Discussion.

### STO-08 · Hypothesis, test, verdict

**In the papers.** The expectation in plain words, the hypothesis in bold, the test with its numbers, then the verdict.

**Examples.**

- [PROG:240] "We expect that people naturally estimate task completion in their daily lives, so progress should be not hard to give."

- [PROG:320] "The average completion time is lower for progress by"

- [PROG:421] "H3 is supported."

**In the dissertation.** The same order. A hypothesis that was not supported is reported as plainly as one that was.

### STO-09 · A surprising result, then the possible reasons

**In the papers.** A result that does not fit is named as interesting and followed by possible reasons.

**Examples.**

- [CHARM:465] "One interesting finding is that while there were no strong correlations between the selected human characteristics and human feedback values, our experiment results demonstrated that incorporating human characteristics into training leads to a significant improvement in modeling human feedback patterns."

- [CHARM:466] "We assume this is because of two reasons."

**Form.** One interesting finding is that while [what was expected], [what was observed]. One possible reason is that … Another is that …

**In the dissertation.** The same, with "One possible reason is that …" in place of "We assume".

### STO-10 · How a discussion closes

**In the papers.** The finding in one sentence, what it explains, a limitation, future work, and last the practical stake or a request to the field.

**Examples.**

- [STEADY:827] "The results above demonstrate that scalar feedback is not inherently worse than binary feedback as a teaching signal even without stabilization."

- [STEADY:856] "One limitation of our work is that the experiments were relatively short-term and only repeated each clip once."

- [STEADY:863] "Overall, our work suggests that HRI and interactive RL practitioners should give scalar feedback more attention"

- [SIDE:374] "We believe this work lays a foundation for bridging the gap between laboratory-based setups and real-world scenarios."

**In the dissertation.** Chapter discussions keep this order, and the last sentence of a chapter names the open question that the next chapter addresses.

### STO-11 · Related work ends with the difference

**In the papers.** The Background of CHARM, Sidetracks, Progress and PHIRL closes with "Our work differs from prior work by …".

**Examples.**

- [PROG:202] "Our work differs from prior work by focusing on non-experts."

- [PH-BG:46] "Our work differs from prior work by improving the data efficiency and reducing human-in-the-loop effort."

- [SIDE:159] "Our work differs from prior work by recognizing that non-optimal behaviors are natural for human manipulation"

**In the dissertation.** "This chapter differs from prior work by …", at the end of the related work of each chapter.

### STO-12 · An observed episode as evidence

**In the papers.** What one participant, or the robot, actually did is told in order, and then what it shows.

**Examples.**

- [PROG:595] "Then the participant decided to reset the arm to the initial position, demonstrated the entire task from the beginning again, and succeeded."

- [PH-EXP:206] "Instead of picking up the can and placing it in the target bin, the robot navigated to the can, closed the gripper, and poked the can with the gripper."

- [STEADY:324] "we conducted a pilot study by recruiting three robot experts from a robotic lab. We asked if they were aware that all clips were repeated once."

**Form.** [Who] [did what], then [did what], and [the outcome]. This [shows what].

**In the dissertation.** The same. A general statement in the Discussion can point back to an episode from a study chapter.

**Shown in.** APP-14.
