---
description: 讲解课件内容或具体题目
agent: build
---

先调用 skill 工具加载 `study-flow`，规则见 @.opencode/skills/study-flow/SKILL.md。

要讲解的对象（课件页/主题/题目）：$ARGUMENTS

从 `slides/` 或 `questions/` 定位目标材料并实际读取：课件对象讲概念、公式、图、先修与假设；题目对象先拆题意与考点，再给解法思路；用户只要提示时逐步给提示。按需查 `readlist/` 补充并标明"参考书来源"，与课件说法分开。讲解默认在聊天中给出，引用 文件+页码/题号；需要留档时保存到 `outputs/notes/` 或按用户指定位置。顺手更新 `outputs/kb/index.md` 中涉及的知识点行。目标不明确时先问。若 skill 工具不可用，以附入文档执行并说明。
