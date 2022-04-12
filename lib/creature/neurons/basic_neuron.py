from math import tanh


class Neuron:
    def __init__(self):
        self.activation_score: float = 0.0

    def add_score(self, weight: float) -> None:
        self.activation_score += weight

    def clear(self):
        self.activation_score = 0.0

    def is_activated(self):
        if tanh(self.activation_score) >= 0.9:
            return True
        else:
            return False

    def wipe(self):
        self.activation_score = 0