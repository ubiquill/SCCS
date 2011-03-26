#####################################################################
# cliqueForest
#
# Params: V:        total number of vertices
#         sccs:     number of strongly connected components in 
#                   resulting graph
#         nodesPer: Nodes per clique
##################################################################### 
def cliqueForest(V, sccs, nodesPer):
    newGraph = Graph()                   # initialize the new graph
    # initialize each vertex
    for v in range(0,V):
        newGraph.addVertex(v, [])
    currVert = 0
    # create cliques
    for i in range(0,sccs):
        # cliques consist of nodes between currVert and
        # (currVert + nodesPer)
        for v in range(currVert, currVert + nodesPer):
            ll = []
            # add each vertex in the clique to every others
            # adjacency list
            ll = range(currVert,currVert + nodesPer)
            newGraph.vertices[v][1].extend(ll)
            # add a few random edges to the graph while ensuring
            # no cycles between cliques are formed
            if ((random.randint(0,100) % 2 == 0) and (i < (sccs - 1))):
              randEdge = [random.randint((currVert + nodesPer), (V - 1))]
              newGraph.vertices[v][1].extend(randEdge)
        currVert += nodesPer
    return newGraph
