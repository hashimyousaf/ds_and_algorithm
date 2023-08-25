import collections
class TreeNode:
    def __init__(self, data=None):
        self.val = data
        self.left = None
        self.right = None

    def add_childs(self, left_child=None, right_child=None):
        self.left = left_child
        self.right = right_child

def find_leaf(root, ll):
    if root is None:
        return False
    elif root.left is None and root.right is None:
        return True
    else:
        left_leaf = find_leaf(root.left, ll)
        if left_leaf:
            ll.append(root.left.val)
            root.left = None
        right_leaf = find_leaf(root.right, ll)
        if right_leaf:
            ll.append(root.right.val)
            root.right = None
        return False

def find_leaf_improved(root, ll):
    if root is None:
        return None
    elif root.left is None and root.right is None:
        ll.append(root.val)
        return None
    else:
        root.left = find_leaf_improved(root.left, ll)
        root.right = find_leaf_improved(root.right, ll)
        return root

# Solution 2
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.d = collections.defaultdict(list)
        self.dfs(root)
        return self.d.values()

    def dfs(self, node):
        if not node:
            return (0, None)
        left_depth, left_node = self.dfs(node.left)
        right_depth, right_node = self.dfs(node.right)
        depth = max(left_depth, right_depth) + 1
        # self.stack.append((depth, node.val))
        self.d[depth].append(node.val)
        return (depth, node)


if __name__ == '__main__':
    root = TreeNode("Drinks")
    cold_drink = TreeNode("Cold")
    hot_drink = TreeNode("Hot")
    root.add_childs(left_child=cold_drink, right_child=hot_drink)

    fanta = TreeNode("Fanta")
    cola = TreeNode("Cola")
    cold_drink.add_childs(left_child=fanta, right_child=cola)

    tea = TreeNode("Tea")
    coffee = TreeNode("Coffee")
    hot_drink.add_childs(left_child=tea, right_child=None)

    # Out Tree becomes
    """
                Drink

        Cold            Hot

    Fanta   Cola    Tea     Coffee
    """
    # print("PreOrder Traversal")
    # pre_order_traversal(root)


    # Solution 2
    print("Solution 2")
    print(Solution().findLeaves(root))

    final_list = []
    while root:
        temp_list = []
        root = find_leaf_improved(root, temp_list)
        final_list.append(temp_list)

    print(final_list)
    # print(leaf_list)



