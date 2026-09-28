# Study Flow

一个面向大学课程的 OpenCode 学习 skill：以课件为课程范围依据，按需查阅参考书，用老师提供的题目练习，并区分外部试卷和生成题。每门课只需一份 `SKILL.md`；自然语言提出需求即可，不必记住阶段命令。

## 安装到一门课

将本仓库的 [`skills/study-flow/SKILL.md`](skills/study-flow/SKILL.md) 复制到课程文件夹的 `.opencode/skills/study-flow/SKILL.md`；推荐同时将 [`commands/`](commands/) 中的 Markdown 命令文件复制到该课程文件夹的 `.opencode/commands/`，以明确触发 skill。按需建立以下资料目录：

```text
<课程文件夹>/
├── .opencode/skills/study-flow/SKILL.md
├── .opencode/commands/     # 可选：显式加载 skill 的快捷命令
├── slides/        # 本课程课件、讲义、课程说明
├── readlist/      # 参考书和指定阅读；不是全书考点清单
├── questions/     # 老师题目、worksheet、答案及收集的试卷
└── outputs/       # 仅放生成内容，可单独清理或转移
```

在课程文件夹中启动 OpenCode；安装或修改 skill 后重新启动 OpenCode。每门课独立存放材料与输出，不要把原始书籍、课件或练习文件提交到这个 skill 仓库。

## 怎么提问

可以直接使用自然语言；也可以使用已安装的快捷命令（这些是真正的 OpenCode `/命令`，均接收后续文字作为参数）：

| 命令 | 用途 | 示例 |
| --- | --- | --- |
| `/study` | 通用学习请求 | `/study 对照课件解释这节课的关键概念` |
| `/preview` | 预习目标课件 | `/preview 下一讲` |
| `/digest` | 课件速读 | `/digest 第 2 讲` |
| `/notes` | 快速生成带出处的课件笔记 | `/notes 第 2 讲` |
| `/reading` | 查参考书及章节 | `/reading 课件中某个概念对应书的哪一章` |
| `/practice` | 老师题目或生成题逐题练习 | `/practice 已学章节，先问我再给答案` |
| `/exam-search` | 核实相似或本课程试卷 | `/exam-search 本周课件涵盖的知识点` |

命令会先加载 `study-flow`，再按当前课程文件夹的资料实际执行；无参数或目标不明确时会询问范围。以下是不依赖快捷命令的自然语言示例：

| 需求 | 示例 |
| --- | --- |
| 预习课件 | `用 study-flow 预习 slides/ 中下节课的课件，先讲先修概念和课堂重点。` |
| 速读与理解 | `速读第二讲课件，列出概念、公式和图表要点，并标出页码。` |
| 对照参考书 | `这张课件里的概念没看懂，查 readlist/ 中对应的章节解释，并区分课件和书的内容。` |
| 练老师的题 | `从 questions/ 选两道与本周课件相关的题，一次问一道，等我回答再讲解。` |
| 生成练习 | `按已讲范围生成五道练习题，题目和解析分开，并注明是生成题。` |
| 查找相似试卷 | `先核对已学范围，再找能验证来源的类似课程试卷；不要把别的课的题叫本课真题。` |
| 建参考书索引 | `只为目前讲到的课件建立参考书章节定位，不需要速读整本书。` |

简单问题可直接在聊天中回答；快速笔记、较完整的分析、练习题集、外部题目检索结果和可复用缓存保存在 `outputs/` 下。需要时分别建立 `notes/`、`analysis/`、`practice/`、`exam-search/`、`cache/` 子目录。`/notes` 默认生成一讲一页式 Markdown，写明来源、覆盖页码、关键概念、自检题和未核实事项；其他保存的结果也需标注证据位置。参考书通常先建立章节定位，反复使用时才考虑缓存带页码文本；重要公式和图仍核对原文。

## 来源与许可

skill 中摘录并适配了 [sanyuan0704/sanyuan-skills](https://github.com/sanyuan0704/sanyuan-skills)、[seb1n/awesome-ai-agent-skills 的 note-taking](https://github.com/seb1n/awesome-ai-agent-skills/tree/main/productivity-and-workflow/note-taking) 与 [ZeKaiNie/universal-examprep-skill](https://github.com/ZeKaiNie/universal-examprep-skill) 的部分方法。具体版本链接、改编说明和 MIT 许可文字见 [`SKILL.md`](skills/study-flow/SKILL.md)。
