# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.
from __future__ import annotations


# ========== 链表模板（以后每道链表题都粘这一段） ==========
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
# =========================================================


class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        l1 = list1
        l2 = list2
        dum = ListNode()
        tail = dum
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 if l1 else l2
        return dum.next


# ========== 测试 ==========
s = Solution()
print(show(s.mergeTwoLists(build([1, 2, 4]), build([1, 3, 4]))))   # 期望 [1,1,2,3,4,4]
print(show(s.mergeTwoLists(build([]),        build([]))))          # 期望 []
print(show(s.mergeTwoLists(build([]),        build([0]))))         # 期望 [0]
print(show(s.mergeTwoLists(build([5]),       build([1, 2, 3]))))   # 期望 [1,2,3,5]