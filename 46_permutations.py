from typing import List

class Solution:
    def permute(self, nums:List[int]) -> List[List[int]]:
        result = []
        used = [False] * len(nums)
        self.backtrack(nums, used, [], result)
        return result

    def backtrack(self, nums, used, path, result):
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue

            used[i] = True
            path.append(nums[i])
            self.backtrack(nums, used, path, result)
            path.pop()
            used[i] = False

s = Solution()
print (s.permute([1,2,3]))    #[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print (s.permute([0,1]))      #[[0,1],[1,0]]