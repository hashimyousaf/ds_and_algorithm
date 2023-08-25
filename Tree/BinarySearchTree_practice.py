
class BSTNode():
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


class BST():
    def __init__(self, data=None):
        self.root_node = BSTNode(data)

def insert_node(root_node, node_value):
    if root_node.data is None:
        root_node.data = node_value
    else:
        if node_value <= root_node.data :
            if root_node.left_child is None:
                root_node.left_child = BSTNode(node_value)
            else:
                insert_node(root_node.left_child, node_value)
        else:
            if root_node.right_child is None:
                root_node.right_child = BSTNode(node_value)
            else:
                insert_node(root_node.right_child, node_value)

def search_node(root_node, node_value):
    if root_node.data == node_value:
        return "Value Found"
    elif node_value < root_node.data:
        if root_node.left_child.data == node_value:
            return "Value Found"
        search_node(root_node.left_child, node_value)
    else:
        if root_node.right_child.data == node_value:
            return "Value Found"
        search_node(root_node.righ_child, node_value)

def in_order_traversal(rootNode: BSTNode): #  root -->  left --> right
    if not rootNode:
        return
    in_order_traversal(rootNode.left_child)
    print(rootNode.data)
    in_order_traversal(rootNode.right_child)

binary_search_tree = BST(70)
insert_node(binary_search_tree.root_node, 36)
insert_node(binary_search_tree.root_node, 80)
insert_node(binary_search_tree.root_node, 20)
insert_node(binary_search_tree.root_node, 40)
insert_node(binary_search_tree.root_node, 50)
insert_node(binary_search_tree.root_node, 75)
insert_node(binary_search_tree.root_node, 90)
insert_node(binary_search_tree.root_node, 20)

in_order_traversal(binary_search_tree.root_node)

print(search_node(binary_search_tree.root_node, 234))
