from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        result = {}
        for num in nums:
            if num in result:
                return True
            result[num] = 0
        return False
    
s = Solution()
print(s.containsDuplicate([1,2,3,1]))   #true
print(s.containsDuplicate([1,2,3,4]))  #false
print(s.containsDuplicate([1,1,1,1,3,3,4,3,2,4,2])) #true