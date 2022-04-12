from lib.creature.creture import Creature
from lib.field.field_renderer import FieldRenderer
from lib.field.field import Field
from lib.creature.genome import Genome
from statitics.log_genomes import write_genomes_to
from statitics.plot_genome_as_graph import plot_genome_as_graph

def filter_function(x, y, field):
    return x >= 110 and y >= 110


def main():
    field = Field(filter_function, size_x=128, size_y=128)
    creatures = []
    for x in range(field.creature_number):
        creature = Creature(None, field)
        genome = Genome(creature, genes_amount=6)
        creature.genome = genome
        creatures.append(creature)

    field.allocate_creatures(creatures)

    renderer = FieldRenderer(field, iters_per_gen=100)
    renderer.generate_colors()
    renderer.start_loop()
    write_genomes_to("genomes.txt", field.creatures)
    plot_genome_as_graph(field.creatures[0].genome)


if __name__ == "__main__":
    main()
