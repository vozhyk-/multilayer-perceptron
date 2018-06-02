import unittest

import flag_parsing
import flag_dataset


class RowTestCase(unittest.TestCase):
    def test_flags(self):
        black = flag_parsing.color_to_number("black")
        green = flag_parsing.color_to_number("green")

        row = ["Afghanistan", 5, 1, 648, 16, 10, 2, 0, 3, 5, 1, 1, 0, 1, 1, 1, 0, green, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, black, green]
        ds = flag_dataset.FlagsRow(row)

        self.assertEqual(ds.expected_result(), row[7])
        self.assertEqual(ds.input(), [0, 3, 5, 1, 1, 0, 1, 1, 1, 0, green, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, black, green])