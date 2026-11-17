# zotero-tagging

面向生物医药与生物材料领域的 Zotero 文献自动导入与 V2.0 十维正交多级打标 Agent Skill，适配 Claude Code、Codex、Antigravity、Cursor 等多平台 AI Agent，配合 `zotero-mcp-plugin`（或兼容 Zotero MCP 服务）实现「文献导入 → 附件挂接 → 受控词表精准打标」一体化流程。

## 核心特性

1. **L0→L4 全角序十维正交词表（153 个受控标签）**
   - 顶层按科研因果与阅读逻辑自然排序：`#Ａ１Type` → `#Ｂ１Disease` → `#Ｂ２Surgery` → `#Ｃ１Material` → `#Ｃ２Carrier` → `#Ｃ３Drug` → `#Ｄ１Target` → `#Ｄ２Mechanism` → `#Ｄ３Phenotype` → `#Ｅ１Method`（无空格全角前缀，兼容 Zotero Style 多级树状展示）。
   - `#Ａ１Type` 严格排他唯一；采用三级叶节点优先（就细不就粗）与 MeSH Major Topic 原则。
2. **AI 打标区分标记 `~ZTag-V2`**
   - 每篇完成 V2.0 打标的条目统一附带普通平铺标签 `~ZTag-V2`（不进入 `#` 多级树或 `/` 状态目录），可在 Zotero 高级筛选通过「`标签` `不包含` `~ZTag-V2`」瞬间筛选未标注或新增条目。
3. **无损导入、挂附件与打标闭环**
   - 严格执行「锁定唯一父条目 → 挂齐 PDF 附件 → 读取全文内容并写入标签与 `~ZTag-V2`」，涵盖本地 PDF 导入、按研究主题批量检索入库、存量文献增量补标三类工作流，并在写入前保护既有 `/Done`、`/reading`、`/unread` 状态与用户自定义标签。
4. **零依赖本地校验器**
   - 内置 `scripts/validate_tags.py`，在写入前强制检验词表白名单、单一 `#Ａ１Type/*` 与叶节点唯一性。

## 快速安装

### 方式一：使用 `skills` CLI 一键安装（推荐）

```bash
npx skills add CMD-cmd/zotero-tagging
```

### 方式二：手动克隆到对应 Agent 的 Skills 目录

- **Codex**：
  ```bash
  git clone https://github.com/CMD-cmd/zotero-tagging.git /tmp/zotero-tagging && cp -R /tmp/zotero-tagging/skills/zotero-tagging ~/.agents/skills/ && rm -rf /tmp/zotero-tagging
  ```
- **Claude Code**：
  ```bash
  git clone https://github.com/CMD-cmd/zotero-tagging.git /tmp/zotero-tagging && cp -R /tmp/zotero-tagging/skills/zotero-tagging ~/.claude/skills/ && rm -rf /tmp/zotero-tagging
  ```
- **Antigravity**：
  ```bash
  git clone https://github.com/CMD-cmd/zotero-tagging.git /tmp/zotero-tagging && cp -R /tmp/zotero-tagging/skills/zotero-tagging ~/.gemini/config/skills/ && rm -rf /tmp/zotero-tagging
  ```
- **Cursor**：
  ```bash
  git clone https://github.com/CMD-cmd/zotero-tagging.git /tmp/zotero-tagging && cp -R /tmp/zotero-tagging/skills/zotero-tagging ~/.cursor/skills/ && rm -rf /tmp/zotero-tagging
  ```

## 前置条件

- 本地运行 Zotero（推荐配合 Zotero Style 多级标签插件显示十维层级树）；
- 已配置可写入的 Zotero MCP 工具（如 `zotero-mcp-plugin`，具备 `add_by_identifier`、`write_item`、`write_tag`、`get_item_details`、`get_content` 等工具）。

## 目录结构

```text
zotero-tagging/
├── README.md
├── LICENSE
└── skills/
    └── zotero-tagging/
        ├── SKILL.md
        ├── references/
        │   ├── ZOTERO_TAG_SPEC.md
        │   └── taxonomy.json
        └── scripts/
            └── validate_tags.py
```

## License

MIT License
