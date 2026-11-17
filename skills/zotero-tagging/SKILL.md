---
name: zotero-tagging
description: >-
  Import literature into Zotero and apply the 154-term V2.1 controlled taxonomy
  (#Ａ１Type..#Ｅ１Method) with the ~ZTag-V2 marker. Use for literature import,
  tagging, targeted tag audits, and approved name migrations while preserving
  collection membership, user tags, reading states, and attachment relationships.
---

# Zotero 文献导入与标签管理

使用 **V2.1（154项）** 十维受控词表。分类服务精读分流、直接检索与结构化多选字段；名称使用熟悉的英文词、缩写和必要中文提示。

- [taxonomy.json](references/taxonomy.json)：唯一规范词表、稳定ID、逐词定义、名称映射与别名。
- [ZOTERO_TAG_SPEC.md](references/ZOTERO_TAG_SPEC.md)：分类边界、完整词表、ZoteroStyle显示规则。
- [pending_review.json](references/pending_review.json)：已有定点待核记录；日常维护保留其分类，内容复核按用户当前授权推进。
- [structured_fields.json](references/structured_fields.json)：十维多选字段映射设计，实际字段和选项ID在连接目标库后绑定。

## 阅读与归类

1. 先查重并确定唯一父条目。已有文献优先补充原条目；通过DOI、PMID等导入时优先使用Zotero元数据解析器。
2. 挂接已有或获准获取的全文附件，保持父条目和已有引用关联。
3. 阅读标题、摘要及能取得的全文，选择与核心研究对象、干预、机制、表型和关键方法相符的规范标签。证据不足的具体归类记入待核清单。
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
- 日常AI选用固定词表。新词提案说明实际检索用途、相关文献与现有分组的不足，集中审定后升级词表。
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
