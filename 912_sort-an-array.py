from typing import List

class solution():
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums)//2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.merge(left, right)  #每次是以最小len=1时通过merge排序成最小有序组合，所以最终是有序的

    def merge(self, left, right):
        result = []
        i = j = 0
        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

s = solution()
print(s.sortArray([5,2,3,1]))   #[1,2,3,5]
print(s.sortArray([5,1,1,2,0,0]))   #[0,0,1,1,2,5]