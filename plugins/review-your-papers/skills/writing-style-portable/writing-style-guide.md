# Writing style guide

This guide describes Hang Yu's writing style for research papers, theses, and talks. It condenses a longer reference built from six published papers in robot learning and human-robot interaction, and from the author's own instructions, hand edits, and decisions on several hundred suggested edits. The rules are written to hold for any paper. The examples come from the author's work and illustrate a rule. They are not text to reuse.

Companion files are [field-conventions.md](field-conventions.md), which shows what experienced robotics and HRI writers do, and [vocabulary.md](vocabulary.md), which lists the terms the author uses.

## Core philosophy

1. **Say what was done, what was found, and what it means.** The voice is direct, concrete, and explanatory.
2. **Match claim strength to the evidence.** State an observation firmly within its scope, qualify an interpretation, and present an untested explanation as a possibility.
3. **Explain through operations.** A method is described by its input, operation, and output before any benefit is named.
4. **Keep terms stable.** A defined term keeps one meaning. Synonyms are not used for variety.
5. **Use literal wording.** Name the relation between ideas with plain verbs and connectors, not figures of speech.
6. **Describe people precisely and without blame.** Imperfect human input can contain systematic structure and useful information.
7. **Use few words and few marks.** Few colons and semicolons, no em dashes, and few value words.
8. **Respect the author's wording when editing.** Move, cut, and correct before writing anything new.

## Which guidance wins

When two sources of guidance conflict, follow the first one in this list.

1. The author's current instructions.
2. The facts, data, and definitions of the passage being written.
3. The author's own past choices. An explicit instruction counts most, then a hand edit or a suggestion the author rewrote, then a suggestion the author declined, then one the author accepted as written. A decline says more about preference than an acceptance.
4. This guide.
5. Field conventions and wording from published papers.

In the forms below, square brackets mark slots to fill. In the examples, ✗ marks wording that was replaced or declined and ✓ marks the wording that the author chose or kept.

## Quick reference

1. Name the actor and use a concrete verb, such as participants provided, the analysis found, or the method infers.
2. Keep technical terms fixed, and keep the author's definitions as written.
3. Report observations directly, interpretations with qualification, and untested explanations as possibilities. Keep the reporting frame of a result, such as Results indicate that.
4. Give the measure, baseline, condition, and uncertainty together. Report a correlation value instead of fairly correlated.
5. Report a nonsignificant test as a difference that was not detected, never as equivalence.
6. Qualify a sentence only where it misstates the evidence. Do not narrow a positive result that the paper tests, and do not add sentences that only say the evidence is weak.
7. Give each sentence one main job. Keep together a governing condition and its claim, a result and the which clause that interprets it, and a list and the sentence that introduces it.
8. Define a term in ordinary language before notation. Give the intuition before the operations and the evaluation.
9. Open a paper or chapter with its place in the larger work, then the gap, the aim, the study, the findings, and what they are useful for.
10. Use few colons and semicolons. Say the relation with which, since, because, such as, or whereas, or start a new sentence. Replace em dashes.
11. Write complete clauses. A comparison gets its own subject and verb.
12. Use literal verbs such as suggest, are consistent with, help explain, and provide.
13. Correct an error in the author's sentence without rewording it. Offer any rewording as a separate suggestion.
14. Move, cut, and correct before writing new sentences. Add a sentence only when asked or when a fact the results depend on is missing.
15. In text drafted from the author's notes, write what the notes say. Do not add a closing sentence that links the point back to the larger work.
16. Choose terms the author already uses, listed in [vocabulary.md](vocabulary.md). Define a term the author has only read.
17. State the thesis of a long work in one sentence. In the author's own work, repeat it in the same words in the abstract, the introduction, and the conclusion. Field dissertations rarely do this, so its absence is not a fault in another writer's paper or thesis.
18. On slides, use few words in a spoken, scientific but casual tone. Report results as measured, keep premises plain, and keep the lines the author wrote.
19. Tell the motivation of a talk or video as a story about the problem, not as a summary of results, and do not overstate what systems can do now.
20. Write for a reader from a neighboring field. Gloss terms at first use, name the members of any counted set, give one case after a general claim, and give the measure and size of each comparative claim in an abstract, introduction, or summary.
21. Before changing a sentence, check any record of the author's earlier decisions on it. Raise a declined change again only as a question.
22. In text that an assistant drafts or revises, remove the patterns that read as machine-written. The most common are a contrast with a claim that nobody made, importance claimed in general terms, a sentence that announces that a point matters, a trailing clause that only comments, a set of three by habit, stacked hedges, and a closing sentence that restates its paragraph. Judge them by how often they recur in the draft rather than by one occurrence, and do not reword a sentence the author wrote only to remove one.
23. Keep most sentences plain and descriptive, and do not use absolute words such as the only, completely, always, or never unless the claim is literally true or the word is part of a technical term. Keep the story of the research, which is the problem, why it matters, the key intuition, and the contributions, to the abstract, the introduction, the conclusion, and the few sentences that state the main point of a method or results section. Use a turn of argument and evaluative wording only there, so that these passages stand out and a reader who reads only them learns the main contributions.

## 1. Word choice

### Verbs for research actions

Choose the verb by the work performed. Investigate or examine a question, characterize a pattern, design a study, recruit participants, collect data, annotate demonstrations, analyze a relationship, evaluate performance, and validate through a stated check. Propose, present, and introduce name a contribution without claiming an outcome. Describe names a direction, and formalize promises a formal definition that follows. Investigate does not establish an effect, and evaluate does not say that the outcome was favorable. Do not turn an open question into demonstrate or prove.

**Forms.** A [study type] was conducted to examine [question]. [Method] was evaluated on [tasks] against [baselines].

- ✗ “are formalized as Agentic Robotics and Agentic HRI” → ✓ “are described in this section as agentic robotics and agentic human-robot interaction (HRI)” (no formal definition followed)

### Operations and what signals provide

Prefer the operation to a vague benefit, such as predict feedback values, infer a reward function, align rewards with annotations, or rescale scalar feedback. For a signal, use describes, indicates, reflects, carries, or provides according to the information it represents. A method name is the subject of its own computations, not of the researchers' observations. Say what each source of information contributes before calling two sources complementary. Enable takes an agent and an action, as in enables robots to detect. Leverage means using something that already exists.

**Forms.** [Method] infers [quantity] from [input]. [Signal A] provides [dimension A], while [signal B] provides [dimension B].

- ✗ “Demonstrations supply dense information …, and progress supplies sparse information” → ✓ “Demonstrations provide dense information …, while progress provides sparse information”

### Prior work and gaps

Write prior work and narrow it to the relevant methods or studies. State the particular assumption, representation, or missing comparison. Claims such as few studies, none, and first need literature support. Interprets, assumes, and relies on make different claims, so choose the one the cited work supports. In a long work, refer to its own earlier studies by chapter or section, not by paper. Attribute a claim about the literature to the work that makes it. Studies have shown and researchers argue need a citation and a statement of what the cited work found. Instead of a list of five citations after many methods exist, name the one or two closest works and the assumption each makes.

**Forms.** Prior [method family] assumes [assumption]. Few studies have examined [specific relationship].

### Hedges and modal verbs

Each modal has its own job. Can is for a supported capability or possibility, may and might for a possible explanation, would for a conditional expectation, and tend to for a pattern that is not universal. Would be expected to states an expectation that was not measured. Write likely only when the evidence warrants it. Use significantly only for a supported statistical claim, with the test nearby. Grade the strength of evidence in words placed next to the value, such as preliminary evidence, limited evidence, or a trend towards, with the p value beside a trend. Do not lower can to may in the author's sentence as a matter of routine.

- ✗ “may benefit learning” (suggested) → ✓ “can be beneficial” (kept)
- ✗ “which should matter more when …” → ✓ “would be expected to matter more when …”
- ✗ “relatively high correlations” → ✓ “positive associations with feedback accuracy, with correlations of 0.25 and 0.16, respectively”

Use one hedge for one uncertainty. Could potentially, may possibly, and might perhaps put two words on one doubt, so keep the one that states it. Replace a degree word that stands in for a value, such as somewhat, relatively, fairly, or to some extent, with the value or the comparison. A hedge that carries the strength of the evidence stays, since removing it would overstate the claim.

### Value words and novelty

Use effective, robust, informative, promising, and similar words sparingly, next to the result or mechanism that gives them meaning. Robust must say robust to what. Prefer a concrete contribution to a claim of importance, and replace a claim of being the first with what the work does. Under-explored as [role] states a gap without claiming that a thing is new.

- ✗ “feedback magnitudes deserve attention” → ✓ “differences between teachers appear mainly in the magnitude of feedback”
- ✗ “this is the first work that systematically characterizes” → ✓ “This chapter systematically characterizes”
- ✗ “STEADY is the first algorithm that enables” → ✓ “STEADY enables”

Do not claim importance in general terms. Plays a crucial role in, paves the way for, sheds light on, opens new avenues for, and is a testament to say that something matters without saying what changes. Name what the result changes, for which task or reader, and by how much, or cut the claim. Replace an intensifier that stands in for a count, such as extensive experiments, a wide range of tasks, or numerous studies, with the count or the list.

### Small word choices

The author prefers concrete, plural, and literal nouns, and joins two adjectives with and. Write a portion of the behaviors, sampling for the active choice of data, prioritized for what is handled first, steps for the points of a task, and quantities for what two signals describe. Write argue for the claim of a cited paper and one reason for a cause that a paper names among others. These belong to their context and are not global replacements. Never replace a defined technical term with one of them.

- ✗ “a larger share of the demonstrated behavior” → ✓ “a larger portion of the demonstrated behaviors”
- ✗ “a short, clear one” → ✓ “a short and clear one”
- ✗ “failed demonstrations are always annotated” → ✓ “failed demonstrations should be prioritized for annotations”

### Words to avoid

Words that read as AI-drafted academic prose, such as delve, landscape, pivotal, underscore, and multifaceted, are absent from the author's papers. [vocabulary.md](vocabulary.md) lists them, the phrases the author replaced, and the words the author tends to overuse.

## 2. Wording of claims

### Voice

Keep the directness of the papers and choose one voice for the document. A paper uses we for what the authors did. The author's dissertation uses an impersonal voice, with this dissertation, this chapter, the study, the method, participants, or the results as the subject, and a procedural passive where the procedure deserves emphasis. This is the author's choice and not a field norm, since all seventeen dissertations in [field-conventions.md](field-conventions.md) use we, between 3.0 and 27.0 times per 1,000 words. In another writer's paper or thesis, keep the voice the writer chose. A chapter or paper can propose, examine, or present, but it does not collect data, find results, or improve anything. Give outcome verbs such as improves or enables to the method or the results. Changing the subject must not change the strength of a claim, so found does not become suggested.

**Forms.** We conducted a study → A study was conducted. Our key insight is that → The key insight is that. [Chapter] collected [data] and found [result] → In [chapter], [data] was collected. The results show that [result].

- ✗ “The second stage indicates that it can” → ✓ “The results of the second stage indicate that it can”
- ✗ “From prior work, we expect that binary feedback is noise-reduced” → ✓ “From prior work, binary feedback is expected to be noise-reduced”

### The document as the subject

Keep This paper, This chapter, or This section as the subject of a verb that describes what the text itself does, such as argues, asks, analyzes, defines, focuses on, investigates, measures, and builds on. Replace it when a more specific actor does the work, such as the results, a method, or an instrument. Drop in this chapter where it only repeats the scope of the sentence. Do not replace it with a frame built on a noun. A repeated This chapter in an opening is acceptable.

- ✗ “The study is based on the premise that” → ✓ “This chapter argues that”
- ✗ “The question that follows is whether” → ✓ “This chapter asks whether”
- ✗ “Here, [term] is defined as” → ✓ “This chapter defines [term] as”
- ✓ “This chapter demonstrates that” became “The results demonstrate that”, and “In this chapter, k is set to 20” became “In the experiments, k is set to 20”.

### Reporting findings

Choose the reporting form by its job. The analysis found and the results showed report observations, the results indicate summarizes a pattern, this suggests or which suggests introduces a bounded interpretation, are consistent with links to earlier evidence, and motivates names a next step that the data did not test. Keep the reporting frame, such as Results indicate that, when a result moves into a discussion. Write associated with for an association, not shaped by or affected by. Demonstrates needs direct evidence, and confirmed needs a stated check. Both which suggests that and suggesting that are the author's forms, so do not change one into the other. Do not rotate verbs for variety.

**Forms.** Results indicate that [result] ([source]), which suggests that [bounded interpretation].

- ✗ a suggestion that deleted “Current results indicate that” → ✓ the author put back “Results indicate that”
- ✗ “non-expert feedback is shaped by” → ✓ “non-expert feedback is associated with”
- ✗ “and they support the selection of what to annotate” → ✓ “This motivates the selection of demonstrations to annotate”

Do not end a sentence with a clause that comments on it without adding a fact, such as highlighting the importance of [topic], underscoring the need for [method], or showcasing the potential of [approach]. Give the fact that the clause points to, or cut the clause. A trailing clause that states a bounded interpretation, such as suggesting that [interpretation], reports a result and stays.

### Differences that were not detected

Report what the comparison detected, as in no difference in [measure] was detected between [A] and [B], or no statistically significant difference was found. Name the compared groups and any tolerance or criterion. A nonsignificant result does not establish equivalence, identical performance, or the disappearance of an effect. For a planned comparison, write similar performance unless an equivalence test is planned. A second sentence can say what the result does not mean.

- ✗ “the difference vanishes” → ✓ “With an agreement tolerance of ±2, we did not detect a difference in self-consistency between scalar and binary feedback”
- ✗ “can obtain equivalent performance” → ✓ “can reach similar performance”
- ✗ “does not need extra workload and time” → ✓ “no significant difference in workload or completion time was detected”

### Numbers and comparisons

Put the measured outcome and its baseline in the same sentence. Use N out of M for counts, give the denominator of a percentage, keep units, and distinguish percentage points from relative percentages. A quantitative result names the measure, gives the values with their spread, and gives the test with its statistic and p value. Join two values with compared with in a sentence and against inside parentheses. Use the exact count that the paper reports. Do not turn a correlation into prediction or causation, and do not add a test or a spread that was not computed.

**Forms.** [Method] achieved [value A] on [metric], compared with [value B] for [baseline]. [N] out of [M] participants [action].

- ✗ “was 11.6 for progress and 25.5 for scalar feedback” → ✓ “was 11.6 for progress, compared with 25.5 for scalar feedback”
- ✓ “(in Lift, 17.1% against 5.6%)”
- ✗ “over 5000 pieces” → ✓ “4,655 pieces”

### Hypotheses and verdicts

State the expectation in plain language, give it a stable label, and attach the verdict to the result that decides it. Write supported, not proven. Report an unsupported hypothesis as plainly as a supported one, and state partial support in words. A short verdict, such as H1 is supported, comes after the measure and the test.

### Possible explanations

Give the result before its possible explanation. Write one possible explanation is, this might be because, or this may be due to when the mechanism was not tested. Reserve this is because for an established procedural or mathematical reason. This explains why can overstate. When two readings remain open, write it is unclear whether [A] or [B].

### Qualifying a result

Qualify a sentence when it misstates what the evidence shows. That covers a null result written as no difference, a cause or intention that was not measured, a guarantee, a heading that claims more than its section, and a result that one scenario established. Do not narrow a positive result that the paper reports with a test, and do not add sentences that only say the evidence is weak. Raise those as questions to the author instead of changing the text.

- ✓ “are often intentional” became “may be intentional”, and “explains why” became “may help explain why”.
- ✓ “are shown to be robust to reward hacking in two representative scenarios” became “a qualitative analysis illustrates how progress alignment can discourage two examined reward-hacking behaviors”.
- ✗ “PHIRL obtains higher returns than all four baselines” (suggested) → ✓ “PHIRL significantly outperforms IRL baselines” (kept, since the paper tests it)
- ✗ an added sentence saying the results “give only weak evidence for the absence of a difference” (declined)

### Conditions attached to benefits

Keep the treatment or reference condition attached to a benefit, as in [signal] can benefit learning when [condition]. Name the processing method when properly handled would hide the actual operation. Do not delete when or if while tightening a sentence. Would does not become does without evidence.

### Limitations and future work

A limitation names the design choice or assumption, the claim it limits, and the test that would address it. Announce it in a short sentence and list each limit with its consequence, without apology. Write planned work with Future work could, One planned step is to, and would for what a planned study does. Keep the scope of a plan general, with such as before an example, when exact details may change. Do not replace a scoped contribution with a generic disclaimer. Future work can consider and can be beneficial are the author's forms.

- ✗ “Future work should extend [method]” → ✓ “Future work could extend [method]”
- ✗ “These strategies should be compared” → ✓ “These strategies would be compared”
- ✗ “the main-track papers of [conference] from 2006 to 2025” → ✓ “the papers from Human-Robot Interaction conferences, such as …”

### Contribution statements

State the contribution as the research operation, the method, the characterization, or the dataset, at the strength the evidence supports. Keep a contribution distinct from an aspiration, and keep a dataset, a characterization, and a performance improvement as different kinds. A colon after a complete lead-in, such as This work makes the following contributions, is fine.

### Terms and definitions

Define a term in a full sentence where it first matters, in ordinary language, and then give its notation and range. Put the sentences that define symbols, loss terms, and superscripts before the algorithm, equation, or figure that uses them, and say what each superscript or subscript stands for, such as gt for ground truth. Keep the author's definitions as written, and ask before changing one to match another part of the work. Spell out a name before its acronym. Refer to chapters, sections, and figures by label, not by a typed number. Spell names the same way throughout. Never change a scale or a scientific quantity for consistency.

- ✗ “defined as non-optimal behaviors in human demonstrations” (suggested) → ✓ “defined as structured imperfections in human demonstrations” (kept)
- ✗ “completion rate” → ✓ “degree of completion” (rate suggests speed or a share of successes)
- ✗ “The formative VLM study” → ✓ “The formative study with a vision-language model (VLM)”

### Scope

Say early, in one or two sentences, what the work does not cover or claim. A scope sentence answers a question that a reviewer would otherwise ask. The excluded topic often returns as future work.

**Forms.** The scope of this work is limited to [setting or population]. [Topic] is not directly addressed in this work.

## 3. Writing style

### Practical purpose

Ground the motivation in what a system needs to learn, what users can provide, and what makes the learning difficult. Move from the requirement to the obstacle and to the response. A practical motivation is not evidence of success in deployment. Avoid opening every paragraph with the same purpose clause.

**Forms.** To [goal], robots need to [capability]. [Source] makes [benefit] possible, but [difficulty] limits [outcome].

### Direct subjects and concrete details

Open a sentence with its subject, not with a That clause. Follow an abstract claim with the task, object, count, or observation that makes it checkable. Concrete detail comes from the study, never from an invented scenario presented as data. A sentence that could appear unchanged in another paper says nothing about this one. Replace it with a fact, mechanism, or result of this work, or cut it.

- ✗ “That progress alignment discounts sidetracks is therefore an inference” → ✓ “The expectation that progress alignment discounts sidetracks is therefore an inference”
- ✗ “associated with who the teacher was” → ✓ “associated with the characteristics of the teacher”

### Writing for a reader outside the subfield

A committee member or reviewer from a neighboring field reads each claim with four questions in mind. What is it, how was it measured, by how much, and what does one case look like. Answer them in the text.

- Gloss a technical term in one clause the first time it appears in a chapter or paper, such as policy, advantage, oracle, or a coined label like data flywheel.
- When a sentence counts the members of a set, such as six domains or two behaviors, name the members there or point to where they are named.
- Introduce a central signal or measure by what it is, who provides it, on what scale or interface, and one example value. Where a later chapter relies on it, remind the reader in one clause.
- After a claim that something is frequent, varied, noisy, useful, or hard, give one concrete case from the study.
- Give an evaluative or comparative claim its measure and its size the first time it appears in an abstract, introduction, or summary, as in more accurate (55.83% against 32.59%).
- Replace a vague noun such as issues, factors, ways, or patterns with the specific thing, or cut it.

Take these details from the work itself. Where the text does not contain them, mark the gap for the author instead of inventing them. When the author asks for a revision for clarity, these additions count as asked for.

- “which are?” (a reader, on “six key domains of human characteristics”)
- “by how much?” (a reader, on “can improve prediction accuracy”)
- “But what is it?” (a reader, on “a type of human feedback that is under-explored as a human teaching signal”)

### Describing people without blame

Describe the behavior precisely, then the task demand, interface constraint, or plausible reason. Do not call a person unreliable when the measured property belongs to their input. State whether a reason was measured, interpreted, or hypothesized, and do not infer a mental state that was not measured. An inefficient but useful accommodation is different from a harmful error.

- ✗ “A human demonstrator who is unsure at such a point pauses” → ✓ “At such a step, a human demonstrator may pause” (the study recorded pauses, not uncertainty)

### Explaining the mechanism

Confidence in a method comes from an understandable computation. Give the intuition in ordinary language, then how the method implements it, then the evaluation claim in a separate sentence with its task and comparison. An analogy is announced as one and returns promptly to the method. Effective, novel, and robust do not explain a computation.

**Forms.** The intuition is that [relationship]. [Method] transforms [input] into [output] by [operation].

### Observation, interpretation, and explanation

Separate a direct measurement from its interpretation and from a possible cause. Do not weaken an observation with an unneeded may, and do not strengthen an association into causation. Separation does not require two sentences, since a result and its which suggests that clause can share one.

### Literal wording

State the relation between findings with literal verbs, such as suggest, are consistent with, help explain, were evaluated separately, and provided. Prefer a concrete scenario to a figurative summary. Keep the register formal, with no contractions or idioms. Use is, has, and can where they are accurate. Serves as, stands as, and functions as often only avoid is, and has the ability to and due to the fact that are longer forms of can and because.

- ✗ “Read together, the two studies point to three sources” → ✓ “Together, these findings suggest three sources”
- ✗ “point in the same direction” → ✓ “are consistent with each other”
- ✗ “the argument was tested link by link” → ✓ “the stages of the argument were evaluated separately”
- ✗ “by two routes” → ✓ “in two ways”
- ✗ “were lost at similar kinds of points” → ✓ “failed at similar kinds of steps”

### A plain tone, with the story in a few places

Write most sentences in a plain and descriptive tone. A method passage says what the method takes as input, what it computes, and what it returns. A results passage says what was measured, under which condition, and what was found. These passages need no evaluative adjectives, no wording that carries feeling or a stance, and no turn of argument, so the reader can read most of the paper at an even pace.

Keep the story of the research to a few places. The story is the problem, why it matters, the key intuition, and what the work contributes. It belongs in the abstract, the introduction, and the conclusion, and in the few sentences that state the main point of a method or results section, such as its key intuition or its main finding. In these places the writing can turn from what prior work assumes to what it overlooks, as in However, [prior assumption] overlooks [behavior], and it can use evaluative and vivid wording, such as a key problem, the central insight, or a sentence on why the problem matters for [task or users]. A reader who reads only these passages should learn the problem, the insight, and the main contributions. If every paragraph is written this way, the paper is tiring to read and no point stands out.

What a sentence does decides which kind it is, not its connector. A contrast that reports a difference is description and can appear anywhere, as in [A] was higher than [B], whereas [C] did not change, or However, no difference in [measure] was detected for [B]. A turn that builds tension sets the work against an assumption or a problem, and it belongs to the story passages.

Do not use absolute or extreme words, such as the only, completely, entirely, fully, totally, perfectly, absolutely, always, never, fundamentally, dramatically, drastically, vastly, and extremely. Where the evidence shows a degree, give the value or the comparison. An absolute word stays when the claim is literally true and the text shows it, as in [condition] was the only condition in which [measure] changed, and in a technical term, such as fully complete and totally incomplete for the endpoints of a progress scale. The story passages follow this rule too, since their force comes from the problem and the evidence. The rules on importance claimed in general terms and on the words that the papers do not use, listed in [vocabulary.md](vocabulary.md), hold in every section.

### Emphasis

Use italics for a technical signal name and, selectively, for a key intuition. Use bold for run-in headings. Quotation marks can mark an informal label. Emphasize sparingly, since repeated bold or italic sentences compete for attention.

Do not announce that a point matters. It is worth noting that, it should be noted that, it is important to note that, importantly, interestingly, and needless to say tell the reader how to weigh a sentence instead of giving a reason. Delete the announcement. If the point still needs weight, give the reason or the size of the effect. A frame that introduces content, such as The key insight is that [statement], is the author's form and stays.

## 4. Sentence style

### One main job per sentence

Give each sentence one main job, while a related comparison, condition, or explanation stays attached. Split a sentence that reports two studies, two findings, or two requirements. Keep together a result and the which clause that interprets it, a chain of results joined by but, a while contrast, and a numbered list of questions or findings with the sentence that introduces it. Sentence length is not a target. Experienced writers in the field average 20 to 26 words, and a short sentence can mark a conclusion.

- ✗ “… grasps. These are the steps that …” → ✓ “… grasps, which are the steps that …”
- ✗ “… This suggests that annotations differ” (split off) → ✓ “…, which suggests that annotations differ”

### Few colons and semicolons

Before writing either mark, try to state the relation in words. A which clause can introduce what a colon would, since or because can attach a reason, such as or including can attach examples, and whereas, while, or but can carry a contrast. A second statement can be a new sentence. Keep a colon in four places, which are before a numbered or listed set, after The key intuition is that, after a sentence that names a property and before the clause that spells it out, and before a quotation. Keep semicolons only between the items of a long list whose items contain commas. Replace every em dash with a comma, a which clause, or a new sentence. Do not put a dash or parentheses where the colon was, and do not join two statements with and when the relation is a reason or a contrast. Equations, citations, headings, and quoted text are outside this rule.

- ✗ “a design choice that recurs in the later chapters: comparing a value” → ✓ “a design choice that recurs in the later chapters, which is to compare a value”
- ✗ “since they may be the most informative: low-quality demonstrations can inform” → ✓ “since low-quality demonstrations can inform”
- ✓ kept “Each stage addresses one question: whether …”

### Parentheses

Parentheses hold a compact example, count, abbreviation, statistic, or figure reference that the sentence does not need in order to be read. The sentence must read correctly without them. A governing condition stays outside, and parentheses never carry a second argument. Use e.g. for examples and i.e. for a restatement.

### Connectors

Use However at the start of a sentence for a contrast, Thus or Therefore for a supported consequence, Specifically for an elaboration, For instance for a case, First, Then, and Finally for a real sequence, and In addition, Additionally, or Moreover for an added point. Many sentences need no connector. Do not rotate connectors to avoid repetition. Consequently claims that the sentence follows from the one before. Do not open consecutive sentences, or most paragraphs of a section, with connectors such as In addition, Additionally, Moreover, and Furthermore. When each sentence adds one more point, join the related points in one sentence or state how they relate.

- ✗ “Consequently, interactions are hard to identify” → ✓ “In addition, interactions are hard to identify”
- ✗ “They suggest, however, that” → ✓ “However, they suggest that”

### Examples

Follow a general claim at once with one case. For instance or For example introduces it, the case names the actor and what happens, and a final clause says what it illustrates. Mark a hypothetical case as hypothetical. One example is enough for one claim. A claim that a behavior is common or that a signal is useful needs a case from the study, not only a count.

### Roadmaps

Open a substantial section with what it explains and, when useful, the order, with this section as the subject. One clause is enough when the paragraphs that follow open with statements that name their items. Do not list in advance what the next paragraphs name, and do not repeat a roadmap before every short subsection.

- ✗ “This section describes three such connections, which are not visible from any single study: …, …, and …” → ✓ “This section describes the connections between chapters, which are not visible from any single study.”
- ✗ an inserted “The chapters that follow address the three points listed above in order.” (declined)

### Tense

Tense follows the kind of content. An overview of a paper or chapter is in the present. A procedure that was carried out and a result are in the past. A model or method is described in the present, and the interpretation of a result is in the present. A summary at the end is in the past.

**Forms.** This [paper / chapter] presents [content]. [Study] was conducted with [participants]. [Method] infers [quantity]. [Measure] was higher in [condition], which suggests that [interpretation].

### Questions

Research questions belong in a numbered list or a heading. A question in running text is rare and comes where the motivation turns into the approach, with the next sentence beginning the answer.

## 5. Sentence structure

### Concession with while

Use While [granted point], [main point] to grant a benefit or shared property before the limit or distinction, with the focus in the second clause. While can also follow the main clause to add a contrast, and the contrast stays in one sentence. Although and even though do the same job. Make the concession substantive.

- ✗ “although less than human annotations did” → ✓ “while the improvement is less than using human annotations”
- ✗ a split into “A robot also needs to learn …” (suggested) → ✓ “while robots also need to learn …” (kept)

### Parallel items and comparisons

Keep paired factors, endpoints, operations, and list items at the same grammatical level. Describe two compared objects with stable subjects and the same dimensions in the same order, then say why the difference matters. In the former case and in the latter suit two cases. Use not only … but also sparingly. List as many items as the content has. Three adjectives or nouns in a row, such as efficient, robust, and scalable, need three claims that the work supports, and the evidence often covers one or two. Do not repeat one sentence form through a paragraph, such as the same subject and verb at the start of each sentence.

- ✗ “can inform completion shaping, negative reward samples, and better data coverage” → ✓ “can inform completion shaping, provide negative reward samples, and improve data coverage”

### A literal alternative

Use rather than or instead of to make a real alternative clear, with both sides concrete. A short contrast can be [A], not [B]. Whereas sets one actor against another. The usual alternative must be one that the cited work actually takes, never an inferior one invented to flatter the chosen approach.

- ✗ “…; an agent that optimizes a reward may stay there” → ✓ “…, whereas an agent that optimizes a reward may stay there”
- ✓ “were evaluated separately, not end to end”

Do not set a claim against one that nobody made, as in [X] is not just [Y], it is [Z], or The challenge is not [A] but [B]. State the claim directly. Keep a contrast when its negative half corrects a claim that cited work makes or a belief that the reader is likely to hold. A run of negations before the point, as in not [A], not [B], but [C], is the same pattern.

### Purpose and means

Put the purpose first when the reader needs it to understand the design choice, as in To [purpose], [action]. Attach it afterward when the design is already the topic. The purpose says what a procedure enables, not that it succeeded, so avoid to prove. Use by and a gerund for the means that performs an operation, as in [method] shapes [quantity] by [operation]-ing [object].

### Known information before new

Let each sentence take up a quantity, object, or finding introduced in the one before. Use This with a noun, such as this approach or this limitation, when more than one referent is possible, and plain This only for the statement just made. Repeat a precise noun instead of an ambiguous pronoun or a phrase such as the resulting values. Use the definite article for something already introduced.

- ✗ “Its margin over the best baseline” → ✓ “PHIRL's margin over the best baseline”
- ✗ “the resulting values carried information” → ✓ “progress values carried information”
- ✗ “A new selection strategy would be compared” → ✓ “The new selection strategy would be compared”

### Procedures and enumerations

Use one actor with parallel verbs for a single procedure, and then where order matters. Count separate reasons or premises with First and Second, and announce the number for a long paragraph. One is … The other one is … are the author's forms for two items. Separate list items with commas, and keep semicolons for a long in-sentence list whose items contain commas. Do not force three items, imply a sequence that did not occur, or add First and Second to two results that one sentence lists.

- ✗ “This section describes future work in two groups. One group addresses” (suggested) → ✓ “This section introduces future work in two aspects. One is future work that addresses” (kept)

### Local reasons and governing conditions

Keep a reason or condition next to the claim it governs. Lead with If, When, Given, or Because when an unqualified main clause could be misread as general. Put because or since after the operation when the operation is the topic. Since often takes the place of a colon before an explanation. Do not turn an if assumption into a when observation, and ask before changing if into since, which changes the claim.

### Complete clauses

Write the clause in full. A comparison gets its own subject and verb instead of ending on did, does not, or so. Repeat the verb instead of stopping at it can. The full clause must keep the claim of the short one, including any limit.

- ✗ “indicate that it can, in two ways that act at different points” → ✓ “indicate that it can act at different points in two ways”
- ✗ “which should matter more when more of the demonstrated behavior does not” → ✓ “The information from progress would be expected to matter more when a larger portion of the demonstrated behaviors does not advance the task”

### Especially and the more

Place especially after a general statement to name the case that matters most, only when the evidence singles it out. State a relationship between two quantities as the more [A], the more [B], with its statistic when it was measured.

## 6. Structure of papers, chapters, and sections

### The thesis in one sentence

A long work can be reduced to one sentence, and the writer provides it. It names the object, such as a model or a method, and what it makes possible. The author repeats it in the same words in the abstract, the introduction, and the conclusion, which field dissertations seldom do (see [field-conventions.md](field-conventions.md)).

**Forms.** The goal of this work is to [verb] [object] for [purpose].

### The introduction

Build the introduction around the practical task and one particular assumption in prior work. Say what that assumption may overlook, why it matters, and the bounded question that follows. Then give the insight, the approach, the study, the main findings, and the contribution. Name the gap precisely, with what prior work covers, what it leaves out, and why. A short concrete scene can show the problem before it is stated in general terms. Reach the statement of what the work does early. These moves are an organizing default, not a fixed paragraph count. Do not dismiss prior work or present a later finding as already established.

**Forms.** Practical stake → prior assumption → overlooked behavior → question → approach → findings → contribution.

Do not open a paper, an abstract, or a section with a stock sentence about the field, such as In recent years, [topic] has attracted increasing attention, With the rapid development of [technology], or Despite recent advances in [field]. Open with the practical task or the specific limitation that the work addresses.

### Openings of a chapter or paper

In a work of several chapters, open each one with a sentence that places it in the larger work, such as This chapter completes the first stage of this dissertation. Then give the chapter's own introduction, which runs from the gap, through the aim or insight and what the chapter proposes, to the study with its participants and task, the main findings, and what they are useful for. Say where the code and data are, and end the opening with the related-work pointer and the original publication. Keep one statement of the aim or contributions near the start, and keep the study summary with its participant counts even if a later section repeats it. Cut a sentence that repeats one a few lines earlier, general background, and a second statement of the findings. The goal is to reduce the feeling of starting a new paper in every chapter. Revise an opening by moving and cutting sentences, not by writing new ones.

- ✓ “It analyzes demonstrations of a long-horizon manipulation task provided by 40 non-experts” became, in the author's own edit, “The main contributions of this chapter are characterizing and categorizing non-optimal behaviors”.
- ✗ cutting “The validation studies covered a wide range of scenarios and involved 116 participants in total” (declined, the sentence stayed)

### Connecting the parts of a long work

Connect the parts through questions and responses, and say what each part makes available to the next. Name the stages with the verbs of the title. A limit found in one study can be named as the reason for the next. The stages are a conceptual dependency, not one controlled experiment, so keep differences in tasks, participants, scales, and evaluations visible. A study can motivate a method without validating it.

**Forms.** The first stage asks [question] and establishes [bounded finding]. Building on [result], the next stage examines how [source] can inform [object].

### From a finding to a method

Make the handoff explicit. The finding leaves a difficulty, an intuition addresses it, and a mechanism implements the intuition. Introduce an unfamiliar method by what its signal means, then the relationship it uses, its notation and assumptions, its operations, and the evaluation question. Do not list symbols or losses before their purpose.

**Forms.** Problem → meaning of the signal → intuition → notation → operations → evaluation design.

### Scenarios and episodes

Use the shortest familiar scenario that makes an abstract difficulty visible, label it as hypothetical, and return promptly to the technical point. One running example can be reused within a paper by changing one detail at a time. Report a real episode in action order, with the obstacle, the adjustment, the outcome, and its link to the measure. Use only episodes and participant remarks that the study recorded, and do not treat one episode as evidence of how common something is.

### Headings

A results heading states the question answered or the supported finding. A discussion run-in heading has a concrete subject. Write a finding as a statement heading only when the section supports it, and keep a question heading when the evidence is mixed. A future-work heading names the direction. A heading must not claim more than its section.

- ✗ “Are the imperfections in non-expert teaching random noise?” → ✓ “The imperfections in non-expert teaching are not random noise.” (after the question was answered)
- ✗ “PHIRL Learns More Robust Reward Functions” → ✓ “Reward Functions in Two Reward Hacking Scenarios”

### A results paragraph and a study

Report every study in the same order, so the reader finds the same information in the same place, with questions or hypotheses first. A results paragraph moves from the question to the condition and measure, the paired outcomes, the test, and the verdict, and repeats that frame for each condition before explaining what changes across them. When a result goes against expectation, name the mismatch and give possible reasons as hypotheses. Do not manufacture surprise or call a result interesting without naming the tension.

### Discussion and synthesis

Begin with the connection or finding to explain, select the evidence from the relevant studies, and state the implication. Then name the differences that limit the comparison and close with a specific question or next step. A study discussion restates the goal, reports which hypotheses held, explains the unexpected results, states the limits, and says what the study provides next. Divide a long discussion into themed paragraphs, each opening with a short sentence or run-in heading that states its point. A synthesis adds an interpretation and does not repeat every summary. Help explain claims less than account for.

- ✗ “They also account for a design choice” → ✓ “They also help explain a design choice”

### Related work

Close a passage of related work with the specific difference in population, question, information, or method, and say why that difference is needed. A difference is not automatically an advantage. A claimed gain in efficiency or effort needs its own evidence.

**Forms.** Prior [methods] address [scope]. This work instead examines [bounded question].

### Endings

End a chapter or paper with what it showed and what that provides for the next step. Link forward only when the next part addresses the named question. Keep a final chapter short, and close a long work on what it is for rather than on a summary.

End a paragraph on its last specific point. Do not add a sentence that restates the paragraph, turns it into a general lesson, or says why the field should care. Cut a closing sentence that only repeats the preceding sentences or adds an unsupported claim of importance. Keep a concise synthesis, bounded implication, or transition when it helps the reader understand the argument and is supported by the source. A paragraph that opens with In summary or In conclusion and only repeats earlier text is the clearest case. A last sentence stays when it states a consequence that the next paragraph builds on.

### Tables that compare studies

Keep each cell short and leave procedures to the text, with a caption that says so. Keep what a reader needs to compare the studies, which is the setting with its place, the size of each group, any pilot, and a word such as non-expert that describes the participants. Write each cell as a phrase that reads on its own.

- ✗ “Replays in simulation” → ✓ “Annotators watched replays of the demonstrations in simulation”
- ✗ “Public space” → ✓ “Public space, university atrium”
- ✗ “90 crowdworkers” → ✓ “90 crowdworkers (45 per condition); 3-expert pilot”

## 7. Editing someone else's text

These rules are for a coauthor, an editor, or an AI assistant revising the author's writing.

### Correct without rewording

When a sentence the author wrote has a spelling or grammar error, correct the error and leave the rest as it is. Keep the words, the sentence boundaries, the number, the modal verb, and the compound terms. If a rewording also seems useful, propose it as a separate suggestion with its own reason, so that the correction can be accepted without it. When a correction needs a new word, choose the one closest to the author's. The same holds for slide lines the author wrote or dictated. Wording that came from the author's published papers is the most settled and was declined most often when reworded. Text that an assistant drafted can be reworded more freely.

- ✗ “Skills grounded in the literature could allow” → ✓ “Literature-grounded skills could allow”
- ✗ “In an interaction between a person and a chatbot, the two take turns” (suggested with spelling fixes) → ✓ “In human-chatbot interaction, a human and a chatbot interact in turns” (kept, and the spelling fixes were accepted later on their own)
- ✗ “whether the model continues to benefit from” → ✓ “whether the model would always benefit from”

### Do not add what was not asked for

Prefer moving, cutting, and correcting the author's sentences to writing new ones. Add a sentence when the author asks for the content, or when the text lacks a fact its own results depend on, such as the scale on which data were collected or how a measure was computed. Keep any addition minimal. Most unrequested insertions were declined, including new limitations, statements that evidence is weak, results the author had chosen to drop, sentences mapping a summary to later sections, and drafted subsections. Offer such content as a question in a review note.

- ✓ an added fact that was missing, “scalar feedback was collected on the same range as progress, from 0 to 100” (accepted)
- ✗ an inserted limitation, “an agreement statistic between the annotators is not reported” (declined)

### Remove a pattern without adding another

When revising text to remove a pattern that reads as machine-written, change only what the pattern needs. Do not replace it with another pattern, such as short fragments for rhythm, a rhetorical question, a first-person aside, or a figure of speech. Do not add a number, name, or example that the source does not contain, and do not drop a hedge, a condition, or a number to make a sentence plainer. When the fix needs a fact that is missing, mark the gap for the author.

### Write from the author's notes

When the author's notes are written out as prose, take each sentence from a note or from a source the author named, and say where a note was interpreted. Move from the starting point to the planned step and to how the step would work, and end on the step or the mechanism. Do not add a closing sentence that restates the questions of the larger work or explains why its findings matter for the new direction, and do not add detail that the notes did not ask for.

- ✗ “The questions of this dissertation would apply at this level as well.” (deleted by the author)
- ✗ “Because these outcomes include the evaluations and reactions of non-experts, the imperfections studied in this dissertation would need to be …” (deleted by the author)

### Separate kinds of change

Keep a spelling or grammar fix separate from a rewording, and a rewording separate from a change of claim. When the author fixes one location, align assistant-written text elsewhere that repeats the same problem, but only flag the author's own text elsewhere.

### Check earlier decisions

If a record of the author's earlier decisions exists, read it before proposing changes to the same sentences. A change the author already declined is raised again only as a question in a review note, even when this guide would suggest it. A reader's request that conflicts with an earlier decision goes to the author the same way.

## 8. Talks, slides, and videos

These rules are for talks and videos. A written paper keeps its own voice.

### Slide text

Write slide text in few words and in the tone a presenter uses aloud, scientific but casual. Prefer a figure, chart, or video to a sentence, and leave the rest to the speaker notes. A title plainly says what the slide shows. First person is normal on slides. Keep a line the author wrote or dictated word for word and fix only its grammar.

**Forms.** Often occurred within 4 s of a task-phase change. Compare under the same human time. They give negative examples and cover more of the task.

### Measured results and plain premises

Report a result on a slide as it was measured, as in the paper. Write no significant difference, or similar (n.s.), for a test that found none, and in this study where scope matters. Keep the premise of the talk plain and direct, including a widely held view that the talk sets up in order to question it. Do not add a qualifying clause or a number to a short caption unless the caption is wrong without it.

- ✗ “no detectable difference” → ✓ “no statistical significance” (the author's own slide edit)
- ✗ “STEADY reached a 4.2 higher return than binary feedback” → ✓ “STEADY reached a higher return than binary feedback”
- ✓ kept “It is widely accepted that human demonstrations are noisy and multi-policy.” Removed “Everyone in the field agrees”.

### A motivation told as a story

Tell the motivation as a short story about the problem, in the order of the author's outline, and set up the problem rather than summarizing what the work already did. Each caption says its point plainly. Avoid references that the audience has to decode. Do not overstate what systems can do now. The author's motivation for this research runs as follows. Robots are already part of daily life, but most of their training data are recorded in labs, and many learning methods require clean data. To be part of everyday life, robots need to learn from everyone, and not everyone can provide clean data.

### Future work and the closing slide

Give future work as what the direction is and what it would make possible, and move the record of what has been built to the speaker notes. Keep untested parts conditional, as in could improve. A closing slide states at a high level how each part builds on the one before.
