from lib.creature.creture import Creature
from lib.field.fiel_renderer import FieldRenderer
from lib.field.field import Field


def main():
    field = Field(lambda x, y: True)
    creatures = []
    for x in range(field.creature_number):
        creatures.append(Creature(None))
    field.allocate_creatures(creatures)

    renderer = FieldRenderer(field)
    renderer.start_loop()


if __name__ == "__main__":
    main()
