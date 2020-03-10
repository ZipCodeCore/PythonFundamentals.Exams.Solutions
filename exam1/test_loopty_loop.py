import unittest
from exam1 import loopty_loop


class LooptyLoopTest(unittest.TestCase):
    def test_generate_list_of_odds(self):
        test_cases = [
            ([1, 2, 3, 4], (1, 5, 1)),
            ([15, 17, 19, 21], (15, 22, 2)),
        ]
        for data_out, data_in  in test_cases:
            with self.subTest(f"{data_in} -> {data_out}"):
                self.assertEqual(data_out, loopty_loop.generate_list(*data_in))
