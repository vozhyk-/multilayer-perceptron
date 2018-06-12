import unittest

import parsing.flags
import flag_dataset
import horse_colic_dataset


class RowTestCase(unittest.TestCase):
    def test_flags(self):
        black = parsing.flags.color_to_number("black")
        green = parsing.flags.color_to_number("green")

        row = ["Afghanistan", 5, 1, 648, 16, 10, 2, 0, 3, 5, 1, 1, 0, 1, 1, 1, 0, green, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, black, green]
        ds = flag_dataset.FlagsRow(row)

        self.assertEqual(ds.expected_result(), 2)
        self.assertEqual(ds.input(), [0, 3, 5, 1, 1, 0, 1, 1, 1, 0, green, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, black, green])
        self.assertEqual(ds.num_output_categories(), 8)

    def test_horse_colic(self):
        row = [2, 1, 530334, 38.30, 40, 24, 1, 1, 3, 1, 3, 3, 1, None, None, None, 1, 1, 33.00, 6.70, None, None, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        ds = horse_colic_dataset.HorseColicRow(row)

        self.assertEqual(ds.expected_result(), 0)
        self.assertEqual(ds.input(), [2, 1, 38.30, 40, 24, 1, 1, 3, 1, 3, 3, 1, None, None, None, 1, 1, 33.00, 6.70, None, None])
        self.assertEqual(ds.num_output_categories(), 3)
