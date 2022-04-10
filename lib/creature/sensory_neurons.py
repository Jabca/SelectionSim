from lib.creature.basic_neuron import Neuron


class SensoryNeuron(Neuron):
    def __init__(self, owner):
        super(Neuron, self).__init__()
        self.owner = owner

