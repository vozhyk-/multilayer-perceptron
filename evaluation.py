from typing import List

import mlpnolib


def split_dataset(dataset: list, training_set_fraction: float = 0.75) -> (list, list):
    training_set_size = int(training_set_fraction * len(dataset))
    training_set = dataset[:training_set_size]
    test_set = dataset[training_set_size:]
    return (training_set, test_set)

def trained_network(
        dataset,
        inner_layer_sizes: List[int],
        max_error: float = 0.1) -> (mlpnolib.Network, List[float]):
    inputs, expected_outputs = separate_inputs_and_outputs(dataset)

    input_layer_size = len(inputs[0])
    output_layer_size = len(expected_outputs[0])
    layer_sizes = [input_layer_size, *inner_layer_sizes, output_layer_size]
    num_output_categories = dataset[0].num_output_categories()

    network = mlpnolib.Network(layer_sizes, num_output_categories)
    errors = mlpnolib.train(
        network, inputs, expected_outputs, max_error=max_error)
    return (network, errors)

def evaluate_network(network: mlpnolib.Network, dataset) -> float:
    inputs, expected_outputs = separate_inputs_and_outputs(dataset)
    outputs = [mlpnolib.apply(network, input) for input in inputs]
    return mlpnolib.error_on_dataset(outputs, expected_outputs)

def separate_inputs_and_outputs(rows):
    inputs = list(map(lambda row: row.input(), rows))
    expected_outputs = list(map(lambda row: [row.expected_result()], rows))
    return (inputs, expected_outputs)
