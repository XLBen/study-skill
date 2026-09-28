---
description: 为课件或题目生成讲透式笔记（按知识点类型选卡片）
agent: build
---

先调用 skill 工具加载 `study-flow`，按 @.opencode/skills/study-flow/SKILL.md 的"卡片家族与讲解质量规则"执行。

笔记对象（课件/讲次/主题/题目）：$ARGUMENTS

从 `slides/` 或 `questions/` 定位目标并实际读取（关键图表或公式需要核对）；先查 `outputs/notes/` 是否已有同主题笔记再新建。课件笔记先给每个知识点判型选卡（概念/公式定理/算法/模型架构/对比/案例证据/背景叙事），按对应卡片模板写：课件原文引用块（页码）、直觉讲解（比喻带失效点）、正式表述、完整例子（含独立验算）、易错边界；知识点在 `readlist/` 有对应时必标书名+章节+页码。长度不限，讲透为准。写完过一遍行文检查（去填充语、bullet 长短混排、术语统一）再保存为 `outputs/notes/YYYY-MM-DD-<slug>.md`，回读确认；顺手更新 `outputs/kb/index.md` 对应知识点行；回复给摘要、路径与覆盖范围。题目笔记走 question-note 流程。若 skill 工具不可用，以附入文档执行并说明。
