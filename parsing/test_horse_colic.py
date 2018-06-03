import unittest

import parsing.horse_colic


class HorseColicParsingTestCase(unittest.TestCase):
    def test_parse_data_file(self):
        with open("data/horse-colic/horse-colic.data") as file:
            input = file.read()
        parsed = parsing.horse_colic.parse(input)

        self.assertEqual(parsed[0][2], 530101)
        self.assertEqual(parsed[299][2], 534618)

    def test_parse_test_file(self):
        with open("data/horse-colic/horse-colic.test") as file:
            input = file.read()
        parsed = parsing.horse_colic.parse(input)

        self.assertEqual(parsed[0][2], 528626)
        self.assertEqual(parsed[67][2], 530670)

    def test_parse_first_few_rows(self):
        # the first 3 rows from horse-colic.data
        # followed by the first 3 rows from horse-colic.test
        input = """\
2 1 530101 38.50 66 28 3 3 ? 2 5 4 4 ? ? ? 3 5 45.00 8.40 ? ? 2 2 11300 00000 00000 2
1 1 534817 39.2 88 20 ? ? 4 1 3 4 2 ? ? ? 4 2 50 85 2 2 3 2 02208 00000 00000 2 
2 1 530334 38.30 40 24 1 1 3 1 3 3 1 ? ? ? 1 1 33.00 6.70 ? ? 1 2 00000 00000 00000 1 
2 1 528626 38.50 54 20 ? 1 2 2 3 4 1 2 2 5.90 ? 2 42.00 6.30 ? ? 1 2 03111 00000 00000 1
2 1 527950 37.60 48 36 ? ? 1 1 ? 3 ? ? ? ? ? ? 44.00 6.30 1 5.00 1 2 03111 00000 00000 1
1 1 535263 37.7 44 28 ? 4 3 2 5 4 4 1 1 ? 3 5 45 70 3 2 1 1 03205 00000 00000 2"""
        parsed = parsing.horse_colic.parse(input)

        self.maxDiff = None
        self.assertEqual(parsed, [
            [2, 1, 530101, 38.50, 66, 28, 3, 3, None, 2, 5, 4, 4, None, None, None, 3, 5, 45.00, 8.40, None, None, 2, 2, "11300", "00000", "00000", 2],
            [1, 1, 534817, 39.2, 88, 20, None, None, 4, 1, 3, 4, 2, None, None, None, 4, 2, 50, 85, 2, 2, 3, 2, "02208", "00000", "00000", 2],
            [2, 1, 530334, 38.30, 40, 24, 1, 1, 3, 1, 3, 3, 1, None, None, None, 1, 1, 33.00, 6.70, None, None, 1, 2, "00000", "00000", "00000", 1],
            [2, 1, 528626, 38.50, 54, 20, None, 1, 2, 2, 3, 4, 1, 2, 2, 5.90, None, 2, 42.00, 6.30, None, None, 1, 2, "03111", "00000", "00000", 1],
            [2, 1, 527950, 37.60, 48, 36, None, None, 1, 1, None, 3, None, None, None, None, None, None, 44.00, 6.30, 1, 5.00, 1, 2, "03111", "00000", "00000", 1],
            [1, 1, 535263, 37.7, 44, 28, None, 4, 3, 2, 5, 4, 4, 1, 1, None, 3, 5, 45, 70, 3, 2, 1, 1, "03205", "00000", "00000", 2]
        ])
