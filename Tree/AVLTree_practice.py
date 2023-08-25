import Queue_Examples.QueueLinkedList as queue
class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.height = 1

def pre_order_traversal(rootNode): #  root -->  left --> right
    if not rootNode:
        return
    print(rootNode.data)
    pre_order_traversal(rootNode.left_child)
    pre_order_traversal(rootNode.right_child)

def in_order_traversal(rootNode): #  root -->  left --> right
    if not rootNode:
        return
    in_order_traversal(rootNode.left_child)
    print(rootNode.data)
    in_order_traversal(rootNode.right_child)

def post_order_traversal(rootNode): #  root -->  left --> right
    if not rootNode:
        return
    post_order_traversal(rootNode.left_child)
    post_order_traversal(rootNode.right_child)
    print(rootNode.data)


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.left_child is not None:
                customQueue.enqueue(root.value.left_child)
            if root.value.right_child is not None:
                customQueue.enqueue(root.value.right_child)


def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print("The value is found")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild.data == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.rightChild, nodeValue)


def right_rotate(disbalanced_node):
    new_root = disbalanced_node.left_child
    disbalanced_node.left_child = disbalanced_node.left_child.right_child
    new_root.right_child = disbalanced_node

    disbalanced_node.height = 1 + max(get_height(disbalanced_node.left_child), get_height(disbalanced_node.right_child))
    new_root.height = 1 + max(get_height(new_root.left_child), get_height(new_root.right_child))

    return new_root


def left_rotate(disbalanced_node):
    new_root = disbalanced_node.right_child
    disbalanced_node.right_child = disbalanced_node.right_child.left_child
    new_root.left_child = disbalanced_node

    disbalanced_node.height = 1 + max(get_height(disbalanced_node.left_child), get_height(disbalanced_node.right_child))
    new_root.height = 1 + max(get_height(new_root.left_child), get_height(new_root.right_child))

    return new_root

def get_height(root_node):
    if not root_node:
        return 0
    return root_node.height

def get_balance(root_node):
    if not root_node:
        return 0
    return get_height(root_node.left_child) - get_height(root_node.right_child)

def insert_node(root_node, node_value):
    if not root_node:
        return AVLNode(node_value)
    elif node_value <= root_node.data:
        root_node.left_child = insert_node(root_node.left_child, node_value)
    else:
        root_node.right_child = insert_node(root_node.right_child, node_value)

    root_node.height = 1 + max(get_height(root_node.left_child), get_height(root_node.right_child))
    balance = get_balance(root_node)

    if balance > 1 and node_value < root_node.left_child.data:  # mean LL condition
        return right_rotate(root_node)
    if balance > 1 and node_value > root_node.left_child.data:  # mean LR condition
        root_node.left_child = left_rotate(root_node.left_child)
        return right_rotate(root_node)

    if balance < -1 and node_value > root_node.right_child.data:  # mean RR condition
        return left_rotate(root_node)
    if balance < -1 and node_value < root_node.right_child.data:  # mean RL condition
        root_node.right_child = left_rotate(root_node.right_child)
        return left_rotate(root_node)

    return root_node

#Deletion of node from adelsin velenski and lendis tree

def get_min_value(root_node):
    if root_node is None or root_node.left_child is None:
        return root_node
    return get_min_value(root_node.left_child)


def deleteNode(rootNode, nodeValue):
    if not rootNode:
        return rootNode
    elif nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        elif rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        temp = get_min_value(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    balance = get_balance(rootNode)
    if balance > 1 and get_balance(rootNode.leftChild) >= 0:
        return right_rotate(rootNode)
    if balance < -1 and get_balance(rootNode.rightChild) <= 0:
        return left_rotate(rootNode)
    if balance > 1 and get_balance(rootNode.leftChild) < 0:
        rootNode.leftChild = left_rotate(rootNode.leftChild)
        return right_rotate(rootNode)
    if balance < -1 and get_balance(rootNode.rightChild) > 0:
        rootNode.rightChild = right_rotate(rootNode.rightChild)
        return left_rotate(rootNode)

    return rootNode


newAVL = AVLNode(5)
newAVL = insert_node(newAVL, 10)
newAVL = insert_node(newAVL, 15)
newAVL = insert_node(newAVL, 20)



levelOrderTraversal(newAVL)
