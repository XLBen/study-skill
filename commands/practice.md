---
description: 习题化：课件出题、题目变式与逐题互动练习
agent: build
---

先调用 skill 工具加载 `study-flow`，按 @.opencode/skills/study-flow/SKILL.md 的练习规则执行。

范围与要求（课件主题/具体题目/题量题型）：$ARGUMENTS

先查 `questions/` 是否有老师原题：讲解或练习优先用原题，保留原题出处；没有官方答案就不得编造"官方解答"。课件输入从实际讲过的内容生成题并标注 AI-generated；题目输入生成同知识点变式。默认互动：一次只出一题、不展示答案，等用户作答后按规则评讲并指出具体误解。用户要求题集时保存到 `outputs/practice/`（题干与答案分区），顺手更新 `outputs/kb/index.md` 涉及的知识点行。范围不明先问。若 skill 工具不可用，以附入文档执行并说明。
