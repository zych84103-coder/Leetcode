"""二叉树本地练习工具（和 linkedlist_tools.py 同一类）。

TreeNode            节点：val、left、right
build_tree(vals)    按 LeetCode 的层序写法建树，None 表示这个位置没有节点
to_list(root)       把树变回层序列表（去掉末尾多余的 None），方便和期望值比较
check(got, expected, label)   对比并打印 ✅ / ❌
"""
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(vals):
    if not vals or vals[0] is None:
        return None
    root = TreeNode(vals[0])
    queue = deque([root])
    i = 1
    while queue and i < len(vals):
        node = queue.popleft()
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i])
            queue.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            queue.append(node.right)
        i += 1
    return root


def to_list(root):
    out = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            out.append(None)
        else:
            out.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out


def check(got, expected, label=""):
    ok = got == expected
    print(("✅" if ok else "❌"), label, "" if ok else f"got={got} expected={expected}")

root2 = build_tree([1, 2, 3, None, 4])
print(root2.val)
print(root2.left.val)

def traverse(node):
    if node is None:          # 终止条件：走到了空，没东西可读，返回
        return
    # ★ 前序：读 node.val 放这里
    traverse(node.left)
    # ★ 中序：读 node.val 放这里
    traverse(node.right)
    # ★ 后序：读 node.val 放这里
    
print(to_list(root2))
