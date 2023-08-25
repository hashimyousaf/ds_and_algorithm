"""
Stack Min: How would you design a stack which, in addition to push and pop, has a function min which returns the
 minimum element? Push, pop and min should all operate in 0(1) time.
"""
class Node:
    def __init__(self, value=None, next=None ):
        self.value = value
        self.next_value = next

    def __str__(self):
        str_value = str(self.value)
        # if self.next_value:
        #     str_value += "," + str(self.next_value)
        return str_value

class Stack:
    def __init__(self):
        self.top = None
        self.minNode = None

    def min(self):
        if not self.minNode:
            return None
        return self.minNode

    def push(self, item):
        if self.minNode and self.minNode.value < item:
            self.minNode = Node(value=self.minNode.value, next= self.minNode)
        else:
            self.minNode = Node(value=item, next= self.minNode)
        self.top = Node(value=item, next=self.top)

    def pop(self):
        if not self.top:
            return None
        self.minNode = self.minNode.next_value
        item = self.top.value
        self.top = self.top.next_value

        return item

if __name__ == '__main__':
    customStack = Stack()
    customStack.push(5)
    print("Min = ", customStack.min())
    customStack.push(6)
    print("Min = ", customStack.min())
    print(customStack.top)
    customStack.pop()
    print("Min = ", customStack.min())
    print(customStack.top)