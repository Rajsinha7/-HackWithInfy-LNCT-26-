#              Merge two sorted linkedlist
"""
You are given the heads of two singly linked lists list1 and list2.
Both linked lists are sorted in ascending order.
Your task is to merge these two lists into one sorted linked list and return the head of the merged list.
The merged list should also remain sorted.
You must rearrange the node pointers instead of creating new nodes.
Example:
Input
list1 = 1 → 3 → 5
list2 = 2 → 4 → 6
Output
1 → 2 → 3 → 4 → 5 → 6
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def mergeLists(l1,l2):

    dummy = Node(0)
    tail = dummy

    while l1 != None and l2 != None:

        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next

        tail = tail.next

    if l1 != None:
        tail.next = l1
    else:
        tail.next = l2

    return dummy.next


def printList(head):

    temp = head

    while temp != None:
        print(temp.data,end=" -> ")
        temp = temp.next

    print("None")


# creating first list
l1 = Node(1)
l1.next = Node(3)
l1.next.next = Node(5)

# creating second list
l2 = Node(2)
l2.next = Node(4)
l2.next.next = Node(6)

print("List 1:")
printList(l1)

print("List 2:")
printList(l2)

merged = mergeLists(l1,l2)

print("Merged List:")
printList(merged)