# ============== 1. 节点定义 ==============
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# ============== 2. list → 树的翻译机 ==============
def list_to_tree(arr, i=0):
    # 越界或当前位置是 None，就没有这个节点
    if i >= len(arr) or arr[i] is None:
        return None
    # 造一个节点
    node = TreeNode(arr[i])
    # 递归造左、右孩子
    node.left  = list_to_tree(arr, 2*i + 1)
    node.right = list_to_tree(arr, 2*i + 2)
    return node

class Solution():
    def maxPathSum(self, root) -> int:
        if root is None:
            return 0
        max_sum = [float('-inf')]
        self.max_branch_sum(root, max_sum)
        return max_sum[0]

    def max_branch_sum(self, node, max_sum):
        if node is None:
            return 0
        left_sum = self.max_branch_sum(node.left, max_sum)
        right_sum = self.max_branch_sum(node.right, max_sum)
        branch_max_sum = node.val + max(0, max(left_sum, right_sum))
        max_sum[0] = max(max_sum[0], 
                        max(branch_max_sum,
                        left_sum + node.val + right_sum))
        return branch_max_sum

# ============== 4. 测试 ==============
# 图里那 4 棵树，用 list 表示
trees = [
    [5, 4, 8],         # 树1：根5, 左4, 右8
    [5, -4, -8],       # 树2：根5, 左-4, 右-8
    [5, 4, -8],        # 树3：根5, 左4, 右-8
    [5, -4, 8],        # 树4：根5, 左-4, 右8
    [-10,9,20,None,None,15,7], #42
]

s = Solution()
for t in trees:
    root = list_to_tree(t)
    print(f"输入: {t}  →  最大路径和: {s.maxPathSum(root)}")