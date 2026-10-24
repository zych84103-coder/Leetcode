# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# # Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]
def searchrange(nums,target):
    result = 0
    left = -1
    right = len(nums)
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid
    first = right

    if right == len(nums) or nums[right] != target:
        return [-1,-1]
    
    left = -1
    right = len(nums)
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid
        else:
            left = mid
    last = left
    return [first,last]

print(searchrange([5,7,7,8,8,10],8))
print(searchrange([5,7,7,8,8,10],6))
print(searchrange([],0))
