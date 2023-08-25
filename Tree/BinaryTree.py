from Queue_Examples.QueueLinkedList import Queue

class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None

    def add_childs(self, left_child=None, right_child=None):
        self.left_child = left_child
        self.right_child = right_child

def pre_order_traversal(rootNode: TreeNode): #  root -->  left --> right
    if not rootNode:
        return
    print(rootNode.data)
    pre_order_traversal(rootNode.left_child)
    pre_order_traversal(rootNode.right_child)

def in_order_traversal(rootNode: TreeNode): #  root -->  left --> right
    if not rootNode:
        return
    in_order_traversal(rootNode.left_child)
    print(rootNode.data)
    in_order_traversal(rootNode.right_child)

def post_order_traversal(rootNode: TreeNode): #  root -->  left --> right
    if not rootNode:
        return
    post_order_traversal(rootNode.left_child)
    post_order_traversal(rootNode.right_child)
    print(rootNode.data)

def level_order_traversal(rootNode: TreeNode): #  root -->  left --> right
    if not rootNode:
        return
    # node_queue = [rootNode]
    # while node_queue:
    #     node = node_queue.pop(0)
    #     print(node.data)
    #     if node.left_child:
    #         node_queue.append(node.left_child)
    #     if node.right_child:
    #         node_queue.append(node.right_child)

    ## Second way using actual queue to make its performance better
    custome_queue = Queue()
    custome_queue.enqueue(rootNode)
    while not custome_queue.isEmpty():
        node = custome_queue.dequeue()
        print(node.value.data)
        if node.value.left_child:
            custome_queue.enqueue(node.value.left_child)
        if node.value.right_child:
            custome_queue.enqueue(node.value.right_child)

def searchBT(rootNode, node_value):
    custome_queue = Queue()
    custome_queue.enqueue(rootNode)
    while not custome_queue.isEmpty():
        node = custome_queue.dequeue()
        if node.value.data == node_value:
            return "{} Successfully found".format(node.value.data)
        if node.value.left_child:
            custome_queue.enqueue(node.value.left_child)
        if node.value.right_child:
            custome_queue.enqueue(node.value.right_child)
    return "Not found"


def insertNodeBT(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "Successfully Inserted"
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return "Successfully Inserted"


def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        deepestNode = root.value
        return deepestNode


def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value is dNode:
                root.value = None
                return
            if root.value.rightChild:
                if root.value.rightChild is dNode:
                    root.value.rightChild = None
                    return
                else:
                    customQueue.enqueue(root.value.rightChild)
            if root.value.leftChild:
                if root.value.leftChild is dNode:
                    root.value.leftChild = None
                    return
                else:
                    customQueue.enqueue(root.value.leftChild)


def deleteNodeBT(rootNode, node):
    if not rootNode:
        return "The BT does not exist"
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == node:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode, dNode)
                return "The node has been successfully deleted"
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        return "Failed to delete"


def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The BT has been successfully deleted"

if __name__ == '__main__':
    bst_tree = TreeNode("Drinks")
    cold_drink = TreeNode("Cold")
    hot_drink = TreeNode("Hot")
    bst_tree.add_childs(left_child=cold_drink, right_child=hot_drink)

    fanta = TreeNode("Fanta")
    cola = TreeNode("Cola")
    cold_drink.add_childs(left_child=fanta, right_child=cola)

    tea = TreeNode("Tea")
    coffee = TreeNode("Coffee")
    hot_drink.add_childs(left_child=tea, right_child=coffee)

    # Out Tree becomes
    """
                Drink
        
        Cold            Hot
    
    Fanta   Cola    Tea     Coffee
    """
    # print("PreOrder Traversal")
    # pre_order_traversal(bst_tree)

    print("In Order Traversal")
    in_order_traversal(bst_tree)

    print("PostOrder Traversal")
    post_order_traversal(bst_tree)

    print("Level order traversal")
    level_order_traversal(bst_tree)

    print("Search BT using Level order traversal")
    print(searchBT(bst_tree, "Fanta"))
    print(searchBT(bst_tree, "Hashim"))




