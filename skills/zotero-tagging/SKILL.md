---
name: zotero-tagging
description: >-
  Import literature into Zotero (from local PDFs or topic-based search) and apply the
  L0-L4 V2.0 orthogonal taxonomy (`#Ａ１Type`..`#Ｅ１Method`) with the `~ZTag-V2` marker.
  Use when adding papers by PDF or research topic, tagging or auditing Zotero items,
  finding untagged entries missing `~ZTag-V2`, or updating item attachments safely.
---

# Zotero 文献导入与 V2.0 多级自动打标 Skill

本 Skill 将用户 Zotero 知识库的 **V2.0 十维正交词表**（153 个受控标签，见 [references/ZOTERO_TAG_SPEC.md](./references/ZOTERO_TAG_SPEC.md) 与 [references/taxonomy.json](./references/taxonomy.json)）与 `zotero-mcp-plugin` 导入链路整合为标准化执行规程，确保新入库与存量文献结构统一、检索精准、标签零损。

---

## 一、AI 打标识别标记与标准执行顺序

### 1. 识别标记：`~ZTag-V2`
- 所有按本规范完成标注的文献统一附带普通标签 **`~ZTag-V2`**（纯 ASCII 字符，不含 `#` 或 `/`），在 ZoteroStyle 中不进入 `#` 多级树与 `/` 状态文件夹，自然位于平铺标签末尾。
- 增量打标前通过 `get_item_details` 检查条目标签，或在 Zotero 高级检索使用 **`标签` `不包含` `~ZTag-V2`** 定位未标注条目；已含 `~ZTag-V2` 的条目仅在用户明确要求更新时重标。

### 2. 导入、挂附件与打标顺序
全部入库与更新任务严格遵循三步顺序：

> **Step 1 锁定唯一父条目 ➔ Step 2 挂齐 PDF 附件 ➔ Step 3 读取全文内容并写入 V2.0 标签与 `~ZTag-V2`**

- 元数据识别（`RecognizeDocument`）作用于未归母条目的孤立 PDF 时会新建父条目并生成新 `itemKey`；而 `write_item(action="import" | "reparent")` 在已定父条目上挂接附件会完整保留父条目现有标签。按上述三步顺序执行即可兼顾元数据准确度、全文可读性与标签完整性。

---

## 二、三大标准工作流（经 MCP 工具执行）

### 工作流 A：基于本地 PDF 导入并打标
1. **提取标识并查重**：读取 PDF 前 1–2 页获取 DOI / PMID / arXiv ID 与标题，调用 `search_library` 检索 Zotero 库；若文献已存在，直接对既有 `itemKey` 补挂缺失 PDF 或增量更新标签。
2. **建立确定父条目**：
   - 具备 DOI / PMID / arXiv ID：调用 `add_by_identifier(identifiers=[id], collectionKey=..., saveAttachments=false)` 生成标准元数据父条目并取得 `parentKey`；
   - 无标准标识符（如产品手册、教材章节、技术报告）：提取题名、作者、年份、出版方后调用 `write_item(action="create", itemType=..., fields=..., creators=...)` 建父条目，必要时调用 `add_items_to_collection` 归档。
3. **挂接本地 PDF**：调用 `write_item(action="import", parentItemKey=parentKey, filePath=absPdfPath, linkMode="imported_file")` 完成附件归档。
4. **读取全文并写入标签**：调用 `get_item_details` 与 `get_item_abstract`（摘要缺失或细节在正文时补充调用 `get_content(itemKey=parentKey)`），经 [scripts/validate_tags.py](./scripts/validate_tags.py) 校验后，通过 `write_tag(action="add", ...)` 写入 V2.0 `#` 标签与 `~ZTag-V2`（若用户指定阅读状态再一并写入）。

### 工作流 B：按研究主题检索、批量导入与打标
1. **外部检索与筛选**：通过学术检索工具（PubMed / OpenAlex / EuropePMC / arXiv 等）筛选高相关性文献，汇总经核验的 DOI / PMID / arXiv ID 列表，并用 `search_library` 过滤库内已有条目。
2. **批量入库与拉取附件**：调用 `add_by_identifier(identifiers=..., collectionKey=..., saveAttachments=true, skipExisting=true, titleDuplicates="flag")`（批次超过 3 篇按返回的 `jobID` 轮询至完成）；若有需手动补挂的本地 PDF，先执行 `write_item(action="import", ...)` 挂齐。
3. **读取落库内容并集中打标**：逐篇调用 `get_item_details`、`get_item_abstract` 及 `get_content`，依据实际研究内容对照 [references/taxonomy.json](./references/taxonomy.json) 选标，经校验后批量写入 V2.0 标签与 `~ZTag-V2`。

### 工作流 C：存量条目补标、重标或更新附件后复核
1. **保护既有状态与用户标签**：先调用 `get_item_details` 读取已有 `tags`，保留既有工作流状态（优先级 `/Done` > `/reading` > `/unread`）及用户自定义标签；仅增量补充时优先用 `write_tag(action="add", ...)`，需替换分类并执行 `write_tag(action="set", ...)` 时先经 `validate_tags.py --existing ...` 合并输出。
2. **更新附件后复核**：通过 `write_item(action="import", parentItemKey=...)` 补充新附件后原有标签保持不变；若新附件提供了此前缺失的实验方法或材料信息，重读 `get_content` 并补充相应标签，确认携带 `~ZTag-V2`。
3. **系统条目边界**：批量任务自动跳过独立笔记（`itemType == "note"`）、插件配置条目及普通 PDF 批注子条目。

---

## 三、V2.0 打标核心规则（153 个受控词表）

1. **受控词表精确匹配**：全部 `#` 标签逐字取自 [references/taxonomy.json](./references/taxonomy.json) 的 `canonical_tags`（含全角前缀 `#Ａ１Type`..`#Ｅ１Method`、中英文、空格、括号与允许的半角 `ﾉ` `U+FF89`），确保编码纯净。
2. **单一 `#Ａ１Type` 排他原则**：每篇文献在 `#Ａ１Type/` 下**严格标注 1 个**标签；横向对比设计归入 `#Ｅ１Method/StudyDesign 研究设计/Comparative 横向对比研究`。
   - 临床研究 5 类互斥：`RCT`、`Prospective`（前瞻随访）、`Retrospective`（回顾病历）、`CrossSectional`（横断面调查或生物标志物横断面关联）、`CaseReport`（病例报告与系列）。
   - 器械评价用 `Article/DeviceEvaluation`；产品说明书用 `ProductManual`；实验流程用 `Protocol`；报告规范与治理标准用 `Standard`。
3. **三级叶节点优先（就细不就粗）**：同一分支下存在明确三级子标签时，只标三级子标签；仅在综述或未限定具体子类时标注二级母标签。常见商品名按真实成分归并：`LactoSorb` → `PLGA`、`SonicWeld`/`Resorb-X`/`PDLLA` → `PDLLA`、`Osteotrans` → `u-HAﾉPLLA`、`TMJ-OA` → `#Ｂ１Disease/TMD.../TMJ-OA`、`BRONJ` → `#Ｂ１Disease/MRONJ.../BRONJ`。
4. **MeSH Major Topic 与正交边界**：
   - 每篇通常标注 **2～9 个**核心 `#` 标签，聚焦核心对象、干预、主要机制/通路与关键表型；
   - `#Ｃ１Material` 表征化学骨架与表面改性，`#Ｃ２Carrier` 区分 `Scaffold` 与 `Nanocarrier`（结构性固定板/螺钉载体留空）；
   - 按实际研究内容严格区分 `Biomechanics` vs `Biodegradation`、`Angiogenesis` vs `Hemostasis`、`Adipogenesis` vs `EnergyMetabolism`、`Wound` vs `Scar`、`CellDifferentiation` / `CellMigration` / `CellSenescence`；仅研究微观破膜/EPS 瓦解机理时标注 `#Ｄ２Mechanism/AntimicrobialMech`，常规 CFU/抑菌圈实验标注 `#Ｄ３Phenotype/Antibacterial`；光热/光动力干预标注 `#Ｅ１Method/PhysicalTherapy 物理治疗技术/Phototherapy 光热与光动力治疗 (PTTﾉPDT)`；
   - 同主题文献保持一致口径：正颌临床/动物研究伴随 `#Ｂ１Disease/DentofacialDeformity 牙颌面畸形`（不混入创伤内固定 `MaxillofacialFixation`）；MRONJ/BRONJ 中 `BPs`/`Denosumab` 仅在药物自身为评价或毒性研究对象时进入 `#Ｃ３Drug`；临床随访与疗效研究统一伴随 `#Ｄ３Phenotype/ClinicalOutcome 临床疗效与并发症`。

---

## 四、写入前机器校验

在调用 `write_tag` 前，先在当前 Skill 目录下运行 [scripts/validate_tags.py](./scripts/validate_tags.py) 校验结构并自动合并保留状态与 `~ZTag-V2`：

```bash
python3 scripts/validate_tags.py \
  --existing '["/unread"]' \
  --tags '#Ａ１Type/Article 论著/Biomaterial 生物材料研究' '#Ｂ１Disease/BoneDefect 骨缺损与拔牙窝创伤'
```
