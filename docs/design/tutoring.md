# 辅导：教学原则与学习方法

本文说明 Cairn 中辅导部分的设计：辅导的目标，教学原则及其依据，指引的写法，学习类型的划分和学习方法的定位，实践型学习的学习方法。交给模型的指引正文属于技能，见[技能](../components/skill.md)。各部分的确认状态见[议题与决策](../decisions.md)。

## 辅导的目标

辅导服务于学习者的目标：学什么、学到什么深度，由学习者决定。对目标之内的内容，衡量的标准是长期掌握：学习者在脱离辅助的条件下，能够准确解释所学内容，把它应用于新的问题，并在此基础上继续学习。讲解的深度、提问与练习的安排、何时直接给出结论，均以对学习者的目标和长期掌握的贡献来权衡。

区分这两者的原因是，学习者不需要掌握学习中遇到的全部内容：有些内容需要掌握，有些只需要能够使用或有所了解。哪些内容属于前者，取决于学习者的目标；对这部分内容，标准不是当次对话中的表现，而是长期的保持和迁移。

模型在辅导中的角色是学习者的长期导师。“长期”有两层含义：衡量的标准是长期的保持和迁移，而不是当次对话中的表现；辅导跨越多次对话，由记忆衔接，模型对学习者的了解来自记忆，一次辅导形成的判断也通过记忆交给之后的对话。

## 教学原则

教学原则说明有效学习的条件，适用于所有学习类型，写在指引中，具体做法由模型依据学习者的情况判断。基础版共七条。下表给出每条原则的要点和主要依据，面向模型的完整表述见[技能](../components/skill.md)中的指引正文。

| 原则 | 要点 | 主要依据 |
|---|---|---|
| 1. 学习来源于学习者自身的认知加工 | 检索、解释、推理、应用和纠错等加工活动使知识得以建立和巩固；讲解、示例和反馈的作用在于引发并支持这些活动。支持的形式和程度随学习者的知识状态与任务难度调整 | 建构性和交互性的学习活动效果优于被动接受（Chi & Wylie, 2014）。提取练习促进长期保持（Roediger & Karpicke, 2006）。辅助的多少需要权衡（Koedinger & Aleven, 2007）。适合初学者的指导方式，对已有基础的学习者效果下降（Kalyuga et al., 2003）。不加限制地用生成式 AI 获取答案，会提高练习成绩而降低其后独立完成时的成绩；带有引导约束的辅导可以减轻这一影响（Bastani et al., 2025） |
| 2. 掌握的判断以多种表现为依据 | 讲解之后即时完成或在提示下完成的正确表现，主要反映内容在当时的提取强度，对长期保持和迁移的预测力有限。掌握的证据来自不同时间、不同情境和不同任务形式下的独立表现 | 训练过程中的表现不能可靠地反映长期保持与迁移（Soderstrom & Bjork, 2015） |
| 3. 理解与熟练是掌握的两个维度 | 理解通过解释、比较和追问形成，熟练通过足量且有反馈的独立练习形成。评估和安排教学时分别考察两个维度；各自需要达到的程度依据学习者的目标判断 | 概念性知识与程序性知识是可以区分的两类知识，二者在发展中相互促进（Rittle-Johnson et al., 2001） |
| 4. 已学内容的保持随时间下降，间隔之后的检验兼有巩固和验证的作用 | 对间隔较长的已学内容，依据它与当前内容的关系和对学习者目标的重要程度，在教学中择机以多种方式引入检验。系统提供各项内容距上次涉及的时间 | 分散练习的保持效果优于集中练习（Cepeda et al., 2006）。提取练习兼有巩固作用（Roediger & Karpicke, 2006） |
| 5. 教学依据对学习者的了解进行个性化 | 新的内容通过与已有的知识建立联系而被理解，同样的讲解和任务对基础不同的学习者效果不同。依据学习者的目标、背景、偏好、掌握状态和学习特征，选择切入点、讲解方式、任务难度和节奏 | 一对一辅导的效果及其与交互细致程度的关系（VanLehn, 2011）。适合初学者的指导方式，对已有基础的学习者效果下降（Kalyuga et al., 2003） |
| 6. 对学习者的判断是推断，在教学中检验 | 掌握状态和学习特征都是依据有限的表现作出的推断。一项推断影响教学安排而依据不足时，选择能够同时检验它的教学活动，并以结果修订学习状态 | 在教学过程中获取关于学习者理解状况的证据并据此调整教学，可以提高学习效果（Black & Wiliam, 1998） |
| 7. 学习者对学习过程拥有决定权 | 学习者对学习过程的自主决定有助于维持学习的动机和持续的投入。学习者的设定和在对话中提出的明确要求是教学的前提。对话之内的教学做法由模型选用，学习者不愿采用时随即调整；改变学习者的投入、分工或进度的安排，由模型提出并说明差别，由学习者决定。要求与长期掌握存在冲突时，说明可能的影响，由学习者决定 | 自主性对内在动机和持续投入的作用（Ryan & Deci, 2000） |

第 4 条和第 6 条都涉及检验，侧重不同。第 4 条针对保持随时间的变化，检验的时机由间隔决定；第 6 条针对判断本身的不确定性，检验的对象既包括掌握状态，也包括学习特征，例如通过尝试不同的讲解或练习方式并比较学习者随后的表现，来确认某种方式对该学习者是否有效。两条的共同点是检验融入教学活动，并且检验本身也是学习活动。

上述文献的题名和出处已经核对，列于文末。七条原则的文字已经定稿；原则与文献之间的对应是初步的，与原文的逐条对照尚未进行，列为详细设计中的一项。

## 指引的写法

指引是交给模型的正文。它的写法依据设计哲学中的“模型为主、目标导向”和“有理论依据”两条立场（见[目标、边界与设计哲学](goals-and-principles.md)），有以下约定。

- 陈述目标、学习发生的条件和需要权衡的因素，具体做法由模型依据学习者的情况判断。
- 每条原则包含结论、所依据的学习条件和对教学的要求，使模型能够在原则未覆盖的情形下自行推理。
- 不针对不同水平的学习者预设处理方式，不使用对比式的反面示例。
- 否定性的条目只在两种情况下写入：实际使用中反复出现的不当做法，以及由当前系统的限制决定的不可行做法。基础版的指引不含否定性条目；使用中观察到反复出现的偏离时，以“需要避免的常见做法”为题补充，每一条写明所针对的现象。
- 使用书面的专业表述，不依赖特定厂商的术语。

## 学习方法

学习方法是针对某一学习类型的说明，供模型在安排教学时参考。

学习类型是学习活动的类别，按活动的形态划分，不按材料的载体划分：同是一门课程，阅读讲义和完成作业是两种不同的学习活动，需要的辅导方式也不同。基础版区分两种学习类型。

| 学习类型 | 定义 | 例子 |
|---|---|---|
| 讲解型 | 学习者通过材料中的讲解以及与模型的交流学习 | 阅读书籍、课程讲义和课件，观看讲座 |
| 实践型 | 学习者通过在作品（代码或系统）上完成任务学习。按学习者与作品的关系分为两类：读，即理解已有的系统；写，即构建新的作品 | 阅读源码；完成课程作业、复现已有的结果、完成自己的项目 |

修改已有的系统（修复、优化、扩展）兼有读和写。调试和实验是读和写中都会出现的环节，不单列为一类。

一个学习项目可以包含多种学习类型，例如一门课程既有讲义，也有作业。当前的内容属于哪种学习类型、怎样推进，由模型依据内容和进度判断；同一个学习项目在不同阶段可以使用不同的学习方法。

一份学习方法包含三项内容：这类学习活动的特点；需要权衡的因素；可以取得的掌握证据的形式和进度的记录方式。学习方法不规定教学的流程。它与指引的写法一致，陈述这类活动中有效学习的条件，具体做法由模型判断。

学习方法与教学原则的分工是：教学原则适用于所有学习类型，写在指引中；学习方法是教学原则在某一学习类型中的应用，各自写在单独的文件中，按需读取。不同学习类型的内容因此相互独立，增加一种类型只需要增加一个文件。

学习方法属于插件，对所有学习者适用。它的内容分在两处。

- 设计理念和依据属于设计层，写在本文中，每种学习方法一节，在该方法设计时加入。
- 面向模型的正文属于实现，写在技能的参考文件中，随插件发布（见[技能](../components/skill.md)）。

学习者对某一类学习的个人安排不构成另一份学习方法，而是作为类型设定写入学习者设定（见[记忆](memory.md)），叠加在插件的学习方法之上；两者不一致时以设定为准。没有对应学习方法的学习活动，由模型依据教学原则和学习者的设定安排。在使用中形成、对其他学习者同样适用的做法，可以提炼后加入插件的学习方法。

学习方法按讲解型和实践型两种学习类型编写。实践型学习的学习方法见下一节；讲解型学习的学习方法在详细设计阶段编写。论文阅读等其他学习活动的学习方法有待调研。

## 实践型学习的学习方法

本节说明实践型学习的学习方法的设计：这类学习的特点，四条要点及其依据，可以取得的证据和进度的记录方式。面向模型的正文见[技能](../components/skill.md)。

### 特点

实践型学习的特点来自任务的形式，学习方法的要点由这些特点得出。

- **作品可以在学习没有发生的情况下完成。** 模型能够完成任务的大部分，任务的完成与能力的形成因此是两件事。在一项随机对照实验中，借助 AI 学习一个新的编程库的开发者，在概念理解、代码阅读和调试上的表现低于不借助 AI 的一组，平均效率没有显著提高；把编码任务完全交给 AI 的参与者效率有所提高，但以学习为代价；在得到 AI 辅助的同时保持认知参与的使用方式，学习效果得以保持（Shen & Tamkin, 2026）。
- **一项任务同时用到多项知识。** 其中有学习者尚未具备的，这些缺口在任务进行中暴露。
- **作品的运行给出不依赖模型的反馈。** 程序的输出、测试和测量可以检验学习者的预测和假设。
- **过程持续多次对话，大部分发生在对话之外。** 模型只能了解学习者带回对话的内容，以及它能够直接读取的内容。
- **读和写的检验方式不同。** 读没有现成的对错标准。程序的理解是自上而下、由假设驱动的过程，起初笼统的假设依据程序文本逐步细化（Brooks, 1983），理解因此通过预测和运行来检验。写有给定的规格和测试，或者学习者自定的验收标准。

### 要点

要点有四条，都是教学原则在实践型学习中的应用，没有新增原则。下表给出每条要点的内容和主要依据。

| 要点 | 内容 | 主要依据 |
|---|---|---|
| 1. 学习的方式由学习者与模型商定 | 实践任务可以有不同的做法：直接从任务开始还是先学前置内容，各部分由谁完成，无法推进时提供何种支持。这些做法在学习效果和所需时间上有明显差别，适合哪一种取决于学习者的目标、基础和时间。模型提出建议并说明各种做法的差别，由学习者决定，写入项目设定；情况变化时重新商定。学习材料对使用 AI 另有规定时，模型说明其内容和用意，作为商定的依据 | 教学原则第 7 条。使用 AI 的方式不同，学习的结果不同（Shen & Tamkin, 2026） |
| 2. 加工由谁完成决定学习是否发生；支持与当前的能力相称，并随能力的提高而减少 | 安排每一部分时权衡两点：它与学习目标的关系，学习者当前能否在支持下完成。与学习目标直接相关的加工尽可能由学习者完成，模型提供使其能够继续推进的支持；写的时候，这类加工包括分解任务、设计、实现、调试和验证，读的时候包括提出问题、预测、追踪和解释。与学习目标无关的部分可以交给模型。学习者尚不能完成的部分先由模型示范或讲解，随后把相近的部分交给学习者，支持逐步减少 | 教学原则第 1 条。辅助的多少需要权衡（Koedinger & Aleven, 2007）。在认知技能形成的初期，学习示例比解题有效，后期则相反；由示例过渡到解题时，逐步加入需要学习者自己完成的部分，直到学习者独立解题（Renkl & Atkinson, 2003） |
| 3. 缺口在任务中补足，补到多深由目标决定，并留下记录 | 在用到时补足，有具体的情境和明确的用途。深度依据学习者的目标判断，区分能够使用和需要掌握，不明确时询问学习者。这样获得的知识比较零散，因此记录每个缺口和补足的程度，供之后有针对地巩固。同一主题的缺口积累较多，或任务在支持下仍无法推进时，模型建议先集中学习相关内容 | 先分析对比案例再听讲解的学生，在约一周后的预测任务中的表现好于先阅读或总结相关文本再听讲解的学生，也好于只分析案例而没有听讲解的学生（Schwartz & Bransford, 1998）。指导充分的教学比指导很少的教学更有效，指导的优势在学习者具备足够的已有知识之后才开始减弱（Kirschner et al., 2006） |
| 4. 完成任务不等于掌握 | 测试通过说明作品可用，不说明学习者能够独立完成。记录表现时注明得到的支持；掌握的证据来自学习者自己完成的加工。对学习者的目标重要的内容，间隔之后在没有支持或不同的情境下再次检验 | 教学原则第 2 条和第 4 条。训练过程中的表现不能可靠地反映长期保持与迁移（Soderstrom & Bjork, 2015）。借助 AI 完成任务时的表现不能代表其后独立完成时的表现（Bastani et al., 2025；Shen & Tamkin, 2026） |

学习材料自带规定的一个例子是斯坦福大学的 CS336 课程（2026 年春季学期）：[课程主页](https://cs336.stanford.edu/)允许就底层的编程问题和高层的概念问题询问 LLM，禁止直接用它解答作业；作业仓库附有一份[给 AI 编码助手的说明](https://github.com/stanford-cs336/assignment1-basics/blob/main/CLAUDE.md)，规定它的角色是助教，不生成解答。

要点 1 所说的做法中，直接从任务开始的一种需要单独说明。学习者着手一项目前无法独立完成的任务，所需的能力和前置知识在任务中借助模型逐步补足，可以较快地取得可用的能力。它成立的条件是任务在有支持时可以完成；缺口过多时，先集中学习一段前置内容更为有效。这种做法有两个风险：在支持下完成的内容，独立时未必能够完成；随用随补的知识比较零散，容易留下缺口。要点 2 至 4 对应这两个风险：支持逐步减少，缺口留下记录并注明补足的程度，重要的内容在没有支持的条件下再次检验。

本节引用的文献，题名、出处和摘要已经核对，列于文末；与原文的逐条对照在学习方法定稿时进行。

### 证据与进度

实践中的表现是掌握证据的重要来源。记录时注明得到的支持：独立完成，还是在何种支持下完成。读和写可以取得的证据不同。

| 任务 | 可以取得的证据 |
|---|---|
| 读 | 阅读或运行之前作出的预测与实际结果的对照；对一条执行路径和设计取舍的解释；可以运行的小改动 |
| 写 | 动手之前提出的任务分解和设计；独立实现并通过测试的部分；调试中提出的假设及其验证方式；对实现和关键决定的讲解 |

预测是其中容易安排的一种。先预测、再运行、再考察和修改已有的程序、最后独立编写的教学安排，在面向 11 至 14 岁学生的对照研究中取得了更好的后测成绩（Sentance et al., 2019）。

实践型学习与讲解型学习更新的是同一批掌握状态页面：实践中暴露的缺口可以回到讲解，讲解过的内容可以在实践中检验。间隔之后的检验也可以采用实践的形式，例如不看参考重写一个部分，或说明一条执行路径。

实践项目的进度页适合按里程碑或问题组织，记录任务的分解、当前位置、尝试过的方案及其结果、未解决的问题和有待巩固的缺口。对话开始时，模型先了解上次之后的进展：可以读取代码和提交历史时直接读取，否则由学习者说明。

### 限制

模型对实践过程的了解取决于客户端。能够访问学习者本机文件的客户端可以直接读取代码、运行结果和提交历史，依据比较完整；网页端和移动端只能依据学习者带回对话的内容。实践型学习因此更适合在前一类客户端中进行。

## 参考资料

- Bastani, H., et al. (2025). 关于生成式 AI 对高中数学学习影响的随机对照实验，发表于 *PNAS*。[SSRN](https://papers.ssrn.com/abstract=4895486)
- Black, P., & Wiliam, D. (1998). Assessment and classroom learning. *Assessment in Education: Principles, Policy & Practice*, 5(1), 7–74. [DOI](https://doi.org/10.1080/0969595980050102)
- Brooks, R. (1983). Towards a theory of the comprehension of computer programs. *International Journal of Man-Machine Studies*. [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0020737383800315)
- Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin*. [PubMed](https://pubmed.ncbi.nlm.nih.gov/16719566/)
- Chi, M. T. H., & Wylie, R. (2014). The ICAP framework: Linking cognitive engagement to active learning outcomes. *Educational Psychologist*. [ASU](https://education.asu.edu/lcl/publications/chi-m-t-h-wylie-r-2014-icap-framework-linking-cognitive-engagement-active-learning)
- Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J. (2003). The expertise reversal effect. *Educational Psychologist*. [UOW](https://ro.uow.edu.au/edupapers/136)
- Kirschner, P. A., Sweller, J., & Clark, R. E. (2006). Why minimal guidance during instruction does not work: An analysis of the failure of constructivist, discovery, problem-based, experiential, and inquiry-based teaching. *Educational Psychologist*. [DOI](https://doi.org/10.1207/s15326985ep4102_1)
- Koedinger, K. R., & Aleven, V. (2007). Exploring the assistance dilemma in experiments with cognitive tutors. *Educational Psychology Review*. [PDF](https://pslcdatashop.web.cmu.edu/KDDCup/FAQ/Koedinger-Aleven-EPR-07.pdf)
- Renkl, A., & Atkinson, R. K. (2003). Structuring the transition from example study to problem solving in cognitive skill acquisition: A cognitive load perspective. *Educational Psychologist*. [DOI](https://doi.org/10.1207/S15326985EP3801_3)
- Rittle-Johnson, B., Siegler, R. S., & Alibali, M. W. (2001). Developing conceptual understanding and procedural skill in mathematics: An iterative process. *Journal of Educational Psychology*. [CMU](https://kilthub.cmu.edu/articles/journal_contribution/Developing_conceptual_understanding_and_procedural_skill_in_mathematics_An_iterative_process/6614285)
- Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science*. [PubMed](https://pubmed.ncbi.nlm.nih.gov/16507066/)
- Ryan, R. M., & Deci, E. L. (2000). Self-determination theory and the facilitation of intrinsic motivation, social development, and well-being. *American Psychologist*. [PubMed](https://pubmed.ncbi.nlm.nih.gov/11392867/)
- Schwartz, D. L., & Bransford, J. D. (1998). A time for telling. *Cognition and Instruction*. [DOI](https://doi.org/10.1207/s1532690xci1604_4)
- Sentance, S., Waite, J., & Kallia, M. (2019). Teaching computer programming with PRIMM: A sociocultural perspective. *Computer Science Education*. [DOI](https://doi.org/10.1080/08993408.2019.1608781)
- Shen, J. H., & Tamkin, A. (2026). How AI impacts skill formation. arXiv:2601.20245. [arXiv](https://arxiv.org/abs/2601.20245)
- Soderstrom, N. C., & Bjork, R. A. (2015). Learning versus performance: An integrative review. *Perspectives on Psychological Science*. [PubMed](https://pubmed.ncbi.nlm.nih.gov/25910388/)
- VanLehn, K. (2011). The relative effectiveness of human tutoring, intelligent tutoring systems, and other tutoring systems. *Educational Psychologist*. [ERIC](https://eric.ed.gov/?id=EJ946764)
