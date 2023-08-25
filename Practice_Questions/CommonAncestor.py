# Design an algo and write code to find the first common ancestor of two nodes in a binary tree.

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def add_children(self, left = None, right = None):
        self.left = left
        self.right = right


def if_exist_recursive(root, node_to_check):
    if not root:
        return False
    elif root.val == node_to_check:
        return True
    else:
        return (if_exist_recursive(root.left, node_to_check) or
                if_exist_recursive(root.right, node_to_check))

def if_exist(root, node_to_check):
    # It will work in O(n)
    queue = [root]
    while queue:
        deq = queue.pop(0)
        if deq.val == node_to_check:
            return True
        if deq.left is not None:
            queue.append(deq.left)
        if deq.right is not None:
            queue.append(deq.right)
    return False

def common_ancestor_utlity(first, second, root):
    # Now check which side do they exist, are the both at one side
    # also additional check if root itself is one of them, we are gonna return the same root as ancestor
    if root.val == first or root.val == second:
        return root  # this is itself a common ancestor
    else:
        first_at_left_side = if_exist(root.left, first)
        second_at_left_side = if_exist(root.left, second)
        first_at_right_side = if_exist(root.right, first)
        second_at_right_side = if_exist(root.right, second)

        if first_at_left_side and second_at_left_side:
            # traverse the left tree
            return find_common_ancestor(first, second, root.left)
        elif first_at_right_side and second_at_right_side:
            # traverse the right tree
            return find_common_ancestor(first, second, root.right)
        else:
            return root


def find_common_ancestor(first, second, root):
    # First check if they both exist
    if if_exist(root, first) and if_exist(root, second):
        ancestor = common_ancestor_utlity(first, second, root)
        return ancestor.val
    else:
        return None


tree = Node(55)
fourty_four = Node(44)
seventy_seven = Node(77)
twenty_two = Node(22)
ninty_nine = Node(99)
thirty_five = Node(35)
eighty_eight = Node(88)
ninety = Node(90)
ninety_five = Node(95)
fifty_four = Node(54)
thirty_three = Node(33)

tree.add_children(fourty_four, seventy_seven)
fourty_four.add_children(twenty_two, ninty_nine)
twenty_two.add_children(thirty_five, eighty_eight)
eighty_eight.add_children(fifty_four, None)
ninty_nine.add_children(ninety, ninety_five)
ninety.add_children(None, thirty_three)

print(find_common_ancestor(seventy_seven.val, fourty_four.val, tree))
print("Stop it")





