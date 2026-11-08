"""Authored part of Hang's technical vocabulary: which terms are listed, and under which heading.

The counts, tiers, and examples are computed by build_vocabulary.py from the papers.
Edit this file and rebuild; never edit tech-vocabulary.md or word-list.md by hand.

Term syntax, one string per term:
    "display form"                 a noun phrase; the last word also matches its plural
    "display form | other | other" other spellings counted as the same term
    "... ~v"                       the last word also matches -s, -ed, -ing (a verb)
    "... ~x"                       exact forms only
    "... ~c"                       case-sensitive (automatic for words with two capitals)
A hyphen in a term also matches a space or nothing ("long-horizon" matches "long horizon").
A term the papers never use is still worth listing when it is a standard term of the field:
the build moves it to "Field terms the papers do not use", which is evidence too.
"""

CATEGORIES = [
    {
        'id': 'areas',
        'title': 'Research areas and learning paradigms',
        'about': 'Fields and families of methods that the papers place their work in.',
        'terms': [
            'robot learning', 'machine learning', 'interactive machine learning',
            'reinforcement learning', 'interactive reinforcement learning | interactive RL',
            'inverse reinforcement learning', 'learning from demonstration | learning from demonstrations',
            'learning from human demonstration | learning from human demonstrations',
            'learning from human feedback', 'reinforcement learning from human feedback',
            'imitation learning', 'behavioral cloning | behavior cloning', 'reward learning',
            'preference learning', 'active learning', 'human-in-the-loop', 'human-robot interaction',
            'online learning', 'offline', 'optimal control', 'learning from non-expert demonstrations',
            'learning from imperfect demonstrations',
            'reward shaping', 'policy shaping', 'skill acquisition', 'robot manipulation',
            'interactive learning', 'deep reinforcement learning', 'multi-task learning',
            'agentic robotics', 'agentic human-robot interaction | agentic HRI',
            # added from the reference dissertations
            'socially assistive robotics', 'shared autonomy', 'motion planning',
            'trajectory optimization', 'computer vision', 'natural language processing',
            'human-computer interaction', 'computer-supported collaborative work | computer supported collaborative work',
            'cognitive science', 'social psychology', 'meta-learning', 'supervised learning',
            'value alignment',
            # added from the recent lab dissertations
            'embodied AI', 'artificial intelligence', 'social robotics',
            'social navigation | social robot navigation',
        ],
    },
    {
        'id': 'signals',
        'title': 'Human teaching signals',
        'about': 'The kinds of human input the studies collect and compare.',
        'terms': [
            'human teaching', 'teaching signal', 'human teaching signal', 'human feedback',
            'feedback modality', 'feedback mechanism', 'evaluative feedback',
            'binary feedback', 'scalar feedback', 'binary evaluative feedback',
            'scalar evaluative feedback', 'human binary feedback', 'raw scalar feedback',
            'preference feedback', 'human preference', 'preference queries | preference query',
            'pairwise comparison', 'trajectory pair', 'ranking', 'critique', 'correction',
            'progress', 'progress annotation', 'progress label', 'progress value',
            'progress feedback', 'progress signal', 'task progress', 'online progress label',
            'VLM-generated progress', 'delta progress', 'end progress', 'start progress',
            'degree of task completion', 'degree of completion', 'task completion',
            'cumulative task completion', 'completion rate', 'completion percentage',
            'totally incomplete', 'fully complete | fully completed | complete fully ~x',
            'feedback value', 'feedback value scale', 'five-point scale', 'confidence degree',
            'verbal feedback', 'facial expressions | facial expression', 'eye gaze',
            'human knowledge', 'prior knowledge', 'human label', 'teaching style',
            'implicit feedback', 'numerical evaluation',
            # added from the recent lab dissertations
            'explicit feedback', 'user preference',
        ],
    },
    {
        'id': 'data',
        'title': 'Demonstrations, annotations, and datasets',
        'about': 'Words for the teaching data itself and its quality.',
        'terms': [
            'demonstration', 'human demonstration', 'expert demonstration',
            'non-expert demonstration', 'successful demonstration', 'failed demonstration',
            'unsuccessful demonstration', 'sub-optimal demonstration', 'imperfect demonstration',
            'noisy demonstration', 'high-quality demonstration', 'low-quality demonstration',
            'optimal demonstration', 'perfect demonstration', 'partial demonstration',
            'error-free demonstration', 'oracle demonstration', 'machine-generated demonstration',
            'oracle', 'demonstration quality', 'demonstration dataset', 'demonstration horizon',
            'mixed-quality dataset', 'high-quality dataset', 'dataset', 'training data',
            'annotation', 'annotate ~v', 'annotated demonstration', 'annotated subset',
            'human annotation', 'annotation percentage', 'annotation coverage',
            'auto-generated annotation', 'label ~v', 'data collection', 'data quality',
            'data annotator', 'ground truth', 'subset of demonstrations', 'keyframe',
            # added from the recent lab dissertations
            'synthetic data', 'data generation | dataset generation', 'training set',
            'validation set', 'test set',
        ],
    },
    {
        'id': 'rl',
        'title': 'Reinforcement learning and reward learning',
        'about': 'The formal quantities of the learning problem, as the PHIRL and STEADY papers use them.',
        'terms': [
            'agent', 'learning agent', 'pre-trained agent', 'trained agent',
            'policy', 'optimal policy', 'learned policy', 'expert policy', 'initial policy',
            'robot policy', 'multi-policy', 'policy roll-out | rollout | roll-out', 'state',
            'current state', 'previous state', 'goal state', 'end state', 'state-action pair',
            'state space', 'observation', 'visual observation', 'action', 'action sequence',
            'transition', 'transition dynamics', 'deterministic dynamics', 'timestep',
            'trajectory', 'sub-trajectory', 'trajectory segment', 'sampled trajectory',
            'generated trajectory', 'expert trajectory', 'partial trajectory', 'reward',
            'reward function', 'learned reward', 'learned reward function',
            'robust reward function', 'reward model', 'reward signal', 'dense reward',
            'sparse reward', 'environmental reward', 'environmental return', 'return',
            'cumulative reward', 'total reward', 'positive reward', 'negative reward',
            'imbalanced reward', 'reward distribution', 'inferred reward function',
            'latent reward function', 'potential function', 'heuristic function',
            'progress function', 'advantage', 'Q-value', 'Q-learning', 'discount factor',
            'horizon', 'task horizon', 'finite horizon', 'infinite horizon', 'exploration',
            'random exploration', 'exploration cost', 'exploit ~v', 'reward hacking',
            'reward hacking scenario', 'non-progressive behavior', 'punish ~v', 'alignment',
            'shaping component', 'potential shaping', 'completion shaping', 'temporal delta',
            'magnitude', 'path-independent', 'state-only', 'discriminator', 'generator',
            'trajectory generator', 'adversarial learner', 'reward learner', 'loss',
            'shaping loss', 'training objective', 'maximum likelihood', 'optimization',
            'optimization problem', 'optimize ~v', 'local optimum', 'convergence', 'domain',
            'environment', 'episode', 'reset ~v', 'training loop', 'learning loop',
            'reward design', 'reward features', 'hinge',
            # added from the reference dissertations
            'Markov decision process', 'partially observable Markov decision process',
            'value function', 'action-value function', 'Q-function', 'SARSA | Sarsa | sarsa ~c',
            'model-based', 'model-free', 'true reward', 'reward parameters',
            'generalizable reward', 'cost function', 'objective function', 'loss function',
            'tile coding', 'sample complexity', 'gradient descent', 'cross-entropy loss',
            # added from the recent lab dissertations
            'action space', 'policy learning',
        ],
    },
    {
        'id': 'methods',
        'title': 'Methods, models, and tools',
        'about': 'Named algorithms, baselines, model families, and software.',
        'terms': [
            'Adversarial Inverse Reinforcement Learning', 'MaxEnt IRL ~c',
            'generative adversarial network | generative adversarial networks',
            'proximal policy optimization', 'TAMER ~c', 'COACH ~c', 'DemoPref ~c',
            'AIRLPref ~c', 'Pref ~c', 'Rank2Reward ~c', 'ReWiND ~c', 'DreamerV3 ~c',
            'diffusion policy', 'BC-RNN ~c', 'neural network', 'multilayer perceptron',
            'vision-language model', 'large language model', 'language model', 'Gemma',
            'LoRA ~c', 'fine-tune ~v', 'pre-train ~v', 'post-training', 'prompt',
            'language instruction', 'base model', 'hyperparameter', 'hyperparameter search',
            'learning rate', 'batch size', 'hidden units', 'random seed', 'seed', 'checkpoint',
            'parallel environment', 'mean squared error', 'Robosuite', 'Robomimic',
            'RoboTurk ~c', 'DeepMind Control Suite', 'MuJoCo ~c', 'Hugging Face', 'algorithm',
            'framework', 'learning framework', 'baseline method', 'heuristic',
            # added from the reference dissertations
            'maximum entropy IRL | ME-IRL ~c', 'TrajOpt ~c',
            'Robot Operating System', 'PyBullet | pybullet', 'particle filter', 'Kalman filter',
            'rule-based', 'data-driven',
            # added from the recent lab dissertations
            'foundation model', 'zero-shot', 'transformer', 'encoder', 'decoder',
            'recurrent neural network', 'graph neural network', 'message passing',
            'random forest', 'behavior tree', 'receding horizon planning | receding horizon',
            'inverse kinematics', 'operational space control', 'knowledge base',
        ],
    },
    {
        'id': 'own',
        'title': 'Names and concepts from the studies',
        'about': 'Method names and concepts that the papers introduce or define.',
        'terms': [
            'PHIRL ~c', 'Progress-Heuristicized Inverse Reinforcement Learning | Progress Heuristicized Inverse Reinforcement Learning',
            'PHIRL-online ~c', 'CHARM ~c',
            'Considering Human Attributes for Reinforcement Modeling', 'STEADY ~c',
            'demonstration sidetracks | demonstration sidetrack',
            'one-dimension control', 'control pattern', 'patterned imperfection',
            'Lift-Drop-Loop | Lift-Drop loop ~c', 'Touch-And-Stay ~c', 'poking behavior',
            'feedback delay', 'feedback pattern', 'human feedback pattern', 'feedback dynamics',
            'noticing window', 'state window', 'human characteristics', 'human attributes',
            'unaware scenario', 'corrected scenario', 'failure scenario',
        ],
    },
    {
        'id': 'people',
        'title': 'Human teachers and their behavior',
        'about': 'Who teaches the robot, what describes them, and how their teaching departs from an ideal.',
        'terms': [
            'human teacher', 'non-expert', 'non-expert user', 'non-expert participant',
            'non-expert demonstrator', 'expert', 'robot expert', 'human expert', 'demonstrator',
            'annotator', 'operator', 'proficient operator', 'crowdworker | crowd worker',
            'crowd-sourced', 'passersby', 'everyday users', 'end user', 'human characteristic',
            'human factor', 'robot experience', 'educational background',
            'teaching experience', 'personality', 'computer science background',
            'demographics', 'expertise', 'proficiency', 'human participation', 'imperfection',
            'human imperfection', 'sub-optimality', 'non-optimal behavior', 'noise',
            'random noise', 'random error', 'inconsistency', 'bias', 'mistake',
            'exploratory action', 'unproductive behavior', 'harmless behavior', 'workload',
            'cognitive load', 'mental effort', 'human effort', 'human engagement',
            'teaching effort', 'human intention', 'human expectations', 'task phase',
            'phase change', 'sub-goal', 'sub-task',
            # added from the reference dissertations
            'novice user | novice users | novice', 'system designer', 'caregiver', 'bystander',
            'human burden', 'human guidance', 'human supervision',
            # added from the recent lab dissertations
            'human behavior', 'human partner', 'human collaborator',
        ],
    },
    {
        'id': 'social',
        'title': 'Social and group interaction',
        'about': ('Terms of social and group human-robot interaction. Most come from the Short and Vázquez '
                  'dissertations, so most are Reference only.'),
        'terms': [
            'socially assistive robot', 'social robot', 'humanoid robot', 'social interaction',
            'social dynamics', 'social behavior', 'social presence', 'social cue | engagement cue',
            'social convention', 'multi-party interaction', 'multi-party human-robot interaction',
            'group interaction', 'group dynamics', 'group cohesion', 'group conversation',
            'conversational group', 'F-formation | f-formation', 'o-space', 'proxemics',
            'proxemic behavior', 'personal space', 'spatial behavior', 'spatial arrangement',
            'spatial formation', 'body orientation', 'lower-body orientation', 'head orientation',
            'head pose', 'gaze behavior', 'mutual gaze', 'shared attention', 'focus of attention',
            'turn-taking', 'addressee', 'utterance', 'voice activity detection',
            'nonverbal behavior', 'engagement', 'user engagement', 'moderation', 'moderator',
            'child-robot interaction', 'children with autism', 'autism spectrum disorder',
            'older adults', 'intergenerational | inter-generational', 'family group',
            'human-human interaction', 'dyadic interaction', 'embodiment', 'embodied agent',
            'behavioral agency', 'morphological agency', 'collaborative game', 'brainstorming',
            'personalization', 'personalized', 'emotion', 'expressive motion',
            'companion',
            # added from the recent lab dissertations
            'social context', 'social situation', 'social environment', 'social norm',
            'mental state', 'theory of mind', 'group member', 'group membership',
            'group detection', 'robot behavior', 'nonverbal cue', 'gesture', 'speech',
            'affective state', 'affect recognition', 'synchrony | social synchrony',
            'joint attention', 'visual attention', 'empathy', 'social support', 'support group',
            'facilitator', 'trust', 'competence', 'warmth', 'discomfort',
            'anthropomorphism | anthropomorphic',
            'perceptions of robots | perception of robots | perceptions of the robot',
            'robot failure', 'apology', 'collaborative task', 'robot partner', 'interruption',
            'assistance', 'assistive robot', 'robot embodiment', 'form factor', 'haptic',
            'pedestrian',
        ],
    },
    {
        'id': 'domains',
        'title': 'Application areas and populations',
        'about': ('Where human-robot interaction is applied and whom it serves. These come from the recent lab '
                  'dissertations, mainly Matheus, Klein, and Birmingham, so all are Reference only.'),
        'terms': [
            'mental health', 'well-being | wellbeing', 'anxiety', 'therapy | therapeutic',
            'intervention', 'healthcare | health care', 'dementia', 'infant', 'adolescent',
        ],
    },
    {
        'id': 'representations',
        'title': 'Representations, human models, and inference',
        'about': ('Terms for what a robot represents and how it interprets human input. Most come from the '
                  'Bobu dissertation, so most are Reference only.'),
        'terms': [
            'representation learning', 'representation alignment', 'robot representation',
            'human representation', 'misalignment', 'misaligned', 'feature', 'feature learning',
            'feature trace', 'feature space', 'feature function', 'feature vector', 'learned feature',
            'feature query', 'similarity query', 'label query', 'demonstration query', 'human input',
            'human model | model of human | models of human', 'human decision model',
            'Boltzmann rationality | Boltzmann model | Boltzmann-rational', 'noisily-rational | noisily rational',
            'situational confidence', 'confidence estimation', 'intent', 'goal inference',
            'policy blending', 'arbitration', 'misspecification | misspecified',
            'spurious correlation', 'causal confusion', 'privileged information', 'latent space',
            'latent representation', 'embedding', 'self-supervised', 'interpretable',
            'high-dimensional', 'low-dimensional', 'Bayesian inference', 'belief', 'posterior',
            'likelihood', 'log-likelihood', 'Laplace approximation', 'probability distribution',
            'uniform distribution', 'distribution shift', 'data augmentation', 'point cloud',
            'perception',
            # added from the recent lab dissertations
            'uncertainty', 'contextual information', 'out-of-distribution', 'information gain',
            'transparency', 'explainability | explainable',
        ],
    },
    {
        'id': 'robots',
        'title': 'Robots, tasks, and environments',
        'about': 'Hardware, interfaces, and the tasks used in the studies.',
        'terms': [
            'robot arm', 'robotic arm', 'Kinova Gen3 Lite | Kinova Gen 3 Lite | Kinova Gen lite', 'Kinova',
            'gripper', 'end effector | end-effector', 'Xbox controller', 'joystick',
            'degrees of freedom', 'teleoperation | teleoperate | teleoperated', 'kinematic',
            'control interface', 'graphical user interface', 'interface', 'button',
            'overhead camera', 'RealSense ~c', 'manipulation', 'manipulation task',
            'robot manipulation task', 'long-horizon task', 'long-horizon', 'pick and place',
            'grasp ~v', 'pour ~v', 'navigate ~v', 'brush ~v', 'PickPlaceCan ~c', 'Lift ~c',
            'Square ~c', 'nut assembly', 'square-shaped nut', 'peg', 'ice cream topping-adding task',
            'topping jar', 'coffee preparation task', 'stirrer', 'button-pressing task',
            'stuffed animal', 'pom-pom', 'target object', 'goal location', 'block', 'bin',
            'shelf', 'simulation', 'simulated robot', 'real robot', 'sim-to-real gap',
            'real-world', 'robot-in-the-wild', 'deployment', 'Proficient Human ~c',
            'Multi Human ~c',
            # added from the reference dissertations
            'mobile robot', 'mobile base', 'manipulator', 'JACO | Jaco ~c', 'sensor',
            'microphone array', 'Kinect', 'RGB-D', 'localization', 'tracking', 'field of view',
            'kinesthetic teaching | kinesthetic', 'gravity compensation', 'autonomous robot',
            'autonomy', 'semi-autonomous', 'navigation', 'tabletop',
            # added from the recent lab dissertations
            'humanoid', 'locomotion', 'contact-rich', 'physical robot', 'robot platform',
            'hardware', 'actuator', 'open-source', 'collision', 'household task | household tasks',
        ],
    },
    {
        'id': 'simulation',
        'title': 'Simulation, vision, and generative models',
        'about': ('Terms of simulation for robot learning, computer vision, and visual generation. They come from the '
                  'recent lab dissertations of Gokmen, Wong, Shi, and Sargent, so most are Reference only.'),
        'terms': [
            'simulator', 'simulation environment', 'physics simulation | physics simulator',
            'digital twin', 'domain randomization', 'sim-to-real | sim2real', 'benchmark', 'scene',
            'scene generation', 'asset', 'articulated object', 'everyday activities | everyday tasks',
            'rendering', 'photorealistic', '3D reconstruction', 'novel view synthesis', 'NeRF ~c',
            'object detection', 'segmentation', 'bounding box', 'depth estimation',
            'generative model', 'diffusion model', 'autoencoder', 'tokenizer', 'compression',
        ],
    },
    {
        'id': 'studies',
        'title': 'Study design and data collection',
        'about': 'How the user studies were set up, run, and coded.',
        'terms': [
            'user study', 'public space study', 'public space', 'university atrium',
            'online study', 'in-person study', 'in-lab', 'non-lab', 'real robot study',
            'validation study', 'ablation study', 'pilot study', 'participant', 'recruit ~v',
            'experimenter', 'Amazon Mechanical Turk', 'Institutional Review Board',
            'consent form', 'questionnaire', 'characteristic questionnaire', 'NASA TLX',
            'study setup', 'experimental setup | experiment setup', 'study procedure | experiment procedure',
            'condition', 'scenario', 'representative scenario', 'video clip', 'replay',
            'open-coded book', 'open coding', 'codebook', 'cross-validate ~v', 'exclude ~v',
            'research question', 'hypothesis | hypotheses', 'session', 'practice session',
            'between-subjects', 'within-subjects', 'counterbalance ~v', 'Likert',
            'demonstration interface', 'annotation interface',
            # added from the reference dissertations
            'Wizard-of-Oz | Wizard of Oz', 'field study | field trial', 'case study',
            'informed consent', 'survey', 'subscale', 'coder', 'data coding',
            'manipulated variable', 'dependent measure', 'experimental design',
            'factorial design', 'repeated-measures | repeated measures', 'sample size',
            'pilot session', 'interview',
            # added from the recent lab dissertations
            'online survey', 'Prolific ~c', 'Qualtrics ~c', 'manipulation check',
            'attention check', 'open-ended', 'self-report | self-reported',
            'semi-structured interview', 'inter-rater reliability | interrater reliability',
            'independent variable', 'dependent variable', 'study design',
            'longitudinal study', 'in-the-wild | in the wild',
            'in-home study', 'Godspeed ~c', 'System Usability Scale',
        ],
    },
    {
        'id': 'measures',
        'title': 'Measures, statistics, and evaluation',
        'about': 'How results are measured, compared, and tested.',
        'terms': [
            'baseline', 'performance', 'success rate', 'task success', 'average return',
            'learning curve', 'reward curve', 'learning outcome', 'converged performance',
            'ceiling performance', 'improvement', 'data efficiency', 'sample efficiency',
            'learning efficiency', 'robustness', 'ablation', 'sensitivity analysis', 'error bar',
            'standard deviation', 'confidence interval', 'shaded area', 'mean', 'median',
            'interquartile range', 'distribution', 'normal distribution', 'correlation',
            'Pearson correlation', 'Spearman', 'correlate ~v', 'Wilcoxon rank-sum test',
            'Kruskal-Wallis H test', 't-test', 'Shapiro-Wilk test', 'Holm-Sidak', 'Box-Cox',
            'Bayes factor', 'Bayesian statistics', 'statistically significant',
            'significant difference', 'significance', 'p-value', 'effect size', 'threshold',
            'absolute difference', 'normalized', 'self-consistency', 'agreement',
            'feedback accuracy', 'accuracy', 'prediction', 'completion time', 'task statistics',
            'variance', 'regression', 'outlier', 'evaluation rollouts', 'x-axis', 'y-axis',
            'feedback distribution', 'spatial distribution',
            # added from the reference dissertations
            'ANOVA ~c', 'Tukey HSD | Tukey\'s HSD | Tukey', 'post hoc | post-hoc', 'main effect',
            'interaction effect', 'random effect', 'mixed-effects | mixed effects | linear mixed model',
            'REML ~c', 'Cronbach\'s alpha | Cronbach | Cronbach alpha', 'Cohen\'s kappa | kappa',
            'standard error', 'paired t-test', 'multiple comparisons', 'classification accuracy',
            'qualitative analysis | qualitative results', 'quantitative analysis', 'objective metric',
            'response time', 'chi-square | chi-squared',
            # added from the recent lab dissertations
            'F1 score | F1-score', 'precision', 'recall', 'confusion matrix',
            'cross-validation | cross validation', 'leave-one-out', 'linear regression',
            'mean absolute error', 'Cohen\'s d', 'Bonferroni',
            'Wilcoxon signed-rank test | Wilcoxon signed-rank', 'evaluation metric',
        ],
    },
    {
        'id': 'writing',
        'title': 'Research-writing words',
        'about': ('General academic verbs, adjectives, and nouns that the papers use to describe the work. '
                  'They carry most of the prose, so their tiers show which ones Hang reaches for.'),
        'groups': [
            ('Verbs for research actions', [
                'investigate ~v', 'examine ~v', 'explore ~v', 'characterize ~v', 'identify ~v',
                'define ~v', 'describe ~v', 'formalize ~v', 'propose ~v', 'introduce ~v',
                'present ~v', 'design ~v', 'develop ~v', 'conduct ~v', 'collect ~v',
                'analyze ~v', 'evaluate ~v', 'assess ~v', 'validate ~v', 'test ~v', 'compare ~v',
                'measure ~v', 'calculate ~v', 'compute ~v', 'estimate ~v', 'predict ~v',
                'infer ~v', 'model ~v', 'train ~v', 'sample ~v', 'select ~v', 'filter ~v',
                'assign ~v', 'extract ~v', 'generate ~v', 'imitate ~v', 'normalize ~v',
                'align ~v', 'shape ~v', 'leverage ~v', 'utilize ~v', 'integrate ~v',
                'combine ~v', 'incorporate ~v', 'adapt ~v', 'extend ~v', 'generalize ~v',
                'deploy ~v', 'visualize ~v', 'interpret ~v', 'quantify ~v', 'hypothesize ~v',
                'assume ~v', 'illustrate ~v', 'instantiate ~v', 'operationalize ~v',
                'disambiguate ~v', 'perceive ~v', 'convey ~v', 'anticipate ~v',
                # added from the recent lab dissertations
                'simulate ~v', 'encode ~v', 'aggregate ~v', 'categorize ~v', 'replicate ~v',
                'verify ~v',
            ]),
            ('Verbs for effects and findings', [
                'mitigate ~v', 'address ~v', 'overcome | overcomes | overcame | overcoming ~x',
                'reduce ~v', 'minimize ~v', 'maximize ~v', 'improve ~v', 'enhance ~v',
                'stabilize ~v', 'outperform ~v', 'achieve ~v', 'demonstrate ~v', 'indicate ~v',
                'suggest ~v', 'reveal ~v', 'highlight ~v', 'observe ~v', 'detect ~v',
                'distinguish ~v', 'capture ~v', 'reflect ~v', 'represent ~v', 'correspond ~v',
                'associate ~v', 'contribute ~v', 'affect ~v', 'vary ~v', 'differ ~v',
                'deviate ~v', 'exhibit ~v', 'require ~v', 'rely ~v', 'enable ~v', 'ensure ~v',
                'bridge ~v', 'encompass ~v', 'discourage ~v', 'prioritize ~v',
            ]),
            ('Adjectives and adverbs', [
                'robust', 'consistent', 'inconsistent', 'informative', 'accurate', 'reliable',
                'unreliable', 'noisy', 'sparse', 'dense', 'efficient', 'effective',
                'data-efficient', 'complementary', 'systematic', 'structured', 'patterned',
                'random', 'diverse', 'imperfect', 'optimal', 'sub-optimal', 'non-optimal',
                'high-quality', 'low-quality', 'interactive', 'evaluative', 'numerical', 'scalar',
                'binary', 'cumulative', 'accumulative', 'incremental', 'temporal', 'spatial',
                'significant', 'representative', 'meaningful', 'crucial', 'critical', 'novel',
                'promising', 'realistic', 'independent', 'expressive',
                'under-explored | underexplored', 'little-used', 'significantly', 'statistically',
                'substantially', 'randomly', 'repeatedly', 'automatically', 'explicitly',
                'implicitly', 'iteratively', 'alternately', 'jointly', 'empirically',
                'intuitively', 'inherently', 'monotonic', 'salient', 'tractable', 'intractable',
                'generalizable', 'qualitatively', 'quantitatively',
                # added from the recent lab dissertations
                'unseen', 'downstream', 'predictive', 'contextual', 'modular', 'empirical',
                'preliminary', 'iterative', 'inherent', 'plausible', 'causal', 'computational',
            ]),
            ('Nouns for research ideas', [
                'insight', 'intuition', 'assumption', 'limitation', 'contribution', 'finding',
                'implication', 'challenge', 'gap', 'bottleneck', 'approach', 'method',
                'methodology', 'mechanism', 'component', 'property', 'dimension', 'aspect',
                'factor', 'characteristic', 'pattern', 'variation', 'representation',
                'trade-off', 'portion', 'applicability', 'capability', 'usability', 'consistency',
                'efficiency', 'expressiveness', 'informativeness', 'generalization',
                'scalability', 'paradigm', 'notion', 'desiderata | desideratum', 'formalism',
                'formalization',
                # added from the recent lab dissertations
                'feasibility', 'variability', 'abstraction', 'fidelity',
            ]),
        ],
    },
]

# Short notes shown with a term. Keep them to facts stated in the papers.
NOTES = {
    'demonstration sidetracks': 'Four types, Exploration, Mistake, Alignment, and Pause, plus one control pattern, one-dimension control.',
    'progress': 'Counts every use of the word, including its everyday sense.',
    'alignment': 'Includes the Alignment type of demonstration sidetrack.',
    'Lift': 'Robosuite task name; capitalized uses only.',
    'Square': 'Robosuite task name; capitalized uses only.',
    'Proficient Human': 'Robomimic dataset type (PH).',
    'Multi Human': 'Robomimic dataset type (MH).',
    'open-coded book': 'The papers\' wording; the dissertation writes a codebook developed through open coding.',
    'recall': ('Counts every use of the word, including its everyday sense (recall that) and remembering. '
               'The example shows the metric sense.'),
    'precision': ('Counts every use of the word. The papers use it for numerical and spatial precision, not the '
                  'classification metric, so the tier does not show familiarity with the metric.'),
    'encoder': ('Counts every use of the word, including position encoders on robot hardware (Shi). '
                'The example shows the neural-network sense.'),
    'transparency': ('Counts every use of the word, including the optical transparency of rendered objects '
                     '(Gokmen, Wong).'),
    'sim-to-real': 'Also counts sim-to-real gap, which the papers use.',
}

# Words with more than one sense. The example comes from a sentence that matches the pattern, so it
# shows the sense the group means; the counts still include every sense, as the note says.
EXAMPLE_SENSE = {
    'encoder': r'\bdecoders?\b|\bneural\b|\blatent\b|\btransformer|\bimages?\b|\btokens?\b',
    'recall': r'\bprecision\b|\bF1\b|true positives?|false negatives?',
}

# Terms that the writing style reference sets as the dissertation's wording.
# term -> (title of the style reference entry, its anchor). A term the papers never use gets the
# tier "Dissertation term" instead of "Not found".
DISSERTATION_TERMS = {
    'degree of completion': ('Established dissertation terminology', 'established-dissertation-terminology'),
    'degree of task completion': ('Established dissertation terminology', 'established-dissertation-terminology'),
    'binary evaluative feedback': ('Teaching signals and learning quantities', 'teaching-signals-and-learning-quantities'),
    'scalar evaluative feedback': ('Teaching signals and learning quantities', 'teaching-signals-and-learning-quantities'),
    'codebook': ('Established dissertation terminology', 'established-dissertation-terminology'),
    'formalize': ('Research actions', 'research-actions'),
    'discourage': ('Established dissertation terminology', 'established-dissertation-terminology'),
    'illustrate': ('Established dissertation terminology', 'established-dissertation-terminology'),
    'prioritize': ('Word choices made in review', 'word-choices-made-in-review'),
    'portion': ('Word choices made in review', 'word-choices-made-in-review'),
    'under-explored': ('Established dissertation terminology', 'established-dissertation-terminology'),
    'agentic robotics': ('Established dissertation terminology', 'established-dissertation-terminology'),
    'agentic human-robot interaction': ('Established dissertation terminology', 'established-dissertation-terminology'),
}

# Words the checker treats as known although the papers do not use them, because they name
# the document itself rather than its content.
ALSO_KNOWN = ['dissertation', 'dissertations', 'chapter', 'chapters']

# For a field term the papers do not use, the nearest term that they do use.
NEAREST = {
    'multi-task learning': 'multi-task extension (PHIRL drafts)',
    'MuJoCo': 'Robosuite',
    'demographics': 'human characteristics',
    'practice session': 'practice, as in minutes to practice',
    'between-subjects': 'condition, groups of participants',
    'within-subjects': 'condition',
    'counterbalance': 'randomly',
    'Likert': 'five-point scale',
    'demonstration interface': 'control interface',
    'annotation interface': 'graphical user interface',
    'median': 'mean',
    'interquartile range': 'IQR, used once as an acronym',
    'effect size': 'Bayes factor, significant difference',
    'deploy': 'deployment',
    'expressive': 'expressiveness',
    'usability': 'applicability',
    'informativeness': 'informative',
    'user preference': 'human preference',
    'simulator': 'simulation, Robosuite',
    'simulation environment': 'simulation, environment',
    'benchmark': 'Robosuite, Robomimic',
    'online survey': 'online study, questionnaire',
    'study design': 'study setup, study procedure',
    'cross-validation': 'cross-validate',
    'evaluation metric': 'performance, success rate',
}

# For a field term the papers do not use, a related term that they do use but that means something else.
# The checker shows these as related, not equivalent, so that a draft keeps the field term when
# changing it would change the study, the metric, or the role.
RELATED = {
    'F1 score': 'accuracy, a different metric',
    'action space': 'action, action sequence; an action space is the set of available actions',
    'independent variable': 'condition, a level or combination of levels of the variables',
    'explicit feedback': 'evaluative feedback, a narrower kind of signal',
    'human partner': 'human teacher, one role a partner can have',
    'human behavior': 'human characteristics, teaching style; both are narrower',
}

# Acronyms: (acronym, expansion as the papers write it, or None to take the expansion the papers define).
ACRONYMS = [
    ('LfD', None), ('LfHF', None), ('RL', None), ('IRL', None), ('RLHF', None),
    ('AIRL', None), ('BC', None), ('VLM', None), ('LLM', None), ('PHIRL', None),
    ('CHARM', 'Considering Human Attributes for Reinforcement Modeling'),
    ('STEADY', 'Stabilizing TEacher Assessment DYnamics'),
    ('HRI', 'human-robot interaction'), ('GUI', None), ('MSE', None),
    ('IRB', None), ('AMT', None), ('HIT', 'Human Intelligence Task'), ('MLP', 'multilayer perceptron'),
    ('BF', None), ('PPO', 'Proximal Policy Optimization'), ('GAN', 'Generative Adversarial Network'),
    ('MDP', 'Markov decision process'), ('DoF', 'degrees of freedom'),
    ('IQR', 'interquartile range'), ('NASA TLX', 'NASA Task Load Index'),
    ('PH', 'Proficient Human'), ('MH', 'Multi Human'),
    ('TAMER', 'Training an Agent Manually via Evaluative Reinforcement'),
    ('COACH', 'Convergent Actor-Critic by Humans'),
    ('LoRA', 'Low-Rank Adaptation'), ('GAE', 'generalized advantage estimation'),
    ('RQ', 'research question'), ('MaxEnt', 'maximum entropy'),
    # defined in the reference dissertations
    ('SAR', None), ('ASD', None), ('POMDP', 'partially observable Markov decision process'),
    ('VAE', 'variational autoencoder'), ('ROS', 'Robot Operating System'), ('ANOVA', 'analysis of variance'),
    ('HSD', 'honestly significant difference'), ('REML', 'restricted maximum likelihood'),
    ('ME-IRL', None), ('FERL', None), ('SIRL', None), ('CASA', None), ('VAD', None),
    # defined in the recent lab dissertations
    ('AI', None), ('ML', None), ('GPU', None), ('API', None), ('CNN', None), ('LSTM', None),
    ('GNN', None), ('IMU', None), ('HCI', None), ('HRC', None), ('SVM', None), ('SUS', None),
    ('SLAM', None), ('IK', None), ('KL', None), ('VR', None), ('GRU', None), ('DPO', None),
    ('VLA', None), ('NeRF', 'neural radiance field'), ('SAC', None), ('CLIP', None),
]

# Technical terms that appear in the titles of works the papers cite but not in the papers' own text.
# They show what Hang has read, which is weaker evidence than using a word.
CITED_ONLY = [
    'suboptimal demonstrations', 'affective feedback', 'human-robot collaboration',
    'dynamical systems', 'movement primitives', 'function approximation',
    'implicit human feedback', 'policy-dependent human feedback', 'off-policy',
    'double Q-learning', 'high-dimensional state spaces', 'self-supervised', 'variational',
    'contrastive', 'stochastic', 'probabilistic', 'keyframe-based', 'egocentric',
    'bimanual', 'visuomotor', 'generalist', 'tactile', 'physical human corrections',
    'feedback modalities', 'multimodal', 'EEG ~c', 'physiological',
    'self-efficacy', 'deception', 'intrinsic motivation', 'planning', 'autonomous',
    'adaptation', 'scalable', 'nonlinear', 'heterogeneous', 'transferable',
    'extrapolation', 'nonparametric', 'socially interactive agents',
    'maximum entropy', 'reward model ensemble', 'world model',
]

# Academic words that are common in generated prose. The build reports which of them the papers
# use. Those the papers never use are listed as words to avoid unless Hang introduces them.
PROSE_WORDS_TO_CHECK = [
    'elucidate', 'delve', 'underscore', 'nuanced', 'salient', 'holistic', 'interplay',
    'facet', 'landscape', 'pivotal', 'intricate', 'foster', 'notably', 'crucially',
    'moreover', 'furthermore', 'thereby', 'wherein', 'whereby', 'albeit', 'hence', 'thus',
    'granular', 'seamless', 'comprehensive', 'multifaceted', 'overarching', 'synergy',
    'culminate', 'realm', 'streamline', 'bolster', 'harness', 'myriad', 'plethora',
    'noteworthy', 'meticulous', 'intriguing', 'dichotomy', 'crux', 'paramount', 'robustly',
    'leverage', 'utilize', 'facilitate', 'underpin', 'substantiate', 'operationalize',
    'instantiate', 'situate', 'foreground', 'interrogate', 'unpack', 'articulate',
    'complement', 'consolidate', 'corroborate', 'delineate', 'discern', 'elicit',
    'exemplify', 'illuminate', 'mediate', 'necessitate', 'reconcile', 'scaffold',
    'trajectory-level', 'well-suited', 'first-class', 'principled', 'in turn', 'that said',
    'taken together', 'in particular', 'to this end', 'in contrast', 'by contrast',
    'on the other hand', 'as such',
]
