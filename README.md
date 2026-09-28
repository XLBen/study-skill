# Study Flow

一个通用的 OpenCode 学习 skill：围绕你正在学习的**知识点**答疑、练习，并在需要时写成可独立阅读的个人博客式笔记。知识解释优先依据指定书籍，课件用来定位课程范围、术语与题目；教材没有覆盖的内容由课件补足。书籍和课件的例子仍讲不清时，才去找可靠的网络教学实例，最后再用标明来源的自拟例子。

默认跳过课件中的考试安排、评分比例等行政内容；专门询问时照实回答。自然语言即可使用，不需要固定笔记模板或统一比喻。

## 安装

在任意目录克隆本仓库，指定希望使用 skill 的项目目录（需要 Python 3）：

```bash
git clone https://github.com/XLBen/study-skill.git
python3 study-skill/scripts/install.py /path/to/project
```

脚本安装 `skills/study-flow/` 中的 skill 和图片提取脚本，以及 `commands/` 中的快捷命令。已有文件默认跳过；需要把旧版更新为本版时使用 `--force`，更新前先检查是否改过本地副本。安装或更新后重启 OpenCode。

也可以手动复制 `skills/study-flow/` 到项目的 `.opencode/skills/study-flow/`，并按需复制 `commands/*.md` 到 `.opencode/commands/`。只装 skill 也可直接用自然语言请求答疑或笔记。

材料目录按实际课程情况决定；以下仅是可选约定：

```text
project/
├── .opencode/skills/study-flow/   # SKILL.md、可选图片脚本
├── .opencode/commands/            # 可选快捷命令
├── readlist/                       # 指定书籍、阅读材料
├── slides/                         # 课件
├── questions/                      # 老师题目及答案
└── outputs/                        # 仅按需保存生成的笔记、题集等
```

**本仓库只放通用 skill、脚本与命令；不要提交任何课程材料、书籍或生成的笔记。**

## 使用

直接提问即可，例如“解释这本书中某个知识点”“讲讲这道题”“把这个知识点写成一篇笔记”。简单问答默认留在聊天里，明确要求笔记或题集时才存入 `outputs/`。

| 可选命令 | 用途 |
| --- | --- |
| `/study` | 根据请求答疑、整理知识点或练习 |
| `/explain` | 讲解指定知识点、公式、图或题目 |
| `/notes` | 把知识点或指定范围写成文章式笔记 |
| `/practice` | 逐题互动或按要求生成题集 |

PDF 图片提取脚本需要 PyMuPDF（`pip3 install pymupdf`）；没有它仍可讲解和写笔记，需要原图时回原页核对并注明未能嵌入。使用了书籍、课件、网页、老师答案或 AI 自拟实例时，分别注明实际核对的来源。

## 来源与许可

skill 借鉴的上游方法、改编说明与许可证信息见 [`SKILL.md`](skills/study-flow/SKILL.md)。
