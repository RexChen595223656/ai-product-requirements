---
name: ai-product-requirements
description: use this skill when the user explicitly wants a structured ai product deliverable such as requirement analysis, ai or agent fit assessment, ai / agent prd, prd review, functional rules, data recycling plan, tracking requirements, data analysis plan, admin console requirements, evaluation criteria, risk fallback plan, or launch readiness plan. use it after the task has already been framed clearly enough for document output. do not use this skill for open-ended brainstorming, general ideation, or generic workflow planning when another process skill is handling clarification. for agent products, explicitly define autonomy level, tool permissions, human approval points, execution states, failure recovery, auditability, instrumentation, and management-side operations.
---

# AI Product Requirements

Use this skill for AI product deliverables and review work. Treat it as a structured output skill, not a general ideation workflow.

## What it does

- Produces structured AI product documents once the problem is clear enough
- Analyzes evidence such as interviews, tickets, feedback, or competitor notes
- Designs AI features and Agent workflows
- Converts requirements into functional rules, tracking, analytics, admin requirements, and launch plans
- Reviews existing PRDs and highlights gaps, risks, and anti-patterns

## Boundary with process skills

- Let process skills handle open-ended brainstorming, clarifying broad goals, and deciding how to approach the work.
- Use this skill when the user clearly wants a product requirement artifact or a standard review output.
- If the conversation is still mainly about "what should we do" or "how should we think about this", another process skill should lead first.
- If the conversation is about "please output the requirement analysis / prd review / tracking spec / admin requirements", this skill should lead.

## Core method chain

Always preserve this chain when relevant:

```text
User role × Typical scenario × Current state
→ Pain point and consequence
→ AI / Agent positioning
→ Value proposition
→ Function / data / model / tool support
→ Functional rules
→ Data recycling and instrumentation
→ Data analysis and admin operations
→ Evaluation and fallback
→ Launch and optimization loop
```

## Language routing / 语言路由

- 中文提问默认输出中文。
- English prompts default to English output.
- Explicit user instruction about output language overrides everything else.
- If the prompt mixes languages, follow the instruction language first, then target audience language.
- Keep engineering identifiers, event names, JSON keys, and script names in English.
- Do not mix Chinese and English randomly in one paragraph.
- For Chinese output, use Chinese-only section headings by default.
- For English output, use English-only section headings by default.
- Use bilingual headings only when the user explicitly asks for bilingual output, or when the deliverable is clearly for mixed product and engineering collaboration.

## Mode routing

- Explicit named deliverable beats inference.
- Review beats generation when the user gives an existing artifact and asks for assessment or improvement.
- Full PRD is used only when explicitly requested or when the context is already complete enough.
- Agent design requires real autonomy, tool use, multi-step execution, cross-system action, or persistent execution state.
- Choose one primary mode and at most one secondary section.
- If the task is still open-ended and exploratory, defer to the active process skill instead of taking over.
- Use clarification mode only when the user explicitly wants a structured clarification memo or when a deliverable is requested but one narrow gap still blocks output.

## Core rules

- Do not assume every problem should be solved with AI.
- Start from user task and business value, not from model capability.
- Mark uncertain points as assumptions.
- Keep facts, assumptions, open questions, and next actions separated.
- Match output format to the real deliverable. Normal analysis documents should read like clean product documents, not teaching demos.
- Do not take over generic brainstorming or generic project planning when another process skill is already guiding that phase.
- For AI features, define input, processing, output, limits, responsibility level, and failure strategy.
- For Agents, define autonomy, permissions, approval points, state machine, recovery, and auditability.
- Every data item needs a purpose, sensitivity label, and handling rule.
- Tracking requirements must map events to metrics and acceptance checks.
- High-risk actions require fallback and confirmation rules.
- End outputs with the next smallest action.

## When to open references

- `references/mode-router.md`: choose the primary mode
- `references/core-principles.md`: apply the default product method
- `references/discovery-playbook.md`: clarify missing information
- `references/*-mode.md`: produce mode-specific outputs
- `references/phrases-and-table-templates.md`: reuse bilingual headings and table patterns
- `references/examples.md`: inspect compact examples and anti-examples

## When to open assets

- `assets/ai-agent-prd-template.md`: full PRD mode
- `assets/functional-rules-template.md`: engineering and QA rules
- `assets/tracking-requirements-template.md`: tracking spec
- `assets/admin-console-template.md`: management-side requirements
- `assets/data-analysis-dashboard-template.md`: metrics and dashboard plan
- `assets/prd-review-checklist.md`: review structure
- `assets/launch-readiness-checklist.md`: rollout and launch checks
