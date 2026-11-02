import unittest
from known_problem import KnownProblem

class TestKnownProblem(unittest.TestCase):
    def test_match_all_keywords(self):
        kp = KnownProblem(
            problem_id="PR-001",
            title="Export Failure",
            keywords=["export", "failed"],
            workaround="Retry with a smaller date range."
        )
        result = kp.matches("Report EXPORT failed.")  # Should match both keywords
        self.assertTrue(result)

    def test_does_not_match_partial_keywords(self):
        kp = KnownProblem(
            problem_id="PR-001",
            title="Export Failure",
            keywords=["export", "failed"],
            workaround="Retry with a smaller date range."
        )
        result = kp.matches("Login failed.")  # Only matches one keyword
        self.assertFalse(result)

    def test_rejects_blank_message(self):
        kp = KnownProblem(
            problem_id="PR-001",
            title="Export Failure",
            keywords=["export", "failed"],
            workaround="Retry with a smaller date range."
        )
        with self.assertRaises(ValueError):
            kp.matches(" ")  # Blank message should raise ValueError