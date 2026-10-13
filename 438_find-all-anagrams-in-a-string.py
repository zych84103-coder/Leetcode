# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

 
# Example 1:
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

# Example 2:
# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".


def findAnagrams(s, p) :
    rec = []
    dp = {}

    for i in p:
        dp[i] = dp.get(i,0)+1
        print (f"dp={dp}")

    n = len(p)
    ds = {}
    for j in range(len(s)):
        ds[s[j]] = ds.get(s[j],0)+1
        if j > n-1:
            c = s[j-n]
            ds[c] -= 1
            if ds[c] == 0:
                del ds[c]
        print (f"ds={ds}")
        if ds == dp:
            rec.append(j-n+1)
            print (f"rec={rec}")
    return rec

print (findAnagrams("cbaebabacd", "abc"))
print (findAnagrams("abab", "ab"))