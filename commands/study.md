---
description: study-flow：任意课程学习任务，按需组合讲解/笔记/练习/查书
agent: build
---

先调用 skill 工具加载 `study-flow`，规则见 @.opencode/skills/study-flow/SKILL.md。

目标与要求：$ARGUMENTS

按 skill 的三类操作（讲解/笔记/习题化）判断本次主操作，允许按需组合辅助能力（如讲解中补一段笔记、查参考书、找相似试卷），并在回复中说明组合了什么。只使用本课程 `slides/`、`readlist/`、`questions/` 与已有 `outputs/`；先读真实材料并标注出处。需要保存的成果按 skill 约定写入 `outputs/`（笔记 `notes/`、题集 `practice/`），并顺手更新 `outputs/kb/index.md` 对应知识点行。回复给出结论、已核对范围、保存路径与未核实处。未给目标时，先简要列出可选材料并询问要处理什么。若 skill 工具不可用，以附入文档执行并说明加载状态。
