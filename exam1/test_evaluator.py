import unittest
from exam1 import evaluator


class EvaluatorTest(unittest.TestCase):

    def test_find_lowest_value(self):
        test_cases = [
            ([512, -256, -128, 0, 128], -256),
            ([8.2, -9.9, 7.66, 1.3, 12.5, -5], -9.9),
            ([-1000, -500, 0, 500, 1000], -1000),
            ([0, 0, 0], 0)
        ]

        for case, expected in test_cases:
            with self.subTest(f"{case} -> {expected}"):
                self.assertEqual(expected, evaluator.find_lowest_value(case))

    def test_find_highest_value(self):
        test_cases = [
            ([512, -256, -128, 0, 128], 512),
            ([8.2, -9.9, 7.66, 1.3, 12.5, -5], 12.5),
            ([-1000, -500, 0, 500, 1000], 1000),
            ([0, 0, 0], 0)
        ]

        for case, expected in test_cases:
            with self.subTest(f"{case} -> {expected}"):
                self.assertEqual(expected, evaluator.find_highest_value(case))

    def test_find_value(self):
        test_cases =[
            (3, [1, 2, 3, 4, 5], 2),
            ('a', ['a', 'e', 'i', 'o', 'u'], 0),
            (False, (True, True, True), -1),
        ]

        for case in test_cases:
            with self.subTest(f"{case}"):
                expected = case[2]
                actual = evaluator.find_value(case[0], case[1])
                self.assertEqual(expected, actual)

    def test_compare_two_numbers(self):
        test_cases = [
            ([2, 2], 0),
            ([2, 9], -1),
            ([9, 2], 1),
        ]

        for case, expected in test_cases:
            with self.subTest(f"{case} -> {expected}"):
                self.assertEqual(expected, evaluator.compare_two_numbers(*case))

    def test_compare_two_strings(self):
        test_cases = [
            (["abc", "abc"], 0),
            (["python", "java"], 1),
            (["go", "java"], -1)
        ]

        for case, expected in test_cases:
            with self.subTest(f"{case} -> {expected}"):
                self.assertEqual(expected, evaluator.compare_two_numbers(*case))
