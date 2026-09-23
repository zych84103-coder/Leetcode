# Example 1:

# Input: x = 1, y = 4
# Output: 2
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# The above arrows point to positions where the corresponding bits are different.
# Example 2:

# Input: x = 3, y = 1
# Output: 1

def hamming(x,y):
    n = x^y #calculate bits differences
    ans = 0
    while n>0:
        ans += n&1 #compare binary last number, if = 1 -> 1,else 0
        n >>= 1 #move binary to right for 1 bits
    return ans

print (hamming(1,4))
print (hamming(3,1))