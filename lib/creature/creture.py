class Creature:
    def __init__(self, genome):
        self.genome = genome
        self.cords = (0, 0)

    def get_cords(self):
        return self.cords

    def set_cords(self, x, y):
        self.cords = (x, y)

    def next_cords(self):
        return self.cords[0] + 1, self.cords[1] + 1

    def get_children(self, number):
        children = []
        for _ in range(number):
            children.append(self.__class__(self.genome))
        return children
