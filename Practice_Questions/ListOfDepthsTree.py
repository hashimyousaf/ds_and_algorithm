class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None

    def add(self, val):
        if self.next == None:
            self.next = LinkedList(val)
        else:
            self.next.add(val)

    def __str__(self):
        return "({val})".format(val=self.val) + str(self.next)


class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def depth(tree):
    if tree is None:
        return 0
    if tree.left is None and tree.right is None:
        return 1
    else:
        depth_left = 1 + depth(tree.left)
        depth_right = 1 + depth(tree.right)
        return max(depth_left, depth_right)


def treeToLinkedList(tree, custDict={}, d=None):
    if not tree:
        return None
    else:
        if d in custDict:
            custDict[d].add(tree.val)
        else:
            custDict[d] = LinkedList(tree.val)
        treeToLinkedList(tree.left, custDict, d-1)
        treeToLinkedList(tree.right, custDict, d -1)
        return custDict

tree = BinaryTree(1)
two = BinaryTree(2)
three = BinaryTree(3)
four = BinaryTree(4)
five = BinaryTree(5)
six = BinaryTree(6)
seven = BinaryTree(7)

tree.left = two
tree.right = three
two.left = four
two.right = five
three.left = six
three.right = seven

test_dict = {}

depth_of_the_tree = depth(tree)
test_dict = treeToLinkedList(tree, test_dict, depth_of_the_tree)
print("Hashim")
print(test_dict)