from typing import List

class solution():
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i, num in enumerate(nums):
            n ^= i ^ num
        return n
#        O(n),O(n)
#        n = len(nums)
#        total = set(range(n+1))
#        numset = set(nums)
#        missingnumber = total - numset
#        return missingnumber.pop()

s = solution()
print (s.missingNumber([9,6,4,2,3,5,7,0,1])) #8
print (s.missingNumber([3,0,1])) #2
print (s.missingNumber([0,1])) #2