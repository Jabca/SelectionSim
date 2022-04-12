from lib.field.field import Field

class Creature:
    def __init__(self, genome, field: Field):
        self.genome = genome
        self.cords = (0, 0)
        self.field = field

    def get_cords(self):
        return self.cords

    def set_cords(self, x, y):
        self.cords = (x, y)

    def next_cords(self):
        move = self.genome.get_next_turn()
        return self.cords[0] + move[0], self.cords[1] + move[1]

    def get_children(self, number):
        children = []
        for _ in range(number):
            children.append(self.__class__(self.genome, self.field))
        return children

    def __hash__(self):
        return self.genome
