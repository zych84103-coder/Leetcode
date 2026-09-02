from typing import List

class Solution:
    def maxsubarry(self, nums:List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]

        f = [0] * n
        f[0] = nums[0]
        for i in range(1, n):
            f[i] = max(nums[i], f[i-1] + nums[i])
        return max(f)

s = Solution()
print (s.maxsubarry([-2,1,-3,4,-1,2,1,-5,4])) #6
print (s.maxsubarry([1])) #1
print (s.maxsubarry([5,4,-1,7,8])) #23