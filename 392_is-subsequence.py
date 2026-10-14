# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true

# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false
def issubsequence(s,t):
    j = 0
    k = 0
    while j < len(s) and k < len(t):
        if s[j] == t[k]:
            j += 1
        k += 1
    return j == len(s)

print (issubsequence("abc","ahbgdc"))
print (issubsequence("axc","ahbgdc"))
