# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.

# Example 1:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
def checkInclusion(s1,s2):
    d = {}
    for i in s1:
        d[i] = d.get(i,0) + 1
    print (f"d={d}")

    n = len(s1)
    win = {}
    for j in range(len(s2)):
        win[s2[j]] = win.get(s2[j],0)+1
        if j >= n:
            c = s2[j-n]
            win[c] -= 1
            if win[c] == 0:
                del win[c]
        if d == win:
            return True
        print (f"win={win}")
    return False

print (checkInclusion("ab", "eidbaooo"))
print (checkInclusion("ab", "eidboaoo"))