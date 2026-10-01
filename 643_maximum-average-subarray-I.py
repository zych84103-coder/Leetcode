# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

# Example 1:
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

# Example 2:
# Input: nums = [5], k = 1
# Output: 5.00000
from typing import List

class solution():
    def findMaxAverage(self,nums: list[int], k: int):
        total = sum(nums[:k])
        best = total
        for i in range(k,len(nums)):
            total = total + nums[i] - nums[i-k]
            best = max(best, total)
        print (f"best={best}")
        return best/k
s = solution()
print (s.findMaxAverage([1,12,-5,-6,50,3],4))
print (s.findMaxAverage([5],1))
print (s.findMaxAverage([0,1,1,3,3],4))