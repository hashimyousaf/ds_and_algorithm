from collections import defaultdict


class Tree():
    def __init__(self, node, child):
        self.tree = defaultdict(list)
        self.tree[node] = [child]
        self.stack = []

    def add_edge(self, parent, child):
        if parent in self.tree:
            self.tree[parent].append(child)
        else:
            self.tree[parent] = [child]


    def print_tree(self, root, level, stack):
        print(("   "*level) + root)
        for i in self.tree[root]:
            stack.insert(0, i)
            self.print_tree(i, level+1, stack)
        stack.pop()

# Print Tree in a DFS Order

"""lifeform
   animal
      mamal
         cat
            lion
      bird
      fish
"""
#Soltuion
tree = Tree("animal", "mamal")
tree.add_edge("animal", "bird")
tree.add_edge("lifeform", "animal")
tree.add_edge("cat", "lion")
tree.add_edge("mamal", "cat")
tree.add_edge("animal", "fish")

tree.print_tree("lifeform", 0, ["lifeform"])
