from collections import defaultdict
class Graph:
    def __init__(self, number_of_vertices):
        self.graph = defaultdict(list)
        self.number_of_vertices = number_of_vertices


    def add_edge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def topological_sort_util(self, v, visited, stack):
        visited.append(v)

        for i in self.graph[v]:
            if i not in visited:
                self.topological_sort_util(i, visited, stack)

        stack.insert(0, v)

    def topological_sort(self):

        visited = []
        stack = []

        for k in list(self.graph):
            if k not in visited:
                self.topological_sort_util(k, visited, stack)

        print(stack)




    def practice_topological_util(self, node, stack, visited):

        for i in self.graph[node]:
            if i not in visited:
                visited.append(i)
                self.practice_topological_util(i, stack, visited)
        stack.insert(0, node)


    def practice_topological(self):
        # we have to use DFS strategy(Queue) --> but with topological rule

        # First traverse on all the edges of the nodes
        # on that node go into that level where there will be no edge depends on that(mean dict will be empty)
        # Conditions becomes if there is no unvisited adjacent node or there is no edge attach then just print
        stack = []
        visited = []
        for node in list(self.graph):
            if node not in visited:
                self.practice_topological_util(node, stack, visited)

        print(stack)



graph = Graph(8)
graph.add_edge("A", "C")
graph.add_edge("C", "E")
graph.add_edge("E", "H")
graph.add_edge("E", "F")
graph.add_edge("F", "G")
graph.add_edge("B", "D")
graph.add_edge("B", "C")
graph.add_edge("D", "F")

graph.practice_topological()

print("Hashim Yousaf")

#graph.topological_sort()


