import unittest

import mlpnolib

import parsing.flags
import flag_dataset


class MLPNetworkAcceptingDatasetsTestCase(unittest.TestCase):
    def test_flags(self):
        with open("data/flags/flag.data") as file:
            input = file.read()
        parsed = parsing.flags.parse(input)
        rows = map(flag_dataset.FlagsRow, parsed)
        inputs = list(map(lambda row: row.input(), rows))

        input_layer_size = len(inputs)
        output_layer_size = 1
        layer_sizes = [input_layer_size, 64, output_layer_size]
