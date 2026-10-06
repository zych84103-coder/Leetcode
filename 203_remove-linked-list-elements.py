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
# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Example 1:
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]

# Example 2:
# Input: head = [], val = 1
# Output: []

# Example 3:
# Input: head = [7,7,7,7], val = 7
# Output: []
def removeElements(head,val):
    dum = ListNode(0)
    dum.next = head
    cur = dum
    while cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return dum.next

print (show(removeElements(build([1,2,6,3,4,5,6]),6)))
print (show(removeElements(build([7,7,7,7]),7)))
print (show(removeElements(build([]),1)))