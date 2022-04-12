from lib.creature.neurons.basic_neuron import Neuron


class NeuralConnection:
    def __init__(self, parent: Neuron, child: Neuron, weight: float):
        self.weight = weight
        self.parent = parent
        self.child = child

    def execute_transaction(self):
        self.child.activation_score += self.parent.activation_score * self.weight
