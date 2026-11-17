# zotero-tagging

面向生物医药与生物材料领域的 Zotero 文献导入与受控打标 Skill。V2.1 提供 154 项 L0–L4 十维正交词表（`ZT-001`–`ZT-154`），服务精读分流、Zotero 多级检索与飞书多维表格同步。

## 核心特性

- **L0–L4 十维正交体系**：Type、Disease、Surgery、Material、Carrier、Drug、Target、Mechanism、Phenotype、Method。
- **精读直接分流**：`#Ａ１Type` 每篇严格唯一，`Article` 直接区分 `Mechanistic` / `Biomaterial` / `DeviceEvaluation`，`Clinical` 六选一（`RCT` / `CaseControl` / `Prospective` / `Retrospective` / `CrossSectional` / `CaseReport`）。
- **按需查词与胶囊兼容**：`query_taxonomy.py` 支持维度、多词检索、品牌/中英文别名与稳定 ID 查询；命名严格兼容 ZoteroStyle 彩色胶囊正则与多级树排序。
- **保留式硬校验**：`validate_tags.py` 自动附带 `~ZTag-V2` 处理标记，硬性拦截非法词、多 `Type`、状态冲突及父子共标（「就细不就粗」），同时完整保留用户自定义标签与阅读状态。
- **结构化多选映射**：随 Skill 提供十维多选字段与选项 ID 映射模板（`structured_fields.json`）。

## 安装

使用 Skills CLI 一键安装：

```bash
npx skills add CMD-cmd/zotero-tagging
```

或获取本仓库后，将 `skills/zotero-tagging` 复制到对应 Agent 的全局 `skills/` 目录。

## 使用条件

本地运行 Zotero 并连接 Zotero MCP 服务（具备 `add_by_identifier`、`write_item`、`write_tag`、`get_item_details`、`get_content` 等读写工具）。推荐配合 **ZoteroStyle** 插件展示十维标签树与列表胶囊。

入库与更新严格遵循三步顺序：**锁定唯一父条目 ➔ 挂齐全文附件 ➔ 读取内容、过校验并写入回读**。

## 按需查询词表

AI 先获取小型维度索引，再按当前文献需求查询候选词条与边界定义，不向上下文倾倒整份词表：

```bash
python3 skills/zotero-tagging/scripts/query_taxonomy.py
python3 skills/zotero-tagging/scripts/query_taxonomy.py --dimension A1 --dimension C1
python3 skills/zotero-tagging/scripts/query_taxonomy.py --query "GelMA 水凝胶"
python3 skills/zotero-tagging/scripts/query_taxonomy.py --id ZT-050
```

## 校验与回归测试

写入 Zotero 前通过 Python 3 标准库脚本校验并生成精确差异 `diff`：

```bash
python3 skills/zotero-tagging/scripts/validate_tags.py \
  --mode replace-managed \
  --existing '["/unread", "自定义标签"]' \
  --tags '#Ａ１Type/Article 论著/Biomaterial 生物材料研究' \
         '#Ｂ１Disease/BoneDefect 骨缺损与拔牙窝创伤'
```

- `--mode add`（默认）：增量补标并保留已有分类、自定义标签及阅读状态。
- `--mode replace-managed`：仅全量替换本词表管理的 `#` 标签与已知旧名，保留其余用户标签与阅读状态。
- `--mode rename-only`：仅按 `rename_map` 映射已改名的词表标签，保持原归属与标记不变。
- `--status /unread|/reading|/Done`：显式切换阅读状态。

运行全套单元测试：

```bash
python3 -m unittest discover -s skills/zotero-tagging/tests -v
```

## 文件结构

- `skills/zotero-tagging/SKILL.md`：Agent 执行入口、按需查词、五条铁规则与三大 MCP 工作流。
- `skills/zotero-tagging/references/taxonomy.json`：154 项规范标签、稳定 ID、定义、中英文别名与旧名称映射。
- `skills/zotero-tagging/references/ZOTERO_TAG_SPEC.md`：L0–L4 架构说明、稀疏激活模板与全量受控词表。
- `skills/zotero-tagging/references/structured_fields.json`：十维结构化多选字段映射模板。
- `skills/zotero-tagging/scripts/query_taxonomy.py`：按维度、多词关键词、别名或 ID 查询词表。
- `skills/zotero-tagging/scripts/validate_tags.py`：写入前硬校验与差异生成脚本。
- `skills/zotero-tagging/tests/test_query_taxonomy.py`、`test_validate_tags.py`：词表、查询与校验器单元测试。

## License

MIT License
