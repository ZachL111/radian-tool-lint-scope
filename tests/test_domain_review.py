import unittest

from src.radian_tool_lint_scope.domain_review import DomainReview, review_lane, review_score


class DomainReviewTests(unittest.TestCase):
    def test_review_lane(self) -> None:
        item = DomainReview(70, 29, 30, 74)
        self.assertEqual(review_score(item), 153)
        self.assertEqual(review_lane(item), "ship")


if __name__ == "__main__":
    unittest.main()
