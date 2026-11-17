# Zotero 全库文献多级标签正式规范（V2.0）

本规范由十维正交受控词表（配套机器可读文件 `taxonomy.json`）构成，旨在支撑 **Zotero（Zotero Style 多级树状按层级序渲染） ↔ AI 自动打标 ↔ TextFold 精读 ↔ 飞书多维表格看板** 的无损协同。

---

## 一、L0→L4 五层全角排序前缀架构

为了使 Zotero Style 侧边栏严格按照从顶层研究范式（L0）到底层实验方法（L4）的自然阅读逻辑排序，10 个顶层母标签采用**全角字母+全角数字 + 单一凝练英文词（中间无空格）**的规范命名：

```text
【L0 元范式层】       #Ａ１Type        —— 唯一排外的研究体裁与证据等级（每篇严格有且仅有 1 个）
          │
          ▼
【L1 临床问题与场景】 #Ｂ１Disease     ∥  #Ｂ２Surgery
          │               (疾病/病理态)     (外科术式与临床操作)
          ▼
【L2 干预工具箱层】   #Ｃ１Material    ➔  #Ｃ２Carrier     ➔  #Ｃ３Drug
          │               (材料骨架/改性)   (递送剂型/载体)   (药理活性载荷)
          ▼
【L3 因果效应链层】   #Ｄ１Target      ➔  #Ｄ２Mechanism   ➔  #Ｄ３Phenotype
          │               (通路/因子/分子)   (底层细胞/物理机制) (宏观表型/力学/结局)
          ▼
【L4 实验方法与设计】 #Ｅ１Method      —— StudyDesign（研究设计）+ Model + 物理干预/制备/表征技术
```

### V2.0 核心设计规则
1. **`#Ａ１Type` 100% 严格唯一排他**：每篇文献在 `#Ａ１Type` 下**严格有且仅有 1 个标签**（`1,086` 篇对应 `1,086` 次标注）。原辅助对比设计标签迁入 `#Ｅ１Method/StudyDesign 研究设计/Comparative 横向对比研究`；临床研究拆清为 5 个互斥子类（`RCT`、`Prospective`、`Retrospective`、`CrossSectional`、`CaseReport`），消除原 `Cohort / Retrospective / Observational` 重叠混乱；产品手册 `ProductManual` 与实验规程 `Protocol` 分立，器械动物/力学评价明确为 `Article/DeviceEvaluation 器械临床前评价`。
2. **「方式一：就细不就粗」父子互斥规则**：
   - 当文献明确对应某三级细化子标签时，**只标三级子标签，禁止再重复标二级母标签**（由 Zotero Style 树自动向上聚合总数）；
   - 仅当综述、泛指研究或未限定具体材质（如通篇只说“可吸收内固定板”未明言 `PLLA`/`PLGA`/`PDLLA`）时，才使用二级母标签。
   - 常见商品名/材料简称统一按此规则下沉：`LactoSorb` → `PLGA`；`SonicWeld` / `Resorb-X` / `BioSorb` / `Inion` → `PDLLA`；`Osteotrans` / `u-HA/PLLA` → `u-HAﾉPLLA`。
3. **干练常见用词与禁滥用 `ﾉ` 拼词原则**：
   - 取消生硬拼词（如不再使用 `BookﾉChapter`、`HumanitiesﾉMethodology`、`PhysicalﾉFabrication`、`AngiogenesisﾉCoagulation`、`BiomechanicsﾉDegradation`、`NanocarrierﾉScaffold` 等）；
   - 半角假名 `ﾉ`（`U+FF89`）**仅限保留在本身即为复合缩写的学术专有名词中**：`BSSROﾉSSRO`、`u-HAﾉPLLA`、`M1ﾉM2`、`MAPKﾉERK`、`cAMPﾉPKA`、`PTTﾉPDT`；严禁出现不可见 Unicode 标签字符（如 `U+E002F`）。
4. **严格区分职责边界，杜绝概念捆绑**：
   - **`#Ｃ１Material` vs `#Ｃ２Carrier`**：`Material` 只表征化学材质骨架及表面改性（如 `Nanomaterial` 只用于无机/碳基等功能纳米材料）；`Carrier` 只表征递送剂型或组织工程载体（拆清 `Scaffold` 与 `Nanocarrier`）；纯接骨板/螺钉等结构性器械的 `#Ｃ２Carrier` 留空。
   - **`#Ｄ２Mechanism` vs `#Ｄ３Phenotype`**：`Biomechanics` 与 `Biodegradation` 拆分；`Angiogenesis` 与 `Hemostasis` 拆分；`Adipogenesis` 与 `EnergyMetabolism` 拆分；`CellDifferentiation` / `CellMigration` / `CellSenescence` 拆分；`AntimicrobialMech`（破膜与生物膜瓦解）**仅**用于研究了微观杀菌/破膜机制的文献，普通抑菌率/CFU 实验仅在 `#Ｄ３Phenotype` 标 `Antibacterial`。
   - **`#Ｅ１Method` 物理治疗与制备工艺分离**：`CAP` 与新补齐的高频标签 `Phototherapy 光热与光动力治疗 (PTTﾉPDT)` 归入 `PhysicalTherapy 物理治疗技术`；`3D-Printing` 与 `Processing` 保留在 `Fabrication 制备与加工工艺`。

---

## 二、制定原则：参考 MeSH 词表而不照搬 MeSH

本规范在词表凝练过程中继续秉持**“取 MeSH 之准、弃 MeSH 之繁”**五项原则：
1. **MeSH 上位归一**：同一疾病或现象统一归入标准词条（例如按 DC/TMD 分类将 `TMJ-OA` 收编至 `#Ｂ１Disease/TMD.../TMJ-OA`，全身骨关节炎保留 `#Ｂ１Disease/Osteoarthritis`）。
2. **弃倒装词序与副主题词斜杠**：语义组合交给 L0→L4 正交维度自由搭配。
3. **树深封顶（<= 3 层）**：杜绝长尾合金/小众化合物孤儿标签（如镁合金型号统一收归 `Mg (Magnesium-Based)`）。
4. **MeSH Major Topic 核心贡献原则**：每篇文献只标核心研究对象、干预、机制、表型与方法（通常 `2～9` 个 `#` 标签），常规细胞活性检测或背景提及不滥标。
5. **同性质文献跨篇一致对齐**：
   - **正颌文献**：所有正颌临床/动物研究（纯体外/尸体力学仿真除外）统一伴随 `#Ｂ１Disease/DentofacialDeformity 牙颌面畸形`，且不与 `#Ｂ２Surgery/MaxillofacialFixation`（专指颌面创伤与重建内固定）混标。
   - **MRONJ / BRONJ 文献**：仅当 `BPs` / `Denosumab` 本身是被研究的治疗或药理/毒性评价对象时才标入 `#Ｃ３Drug`；仅作为建立动物 BRONJ 模型的背景诱导剂或病例既往用药史时，由 `BRONJ`/`DRONJ` 疾病标签体现，**不标 `#Ｃ３Drug`**。
   - **临床疗效/并发症研究**：凡以临床随访结局、并发症或诊断准确率为主的 `#Ａ１Type/Clinical` 与临床比较型系统综述，统一对齐 `#Ｄ３Phenotype/ClinicalOutcome 临床疗效与并发症`。

---

## 三、书写与工作流硬规范

1. **顶层前缀**：必须为 `#Ａ１Type`、`#Ｂ１Disease`、`#Ｂ２Surgery`、`#Ｃ１Material`、`#Ｃ２Carrier`、`#Ｃ３Drug`、`#Ｄ１Target`、`#Ｄ２Mechanism`、`#Ｄ３Phenotype`、`#Ｅ１Method` 之一（全角字母与数字，无空格）。
2. **工作流阅读状态**：顶层允许最多保留 **1 个**既有状态标签（`/Done` > `/reading` > `/unread`）；不强行给原无状态条目补标。
3. **系统保护对象**：独立笔记、插件配置条目及普通 PDF 批注子条目保持原样，不参与文献批量打标。
4. **AI 已标识别标记（`~ZTag-V2`）**：每篇经 AI Agent 按 V2.0 规范完成打标的条目，统一附加普通平铺标签 **`~ZTag-V2`**（纯 ASCII 字符，不带 `#` 或 `/`），不进入 `#` 多级树与 ZoteroStyle 正则列，也不占用 `/` 状态空间；可在 Zotero 高级筛选通过「标签 不包含 `~ZTag-V2`」快速定位待标注文献。
5. **标准导入与标注顺序**：严格执行「**锁定父条目 ➔ 挂齐 PDF 附件 ➔ 读取全文并写入 V2.0 标签与 `~ZTag-V2`**」，防止在未绑定父条目的孤立 PDF 上先打标后触发元数据识别导致标签滞留子附件。

---

## 四、不同文献类型的稀疏激活指南

- **机制研究 (`#Ａ１Type/Article 论著/Mechanistic 机制研究`)**：重点标 `#Ｂ１Disease` + `#Ｄ１Target` + `#Ｄ２Mechanism` + `#Ｄ３Phenotype` + `#Ｅ１Method/AnimalModel` 或 `InVitroModel`；`#Ｃ１Material`/`#Ｃ２Carrier`/`#Ｂ２Surgery` 天然留空。
- **生物材料研究 (`#Ａ１Type/Article 论著/Biomaterial 生物材料研究`)**：按需激活 `#Ｃ１Material`/`#Ｃ２Carrier`/`#Ｃ３Drug` + `#Ｂ１Disease` + `#Ｄ３Phenotype` + `#Ｄ２Mechanism` + `#Ｄ１Target` + `#Ｅ１Method`。
- **器械临床前评价 (`#Ａ１Type/Article 论著/DeviceEvaluation 器械临床前评价`)**：重点标 `#Ｂ２Surgery`/`#Ｂ１Disease` + `#Ｃ１Material` + `#Ｄ３Phenotype/Biomechanics`（及/或 `Biodegradation` / `Osteogenesis`）+ `#Ｅ１Method`；`#Ｄ１Target`/`#Ｃ２Carrier` 通常留空。
- **计算与仿真 (`#Ａ１Type/Computational 计算与仿真/...`)**：重点标 `#Ｂ２Surgery`/`#Ｂ１Disease` + `#Ｃ１Material` + `#Ｄ３Phenotype/Biomechanics`（若属生信/分子模拟可带对应靶点）+ `#Ｅ１Method/Characterization.../Simulation`。
- **临床研究与综述 (`#Ａ１Type/Clinical...` / `Review` / `SystematicReview`)**：严格 1 个主 `#Ａ１Type` + 对应临床对比（`#Ｅ１Method/StudyDesign.../Comparative`）+ `#Ｂ１Disease`/`#Ｂ２Surgery` + `#Ｃ１Material`/`#Ｃ３Drug` + `#Ｄ３Phenotype/ClinicalOutcome`。
- **指南/规程/手册/人文 (`Guideline` / `Protocol` / `ProductManual` / `Book` / `Humanities`)**：准确标注 `#Ａ１Type` 与其直接覆盖的疾病/材料/技术范围，绝不牵强凑分子靶点。

---

## 五、标准受控词表全览（153 个受控标签，10 维）

### 1. `#Ａ１Type`（L0：研究范式与文献体裁，21 个）
- `#Ａ１Type/Article 论著/Mechanistic 机制研究`
- `#Ａ１Type/Article 论著/Biomaterial 生物材料研究`
- `#Ａ１Type/Article 论著/DeviceEvaluation 器械临床前评价`
- `#Ａ１Type/Clinical 临床研究/RCT (Randomized Controlled Trial) 随机对照试验`
- `#Ａ１Type/Clinical 临床研究/Prospective 前瞻性临床研究`
- `#Ａ１Type/Clinical 临床研究/Retrospective 回顾性临床研究`
- `#Ａ１Type/Clinical 临床研究/CrossSectional 横断面研究`
- `#Ａ１Type/Clinical 临床研究/CaseReport 病例报告与系列`
- `#Ａ１Type/Review 综述`
- `#Ａ１Type/SystematicReview 系统综述`
- `#Ａ１Type/SystematicReview 系统综述/MetaAnalysis Meta分析`
- `#Ａ１Type/Computational 计算与仿真/FEA (Finite Element Analysis) 有限元分析`
- `#Ａ１Type/Computational 计算与仿真/Bioinformatics 生物信息与分子模拟`
- `#Ａ１Type/Guideline 指南与规范/ClinicalGuideline 临床诊疗指南`
- `#Ａ１Type/Guideline 指南与规范/Standard 技术标准与报告规范`
- `#Ａ１Type/Protocol 实验方案与规程`
- `#Ａ１Type/ProductManual 产品手册与说明书`
- `#Ａ１Type/Book 专著与教材`
- `#Ａ１Type/Commentary 述评与观点`
- `#Ａ１Type/Humanities 科技人文与方法论`
- `#Ａ１Type/Humanities 科技人文与方法论/Bioethics 生命伦理与治理`

### 2. `#Ｂ１Disease`（L1：临床疾病与病理状态，27 个）
- `#Ｂ１Disease/MRONJ (Medication-Related Osteonecrosis of the Jaw) 药物相关颌骨坏死`
- `#Ｂ１Disease/MRONJ (Medication-Related Osteonecrosis of the Jaw) 药物相关颌骨坏死/BRONJ 双膦酸盐相关颌骨坏死`
- `#Ｂ１Disease/MRONJ (Medication-Related Osteonecrosis of the Jaw) 药物相关颌骨坏死/DRONJ 地诺单抗相关颌骨坏死`
- `#Ｂ１Disease/ONFH (Osteonecrosis of the Femoral Head) 股骨头坏死`
- `#Ｂ１Disease/ONFH (Osteonecrosis of the Femoral Head) 股骨头坏死/SONFH 激素性股骨头坏死`
- `#Ｂ１Disease/ONFH (Osteonecrosis of the Femoral Head) 股骨头坏死/IschemicONFH 缺血性股骨头坏死`
- `#Ｂ１Disease/TMD (Temporomandibular Disorders) 颞下颌关节病`
- `#Ｂ１Disease/TMD (Temporomandibular Disorders) 颞下颌关节病/TMJ-OA (Temporomandibular Joint Osteoarthritis) 颞下颌关节骨关节炎`
- `#Ｂ１Disease/Osteoarthritis 骨关节炎`
- `#Ｂ１Disease/Osteoporosis 骨质疏松症`
- `#Ｂ１Disease/Periodontitis 牙周炎`
- `#Ｂ１Disease/Peri-Implantitis 种植体周围炎`
- `#Ｂ１Disease/Endodontics 牙体牙髓病`
- `#Ｂ１Disease/DentofacialDeformity 牙颌面畸形`
- `#Ｂ１Disease/Craniosynostosis 颅缝早闭`
- `#Ｂ１Disease/CraniofacialFracture 颅颌面骨折`
- `#Ｂ１Disease/CraniofacialFracture 颅颌面骨折/MandibularFracture 下颌骨骨折`
- `#Ｂ１Disease/CraniofacialFracture 颅颌面骨折/MidfacialFracture 面中部与眶壁骨折`
- `#Ｂ１Disease/BoneDefect 骨缺损与拔牙窝创伤`
- `#Ｂ１Disease/Infection 感染性疾病/OralInfection 口腔细菌与生物膜感染`
- `#Ｂ１Disease/Infection 感染性疾病/ImplantInfection 手术与植入物感染`
- `#Ｂ１Disease/Wound 皮肤黏膜创面`
- `#Ｂ１Disease/Scar 病理性瘢痕与纤维化`
- `#Ｂ１Disease/MetabolicDisorder 糖脂代谢疾病`
- `#Ｂ１Disease/AutoimmuneDisease 自身免疫与风湿病`
- `#Ｂ１Disease/CardiovascularDisease 心血管疾病`
- `#Ｂ１Disease/Tumor 肿瘤`

### 3. `#Ｂ２Surgery`（L1：外科术式与临床操作，8 个）
- `#Ｂ２Surgery/Orthognathic 正颌外科`
- `#Ｂ２Surgery/Orthognathic 正颌外科/BSSROﾉSSRO (Sagittal Split Ramus Osteotomy) 下颌升支矢状劈开术`
- `#Ｂ２Surgery/Orthognathic 正颌外科/LeFort-I Le Fort I型截骨术`
- `#Ｂ２Surgery/Orthognathic 正颌外科/Genioplasty 颏成形术`
- `#Ｂ２Surgery/Orthognathic 正颌外科/DO (Distraction Osteogenesis) 牵张成骨`
- `#Ｂ２Surgery/MaxillofacialFixation 颌面创伤与重建内固定`
- `#Ｂ２Surgery/ImplantSurgery 牙槽与种植外科`
- `#Ｂ２Surgery/OrthopedicFixation 骨科内固定与关节置换`

### 4. `#Ｃ１Material`（L2：工程材料骨架与表面改性，21 个）
- `#Ｃ１Material/ResorbablePolymer 可吸收高分子`
- `#Ｃ１Material/ResorbablePolymer 可吸收高分子/PLLA (Poly-L-Lactic Acid) 左旋聚乳酸`
- `#Ｃ１Material/ResorbablePolymer 可吸收高分子/PDLLA (Poly-DL-Lactic Acid) 外消旋与共聚聚乳酸`
- `#Ｃ１Material/ResorbablePolymer 可吸收高分子/PLGA (Poly(lactic-co-glycolic acid)) 聚乳酸-羟基乙酸共聚物`
- `#Ｃ１Material/ResorbablePolymer 可吸收高分子/PGA (Polyglycolic Acid) 聚乙醇酸`
- `#Ｃ１Material/ResorbablePolymer 可吸收高分子/PCL (Polycaprolactone) 聚己内酯`
- `#Ｃ１Material/ResorbablePolymer 可吸收高分子/u-HAﾉPLLA 羟基磷灰石ﾉ聚乳酸复合材料`
- `#Ｃ１Material/BiodegradableMetal 可降解金属`
- `#Ｃ１Material/BiodegradableMetal 可降解金属/Mg (Magnesium-Based) 镁与镁合金`
- `#Ｃ１Material/BiodegradableMetal 可降解金属/ZnFeAlloy 锌基与铁基合金`
- `#Ｃ１Material/Titanium 钛与钛合金`
- `#Ｃ１Material/Hydrogel 水凝胶`
- `#Ｃ１Material/Hydrogel 水凝胶/GelMA (Gelatin Methacryloyl) 甲基丙烯酰化明胶`
- `#Ｃ１Material/Hydrogel 水凝胶/NaturalHydrogel 天然高分子水凝胶`
- `#Ｃ１Material/Hydrogel 水凝胶/SmartHydrogel 合成与响应型水凝胶`
- `#Ｃ１Material/MOF (Metal-Organic Framework) 金属有机框架`
- `#Ｃ１Material/MOF (Metal-Organic Framework) 金属有机框架/ZIF-8 (Zeolitic Imidazolate Framework-8) 沸石咪唑酯骨架-8`
- `#Ｃ１Material/Bioceramic 生物陶瓷与活性玻璃`
- `#Ｃ１Material/Nanomaterial 无机与复合纳米材料`
- `#Ｃ１Material/SurfaceModification 表面改性/Coating 表面涂层`
- `#Ｃ１Material/SurfaceModification 表面改性/SurfaceTopography 表面形貌与电荷修饰`

### 5. `#Ｃ２Carrier`（L2：递送载体与制剂剂型，5 个）
- `#Ｃ２Carrier/Scaffold 组织工程与控释支架`
- `#Ｃ２Carrier/Nanocarrier 纳米递送载体`
- `#Ｃ２Carrier/tFNAs (Tetrahedral Framework Nucleic Acids) 四面体框架核酸`
- `#Ｃ２Carrier/EVs (Extracellular Vesicles) 细胞外囊泡与外泌体`
- `#Ｃ２Carrier/CellCarrier 细胞与血小板载体`

### 6. `#Ｃ３Drug`（L2：活性药物与生物载荷，9 个）
- `#Ｃ３Drug/Antiresorptive 抗骨吸收药/BPs (Bisphosphonates) 双膦酸盐`
- `#Ｃ３Drug/Antiresorptive 抗骨吸收药/Denosumab 地诺单抗`
- `#Ｃ３Drug/Biologics 蛋白与抗体药物/TCZ (Tocilizumab) 托珠单抗`
- `#Ｃ３Drug/Biologics 蛋白与抗体药物/GrowthFactor 重组生长因子与多肽`
- `#Ｃ３Drug/SmallMolecule 小分子化学药`
- `#Ｃ３Drug/NucleicAcid 核酸药物`
- `#Ｃ３Drug/NaturalProduct 天然产物与中药成分`
- `#Ｃ３Drug/Antibiotic 抗生素与抗菌药`
- `#Ｃ３Drug/GasTherapy 气体与活性氧分子`

### 7. `#Ｄ１Target`（L3：分子靶点与信号通路，18 个）
- `#Ｄ１Target/Pathway 信号通路/JAK-STAT 信号通路`
- `#Ｄ１Target/Pathway 信号通路/NF-κB-RANKL 信号通路`
- `#Ｄ１Target/Pathway 信号通路/MAPKﾉERK 信号通路`
- `#Ｄ１Target/Pathway 信号通路/PI3K-Akt-mTOR 信号通路`
- `#Ｄ１Target/Pathway 信号通路/Wnt-BMP-TGFβ 信号通路`
- `#Ｄ１Target/Pathway 信号通路/Hippo-YAP 信号通路`
- `#Ｄ１Target/Pathway 信号通路/cAMPﾉPKA 信号通路`
- `#Ｄ１Target/Pathway 信号通路/InnateImmune 固有免疫通路 (TLR-NLRP3-STING)`
- `#Ｄ１Target/Pathway 信号通路/Nrf2 抗氧化通路`
- `#Ｄ１Target/Cytokine 细胞因子与生长因子/IL-6 白介素-6`
- `#Ｄ１Target/Cytokine 细胞因子与生长因子/InflammatoryCytokine 促炎因子 (IL-1-TNFα)`
- `#Ｄ１Target/Cytokine 细胞因子与生长因子/AngiogenicFactor 促血管生长因子 (VEGF-FGF)`
- `#Ｄ１Target/BoneMetabolism 骨与代谢分子/OCN (Osteocalcin) 骨钙素`
- `#Ｄ１Target/BoneMetabolism 骨与代谢分子/Zfp467 (Zinc Finger Protein 467) 锌指蛋白467`
- `#Ｄ１Target/BoneMetabolism 骨与代谢分子/OsteogenicTF 成骨与成脂转录因子`
- `#Ｄ１Target/BoneMetabolism 骨与代谢分子/BoneMatrixProtein 骨基质与矿化蛋白`
- `#Ｄ１Target/BoneMetabolism 骨与代谢分子/MetabolicHormone 糖脂代谢激素与受体`
- `#Ｄ１Target/NoncodingRNA 非编码RNA与表观调控`

### 8. `#Ｄ２Mechanism`（L3：通用生物学与物理化学机制，13 个）
- `#Ｄ２Mechanism/MetabolicReprogramming 代谢重编程/Glycolysis-OXPHOS 糖酵解与氧化磷酸化`
- `#Ｄ２Mechanism/MetabolicReprogramming 代谢重编程/LipidAminoAcid 脂质与氨基酸代谢`
- `#Ｄ２Mechanism/CellDifferentiation 细胞分化调控`
- `#Ｄ２Mechanism/CellMigration 细胞迁移与招募`
- `#Ｄ２Mechanism/CellSenescence 细胞衰老`
- `#Ｄ２Mechanism/CellDeath 细胞死亡与自噬`
- `#Ｄ２Mechanism/CellCommunication 细胞通讯与旁分泌`
- `#Ｄ２Mechanism/Mechanotransduction 力学信号转导`
- `#Ｄ２Mechanism/OxidativeHypoxia 氧化应激与缺氧调控`
- `#Ｄ２Mechanism/IonMicroenvironment 离子与酸碱微环境`
- `#Ｄ２Mechanism/AntimicrobialMech 破膜与生物膜瓦解`
- `#Ｄ２Mechanism/Biomineralization 生物矿化与钙化`
- `#Ｄ２Mechanism/ForeignBodyReaction 异物与植入物免疫反应`

### 9. `#Ｄ３Phenotype`（L3：宏观表型与力学/临床结局，15 个）
- `#Ｄ３Phenotype/Osteogenesis 成骨与骨再生`
- `#Ｄ３Phenotype/BoneResorption 破骨与骨吸收`
- `#Ｄ３Phenotype/Adipogenesis 成脂分化`
- `#Ｄ３Phenotype/EnergyMetabolism 糖脂与能量代谢`
- `#Ｄ３Phenotype/CartilageHomeostasis 软骨修复与退变`
- `#Ｄ３Phenotype/Angiogenesis 促血管生成`
- `#Ｄ３Phenotype/Hemostasis 凝血与止血`
- `#Ｄ３Phenotype/Immunomodulation 免疫调控/MacrophagePolarization 巨噬细胞极化 (M1ﾉM2)`
- `#Ｄ３Phenotype/Immunomodulation 免疫调控/Anti-Inflammation 抗炎调控`
- `#Ｄ３Phenotype/Antibacterial 抗菌与抗生物膜`
- `#Ｄ３Phenotype/WoundHealing 创面愈合与抗瘢痕`
- `#Ｄ３Phenotype/Antitumor 抗肿瘤`
- `#Ｄ３Phenotype/Biomechanics 生物力学稳定性`
- `#Ｄ３Phenotype/Biodegradation 生物降解与吸收`
- `#Ｄ３Phenotype/ClinicalOutcome 临床疗效与并发症`

### 10. `#Ｅ１Method`（L4：研究设计、实验模型与表征/治疗技术，16 个）
- `#Ｅ１Method/StudyDesign 研究设计/Comparative 横向对比研究`
- `#Ｅ１Method/AnimalModel 动物模型/SmallAnimal 小动物模型`
- `#Ｅ１Method/AnimalModel 动物模型/LargeAnimal 大动物模型`
- `#Ｅ１Method/InVitroModel 体外模型/CellCulture 细胞培养体系`
- `#Ｅ１Method/InVitroModel 体外模型/Organoid 3D培养与类器官`
- `#Ｅ１Method/InVitroModel 体外模型/BiofilmModel 细菌与生物膜模型`
- `#Ｅ１Method/InVitroModel 体外模型/SyntheticBone 体外仿真骨与力学模型`
- `#Ｅ１Method/PhysicalTherapy 物理治疗技术/CAP (Cold Atmospheric Plasma) 冷大气等离子体`
- `#Ｅ１Method/PhysicalTherapy 物理治疗技术/Phototherapy 光热与光动力治疗 (PTTﾉPDT)`
- `#Ｅ１Method/Fabrication 制备与加工工艺/3D-Printing 3D打印与增材制造`
- `#Ｅ１Method/Fabrication 制备与加工工艺/Processing 成型加工与灭菌`
- `#Ｅ１Method/Characterization 表征与分析技术/BiomechanicalTest 生物力学测试`
- `#Ｅ１Method/Characterization 表征与分析技术/Physicochemical 理化与定量表征`
- `#Ｅ１Method/Characterization 表征与分析技术/Simulation 有限元与分子模拟`
- `#Ｅ１Method/Characterization 表征与分析技术/Omics 多组学与测序`
- `#Ｅ１Method/Characterization 表征与分析技术/HistologyImaging 影像与组织学分析`

---

## 六、历史旧 `#` 标签迁移与纠偏要点（V2.0 对照摘要）

| 旧标签模式 | V2.0 新规范去向 | 说明 |
|---|---|---|
| `#A` / `#R` / `#C/*` / `#M` / `#O` | `#Ａ１Type/*`（严格 1 个） | 依据研究范式与设计细分为 Mechanistic / Biomaterial / DeviceEvaluation、5 类互斥 Clinical、Standard、ProductManual 等 |
| `#00Mc/*` | `#Ｄ２Mechanism/*` 或 `#Ｃ１Material/SurfaceModification/*` | `改变pH`→`IonMicroenvironment`；`消除缺氧`→`OxidativeHypoxia`；表面特征→`SurfaceTopography`；真破膜/物理杀菌机理→`AntimicrobialMech` |
| `#01Ds/*` | `#Ｂ１Disease/*` | 修正 `Fructure` 拼写；`TMJ-OA` 归入 `TMD`；`UUO` 归入 `Scar` 病理性瘢痕与纤维化 |
| `#02Pt/Apoptosis`、`Paracrine` | `#Ｄ２Mechanism/*` | 从表型迁回机制层（`CellDeath`、`CellCommunication`） |
| `#12Pw/Migration`、`MAPK/ERK1...` | `#Ｄ２Mechanism/CellMigration`、`#Ｄ１Target/Pathway/MAPKﾉERK` | 迁移独立成机制，清除 `U+E002F` 不可见字符 |
| `#13Dg/BPs...ZA` | 仅当药物本身为评价对象时标 `#Ｃ３Drug` | 纯 BRONJ 动物造模诱导剂或病例既往史不标 `#Ｃ３Drug` |
| `#14Tm/*`、`#21Mt/*` | `#Ｃ１Material/*` / `#Ｃ２Carrier/*` / `#Ｃ３Drug/*` | 按“化学材质骨架 / 递送载体 / 活性药载”正交拆清；商品名材料按方式一下沉 |
| `#15Tq/*`、`#31Tq/FEA`、`#16Mb/*` | `#Ｅ１Method/*` | 物理治疗（CAP/PTTﾉPDT）独立于加工工艺；生物膜模型归入 `InVitroModel` |
| `#41VS/*` | `#Ｅ１Method/StudyDesign 研究设计/Comparative 横向对比研究` + 对应临床/材料标签 | 迁入 L4 研究设计轴，确保 `#Ａ１Type` 严格唯一排他 |
