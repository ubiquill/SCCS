#####################################################################
# randGraph1
#
# Params: V: number of vertices
#         E: number of edges
#####################################################################
def randGraph1(V,E):
    newGraph = Graph()
    random.seed()
    # initialize all vertices
    for v in range(0,V):
        newGraph.addVertex(v, [])
    e = 0
    # choose a possible edge at random and at it to the graph
    while (e < E):
        vert = random.randint(0,V-1)
        edge = random.randint(0,V-1)
        # Parallel edges are not very interesting so I forbid them
        if (newGraph.vertices[vert][1].count(edge) == 0):
            newGraph.vertices[vert][1].append(edge)
            e += 1
    return newGraph
