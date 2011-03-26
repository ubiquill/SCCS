#####################################################################
# randGraph2
#
# Params: V:         number of vertices
#         E:         number of edges
#         outDegree: maximum out-degree of each vertex
#####################################################################
def randGraph2(V, E, outDegree = 3):
    ll = []
    ll = range(0,V)        # a list of all vertices
    random.seed()
    newGraph = Graph()
    edgeCount = 0
    verts = range(0,V)     # a second list of all vertices
    random.shuffle(verts)  # the list is shuffled for more randomness
    for i in verts:
        adj = []
        if (edgeCount < E -1):
            # out degree of this vertex is randomly chosen
            rOut = random.randint(1, outDegree) 
            # a random sample of possible edges are taken
            adj = random.sample(ll, rOut)
            if i in adj:
                adj.pop(adj.index(i))  # no self loops
        newGraph.addVertex(i, adj)     # add the vertex to the graph
    return newGraph
