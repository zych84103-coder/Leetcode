from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return []
        j = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        return j+1, nums[0:j+1]

#newlist
#        rmset = [nums[0]]
#        for i in range(1,len(nums)):
#            if nums[i] != nums[i-1]:
#                rmset.append(nums[i])
#        return len(rmset)

#set
#       rmset = set(nums)
#       return len(rmset)

s = Solution()
print (s.removeDuplicates([1,1,2])) #2(nums = [1,2,_])
print (s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])) #5 (nums = [0,1,2,3,4,_,_,_,_,_])