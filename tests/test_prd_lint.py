from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "skill" / "scripts"))

from prd_lint import lint_prd  # noqa: E402


def read_fixture(name: str) -> str:
    return (ROOT / "tests" / "fixtures" / name).read_text(encoding="utf-8")


def test_good_fixture_passes_or_warns_minimally():
    result = lint_prd(read_fixture("sample_ai_prd_good.md"))
    assert result["status"] in {"pass", "warn"}
    assert not result["missing_sections"]
    assert "fully automated" not in result["risky_patterns"]


def test_weak_fixture_warns_or_fails():
    result = lint_prd(read_fixture("sample_ai_prd_weak.md"))
    assert result["status"] in {"warn", "fail"}
    assert result["missing_sections"]
    assert "use ai to generate" in result["risky_patterns"]
    assert "fully automated" in result["risky_patterns"]


def test_heading_alias_detection():
    result = lint_prd(
        "# One Page Summary\n\nEnough text for summary body.\n\n"
        "# Background\n\nEnough text for background body.\n\n"
        "# User role and scenario\n\nEnough text for roles and scenarios body.\n\n"
        "# Current state\n\nEnough text for current state and pain body.\n\n"
        "# Positioning and value\n\nEnough text for position and value body.\n\n"
        "# AI capability\n\nEnough text for ai capability body.\n\n"
        "# Functional rules\n\n|a|b|c|\n|---|---|---|\n|1|2|3|\n\n"
        "# Knowledge base / prompt strategy\n\nEnough text for strategy body.\n\n"
        "# Data recycling\n\nEnough text for data recycle body.\n\n"
        "# Instrumentation\n\n|a|b|c|\n|---|---|---|\n|1|2|3|\n\n"
        "# Data analysis\n\n|a|b|c|\n|---|---|---|\n|1|2|3|\n\n"
        "# Evaluation and acceptance\n\nEnough text for evaluation body.\n\n"
        "# Risk and fallback\n\nEnough text for risk body.\n\n"
        "# Roadmap\n\nEnough text for roadmap body.\n\n"
        "# Assumptions and open questions\n\n- one\n- two\n"
    )
    assert "one_page_summary" not in result["missing_sections"]
    assert "version_scope_and_roadmap" not in result["missing_sections"]


def test_agent_trigger_requires_agent_section():
    text = read_fixture("sample_ai_prd_good.md") + "\n\nThis workflow uses Agent workflow and tool call orchestration."
    result = lint_prd(text)
    assert "agent_design" in result["missing_sections"]


def test_admin_trigger_requires_admin_section():
    text = "# One-page summary\n\nEnough text for summary body.\n\n# Background\n\nEnough text for background body.\n\n# User role and scenario\n\nEnough text for roles body.\n\n# Current state\n\nEnough text for current state body.\n\n# Positioning and value\n\nEnough text for value body.\n\n# AI capability definition\n\nEnough text for ai body.\n\n# Functional rules\n\n|a|b|c|\n|---|---|---|\n|1|2|3|\n\n# Data / knowledge base / prompt strategy\n\nEnough strategy body text.\n\n# Data recycling\n\nEnough recycle body text.\n\n# Tracking requirements\n\n|a|b|c|\n|---|---|---|\n|1|2|3|\n\n# Data analysis and dashboard\n\n|a|b|c|\n|---|---|---|\n|1|2|3|\n\n# Evaluation and acceptance criteria\n\nEnough evaluation body text.\n\n# Risk and fallback\n\nEnough risk body text.\n\n# Version scope and roadmap\n\nEnough roadmap body text.\n\n# Assumptions and open questions\n\n- one\n- two\n\nThis product needs ops review and audit workflows."
    result = lint_prd(text)
    assert "admin_console" in result["missing_sections"]
