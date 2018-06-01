import unittest

import flag_parsing


class ParsingTestCase(unittest.TestCase):
    def test_parse_first_few_flags(self):
        input = """\
Afghanistan,5,1,648,16,10,2,0,3,5,1,1,0,1,1,1,0,green,0,0,0,0,1,0,0,1,0,0,black,green
Albania,3,1,29,3,6,6,0,0,3,1,0,0,1,0,1,0,red,0,0,0,0,1,0,0,0,1,0,red,red
Algeria,4,1,2388,20,8,2,2,0,3,1,1,0,0,1,0,0,green,0,0,0,0,1,1,0,0,0,0,green,white"""

        parsed = flag_parsing.parse(input)

        black = flag_parsing.color_to_number("black")
        green = flag_parsing.color_to_number("green")
        white = flag_parsing.color_to_number("white")
        red = flag_parsing.color_to_number("red")

        self.assertEqual(parsed, [
            ["Afghanistan", 5, 1, 648, 16, 10, 2, 0, 3, 5, 1, 1, 0, 1, 1, 1, 0, green, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, black, green],
            ["Albania", 3, 1, 29, 3, 6, 6, 0, 0, 3, 1, 0, 0, 1, 0, 1, 0, 6, black, 0, 0, 0, 1, 0, 0, 0, 1, 0, red, red],
            ["Algeria", 4, 1, 2388, 20, 8, 2, 2, 0, 3, 1, 1, 0, 0, 1, 0, 0, green, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, green, white],
        ])

    def test_color_to_number(self):
        self.assertEqual(flag_parsing.color_to_number("black"), 0)
        self.assertEqual(flag_parsing.color_to_number("green"), 4)
        self.assertEqual(flag_parsing.color_to_number("red"), 6)
        self.assertEqual(flag_parsing.color_to_number("white"), 7)
