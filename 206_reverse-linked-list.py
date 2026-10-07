# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
# Input: head = [1,2]
# Output: [2,1]

# Example 3:
# Input: head = []
# Output: []
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
def reverselinkedlist(head):
    cur = head
    prev = None
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev
print (show(reverselinkedlist(build([1,2,6,3,4,5,6]))))