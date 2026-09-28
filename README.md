# Study Flow

一个面向大学课程的 OpenCode 学习 skill。核心模型：**两类输入（课件、题目）× 三类操作（讲解、笔记、习题化）**，外加一个把习题—课件—笔记—参考书串起来的轻量索引。自然语言即可使用，不必记住一堆阶段命令。

## 安装到一门课

将本仓库的 [`skills/study-flow/SKILL.md`](skills/study-flow/SKILL.md) 复制到课程文件夹的 `.opencode/skills/study-flow/SKILL.md`；推荐同时将 [`commands/`](commands/) 中的 Markdown 命令文件复制到该课程文件夹的 `.opencode/commands/`。按需建立以下资料目录：

```text
<课程文件夹>/
├── .opencode/skills/study-flow/SKILL.md
├── .opencode/commands/     # 可选：study / explain / notes / practice
├── slides/        # 本课程课件、讲义、课程说明
├── readlist/      # 参考书和指定阅读；按需查阅，不是考点清单
├── questions/     # 老师题目、worksheet、答案及收集的试卷
└── outputs/       # 仅放生成内容：notes/ practice/ kb/ cache/
```

在课程文件夹中启动 OpenCode；安装或修改 skill 后重新启动 OpenCode。每门课独立存放材料与输出，不要把原始书籍、课件或练习文件提交到这个 skill 仓库。

## 怎么用

| 命令 | 用途 | 示例 |
| --- | --- | --- |
| `/study` | 任意学习任务（含找相似试卷等） | `/study 帮我找和本周课件相关的真题` |
| `/explain` | 讲解课件内容或具体题目 | `/explain 课件里的感知机收敛定理`、`/explain 这道题怎么做` |
| `/notes` | 为课件或题目生成一页式笔记 | `/notes 第 2 讲`、`/notes 把这道错题整理成笔记` |
| `/practice` | 课件出题 / 题目变式 / 逐题互动 | `/practice 已学章节，一次一题` |

每个入口都能接收课件或题目；执行中按需组合辅助能力（讲解时查参考书、练习时更新索引），并在回复中说明。不使用命令、直接自然语言描述也可以。

## 知识库索引

`outputs/kb/index.md` 是唯一的跨材料登记处，每个知识点一行：

```text
知识点 → 课件 文件+页 → 笔记 → 题目 文件+题号 → 参考书 章节+页（已核对）
```

生成笔记或练习时**顺手**更新对应行，不专门"建库"；只登记实际核对过的链接，未查的书页留空、仅主题相近的关联标"待核对"；索引只是检索入口，答题前仍回原文核对。

## 输出与来源约定

`outputs/notes/` 存一页式笔记（含来源与覆盖页码）；`outputs/practice/` 存题集（题干与答案分区，标注 teacher-provided / AI-generated）；`outputs/cache/` 存参考书定位与带页码缓存。题目永远区分老师原题、相似课程真题与生成题；他课试卷不冒充本课往年题；搜不到就如实报告。

## 来源与许可

skill 中摘录并适配了 [sanyuan0704/sanyuan-skills](https://github.com/sanyuan0704/sanyuan-skills)、[seb1n/awesome-ai-agent-skills 的 note-taking](https://github.com/seb1n/awesome-ai-agent-skills/tree/main/productivity-and-workflow/note-taking) 与 [ZeKaiNie/universal-examprep-skill](https://github.com/ZeKaiNie/universal-examprep-skill) 的部分方法。具体版本链接、改编说明和 MIT 许可文字见 [`SKILL.md`](skills/study-flow/SKILL.md)。
