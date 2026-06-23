# Contributing

Thank you for contributing to `ai-product-requirements`.

## Good contribution areas

- Better prompt routing rules
- Better bilingual output structure
- Stronger templates for PRDs, tracking, analytics, and admin requirements
- More realistic examples and anti-examples
- Safer Agent guidance
- More deterministic lint rules and tests

## Keep the project aligned

Please keep changes aligned with the main goal:

- Help teams define AI product requirements more clearly
- Avoid turning the Skill into a generic writing tool
- Keep outputs practical for real product work
- Stay conservative around high-autonomy Agent design

## Repository structure

- `skill/SKILL.md`
  - Keep this compact
- `skill/references/`
  - Put detailed workflow guidance here
- `skill/assets/`
  - Put reusable templates here
- `skill/scripts/`
  - Keep scripts deterministic and dependency-light
- `tests/`
  - Update tests when behavior changes

## Local validation

Run:

```bash
python3 skill/scripts/prd_lint.py tests/fixtures/sample_ai_prd_good.md
python3 skill/scripts/prd_lint.py tests/fixtures/sample_ai_prd_weak.md
python3 -m pytest
```
