# 辅导：教学原则与学习方法

本文说明 Cairn 中辅导部分的设计：辅导的目标，教学原则及其依据，指引的写法，学习方法的定位。交给模型的指引正文属于技能，见[技能](../components/skill.md)。各部分的确认状态见[议题与决策](../decisions.md)。

## 辅导的目标

辅导以长期掌握为目标：学习者在脱离辅助的条件下，能够准确解释所学内容，把它应用于新的问题，并在此基础上继续学习。讲解的深度、提问与练习的安排、何时直接给出结论，均以对这一目标的贡献来权衡。

模型在辅导中的角色是学习者的长期导师。“长期”有两层含义：衡量的标准是长期的保持和迁移，而不是当次对话中的表现；辅导跨越多次对话，由记忆衔接。

## 教学原则

教学原则说明有效学习的条件，适用于所有学习类型，写在指引中，具体做法由模型依据学习者的情况判断。基础版共七条。下表给出每条原则的要点和主要依据，面向模型的完整表述见[技能](../components/skill.md)中的指引正文。

| 原则 | 要点 | 主要依据 |
|---|---|---|
| 1. 学习来源于学习者自身的认知加工 | 检索、解释、推理、应用和纠错等加工活动使知识得以建立和巩固；讲解、示例和反馈的作用在于引发并支持这些活动。支持的形式和程度随学习者的知识状态与任务难度调整 | 建构性和交互性的学习活动效果优于被动接受（Chi & Wylie, 2014）。提取练习促进长期保持（Roediger & Karpicke, 2006）。辅助的多少需要权衡（Koedinger & Aleven, 2007）。适合初学者的指导方式，对已有基础的学习者效果下降（Kalyuga et al., 2003）。不加限制地用生成式 AI 获取答案，会提高练习成绩而降低其后独立完成时的成绩；带有引导约束的辅导可以减轻这一影响（Bastani et al., 2025） |
| 2. 掌握的判断以多种表现为依据 | 讲解之后即时完成或在提示下完成的正确表现，主要反映内容在当时的提取强度，对长期保持和迁移的预测力有限。掌握的证据来自不同时间、不同情境和不同任务形式下的独立表现 | 训练过程中的表现不能可靠地反映长期保持与迁移（Soderstrom & Bjork, 2015） |
| 3. 理解与熟练是掌握的两个维度 | 理解通过解释、比较和追问形成，熟练通过足量且有反馈的独立练习形成。评估和安排教学时分别考察两个维度 | 概念性知识与程序性知识是可以区分的两类知识，二者在发展中相互促进（Rittle-Johnson et al., 2001） |
| 4. 已学内容的保持随时间下降，间隔之后的检验兼有巩固和验证的作用 | 对间隔较长、且与当前内容相关的已学内容，在教学中择机以多种方式引入检验。系统提供各项内容距上次涉及的时间 | 分散练习的保持效果优于集中练习（Cepeda et al., 2006）。提取练习兼有巩固作用（Roediger & Karpicke, 2006） |
| 5. 教学依据对学习者的了解进行个性化 | 依据学习者的目标、背景、偏好、掌握状态和学习特征，选择切入点、讲解方式、任务难度和节奏 | 一对一辅导的效果及其与交互细致程度的关系（VanLehn, 2011） |
| 6. 对学习者的判断是推断，在教学中检验 | 掌握状态和学习特征都是依据有限的表现作出的推断。一项推断影响教学安排而依据不足时，选择能够同时检验它的教学活动，并以结果修订学习状态 | 在教学过程中获取关于学习者理解状况的证据并据此调整教学，可以提高学习效果（Black & Wiliam, 1998） |
| 7. 学习者对学习过程拥有决定权 | 学习者的设定和在对话中提出的明确要求是教学的前提。要求与长期掌握的目标存在冲突时，说明可能的影响，由学习者决定 | 自主性对内在动机和持续投入的作用（Ryan & Deci, 2000） |

第 4 条和第 6 条都涉及检验，侧重不同。第 4 条针对保持随时间的变化，检验的时机由间隔决定；第 6 条针对判断本身的不确定性，检验的对象既包括掌握状态，也包括学习特征，例如通过尝试不同的讲解或练习方式并比较学习者随后的表现，来确认某种方式对该学习者是否有效。两条的共同点是检验融入教学活动，并且检验本身也是学习活动。

上述文献的题名和出处已经核对，列于文末。原则与文献之间的对应是初步的，逐条对照原文在指引定稿时进行。

## 指引的写法

指引是交给模型的正文。它的写法依据设计哲学中的“模型为主、目标导向”和“有理论依据”两条立场（见[目标、边界与设计哲学](goals-and-principles.md)），有以下约定。

- 陈述目标、学习发生的条件和需要权衡的因素，具体做法由模型依据学习者的情况判断。
- 每条原则包含结论、所依据的学习条件和对教学的要求，使模型能够在原则未覆盖的情形下自行推理。
- 不针对不同水平的学习者预设处理方式，不使用对比式的反面示例。
- 否定性的条目只在两种情况下写入：实际使用中反复出现的不当做法，以及由当前系统的限制决定的不可行做法。基础版的指引不含否定性条目；使用中观察到反复出现的偏离时，以“需要避免的常见做法”为题补充，每一条写明所针对的现象。
- 使用书面的专业表述，不依赖特定厂商的术语。

## 学习方法

学习方法说明某一学习类型的常用安排，供模型在安排教学时参考。一份学习方法包含三项内容：该类型学习的常用推进方式，例如课程中讲座、阅读和作业的衔接，书籍中章节阅读和练习的安排；该类型下可以获得的掌握证据的形式；进度页的建议结构。

学习方法与教学原则的分工是：教学原则适用于所有学习类型，写在指引中；学习方法只适用于某一类型，各自写在单独的文件中，按需读取。不同学习类型的内容因此相互独立，增加一种类型只需要增加一个文件。

学习方法属于插件，对所有学习者适用。它的内容分在两处。

- 设计理念和依据属于设计层，写在本文中，每种学习方法一节，在该方法设计时加入。
- 具体的流程属于实现，写在技能的参考文件中，随插件发布（见[技能](../components/skill.md)）。

学习者对某一类学习的个人安排不构成另一份学习方法，而是作为类型设定写入学习者设定（见[记忆](memory.md)），叠加在插件的学习方法之上；两者不一致时以设定为准。没有对应学习方法的学习类型，由模型依据教学原则和学习者的设定安排。在使用中形成、对其他学习者同样适用的安排，可以提炼为新的学习方法加入插件。

基础版提供课程和书籍两种学习方法。实践项目、源码阅读和论文阅读的学习方法有待调研。

## 参考资料

- Bastani, H., et al. (2025). 关于生成式 AI 对高中数学学习影响的随机对照实验，发表于 *PNAS*。[SSRN](https://papers.ssrn.com/abstract=4895486)
- Black, P., & Wiliam, D. (1998). Assessment and classroom learning. *Assessment in Education: Principles, Policy & Practice*, 5(1), 7–74. [DOI](https://doi.org/10.1080/0969595980050102)
- Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin*. [PubMed](https://pubmed.ncbi.nlm.nih.gov/16719566/)
- Chi, M. T. H., & Wylie, R. (2014). The ICAP framework: Linking cognitive engagement to active learning outcomes. *Educational Psychologist*. [ASU](https://education.asu.edu/lcl/publications/chi-m-t-h-wylie-r-2014-icap-framework-linking-cognitive-engagement-active-learning)
- Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J. (2003). The expertise reversal effect. *Educational Psychologist*. [UOW](https://ro.uow.edu.au/edupapers/136)
- Koedinger, K. R., & Aleven, V. (2007). Exploring the assistance dilemma in experiments with cognitive tutors. *Educational Psychology Review*. [PDF](https://pslcdatashop.web.cmu.edu/KDDCup/FAQ/Koedinger-Aleven-EPR-07.pdf)
- Rittle-Johnson, B., Siegler, R. S., & Alibali, M. W. (2001). Developing conceptual understanding and procedural skill in mathematics: An iterative process. *Journal of Educational Psychology*. [CMU](https://kilthub.cmu.edu/articles/journal_contribution/Developing_conceptual_understanding_and_procedural_skill_in_mathematics_An_iterative_process/6614285)
- Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science*. [PubMed](https://pubmed.ncbi.nlm.nih.gov/16507066/)
- Ryan, R. M., & Deci, E. L. (2000). Self-determination theory and the facilitation of intrinsic motivation, social development, and well-being. *American Psychologist*. [PubMed](https://pubmed.ncbi.nlm.nih.gov/11392867/)
- Soderstrom, N. C., & Bjork, R. A. (2015). Learning versus performance: An integrative review. *Perspectives on Psychological Science*. [PubMed](https://pubmed.ncbi.nlm.nih.gov/25910388/)
- VanLehn, K. (2011). The relative effectiveness of human tutoring, intelligent tutoring systems, and other tutoring systems. *Educational Psychologist*. [ERIC](https://eric.ed.gov/?id=EJ946764)
