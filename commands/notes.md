---
description: 为课件或题目生成一页式笔记
agent: build
---

先调用 skill 工具加载 `study-flow`，按 @.opencode/skills/study-flow/SKILL.md 的笔记模板与来源规则执行。

笔记对象（课件/讲次/主题/题目）：$ARGUMENTS

从 `slides/` 或 `questions/` 定位目标；目标不唯一时询问。实际读取材料，关键的图表或公式需要核对；先查 `outputs/notes/` 是否已有同主题笔记再新建。按模板生成一屏内笔记：元信息（日期/来源/覆盖范围/标签）、一句话主线、关键点（每条带页码或题号）、公式与图（题目笔记可换成易错点）、自检问题、未核实处。保存为 `outputs/notes/YYYY-MM-DD-<slug>.md` 并回读确认；顺手更新 `outputs/kb/index.md` 对应知识点行；回复给摘要、路径与覆盖范围。不要凭文件名编造笔记。若 skill 工具不可用，以附入文档执行并说明。
