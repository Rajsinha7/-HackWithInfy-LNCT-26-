#                Linkedlist cycle

"""
You are given the head of a linked list.
Determine whether the linked list contains a cycle (loop).
A cycle occurs if a node’s next pointer points to any previous node in the list instead of None.
Return:
True → if cycle exists
False → if no cycle
Example:
Normal List
1 → 2 → 3 → 4 → None
Cycle List
1 → 2 → 3 → 4
        ↑   ↓
        ← ←
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def hasCycle(head):

    slow = head
    fast = head

    while fast != None and fast.next != None:

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

# create nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# connect nodes
a.next = b
b.next = c
c.next = d
d.next = b   # cycle here

print(hasCycle(a))