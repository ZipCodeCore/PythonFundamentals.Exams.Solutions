import unittest
from exam1 import gregorian_cal_utils


class GregorianCalendarUtilsTest(unittest.TestCase):

    def test_is_leap_year(self):

        test_cases = [
            (1800, False),  # divisible by 4 and 100 but not by 400
            (1818, False),  # not divisible by 4
            (2000, True),   # divisible by 4 and 100 and 400
            (2020, True),   # divisible by 4 but not 100
        ]

        for data_in, data_out in test_cases:
            with self.subTest(f"{data_in} -> {data_out}"):
                self.assertEqual(data_out, gregorian_cal_utils.is_leap_year(data_in))
