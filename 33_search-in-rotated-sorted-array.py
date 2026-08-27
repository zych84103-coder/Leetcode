from typing import List

class Solution():
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[right]: #先一边有序
                if nums[mid] < target <= nums[right]:    #确定在一边
                    left = mid + 1     #从这边缩小边界
                else:
                    right = mid -1     #不在这一边，跳过这边
            else:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  #从这边缩小边界
                else:
                    left = mid + 1  #不在这一边，跳过这边
        return -1

s = Solution()
print (s.search([4,5,6,7,0,1,2], 0))    #4
print (s.search([4,5,6,7,0,1,2], 3))    #-1
print (s.search([1], 0))                #-1