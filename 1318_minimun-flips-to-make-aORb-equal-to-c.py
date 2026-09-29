# Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
# Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.

# Example 1:
# Input: a = 2, b = 6, c = 5
# Output: 3
# Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)

# Example 2:

# Input: a = 4, b = 2, c = 7
# Output: 1

# Example 3:

# Input: a = 1, b = 2, c = 3
# Output: 0
def minflips(a,b,c):
    flip = 0
    for k in range(32):
        ak = (a >> k) & 1
        bk = (b >> k) & 1
        ck = (c >> k) & 1
        if ck == 1:
            if ak == bk == 0:
                flip += 1
        else:
            flip += ak + bk     #when ck == 0, how many 1 in a or b need to add how many 1.
    return flip

print (minflips(2,6,5))
print (minflips(4,2,7))
print (minflips(1,2,3))