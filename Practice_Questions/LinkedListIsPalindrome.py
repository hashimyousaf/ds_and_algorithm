class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self, data):
        self.head = Node(data=data)
        self.tail = self.head
        self.head.next = None

    def add(self, data):
        temp = self.head
        node = Node(data)
        while temp.next:
            temp = temp.next
        temp.next = node
        self.tail = node

    def __iter__(self):
        temp = self.head
        while temp:
            yield temp
            temp = temp.next




def is_palindrome(stack, fastrunner, slow):
# This method should take slow runner to the half of the list while populating
# elements to the stack
# R -> A -> D -> A -> R
    if not (fastrunner and fastrunner.next):
        return slow, fastrunner
    else:
        stack.append(slow.data)
        return is_palindrome(stack, fastrunner.next.next, slow.next)

def check_palindrome(ll):
    stack = []
    slow, fast = is_palindrome(stack, ll.head, ll.head)
    if fast:
        slow = slow.next

    while slow:
        if slow.data != stack.pop():
            return False
        slow = slow.next
    return True

ll = linkedList("R")
ll.add("A")
ll.add("D")
ll.add("A")
ll.add("R")

print(check_palindrome(ll))


