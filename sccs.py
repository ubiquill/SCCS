#!/usr/bin/env python

#################################################
# sccs.py
# Copyright 2011 Thomas Schreiber
#
# An algorithm for finding the strongly connected
# components of a graph.
# 
# Created for CS350 Winter 2011 PSU
#################################################

import random
import time
import matplotlib.pyplot as plt

class Graph():
    def __init__(self, t=False):
        self.vertices = {}
        self.discovery = []
        self.finish = []
        self.t = 0
        self.isTranspose = t
        self.vertCnt = 0
        self.edgeCnt = 0
        self.components = []
        self.compCount = 0
        
    
    def addVertex(self, vId, edges):
        self.vertices[vId] = ["unvisited", edges]

    def dfs(self):
        for k,v in self.vertices.items():
            v[0] = "unvisited"
        self.time = 0
        if (self.isTranspose):
            self.revfinish = list(self.finish)
            self.revfinish.reverse()
            for v in self.revfinish:
                if(self.vertices[v][0] == "unvisited"):
                    self.components += [[v]] 
                    self.visit(v,v)
                self.compCount += 1
        else:
            for k,v in self.vertices.items():
                if(v[0] == "unvisited"):
                    self.visit(v,k)
            self.t.finish = self.finish

    def visit(self, u, idx):
        self.vertices[idx][0] = "discovered"
        
        self.time = self.time + 1
        self.discovery.append(idx)

        for v in self.vertices[idx][1]:
            if (self.vertices[v][0] == "unvisited"):
                self.visit(v,v)
                if(self.isTranspose):
                    #print self.finish
                    #print self.components
                    #print self.compCount
                    self.components[len(self.components) - 1].append(v)
                              
        self.vertices[idx][0] = "visited"
        self.time = self.time + 1
        self.finish.append(idx)

    def transpose(self):
        newGraph = Graph(True)
        for v in range(0,len(self.vertices)):
            newGraph.addVertex(v, [])
            self.vertCnt += 1
        
        for k,v in self.vertices.items():
            for adjacent in v[1]:
                if (newGraph.vertices.has_key(adjacent)):
                    (newGraph.vertices[adjacent])[1].append(k)
                    self.edgeCnt += 1
                else:
                    newGraph.vertices[adjacent] = ["unvisited", [ k ]]
                    self.edgeCnt += 1

        newGraph.isTranspose = True
        return newGraph

    def sccs(self):
        components = []
        self.dfs()
        self.t.dfs()
        self.components = self.t.components
        return self.components
        

def createRandGraph(V, E, outDegree = 2):
    ll = []
    ll = range(0,V)
    random.seed()
    newGraph = Graph()
    edgeCount = 0
    verts = range(0,V)
    random.shuffle(verts)
    for i in verts:
        adj = []
        if (edgeCount < E -1):
            rOut = random.randint(1, outDegree)
            adj = random.sample(ll, rOut)
            edgeCount += len(adj)
            if i in adj:
                adj.pop(adj.index(i))
        newGraph.addVertex(i, adj)
    newGraph.vertCnt = V
    newGraph.edgeCnt = E
    #newGraph.t = newGraph.transpose()
    return newGraph

def randGraph2(V,E):
    newGraph = Graph()
    random.seed()
    newGraph.vertCnt = V
    newGraph.edgeCnt = E
    for v in range(0,V):
        newGraph.addVertex(v, [])
    e = 0
    while (e < E):
        vert = random.randint(0,V-1)
        edge = random.randint(0,V-1)
        if (newGraph.vertices[vert][1].count(edge) == 0):
            newGraph.vertices[vert][1].append(edge)
            e += 1
    newGraph.t = newGraph.transpose()
    return newGraph

def randGraph3(V, sccs, nodesPer):
    newGraph = Graph()
    for v in range(0,V):
        newGraph.addVertex(v, [])
        newGraph.vertCnt += 1
    currVert = 0
    for i in range(0,sccs):
        for v in range(currVert, currVert + nodesPer):
            ll = []
            ll = range(currVert,currVert + nodesPer)
            newGraph.vertices[v][1].extend(ll)
            newGraph.edgeCnt += nodesPer
            if ((random.randint(0,100) % 2 == 0) and (i < (sccs - 1))):
              randEdge = [random.randint((currVert + nodesPer), (V - 1))]
              newGraph.vertices[v][1].extend(randEdge)
              newGraph.edgeCnt += 1
        currVert += nodesPer
    #newGraph.t = newGraph.transpose()
    return newGraph

def randUndirected(V,E):
    newGraph = Graph()
    for v in range(0,V):
        newGraph.addVertex(v,[])
    e = 0
    random.seed()
    while e < E:
        u = random.randint(0,V-1)
        w = random.randint(0,V-1)
        newGraph.vertices[u][1].append(w)
        newGraph.vertices[w][1].append(u)
        e += 1
    newGraph.vertCnt = V
    newGraph.edgeCnt = E
    #newGraph.t = newGraph.transpose()
    return newGraph
        


if __name__ == "__main__":
    tTimes = []
    ve = []
    for i in range(0,100):
        V = (i+2) 
        E = random.randint(V, 3*V)
        graph4 = randGraph3(V*V, V, V)
        time1 = time.time()
        graph4.t = graph4.transpose()
        graph4.sccs()
        time2 = time.time()
        totalTime = time2 - time1
        tTimes.append(totalTime)
        vPlusE = graph4.vertCnt + graph4.edgeCnt
        ve.append(vPlusE)
    plt.plot(ve, tTimes)
    plt.ylabel('Time (seconds)')
    plt.xlabel('V + E (vertices + edges)')
    plt.show()

