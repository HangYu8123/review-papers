# Vocabulary

Words and terms for writing about robot learning from human input and human-robot interaction. Part 1 is the author's own vocabulary, taken from six published papers and their drafts (about 54,000 words), with an estimate of how familiar each term is to the author. Part 2 is the vocabulary of five robotics and HRI dissertations (about 245,000 words), which shows what expert readers in the field know without a definition. Part 3 lists words to watch. Part 4 lists acronyms. Counts, examples, and sources were removed to keep the file small.

Use the [writing style guide](writing-style-guide.md) for how to use the words. A term the author writes routinely needs no explanation. A term the author has only read or seen in a title needs a definition on first use, or a check that its field meaning fits.

## How familiarity is marked

| Mark | Meaning | How to use it |
| --- | --- | --- |
| Core | Used in at least three of six studies and at least five times, or in two studies at least twenty times | Use it without explanation |
| Familiar | Used in two studies, or at least five times in one | Use it freely |
| Chosen | Not in the papers, but set as the preferred wording by the style guide | Use it as the guide says |
| One study | Used two to four times, all in one study | Keep to that sense |
| Once | Used once | Prefer a Core or Familiar word, or check the sense |
| Read only | Not in the papers, but used in the field dissertations | Define it on first use and check the field meaning |
| Cited only | Seen only in the title of a cited work | Gloss it on first use, or ask before relying on it |

A count is by word form, so a common word such as state, return, or progress counts in every sense.

## Terms with fixed meanings

These distinctions recur in the author's papers. Keep them stable and never swap them for variety.

- **People.** Non-experts are the general population, participants are the people in a study, demonstrators control the robot, and annotators label data. Human teachers suits broader teaching claims. Non-expert describes relevant experience, not ability. Do not assume that demonstrators and annotators were the same people.
- **Settings.** Public space, passersby, crowdworkers, online study, in-lab, and non-lab are distinct settings. Name the setting when it affects how a result is read.
- **Imperfection.** Imperfections is the umbrella term. Sub-optimal departs from an optimal policy or trajectory, noisy has relevant variability or errors, and unsuccessful fails the task. Patterned, systematic, and task-related need an analysis that shows structure. A non-optimal action does not make a whole demonstration a failure, and patterned behavior is not automatically intentional or beneficial.
- **Teaching signals.** Binary evaluative feedback is a two-way evaluation, scalar evaluative feedback is an evaluation on a scale, and *progress* describes the cumulative degree of task completion. Progress annotations or labels are the collected values. Feedback, progress, reward, reward function, and policy have separate roles in a learning formulation. Italicize *progress* when it names the signal.
- **Completion.** Write degree of completion, not completion rate, since rate suggests speed or a share of successes.
- **Information.** Say what each signal contributes, such as dense policy-level information or sparse local evaluations, before calling two signals complementary. Density, scope, precision, and accuracy are separate dimensions, and dense does not mean accurate.
- **Consistency and robustness.** Name the unit of comparison, such as consistency within a participant or across participants, direction accuracy or numerical precision. Robust must say robust to what. Consistent ratings can still be systematically inaccurate.
- **Scales.** Explain a scale by its endpoints and reference states, as in a value of 0 indicates that the task has not yet begun and 100 indicates completion. Shared endpoints do not make intermediate values comparable across users or tasks. Never change a scale to make chapters look consistent.
- **Operations.** Predict and infer are not interchangeable when their targets differ. Alignment does not imply numerical identity. Formalize promises a formal definition. Validate needs a stated check. Evaluate does not say the outcome was favorable. Write account for systematic variation in human teaching for what a method does with structured imperfection, not admit or tolerate.
- **Codes and RL terms.** Write a codebook developed through open coding, and advantages for the RL quantity, not advantaged rewards.

## Part 1. The author's vocabulary

Terms are grouped by topic. Within each mark, the most used come first.

### Research areas and learning paradigms

- **Core.** reinforcement learning, reward learning, inverse reinforcement learning, learning from demonstration, learning from human feedback, human-in-the-loop, machine learning, robot learning, interactive reinforcement learning, learning from human demonstration, behavioral cloning
- **Familiar.** reward shaping, preference learning, interactive machine learning, robot manipulation, offline, policy shaping, online learning, learning from non-expert demonstrations, optimal control, imitation learning, learning from imperfect demonstrations
- **Chosen.** agentic human-robot interaction, agentic robotics
- **One study.** reinforcement learning from human feedback, deep reinforcement learning, active learning, interactive learning, skill acquisition
- **Once.** human-robot interaction
- **Read only.** socially assistive robotics, shared autonomy, motion planning, computer vision, social psychology, meta-learning, cognitive science, computer-supported collaborative work, human-computer interaction, multi-task learning, natural language processing, trajectory optimization, value alignment, supervised learning

### Human teaching signals

- **Core.** progress, human feedback, scalar feedback, task completion, binary feedback, feedback value, progress annotation, teaching signal, progress label, human teaching, human knowledge, human preference, fully complete, ranking, completion rate, evaluative feedback, totally incomplete, human teaching signal, critique
- **Familiar.** preference feedback, task progress, VLM-generated progress, confidence degree, degree of task completion, end progress, delta progress, preference queries, progress value, facial expressions, feedback modality, cumulative task completion, online progress label, progress signal, raw scalar feedback, start progress, teaching style, trajectory pair, eye gaze, five-point scale, numerical evaluation, verbal feedback, human label, correction, human binary feedback
- **Chosen.** binary evaluative feedback, degree of completion
- **One study.** pairwise comparison, prior knowledge, feedback value scale, progress feedback, completion percentage
- **Once.** feedback mechanism, scalar evaluative feedback
- **Cited only.** implicit feedback

### Demonstrations, annotations, and datasets

- **Core.** demonstration, human demonstration, dataset, annotation, annotate, label, non-expert demonstration, successful demonstration, demonstration dataset, failed demonstration, oracle, data collection, expert demonstration, high-quality demonstration, optimal demonstration
- **Familiar.** demonstration quality, annotated demonstration, keyframe, human annotation, auto-generated annotation, high-quality dataset, mixed-quality dataset, subset of demonstrations, low-quality demonstration, sub-optimal demonstration, annotated subset, annotation percentage, demonstration horizon, error-free demonstration, imperfect demonstration, partial demonstration, perfect demonstration, annotation coverage, data annotator, ground truth, noisy demonstration, training data, data quality
- **One study.** machine-generated demonstration, unsuccessful demonstration
- **Once.** oracle demonstration

### Reinforcement learning and reward learning

- **Core.** reward, reward function, trajectory, policy, state, domain, agent, learned reward, reward hacking, action, learned reward function, environmental reward, advantage, horizon, return, robust reward function, alignment, exploration, observation, loss, optimal policy, reward model, environment, learning agent, magnitude, learned policy, pre-trained agent, reward signal
- **Familiar.** sub-trajectory, discriminator, generated trajectory, generator, reward hacking scenario, cumulative reward, shaping component, current state, task horizon, multi-policy, optimization, completion shaping, episode, negative reward, total reward, positive reward, previous state, training loop, learning loop, potential function, progress function, timestep, dense reward, optimize, discount factor, environmental return, policy roll-out, punish, reward distribution, transition, imbalanced reward, training objective, adversarial learner, exploit, reset, trajectory generator, convergence, deterministic dynamics, end state, expert trajectory, goal state, heuristic function, maximum likelihood, optimization problem, reward design, state-only, inferred reward function, partial trajectory, sampled trajectory, state-action pair, trained agent, expert policy, initial policy, robot policy, value function
- **One study.** action sequence, local optimum, non-progressive behavior, Q-value, random exploration, reward features, reward learner, shaping loss, trajectory segment, transition dynamics, visual observation, finite horizon, infinite horizon, latent reward function, path-independent, potential shaping, temporal delta, loss function, model-based
- **Once.** exploration cost, hinge, Q-learning, sparse reward
- **Read only.** state space, SARSA, cost function, objective function, generalizable reward, reward parameters, sample complexity, true reward, action-value function, cross-entropy loss, gradient descent, tile coding, model-free, Markov decision process, partially observable Markov decision process, Q-function

### Methods, models, and tools

- **Core.** algorithm, Pref, framework, Robosuite, Robomimic, learning framework, pre-train, heuristic, language model, large language model
- **Familiar.** AIRLPref, fine-tune, hyperparameter, prompt, baseline method, DemoPref, Gemma, TAMER, batch size, checkpoint, learning rate, Adversarial Inverse Reinforcement Learning, diffusion policy, seed, COACH, hyperparameter search, RoboTurk, base model, Hugging Face, post-training, Rank2Reward, vision-language model, language instruction, ReWiND, random seed
- **One study.** DreamerV3, hidden units, MaxEnt IRL, parallel environment, DeepMind Control Suite, LoRA
- **Once.** BC-RNN, mean squared error, multilayer perceptron
- **Read only.** maximum entropy IRL, neural network, particle filter, TrajOpt, data-driven, rule-based, PyBullet, Kalman filter, Robot Operating System
- **Cited only.** generative adversarial network, proximal policy optimization

### Names and concepts from the studies

- **Core.** PHIRL, demonstration sidetracks, human characteristics, feedback pattern, human feedback pattern
- **Familiar.** PHIRL-online, STEADY, feedback delay, CHARM, Lift-Drop-Loop, poking behavior, failure scenario, Progress-Heuristicized Inverse Reinforcement Learning, Touch-And-Stay, control pattern, feedback dynamics, patterned imperfection, unaware scenario, noticing window
- **One study.** Considering Human Attributes for Reinforcement Modeling, corrected scenario, human attributes, state window, one-dimension control

### Human teachers and their behavior

- **Core.** non-expert, human characteristic, expert, noise, imperfection, mistake, workload, robot experience, sub-task, demonstrator, human teacher, sub-optimality, annotator, non-expert user, bias, human imperfection, robot expert
- **Familiar.** operator, educational background, non-optimal behavior, human factor, task phase, sub-goal, personality, teaching experience, human engagement, expertise, crowd-sourced, human effort, passersby, random error, crowdworker, human intention, human participation, mental effort, phase change, proficiency, proficient operator, teaching effort, cognitive load, harmless behavior, inconsistency, exploratory action, human expectations, human expert, non-expert participant, random noise
- **One study.** computer science background, unproductive behavior, non-expert demonstrator, system designer, everyday users, novice user
- **Read only.** bystander, end user, demographics, caregiver, human burden, human guidance, human supervision

### Social and group interaction

- **Familiar.** engagement
- **One study.** emotion
- **Once.** humanoid robot
- **Read only.** moderation, moderator, F-formation, o-space, group conversation, children with autism, spatial behavior, lower-body orientation, group interaction, proxemics, intergenerational, socially assistive robot, utterance, group cohesion, multi-party interaction, social interaction, older adults, body orientation, brainstorming, gaze behavior, family group, behavioral agency, child-robot interaction, conversational group, head orientation, spatial arrangement, focus of attention, turn-taking, human-human interaction, social behavior, social dynamics, morphological agency, addressee, collaborative game, social robot, personalized, personal space, head pose, spatial formation, companion, dyadic interaction, mutual gaze, multi-party human-robot interaction, proxemic behavior, shared attention, social presence, voice activity detection, embodied agent, embodiment, personalization, social cue, user engagement, social convention, expressive motion, group dynamics, nonverbal behavior, autism spectrum disorder

### Representations, human models, and inference

- **Familiar.** feature, likelihood
- **One study.** perception
- **Once.** data augmentation, human input
- **Read only.** intent, feature trace, situational confidence, misalignment, high-dimensional, posterior, embedding, learned feature, belief, similarity query, low-dimensional, representation alignment, misaligned, feature learning, feature function, feature space, label query, point cloud, arbitration, confidence estimation, spurious correlation, robot representation, Boltzmann rationality, human model, human representation, latent space, feature query, probability distribution, representation learning, interpretable, feature vector, privileged information, self-supervised, demonstration query, latent representation, human decision model, log-likelihood, policy blending, distribution shift, Laplace approximation, misspecification, noisily-rational, uniform distribution, Bayesian inference, goal inference
- **Cited only.** causal confusion

### Robots, tasks, and environments

- **Core.** block, manipulation, button, gripper, simulation, long-horizon, real-world, manipulation task, pour, long-horizon task, real robot, grasp, navigate, interface, ice cream topping-adding task, robot arm, deployment, topping jar, Xbox controller, Kinova, Kinova Gen3 Lite, shelf, target object
- **Familiar.** Lift, PickPlaceCan, pom-pom, bin, brush, peg, Square, stuffed animal, button-pressing task, control interface, goal location, pick and place, robot manipulation task, robotic arm, stirrer, nut assembly, simulated robot, teleoperation, coffee preparation task, degrees of freedom, robot-in-the-wild, graphical user interface
- **One study.** end effector, sim-to-real gap, square-shaped nut, Multi Human, overhead camera, Proficient Human, joystick
- **Once.** JACO, kinematic, RealSense
- **Read only.** sensor, tracking, autonomy, localization, Kinect, tabletop, microphone array, manipulator, mobile robot, autonomous robot, navigation, field of view, mobile base, RGB-D, gravity compensation, kinesthetic teaching, semi-autonomous

### Study design and data collection

- **Core.** participant, scenario, online study, condition, public space, recruit, public space study, questionnaire, replay, hypothesis, study setup, experimental setup, in-lab, exclude, consent form, non-lab
- **Familiar.** session, ablation study, real robot study, experimenter, in-person study, NASA TLX, representative scenario, university atrium, user study, video clip, Amazon Mechanical Turk, Institutional Review Board, study procedure, validation study
- **One study.** characteristic questionnaire, open-coded book, codebook, open coding, research question
- **Once.** cross-validate, Likert, pilot study
- **Read only.** survey, dependent measure, subscale, pilot session, experimental design, case study, manipulated variable, coder, sample size, interview, repeated-measures, within-subjects, informed consent, data coding, factorial design, field study, Wizard-of-Oz, counterbalance, between-subjects

### Measures, statistics, and evaluation

- **Core.** performance, baseline, distribution, correlation, mean, accuracy, data efficiency, improvement, sample efficiency, correlate, standard deviation, x-axis, significance
- **Familiar.** success rate, task statistics, ablation, learning outcome, task success, learning efficiency, normalized, reward curve, significant difference, t-test, error bar, robustness, Wilcoxon rank-sum test, completion time, converged performance, feedback accuracy, learning curve, prediction, sensitivity analysis, statistically significant, threshold, y-axis, absolute difference, confidence interval, Kruskal-Wallis H test, shaded area, average return, ceiling performance, feedback distribution, normal distribution, Pearson correlation, Shapiro-Wilk test
- **One study.** Bayesian statistics, evaluation rollouts, agreement, Holm-Sidak, p-value, spatial distribution, variance, Bayes factor, regression
- **Once.** Box-Cox, outlier, post hoc, qualitative analysis, quantitative analysis, self-consistency, Spearman
- **Read only.** main effect, ANOVA, standard error, effect size, response time, Tukey HSD, classification accuracy, REML, Cronbach's alpha, objective metric, paired t-test, interaction effect, random effect, chi-square, multiple comparisons, Cohen's kappa

### Research-writing words

#### Verbs for research actions

- **Core.** model, train, collect, shape, align, generate, sample, compare, infer, describe, propose, conduct, design, evaluate, introduce, adapt, combine, select, leverage, test, validate, assume, investigate, identify, predict, present, calculate, interpret, develop, hypothesize, assess, define, utilize, analyze, integrate, visualize, measure, assign, characterize, compute, examine, explore, extend, extract
- **Familiar.** normalize, imitate, filter, incorporate, estimate, perceive
- **Chosen.** formalize
- **One study.** illustrate
- **Once.** generalize, quantify
- **Read only.** instantiate, convey, disambiguate, anticipate, operationalize, deploy

#### Verbs for effects and findings

- **Core.** indicate, improve, require, demonstrate, achieve, reduce, represent, outperform, capture, observe, suggest, correspond, enable, mitigate, vary, affect, address, associate, reflect, differ, rely, contribute, exhibit, stabilize, overcome, detect, enhance, highlight, deviate, ensure
- **Familiar.** distinguish, minimize, maximize, bridge, reveal
- **Chosen.** discourage, prioritize
- **One study.** encompass

#### Adjectives and adverbs

- **Core.** scalar, binary, significantly, robust, consistent, optimal, significant, noisy, high-quality, effective, random, imperfect, interactive, accurate, novel, non-optimal, randomly, dense, sub-optimal, representative, diverse, independent, reliable, meaningful, numerical, complementary, crucial, statistically, temporal, evaluative, unreliable, automatically, explicitly, structured, accumulative, inconsistent, empirically
- **Familiar.** cumulative, repeatedly, sparse, alternately, critical, low-quality, jointly, patterned, informative, efficient, implicitly, inherently, iteratively, spatial, intuitively, promising, realistic, substantially, under-explored
- **One study.** data-efficient, incremental, systematic
- **Once.** little-used, monotonic
- **Read only.** expressive, generalizable, intractable, salient, tractable, qualitatively, quantitatively

#### Nouns for research ideas

- **Core.** method, characteristic, pattern, efficiency, factor, limitation, component, approach, intuition, dimension, aspect, assumption, contribution, insight, gap, representation, methodology, challenge, property, finding
- **Familiar.** bottleneck, capability, applicability, variation, scalability, mechanism, portion
- **One study.** consistency, expressiveness, paradigm
- **Read only.** trade-off, generalization, implication, formalism, desiderata, notion, formalization, usability, informativeness

### Field terms the sources never use

These standard terms were searched for and found nowhere in the papers, the field dissertations, or the cited titles. The author may still know them. MuJoCo, practice session, demonstration interface, annotation interface, median, interquartile range, mixed-effects.

### Terms seen only in cited titles

adaptation, affective feedback, autonomous, bimanual, contrastive, deception, double Q-learning, dynamical systems, EEG, egocentric, extrapolation, feedback modalities, function approximation, generalist, heterogeneous, high-dimensional state spaces, human-robot collaboration, implicit human feedback, intrinsic motivation, keyframe-based, maximum entropy, movement primitives, multimodal, nonlinear, nonparametric, off-policy, physical human corrections, physiological, planning, policy-dependent human feedback, probabilistic, reward model ensemble, scalable, self-efficacy, self-supervised, socially interactive agents, stochastic, suboptimal demonstrations, tactile, transferable, variational, visuomotor, world model.

## Part 2. Vocabulary of field dissertations

From five robotics and HRI dissertations, by Short (2017), Vázquez (2017), Bobu (2023), Matarić (1994), and Scassellati (2001). Terms are listed by how much the first three use them, most used first. A term in bold is used by all of Short, Vázquez, and Bobu. A term marked † does not appear in the author's papers, so it is familiar to these readers and new in the author's writing.

### Naming the work and its parts (writing)

Nouns for the document, its parts, and what it contributes.

**task**, **study**, **method**, **model**, **result**, **algorithm**, **experiment**, **approach**, **system**, **chapter**†, **section**, **problem**, **hypothesis**, **analysis**, **this work**, **observation**, **dissertation**†, **scenario**, **domain**, **setting**, **evaluation**, **framework**, **evidence**, **finding**, **application**, **insight**, **implementation**, **technique**, assumption, **contribution**, intuition, **methodology**, architecture, formulation, thesis†, case study†, mechanism, principle†, paradigm.

### What a chapter, study, or method does (writing)

Verbs whose subject is the dissertation, a chapter, a study, or a method.

**test**, **design**, **describe**, **enable**, **present**, **allow**, **focus on**, **develop**, **compare**, **evaluate**, **propose**, **address**, **combine**, **build**, **introduce**, **define**, **demonstrate**, **discuss**, **apply**, **leverage**, **analyze**, **explore**, validate, **examine**, **implement**, instantiate†, **investigate**, **incorporate**, summarize, **review**, showcase†, **extend**, formalize†, **integrate**, **characterize**, construct, **outline**†, utilize, tackle†, formulate†.

### Reporting results (writing)

Verbs and phrases that report what a study or an analysis found.

**find**, **show**, **support**, **suggest**, **affect**, **increase**, **observe**, **improve**, **result in**, **reduce**, **indicate**, **lead to**, **the results**, **achieve**, **predict**, **influence**, **significant difference**, decrease, **reveal**, **no significant**, **correlate**, **our results**, **differ**, outperform, **contribute to**, account for, confirm, perform better†, yield.

### Hedges and graded certainty (writing)

Modals, adverbs, and phrases that grade how firm a claim is.

**can**, **may**, **could**, **would**, **might**, **often**, **possible**, **likely**, **limited**, tend, **suggesting that**†, typically, **trend**†, approximately, **appear**, **potentially**, seem†, **slightly**, **sometimes**, **generally**, relatively, preliminary†, possibly, perhaps†, partially, it is unclear, **some evidence**†, some support†, unlikely, it is possible that†, roughly†, usually, to some extent†, marginally†, mostly, somewhat†.

### Connectives and sentence openers (writing)

Words that open a sentence and mark its relation to the one before. Openers are counted only at the start of a sentence, before a comma.

**while**, **because**, **However**, **since**, **For example**, **that is**, **although**, **rather than**, **Finally**, Additionally, **Thus**, **First**, Moreover, Unfortunately†, whereas, Lastly, **Furthermore**, **instead of**, **In general**†, In particular†, For instance, **Overall**, **Second**, Instead, Then, In addition, **In contrast**, As a result, Interestingly†, **Similarly**, Therefore, Importantly†, In other words†, Nonetheless†, Hence†, On the other hand, Third†, By contrast†, Indeed†, Specifically, **Consequently**, Likewise†, **unlike**, Notably†, Conversely, Nevertheless.

### Evaluative and emphatic words (writing)

Words that judge or stress. Their rates show how restrained each writer is.

**new**, **significant**, **important**, **significantly**, **natural**, **useful**, **novel**, **difficult**, **robust**, **simple**, **key**, challenging, **efficient**, **naturally**, **highly**, **interesting**, **unique**, **clearly**†, **successfully**, **effective**, intuitive, **state-of-the-art**†, **successful**, crucial, **importance**, widely, **effectively**, essential, **extremely**, rich, seamless†, intuitively, seamlessly†, strongly, truly†, fundamental†, obvious†, substantial, substantially, surprising†, surprisingly†, **central**†, **first to**, **powerful**, promising, **valuable**†, compelling, critical, fundamentally†, greatly, critically†, dramatically, remarkably†.

### Problem, gap, and motivation (writing)

Words that set up a problem and what prior work leaves open.

**goal**, **problem**, **need**, **question**, assume, **difficulty**, **prior work**, **standard**, **typical**, rely on, **motivate**, **challenge**, **opportunity**†, **lack**, related work, **so far**, **aim**, **issue**, **motivation**†, gap, **traditional**†, conventional, few studies, open problem†, previous work, traditionally†.

### Scope, limits, and future work (writing)

Words that bound a claim and point to what comes next.

**direction**, **limit**, generalize, **in this work**, **limitation**, **remain**, **future work**, generalization†, **long-term**, **ultimately**, **future research**†, **foundation**, **extension**, step toward†, scope†, avenue†, first step, beyond the scope†, we hope†, envision†, open question†, outside the scope†, take-home message†.

### Human-robot interaction and social robotics (field)

Terms of human-robot interaction, social robots, and social cognition.

conversation†, moderation†, moderator†, **gaze**, intent†, family†, autism†, F-formation†, **HRI**, **attention**, **human-robot interaction**, group conversation†, SAR†, socially assistive robotics†, multi-party†, proxemics†, older adult†, **autonomous**†, group cohesion†, social interaction†, engagement, **humanoid**, **autonomy**†, child-robot interaction†, **teleoperation**, **gesture**, turn-taking†, social dynamics†, social robot†, embodied†, nonverbal†, spatial pattern†, situated†, **trust**, caregiver†, embodiment†, mental state†, Wizard-of-Oz†, intention, theory of mind†, eye contact†, rapport†.

### Robot learning and human input (field)

Terms for how robots learn, and for the input people give them.

**feature**, **representation**, reward, trajectory, demonstration, **preference**, human input, reward function, **correction**, reward learning, **comparison**, **expert**, **dataset**, **skill**, policy, **online**, **teaching**, state space†, embedding†, **feedback**, offline, **controller**, neural network†, non-expert, generalization†, active learning, learning from demonstration, motion planning†, reinforcement learning, **teacher**, novice, physical correction†, end user†, imitation learning, learner, human feedback, inverse reinforcement learning, planner†, subgoal, distribution shift†, task learning†, deep learning†, sample efficiency, action space†, MDP, shaping, Markov decision process†, supervised learning†, value function.

### Human models and inference (field)

Terms for modeling people and inferring what they want.

confidence, inference, **objective**, Boltzmann, **infer**, alignment, posterior†, belief†, **aligned**, representation alignment†, **likelihood**, latent, Bayesian, uncertainty†, explainability†, interpretable†, utility, preference learning, rationality, noisy-rational†, human model†, misspecified†, hypothesis space†, mental model†, misspecification†, transparency†.

### Multi-agent and behavior-based systems (field)

Terms from Matarić's field, behavior-based control of groups of robots.

**agent**, **communication**†, arbitration†, cooperation†, **distributed**, ensemble, multi-agent†, swarm†.

### Study design, measures, and statistics (field)

Terms for how the studies were run and analyzed.

**participant**, **condition**, **performance**, session, accuracy, **error**, **baseline**, simulation, questionnaire, **annotation**, **ground truth**, **metric**, correlation, user study, **pilot**, **video**, **survey**†, **trial**†, ANOVA†, **regression**, **annotate**, standard error†, deployment, **Likert**, **t-test**, standard deviation, effect size†, interview†, within-subjects†, ablation, real robot, subjects†, counterbalance†, p-value, benchmark, between-subjects†, in the wild, Mechanical Turk, objective measure†, success rate.

### Words all five use

Word families that every one of the five uses at least twice, leaving out the most common English words, most used first. Words marked † are not in the author's papers.

robot, behavior, feature, interaction, task, agent, object, algorithm, function, approach, condition, input, describe, chapter†, environment, experiment, orientation†, perform, motion, movement, complex, detect, map, estimate, domain, require, structure, distance, observe, interact, label, evaluate, distribution, generate, enable, analysis, physical, error, frame, direction, measure, apply, ability, location, shown, random, directly, strategy, demonstrate, multiple, explain, significant, sensor†, implement, develop, maintain, address, attempt, select, produce, positive, compute, scale, compare, suggest, probability, appropriate, consider, affect, represent, achieve, reach, avoid, choose, detail, direct, define, camera, rule†, combine, context, indicate, evaluation, detection†, implementation, collect, desire, observation, additional, challenge, limit, perception, update, combination, component, knowledge, correct, obtain, reduce, discuss, introduce, degree, robotics, feedback, improve, dynamics, influence, engage†, relative, relate, aspect, sequence, difficulty, experimental, comparison, pose, communication†, identify, relevant, vary, useful, necessary, active, scenario, involve, variety, receive, serve, analyze, predict, criterion†, angle†, technique, operate, output, initial, interpret, pair, computational†, shape, negative, easily, exist, factor, depend, accord, solve, contain, capability, explore, remain, framework, explicitly, contrast, randomly, execute, conduct, presence†, collection, prediction, coordinate†, researcher, typical, robust, begin, encourage, minute, perceive, chosen, procedure, similarly, maximum, appear, associate, adapt, description, extend, application, expressive†, instance, protocol, discussion, otherwise, monitor, summary†, limitation, occur, assign, autonomous†, maximize, express, constant, primary†, naturally, classify, linear, purpose†, insight, guide, intended, command†, concern, decide, category, engineer, manipulation, relation, motivate, perspective, external†, qualitative, treat, separate, whenever†, specifically, prevent, differ, converge, facilitate, contribution, literature, independent, contribute, automatically, throughout, lack, deviation, accomplish†, variation, particularly, outline†, characterize, dot, unique, author†, easier, impact, physically†, element, independently†, smaller, behave, mental, recruit, repeat, impossible†, variance, foundation, clearly†, analogous†, closely, sensitive.

### Field words new to the author

Words that at least two of Short, Vázquez, and Bobu use and that none of the author's papers uses, most used first. Use one only when a plain word for the same thing is missing, and keep established terms where they exist.

orientation, turn, track, sensor, detection, front, graph, autonomous, angle, speak, collaboration, engage, request, quickly, trend, team, rule, inspire, expressive, day, opportunity, sense, core, presence, primary, communication, old, decision, functional, latter, computational, coordinate, autonomy, continue, name, purpose, thought, versus, command, power, tell, something, independently, gray, criterion, whole, physically, author, unify, clearly, impossible, accomplish, alternate, connect, whenever, write, favorite, inherent, course, recall, analogous, white, social, game, children, sec, player, moderator, member, conversation, assistive, laptop, activity, adult, speech, speaker, induce, intervention, utterance, proxemics, collaborative, audio, child, trace, survey, socially, animation, multi-party, picture, family, mobile, communicate, appearance, establish, microphone, orient, character, min, reinforce, proxy.

## Part 3. Words to watch

### Common academic words

These words are frequent in academic prose and in text drafted by AI assistants. None is wrong, but the author's papers use only the first group. In text written for the author, choose a word from the first group or from Part 1 unless the author introduces the word.

**Used in the papers.** thus, leverage, moreover, utilize, furthermore, on the other hand, in contrast, consolidate, intricate, thereby, facilitate, streamline, noteworthy, trajectory-level, that said.

**Not used in the papers.** albeit, articulate, as such, bolster, by contrast, complement, comprehensive, corroborate, crucially, crux, culminate, delineate, delve, dichotomy, discern, elicit, elucidate, exemplify, facet, first-class, foreground, foster, granular, harness, hence, holistic, illuminate, in particular, in turn, instantiate, interplay, interrogate, intriguing, landscape, mediate, meticulous, multifaceted, myriad, necessitate, notably, nuanced, operationalize, overarching, paramount, pivotal, plethora, principled, realm, reconcile, robustly, salient, scaffold, seamless, situate, substantiate, synergy, taken together, to this end, underpin, underscore, unpack, well-suited, whereby, wherein.

### Words the author uses more than field writers

In the author's dissertation draft, these words appear at least twice as often per word as in any of the five field dissertations. Give them a second look in revision. A count alone is not a reason to change the author's wording.

indicate, give, consistent, collect, conduct, key, contribution, namely, repeat, consistency, bad, mitigate, actual, complementary, assess, advance, conclusion.

### Phrases replaced in review

Figurative or vague phrases that the author replaced with literal wording. See Literal wording in the style guide.

| Replaced | With |
| --- | --- |
| read together | together, these findings suggest |
| point in the same direction | are consistent with each other |
| link by link | were evaluated separately |
| by two routes, the two routes | in two ways, both approaches |
| supplied, supply | provided, provide |
| were lost at similar kinds of points | failed at similar kinds of steps |
| a sense in which | illustrates how |
| account for (a design choice) | help explain |
| shaped by, affected by (for an association) | associated with |
| fairly correlated, relatively high correlation | the correlation value, such as r = 0.25 |
| the difference vanishes, as good as | no difference was detected |
| structurally resilient against | illustrates how [mechanism] can discourage |
| completion rate | degree of completion |
| novel signal, less-explored | under-explored as a human teaching signal |
| the first work that | what the work does, or few studies have examined |

## Part 4. Acronyms

The expansion is the one the author's papers define, or else the one a field dissertation defines. Spell out the full form before the first use of the acronym.

**AIRL** Adversarial Inverse Reinforcement Learning · **AMT** Amazon Mechanical Turk · **ANOVA** analysis of variance · **ASD** Autism Spectrum Disorder · **BC** Behavioral Cloning · **BF** Bayes Factor · **CASA** Confidence-Aware Shared Autonomy · **CHARM** Considering Human Attributes for Reinforcement Modeling · **COACH** Convergent Actor-Critic by Humans · **DoF** degrees of freedom · **FERL** Feature Expansive Reward Learning · **GAE** generalized advantage estimation · **GAN** Generative Adversarial Network · **GUI** graphical user interface · **HIT** Human Intelligence Task · **HRI** human-robot interaction · **HSD** honestly significant difference · **IQR** interquartile range · **IRB** Institutional Review Board · **IRL** Inverse Reinforcement Learning · **LfD** Learning from Demonstration · **LfHF** Learning from Human Feedback · **LLM** Large Language Models · **LoRA** Low-Rank Adaptation · **MaxEnt** maximum entropy · **MDP** Markov decision process · **ME-IRL** Maximum Entropy Inverse Reinforcement Learning · **MH** Multi Human · **MLP** multilayer perceptron · **MSE** Mean Squared Error · **NASA TLX** NASA Task Load Index · **PH** Proficient Human · **PHIRL** Progress-Heuristicized Inverse Reinforcement Learning · **POMDP** partially observable Markov decision process · **PPO** Proximal Policy Optimization · **REML** restricted maximum likelihood · **RL** Reinforcement Learning · **RLHF** Reinforcement Learning from Human Feedback · **ROS** Robot Operating System · **RQ** research question · **SAR** socially assistive robotics · **SIRL** Similarity-based Implicit Representation Learning · **STEADY** Stabilizing TEacher Assessment DYnamics · **TAMER** Training an Agent Manually via Evaluative Reinforcement · **VAD** voice activity detection (Short), or Valence-Arousal-Dominance (Bobu) · **VAE** variational autoencoder · **VLM** Vision-Language Model
