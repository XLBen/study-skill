---
description: 为课件或题目生成讲透式笔记（按知识点类型选卡片，统一版式）
agent: build
---

先调用 skill 工具加载 `study-flow`，按 @.opencode/skills/study-flow/SKILL.md 的"卡片家族与讲解质量规则"执行。

笔记对象（课件/讲次/主题/题目）：$ARGUMENTS

从 `slides/` 或 `questions/` 定位目标并实际读取；先查 `outputs/notes/` 是否已有同主题笔记再新建。课件笔记先给每个知识点判型选卡（概念/公式定理/算法/模型架构/对比/案例证据/背景叙事），然后**按统一读者版式输出**：导读两三句、H2 知识点、原文引用块标一次页码、首段人话总结、术语首现标课件原词、符号当句解释、例子独立小节含独立验算、末尾斜体来源行与术语表。图按图片政策：优先用 pdftoppm 提取课件/书本原图存 `outputs/notes/assets/<slug>/`，禁止 ASCII 结构图；工具缺失就写"见课件 p.N"。知识点在 `readlist/` 有对应时必标书名+章节+页码。长度不限，讲透为准。写完过行文检查再保存为 `outputs/notes/YYYY-MM-DD-<slug>.md` 并回读确认；顺手更新 `outputs/kb/index.md`；回复给摘要、路径与覆盖范围。题目笔记走 question-note 流程。若 skill 工具不可用，以附入文档执行并说明。
