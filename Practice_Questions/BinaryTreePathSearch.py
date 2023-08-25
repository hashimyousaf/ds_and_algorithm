# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def add_children(self, left, right):
        self.left = left
        self.right = right
class Solution:

    def find_path(self, root, start, dest, start_tracking_path):
        if not root:
            if self.path:
                self.path.pop()
            return None
        if root.val == start:
            start_tracking_path = True
            self.path = []
        if root.val == dest and start_tracking_path is True:
            #print("".join(self.path))
            return self.path
        else:
            self.path.append("L")
            if_path = self.find_path(root.left, start, dest, start_tracking_path)
            if if_path: return if_path
            self.path.append("R")
            if_path = self.find_path(root.right, start, dest, start_tracking_path)
            if if_path: return if_path
        self.path.append("U")


    def getDirections(self, root, startValue: int, destValue: int) -> str:
        # First you need to reach to the node which is source in your case
        # If you are there then start collectin/printing path
        # Whenever there is pop it's U action
        # On Left it's L
        # On Right it's R
        self.path = []
        self.find_path(root, startValue, destValue, False)
        return "".join(self.path)

if __name__ == '__main__':
    # tree = TreeNode(5)
    # one = TreeNode(1)
    # two = TreeNode(2)
    # three = TreeNode(3)
    # four = TreeNode(4)
    # six = TreeNode(6)
    # tree.add_children(one, two)
    # one.add_children(three, None)
    # two.add_children(six, four)
    # print(Solution().getDirections(tree, 3, 6))

    one_tree = TreeNode(1)
    two_child = TreeNode(2)
    one_tree.add_children(two_child, None)

    print(Solution().getDirections(one_tree, 2, 1))