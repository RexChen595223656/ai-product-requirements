# AI Product Requirements
# AI 产品需求助手

A reusable Skill for turning rough AI product ideas into structured requirement deliverables.
一个把模糊 AI 产品想法整理成标准需求交付物的可复用 Skill。

[English](#english) | [中文](#中文)

## Table of contents

- [English](#english)
- [Quick overview](#quick-overview)
- [Who should use this](#who-should-use-this)
- [Common use cases](#common-use-cases)
- [Before and after](#before-and-after)
- [Installation](#how-to-install-this-skill-into-codex)
- [How this differs from superpowers](#how-this-differs-from-superpowers)
- [中文](#中文)

## English

`AI Product Requirements` is a reusable Skill package for Codex-style local agent workflows.

If that sentence feels abstract, here is the plain version:

- You have an AI product idea, but it is still messy
- Or you already wrote something, but it is incomplete
- Or you have feedback, tickets, or interview notes, but they are not yet usable as product requirements
- This Skill helps turn those inputs into structured product outputs that a team can actually work with

In practice, this Skill helps you move from:

```text
rough idea / scattered feedback / incomplete PRD
→ clearer requirement analysis
→ more buildable product logic
→ better tracking, analytics, admin, and launch planning
```

This is not a one-shot PRD writer.
It is a workflow helper for AI product definition, review, and refinement.

## Quick overview

| Item | Summary |
|---|---|
| What it is | A Codex Skill for structured AI product requirement outputs |
| Best for | Requirement analysis, PRD review, rules, tracking, analytics, admin requirements |
| Not best for | Open-ended brainstorming or general project ideation |
| Works with | Codex directly, Claude Code as a workflow reference |
| Main value | Makes AI product outputs more consistent, structured, and operational |

### What this Skill is for

Use this Skill when you already want a clear product deliverable, for example:

- requirement analysis
- AI or Agent fit assessment
- PRD review
- functional rules
- tracking requirements
- analytics planning
- admin console requirements
- launch-readiness checklist

### What this Skill is not for

Do not use this as your first tool for:

- open-ended brainstorming
- generic ideation
- "help me think about this project"
- broad workflow planning

For those cases, a process skill such as `superpowers` should lead first.

### Fast mental model

- `superpowers` handles process
- `ai-product-requirements` handles deliverables

If the question is:

- "How should we think about this?" -> process skill
- "Please output the requirement analysis / review / tracking spec" -> this skill

### Quick start in 3 steps

1. Copy `skill/` into:

```text
~/.codex/skills/ai-product-requirements/
```

2. Restart Codex
3. Try:

```text
Help me break this AI idea into requirement analysis
Review this AI PRD
Write tracking requirements for this feature
```

## Common use cases

People usually use this Skill for a few repeated situations:

### Use case 1: A vague AI feature idea

You have an idea, but it is still too loose for engineering or product review.
You want a structured requirement analysis instead of another loose brainstorm.

### Use case 2: An existing AI PRD that feels incomplete

You already have a document, but it is missing:

- functional rules
- event tracking
- analytics design
- fallback logic
- admin-side operations

### Use case 3: AI vs Agent decision

You need a more rigorous answer than "this sounds like an Agent".
You want a structured judgment based on autonomy, tool use, approval points, and workflow complexity.

### Use case 4: Launch preparation

You need the operational layer, not just feature copy:

- tracking requirements
- dashboard design
- admin requirements
- risk and fallback
- launch readiness

## Before and after

### Before

```text
We want to build an AI customer support feature for our team. Can you help write something?
```

### After

This Skill is designed to push that into outputs such as:

- a requirement analysis with target users, scenarios, pain points, and opportunity
- an AI vs Agent fit assessment
- functional rules and acceptance logic
- tracking and analytics requirements
- risk and fallback design

That is the real point of the project: moving from vague product language to reusable working artifacts.

## Why this exists

Many AI product efforts fail for predictable reasons:

- the user problem is still vague
- AI is used where it is not actually needed
- PRDs stop at feature description and skip rules, data, metrics, and fallback
- Agent ideas are over-designed before the core value is proven

This project exists to reduce those failures and make AI product work more operational.

## What this repository contains

This repository contains two layers:

1. The actual installable Skill package
2. Supporting files used to validate and maintain the Skill

The installable part is the `skill/` directory.

The rest of the repository helps you understand, test, and improve the Skill.

## Who should use this

This Skill is meant for people working on AI products, especially:

- Product managers
- Founders
- AI feature owners
- Teams discussing whether something should become an Agent
- Product and engineering teams reviewing AI PRDs together

You will get the most value from it if you often face questions like:

- "This idea sounds interesting, but what problem are we actually solving?"
- "Is this even a good fit for AI?"
- "Should this be a normal AI feature or an Agent?"
- "This PRD is missing rules, metrics, or fallback logic"
- "We need a better launch plan for this AI feature"

## What the Skill can help produce

Depending on what you ask, the Skill can produce:

- Requirement analysis
- One-page summary
- AI solution design
- Agent design
- Functional rules
- Data recycling plan
- Tracking requirements
- Data analysis plan
- Admin console requirements
- Full AI PRD
- PRD review
- Evaluation and acceptance criteria
- Risk and fallback design
- Launch readiness checklist

## What kind of input you can give it

You do not need to start with a perfect spec.

The Skill can work from inputs such as:

- A rough feature idea
- A short product paragraph
- Interview notes
- Support tickets
- User complaints
- Competitor analysis notes
- Business goals
- Existing PRDs
- Existing AI solution drafts
- Existing Agent concepts

## What makes this Skill different from a normal prompt

A normal prompt often jumps straight into "write the PRD".

This Skill tries to slow that down in useful ways:

- It checks whether the problem is clear enough
- It checks whether AI is appropriate at all
- It distinguishes AI features from Agent workflows
- It pushes you to define rules, metrics, data loops, fallback, and operations
- It tries to produce outputs that are easier for a team to use directly

## How this differs from superpowers
In practice:

- Use `superpowers` when the task is still open-ended and you need help thinking, scoping, clarifying, or sequencing the work
- Use `ai-product-requirements` when you already want a structured AI product output such as requirement analysis, PRD review, functional rules, tracking requirements, analytics planning, or admin requirements

Another way to say it:

- If the question is "how should we think about this?" -> process skill
- If the question is "please output the document / review / rules / tracking spec" -> this skill

## Why people keep both skills installed

These two skills are useful together when their roles stay separate:

- `superpowers` helps structure the thinking process
- `ai-product-requirements` helps standardize the final AI product deliverable

That combination is often better than using either one alone.

## Default behavior

By default, the Skill follows these rules:

- Chinese prompts produce Chinese output
- English prompts produce English output
- Engineering identifiers stay in English
- Normal Chinese product documents use Chinese-only headings
- Bilingual headings are used only when clearly needed
- It does not assume every problem should become an AI feature
- It prefers lower-autonomy recommendations unless real Agent behavior is justified
- It should not take over generic brainstorming if another process skill is already guiding that phase

## Before you install

You need one of these environments:

### Option A: Codex

This is the most direct fit if you want to use the local `~/.codex/skills/` workflow.

Install:

```bash
npm install -g @openai/codex
```

Update:

```bash
codex --upgrade
```

Docs:

- [OpenAI Help: Codex CLI getting started](https://help.openai.com/en/articles/11096431)
- [OpenAI: Get started with Codex](https://openai.com/codex/get-started/)

### Option B: Claude Code

If your team already uses Anthropic's local CLI flow, you can still use the ideas and prompt workflow in this repository.

Install:

```bash
npm install -g @anthropic-ai/claude-code
```

Update:

```bash
claude update
```

Docs:

- [Anthropic Docs: Set up Claude Code](https://docs.anthropic.com/en/docs/claude-code/setup?asuniq=786d6f60)

### Which one should you pick

- Pick Codex if you want to use the packaged Skill directly with `~/.codex/skills/`
- Pick Claude Code if your team already runs that workflow and mainly wants the structure and prompts

## How to install this Skill into Codex

If you are using Codex, install the Skill like this:

### Step 1

Copy the contents of the `skill/` directory into:

```text
~/.codex/skills/ai-product-requirements/
```

Important:

- The folder name should be `ai-product-requirements`
- The installed folder should contain `SKILL.md` directly inside it

The final structure should look roughly like:

```text
~/.codex/skills/ai-product-requirements/
├── SKILL.md
├── agents/
├── assets/
├── references/
└── scripts/
```

### Step 2

Restart Codex.

### Step 3

Open a new chat and test with a real prompt.

Examples:

```text
Help me break this AI idea into requirement analysis
Is this better as an Agent or a normal AI feature?
Review this AI PRD
Write tracking requirements for this feature
What data should we recycle after launch?
```

## How to tell whether installation worked

A successful test usually looks like this:

- The Skill triggers automatically when the prompt matches
- The output format matches the request
- The language matches your prompt language
- The answer looks like a structured product deliverable

More concretely:

- If you ask in Chinese, headings should normally be Chinese-only
- If you ask for PRD review, it should point out gaps instead of rewriting everything
- If you ask for tracking requirements, it should give events, properties, and metric mapping

## Recommended first tests

If you are trying this for the first time, use these prompts in order:

### Test 1: Requirement analysis

```text
Help me break this AI feature idea into requirement analysis
```

Expected result:

- Requirement-analysis structure
- Clear target users, scenarios, pain points, opportunity, risks, and next step

### Test 2: AI vs Agent decision

```text
Is this better as an Agent or a normal AI feature?
```

Expected result:

- Recommendation first
- Reasoning about autonomy, tool use, and workflow complexity

### Test 3: PRD review

```text
Review this AI PRD and focus on missing rules, tracking, fallback, and analytics
```

Expected result:

- Gaps and risks
- Not a full rewrite

### Test 4: Tracking requirements

```text
Write tracking requirements for this feature
```

Expected result:

- Event table
- Properties
- Metric mapping

## Important usage notes

- This Skill is not meant to replace open-ended brainstorming
- It is not the best first step for every vague idea
- It is strongest when the user asks for a standard product deliverable
- If you use it too early, before the problem is framed, it can overlap with process-oriented skills
- If you use it at the right moment, it improves output consistency a lot

## Repository structure explained

If you are new to the repository, this is what each part does.

### `skill/`

This is the real Skill package.
If you want to install or publish the Skill, this is the directory that matters most.

### `skill/SKILL.md`

This is the compact control plane.
It tells the agent:

- when to use the Skill
- what the Skill is for
- how to route between output modes
- what core rules to follow

### `skill/references/`

These files hold the detailed working instructions.

Examples:

- how requirement analysis should be structured
- how Agent design should be handled
- how PRD review should be framed
- how tracking requirements should be output

### `skill/assets/`

These are reusable templates.
They are useful when the output needs a stable shape, such as:

- full PRDs
- functional rule tables
- tracking templates
- admin-side requirement templates

### `skill/scripts/prd_lint.py`

This is a small deterministic checker for PRD-like markdown.
It does not judge whether a product idea is smart.
It only checks whether important sections are present or missing.

### `tests/`

This folder contains fixtures and tests for the lint script.

## How to validate locally

If you want to confirm the lint script works:

```bash
python3 skill/scripts/prd_lint.py tests/fixtures/sample_ai_prd_good.md
python3 skill/scripts/prd_lint.py tests/fixtures/sample_ai_prd_weak.md
python3 -m pytest
```

What this gives you:

- a "good" sample that should pass
- a "weak" sample that should warn or fail
- automated tests to verify the structural rules

## Example prompt list

You can use prompts like these directly:

```text
Help me break this AI idea into requirement analysis
Is this product better as an Agent?
Turn this PRD into functional rules
Write tracking requirements for this feature
Design the admin console requirements
Review this AI PRD and focus on fallback, analytics, and data loops
What data should we recycle after launch?
```

## Common mistakes

Here are the most common mistakes when using this Skill:

### Mistake 1: Starting with "write me a PRD"

If the idea is still vague, the better first step is requirement clarification or requirement analysis.

### Mistake 2: Treating every AI feature like an Agent

Many product problems only need AI assistance, not multi-step autonomous workflows.

### Mistake 3: Forgetting post-launch operations

An AI feature usually needs:

- tracking
- analytics
- fallback
- review logic
- data recycling

### Mistake 4: Treating output as final truth

The Skill helps structure thinking and documentation.
It should not replace product judgment or human review.

## FAQ

### Is this only for PRDs?

No.
PRDs are only one output type.
The Skill also supports requirement analysis, rules, data loops, tracking, analytics, admin requirements, evaluation, and launch readiness.

### Does this force everything into AI?

No.
One of the Skill's explicit rules is to check whether AI is appropriate at all.

### Does it automatically design high-autonomy Agents?

No.
It intentionally leans conservative unless there is strong evidence that real Agent behavior is needed.

### Can I use this even if my starting input is messy?

Yes.
That is one of the main reasons the Skill exists.

### Do I need to understand all the reference files before using it?

No.
If you are just trying the Skill, install `skill/`, restart Codex, and start with a real prompt.
The references are there to support the agent and future maintenance.

## Packaging

If you want to publish or install the Skill elsewhere later, use the contents of `skill/` as the final package.

## Community use

You can use this repository in at least three ways:

1. Install the Skill into Codex and use it directly
2. Reuse the prompt structure in another local agent workflow
3. Fork the repository and adapt the templates for your own team

## Contributing

If you want to improve the Skill, examples, templates, or lint rules, see [CONTRIBUTING.md](./CONTRIBUTING.md).

## License

This project is released under the [MIT License](./LICENSE).

---

## 中文

`AI 产品需求助手` 是一个可以安装到 Codex 里的可复用 Skill。

如果上面这句话还是有点抽象，可以直接理解成：

- 你有一个 AI 产品想法，但现在还比较乱
- 或者你已经写了一些内容，但还不够完整
- 或者你手里有用户反馈、访谈纪要、工单、PRD，但还没法直接拿给团队推进
- 这个 Skill 的作用，就是帮你把这些输入整理成更像“真实产品交付物”的东西

它更像一个 AI 产品需求工作流助手，而不是一个“你说一句话它就自动写完 PRD”的工具。

## 快速概览

| 项目 | 说明 |
|---|---|
| 它是什么 | 一个用于标准化 AI 产品需求输出的 Codex Skill |
| 最适合做什么 | 需求分析、PRD review、规则、埋点、分析、管理端需求 |
| 不最适合做什么 | 开放式 brainstorming、泛化想法发散 |
| 可配合什么用 | Codex 可直接安装，Claude Code 可参考工作流 |
| 核心价值 | 让 AI 产品交付物更稳定、更结构化、更可运营 |

## 快速说明

### 这个 Skill 适合干什么

当你已经明确要某种产品交付物时，用它最合适，比如：

- 需求分析
- AI / Agent 适配性判断
- PRD review
- 功能规则
- 埋点需求
- 数据分析方案
- 管理端需求
- 上线准备清单

### 这个 Skill 不适合先干什么

不要把它当成第一步工具来处理这些问题：

- 开放式 brainstorming
- 泛化想法发散
- “这个项目我们先怎么想”
- 宽泛的流程规划

这些情况更适合先让 `superpowers` 这类过程型 skill 主导。

### 最简单的区分方式

- `superpowers` 管过程
- `ai-product-requirements` 管交付物

如果问题是：

- “这件事该怎么想” -> 过程型 skill
- “请把这个标准化输出出来” -> 这个 skill

### 3 步快速开始

1. 把 `skill/` 复制到：

```text
~/.codex/skills/ai-product-requirements/
```

2. 重启 Codex
3. 试这些提示词：

```text
帮我把这个 AI 想法拆成需求分析
帮我 review 这份 AI PRD
帮我输出这个功能的埋点需求
```

## 常见使用场景

大家通常会在下面几类问题里用到这个 Skill：

### 场景 1：AI 功能想法很模糊

你已经有想法，但还不够清楚，没法直接进入产品或工程讨论。
这时你需要的是结构化需求分析，而不是继续发散。

### 场景 2：已有 AI PRD，但明显不完整

你已经有文档，但还缺：

- 功能规则
- 埋点设计
- 数据分析方案
- 兜底逻辑
- 管理端和运营侧设计

### 场景 3：判断该做 AI 还是 Agent

你不想停留在“听起来像 Agent”这种泛泛判断，而是要一份基于自主性、工具调用、确认点和流程复杂度的结构化结论。

### 场景 4：准备上线

你关心的已经不是功能描述，而是：

- 埋点需求
- 看板设计
- 管理端需求
- 风险与兜底
- 上线准备

## Before / After 示例

### Before

```text
我们想做一个 AI 客服功能，帮我写点东西
```

### After

这个 Skill 目标不是给你一段泛化文案，而是把它推进成下面这些可复用产物：

- 带目标用户、场景、痛点和机会判断的需求分析
- AI / Agent 适配性判断
- 功能规则与验收逻辑
- 埋点和分析需求
- 风险与兜底设计

这也是这个项目真正的意义：把模糊产品语言推成可工作的标准交付物。

## 为什么会有这个项目

很多 AI 产品工作推进不顺，并不是因为没人写文档，而是因为：

- 用户问题本身还没想清楚
- 不适合 AI 的问题也被硬套进 AI
- PRD 只写功能描述，没有规则、数据、指标和兜底
- Agent 方案在核心价值没验证前就被设计得太重

这个项目的目标，就是降低这些常见失误。

它帮助你从：

```text
模糊想法 / 零散反馈 / 不完整 PRD
→ 更清楚的需求分析
→ 更可落地的产品规则
→ 更完整的埋点、分析、管理端和上线准备方案
```

## 这个仓库里有什么

这个仓库包含两层内容：

1. 真正可安装的 Skill 包
2. 用来验证和维护这个 Skill 的辅助文件

其中真正需要安装的是 `skill/` 目录。

仓库里的其他文件主要用于：

- 帮你理解这个 Skill
- 帮你测试它是否正常
- 帮你后续继续维护或迭代

## 适合谁用

这个 Skill 主要适合下面这些角色：

- 做 AI 功能的产品经理
- 在探索 Agent 工作流的团队
- 想把粗糙想法收敛成产品需求的创始人或业务负责人
- 需要一起 review AI PRD 的产品、工程和 AI 团队

如果你经常遇到下面这些问题，这个 Skill 就很适合：

- “这个想法听起来不错，但到底在解决什么问题？”
- “这个问题到底适不适合用 AI？”
- “这到底该做普通 AI 功能，还是该做 Agent？”
- “这份 PRD 缺规则、缺埋点、缺兜底”
- “我们想把 AI 功能上线前的准备做完整一点”

## 它能帮你产出什么

你可以用它产出这些东西：

- 需求分析
- 一页纸摘要
- AI 方案设计
- Agent 设计
- 功能规则
- 数据回收方案
- 埋点需求
- 数据分析方案
- 管理端需求
- 完整 AI PRD
- PRD 评审意见
- 评估与验收标准
- 风险与兜底设计
- 上线准备清单

## 你可以给它什么输入

你不需要一开始就有一份完整的文档。

它可以从这些输入开始工作：

- 一个模糊的功能想法
- 一小段产品描述
- 用户访谈纪要
- 工单和投诉
- 用户反馈
- 竞品拆解笔记
- 业务目标
- 已有 PRD
- 已有 AI 方案草稿
- 已有 Agent 方案草稿

## 它和普通提示词有什么不同

普通提示词很容易直接跳到“帮我写 PRD”。

这个 Skill 更强调过程中的关键判断：

- 先看问题有没有说清楚
- 先看这个问题是否真的适合用 AI
- 区分普通 AI 功能和 Agent
- 强制你把规则、指标、数据闭环、兜底和运营想清楚
- 让最后输出更像团队能直接拿去继续推进的交付物

## 它和 superpowers 的区别
具体来说：

- 当任务还处在开放探索阶段，需要先澄清、先拆解、先判断怎么推进时，更适合 `superpowers`
- 当用户已经明确要某种 AI 产品文档、规则、评审结果、埋点方案、分析方案时，更适合 `ai-product-requirements`

也可以记成一句话：

- 如果问题是“这件事该怎么想”，优先过程型 skill
- 如果问题是“请把这个标准化输出出来”，优先这个 skill

## 为什么很多人会同时保留两个 skill

如果边界清楚，这两个 skill 一起用反而更强：

- `superpowers` 帮你把思考过程理顺
- `ai-product-requirements` 帮你把最终 AI 产品交付物标准化

很多真实工作流里，这两个角色本来就应该分开。

## 它默认怎么工作

默认规则如下：

- 中文提问输出中文
- 英文提问输出英文
- 工程标识保持英文
- 正常中文产品文档默认使用纯中文标题
- 只有在明确需要时才使用双语标题
- 不会默认所有问题都应该做成 AI 功能
- 除非确实需要 Agent 行为，否则默认更保守
- 如果另一个 process skill 已经在主导 brainstorming 阶段，它不应该去抢这个阶段

## 安装前你需要什么

你需要有一个本地 coding agent 环境。

### 方案 A：Codex

如果你想直接用 `~/.codex/skills/` 这套本地 Skill 目录方式，Codex 是最直接的选择。

安装：

```bash
npm install -g @openai/codex
```

更新：

```bash
codex --upgrade
```

官方文档：

- [OpenAI Help: Codex CLI getting started](https://help.openai.com/en/articles/11096431)
- [OpenAI: Get started with Codex](https://openai.com/codex/get-started/)

### 方案 B：Claude Code

如果你团队已经在用 Anthropic 的本地 CLI 工作流，也可以借用这套仓库里的方法和提示结构。

安装：

```bash
npm install -g @anthropic-ai/claude-code
```

更新：

```bash
claude update
```

官方文档：

- [Anthropic Docs: Set up Claude Code](https://docs.anthropic.com/en/docs/claude-code/setup?asuniq=786d6f60)

### 该选哪个

- 如果你想直接使用 `~/.codex/skills/` 这套 Skill 安装方式，优先用 Codex
- 如果你团队已经在用 Anthropic CLI 工作流，也可以用 Claude Code 跑类似流程

## 怎么把这个 Skill 安装到 Codex

如果你使用的是 Codex，按下面这几步来：

### 第一步

把 `skill/` 目录里的内容复制到：

```text
~/.codex/skills/ai-product-requirements/
```

这里有两个关键点：

- 目录名用 `ai-product-requirements`
- `SKILL.md` 要直接出现在这个目录下

安装完成后的目录结构大概应该是：

```text
~/.codex/skills/ai-product-requirements/
├── SKILL.md
├── agents/
├── assets/
├── references/
└── scripts/
```

### 第二步

重启 Codex。

### 第三步

新开一个对话，输入一条真实提示词测试。

比如：

```text
帮我把这个 AI 想法拆成需求分析
这个需求更适合做成 Agent 吗？
帮我 review 这份 AI PRD
帮我输出这个功能的埋点需求
上线后这个功能要回收哪些数据？
```

## 怎么判断安装成功了

安装成功后，测试通常会表现为：

- 这个 Skill 会在相关提示词下自动触发
- 输出语言和你的提问语言一致
- 输出格式明显像产品交付物
- 它会根据问题类型自动选对模式

更具体一点：

- 如果你用中文提问，标题通常应该是纯中文
- 如果你让它 review PRD，它应该指出缺口，而不是整篇重写
- 如果你让它写埋点，它应该给出事件、属性和指标映射

## 建议你第一次怎么测

如果你第一次试这个 Skill，推荐按这个顺序测：

### 测试 1：需求分析

```text
帮我把这个 AI 功能想法拆成需求分析
```

你应该看到：

- 比较完整的需求分析结构
- 明确的目标用户、场景、痛点、机会、风险和下一步

### 测试 2：AI 还是 Agent

```text
这个需求更适合做成 Agent 吗？
```

你应该看到：

- 先给结论
- 再解释自主性、工具调用、流程复杂度这些判断依据

### 测试 3：PRD 评审

```text
帮我 review 这份 AI PRD，重点看规则、埋点、兜底和分析
```

你应该看到：

- 关键缺口和风险
- 而不是整篇重新生成一份文档

### 测试 4：埋点需求

```text
帮我输出这个功能的埋点需求
```

你应该看到：

- 事件表
- 属性
- 指标映射

## 使用注意事项

- 这个 Skill 不是拿来替代开放式 brainstorming 的
- 对特别模糊的问题，它不一定是第一步
- 它最强的地方，是把 AI 产品需求交付物写得更稳定、更标准
- 如果用得太早，容易和过程型 skill 发生重叠
- 如果在正确阶段使用，它能明显提升输出一致性

## 仓库结构说明

如果你第一次看这个仓库，下面这部分最重要。

### `skill/`

这是最核心的目录。
如果你要安装或发布这个 Skill，真正要用的就是它。

### `skill/SKILL.md`

这是 Skill 的精简控制面。
它的作用是告诉 agent：

- 什么情况下该用这个 Skill
- 这个 Skill 是干什么的
- 不同问题应该走哪个输出模式
- 有哪些默认规则必须遵守

### `skill/references/`

这里放的是各类详细说明。

比如：

- 需求分析应该怎么写
- Agent 设计应该怎么判断
- PRD review 应该怎么看
- 埋点需求应该怎么输出

### `skill/assets/`

这里放的是可复用模板。
当输出需要稳定结构时，它们很有用，比如：

- 完整 PRD
- 功能规则表
- 埋点模板
- 管理端需求模板

### `skill/scripts/prd_lint.py`

这是一个小型的结构检查脚本。
它不是拿来判断产品想法好不好，而是用来检查一份 PRD 风格文档的结构是不是缺关键部分。

### `tests/`

这里放的是 `prd_lint.py` 的样例和自动化测试。

## 如何在本地验证

如果你想确认结构检查脚本正常工作，可以运行：

```bash
python3 skill/scripts/prd_lint.py tests/fixtures/sample_ai_prd_good.md
python3 skill/scripts/prd_lint.py tests/fixtures/sample_ai_prd_weak.md
python3 -m pytest
```

运行后你可以得到：

- 一份应该通过的好样例
- 一份应该告警或失败的弱样例
- 自动化测试结果

## 示例提示词

下面这些提示词可以直接拿来试：

```text
帮我把这个 AI 功能想法拆成需求分析
这个产品更适合做成 Agent 吗？
帮我把这份 PRD 拆成功能规则
帮我输出这个功能的埋点需求
帮我设计管理端需求
帮我 review 这份 AI PRD，重点看数据闭环、分析和兜底
上线后这个功能要回收哪些数据？
```

## 常见误区

这里是最常见的几类误区：

### 误区 1：一上来就说“帮我写 PRD”

如果想法本身还很模糊，更好的第一步通常是需求澄清或需求分析。

### 误区 2：把所有 AI 功能都当成 Agent

很多问题其实只需要 AI 辅助，并不需要多步自动化工作流。

### 误区 3：只关心生成，不关心上线后运营

一个真正可上线的 AI 功能，通常还需要：

- 埋点
- 分析
- 兜底
- 审核逻辑
- 数据回收

### 误区 4：把输出当成最终结论

这个 Skill 的作用是帮助你把思路和文档结构化。
它不能替代产品判断，也不能替代人工 review。

## 常见问题

### 它是不是只会写 PRD？

不是。
PRD 只是其中一种输出，它还支持需求分析、规则设计、数据闭环、埋点、分析、管理端、评估和上线准备。

### 它会不会把所有问题都往 AI 上套？

不会。
它的明确规则之一，就是先判断这个问题到底适不适合用 AI。

### 它会不会默认帮我设计高自主 Agent？

不会。
它整体是偏保守的。除非真的存在明确的多步执行、工具调用和跨系统动作，否则它会优先建议普通 AI 功能或低自主方案。

### 如果我的输入很乱，还能用吗？

可以。
这恰好是这个 Skill 最主要的使用场景之一。

### 我需不需要先读完所有 reference 文件？

不需要。
如果你只是第一次试，装好 `skill/`，重启 Codex，然后直接用真实提示词开始就行。
那些 reference 主要是给 agent 和后续维护使用的。

## 后续怎么打包

如果你后面要安装到别处，或者想发布这个 Skill，直接使用 `skill/` 目录内容作为最终包即可。

## 社区使用方式

你可以用下面三种方式使用这个仓库：

1. 直接安装到 Codex 里使用
2. 把这里的提示结构迁移到其他本地 agent 工作流
3. Fork 这个仓库，再按你团队自己的方法论去改模板和规则

## 如何参与改进

如果你想优化这个 Skill、示例、模板或 lint 规则，可以先看 [CONTRIBUTING.md](./CONTRIBUTING.md)。

## 开源协议

本项目使用 [MIT License](./LICENSE)。
