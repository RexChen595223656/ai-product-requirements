# 一页纸摘要

这个版本面向跨境客服团队，目标是在多渠道消息处理场景中，用 AI 草拟回复并保留人工确认，以减少平均处理时长并提升回复一致性。

# 背景与版本目标

当前客服需要在多个后台手工检索知识、复制话术并改写，响应慢且质量不稳定。这个版本目标是先做草稿生成和知识引用，不做自动发送。

# 用户角色与典型场景

主要用户是客服专员和客服主管。典型场景包括售前咨询、物流异常回复和退款解释。主管还需要抽查高风险回复并追踪知识缺口。

# 现状、痛点与后果

现状是人工检索和人工改写占用大量时间。痛点是效率低、知识使用不一致、培训成本高。后果是响应延迟、满意度下降、主管复核成本上升。

# 产品定位与价值主张

这是一个低自主 AI 助手，不替代客服决策，只负责生成可编辑草稿并提供知识引用。价值是缩短处理时长、提升一致性、降低培训门槛。

# AI 能力定义

AI 输入包括用户问题、订单上下文、知识库内容和历史处理策略。AI 输出是带引用的回复草稿、风险提示和缺失信息提示。失败时返回需要人工处理的原因。

# 功能规则与状态逻辑

| Rule ID | Rule Name | Trigger | Condition | System Behavior | User Feedback |
|---|---|---|---|---|---|
| FR-1 | Draft Reply | Submit question | Knowledge available | Generate draft with citations | Show editable draft |

# 数据 / 知识库 / Prompt 策略

知识库按物流、退款、售前 FAQ 分类维护，Prompt 按场景版本化管理。输出必须引用命中的知识片段并标记低置信度情形。

# 数据回收与优化闭环

回收用户输入、AI 输出、用户编辑、采纳结果、低置信度样本和知识缺口。数据用于知识库修复、Prompt 优化和评估集更新。

# 埋点需求

| Event Name | 中文名称 | Trigger Timing | Properties | Purpose | Downstream Metric | Priority |
|---|---|---|---|---|---|---|
| ai_generate_success | 生成成功 | Draft generated | task_id, scenario | Measure generation success | success_rate | P0 |

# 数据分析与看板

| Layer | Metrics | Purpose |
|---|---|---|
| User value | adoption_rate, time_saved | Evaluate usefulness |

# 管理端需求

| Module | Goal | Core Capabilities |
|---|---|---|
| Review Center | Review risky drafts | Filter, inspect, comment |

# 评估与验收标准

验收包括草稿可用率、人工采纳率、平均处理时长下降幅度和高风险场景拦截准确率。每周复测一次样本集。

# 风险与兜底

低置信度、知识缺失和敏感问题一律提示人工处理，不允许自动发送。出现引用缺失时直接阻断生成结果落地。

# 版本范围与路线图

MVP 只覆盖中文客服草稿生成和知识引用。后续再扩展英文场景、总结能力和主管批量审阅能力。

# 假设与开放问题

- 假设现有知识库质量足够支持前两个客服场景。
- 开放问题是订单上下文字段是否能稳定接入，以及主管审批是否需要强制化。
