from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        s = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[s] = nums[s], nums[i]
                s += 1
        return nums

s = Solution()
print (s.moveZeroes([0,1,0,3,5,13]))