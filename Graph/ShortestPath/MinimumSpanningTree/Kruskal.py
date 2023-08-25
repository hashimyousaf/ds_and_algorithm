#   Created by Elshad Karimov
#   Copyright © 2021 AppMillers. All rights reserved.

# Kruskal Algorithm  in Python
import DisjointSet as dst


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.nodes = []
        self.MST = []

    def addEdge(self, s, d, w):
        self.graph.append([s, d, w])

    def addNode(self, value):
        self.nodes.append(value)

    def printSolution(self, s, d, w):
        for s, d, w in self.MST:
            print("%s - %s: %s" % (s, d, w))

    def kruskalAlgo(self):
        i, e = 0, 0
        ds = dst.DisjointSet(self.nodes)
        self.graph = sorted(self.graph, key=lambda item: item[2])
        while e < self.V - 1: # -1, because we want to avoid cycle minimum edges would always be  = node - 1
            s, d, w = self.graph[i]
            i += 1
            x = ds.find(s)
            y = ds.find(d)
            if x != y:
                e += 1
                self.MST.append([s, d, w])
                ds.union(x, y)
        self.printSolution(s, d, w)


g = Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.addEdge("A", "B", 5)
g.addEdge("A", "C", 13)
g.addEdge("A", "E", 15)
g.addEdge("B", "A", 5)
g.addEdge("B", "C", 10)
g.addEdge("B", "D", 8)
g.addEdge("C", "A", 13)
g.addEdge("C", "B", 10)
g.addEdge("C", "E", 20)
g.addEdge("C", "D", 6)
g.addEdge("D", "B", 8)
g.addEdge("D", "C", 6)
g.addEdge("E", "A", 15)
g.addEdge("E", "C", 20)

g.kruskalAlgo()

"""from collections import deque

from collections import defaultdict
import DisjointSet as dst

class Graph():
    def __init__(self, vertices=None):
        if vertices is None:
            self.vertices = set()
        else:
            self.vertices = vertices

        self.edges = defaultdict(list)
        self.distances = {}
        self.stack = deque()
        self.visited = []


    def add_vertices(self, vertices):
        self.vertices = vertices

    def add_vertex(self, vertex):
        self.vertices.append(vertex)

    def add_weighted_edge(self, from_vertex, to_vertex, weight):
        self.edges[from_vertex].append(to_vertex)
        self.distances[(from_vertex, to_vertex)] = weight

    def print_graph_using_dfs(self, vertex):
        self.stack.append(vertex)
        print(vertex)
        self.visited.append(vertex)

        for i in self.edges[vertex]:
            if i not in self.visited:
                self.print_graph_using_dfs(i)
        self.stack.pop()

    # def kruskal_algo(self):
        # kruskal_graph = []
        # for vertex in self.vertices:
        #     for edge in self.edges[vertex]:
        # i, e = 0, 0
        # ds = dst.DisjointSet(self.vertices)
        # self.edges = sorted(self.edges, key=lambda item: item[2])
        # while e



graph = Graph(('a', 'b', 'c', 'd', 'e'))
graph.add_weighted_edge('a', 'e', 15)
graph.add_weighted_edge('a', 'c', 13)
graph.add_weighted_edge('a', 'b', 5)

graph.add_weighted_edge('b', 'a', 5)
graph.add_weighted_edge('b', 'c', 10)
graph.add_weighted_edge('b', 'd', 8)

graph.add_weighted_edge('c', 'a', 13)
graph.add_weighted_edge('c', 'b', 10)
graph.add_weighted_edge('c', 'd', 6)

graph.add_weighted_edge('d', 'c', 6)
graph.add_weighted_edge('d', 'b', 8)

graph.add_weighted_edge('e', 'a', 15)
graph.add_weighted_edge('e', 'c', 20)

graph.print_graph_using_dfs('a')
print("hashim")"""