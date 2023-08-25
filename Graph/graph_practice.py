
class Graph:
    def __init__(self, gdict=None):
        self.visited_dict = {}
        self.stack = []
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def add_edge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def bfs(self, vertex):
        visited = [vertex]
        queue = [vertex]

        while queue:
            deq_vertex = queue.pop(0)
            print(deq_vertex)
            for adjacent_vertex in self.gdict[deq_vertex]:
                if adjacent_vertex not in visited:
                    visited.append(adjacent_vertex)
                    queue.append(adjacent_vertex)

    def dfs_recursive(self, vertex):
        if vertex not in self.visited_dict:
            self.visited_dict[vertex] = True
            print(vertex)
            for i in self.gdict[vertex]:
                self.stack.append(i)
                self.dfs_recursive(i)
        else:
            self.stack.pop()

    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]

        while stack:
            poped_element = stack.pop()
            print(poped_element)
            for adjacent_vertex in self.gdict[poped_element]:
                if adjacent_vertex not in visited:
                    visited.append(adjacent_vertex)
                    stack.append(adjacent_vertex)


def dfs_true(graph , vertex):
    visited = []
    stack = [vertex]

    while stack:
        poped_element = stack.pop()
        print(poped_element)
        for i in graph[poped_element]:
            if i not in visited:
                visited.append(i)
                stack.append(i)


# DFS --> 1 - 2 -5 - 8 - 7 - 9 - 6 - 3 - 4
test_tree = {
            "1" : ["2", "3", "4"],
            "2" : ["5", "6", "7"],
            "3" : ["4"],
            "4" : [],
            "5" : ["8"],
            "6" : [],
            "7" : ["9"],
            "8" : ["7"],
            "9" : []
            }

custom_dict = {
            "a" : ["b","c"],
            "b" : ["a", "d", "e"],
            "c" : ["a", "e"],
            "d" : ["b", "e", "f"],
            "e" : ["d", "f", "c"],
            "f" : ["d", "e"]
            }
graph = Graph(test_tree)
# graph.add_edge("e", "c")
# print(graph.gdict)

# graph.bfs("a")
graph.dfs("1")
print("Using recursive DFS")
graph.dfs_recursive("1")
print("DFS True")
dfs_true(test_tree, "1")
