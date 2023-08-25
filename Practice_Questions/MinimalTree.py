import math


class BSTNode:
    def __init__(self, data=None, left = None, right= None):
        self.data = data
        self.left = left
        self.right = right

def minimalTree(sortedArray):
    if len(sortedArray) == 0:
        return None
    if len(sortedArray) == 1:
        return BSTNode(sortedArray[0])
    mid = int(len(sortedArray)/2)
    left = minimalTree(sortedArray[:mid])
    right = minimalTree(sortedArray[mid+1:])
    return BSTNode(sortedArray[mid], left, right)

def level_order_traversal(root_node):
    queue = [root_node]
    while queue:
        deq_element = queue.pop(0)
        print(deq_element.data)
        if deq_element.left is not None:
            queue.append(deq_element.left)
        if deq_element.right is not None:
            queue.append(deq_element.right)



sortedArray = [1,2,3,4,5]
root_node = minimalTree(sortedArray)
level_order_traversal(root_node)