# zotero-tagging

面向生物医药与生物材料领域的 Zotero 文献导入与受控打标 Skill。V2.1 提供154项十维标签，服务精读分流、文献检索与结构化多选字段。

## 核心特性

- 十个维度：Type、Disease、Surgery、Material、Carrier、Drug、Target、Mechanism、Phenotype、Method。
- Article直接分为Mechanistic、Biomaterial、DeviceEvaluation；Clinical使用RCT、Prospective、Retrospective、CrossSectional、CaseReport、CaseControl六个入口。
- 名称采用熟悉英文词、缩写和必要中文提示，配有稳定ID、定义及精确名称映射。
- `~ZTag-V2`继续作为V2系列处理标记，词表版本单独记录。
- 校验器支持增补、受控分类替换和仅名称迁移，保留用户自定义标签及阅读状态。
- 十维标签可映射为十个多选字段；字段模板随Skill提供。

## 安装

使用已有的skills CLI安装方式：

```bash
npx skills add CMD-cmd/zotero-tagging
```

也可获取本仓库，将`skills/zotero-tagging`目录复制到Agent的Skills目录。

## 使用条件

本地运行Zotero，并连接可读取和写入标签的Zotero MCP服务。典型工具包括`add_by_identifier`、`write_item`、`write_tag`、`get_item_details`和`get_content`。ZoteroStyle可展示多级标签树和标签列。

先确定唯一文献条目，挂接附件并读取文献内容，再按受控词表选择标签。写入前检查拟新增、移除和保留的标签，写后回读。

## 校验

Python 3标准库即可运行：

```bash
python3 skills/zotero-tagging/scripts/validate_tags.py \
  --existing '["/unread"]' \
  --tags '#Ａ１Type/Article 论著/Biomaterial 生物材料研究' \
         '#Ｂ１Disease/BoneDefect 骨缺损与拔牙窝创伤'
```

- 默认`add`：增补受控标签并保留现有标签。
- `--mode replace-managed`：仅替换词表管理的分类，保留其他用户标签。
- `--mode rename-only`：执行精确名称映射并保持标签归属。
- `--status /Done`：显式转换阅读状态。

校验结果包含`valid`、`errors`、`warnings`、`final_tags`和`diff`。校验器生成建议结果，Zotero写入由Agent通过连接工具完成。

运行回归检查：

```bash
python3 -m unittest discover -s skills/zotero-tagging/tests -v
```

## 文件

- `SKILL.md`：工作流程与分类边界。
- `references/taxonomy.json`：154项规范标签、稳定ID、定义和旧名称映射。
- `references/ZOTERO_TAG_SPEC.md`：完整标签规范与显示规则。
- `references/pending_review.json`：待核记录模板。
- `references/structured_fields.json`：十维多选字段映射。
- `scripts/validate_tags.py`：保留式标签校验。

## License

MIT License
