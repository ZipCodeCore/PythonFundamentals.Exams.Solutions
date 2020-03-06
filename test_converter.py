import unittest
import converter


class ConverterTest(unittest.TestCase):

    def test_meters_to_feet(self):
        test_cases = [
            (1, 3.28),
            (5, 16.40),
            (10, 32.81),
            (100, 328.08),
            (0.91, 2.99),
        ]

        for meter_in, expected in test_cases:
            with self.subTest(f"{meter_in} -> {expected}"):
                self.assertEqual(expected, converter.meters_to_feet(meter_in))

    def test_feet_to_meters(self):
        test_cases = [
            (1, .30),
            (33, 10.06),
            (125, 38.10)
        ]

        for feet_in, expected in test_cases:
            with self.subTest(f"{feet_in} -> {expected}"):
                self.assertEqual(expected, converter.feet_to_meters(feet_in))
