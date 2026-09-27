# Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

# Example 1:

# Input: n = 5
# Output: true
# Explanation: The binary representation of 5 is: 101
# Example 2:

# Input: n = 7
# Output: false
# Explanation: The binary representation of 7 is: 111.
# Example 3:

# Input: n = 11
# Output: false
# Explanation: The binary representation of 11 is: 1011.
def binaryAlternatingBits(n):
    m = n.bit_length()
    for k in range(m - 1):
        a = (n>>k)&1
        b = (n>>(k+1))&1
        if a == b:
            return False
    return True

print (binaryAlternatingBits(5))
print (binaryAlternatingBits(11))
print (binaryAlternatingBits(7))