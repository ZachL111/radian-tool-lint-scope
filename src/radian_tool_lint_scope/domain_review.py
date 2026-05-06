from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DomainReview:
    signal: int
    slack: int
    drag: int
    confidence: int


def review_score(item: DomainReview) -> int:
    return item.signal * 2 + item.slack + item.confidence - item.drag * 3


def review_lane(item: DomainReview) -> str:
    score = review_score(item)
    if score >= 140:
        return "ship"
    if score >= 105:
        return "watch"
    return "hold"
