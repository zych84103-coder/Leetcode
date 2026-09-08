from typing import List

class Solution:
    def combination(self, nums, target):
        nums.sort()
        result = []
        self.backtrack(nums, target, 0, [], result)
        return result

    def backtrack(self, nums, target, start, path, result):
        if sum(path) == target:
            result.append(path[:])
            return

        if sum(path) > target:
            return

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            path.append(nums[i])
            self.backtrack(nums, target, i+1, path, result)
            path.pop()

s = Solution()
print (s.combination([10,1,2,7,6,1,5], 8)) 
#[[1,1,6],[1,2,5],[1,7],[2,6]]