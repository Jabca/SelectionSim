from lib.creature.neurons.basic_neuron import Neuron
from lib.creature.creture import Creature


class MotorNeuron(Neuron):
    def __init__(self, owner: Creature):
        super(Neuron, self).__init__()
        self.owner = owner


class ML(MotorNeuron):
    def get_turn(self):
        return 1, 0


class MR(MotorNeuron):
    def get_turn(self):
        return -1, 0


class MU(MotorNeuron):
    def get_turn(self):
        return 0, -1


class MD(MotorNeuron):
    def get_turn(self):
        return 0, 1
