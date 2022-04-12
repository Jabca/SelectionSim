from math import floor
from random import randint


class Field:
    def __init__(self, filter_function, size_x=128, size_y=128, creatures_number=1000):
        self.board = [[0 for _ in range(size_x)] for __ in range(size_y)]
        self.size_x = size_x
        self.size_y = size_y
        self.creatures = []
        self.creature_number = creatures_number
        self.filter_function = filter_function
        self.clear_board()

        for x in range(self.size_x):
            self.board[0][x] = -1
            self.board[-1][x] = -1

        for y in range(self.size_y):
            self.board[y][0] = -1
            self.board[y][-1] = -1

    def clear_board(self):
        self.creatures.clear()
        for y in range(1, self.size_y - 1):
            for x in range(1, self.size_x - 1):
                self.board[y][x] = 0

    def next_gen(self):
        survived_creatures = []
        next_gen_creatures = []
        for y in range(1, self.size_y - 1):
            for x in range(1, self.size_x - 1):
                if self.filter_function(x, y, self.board):
                    if type(self.board[y][x]) is not int:
                        survived_creatures.append(self.board[y][x])

        try:
            children_number = floor(self.creature_number / len(survived_creatures))
        except ZeroDivisionError:
            children_number = 0

        for creature in survived_creatures:
            next_gen_creatures.extend(creature.get_children(children_number))
        self.allocate_creatures(next_gen_creatures)



    def allocate_creatures(self, creatures):
        self.clear_board()
        self.creatures = creatures.copy()
        for creature in creatures:
            n_x, n_y = randint(0, self.size_x - 1), randint(0, self.size_y - 1)
            while self.board[n_y][n_x] != 0:
                n_x, n_y = randint(0, self.size_x - 1), randint(0, self.size_y - 1)
            self.board[n_y][n_x] = creature
            creature.set_cords(n_x, n_y)

    def cell_free(self, x, y):
        try:
            return self.board[y][x] == 0
        except IndexError:
            return False

    def cell_populated(self, x, y):
        return self.board[y][x] is not int

    def next_iter(self):
        for creature in self.creatures:
            new_pos = creature.next_cords()
            if self.cell_free(*new_pos):
                x, y = creature.get_cords()
                n_x, n_y = new_pos
                self.board[y][x] = 0
                self.board[n_y][n_x] = creature
                creature.set_cords(n_x, n_y)
