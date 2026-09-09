from typing import List

class Solution:
    def removeElement(self, nums:List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[i], nums[k] = nums[k], nums[i]
                k += 1
        return k

s = Solution()
print (s.removeElement([3,2,2,3], 3))   #2
print (s.removeElement([0,1,2,2,3,0,4,2], 2))   #5