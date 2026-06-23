# Mode Router / 模式路由

## Routing priority

1. Explicit named deliverable wins.
2. Review beats generation for existing artifacts.
3. Full PRD is used only when explicitly requested or clearly supported by context.
4. Agent mode requires real autonomy or tool-execution behavior.
5. Use one primary mode and at most one secondary section.
6. If the conversation is still exploratory, let the active process skill lead.
7. Use clarification mode only for a structured clarification deliverable, not for generic ideation.

## Fast mapping

| Input | Primary mode |
|---|---|
| Rough idea with explicit request for a requirement memo | Requirement clarification |
| Interviews / tickets / feedback | Requirement analysis |
| Leadership summary request | One-pager |
| Prompt / RAG / knowledge / model design | AI solution design |
| Multi-step workflow / automation / tools | Agent design |
| PRD to engineering logic | Functional rules |
| Feedback loop / data reuse | Data recycling |
| Event design | Tracking requirements |
| Dashboard / metrics / diagnosis | Data analysis |
| Ops / moderation / management side | Admin console requirements |
| Complete document request | Full PRD |
| Existing PRD review | PRD review |
| Test / accept / readiness | Evaluation and acceptance |
| Safety / fallback | Risk fallback |
| Beta / GA / rollout | Launch readiness |
| Audience-specific versions | Role-specific outputs |

## Tie-break examples

- Existing PRD + "review this" -> PRD review
- Existing PRD + "turn this into rules" -> Functional rules
- Rough idea + open-ended exploration -> process skill leads, not this skill
- Rough idea + "write a requirement analysis" -> Requirement analysis, with assumptions clearly marked
- Rough idea + "is this an Agent?" -> AI or Agent fit assessment as a structured deliverable only if the user wants a concrete judgment document
- Support tickets + "what should we track?" -> Tracking requirements, plus a short analysis summary if needed
