---
description: 从课件快速生成一份带来源的结构化学习笔记
agent: build
---

先调用 skill 工具加载 `study-flow`，阅读 @.opencode/skills/study-flow/SKILL.md 的 “Fast lecture notes” 和来源规则，再实际执行。

笔记目标、范围和格式偏好：$ARGUMENTS

从当前课程 `slides/` 找到目标课件；目标不唯一时询问，不默认遍历整门课。读取该课件的实际内容并检查对笔记关键的图表或公式。依照 skill 中借鉴的 note-taking 方法：先查 `outputs/notes/` 是否已有同主题笔记，再生成紧凑 Markdown，包含日期/来源/覆盖页范围/标签、一句话主线、要点、必要的公式或图、自检问题及未核实处。每项关键内容附原始页码或幻灯片号；默认不速读整本 `readlist/`。将文件保存在 `outputs/notes/` 并回读确认，再给用户摘要、文件路径和覆盖范围；不要只列计划或凭文件名编造笔记。若 skill 工具不可用，以附入的 skill 文档为执行依据并说明。
