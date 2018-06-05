import unittest

import mlpnolib

import parsing.flags
import flag_dataset


class MLPNetworkAcceptingDatasetsTestCase(unittest.TestCase):
    def test_flags(self):
        training_set_size = 64

        with open("data/flags/flag.data") as file:
            input = file.read()
        parsed = parsing.flags.parse(input)[:training_set_size]
        rows = list(map(flag_dataset.FlagsRow, parsed))

        inputs = list(map(lambda row: row.input(), rows))
        outputs = list(map(lambda row: [row.expected_result()], rows))

        input_layer_size = len(inputs)
        output_layer_size = 1
        layer_sizes = [input_layer_size, 16, 16, output_layer_size]

        network = mlpnolib.Network(layer_sizes)
        mlpnolib.train(network, inputs, outputs, max_error=0.1)
        output = mlpnolib.apply(network, inputs[training_set_size])
