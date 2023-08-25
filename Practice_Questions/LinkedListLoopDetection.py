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

def loop_detection(ll):
    loop_detector = {}
    current = ll.head
    loop_detector[id(current)] = True
    while current:
        if id(current.next) not in loop_detector:
            loop_detector[id(current.next)] = True
        else:
            return current.next
        current = current.next
    return None

ll = linkedList("A")
ll.add("B")
ll.add("C")
ll.add("D")
ll.add("E")
print([i.data for i in ll])
# Introducing loop to the linkedlist
# ll.tail.next = ll.head.next.next

loop_starting_node = loop_detection(ll)
print(loop_starting_node)
#print([i.data for i in ll])