# Given an integer n, return true if it is a power of four. Otherwise, return false.
# An integer n is a power of four, if there exists an integer x such that n == 4x.

# Example 1:

# Input: n = 16
# Output: true
# Example 2:

# Input: n = 5
# Output: false
# Example 3:

# Input: n = 1
# Output: true
def ispowerofFourA(n):
    m = n.bit_length()
    return n > 0 and  n&(n-1) == 0 and m & 1 == 1

print (ispowerofFourA(16))
print (ispowerofFourA(1))
print (ispowerofFourA(5))