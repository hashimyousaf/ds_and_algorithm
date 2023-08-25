#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

# Disjoint Set in Python

class DisjointSet:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {}
        for v in vertices:
            self.parent[v] = v
            # parent {"A": "A", "B": "B", "C": "C", "D": "D", "E": "E"}
        self.rank = dict.fromkeys(vertices, 0)
        #  rank {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}
    
    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            return self.find(self.parent[item])
    
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1

# vertices = ["A", "B", "C", "D", "E"]

# ds = DisjointSet(vertices)
# ds.union("A", "B")
#  # # # parent {"A": "A", "B": "A", "C": "C", "D": "D", "E": "E"}
#  # # # rank {"A": 1, "B": 0, "C": 0, "D": 0, "E": 0}

# ds.union("A", "C")
#  # # # parent {"A": "A", "B": "A", "C": "A", "D": "D", "E": "E"}
#  # # # rank {"A": 1, "B": 0, "C": 0, "D": 0, "E": 0}
# print(ds.find("A"))