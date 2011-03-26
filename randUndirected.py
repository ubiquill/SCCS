#####################################################################
# randUndirected
#
# Params: V: number of vertices
#         E: number of edges
#####################################################################
def randUndirected(V,E):
    # initialize new graph and vertices
    newGraph = Graph()
    for v in range(0,V):
        newGraph.addVertex(v,[])
    e = 0
    random.seed()
    # for every edge added that connects u to w
    # add another that connects w to u
    while e < E:
        u = random.randint(0,V-1)
        w = random.randint(0,V-1)
        newGraph.vertices[u][1].append(w)
        newGraph.vertices[w][1].append(u)
        e += 1
    return newGraph
