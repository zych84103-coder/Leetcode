from typing import Optional

class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class solution():
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        cur = head
        while cur:
            vals.append(cur.val)
            cur = cur.next

        if len(vals) == 1:
            return True

        i = 0
        j = len(vals) - 1
        while i<j:
            if vals[i] != vals[j]:
                return False
            i += 1
            j -= 1
        return True

# 辅助函数：将列表转成链表
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    cur = head
    for v in values[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head

s = solution()
head = build_linked_list([1,2,2,1])
print (s.isPalindrome(head)) #True