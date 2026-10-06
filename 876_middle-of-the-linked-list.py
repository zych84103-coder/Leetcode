# ========== 链表模板（每道链表题都粘这一段） ==========
from __future__ import annotations

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build(arr):
    """list → 链表，返回头节点"""
    dum = ListNode()
    tail = dum
    for v in arr:
        tail.next = ListNode(v)
        tail = tail.next
    return dum.next


def show(head):
    """链表 → list，方便 print"""
    out = []
    cur = head
    while cur:
        out.append(cur.val)
        cur = cur.next
    return out
# ====================================== #
# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.


# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.

# Example 2:
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.


def middelNode1(head):
    n = 0
    cur = head
    while cur:
        cur = cur.next
        n += 1
    step = n//2

    cur = head  #reset cur
    for _ in range(step):
        cur = cur.next
    return cur

print(show(middelNode1(build([1,2,3,4,5,6]))))   # [4, 5, 6]
print(show(middelNode1(build([1,2,3,4,5]))))     # [3, 4, 5]

def middelNode2(head):
    slow = head
    fast = head
    while fast and fast.next:   #make sure in range
        slow = slow.next
        fast = fast.next.next
    return slow
print(show(middelNode2(build([1,2,3,4,5,6]))))   # [4, 5, 6]
print(show(middelNode2(build([1,2,3,4,5]))))     # [3, 4, 5]

def middelNode3(head):
    nodes = []
    cur = head
    while cur:
        nodes.append(cur)
        cur = cur.next
    return nodes[len(nodes) // 2]
print(show(middelNode3(build([1,2,3,4,5,6]))))   # [4, 5, 6]
print(show(middelNode3(build([1,2,3,4,5]))))     # [3, 4, 5]