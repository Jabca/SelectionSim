from lib.creature.genome import Genome
from igraph import Graph, plot


def plot_genome_as_graph(genome):
    vertices = set()
    for con in genome.connections:
        vertices.add(con.parent)
        vertices.add(con.child)

    i = 0
    d = {}
    g = Graph(directed=True)
    for el in vertices:
        d[el] = i
        i += 1
        g.add_vertex(type(el).__name__)

    for el in genome.connections:
        g.add_edge(d[el.parent], d[el.child], weight=el.weight)

    for v in g.vs:
        # print(v["name"])
        v["label"] = v["name"]
        if v["name"] in ["PR", "PL", "PD", "PU", "DL", "DU", "RND"]:
            v["color"] = "lightpink"
        elif v["name"] in ["ML", "MR", "MD", "MU"]:
            v["color"] = "lightblue"
        else:
            v["color"] = "lightgrey"

    for e in g.es:
        if e['weight'] < 0:
            e['color'] = 'lightcoral'
        elif e['weight'] == 0:
            e['color'] = 'grey'
        else:
            e['color'] = 'green'

        width = abs(e['weight'])
        e['width'] = 1 + 1.25 * width

    layout = g.layout(layout="fruchterman_reingold")
    print(g)
    g.es["curved"] = False
    plot(g, layout=layout, edge_curved=True)

