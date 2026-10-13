# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations. 

# Example 1:
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

# Example 2:
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
def characterReplacement(s,k):
    ds = {}
    best = 0
    left = 0
    for right in range(len(s)):
        ds[s[right]] = ds.get(s[right],0) + 1
        win = right - left + 1
        most = max(ds.values())
        longest = most + k
        if win <= longest:
            best = win
        else:
            ds[s[left]] -= 1
            if ds[s[left]] == 0:
                del ds[s[left]]
            left += 1
    return best

print (characterReplacement("ABAB",2))
print (characterReplacement("AABABBA",1))
print (characterReplacement("ABAB",0))