# Zotero V2.1 十维正交标签规范

本规范由单一受控词表 [taxonomy.json](taxonomy.json)（154 项，稳定 ID `ZT-001`–`ZT-154`）驱动，用于支撑 **Zotero（ZoteroStyle 多级树与彩色胶囊）↔ AI 自动打标 ↔ TextFold 精读分流 ↔ 飞书多维表格同步**。

---

## 一、L0→L4 五层全角前缀架构

10 个顶层维度采用**全角字母 + 全角数字 + 凝练英文词（无空格）**命名，确保侧边栏严格按从顶层研究范式（L0）到底层实验方法（L4）顺序排列：

```text
【L0 元范式与分流】   #Ａ１Type        —— 唯一排外的研究体裁与精读入口（每篇严格 1 个）
          │
          ▼
【L1 临床问题与场景】 #Ｂ１Disease     ∥  #Ｂ２Surgery
          │               (疾病/病理态)     (外科术式与操作)
          ▼
【L2 干预工具箱层】   #Ｃ１Material    ➔  #Ｃ２Carrier     ➔  #Ｃ３Drug
          │               (材料骨架/改性)   (递送载体/剂型)   (药理活性载荷)
          ▼
【L3 因果效应链层】   #Ｄ１Target      ➔  #Ｄ２Mechanism   ➔  #Ｄ３Phenotype
          │               (通路/因子/分子)   (底层细胞/物理机制) (宏观表型/力学/结局)
          ▼
【L4 实验方法与设计】 #Ｅ１Method      —— 研究设计、体外/动物模型、物理治疗与表征技术
```

---

## 二、核心命名与显示规则

1. **ZoteroStyle 胶囊正则兼容**：列视图提取正则 `/#(?:.+\/)*(?:(?=.*[a-zA-Zα-ω\d-])([a-zA-Zα-ω\d-]+)|(.+))/` 以首个空格前的英文/希腊字母/数字/连字符片段渲染彩色胶囊。
   - 多词英文标识符统一使用普通连字符 `-`：`LeFort-I`、`Zn-Fe`、`3D-Organoid`、`3D-Printing`、`Anti-Inflammation`。
   - 半角假名 `ﾉ`（`U+FF89`）专用于复合学术缩写：`u-HAﾉPLLA`、`MAPKﾉERK`、`cAMPﾉPKA`。
   - 严禁写入不可见 Unicode 标签字符（如 `U+E002F`）或其他控制字符。
2. **「就细不就粗」父子互斥**：命中明确三级子标签时，只标三级子标签，禁止同时标注二级母标签（`validate_tags.py` 在 `add` / `replace-managed` 模式下硬拦截）。仅在综述、泛指多体系或原文未限定具体亚型时使用二级母标签。
3. **MeSH Major Topic 核心贡献原则**：每篇通常精选 **2–9 个**核心 `#` 标签，只标文章研究重心；无关维度留空，不把常规鉴定或背景提及机械扩标。
4. **跨文献口径与标记规范**：
   - AI 打标标记：统一附带平铺标签 `~ZTag-V2`（纯 ASCII，不进 `#` 树与 `/` 状态）。
   - 阅读状态与用户标签：至多保留 1 个状态标签（`/Done` > `/reading` > `/unread`），普通维护与全量重标均完整保留既有用户标签、集合归属、附件与批注。
   - 严禁在未绑定父条目的孤立 PDF 上先打标后识别元数据；跳过独立 `note`、插件配置条目及批注子项。

---

## 三、不同体裁的稀疏激活模板

| 文献体裁 (`#Ａ１Type`) | 典型激活维度 | 留空或谨慎边界 |
|---|---|---|
| `Article/Mechanistic` | `#Ｂ１Disease` + `#Ｄ１Target` + `#Ｄ２Mechanism` + `#Ｄ３Phenotype` + `#Ｅ１Method` | `#Ｃ１Material`/`#Ｃ２Carrier`/`#Ｂ２Surgery` 天然留空；常规三系分化鉴定不标 `CellDifferentiation` |
| `Article/Biomaterial` | `#Ｃ１Material` + `#Ｃ２Carrier`/`#Ｃ３Drug` + `#Ｂ１Disease` + `#Ｄ３Phenotype` + `#Ｄ２Mechanism`/`#Ｅ１Method` | 单纯 CFU/抑菌圈只标 `Antibacterial`，不标 `AntimicrobialMech` |
| `Article/DeviceEvaluation` | `#Ｂ２Surgery`/`#Ｂ１Disease` + `#Ｃ１Material` + `#Ｄ３Phenotype/Biomechanics`（/降解/成骨）+ `#Ｅ１Method` | 结构性固定板钉 `#Ｃ２Carrier`、`#Ｄ１Target` 留空 |
| `Clinical/...`（6 选 1） | 按当前论文实际设计选 1 项 + `#Ｂ１Disease`/`#Ｂ２Surgery` + `#Ｃ１Material`/`#Ｃ３Drug` + `ClinicalOutcome` | 横断面流行病学关联不标 `ClinicalOutcome`；`CaseControl` 优先于 `Retrospective` |
| `Computational/...` | `FEA` 配术式/疾病/材料 + `Biomechanics` + `Simulation`；`Bioinformatics` 配疾病/靶点/组学 | 不虚构实体动物/细胞模型标签 |
| `Guideline` / `Protocol` / `ProductInfo` / `Book` / `Commentary` / `Humanities` | 准确标 `#Ａ１Type` 及直接覆盖的疾病/材料/方法范围 | 不强凑分子通路与机制标签 |

---

## 四、受控词表更新检查清单

词表维护以 `taxonomy.json` 为唯一源码：
1. 新增词分配新递增 `ZT-xxx` ID，明确定义、正交边界与 `aliases`；合并或更名保持原稳定 ID 并将旧路径写入 `rename_map`；检查 ZoteroStyle 胶囊切片无空格截断。
2. 同步生成本文件 [ZOTERO_TAG_SPEC.md](ZOTERO_TAG_SPEC.md) 与飞书字段模板 [structured_fields.json](structured_fields.json)。
3. 运行全套单测 `python3 -m unittest discover -s skills/zotero-tagging/tests -v` 验证唯一性、`rename_map` 完备性与胶囊显示。

---

## 五、全量受控词表（154 项，10 维）

### 1. `#Ａ１Type`（L0：精读分流与文献体裁，22 项）

每篇严格有且仅有 1 个，按主导研究贡献与当前论文设计选择。

| ID | 标签 | 定义与边界 |
|---|---|---|
| ZT-001 | `#Ａ１Type/Article 论著/Mechanistic 机制研究` | 论著的主导贡献为分子、细胞或生理调控机制解析；交叉设计以机制发现为核心时优先选此类。 |
| ZT-002 | `#Ａ１Type/Article 论著/Biomaterial 生物材料研究` | 论著的主导贡献为材料合成、结构改性、载药配方设计及其体外或动物生物效应评价。 |
| ZT-003 | `#Ａ１Type/Article 论著/DeviceEvaluation 器械临床前评价` | 论著的主导贡献为成熟医疗器械、接骨板钉或植入系统在力学、降解、生物相容性或动物手术中的临床前评价。 |
| ZT-004 | `#Ａ１Type/Clinical 临床研究/RCT 随机对照试验` | 临床随机对照试验（依据当前论文实际采取的随机分组干预设计判定）。 |
| ZT-005 | `#Ａ１Type/Clinical 临床研究/Prospective 前瞻性临床研究` | 前瞻性临床观察或队列随访研究（不含明确随机对照试验或病例对照研究；RCT 衍生前瞻随访按当前队列分析归入此类）。 |
| ZT-006 | `#Ａ１Type/Clinical 临床研究/Retrospective 回顾性临床研究` | 回顾性临床病历或队列分析（明确按病例-对照匹配选择研究对象时归入 CaseControl）。 |
| ZT-007 | `#Ａ１Type/Clinical 临床研究/CrossSectional 横断面研究` | 单一时间点的临床现况调查、患病率调查或横断面相关性分析。 |
| ZT-008 | `#Ａ１Type/Clinical 临床研究/CaseReport 病例报告与系列` | 个案病例报告或临床病例系列总结。 |
| ZT-009 | `#Ａ１Type/Review 综述` | 一般性叙述综述；具备完整系统检索策略或定量合并分析时改用 SystematicReview 或 MetaAnalysis。 |
| ZT-010 | `#Ａ１Type/SystematicReview 系统综述` | 遵循明确检索与纳排流程的定性系统综述；包含定量 Meta 合并分析时使用子标签 MetaAnalysis。 |
| ZT-011 | `#Ａ１Type/SystematicReview 系统综述/MetaAnalysis Meta分析` | 包含统计学效应量合并的定量系统综述与 Meta 分析。 |
| ZT-012 | `#Ａ１Type/Computational 计算与仿真/FEA 有限元分析` | 以有限元应力应变建模、生物力学仿真或拓扑优化为主体贡献的研究。 |
| ZT-013 | `#Ａ１Type/Computational 计算与仿真/Bioinformatics 生物信息与分子模拟` | 以生信数据挖掘、分子对接或分子动力学模拟为主体贡献的研究。 |
| ZT-014 | `#Ａ１Type/Guideline 指南与规范/ClinicalGuideline 临床诊疗指南` | 临床诊疗指南或临床专家共识。 |
| ZT-015 | `#Ａ１Type/Guideline 指南与规范/Standard 技术标准与报告规范` | 技术检测标准、ISO/ASTM 行业规范、学术命名共识或报告规范（如 CONSORT、STROBE、ARRIVE）。 |
| ZT-016 | `#Ａ１Type/Protocol 实验方案与规程` | 可直接复现分步执行的实验方法学文章、SOP 或标准化操作规程。 |
| ZT-017 | `#Ａ１Type/ProductInfo 产品资料` | 商业器械或材料的产品手册、使用说明书、产品技术白皮书及注册摘要（如 FDA 510(k)）。 |
| ZT-018 | `#Ａ１Type/Book 专著与教材` | 学术专著、教材或书籍独立章节。 |
| ZT-019 | `#Ａ１Type/Commentary 述评与观点` | 学术述评、编者按、观点文章（Perspective）或读者来信。 |
| ZT-020 | `#Ａ１Type/Humanities 科技人文与方法论` | 科研方法论探讨、医学史、科学哲学或文献计量与学术写作方法类文献。 |
| ZT-021 | `#Ａ１Type/Humanities 科技人文与方法论/Bioethics 生命伦理与治理` | 医学伦理、动物实验伦理、AI 科研伦理及学术治理相关文献。 |
| ZT-154 | `#Ａ１Type/Clinical 临床研究/CaseControl 病例对照` | 按疾病或结局分组选择病例与对照并回顾比较暴露因素或危险因素的研究（优先于笼统的 Retrospective）。 |

### 2. `#Ｂ１Disease`（L1：临床疾病与病理状态，27 项）

| ID | 标签 | 定义与边界 |
|---|---|---|
| ZT-022 | `#Ｂ１Disease/MRONJ 药物相关颌骨坏死` | 药物相关性颌骨坏死总类（综述或同时覆盖多类药物；明确单指双膦酸盐或地诺单抗时使用三级子标签）。 |
| ZT-023 | `#Ｂ１Disease/MRONJ 药物相关颌骨坏死/BRONJ 双膦酸盐相关颌骨坏死` | 双膦酸盐类药物（如唑来膦酸）诱发的颌骨坏死。 |
| ZT-024 | `#Ｂ１Disease/MRONJ 药物相关颌骨坏死/DRONJ 地诺单抗相关颌骨坏死` | 地诺单抗诱发的颌骨坏死。 |
| ZT-025 | `#Ｂ１Disease/ONFH 股骨头坏死` | 股骨头坏死总类（未区分激素性/缺血性或综述时使用；明确病因时优先三级子标签）。 |
| ZT-026 | `#Ｂ１Disease/ONFH 股骨头坏死/SONFH 激素性股骨头坏死` | 糖皮质激素诱导的股骨头坏死。 |
| ZT-027 | `#Ｂ１Disease/ONFH 股骨头坏死/IschemicONFH 缺血性股骨头坏死` | 外伤或血供障碍所致的缺血性股骨头坏死。 |
| ZT-028 | `#Ｂ１Disease/TMD 颞下颌关节病` | 颞下颌关节紊乱病总类（明确属于颞下颌关节骨关节炎时使用子标签 TMJ-OA）。 |
| ZT-029 | `#Ｂ１Disease/TMD 颞下颌关节病/TMJ-OA 颞下颌关节骨关节炎` | 颞下颌关节骨关节炎（含髁突软骨退变与软骨下骨改建）。 |
| ZT-030 | `#Ｂ１Disease/Osteoarthritis 骨关节炎` | 膝、髋或全身骨关节炎（颞下颌关节骨关节炎归入 TMJ-OA）。 |
| ZT-031 | `#Ｂ１Disease/Osteoporosis 骨质疏松症` | 系统性或绝经后/老年性骨质疏松症与骨量丢失模型。 |
| ZT-032 | `#Ｂ１Disease/Periodontitis 牙周炎` | 慢性/侵袭性牙周炎及牙槽骨吸收（种植体周围病变归入 Peri-Implantitis）。 |
| ZT-033 | `#Ｂ１Disease/Peri-Implantitis 种植体周围炎` | 口腔种植体周围黏膜炎及种植体周围骨吸收。 |
| ZT-034 | `#Ｂ１Disease/Endodontics 牙体牙髓病` | 龋病、牙髓炎、根尖周炎及牙体硬组织缺损修复相关研究。 |
| ZT-035 | `#Ｂ１Disease/DentofacialDeformity 牙颌面畸形` | 上下颌发育性/骨性畸形、偏颌、反颌及正颌手术所涉临床与动物研究（颅缝早闭除外）。 |
| ZT-036 | `#Ｂ１Disease/Craniosynostosis 颅缝早闭` | 颅缝早闭及先天性颅颌面骨缝早闭畸形。 |
| ZT-037 | `#Ｂ１Disease/CraniofacialFracture 颅颌面骨折` | 颅颌面骨骨折总类（仅在综述或同时跨上下颌/中面部多部位且不细拆时使用）。 |
| ZT-038 | `#Ｂ１Disease/CraniofacialFracture 颅颌面骨折/MandibularFracture 下颌骨骨折` | 下颌骨体部、角部、颏部或髁突骨折（正颌医源性截骨固定归入 Orthognathic，不标骨折）。 |
| ZT-039 | `#Ｂ１Disease/CraniofacialFracture 颅颌面骨折/MidfacialFracture 面中部与眶壁骨折` | 颧骨复合体、上颌骨 Le Fort、鼻眶筛及眶壁骨折。 |
| ZT-040 | `#Ｂ１Disease/BoneDefect 骨缺损与拔牙窝创伤` | 颅骨/股骨/下颌节段或临界骨缺损、骨不连及拔牙窝创伤愈合模型。 |
| ZT-041 | `#Ｂ１Disease/Infection 感染性疾病/OralInfection 口腔细菌与生物膜感染` | 口腔感染、牙菌斑生物膜、根管感染及口腔致病菌研究。 |
| ZT-042 | `#Ｂ１Disease/Infection 感染性疾病/ImplantInfection 手术与植入物感染` | 骨科或外科植入物相关感染、骨髓炎及术后切口深部感染（限感染为明确研究对象时使用）。 |
| ZT-043 | `#Ｂ１Disease/Wound 皮肤黏膜创面` | 皮肤、糖尿病创面或口腔黏膜缺损创面修复研究。 |
| ZT-044 | `#Ｂ１Disease/Scar 病理性瘢痕与纤维化` | 增生性瘢痕、瘢痕疙瘩及组织器官纤维化（含肾/肝/肺纤维化 UUO 等）。 |
| ZT-045 | `#Ｂ１Disease/MetabolicDisorder 糖脂代谢疾病` | 糖尿病、高脂血症、肥胖等糖脂代谢异常疾病（仅关注糖尿病创面修复时可与 Wound 联用）。 |
| ZT-046 | `#Ｂ１Disease/AutoimmuneDisease 自身免疫与风湿病` | 类风湿关节炎、系统性红斑狼疮等自身免疫与风湿性疾病。 |
| ZT-047 | `#Ｂ１Disease/CardiovascularDisease 心血管疾病` | 动脉粥样硬化、心肌缺血或血管疾病相关研究。 |
| ZT-048 | `#Ｂ１Disease/Tumor 肿瘤` | 骨肉瘤、口腔鳞癌等恶性肿瘤机制与治疗研究。 |

### 3. `#Ｂ２Surgery`（L1：外科术式与临床操作，8 项）

| ID | 标签 | 定义与边界 |
|---|---|---|
| ZT-049 | `#Ｂ２Surgery/Orthognathic 正颌外科` | 正颌外科总类（用于正颌综述、双颌手术综合评价或未具体区分截骨术式时）。 |
| ZT-050 | `#Ｂ２Surgery/Orthognathic 正颌外科/SSRO 矢状劈开术` | 下颌升支矢状劈开截骨术。 |
| ZT-051 | `#Ｂ２Surgery/Orthognathic 正颌外科/LeFort-I 截骨术` | 上颌 Le Fort I 型水平截骨术。 |
| ZT-052 | `#Ｂ２Surgery/Orthognathic 正颌外科/Genioplasty 颏成形术` | 颏成形术（水平截骨颏部前移/后退/整形术）。 |
| ZT-053 | `#Ｂ２Surgery/Orthognathic 正颌外科/DO 牵张成骨` | 颌骨或颅骨牵张成骨术及骨搬运术。 |
| ZT-054 | `#Ｂ２Surgery/MaxillofacialFixation 颌面创伤与重建内固定` | 颌面创伤骨折、正颌/肿瘤术后缺损的坚强或可吸收内固定操作（纯正颌发育畸形临床/动物研究勿混入此标签）。 |
| ZT-055 | `#Ｂ２Surgery/ImplantSurgery 牙槽与种植外科` | 牙种植外科、引导骨再生（GBR）、上颌窦提升及牙槽外科手术。 |
| ZT-056 | `#Ｂ２Surgery/OrthopedicFixation 骨科内固定与关节置换` | 四肢脊柱骨折内固定、骨科人工关节置换及骨科植入手术。 |

### 4. `#Ｃ１Material`（L2：工程材料骨架与表面改性，21 项）

| ID | 标签 | 定义与边界 |
|---|---|---|
| ZT-057 | `#Ｃ１Material/ResorbablePolymer 可吸收高分子` | 可吸收高分子总类（仅用于综述或未限定具体聚合单体的聚合物支架；明确成分时使用三级子标签）。 |
| ZT-058 | `#Ｃ１Material/ResorbablePolymer 可吸收高分子/PLLA` | 左旋聚乳酸均聚物及左旋聚乳酸基材料。 |
| ZT-059 | `#Ｃ１Material/ResorbablePolymer 可吸收高分子/PDLLA 乳酸共聚物` | 外消旋聚乳酸、D,L-丙交酯立体共聚物（如 70/30 P(L/DL)LA）及含三亚甲基碳酸酯（TMC）等乳酸基共聚物；商业品牌 SonicWeld、Resorb-X、BioSorb FX、Inion CPS 归此类。 |
| ZT-060 | `#Ｃ１Material/ResorbablePolymer 可吸收高分子/PLGA` | 聚乳酸-羟基乙酸共聚物（PLLA/PGA 共聚物）；商业品牌 LactoSorb 归此类（按主聚合骨架归标）。 |
| ZT-061 | `#Ｃ１Material/ResorbablePolymer 可吸收高分子/PGA` | 聚乙醇酸/聚羟基乙酸均聚物。 |
| ZT-062 | `#Ｃ１Material/ResorbablePolymer 可吸收高分子/PCL` | 聚己内酯及其作为主导骨架的复合体系。 |
| ZT-063 | `#Ｃ１Material/ResorbablePolymer 可吸收高分子/u-HAﾉPLLA` | 未煅烧羟基磷灰石颗粒增强左旋聚乳酸复合材料；商业品牌 Osteotrans 归此类。 |
| ZT-064 | `#Ｃ１Material/BiodegradableMetal 可降解金属` | 可降解金属总类（综述或同时囊括多系可降解金属时使用；明确单系基体时使用三级子标签）。 |
| ZT-065 | `#Ｃ１Material/BiodegradableMetal 可降解金属/Mg 镁基` | 以镁为主体基体的纯镁及镁合金材料（如 WE43、ZK60、AZ31、Mg-Zn-Ca）。 |
| ZT-066 | `#Ｃ１Material/BiodegradableMetal 可降解金属/Zn-Fe 锌基与铁基` | 以锌或铁为主体基体的纯金属及合金材料（合金按主基体元素归类，如 Zn-1Mg 仅归此类而不归镁基）。 |
| ZT-067 | `#Ｃ１Material/Titanium 钛与钛合金` | 不可吸收钛及钛合金材料（纯钛、Ti-6Al-4V、多孔钛网等，含表面改性对比对照）。 |
| ZT-068 | `#Ｃ１Material/Hydrogel 水凝胶` | 水凝胶总类（综述或泛指未区分子类的水凝胶体系时使用；已明确具体体系时使用三级子标签）。 |
| ZT-069 | `#Ｃ１Material/Hydrogel 水凝胶/GelMA` | 甲基丙烯酰化明胶水凝胶体系。 |
| ZT-070 | `#Ｃ１Material/Hydrogel 水凝胶/NaturalHydrogel 天然高分子水凝胶` | 壳聚糖、透明质酸、海藻酸钠、丝素蛋白、胶原、脱细胞基质（dECM）及葡聚糖等天然高分子水凝胶。 |
| ZT-071 | `#Ｃ１Material/Hydrogel 水凝胶/SmartHydrogel 合成与响应型水凝胶` | PEG、PVA、F127、pNIPAM 等合成高分子水凝胶及 pH/ROS/光/温/磁响应智能水凝胶。 |
| ZT-072 | `#Ｃ１Material/MOF 金属有机框架` | 金属有机框架总类（UiO-66、MIL、Cu-MOF 等非 ZIF-8 类 MOF）。 |
| ZT-073 | `#Ｃ１Material/MOF 金属有机框架/ZIF-8` | 沸石咪唑酯骨架-8 金属有机框架材料。 |
| ZT-074 | `#Ｃ１Material/Bioceramic 生物陶瓷与活性玻璃` | 羟基磷灰石（HA）、β-TCP、硅酸钙、生物活性玻璃、ACP 等无机生物陶瓷与骨水泥材料。 |
| ZT-075 | `#Ｃ１Material/Nanomaterial 无机与复合纳米材料` | 碳纳米管、氧化石墨烯、MXene、黑磷、二氧化钛纳米管及无机功能纳米颗粒材料。 |
| ZT-076 | `#Ｃ１Material/SurfaceModification 表面改性/Coating 表面涂层` | 金属/陶瓷/高分子基材表面的微弧氧化（MAO）、阳极氧化、溶胶凝胶、生物矿化或抗菌涂层（若同时修饰具体基体材料，可与基材标签联用）。 |
| ZT-077 | `#Ｃ１Material/SurfaceModification 表面改性/SurfaceTopography 表面形貌与电荷修饰` | 材料表面的纳米形貌构建（微纳沟槽、纳米管阵列）、润湿性调控或表面电荷/化学接枝修饰。 |

### 5. `#Ｃ２Carrier`（L2：递送载体与制剂剂型，5 项）

| ID | 标签 | 定义与边界 |
|---|---|---|
| ZT-078 | `#Ｃ２Carrier/Scaffold 组织工程与控释支架` | 承担三维空间支撑或药物局部缓释功能的多孔支架、水凝胶敷料、电纺纤维膜及复合微球（纯接骨板钉等结构固定器械本维度留空）。 |
| ZT-079 | `#Ｃ２Carrier/Nanocarrier 纳米递送载体` | 脂质体、胶束、介孔硅、纳米粒及金属有机框架等纳米尺度递送载体。 |
| ZT-080 | `#Ｃ２Carrier/tFNAs 四面体核酸` | 四面体框架核酸载体平台。 |
| ZT-081 | `#Ｃ２Carrier/EVs 细胞外囊泡` | 细胞外囊泡、外泌体、凋亡小体及工程化囊泡递送体系。 |
| ZT-082 | `#Ｃ２Carrier/CellCarrier 细胞与血小板载体` | 以活细胞（如 BMSC、MSC）或富血小板浓缩物（PRP、PRF、CGF）作为治疗单元或递送载体（无细胞条件培养基不标此类）。 |

### 6. `#Ｃ３Drug`（L2：活性药物与生物载荷，9 项）

| ID | 标签 | 定义与边界 |
|---|---|---|
| ZT-083 | `#Ｃ３Drug/Antiresorptive 抗骨吸收药/BPs 双膦酸盐` | 唑来膦酸、阿仑膦酸等双膦酸盐药物（仅当药物本身为治疗/药理/毒性评价对象时标注；仅作动物造模诱导剂或病例既往史时不标）。 |
| ZT-084 | `#Ｃ３Drug/Antiresorptive 抗骨吸收药/Denosumab 地诺单抗` | 地诺单抗/RANKL 单抗（仅当药物本身为治疗/药理/毒性评价对象时标注；仅作背景造模/既往史时不标）。 |
| ZT-085 | `#Ｃ３Drug/Biologics 蛋白与抗体药物/TCZ 托珠单抗` | IL-6 受体拮抗剂托珠单抗。 |
| ZT-086 | `#Ｃ３Drug/Biologics 蛋白与抗体药物/GrowthFactor 重组生长因子与多肽` | 作为外源活性载荷给药的重组生长因子、趋化因子、活性多肽及抗体蛋白药物（内源分泌检测归入 D1）。 |
| ZT-087 | `#Ｃ３Drug/SmallMolecule 小分子化学药` | 化学合成小分子药物、靶向抑制剂、激素激动剂及化学活性分子（如地塞米松、二甲双胍、AMD3100）。 |
| ZT-088 | `#Ｃ３Drug/NucleicAcid 核酸药物` | 作为外源治疗载荷递送的 siRNA、miRNA 模拟物/抑制剂、ASO、质粒 DNA 或 mRNA（内源机制靶点归入 D1 NoncodingRNA）。 |
| ZT-089 | `#Ｃ３Drug/NaturalProduct 天然产物与中药成分` | 天然植物提取物、中药单体及生物碱/黄酮/多酚类天然活性分子（如白藜芦醇、姜黄素、淫羊藿苷、丹参酮）。 |
| ZT-090 | `#Ｃ３Drug/Antibiotic 抗生素与抗菌药` | 抗生素（万古霉素、庆大霉素、甲硝唑等）与临床小分子抗菌剂（氯己定、季铵盐等）。 |
| ZT-091 | `#Ｃ３Drug/GasTherapy 气体与活性氧分子` | 作为外源治疗干预递送的活性气体分子或产气/产 ROS 前体（CO、NO、H2S、H2、O2、声敏剂/光敏剂活性氧体系）。 |

### 7. `#Ｄ１Target`（L3：分子靶点与信号通路，18 项）

| ID | 标签 | 定义与边界 |
|---|---|---|
| ZT-092 | `#Ｄ１Target/Pathway 信号通路/JAK-STAT` | JAK-STAT 信号通路及相关调控轴。 |
| ZT-093 | `#Ｄ１Target/Pathway 信号通路/NF-κB-RANKL` | NF-κB 及 RANK/RANKL/OPG 信号通路与破骨/炎症下游轴。 |
| ZT-094 | `#Ｄ１Target/Pathway 信号通路/MAPKﾉERK` | MAPK、ERK1/2、p38 及 JNK 丝裂原活化蛋白激酶信号通路。 |
| ZT-095 | `#Ｄ１Target/Pathway 信号通路/PI3K-Akt-mTOR` | PI3K-Akt-mTOR 信号通路及相关生存/自噬/合成调控轴。 |
| ZT-096 | `#Ｄ１Target/Pathway 信号通路/Wnt-BMP-TGFβ` | Wnt/β-catenin、BMP/Smad 及 TGF-β 经典成骨/成纤维分化信号通路（涵盖任一核心通路）。 |
| ZT-097 | `#Ｄ１Target/Pathway 信号通路/Hippo-YAP` | Hippo-YAP/TAZ 力学与细胞增殖调控通路。 |
| ZT-098 | `#Ｄ１Target/Pathway 信号通路/cAMPﾉPKA` | cAMP-PKA-CREB 及 PTH 下游环磷酸腺苷信号轴。 |
| ZT-099 | `#Ｄ１Target/Pathway 信号通路/InnateImmune 固有免疫` | TLR（TLR4/MyD88）、NLRP3 炎症小体及 cGAS-STING 固有免疫感知通路。 |
| ZT-100 | `#Ｄ１Target/Pathway 信号通路/Nrf2` | Keap1-Nrf2-ARE 抗氧化应激与铁死亡防御通路。 |
| ZT-101 | `#Ｄ１Target/Cytokine 细胞因子与生长因子/IL-6` | 白介素-6（IL-6）及其经典/反式受体（IL-6R/gp130）靶点分子。 |
| ZT-102 | `#Ｄ１Target/Cytokine 细胞因子与生长因子/InflammatoryCytokine 促炎因子 (IL-1-TNFα)` | TNF-α、IL-1β、IL-17 等核心促炎细胞因子与趋化因子。 |
| ZT-103 | `#Ｄ１Target/Cytokine 细胞因子与生长因子/AngiogenicFactor 促血管生长因子 (VEGF-FGF)` | 内源性 VEGF、FGF、PDGF、HIF-1α 等促血管生成细胞因子与调控靶点（作外源药物载荷给药时另标 C3）。 |
| ZT-104 | `#Ｄ１Target/BoneMetabolism 骨与代谢分子/OCN 骨钙素` | 骨钙素（OCN/BGLAP）及相关内分泌骨-能量交互轴（仅当作为核心靶点/激素机制研究而非单纯成骨常规染色指标时标注）。 |
| ZT-105 | `#Ｄ１Target/BoneMetabolism 骨与代谢分子/Zfp467` | 锌指蛋白 Zfp467（决定 MSC 成骨/成脂分化平衡的关键转录共调控因子）。 |
| ZT-106 | `#Ｄ１Target/BoneMetabolism 骨与代谢分子/OsteogenicTF 成骨与成脂转录因子` | 决定细胞谱系定向的关键转录因子（如 Runx2、Osterix/Sp7、Sox9、PPARγ、NFATc1）。 |
| ZT-107 | `#Ｄ１Target/BoneMetabolism 骨与代谢分子/BoneMatrixProtein 骨基质与矿化蛋白` | 核心骨/牙基质矿化与结构蛋白作为机制研究靶点（如 COL1A1、OPN、BSP、ALP、DMP1）。 |
| ZT-108 | `#Ｄ１Target/BoneMetabolism 骨与代谢分子/MetabolicHormone 糖脂代谢激素与受体` | 胰岛素/IGF-1、GLP-1、瘦素（Leptin）、脂联素等糖脂代谢激素及其受体靶点。 |
| ZT-109 | `#Ｄ１Target/NoncodingRNA 非编码RNA与表观调控` | 作为内源调控因子的非编码 RNA（miRNA、lncRNA、circRNA）及表观遗传调控修饰（甲基化、乙酰化、乳酸化、m6A）。 |

### 8. `#Ｄ２Mechanism`（L3：生物学与物理化学机制，13 项）

| ID | 标签 | 定义与边界 |
|---|---|---|
| ZT-110 | `#Ｄ２Mechanism/MetabolicReprogramming 代谢重编程/Glycolysis-OXPHOS 糖酵解与氧化磷酸化` | 糖酵解与线粒体氧化磷酸化（OXPHOS）代谢重编程、线粒体自噬及线粒体动力学（仅当代谢转变为核心机制时标注）。 |
| ZT-111 | `#Ｄ２Mechanism/MetabolicReprogramming 代谢重编程/LipidAminoAcid 脂质与氨基酸代谢` | 脂肪酸氧化（FAO）、脂滴代谢、胆固醇及氨基酸（谷氨酰胺等）代谢调控机制。 |
| ZT-112 | `#Ｄ２Mechanism/CellDifferentiation 细胞分化调控` | 干预直接改变成骨、成软骨、破骨、内皮或成纤维细胞分化命运的核心机制研究（仅作常规细胞身份三系分化鉴定时不标）。 |
| ZT-113 | `#Ｄ２Mechanism/CellMigration 细胞迁移与招募` | 干细胞归巢、成骨/内皮细胞迁移募集、趋化因子招募（如 SDF-1/CXCR4）。 |
| ZT-114 | `#Ｄ２Mechanism/CellSenescence 细胞衰老` | 细胞衰老、SASP 衰老相关分泌表型、端粒损伤及细胞周期阻滞机制。 |
| ZT-115 | `#Ｄ２Mechanism/CellDeath 细胞死亡与自噬` | 调控性细胞死亡及稳态机制（凋亡、自噬、铁死亡、铜死亡、细胞焦亡、坏死性凋亡）。 |
| ZT-116 | `#Ｄ２Mechanism/CellCommunication 细胞通讯与旁分泌` | 外泌体/囊泡介导的细胞间通讯、旁分泌耦合（如 H 型血管-成骨耦合）及条件培养液机制。 |
| ZT-117 | `#Ｄ２Mechanism/Mechanotransduction 力学信号转导` | 细胞外基质刚度、流体剪切力、应力拉伸或 Piezo1/整合素/粘着斑介导的力学信号转导。 |
| ZT-118 | `#Ｄ２Mechanism/OxidativeHypoxia 氧化应激与缺氧调控` | ROS 清除/过载调控、线粒体氧化应激稳态及组织低氧（Hypoxia）微环境改善机制。 |
| ZT-119 | `#Ｄ２Mechanism/IonMicroenvironment 离子与酸碱微环境` | 可降解材料释出的镁/锌/钙/硅等离子浓度及局部酸性/碱性 pH 微环境调控生物学效应的机制。 |
| ZT-120 | `#Ｄ２Mechanism/AntimicrobialMech 破膜与生物膜瓦解` | 材料或药物对细菌细胞膜破坏、胞内物质泄漏、群体感应（QS）抑制、抗黏附电荷排斥或成熟生物膜 EPS 基质瓦解机理（单纯抑菌圈/CFU 计数仅标 D3 Antibacterial）。 |
| ZT-121 | `#Ｄ２Mechanism/Biomineralization 生物矿化与钙化` | 仿生矿化、磷灰石成核生长、胶原纤维内/外矿化沉积及病理性血管/软骨钙化机制。 |
| ZT-122 | `#Ｄ２Mechanism/ForeignBodyReaction 异物与植入物免疫反应` | 植入物触发的异物巨细胞反应（FBGC）、纤维包囊形成、补体激活与材料降解免疫相容性机制。 |

### 9. `#Ｄ３Phenotype`（L3：宏观表型、力学与临床结局，15 项）

| ID | 标签 | 定义与边界 |
|---|---|---|
| ZT-123 | `#Ｄ３Phenotype/Osteogenesis 成骨与骨再生` | 骨形成、骨缺损再生修复、骨整合及种植体周围骨量提升效应。 |
| ZT-124 | `#Ｄ３Phenotype/BoneResorption 破骨与骨吸收` | 破骨细胞骨吸收活性、骨侵蚀、骨溶解及抑制异常骨吸收效应。 |
| ZT-125 | `#Ｄ３Phenotype/Adipogenesis 成脂分化` | 骨髓间充质干细胞成脂向分化及骨髓脂肪化表型。 |
| ZT-126 | `#Ｄ３Phenotype/EnergyMetabolism 糖脂与能量代谢` | 全身血糖、胰岛素敏感性、脂代谢稳态及能量消耗等系统性代谢表型。 |
| ZT-127 | `#Ｄ３Phenotype/CartilageHomeostasis 软骨修复与退变` | 透明软骨再生修复、细胞外基质维持及软骨退变/骨关节炎进展延缓。 |
| ZT-128 | `#Ｄ３Phenotype/Angiogenesis 促血管生成` | 新生血管形成、微血管密度提升、内皮管腔形成及组织血供改善。 |
| ZT-129 | `#Ｄ３Phenotype/Hemostasis 凝血与止血` | 快速止血、血小板聚集、凝血瀑布激活及封闭创面渗血效应。 |
| ZT-130 | `#Ｄ３Phenotype/Immunomodulation 免疫调控/Macrophage 巨噬细胞极化` | 巨噬细胞由促炎 M1 表型向促修复 M2 表型重塑及极化比例调控。 |
| ZT-131 | `#Ｄ３Phenotype/Immunomodulation 免疫调控/Anti-Inflammation 抗炎调控` | 系统性或局部组织炎症水平下降、炎性细胞浸润减少及促炎微环境缓解。 |
| ZT-132 | `#Ｄ３Phenotype/Antibacterial 抗菌与抗生物膜` | 抑制浮游菌增殖、降低细菌黏附或清除生物膜感染（常规 CFU/抑菌圈评价归此表型）。 |
| ZT-133 | `#Ｄ３Phenotype/WoundHealing 创面愈合与抗瘢痕` | 皮肤或口腔黏膜缺损再上皮化加速、肉芽重建及减少病理性瘢痕增生与纤维化。 |
| ZT-134 | `#Ｄ３Phenotype/Antitumor 抗肿瘤` | 肿瘤细胞杀伤、肿瘤生长抑制或术后防复发联合骨修复效应。 |
| ZT-135 | `#Ｄ３Phenotype/Biomechanics 生物力学稳定性` | 接骨板/螺钉、支架或修复体维持力学强度、刚度、抗扭转或骨骼空间稳定性的功能结局。 |
| ZT-136 | `#Ｄ３Phenotype/Biodegradation 生物降解与吸收` | 植入材料、可吸收骨钉或水凝胶随时间发生的体外/体内水解、腐蚀降解速率及组织替代结局。 |
| ZT-137 | `#Ｄ３Phenotype/ClinicalOutcome 临床疗效与并发症` | 临床随访中的术后愈合率、骨骼稳定性、疼痛/开口度改善、植入物取出率及并发症（不用于横断面纯相关性或流行病学关联研究）。 |

### 10. `#Ｅ１Method`（L4：研究设计、实验模型与表征技术，16 项）

| ID | 标签 | 定义与边界 |
|---|---|---|
| ZT-138 | `#Ｅ１Method/StudyDesign 研究设计/Comparative 横向对比研究` | 以多组体系、多材料或不同固定构型横向头对头比较为主设计的实证研究（普通单一对照实验不滥用）。 |
| ZT-139 | `#Ｅ１Method/AnimalModel 动物模型/SmallAnimal 小动物模型` | 以小鼠、大鼠、豚鼠或兔等小型实验动物为主体的体内实验研究。 |
| ZT-140 | `#Ｅ１Method/AnimalModel 动物模型/LargeAnimal 大动物模型` | 以山羊、绵羊、犬、猪或非人灵长类等大动物为主体的临床前体内实验研究。 |
| ZT-141 | `#Ｅ１Method/InVitroModel 体外模型/CellCulture 细胞培养体系` | 采用常规二维（2D）原代细胞或永生化细胞系的体外细胞学实验体系（如 BMSC、RAW264.7、HUVEC、MC3T3-E1）。 |
| ZT-142 | `#Ｅ１Method/InVitroModel 体外模型/3D-Organoid 三维培养与类器官` | 将活细胞包埋于三维水凝胶/多孔微环境进行立体培养，或使用多细胞自组织形成器官结构特征的类器官/微球体体外模型（单纯微CT 3D 重建图像不标此项）。 |
| ZT-143 | `#Ｅ１Method/InVitroModel 体外模型/BiofilmModel 细菌与生物膜模型` | 体外浮游菌培养、多菌种共培养或单/多菌生物膜形成与清除实验模型。 |
| ZT-144 | `#Ｅ１Method/InVitroModel 体外模型/SyntheticBone 体外仿真骨与力学模型` | 采用聚氨酯仿真颌骨（如 Synbone、Sawbones）或离体动物/尸体骨骼开展的体外模拟固定力学模型。 |
| ZT-145 | `#Ｅ１Method/PhysicalTherapy 物理治疗技术/CAP 冷大气等离子体` | 冷大气等离子体（CAP）及等离子体活化水（PAW）物理干预技术。 |
| ZT-146 | `#Ｅ１Method/PhysicalTherapy 物理治疗技术/Phototherapy 光热与光动力` | 近红外光热治疗（PTT）与光敏抗菌/抗肿瘤光动力治疗（PDT）物理干预技术。 |
| ZT-147 | `#Ｅ１Method/Fabrication 制备与加工工艺/3D-Printing 3D打印与增材制造` | 挤出式生物 3D 打印、光固化（DLP/SLA）或选择性激光熔化（SLM）等增材制造工艺。 |
| ZT-148 | `#Ｅ１Method/Fabrication 制备与加工工艺/Processing 成型加工与灭菌` | 静电纺丝、冷冻干燥、超声焊接、注塑自增强（SR）或环氧乙烷/辐照灭菌等工程加工与成型工艺。 |
| ZT-149 | `#Ｅ１Method/Characterization 表征与分析技术/BiomechanicalTest 生物力学测试` | 万能试验机压缩/拉伸/三点弯曲、疲劳循环、拔出力及纳米压痕等物理力学性能测试。 |
| ZT-150 | `#Ｅ１Method/Characterization 表征与分析技术/Physicochemical 理化与定量表征` | SEM、TEM、FTIR、XRD、XPS、NMR、ICP-MS 离子释放及流变/降解失重等材料理化表征技术。 |
| ZT-151 | `#Ｅ１Method/Characterization 表征与分析技术/Simulation 有限元与分子模拟` | 在实验研究内部配套使用的有限元力学仿真、分子对接或分子动力学模拟技术（若全篇以计算建模为主体，同时匹配 Type Computational）。 |
| ZT-152 | `#Ｅ１Method/Characterization 表征与分析技术/Omics 多组学与测序` | 批量 RNA-seq、单细胞测序（scRNA-seq）、空间转录组、蛋白质组学或代谢组学高通量测序与分析。 |
| ZT-153 | `#Ｅ１Method/Characterization 表征与分析技术/HistologyImaging 影像与组织学分析` | Micro-CT、CBCT、MRI、X 线影像分析以及 H&E、Masson、Trap、免疫荧光/免疫组化染色切片组织学评价。 |
