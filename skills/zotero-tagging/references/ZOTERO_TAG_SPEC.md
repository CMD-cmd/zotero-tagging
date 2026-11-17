# Zotero V2.1 标签规范

共154项受控标签，使用稳定ID管理名称及十维字段映射。

## 分类与检索

Article三类分别服务机制、材料、器械评价精读。Clinical使用六个直接类型；每篇选择一个主要Type。其他维度依据核心研究内容稀疏选择。复合标签表示主题并集。

## 名称与显示

常用英文词、缩写和必要中文提示构成标签名。ZoteroStyle列当前使用`[a-zA-Zα-ω\d-]+`提取胶囊；LeFort-I、Zn-Fe、3D-Organoid使用普通连字符，PDLLA后用普通空格连接中文说明。保留已有`ﾉ`作为词表中的复合缩写分隔符。

完整别名由词表识别。具体名称更换使用`rename_map`中的精确映射，标签身份与文献归属按映射保持。

## 数据保留

普通维护保留用户自定义标签、阅读状态、集合归属、附件和批注关系。全量替换分类仅作用于本词表管理的标签。定点待核记录见`pending_review.json`。

## 全部规范标签

### Ａ１Type

| ID | 标签 | 定义 |
|---|---|---|
| ZT-001 | `#Ａ１Type/Article 论著/Mechanistic 机制研究` | Mechanistic：主要阅读目标是分子或细胞机制、调控关系与生物学解释。关联、干预和计算证据的强度另行记录。 |
| ZT-002 | `#Ａ１Type/Article 论著/Biomaterial 生物材料研究` | Biomaterial：主要阅读目标是材料合成、配方、载体设计及生物效应。 |
| ZT-003 | `#Ａ１Type/Article 论著/DeviceEvaluation 器械临床前评价` | DeviceEvaluation：主要阅读目标是成熟器械或固定系统的力学、降解、相容性或临床前性能评价。 |
| ZT-004 | `#Ａ１Type/Clinical 临床研究/RCT 随机对照试验` | RCT用于在Clinical下，直接一次筛选；按论文的随机干预设计判定。 |
| ZT-005 | `#Ａ１Type/Clinical 临床研究/Prospective 前瞻性临床研究` | Prospective用于在Clinical下，直接筛选前瞻临床研究；明确的RCT或CaseControl优先使用具体类型。 |
| ZT-006 | `#Ａ１Type/Clinical 临床研究/Retrospective 回顾性临床研究` | Retrospective用于在Clinical下，直接筛选回顾临床研究；明确病例对照时用CaseControl。 |
| ZT-007 | `#Ａ１Type/Clinical 临床研究/CrossSectional 横断面研究` | CrossSectional用于；仅将已核实的病例对照误标条目转入新增CaseControl。 |
| ZT-008 | `#Ａ１Type/Clinical 临床研究/CaseReport 病例报告与系列` | CaseReport统一覆盖病例报告与病例系列，按论文主要设计选择。 |
| ZT-009 | `#Ａ１Type/Review 综述` | Review继续作为一般综述入口；有明确系统检索或Meta分析证据时用已有具体子类。 |
| ZT-010 | `#Ａ１Type/SystematicReview 系统综述` | 用于SystematicReview入口及其与MetaAnalysis的既有层级。 |
| ZT-011 | `#Ａ１Type/SystematicReview 系统综述/MetaAnalysis Meta分析` | MetaAnalysis用于具体入口；同一篇在Type中选择一个主要类型。 |
| ZT-012 | `#Ａ１Type/Computational 计算与仿真/FEA 有限元分析` | FEA仍在Computational下直接分流，缩短英文展开式。 |
| ZT-013 | `#Ａ１Type/Computational 计算与仿真/Bioinformatics 生物信息与分子模拟` | 3篇使用Bioinformatics，定义覆盖生信与分子模拟；用于综合计算研究入口。 |
| ZT-014 | `#Ａ１Type/Guideline 指南与规范/ClinicalGuideline 临床诊疗指南` | ClinicalGuideline用于临床指南与规范入口。 |
| ZT-015 | `#Ａ１Type/Guideline 指南与规范/Standard 技术标准与报告规范` | Standard用于技术、报告与命名共识等规范性资料。 |
| ZT-016 | `#Ａ１Type/Protocol 实验方案与规程` | Protocol用于可执行实验规程，用于方法学习入口。 |
| ZT-017 | `#Ａ１Type/ProductInfo 产品资料` | 产品手册、说明书、注册技术摘要等产品资料。 |
| ZT-018 | `#Ａ１Type/Book 专著与教材` | Book统一专著、教材与章节，保持原范围。 |
| ZT-019 | `#Ａ１Type/Commentary 述评与观点` | Commentary用于述评与观点入口。 |
| ZT-020 | `#Ａ１Type/Humanities 科技人文与方法论` | Humanities用于科技人文与方法论资料。 |
| ZT-021 | `#Ａ１Type/Humanities 科技人文与方法论/Bioethics 生命伦理与治理` | Bioethics用于生命伦理与治理资料。 |
| ZT-154 | `#Ａ１Type/Clinical 临床研究/CaseControl 病例对照` | 病例对照研究，按结局或病例状态选择病例和对照，再比较暴露或相关因素。用于Clinical单次筛选；病例对照优先于笼统的回顾性描述。 |

### Ｂ１Disease

| ID | 标签 | 定义 |
|---|---|---|
| ZT-022 | `#Ｂ１Disease/MRONJ 药物相关颌骨坏死` | 药物相关颌骨坏死总类；BRONJ、DRONJ作为对应具体类型。 |
| ZT-023 | `#Ｂ１Disease/MRONJ 药物相关颌骨坏死/BRONJ 双膦酸盐相关颌骨坏死` | 双膦酸盐相关颌骨坏死。 |
| ZT-024 | `#Ｂ１Disease/MRONJ 药物相关颌骨坏死/DRONJ 地诺单抗相关颌骨坏死` | 地诺单抗相关颌骨坏死。 |
| ZT-025 | `#Ｂ１Disease/ONFH 股骨头坏死` | 股骨头坏死总类，含病因子类。 |
| ZT-026 | `#Ｂ１Disease/ONFH 股骨头坏死/SONFH 激素性股骨头坏死` | 激素性股骨头坏死。 |
| ZT-027 | `#Ｂ１Disease/ONFH 股骨头坏死/IschemicONFH 缺血性股骨头坏死` | 缺血性股骨头坏死的检索类别。 |
| ZT-028 | `#Ｂ１Disease/TMD 颞下颌关节病` | 颞下颌关节病总类，含TMJ-OA。 |
| ZT-029 | `#Ｂ１Disease/TMD 颞下颌关节病/TMJ-OA 颞下颌关节骨关节炎` | 颞下颌关节骨关节炎。 |
| ZT-030 | `#Ｂ１Disease/Osteoarthritis 骨关节炎` | 用于疾病分类范围与层级。 |
| ZT-031 | `#Ｂ１Disease/Osteoporosis 骨质疏松症` | 用于疾病分类范围与层级。 |
| ZT-032 | `#Ｂ１Disease/Periodontitis 牙周炎` | 用于疾病分类范围与层级。 |
| ZT-033 | `#Ｂ１Disease/Peri-Implantitis 种植体周围炎` | 用于疾病分类范围与层级。 |
| ZT-034 | `#Ｂ１Disease/Endodontics 牙体牙髓病` | 用于牙体牙髓疾病的综合入口。 |
| ZT-035 | `#Ｂ１Disease/DentofacialDeformity 牙颌面畸形` | 用于疾病分类范围与层级。 |
| ZT-036 | `#Ｂ１Disease/Craniosynostosis 颅缝早闭` | 用于疾病分类范围与层级。 |
| ZT-037 | `#Ｂ１Disease/CraniofacialFracture 颅颌面骨折` | 用于疾病分类范围与层级。 |
| ZT-038 | `#Ｂ１Disease/CraniofacialFracture 颅颌面骨折/MandibularFracture 下颌骨骨折` | 用于疾病分类范围与层级。 |
| ZT-039 | `#Ｂ１Disease/CraniofacialFracture 颅颌面骨折/MidfacialFracture 面中部与眶壁骨折` | 面中部与眶壁作为本库已有综合部位入口。 |
| ZT-040 | `#Ｂ１Disease/BoneDefect 骨缺损与拔牙窝创伤` | 用于骨缺损与拔牙窝的共同应用场景。 |
| ZT-041 | `#Ｂ１Disease/Infection 感染性疾病/OralInfection 口腔细菌与生物膜感染` | 用于口腔细菌与生物膜感染的综合疾病入口。 |
| ZT-042 | `#Ｂ１Disease/Infection 感染性疾病/ImplantInfection 手术与植入物感染` | 标签对应手术与植入物感染；历史自动映射须按实际疾病核实。 |
| ZT-043 | `#Ｂ１Disease/Wound 皮肤黏膜创面` | 用于疾病分类范围与层级。 |
| ZT-044 | `#Ｂ１Disease/Scar 病理性瘢痕与纤维化` | 瘢痕与纤维化用于综合入口，沿用已形成的检索习惯。 |
| ZT-045 | `#Ｂ１Disease/MetabolicDisorder 糖脂代谢疾病` | 用于糖脂代谢疾病的综合疾病入口。 |
| ZT-046 | `#Ｂ１Disease/AutoimmuneDisease 自身免疫与风湿病` | 用于自身免疫与风湿病的综合疾病入口。 |
| ZT-047 | `#Ｂ１Disease/CardiovascularDisease 心血管疾病` | 用于疾病分类范围与层级。 |
| ZT-048 | `#Ｂ１Disease/Tumor 肿瘤` | 用于疾病分类范围与层级。 |

### Ｂ２Surgery

| ID | 标签 | 定义 |
|---|---|---|
| ZT-049 | `#Ｂ２Surgery/Orthognathic 正颌外科` | Orthognathic总类及其常用术式叶节点使用。 |
| ZT-050 | `#Ｂ２Surgery/Orthognathic 正颌外科/SSRO 矢状劈开术` | SSRO统一收纳SSRO、BSSRO、SSO、BSSO等升支矢状劈开术写法。 |
| ZT-051 | `#Ｂ２Surgery/Orthognathic 正颌外科/LeFort-I 截骨术` | LeFort-I截骨术，名称兼容ZoteroStyle胶囊提取规则。 |
| ZT-052 | `#Ｂ２Surgery/Orthognathic 正颌外科/Genioplasty 颏成形术` | 用于术式检索入口。 |
| ZT-053 | `#Ｂ２Surgery/Orthognathic 正颌外科/DO 牵张成骨` | 牵张成骨，在正颌分支中提供直接入口。 |
| ZT-054 | `#Ｂ２Surgery/MaxillofacialFixation 颌面创伤与重建内固定` | 用于颌面创伤与重建固定入口。 |
| ZT-055 | `#Ｂ２Surgery/ImplantSurgery 牙槽与种植外科` | 用于牙槽与种植外科的综合操作入口。 |
| ZT-056 | `#Ｂ２Surgery/OrthopedicFixation 骨科内固定与关节置换` | 用于骨科固定与关节置换入口。 |

### Ｃ１Material

| ID | 标签 | 定义 |
|---|---|---|
| ZT-057 | `#Ｃ１Material/ResorbablePolymer 可吸收高分子` | 用于可吸收高分子的上位材料词；已有具体成分时按原粒度选择。 |
| ZT-058 | `#Ｃ１Material/ResorbablePolymer 可吸收高分子/PLLA` | 用于PLLA具体材料体系；全称由词表定义承接。 |
| ZT-059 | `#Ｃ１Material/ResorbablePolymer 可吸收高分子/PDLLA 乳酸共聚物` | 外消旋聚乳酸及乳酸立构共聚、含TMC体系的综合材料类；明确PLGA、PLLA等已有专类时优先专类。 |
| ZT-060 | `#Ｃ１Material/ResorbablePolymer 可吸收高分子/PLGA` | 用于PLGA成分入口；具体比例属于配方信息。 |
| ZT-061 | `#Ｃ１Material/ResorbablePolymer 可吸收高分子/PGA` | 用于PGA成分入口。 |
| ZT-062 | `#Ｃ１Material/ResorbablePolymer 可吸收高分子/PCL` | 用于PCL成分入口。 |
| ZT-063 | `#Ｃ１Material/ResorbablePolymer 可吸收高分子/u-HAﾉPLLA` | 用于u-HAﾉPLLA复合体系，分隔符与检索含义沿用。 |
| ZT-064 | `#Ｃ１Material/BiodegradableMetal 可降解金属` | 用于可降解金属上位材料词。 |
| ZT-065 | `#Ｃ１Material/BiodegradableMetal 可降解金属/Mg 镁基` | 镁为基体的金属材料。 |
| ZT-066 | `#Ｃ１Material/BiodegradableMetal 可降解金属/Zn-Fe 锌基与铁基` | 锌基或铁基任一材料体系的综合类别。 |
| ZT-067 | `#Ｃ１Material/Titanium 钛与钛合金` | 用于材料体系范围。 |
| ZT-068 | `#Ｃ１Material/Hydrogel 水凝胶` | 用于通用Hydrogel入口及已有具体子类。 |
| ZT-069 | `#Ｃ１Material/Hydrogel 水凝胶/GelMA` | GelMA使用熟悉缩写；全称用于在定义中。 |
| ZT-070 | `#Ｃ１Material/Hydrogel 水凝胶/NaturalHydrogel 天然高分子水凝胶` | 用于天然高分子水凝胶综合材料类。 |
| ZT-071 | `#Ｃ１Material/Hydrogel 水凝胶/SmartHydrogel 合成与响应型水凝胶` | 用于合成与响应型水凝胶的综合类，具体性质按实际研究记录。 |
| ZT-072 | `#Ｃ１Material/MOF 金属有机框架` | 用于材料体系范围。 |
| ZT-073 | `#Ｃ１Material/MOF 金属有机框架/ZIF-8` | 用于材料体系范围。 |
| ZT-074 | `#Ｃ１Material/Bioceramic 生物陶瓷与活性玻璃` | 用于生物陶瓷与活性玻璃的综合材料类。 |
| ZT-075 | `#Ｃ１Material/Nanomaterial 无机与复合纳米材料` | 用于无机与复合纳米材料范围；成分与递送角色分别按C1、C2的用途表达。 |
| ZT-076 | `#Ｃ１Material/SurfaceModification 表面改性/Coating 表面涂层` | 用于Coating涂层入口。 |
| ZT-077 | `#Ｃ１Material/SurfaceModification 表面改性/SurfaceTopography 表面形貌与电荷修饰` | 用于表面形貌与电荷的综合设计入口。 |

### Ｃ２Carrier

| ID | 标签 | 定义 |
|---|---|---|
| ZT-078 | `#Ｃ２Carrier/Scaffold 组织工程与控释支架` | 用于组织工程及控释支架入口，按具体结构用途选择。 |
| ZT-079 | `#Ｃ２Carrier/Nanocarrier 纳米递送载体` | 用于纳米递送载体入口。 |
| ZT-080 | `#Ｃ２Carrier/tFNAs 四面体核酸` | tFNAs用于四面体框架核酸平台。 |
| ZT-081 | `#Ｃ２Carrier/EVs 细胞外囊泡` | EVs覆盖细胞外囊泡及外泌体，沿用综合粒度。 |
| ZT-082 | `#Ｃ２Carrier/CellCarrier 细胞与血小板载体` | 细胞或血小板相关载体与递送形式继续用于；无细胞条件培养基不自动归入该类。 |

### Ｃ３Drug

| ID | 标签 | 定义 |
|---|---|---|
| ZT-083 | `#Ｃ３Drug/Antiresorptive 抗骨吸收药/BPs 双膦酸盐` | BPs为双膦酸盐药物入口；按研究中药物的实际角色选择。 |
| ZT-084 | `#Ｃ３Drug/Antiresorptive 抗骨吸收药/Denosumab 地诺单抗` | 用于Denosumab地诺单抗入口。 |
| ZT-085 | `#Ｃ３Drug/Biologics 蛋白与抗体药物/TCZ 托珠单抗` | TCZ继续对应托珠单抗。 |
| ZT-086 | `#Ｃ３Drug/Biologics 蛋白与抗体药物/GrowthFactor 重组生长因子与多肽` | 用于生长因子与多肽药载的综合入口。 |
| ZT-087 | `#Ｃ３Drug/SmallMolecule 小分子化学药` | 用于小分子药物入口。 |
| ZT-088 | `#Ｃ３Drug/NucleicAcid 核酸药物` | 用于核酸药物入口。 |
| ZT-089 | `#Ｃ３Drug/NaturalProduct 天然产物与中药成分` | 用于天然产物与中药成分入口。 |
| ZT-090 | `#Ｃ３Drug/Antibiotic 抗生素与抗菌药` | 用于Antibiotic英文抓手；定义沿用抗生素与其他抗菌药，如氯己定。 |
| ZT-091 | `#Ｃ３Drug/GasTherapy 气体与活性氧分子` | 用于气体与活性氧干预综合入口；给药载荷与内源氧化应激根据研究角色区分。 |

### Ｄ１Target

| ID | 标签 | 定义 |
|---|---|---|
| ZT-092 | `#Ｄ１Target/Pathway 信号通路/JAK-STAT` | 用于通路组合，缩去重复的“信号通路”字样。 |
| ZT-093 | `#Ｄ１Target/Pathway 信号通路/NF-κB-RANKL` | 用于NF-κB与RANKL相关信号的综合入口；标签表示覆盖相关内容。 |
| ZT-094 | `#Ｄ１Target/Pathway 信号通路/MAPKﾉERK` | 用于MAPK/ERK综合信号入口。 |
| ZT-095 | `#Ｄ１Target/Pathway 信号通路/PI3K-Akt-mTOR` | 用于PI3K-Akt-mTOR信号轴。 |
| ZT-096 | `#Ｄ１Target/Pathway 信号通路/Wnt-BMP-TGFβ` | 用于Wnt-BMP-TGFβ综合入口；任一组成通路为核心研究内容即可适用。 |
| ZT-097 | `#Ｄ１Target/Pathway 信号通路/Hippo-YAP` | 用于Hippo-YAP信号轴。 |
| ZT-098 | `#Ｄ１Target/Pathway 信号通路/cAMPﾉPKA` | 用于cAMP/PKA信号轴。 |
| ZT-099 | `#Ｄ１Target/Pathway 信号通路/InnateImmune 固有免疫` | 用于固有免疫综合入口，包含TLR、NLRP3、STING等；按实际研究主题选标。 |
| ZT-100 | `#Ｄ１Target/Pathway 信号通路/Nrf2` | 用于Nrf2入口。 |
| ZT-101 | `#Ｄ１Target/Cytokine 细胞因子与生长因子/IL-6` | 用于IL-6分子入口。 |
| ZT-102 | `#Ｄ１Target/Cytokine 细胞因子与生长因子/InflammatoryCytokine 促炎因子 (IL-1-TNFα)` | 用于促炎因子综合入口，IL-1、TNF等在定义中列为覆盖范围。 |
| ZT-103 | `#Ｄ１Target/Cytokine 细胞因子与生长因子/AngiogenicFactor 促血管生长因子 (VEGF-FGF)` | 用于VEGF、FGF等血管生长因子综合入口。 |
| ZT-104 | `#Ｄ１Target/BoneMetabolism 骨与代谢分子/OCN 骨钙素` | OCN用于骨钙素辨识提示。 |
| ZT-105 | `#Ｄ１Target/BoneMetabolism 骨与代谢分子/Zfp467` | Zfp467采用常用分子名称。 |
| ZT-106 | `#Ｄ１Target/BoneMetabolism 骨与代谢分子/OsteogenicTF 成骨与成脂转录因子` | 用于成骨与成脂转录因子综合入口。 |
| ZT-107 | `#Ｄ１Target/BoneMetabolism 骨与代谢分子/BoneMatrixProtein 骨基质与矿化蛋白` | 用于骨基质与矿化蛋白综合入口。 |
| ZT-108 | `#Ｄ１Target/BoneMetabolism 骨与代谢分子/MetabolicHormone 糖脂代谢激素与受体` | 用于糖脂代谢激素与受体综合入口。 |
| ZT-109 | `#Ｄ１Target/NoncodingRNA 非编码RNA与表观调控` | 用于非编码RNA与表观调控的既有综合入口。 |

### Ｄ２Mechanism

| ID | 标签 | 定义 |
|---|---|---|
| ZT-110 | `#Ｄ２Mechanism/MetabolicReprogramming 代谢重编程/Glycolysis-OXPHOS 糖酵解与氧化磷酸化` | 用于糖酵解与氧化磷酸化综合入口。 |
| ZT-111 | `#Ｄ２Mechanism/MetabolicReprogramming 代谢重编程/LipidAminoAcid 脂质与氨基酸代谢` | 用于脂质与氨基酸代谢综合入口。 |
| ZT-112 | `#Ｄ２Mechanism/CellDifferentiation 细胞分化调控` | 细胞分化作为核心研究过程时使用；只对已发现的“细胞鉴定检测”疑点做定点核查。 |
| ZT-113 | `#Ｄ２Mechanism/CellMigration 细胞迁移与招募` | 用于迁移、募集与归巢的综合入口。 |
| ZT-114 | `#Ｄ２Mechanism/CellSenescence 细胞衰老` | 用于细胞衰老入口。 |
| ZT-115 | `#Ｄ２Mechanism/CellDeath 细胞死亡与自噬` | 用于细胞死亡与自噬综合入口。 |
| ZT-116 | `#Ｄ２Mechanism/CellCommunication 细胞通讯与旁分泌` | 用于细胞通讯与旁分泌综合入口。 |
| ZT-117 | `#Ｄ２Mechanism/Mechanotransduction 力学信号转导` | 用于Mechanotransduction力学转导入口。 |
| ZT-118 | `#Ｄ２Mechanism/OxidativeHypoxia 氧化应激与缺氧调控` | 用于氧化应激与缺氧调控综合入口。 |
| ZT-119 | `#Ｄ２Mechanism/IonMicroenvironment 离子与酸碱微环境` | 用于离子与酸碱微环境综合入口。 |
| ZT-120 | `#Ｄ２Mechanism/AntimicrobialMech 破膜与生物膜瓦解` | 沿用既有破膜及生物膜瓦解范围；对已定位的抗黏附等边界个案核实后处理。 |
| ZT-121 | `#Ｄ２Mechanism/Biomineralization 生物矿化与钙化` | 用于生物矿化与钙化过程入口。 |
| ZT-122 | `#Ｄ２Mechanism/ForeignBodyReaction 异物与植入物免疫反应` | 用于异物与植入物免疫反应入口。 |

### Ｄ３Phenotype

| ID | 标签 | 定义 |
|---|---|---|
| ZT-123 | `#Ｄ３Phenotype/Osteogenesis 成骨与骨再生` | 用于成骨与骨再生综合表型。 |
| ZT-124 | `#Ｄ３Phenotype/BoneResorption 破骨与骨吸收` | 用于破骨与骨吸收综合表型。 |
| ZT-125 | `#Ｄ３Phenotype/Adipogenesis 成脂分化` | 用于成脂分化表型。 |
| ZT-126 | `#Ｄ３Phenotype/EnergyMetabolism 糖脂与能量代谢` | 用于糖脂与能量代谢综合表型。 |
| ZT-127 | `#Ｄ３Phenotype/CartilageHomeostasis 软骨修复与退变` | 用于软骨修复与退变综合表型。 |
| ZT-128 | `#Ｄ３Phenotype/Angiogenesis 促血管生成` | 用于血管生成表型。 |
| ZT-129 | `#Ｄ３Phenotype/Hemostasis 凝血与止血` | 用于凝血与止血综合表型。 |
| ZT-130 | `#Ｄ３Phenotype/Immunomodulation 免疫调控/Macrophage 巨噬细胞极化` | 名称用于Macrophage英文辨识和巨噬极化中文提示；具体状态在原文证据中核对。 |
| ZT-131 | `#Ｄ３Phenotype/Immunomodulation 免疫调控/Anti-Inflammation 抗炎调控` | 用于抗炎表型。 |
| ZT-132 | `#Ｄ３Phenotype/Antibacterial 抗菌与抗生物膜` | 用于抗菌与抗生物膜综合表型。 |
| ZT-133 | `#Ｄ３Phenotype/WoundHealing 创面愈合与抗瘢痕` | 用于创面愈合与抗瘢痕综合表型。 |
| ZT-134 | `#Ｄ３Phenotype/Antitumor 抗肿瘤` | 用于抗肿瘤表型。 |
| ZT-135 | `#Ｄ３Phenotype/Biomechanics 生物力学稳定性` | 用于Biomechanics力学稳定性入口。 |
| ZT-136 | `#Ｄ３Phenotype/Biodegradation 生物降解与吸收` | 用于Biodegradation降解与吸收入口。 |
| ZT-137 | `#Ｄ３Phenotype/ClinicalOutcome 临床疗效与并发症` | 用于临床疗效与并发症范围；疾病间关联的已定位个案单独纠偏。 |

### Ｅ１Method

| ID | 标签 | 定义 |
|---|---|---|
| ZT-138 | `#Ｅ１Method/StudyDesign 研究设计/Comparative 横向对比研究` | 用于Comparative比较研究入口；是否存在比较与比较的证据质量分别判断。 |
| ZT-139 | `#Ｅ１Method/AnimalModel 动物模型/SmallAnimal 小动物模型` | 用于小动物模型入口。 |
| ZT-140 | `#Ｅ１Method/AnimalModel 动物模型/LargeAnimal 大动物模型` | 用于大动物模型入口。 |
| ZT-141 | `#Ｅ１Method/InVitroModel 体外模型/CellCulture 细胞培养体系` | 用于CellCulture细胞培养入口及既有归属。 |
| ZT-142 | `#Ｅ１Method/InVitroModel 体外模型/3D-Organoid 三维培养与类器官` | 三维细胞培养或类器官的综合模型入口。 |
| ZT-143 | `#Ｅ１Method/InVitroModel 体外模型/BiofilmModel 细菌与生物膜模型` | 用于细菌与生物膜模型的综合入口；词表明示其包括普通细菌培养。 |
| ZT-144 | `#Ｅ１Method/InVitroModel 体外模型/SyntheticBone 体外仿真骨与力学模型` | 用于SyntheticBone仿真骨与力学模型入口。 |
| ZT-145 | `#Ｅ１Method/PhysicalTherapy 物理治疗技术/CAP 冷大气等离子体` | 用于CAP缩写及中文提示。 |
| ZT-146 | `#Ｅ１Method/PhysicalTherapy 物理治疗技术/Phototherapy 光热与光动力` | 用于光热与光动力综合干预入口。 |
| ZT-147 | `#Ｅ１Method/Fabrication 制备与加工工艺/3D-Printing 3D打印与增材制造` | 用于3D-Printing及增材制造入口。 |
| ZT-148 | `#Ｅ１Method/Fabrication 制备与加工工艺/Processing 成型加工与灭菌` | 用于加工与灭菌综合方法入口。 |
| ZT-149 | `#Ｅ１Method/Characterization 表征与分析技术/BiomechanicalTest 生物力学测试` | 用于BiomechanicalTest力学测试入口。 |
| ZT-150 | `#Ｅ１Method/Characterization 表征与分析技术/Physicochemical 理化与定量表征` | 用于Physicochemical理化表征入口。 |
| ZT-151 | `#Ｅ１Method/Characterization 表征与分析技术/Simulation 有限元与分子模拟` | 用于Simulation有限元与分子模拟综合方法入口。 |
| ZT-152 | `#Ｅ１Method/Characterization 表征与分析技术/Omics 多组学与测序` | 用于Omics组学与测序入口。 |
| ZT-153 | `#Ｅ１Method/Characterization 表征与分析技术/HistologyImaging 影像与组织学分析` | 用于HistologyImaging影像与组织学综合方法入口。 |

