class Heap:
    def __init__(self, size):
        self.custom_list = (size+1) * [None]
        self.heap_size = 0
        self.max_size = size + 1 # because don't want to use the 0th index to make calculations easy.

def peak_heap(root_node):
    if not root_node:
        return
    else:
        return root_node.custom_list[1]

def size_of_heap(root_node):
    if not root_node:
        return
    else:
        return root_node.heap_size

def level_order_traversal(root_node):
    if not root_node:
        return
    else:
        for i in range(1, root_node.heap_size+1):
            print(root_node.custom_list[i])

def heapify_tree_insert(root_node, index, heap_type):
    parent_index = int(index/2)
    if index <= 1:
        return
    if heap_type == "min":
        if root_node.custom_list[parent_index] > root_node.custom_list[index]:
            temp = root_node.custom_list[parent_index]
            root_node.custom_list[parent_index] = root_node.custom_list[index]
            root_node.custom_list[index] = temp
        heapify_tree_insert(root_node, parent_index, heap_type)
    elif heap_type == "max":
        if root_node.custom_list[parent_index] < root_node.custom_list[index]:
            temp = root_node.custom_list[parent_index]
            root_node.custom_list[parent_index] = root_node.custom_list[index]
            root_node.custom_list[index] = temp
        heapify_tree_insert(root_node, parent_index, heap_type)

def insert_node(root_node, node_value, heap_type):
    if not root_node:
        return
    root_node.custom_list[root_node.heap_size + 1] = node_value
    root_node.heap_size += 1
    heapify_tree_insert(root_node, root_node.heap_size, heap_type)

def heapifyTreeExtract(rootNode, index, heapType):
    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swapChild = 0

    if rootNode.heap_size < leftIndex:
        return
    elif rootNode.heap_size == leftIndex:
        if heapType == "min":
            if rootNode.custom_list[index] > rootNode.custom_list[leftIndex]:
                temp = rootNode.custom_list[index]
                rootNode.custom_list[index] = rootNode.custom_list[leftIndex]
                rootNode.custom_list[leftIndex] = temp
            return
        else:
            if rootNode.custom_list[index] < rootNode.custom_list[leftIndex]:
                temp = rootNode.custom_list[index]
                rootNode.custom_list[index] = rootNode.custom_list[leftIndex]
                rootNode.custom_list[leftIndex] = temp
            return

    else:
        if heapType == "min":
            if rootNode.custom_list[leftIndex] < rootNode.custom_list[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.custom_list[index] > rootNode.custom_list[swapChild]:
                temp = rootNode.custom_list[index]
                rootNode.custom_list[index] = rootNode.custom_list[swapChild]
                rootNode.custom_list[swapChild] = temp
        else:
            if rootNode.custom_list[leftIndex] > rootNode.custom_list[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.custom_list[index] < rootNode.custom_list[swapChild]:
                temp = rootNode.custom_list[index]
                rootNode.custom_list[index] = rootNode.custom_list[swapChild]
                rootNode.custom_list[swapChild] = temp
    heapifyTreeExtract(rootNode, swapChild, heapType)

def extractNode(rootNode, heapType):
    if rootNode.heap_size == 0:
        return
    else:
        extractedNode = rootNode.custom_list[1]
        rootNode.custom_list[1] = rootNode.custom_list[rootNode.heap_size]
        rootNode.custom_list[rootNode.heap_size] = None
        rootNode.heap_size -= 1
        heapifyTreeExtract(rootNode, 1, heapType)
        return extractedNode

def deleteEntireBP(rootNode):
    rootNode.custom_list = None


binary_heap = Heap(5)
insert_node(binary_heap, 4, "min")
insert_node(binary_heap, 5, "min")
insert_node(binary_heap, 2, "min")
insert_node(binary_heap, 1, "min")
print("Extracted Node ", extractNode(binary_heap, "min"))
print("Extracted Node ", extractNode(binary_heap, "min"))
level_order_traversal(binary_heap)

"""
                    5
            4            4
        1  
"""