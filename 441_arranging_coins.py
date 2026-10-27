# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.
# Given the integer n, return the number of complete rows of the staircase you will build.

# Example 1:
# Input: n = 5
# Output: 2
# Explanation: Because the 3rd row is incomplete, we return 2.

# Example 2:
# Input: n = 8
# Output: 3
# Explanation: Because the 4th row is incomplete, we return 3.
def arrange1(n):
    sumi = 0
    for i in range(n+1):
        sumi += i
        if sumi == n:
            return i
        elif sumi > n:
            return i - 1

print(arrange1(5))  #2
print(arrange1(8))  #3
print(arrange1(1))  #1
print(arrange1(2))  #1

def arrange2(n):
    left, right = 0, n+1
    while left + 1 < right:
        mid = (left+right)//2
        if mid * (mid+1)//2 > n:
            right = mid
        else:
            left = mid
    return left
print(arrange2(5))  #2
print(arrange2(8))  #3
print(arrange2(1))  #1
print(arrange2(2))  #1