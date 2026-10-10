# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

# Example 2:
# Input: target = 4, nums = [1,4,4]
# Output: 1

# Example 3:
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0

#solution1, can't pass for time limit
def minSubArrayLen1(target, nums):
    short = 0
    n1 = len(nums)
    #先判断最大窗口时是否满足
    if sum(nums) >= target:
        short = n1
    else:
        return 0
    
    #缩小窗口移动是否满足
    n2 = n1-1
    while n2 > 0:
        for i in range(n1-n2+1):     #不满足移动，满足再缩小 
            if sum(nums[i:(n2+i)]) >= target:
                short = n2
        n2 -= 1
    return short

print (minSubArrayLen1(7, [2,3,1,2,4,3]))
print (minSubArrayLen1(4, [1,4,4]))
print (minSubArrayLen1(11, [1,1,1,1,1,1,1,1]))

#solution2
def minSubArrayLen2(target, nums):
    n = len(nums)
    best = n+1
    total = 0
    left = 0
    for right in range(n):
        total += nums[right]    #adding numbers
        while total >= target:  #reach the condition
            best = min(best, right-left+1)  #renew the best
            total -= nums[left] #remove the left one
            left += 1   #left moveforward

    if best == n+1:
        return 0
    else:
        return best

print (minSubArrayLen2(7, [2,3,1,2,4,3]))
print (minSubArrayLen2(4, [1,4,4]))
print (minSubArrayLen2(11, [1,1,1,1,1,1,1,1]))
