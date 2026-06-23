# Repository Instructions

This repository contains a ChatGPT Skill package for AI product and Agent requirement analysis.

## Principles

- Keep `skill/SKILL.md` concise. It is the control plane.
- Put detailed workflow instructions in `skill/references/`.
- Put reusable templates in `skill/assets/`.
- Put deterministic checks in `skill/scripts/`.
- Do not add unnecessary dependencies.
- Prefer markdown tables and concise templates.
- Keep all skill frontmatter lowercase where required.
- Do not rename the skill unless explicitly requested.

## Validation

Run:

```bash
python skill/scripts/prd_lint.py tests/fixtures/sample_ai_prd_good.md
python skill/scripts/prd_lint.py tests/fixtures/sample_ai_prd_weak.md
pytest
```

## Expected implementation

Build a complete, readable Skill package, not only documentation.
