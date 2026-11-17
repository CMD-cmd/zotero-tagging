---
name: zotero-tagging
description: >-
  Import literature into Zotero (from local PDFs or topic search) and apply the
  L0-L4 V2.1 ten-dimension taxonomy (#Ａ１Type..#Ｅ１Method) with the ~ZTag-V2
  marker. Use when adding papers, tagging or auditing Zotero items, querying
  controlled terms, or migrating legacy tags while preserving user tags, reading
  states, collections, and attachments.
---

# Zotero 文献导入与 V2.1 自动打标

以十维正交受控词表服务 **TextFold 精读分流、Zotero 多级筛选与飞书多维表格同步**。下文脚本路径均相对于本 `SKILL.md` 所在目录 `<skill_dir>` 执行。

## 一、按需查词（禁全量硬背词表）

唯一词表数据源为 [references/taxonomy.json](references/taxonomy.json)（154 项，稳定 ID `ZT-001`–`ZT-154`）。先取十维索引，再按维度、多词关键词或 ID 查询候选：

```bash
python3 <skill_dir>/scripts/query_taxonomy.py
python3 <skill_dir>/scripts/query_taxonomy.py --dimension A1 --dimension C1
python3 <skill_dir>/scripts/query_taxonomy.py --query "GelMA 水凝胶"
python3 <skill_dir>/scripts/query_taxonomy.py --id ZT-050
```

仅在整库对齐时显式调用 `--all --limit 200`。详细层级与稀疏激活示例见 [references/ZOTERO_TAG_SPEC.md](references/ZOTERO_TAG_SPEC.md)；飞书十维字段映射模板见 [references/structured_fields.json](references/structured_fields.json)。

## 二、五条铁规则

1. **三步铁序与系统边界**：严格执行 **锁定唯一父条目 ➔ 挂齐全文附件 ➔ 读内容并校验打标**。禁止在未绑定父条目的孤立 PDF 上先打标后触发元数据识别；跳过独立 `note`、插件配置条目及批注子项。
2. **受控精准匹配与零损保留**：全部 `#` 标签必须逐字取自 `taxonomy.json`（含全角维度前缀与专有半角 `ﾉ` `U+FF89`），写入前必过 `<skill_dir>/scripts/validate_tags.py`。自动附带平铺标记 **`~ZTag-V2`**（用于「标签 不包含 `~ZTag-V2`」定位未标文献），并完整保留用户自定义标签、阅读状态（`/Done` > `/reading` > `/unread`）、集合归属与附件。
3. **`#Ａ１Type` 严格唯一排他**：每篇文献在 `#Ａ１Type/` 下有且仅有 1 个标签，按当前论文主导贡献与实际研究设计判定：
   - **论著三分精读**：`Article/Mechanistic`（分子/细胞机制）、`Article/Biomaterial`（材料设计/改性/配方与生物效应）、`Article/DeviceEvaluation`（成熟器械/板钉的力学、降解、临床前性能评价）。
   - **临床六选一**：`RCT`、`CaseControl`（按结局选病例对照，优先于笼统回顾）、`Prospective`（含 RCT 衍生前瞻随访分析）、`Retrospective`、`CrossSectional`、`CaseReport`。
   - **其他体裁各归其位**：`Review` / `SystematicReview` / `MetaAnalysis`、`Computational`（`FEA` / `Bioinformatics`）、`Guideline`（`ClinicalGuideline` / `Standard` 含报告规范与命名共识）、`Protocol`、`ProductInfo`（手册/说明书/FDA 510(k) 注册摘要）、`Book`、`Commentary`、`Humanities` / `Bioethics`。
4. **「就细不就粗」父子互斥**：命中明确三级子标签时，**只标三级子标签，严禁重复标二级母标签**（校验器在 `add` / `replace-managed` 模式下硬拦截）。常见材料与品牌按真实主成分下沉：`LactoSorb` → `PLGA`；`Osteotrans` → `u-HAﾉPLLA`；`SonicWeld` / `Resorb-X` / `BioSorb FX` / `Inion CPS` → `PDLLA 乳酸共聚物`。
5. **正交稀疏与跨篇一致性**：每篇精选 **2–9 个**核心 `#` 标签，无关维度天然留空，严禁为凑数机械扩标或把常规鉴定检测当机制：
   - **材料与载体分工**：`#Ｃ１Material` 按主基体元素/化学骨架判定（如 `Zn-1Mg` 归 `Zn-Fe`，不归 `Mg`）；`#Ｃ２Carrier` 区分 `Scaffold` 与 `Nanocarrier`，纯接骨板钉载体留空，无细胞条件培养基（CM）不标 `CellCarrier`。
   - **因果链严格判据**：纯 CFU/抑菌圈只标 `#Ｄ３Phenotype/Antibacterial`，有破膜、QS 抑制、抗黏附电荷或 EPS 瓦解机理才加 `#Ｄ２Mechanism/AntimicrobialMech`；常规干细胞鉴定用三系分化不标 `CellDifferentiation`。
   - **疾病、药物与临床口径对齐**：正颌研究固定配 `DentofacialDeformity` + `Orthognathic/...`，不混入创伤内固定 `MaxillofacialFixation`；`MRONJ`/`BRONJ` 中 `BPs`/`Denosumab` 仅在药物本身为评价或毒性研究对象时才标 `#Ｃ３Drug`（造模诱导剂或既往史不标）；临床随访/疗效/并发症研究统一伴随 `#Ｄ３Phenotype/ClinicalOutcome`（横断面纯流行病学关联除外）。

## 三、三大 MCP 执行流

- **A. 本地 PDF 入库**：读取前页提取 DOI/PMID/arXiv ID 与题名，调用 `search_library` 查重。有标识符时用 `add_by_identifier(..., saveAttachments=false)` 建父条目（无标准标识符时 `write_item(action="create")` + `add_items_to_collection`），再 `write_item(action="import", parentItemKey=..., linkMode="imported_file")` 挂 PDF，读取 `get_item_details`/`get_item_abstract`/`get_content`，过校验后 `write_tag(action="add")` 并回读。
- **B. 按主题批量导入**：学术检索汇总已核验 DOI/PMID 列表并 `search_library` 去重后，调用 `add_by_identifier(..., saveAttachments=true, skipExisting=true, titleDuplicates="flag")`（超 3 篇轮询 `jobID` 至完成）；补齐缺失附件后逐篇读取全文、过校验、写入并回读。
- **C. 存量补标、重标与更名**：先读取 `tags`。增量补标用 `validate_tags.py --mode add`；全量重构本词表标签并彻底保留用户标签与阅读状态时用 `--mode replace-managed` 后 `write_tag(action="set")`；纯旧词改名映射用 `--mode rename-only`；显式切换阅读状态传 `--status /unread|/reading|/Done`。

## 四、写入前校验与词表演进

每次写入前运行校验脚本取得精确 `final_tags` 与 `diff`：

```bash
python3 <skill_dir>/scripts/validate_tags.py \
  --mode replace-managed \
  --existing '["/reading", "自定义标签"]' \
  --tags '#Ａ１Type/Article 论著/Biomaterial 生物材料研究' \
         '#Ｂ１Disease/BoneDefect 骨缺损与拔牙窝创伤' \
         '#Ｃ１Material/Hydrogel 水凝胶/GelMA'
```

**词表演进规则**：日常打标严格遵守已发布词表，不向 Skill 目录写入临时状态文件；若连续多篇文献出现无法表达的高频实体或检索痛点，仅在回复末尾向用户附一条简短扩展建议；获用户确认修订词表时，以 `references/taxonomy.json` 为唯一源码更新并保持已有 `ZT-xxx` 与 `rename_map`、遵循 ZoteroStyle 胶囊正则 `[a-zA-Zα-ω\d-]+`（词组用 `-`，复合缩写用 `ﾉ`），同步更新 `ZOTERO_TAG_SPEC.md` 与 `structured_fields.json` 并通过单测后写入同步。
