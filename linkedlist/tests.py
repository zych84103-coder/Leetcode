from __future__ import annotations

# ========== 链表模板（每道链表题都粘这一段） ==========
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


head = build([1, 2, 3])
print("起始：       ", show(head))

print("动作1")
# 动作 1 · 读
cur = head
print("cur.val ：   ", cur.val)
print("链没变：     ", show(head))

print("动作2")
# 动作 2 · 走
cur = cur.next
print("走一步后 cur.val：", cur.val)
print("链还是没变： ", show(head))
print("head 也没动： ", head.val)

# 动作 3 · 改 
print("动作3")
cur = head                      # 先回到第一个节点
cur.next = cur.next.next
print("改箭头后：   ", show(head))
print("cur 没动：   ", cur.val)