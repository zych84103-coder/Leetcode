# Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.


# Example 1:

# Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16
# Explanation: The two words can be "abcw", "xtfn".

# Example 2:

# Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
# Output: 4
# Explanation: The two words can be "ab", "cd".

# Example 3:

# Input: words = ["a","aa","aaa","aaaa"]
# Output: 0
# Explanation: No such pair of words.
def maxproduct(words):
    masks = []
    for w in words:
        m = 0
        for ch in w:
            m |= 1 << (ord(ch)-ord('a'))    #turn characters into 01010...
        masks.append(m)

    best = 0
    for i in range(len(words)):
        for j in range(i+1,len(words)):
            if masks[i] & masks[j] == 0:    # =0 means no repeat character
                best = max(best, len(words[i] * len(words[j])))
    return best