from __future__ import annotations

from dataclasses import dataclass

THRESHOLD = 173
RISK_PENALTY = 5
LATENCY_PENALTY = 2
WEIGHT_BONUS = 4


@dataclass(frozen=True)
class Signal:
    demand: int
    capacity: int
    latency: int
    risk: int
    weight: int


def score(signal: Signal) -> int:
    return (
        signal.demand * 2
        + signal.capacity
        + signal.weight * WEIGHT_BONUS
        - signal.latency * LATENCY_PENALTY
        - signal.risk * RISK_PENALTY
    )


def classify(signal: Signal) -> str:
    return "accept" if score(signal) >= THRESHOLD else "review"
