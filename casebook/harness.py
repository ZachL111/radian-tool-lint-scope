"""Executable checks for the radian-tool-lint-scope casebook."""

from __future__ import annotations

from collections import Counter

from . import radian_tool_lint_scope_segment_00
from . import radian_tool_lint_scope_segment_01
from . import radian_tool_lint_scope_segment_02
from . import radian_tool_lint_scope_segment_03
from . import radian_tool_lint_scope_segment_04
from . import radian_tool_lint_scope_segment_05
from . import radian_tool_lint_scope_segment_06
from . import radian_tool_lint_scope_segment_07
from . import radian_tool_lint_scope_segment_08
from . import radian_tool_lint_scope_segment_09
from .expected import EXPECTED
from .model import validate_case


def iter_cases():
    yield from radian_tool_lint_scope_segment_00.iter_radian_tool_lint_scope_00()
    yield from radian_tool_lint_scope_segment_01.iter_radian_tool_lint_scope_01()
    yield from radian_tool_lint_scope_segment_02.iter_radian_tool_lint_scope_02()
    yield from radian_tool_lint_scope_segment_03.iter_radian_tool_lint_scope_03()
    yield from radian_tool_lint_scope_segment_04.iter_radian_tool_lint_scope_04()
    yield from radian_tool_lint_scope_segment_05.iter_radian_tool_lint_scope_05()
    yield from radian_tool_lint_scope_segment_06.iter_radian_tool_lint_scope_06()
    yield from radian_tool_lint_scope_segment_07.iter_radian_tool_lint_scope_07()
    yield from radian_tool_lint_scope_segment_08.iter_radian_tool_lint_scope_08()
    yield from radian_tool_lint_scope_segment_09.iter_radian_tool_lint_scope_09()


def summarize_cases() -> dict:
    rows = list(iter_cases())
    for row in rows:
        validate_case(row)
    lanes = Counter(row.expected_lane for row in rows)
    focus = Counter(row.focus for row in rows)
    return {
        "case_count": len(rows),
        "score_min": min(row.expected_score for row in rows),
        "score_max": max(row.expected_score for row in rows),
        "lane_counts": dict(sorted(lanes.items())),
        "focus_counts": dict(sorted(focus.items())),
        "score_checksum": sum((index + 1) * row.expected_score for index, row in enumerate(rows)),
        "pressure_checksum": sum((index % 17 + 1) * row.pressure for index, row in enumerate(rows)),
    }


def assert_expected() -> dict:
    summary = summarize_cases()
    if summary != EXPECTED:
        raise AssertionError(f"casebook summary mismatch: {summary!r} != {EXPECTED!r}")
    return summary


def radian_tool_lint_scope_summary() -> dict:
    return assert_expected()
