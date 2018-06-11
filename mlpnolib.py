#MLP without libraries
from typing import List
import math
import numpy as np

class Connection:
    def __init__(self, connectedNeuron):
        self.connectedNeuron = connectedNeuron
        self.weight = np.random.normal()
        self.dWeight = 0.0

class Neuron:
    eta = 0.09
    alpha = 0.015

    def __init__(self, layer):
        self.dendrons = []
        self.error = 0.0
        self.gradient = 0.0
        self.output = 0.0
        if layer is None:
            pass
        else:
            for neuron in layer:
                con = Connection(neuron)
                self.dendrons.append(con)

    def addError(self, err):
        self.error = self.error + err

    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x * 1.0))

    def dSigmoid(self, x):
        return x * (1.0 - x)

    def setError(self, err):
        self.error = err

    def setOutput(self, output):
        self.output = output

    def getOutput(self):
        return self.output

    def feedForword(self):
        sumOutput = 0
        if len(self.dendrons) == 0:
            return
        for dendron in self.dendrons:
            sumOutput = sumOutput + dendron.connectedNeuron.getOutput() * dendron.weight
        self.output = self.sigmoid(sumOutput)

    def backPropagate(self):
        self.gradient = self.error * self.dSigmoid(self.output);
        for dendron in self.dendrons:
            dendron.dWeight = Neuron.eta * (
            dendron.connectedNeuron.output * self.gradient) + self.alpha * dendron.dWeight;
            dendron.weight = dendron.weight + dendron.dWeight;
            dendron.connectedNeuron.addError(dendron.weight * self.gradient);
            self.error = 0;

class Network:
    def __init__(self, topology, num_output_categories):
        self.layers = []
        self.num_categories = num_output_categories
        for numNeuron in topology:
            layer = []
            for i in range(numNeuron):
                if (len(self.layers) == 0):
                    layer.append(Neuron(None))
                else:
                    layer.append(Neuron(self.layers[-1]))
            layer.append(Neuron(None)) # bias neuron
            layer[-1].setOutput(1) # setting output of bias neuron as 1
            self.layers.append(layer)
    def setInput(self, inputs):
        for i in range(len(inputs)):
            self.layers[0][i].setOutput(inputs[i])

    def feedForword(self):
        for layer in self.layers[1:]:
            for neuron in layer:
                neuron.feedForword();
    def backPropagate(self, target):
        target = self.unthreshold(target)
        for i in range(len(target)):
            self.layers[-1][i].setError(target[i] - self.layers[-1][i].getOutput())
        for layer in self.layers[::-1]: #reverse the order
            for neuron in layer:
                neuron.backPropagate()

    def getThResults(self):
        output = []
        for neuron in self.layers[-1]:
            o = self.threshold(neuron.getOutput())
            output.append(o)
        output.pop()# removing the bias neuron
        return output

    def threshold(self, output: float) -> int:
        max_output = 1.0
        step = max_output / self.num_categories
        steps = math.ceil(output / step)
        return steps - 1 # start from 0

    def unthreshold(self, categorical_output: List[int]) -> float:
        max_output = 1.0
        step = max_output / self.num_categories
        return [step * o + step / 2 for o in categorical_output]


def train(net: Network,
          inputs: List[list], expected_outputs: List[list],
          max_error : float = 0.01):
    assert len(inputs) == len(expected_outputs)

    generation = 1
    while True:
        outputs = []
        for i in range(len(inputs)):
            outputs.append(apply(net, inputs[i]))
            net.backPropagate(expected_outputs[i])

        err = error_on_dataset(outputs, expected_outputs)
        print ("generation:", generation, "error: ", err)
        if (err < max_error):
            break
        generation += 1

def apply(net: Network, input: list) -> List[int]:
    net.setInput(input)
    net.feedForword()
    return net.getThResults()

def error(actual: List[int], expected: List[int]):
    assert len(actual) == len(expected)

    return int(actual != expected)

def error_on_dataset(actual: List[List[int]], expected: List[List[int]]):
    assert len(actual) == len(expected)

    err_sum = sum(map(lambda t: error(t[0], t[1]), zip(actual, expected)))
    return err_sum / len(actual)
