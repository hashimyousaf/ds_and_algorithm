import LinkedLists.SinglyLinkedList
from LinkedLists.SinglyLinkedList import SLinkedList
singlyLinkedList = SLinkedList()

singlyLinkedList.insertSLL(10, 1)
singlyLinkedList.insertSLL(4, 1)
singlyLinkedList.insertSLL(7, 1)
singlyLinkedList.insertSLL(3, 1)
singlyLinkedList.insertSLL(2,1)

print([node.value for node in singlyLinkedList])

def partition(ll, x):
    current = ll.tail = ll.head

    while current:
        next_node = current.next
        current.next = None
        if current.value < x:
            current.next = ll.head
            ll.head = current
        else:
            ll.tail.next = current
            ll.tail = current
        current = next_node

    # Error check in case all nodes are less than x
    if ll.tail.next is not None:
        ll.tail.next = None

partition(singlyLinkedList, 3)

print([node.value for node in singlyLinkedList])
