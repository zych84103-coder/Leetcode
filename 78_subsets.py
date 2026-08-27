from typing import List

class solution():
    def subsets(self, nums:List[int]) -> List[List[int]]:
        result = []
        self.backtrack(nums, 0, [], result)
        return result

    def backtrack(self, nums, start, path, result):
        if start == len(nums):      #回溯的停止条件（先设定）
            result.append(path[:])  #附path的复制给result
            return

        path.append(nums[start])
        self.backtrack(nums, start + 1, path, result)
        path.pop()

        self.backtrack(nums, start + 1, path, result)

s = solution()
print (s.subsets([1,2,3]))  #[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
print (s.subsets([0]))  #[[],[0]]