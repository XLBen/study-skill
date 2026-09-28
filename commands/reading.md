---
description: 按课件需要查询参考书、定位章节或精读片段
agent: build
---

先调用 skill 工具加载 `study-flow`，遵守 @.opencode/skills/study-flow/SKILL.md 的参考书按需阅读和缓存规则。

要查的概念、参考书或课件关联：$ARGUMENTS

在当前课程 `readlist/` 中寻找相应参考书，结合相关 `slides/` 定位需要的章节/页；只读当前问题需要的部分，不把初次索引冒充整书精读。若要建章节索引，保存到 `outputs/cache/`；若要解释或对比，保存有价值的完整分析到 `outputs/analysis/`。列明课程课件与书分别支持什么、实际看过的页码以及缓存是否仅为索引/提取文本；重要公式与图回查原文。参考书或主题不明确时先询问。若 skill 工具不可用，以附入的文档执行并说明。
