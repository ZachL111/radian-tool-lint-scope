import csv
import unittest
from pathlib import Path

from src.radian_tool_lint_scope.policy import Signal, classify, score


class PolicyTests(unittest.TestCase):
    def test_fixture_decisions(self) -> None:
        rows = csv.DictReader(Path("fixtures/cases.csv").read_text().splitlines())
        for row in rows:
            signal = Signal(*(int(row[key]) for key in ["demand", "capacity", "latency", "risk", "weight"]))
            self.assertEqual(score(signal), int(row["score"]))
            self.assertEqual(classify(signal), row["decision"])


if __name__ == "__main__":
    unittest.main()
