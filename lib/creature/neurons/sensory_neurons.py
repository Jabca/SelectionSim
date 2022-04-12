from lib.creature.neurons.basic_neuron import Neuron
from lib.creature.creture import Creature
from random import random

class SensoryNeuron(Neuron):
    def __init__(self, owner: Creature):
        super(Neuron, self).__init__()
        self.owner = owner


class PL(SensoryNeuron):
    def excite(self):
        x, y = self.owner.get_cords()
        if type(self.owner.field.board[y][x - 1]) is not int:
            self.activation_score = 1.0
        else:
            self.activation_score = 0.0


class PR(SensoryNeuron):
    def excite(self):
        x, y = self.owner.get_cords()
        if type(self.owner.field.board[y][x + 1]) is not int:
            self.activation_score = 1.0
        else:
            self.activation_score = 0.0


class PU(SensoryNeuron):
    def excite(self):
        x, y = self.owner.get_cords()
        if type(self.owner.field.board[y - 1][x]) is not int:
            self.activation_score = 1.0
        else:
            self.activation_score = 0.0


class PD(SensoryNeuron):
    def excite(self):
        x, y = self.owner.get_cords()
        if type(self.owner.field.board[y + 1][x]) is not int:
            self.activation_score = 1.0
        else:
            self.activation_score = 0.0


class DL(SensoryNeuron):
    def excite(self):
        x, y = self.owner.get_cords()
        self.activation_score = x / self.owner.field.size_x


class DU(SensoryNeuron):
    def excite(self):
        x, y = self.owner.get_cords()
        self.activation_score = y / self.owner.field.size_y


class RND(SensoryNeuron):
    def excite(self):
        self.activation_score = random()
