---
description: 为课件或题目生成讲透式笔记（固定三段版式 + 原图嵌入 + 易错点清单）
agent: build
---

先调用 skill 工具加载 `study-flow`，按 @.opencode/skills/study-flow/SKILL.md 的"卡片家族与统一读者版式"执行。

笔记对象（课件/讲次/主题/题目）：$ARGUMENTS

从 `slides/` 或 `questions/` 定位目标并实际读取；先查 `outputs/notes/` 是否已有同主题笔记再新建。课件笔记按判型选卡后，用**固定三段版式**输出：核心定义与数学表达（跟随课件形式化程度，符号当句解释）→ 直观物理内核（挂 `outputs/kb/analogy.md` 的课程级比喻系统，首次生成时选型写入）→ 定量推导实例（完整算例/状态轨迹/失效样本诊断，末尾独立验算）；末尾加"易错点清单"（普遍误解→核心破析→具体实例；素材：课件→互联网检索→省略，不凭空生成）。配图用 skill 自带脚本 `scripts/extract_figures.py` 提取课件/书本原图（书本用 --caption 锚定）存 `outputs/notes/assets/<slug>/`，禁止 ASCII 结构图；术语首现简约标 `中文（English）`；知识点在 `readlist/` 有对应时必标书名+章节+页码。写完过行文检查再保存为 `outputs/notes/YYYY-MM-DD-<slug>.md` 并回读确认；顺手更新 `outputs/kb/index.md`；回复给摘要、路径与覆盖范围。题目笔记走 question-note 流程。若 skill 工具不可用，以附入文档执行并说明。
