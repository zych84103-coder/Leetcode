from typing import List

class Solution:
    def removeduplicates(self, nums):
        s = 2
        for i in range(2,len(nums)):
            if nums[i] != nums[s-2]:
                nums[i] = nums[s]
                s += 1
        return s

s = Solution()
print (s.removeduplicates([1,1,1,2,2,3])) #5