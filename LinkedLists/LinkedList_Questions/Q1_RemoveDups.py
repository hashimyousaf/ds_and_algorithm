#   Created by Elshad Karimov on 17/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# Question 1 - Remove Dups : Write a code to remove duplicates from an unsorted linked list. 


from LinkedList import LinkedList

def removeDups(ll):
    if ll.head is None:
        return
    else:
        currentNode = ll.head
        visited = set([currentNode.value])
        while currentNode.next_value:
            if currentNode.next_value.value in visited:
                currentNode.next_value = currentNode.next_value.next_value
            else:
                visited.add(currentNode.next_value.value)
                currentNode = currentNode.next_value
        return ll

def removeDups1(ll):
    if ll.head is None:
        return
    
    currentNode = ll.head
    while currentNode:
        runner = currentNode
        while runner.next_value:
            if runner.next_value.value == currentNode.value:
                runner.next_value = runner.next_value.next_value
            else:
                runner = runner.next_value
        currentNode = currentNode.next_value
    return ll.head



customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
removeDups1(customLL)
print(customLL)