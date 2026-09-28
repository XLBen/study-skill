---
description: 从老师题目或已讲课件开始逐题练习
agent: build
---

先调用 skill 工具加载 `study-flow`，使用 @.opencode/skills/study-flow/SKILL.md 的练习与来源区分规则。

范围、题型、题量及额外要求：$ARGUMENTS

先查当前课程 `questions/` 中有无匹配的老师题目，再根据已检查的 `slides/` 补充 AI 生成题。严格区分老师原题、AI 生成题，以及老师答案与 AI 推导答案；不要编造“官方解答”。默认互动模式：一次只展示 1 道题、不提前展示答案，等待用户作答后再评价、给提示与讲解；用户明确要求一次生成题集时再按 skill 格式将题干与答案分开保存到 `outputs/practice/` 并给路径。无明确范围且无法选题时先询问。若 skill 工具不可用，以附入的文档执行并说明。
