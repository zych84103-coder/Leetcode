from typing import List

class Solution:
    def squaresofsortedarray(self, nums):
        n = len(nums)
        left = 0
        right = n-1
        result = [0] * n
        for i in range(n-1, -1, -1):    #(n-1,-1)-> n-1 to 0
            if abs(nums[left]) <= abs(nums[right]):
                result[i] = nums[right] ** 2
                right -= 1
            else:
                result[i] = nums[left] ** 2
                left += 1
        return result

s = Solution()
print (s.squaresofsortedarray([-4,-1,0,3,10]))