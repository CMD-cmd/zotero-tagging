---
name: zotero-tagging
description: >-
  Import literature into Zotero and apply the versioned ten-dimension taxonomy
  (#Ａ１Type..#Ｅ１Method) with the ~ZTag-V2 marker. Use for literature import,
  tagging, targeted tag audits, and approved name migrations while preserving
  collection membership, user tags, reading states, and attachment relationships.
---

# Zotero 文献导入与标签管理

使用版本化的十维受控词表，具体版本、数量与路径由词表查询返回。分类服务精读分流、直接检索与结构化多选字段；名称使用熟悉的英文词、缩写和必要中文提示。

- [taxonomy.json](references/taxonomy.json)：唯一规范词表、稳定ID、逐词定义、名称映射与别名。
- [ZOTERO_TAG_SPEC.md](references/ZOTERO_TAG_SPEC.md)：分类边界、完整词表、ZoteroStyle显示规则。
- [pending_review.json](references/pending_review.json)：已有定点待核记录；日常维护保留其分类，内容复核按用户当前授权推进。
- [taxonomy_evolution.md](references/taxonomy_evolution.md)：日常发现缺口、评估新增或合并及版本迁移的流程。
- [taxonomy_candidates.json](references/taxonomy_candidates.json)：当前实例的词表候选与审议记录。
- [structured_fields.json](references/structured_fields.json)：十维多选字段映射设计，实际字段和选项ID在连接目标库后绑定。

## 按需读取

入口负责工作流程和分流原则；`taxonomy.json`负责规范标签、定义、稳定ID及名称映射。校验脚本从同一数据源读入完整词表，AI上下文只接收当前任务需要的内容。

| 当前任务 | 读取方式 |
|---|---|
| 初次选择分类 | 运行查询脚本获取十维索引，再选所需维度 |
| 为文献选标 | 按维度、关键词或稳定ID查询候选词，核对定义 |
| 仅做名称迁移 | 使用`validate_tags.py --mode rename-only`，检查输出差异 |
| 处理待核条目 | 读取`pending_review.json`中的活动记录及对应证据 |
| 发现分类缺口、研究领域变化或检索困难 | 读取`taxonomy_evolution.md`，更新`taxonomy_candidates.json` |
| 维护词表、审查分类边界 | 按需读取`ZOTERO_TAG_SPEC.md`及相关词表范围 |
| 结构化表格同步 | 读取`structured_fields.json` |

```bash
python3 scripts/query_taxonomy.py
python3 scripts/query_taxonomy.py --dimension A1 --dimension C1
python3 scripts/query_taxonomy.py --query SSRO
python3 scripts/query_taxonomy.py --id ZT-050
```

多种筛选条件按交集处理。结果中的`total_matches`和`next_offset`显示分页情况；需要后续候选时继续读取。全词表查询显式使用`--all --limit 200`。查询与校验均以`taxonomy.json`为唯一数据源；规范文档和字段映射随词表发布保持一致。

## 阅读与归类

1. 先查重并确定唯一父条目。已有文献优先补充原条目；通过DOI、PMID等导入时优先使用Zotero元数据解析器。
2. 挂接已有或获准获取的全文附件，保持父条目和已有引用关联。
3. 阅读标题、摘要及能取得的全文，选择与核心研究对象、干预、机制、表型和关键方法相符的规范标签。证据不足的具体归类记入待核清单；词表无法准确表达的检索需求记入候选清单，同时完成其余有依据的归类。
4. 运行校验脚本，检查拟新增、移除及保留内容后，通过Zotero工具写入并回读。

独立笔记、插件配置和PDF批注属于系统与用户内容。已按本规范打标的独立文献PDF，可在授权的名称迁移中同步更名。

## 精读分流

`#Ａ１Type`选择一个主要类型：

- `Article/Mechanistic`：生物学机制、分子或细胞调控关系。
- `Article/Biomaterial`：材料设计、制备及生物效应。
- `Article/DeviceEvaluation`：器械或固定系统的力学、降解、相容性及临床前评价。
- `Clinical`保留RCT、Prospective、Retrospective、CrossSectional、CaseReport，并包含CaseControl。按当前论文明确的主要设计选择；病例对照使用CaseControl，RCT衍生随访按当前分析设计归类。
- Review、SystematicReview、MetaAnalysis、Computational等沿用各自直接入口。

交叉研究按主要贡献选择阅读路线。机制主题与证据强度分别记录；关联证据也可服务机制类阅读。

## 内容标签与词表维护

- 其余九维按实际研究内容选择，可留空。同一分支已有明确具体词时优先具体词。
- Wnt-BMP-TGFβ、InnateImmune、糖酵解与氧化磷酸化、脂质与氨基酸代谢等综合词，表示其中一个或多个相关主题。
- 保留材料体系、载体、药物、靶点、机制、表型与方法的职责边界。材料按基体和组成判断；商品配方以具体原文或产品版本为依据。
- 日常AI使用当前发布词表，并记录分类缺口和检索反馈。领域变化、重复出现的缺口或实际筛选困难可触发小范围调整；按[词表演进流程](references/taxonomy_evolution.md)提出新增、别名、更名、合并或拆分，依据已获授权的变更范围发布新版本。
- 标签数量用于观察检索质量；内容重标依据具体问题和证据，保存逐条判断。
- 十维标签可直接映射十个多选字段。笔记记录证据来源和阅读理解；持续需要筛选的属性采用受控标签或明确的结构化字段。

## 写入与保留规则

`~ZTag-V2`作为V2系列已打标标记继续使用；词表精确版本保存在词表与操作记录中。标记表示处理状态，证据及待核状态单独记录。

- `add`模式保留已有标签并增补受控词。
- `replace-managed`模式仅替换词表管理的标签及其已知旧名称，保留用户自定义标签，包括以`#`或`/`开头的标签。
- 阅读状态默认原样保留。明确需要转换状态时使用`--status`；普通名称迁移保持状态、标记和标签属性。
- 批量迁移先备份数据库、Skill、条目标签与集合关系；冻结逐条变更清单，写入前核对当前状态，写后回读。遇到状态变化时先重新对照差异。
- 集合组织按用户当前任务独立处理；标签写入保持集合和附件关系。

```bash
python3 scripts/validate_tags.py \
  --existing '["/unread"]' \
  --tags '#Ａ１Type/Article 论著/Biomaterial 生物材料研究' \
         '#Ｂ１Disease/BoneDefect 骨缺损与拔牙窝创伤'
```

完整替换本词表管理的分类时，增加`--mode replace-managed`并提供该条完整拟保留分类。校验结果中的`diff`用于检查变更范围。旧名称通过精确一对一映射归一，陌生名称返回错误。
