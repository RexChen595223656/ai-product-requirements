#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path


SECTION_ALIASES = {
    "one_page_summary": ["one-page summary", "one page summary", "一页纸摘要"],
    "background_and_version_goal": ["background and version goal", "background", "背景与版本目标", "项目背景", "版本目标"],
    "user_role_and_scenario": ["user roles and typical scenarios", "user role and scenario", "用户角色与典型场景", "用户角色与场景"],
    "current_state_pain_consequence": ["current state, pain points, and consequences", "current state", "现状、痛点与后果", "痛点与后果"],
    "positioning_and_value": ["product positioning and value proposition", "positioning and value", "产品定位与价值主张", "定位与价值"],
    "ai_capability_definition": ["ai capability definition", "ai capability", "ai能力定义", "ai能力设计"],
    "agent_design": ["agent design", "agent design if applicable", "agent 设计", "agent设计"],
    "functional_rules": ["functional rules and state logic", "functional rules", "功能规则", "功能规则与状态逻辑"],
    "data_knowledge_prompt_strategy": ["data / knowledge base / prompt strategy", "knowledge base / prompt strategy", "数据 / 知识库 / prompt 策略", "数据与prompt策略"],
    "data_recycling": ["data recycling and optimization loop", "data recycling", "数据回收与优化闭环", "数据回收"],
    "tracking_requirements": ["tracking requirements", "instrumentation", "埋点需求", "追踪需求"],
    "data_analysis_dashboard": ["data analysis and dashboard", "data analysis", "数据分析与看板", "数据分析"],
    "admin_console": ["admin console requirements", "admin console", "管理端需求", "管理后台需求"],
    "evaluation_and_acceptance": ["evaluation and acceptance criteria", "evaluation and acceptance", "评估与验收标准", "验收标准"],
    "risk_and_fallback": ["risk and fallback", "risk and fallback design", "风险与兜底", "风险与回退"],
    "version_scope_and_roadmap": ["version scope and roadmap", "roadmap", "版本范围与路线图", "路线图"],
    "assumptions_open_questions": ["assumptions", "open questions", "assumptions and open questions", "假设", "开放问题", "假设与开放问题"],
}

RISKY_PATTERNS = [
    "call the llm",
    "use ai to generate",
    "fully automated",
    "no human review",
    "final decision",
    "always correct",
    "no need for fallback",
]

AGENT_HINTS = ["agent workflow", "multi-step", "tool call", "tool use", "autonomous", "autonomy level", "agent_task", "agent "]
ADMIN_HINTS = ["admin", "ops", "review", "config", "audit", "moderation", "intervention", "管理端", "管理后台", "运营", "审核", "审计"]
LIST_EXPECTED = {"assumptions_open_questions"}
TABLE_EXPECTED = {"functional_rules", "tracking_requirements", "data_analysis_dashboard", "admin_console"}


def normalize(text: str) -> str:
    return re.sub(r"\s+", "", text.strip().lower())


def extract_sections(text: str):
    sections = []
    current = None
    for line in text.splitlines():
        if re.match(r"^\s{0,3}#{1,6}\s+", line):
            if current:
                sections.append(current)
            current = {"heading": line.strip().lstrip("#").strip(), "body": []}
        elif current:
            current["body"].append(line)
    if current:
        sections.append(current)
    return sections


def find_section(sections, aliases):
    normalized_aliases = {normalize(alias) for alias in aliases}
    for section in sections:
        heading = normalize(section["heading"])
        if heading in normalized_aliases:
            return section
    return None


def body_text(section):
    return "\n".join(section["body"]).strip()


def is_weak(key, section):
    body = body_text(section)
    if len(re.sub(r"\s+", "", body)) < 40:
        return True
    if key in TABLE_EXPECTED:
        lines = [line for line in section["body"] if line.strip()]
        table_rows = [line for line in lines if "|" in line]
        if len(table_rows) < 3:
            return True
    if key in LIST_EXPECTED:
        bullets = [line for line in section["body"] if re.match(r"^\s*[-*]\s+", line)]
        if len(bullets) < 2:
            return True
    return False


def should_require_agent(text):
    lowered = text.lower()
    return any(hint in lowered for hint in AGENT_HINTS)


def should_require_admin(text):
    lowered = text.lower()
    return any(hint in lowered for hint in ADMIN_HINTS)


def lint_prd(text: str):
    sections = extract_sections(text)
    missing = []
    weak = []
    for key, aliases in SECTION_ALIASES.items():
        if key == "agent_design" and not should_require_agent(text):
            continue
        if key == "admin_console" and not should_require_admin(text):
            continue
        section = find_section(sections, aliases)
        if not section:
            missing.append(key)
            continue
        if is_weak(key, section):
            weak.append(key)

    lowered = text.lower()
    risky = [pattern for pattern in RISKY_PATTERNS if pattern in lowered]

    if missing:
        status = "fail"
    elif weak or risky:
        status = "warn"
    else:
        status = "pass"

    suggested_fixes = []
    for key in missing:
        suggested_fixes.append(f"Add section: {key}")
    for key in weak:
        suggested_fixes.append(f"Strengthen section: {key}")
    for pattern in risky:
        suggested_fixes.append(f"Replace risky phrase: {pattern}")

    return {
        "status": status,
        "missing_sections": missing,
        "weak_sections": weak,
        "risky_patterns": risky,
        "suggested_fixes": suggested_fixes,
    }


def main():
    if len(sys.argv) != 2:
        print("Usage: python skill/scripts/prd_lint.py path/to/prd.md", file=sys.stderr)
        return 1
    path = Path(sys.argv[1])
    text = path.read_text(encoding="utf-8")
    print(json.dumps(lint_prd(text), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
