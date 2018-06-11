import unittest
import random

import reading
import evaluation


class MLPNetworkAcceptingDatasetsTestCase(unittest.TestCase):
    def test_flags(self):
        rows = reading.read_flag_dataset()

        random.shuffle(rows)
        training_set, test_set = evaluation.split_dataset(rows)

        max_error = 0.76
        network, training_errors = evaluation.trained_network(
            training_set, [16, 16], max_error=max_error)
        error = evaluation.evaluate_network(network, test_set)
        self.assertLess(error, max_error)
