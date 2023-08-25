from collections import defaultdict

class Graph():
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance


def dijkstra(graph, initial):
    visited = {initial: 0}
    path = defaultdict(list)

    # Assigning nodes to new variable because we have to remove nodes from them
    # Won't like to remove it from actual graph nodes variables.
    nodes = set(graph.nodes)

    while nodes:
        minNode = None
        for node in nodes:
            # Because we are only interested in already visited node, why would we be interested in G or F when
            # our counting on minimum distance did not reach uptill those node which we have not visited yet.
            if node in visited:
                if minNode is None:
                    minNode = node
                elif visited[node] < visited[minNode]:
                    minNode = node

        # This can also be the statement that can exit outer loop
        if minNode is None:
            break

        # This will help us to exit outer loop.
        nodes.remove(minNode)
        currentWeight = visited[minNode]

        for edge in graph.edges[minNode]:
            weight = currentWeight + graph.distances[(minNode, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(minNode)

    return visited, path

customGraph = Graph()
customGraph.add_node("A")
customGraph.add_node("B")
customGraph.add_node("C")
customGraph.add_node("D")
customGraph.add_node("E")
customGraph.add_node("F")
customGraph.add_node("G")
customGraph.add_edge("A", "B", 2)
customGraph.add_edge("A", "C", 5)
customGraph.add_edge("B", "C", 6)
customGraph.add_edge("B", "D", 1)
customGraph.add_edge("B", "E", 3)
customGraph.add_edge("C", "F", 8)
customGraph.add_edge("D", "E", 4)
customGraph.add_edge("E", "G", 9)
customGraph.add_edge("F", "G", 7)

print(dijkstra(customGraph, "A"))