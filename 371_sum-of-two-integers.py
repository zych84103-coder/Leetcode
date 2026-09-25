# Given two integers a and b, return the sum of the two integers without using the operators + and -.

# Example 1:

# Input: a = 1, b = 2
# Output: 3
# Example 2:

# Input: a = 2, b = 3
# Output: 5

def getsum(a,b):
    while b:
        carry = (a & b) << 1
        a = a ^ b
        b = carry
        print (f"a = {a}, b = {b}")
    return a

print (getsum(1,2))
print (getsum(3,2))