class Node:
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None

def insert(node, data):
   if node is None:
       return Node(data)
   else:
       if data <= node.data:
           temp = insert(node.left, data)
           node.left = temp
           temp.parent = node
       else:
           temp = insert(node.right, data)
           node.right = temp
           temp.parent = node
       return node


def inOrderSuccessor(root, n):
    if n.right is not None:
        demo = n.right
        while demo.left:
            demo = demo.left
        return demo
    elif n.right is None and n.left is None:
        return None
    else:
        parent = n.parent
        while parent is not None:
            if n != parent.right:
                break
            n = parent
            parent = parent.parent

        return parent

root = None
root = insert(root, 4)
root = insert(root, 2)
root = insert(root, 8)
root = insert(root, 1)
root = insert(root, 3)
root = insert(root, 5)
root = insert(root, 9)

temp = root.right.right
successor = inOrderSuccessor(root, temp)

if successor is not None:
    print("Successor of {} of {}".format(temp.data, successor.data))
else:
    print("Inorder Sucessor does not exist")