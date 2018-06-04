import unittest

import mlpnet

import parsing.flags
import flag_dataset


class MLPNetworkAcceptingDatasetsTestCase(unittest.TestCase):
    def test_flags(self):
        with open("data/flags/flag.data") as file:
            input = file.read()
        parsed = parsing.flags.parse(input)
        rows = map(flag_dataset.FlagRow, parsed)
        inputs = map(lambda row: row.input(), rows)

        input_layer_size = len(inputs)
        output_layer_size = 1
        layer_sizes = [input_layer_size, 64, output_layer_size]

        network = mlpnet.MLPNetwork(layer_sizes)
        outputs = network.predict(inputs)
