#                                Reverse linkedlist

"""
You are given the head of a singly linked list.
Your task is to reverse the linked list and return the new head of the reversed list.
A singly linked list consists of nodes where each node contains a value and a pointer to the next node in the list.
You must reverse the list such that the last node becomes the first node, and every node points to the previous node instead of the next node.
Example
Input:
1 → 2 → 3 → 4 → 5
Output:
5 → 4 → 3 → 2 → 1
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def reversekist(head):

    prev = None
    curr = head

    while curr != None:

        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode

    return prev


def printList(head):

    temp = head

    while temp != None:
        print(temp.data, end=" -> ")
        temp = temp.next

    print("None")


# creating linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)


#print("Original List:")
#printList(head)

head = reversekist(head)

print("Reversed List:")
printList(head)