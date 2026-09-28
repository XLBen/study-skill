# Study Flow

一个面向大学课程的 OpenCode 学习 skill：以课件为课程范围依据，按需查阅参考书，用老师提供的题目练习，并区分外部试卷和生成题。每门课只需一份 `SKILL.md`；自然语言提出需求即可，不必记住阶段命令。

## 安装到一门课

将本仓库的 [`skills/study-flow/SKILL.md`](skills/study-flow/SKILL.md) 复制到课程文件夹的 `.opencode/skills/study-flow/SKILL.md`，并按需建立以下资料目录：

```text
<课程文件夹>/
├── .opencode/skills/study-flow/SKILL.md
├── slides/        # 本课程课件、讲义、课程说明
├── readlist/      # 参考书和指定阅读；不是全书考点清单
├── questions/     # 老师题目、worksheet、答案及收集的试卷
└── outputs/       # 仅放生成内容，可单独清理或转移
```

在课程文件夹中启动 OpenCode；安装或修改 skill 后重新启动 OpenCode。每门课独立存放材料与输出，不要把原始书籍、课件或练习文件提交到这个 skill 仓库。

## 怎么提问

直接使用自然语言；下列是示例，不是需要安装的斜杠命令：

| 需求 | 示例 |
| --- | --- |
| 预习课件 | `用 study-flow 预习 slides/ 中下节课的课件，先讲先修概念和课堂重点。` |
| 速读与理解 | `速读第二讲课件，列出概念、公式和图表要点，并标出页码。` |
| 对照参考书 | `这张课件里的概念没看懂，查 readlist/ 中对应的章节解释，并区分课件和书的内容。` |
| 练老师的题 | `从 questions/ 选两道与本周课件相关的题，一次问一道，等我回答再讲解。` |
| 生成练习 | `按已讲范围生成五道练习题，题目和解析分开，并注明是生成题。` |
| 查找相似试卷 | `先核对已学范围，再找能验证来源的类似课程试卷；不要把别的课的题叫本课真题。` |
| 建参考书索引 | `只为目前讲到的课件建立参考书章节定位，不需要速读整本书。` |

简单问题可直接在聊天中回答；较完整的笔记、练习题集、外部题目检索结果和可复用缓存保存在 `outputs/` 下。需要时分别建立 `analysis/`、`practice/`、`exam-search/`、`cache/` 子目录。保存的 Markdown 会写明范围、核心结论、证据位置、分析或题目、未核实事项。参考书通常先建立章节定位，反复使用时才考虑缓存带页码文本；重要公式和图仍核对原文。

## 来源与许可

skill 中摘录并适配了 [sanyuan0704/sanyuan-skills](https://github.com/sanyuan0704/sanyuan-skills) 与 [ZeKaiNie/universal-examprep-skill](https://github.com/ZeKaiNie/universal-examprep-skill) 的部分方法。具体版本链接、改编说明和 MIT 许可文字见 [`SKILL.md`](skills/study-flow/SKILL.md)。
