from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]

        f = [0] * n
        f[0] = nums[0]
        f[1] = max(nums[0], nums[1])

        for i in range(2,n):
            f[i] = max(f[i-1],              #不偷i
                       f[i-2] + nums[i])    #偷i
        return f[n-1]

s = Solution()
print (s.rob([1,2,3,1])) #4
print (s.rob([2,7,9,3,1])) #12
print (s.rob([2,1,1,2])) #4