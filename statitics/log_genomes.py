from lib.field.field import Field


def write_genomes_to(file_name, creatures):
    genomes = set()
    for creature in creatures:
        genomes.add(creature.genome)
    with open(file_name, mode="w") as file:
        for genome in genomes:
            print("==============", file=file)
            for i, con in enumerate(genome.connections):
                print(
                    i, "   ",
                    con.parent.__class__,
                    con.child.__class__,
                    con.weight, file=file
                )
