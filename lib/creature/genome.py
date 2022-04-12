from lib.creature.neurons.motor_neurons import *
from lib.creature.neurons.sensory_neurons import *
from lib.creature.neurons.internal_neuron import IN
from lib.creature.neural_connection import NeuralConnection
from random import choice, random


class Genome:
    def __init__(self, owner, genes_amount=8):
        self.owner = owner
        self.motor_neurons = [MU(self.owner),
                              MD(self.owner),
                              ML(self.owner),
                              MR(self.owner)]

        self.internal_neurons = [IN(), IN()]

        self.sensory_neurons = [PL(self.owner),
                                PR(self.owner),
                                PU(self.owner),
                                PD(self.owner),
                                # DL(self.owner),
                                # DU(self.owner),
                                RND(self.owner)]

        self.neurons = {
            "motor": self.motor_neurons,
            "internal": self.internal_neurons,
            "sensory": self.sensory_neurons,
        }

        self.connections = []
        for _ in range(genes_amount):
            self.connections.append(self.generate_connection())

        # self.clear_unused_neurons()
        self.sort_connections()

    def generate_connection(self):
        start_type = choice(["sensory", "internal"])
        end_type = choice(["motor", "internal"])
        weight = (random() - 0.5) * 8.0
        start_neuron = choice(self.neurons[start_type])
        end_neuron = choice(self.neurons[end_type])
        return NeuralConnection(start_neuron, end_neuron, weight)

    def clear_unused_neurons(self):
        for neu in self.sensory_neurons:
            if not any([con.parent == neu for con in self.connections]):
                self.sensory_neurons.remove(neu)

        for neu in self.motor_neurons:
            if not any([con.child == neu for con in self.connections]):
                self.motor_neurons.remove(neu)

        for neu in self.internal_neurons:
            if not any([(con.child == neu or con.parent == neu) for con in self.connections]):
                self.internal_neurons.remove(neu)

    def sort_connections(self):
        sorted_connections = []
        for con in self.connections:
            if con.parent.__class__.__base__ == SensoryNeuron and con.child.__class__.__base__ == Neuron:
                sorted_connections.append(con)

        for con in self.connections:
            if con.parent.__class__.__base__ == Neuron and con.child.__class__.__base__ == Neuron:
                sorted_connections.append(con)

        for con in self.connections:
            if con.parent.__class__.__base__ == Neuron and con.child.__class__.__base__ == MotorNeuron:
                sorted_connections.append(con)

        for con in self.connections:
            if con.parent.__class__.__base__ == SensoryNeuron and con.child.__class__.__base__ == MotorNeuron:
                sorted_connections.append(con)

        self.connections = sorted_connections

    def wipe_neurons(self):
        for key in self.neurons:
            for el in self.neurons[key]:
                el.wipe()

    def get_next_turn(self):
        self.wipe_neurons()
        for el in self.sensory_neurons:
            el.excite()

        for con in self.connections:
            con.execute_transaction()

        next_turn = [0, 0]
        for neu in self.motor_neurons:
            if neu.is_activated():
                turn = neu.get_turn()
                next_turn[0] += turn[0]
                next_turn[1] += turn[1]

        return next_turn
