"""
LeetCode 链表 · 本地测试工具
================================
用法：
  1. 把这个文件放进 ~/projects/leetcodepython/linkedlist/
  2. 把 LeetCode 上的 Solution 类粘到下面「你的解法」区域（替换掉示例那个）
  3. 在最下面「测试」区域写几行 check(...)
  4. 直接运行这个文件
"""

from typing import Optional, List


# ============================================================
# 节点定义（和 LeetCode 给的一模一样，不要改）
# ============================================================
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ============================================================
# 造链 / 看链
# ============================================================
def build(vals):
    """list → 链表。build([1,2,3]) 返回 head"""
    dum = ListNode()
    tail = dum
    for v in vals:
        tail.next = ListNode(v)
        tail = tail.next
    return dum.next


def show(head, limit=100):
    """链表 → list，方便 print。
    有环时最多打 limit 个就停，不会卡死。"""
    out = []
    cur = head
    while cur and len(out) < limit:
        out.append(cur.val)
        cur = cur.next
    if cur:
        out.append("...(超过 %d 个，可能有环)" % limit)
    return out


def build_cycle(vals, pos):
    """按 LC 141 / 142 的输入格式造链。
    pos = 尾巴要接回第几个节点（从 0 数起）；pos = -1 表示无环。
    注意：pos 不是你解法的参数，只是 LeetCode 描述测试用例的方式。"""
    head = build(vals)
    if head is None or pos == -1:
        return head

    entry = head                    # 走 pos 步，找到环的入口
    for _ in range(pos):
        entry = entry.next

    tail = head                     # 走到最后一个节点
    while tail.next:
        tail = tail.next

    tail.next = entry               # 尾巴接回入口，环成形
    return head


# ============================================================
# 小测试框架
# ============================================================
def check(got, expected, label=""):
    mark = "✅" if got == expected else "❌"
    print(f"{mark} {label:32} 得到 {got}   期望 {expected}")


# ============================================================
# 你的解法：把 LeetCode 的 Solution 粘到这里
# ============================================================
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False


# ============================================================
# 测试
# ============================================================
if __name__ == "__main__":
    s = Solution()

    # ---- 返回 True / False 的题：直接比 ----
    check(s.hasCycle(build_cycle([3, 2, 0, -4], 1)), True,  "141 [3,2,0,-4] pos=1")
    check(s.hasCycle(build_cycle([1, 2], 0)),        True,  "141 [1,2] pos=0")
    check(s.hasCycle(build_cycle([1, 2], -1)),       False, "141 [1,2] 无环")
    check(s.hasCycle(build_cycle([1], -1)),          False, "141 [1] 无环")
    check(s.hasCycle(build_cycle([], -1)),           False, "141 [] 空链表")
    check(s.hasCycle(build_cycle([1], 0)),           True,  "141 [1] 自己指自己")

    # ---- 返回节点的题：外面包一层 show ----
    # check(show(s.middleNode(build([1,2,3,4,5]))),      [3,4,5], "876 [1,2,3,4,5]")
    # check(show(s.deleteDuplicates(build([1,1,2]))),    [1,2],   "83  [1,1,2]")
    # check(show(s.removeElements(build([7,7,7,7]), 7)), [],      "203 [7,7,7,7] val=7")

    # ---- 返回数字的题：直接比 ----
    # check(s.getDecimalValue(build([1,0,1])), 5, "1290 [1,0,1]")