class Node:
    def __init__(self, data=""):
        self.data: str = data
        self.next = None

    def __str__(self):
        return str(self.data)

class LinkedList:

    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

    def __str__(self):
        values = [str(i.data) for i in self]
        return '-->'.join(values)

    def __iter__(self):
        temp_node = self.head

        while temp_node is not None:
            yield temp_node
            temp_node = temp_node.next

    def __len__(self):
        length = 0
        node = self.head
        while node:
            length += 1
            node = node.next
        return length

    def get_node_at_location(self, n):
        temp_node = self.head
        index = 0

        while temp_node.next is not None and index != n:
            temp_node = temp_node.next
            index += 1
        if index != n:
            return "Locaiton does not exist"
        else:
            return temp_node

    def add_node(self, data):
        new_node = Node(data)
        new_node.next = None

        if self.head is None: # means it's first node in the list
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def print_linked_list(self):
        temp_node = self.head

        while temp_node is not None:
            print(temp_node.data)
            temp_node = temp_node.next

    def search_data(self, data):
        if self.head is None:
            print("Singly linked list is empty")
        else:
            index = 0
            temp_node = self.head
            while temp_node is not None:
                if temp_node.data == data:
                    return "{} found at index {}".format(temp_node.data, index)
                index += 1
                temp_node = temp_node.next
            return "Value not found in linked list"

    def delete_node_at(self, index):
        if self.head is not None: # Mean it's not empty
            if index == 0:
                if self.head.next is None:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            else:
                node = self.get_node_at_location(index-1)
                if node.next.next is None:
                    node.next = node.next.next
                    self.tail = node
                else:
                    node.next = node.next.next
        else:
            return "No element in the linklist"

# ll = LinkedList()
# ll.add_node("one")
# ll.add_node("two")
# ll.add_node("three")
# ll.add_node(417)
# ll.add_node(233.435)
# #ll.print_linked_list()
# print(f'Location :: {ll.get_node_at_location(1)}')
# print([i.data for i in ll])
# print(ll.search_data(417))
# ll.delete_node_at(4)
# print([i.data for i in ll])
# print(ll.tail.data)
