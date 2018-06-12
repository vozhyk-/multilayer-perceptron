import unittest

import reading


class ReadingTestCase(unittest.TestCase):
    def test_flags(self):
        ds = reading.read_flag_dataset()

        self.assertEqual(ds[0].expected_result(), 2)
        self.assertEqual(ds[193].expected_result(), 5)

    def test_horse_colic_training(self):
        ds = reading.read_horse_colic_training_dataset()

        self.assertEqual(ds[0].expected_result(), 1)
        self.assertEqual(ds[299].expected_result(), 2)

    def test_horse_colic_test(self):
        ds = reading.read_horse_colic_test_dataset()

        self.assertEqual(ds[0].expected_result(), 0)
        self.assertEqual(ds[67].expected_result(), 1)
