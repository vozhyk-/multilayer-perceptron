import unittest
import random

import reading
import evaluation


class MLPNetworkAcceptingDatasetsTestCase(unittest.TestCase):
    def test_flags(self):
        rows = reading.read_flag_dataset()
        random.shuffle(rows)

        training_set_size = int(0.75 * len(rows))
        training_set = rows[:training_set_size]
        test_set = rows[training_set_size:]

        network = evaluation.trained_network(training_set, [16, 16], max_error=0.1)
        error = evaluation.evaluate_network(network, test_set)
        self.assertLess(error, 0.1)
