import unittest

import flag_parsing


class ParsingTestCase(unittest.TestCase):
    def test_parse_first_few_flags(self):
        input = """\
Afghanistan,5,1,648,16,10,2,0,3,5,1,1,0,1,1,1,0,green,0,0,0,0,1,0,0,1,0,0,black,green
Albania,3,1,29,3,6,6,0,0,3,1,0,0,1,0,1,0,red,0,0,0,0,1,0,0,0,1,0,red,red
Algeria,4,1,2388,20,8,2,2,0,3,1,1,0,0,1,0,0,green,0,0,0,0,1,1,0,0,0,0,green,white"""

        parsed = flag_parsing.parse(input)

        self.assertEqual(parsed[0], ["Afghanistan", 5, 1, 648, 16, 10, 2, 0, 3, 5, 1, 1, 0, 1, 1, 1, 0, "green", 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, "black", "green"])
