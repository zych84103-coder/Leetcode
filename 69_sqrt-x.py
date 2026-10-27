# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator.
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 
# Example 1:
# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.

# Example 2:
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
def my_sqrt(x):
    left = -1
    right = x + 1
    while left + 1<right:
        mid = (left + right)//2
        if mid * mid > x:
            right = mid
        else:
            left = mid
    return left

print(my_sqrt(0))           # 0
print(my_sqrt(1))           # 1
print(my_sqrt(8))           # 2
print(my_sqrt(9))           # 3
print(my_sqrt(2147395599))  # 46339