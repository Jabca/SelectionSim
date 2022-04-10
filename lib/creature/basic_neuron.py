class Neuron:
    def __init__(self):
        self.activation_score: float = 0.0

    def add_score(self, weight: float) -> None:
        self.activation_score += weight

    def clear(self):
        self.activation_score = 0.0
