from typing import List

class Solution:
    def binarysearch(self, nums, target):
        n = len(nums) - 1
        left = 0
        right = n
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return -1

s = Solution()
print (s.binarysearch([-1,0,3,5,9,12], 9))  #4
print (s.binarysearch([-1,0,3,5,9,12], 2))  #-1