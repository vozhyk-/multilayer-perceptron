import unittest

import mlpnolib


class MLPNetworkThresholdTestCase(unittest.TestCase):
    def test_2_categories(self):
        network = make_network(2)

        self.assertEqual(network.threshold(0.4), 0)
        self.assertEqual(network.threshold(0.5), 0)
        self.assertEqual(network.threshold(0.6), 1)
        self.assertEqual(network.threshold(1.0), 1)

    def test_3_categories(self):
        network = make_network(3)

        self.assertEqual(network.threshold(0.32), 0)
        self.assertEqual(network.threshold(0.33), 0)
        self.assertEqual(network.threshold(0.34), 1)
        self.assertEqual(network.threshold(0.66), 1)
        self.assertEqual(network.threshold(0.67), 2)
        self.assertEqual(network.threshold(1.0), 2)

    def test_7_categories(self):
        network = make_network(7)

        self.assertEqual(network.threshold(0.1), 0)
        self.assertEqual(network.threshold(0.5), 3)
        self.assertEqual(network.threshold(0.9), 6)
        self.assertEqual(network.threshold(1.0), 6)

class MLPNetworkUnthresholdTestCase(unittest.TestCase):
    def test_2_categories(self):
        self.network = make_network(2)

        self.check(0, 0.25)
        self.check(1, 0.75)

    def test_3_categories(self):
        self.network = make_network(3)

        self.check(0, 1.0 / 3 / 2)
        self.check(1, 0.5)
        self.check(2, 1.0 / 3 * 2 + 1.0 / 6)

    def test_7_categories(self):
        self.network = make_network(7)

        self.check(3, 0.5)

    def check(self, input, expected_result):
        self.assertEqual(self.network.unthreshold([input]), [expected_result])

def make_network(num_output_categories: int) -> mlpnolib.Network:
    layer_sizes = [7, 4, 1]
    return mlpnolib.Network(layer_sizes, num_output_categories)
