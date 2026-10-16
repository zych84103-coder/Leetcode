# You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.

# You are also given an integer k, which is the desired number of consecutive black blocks.
# In one operation, you can recolor a white block such that it becomes a black block.
# Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.
 
# Example 1:
# Input: blocks = "WBBWWBBWBW", k = 7
# Output: 3
# Explanation:
# One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
# so that blocks = "BBBBBBBWBW". 
# It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
# Therefore, we return 3.

# Example 2:
# Input: blocks = "WBWBBBW", k = 2
# Output: 0
# Explanation:
# No changes need to be made, since 2 consecutive black blocks already exist.
# Therefore, we return 0.

def minrecolor(blocks, k):
    w = 0
    for i in range(k):
        if blocks[i] == 'W':
            w += 1
    best = w
    n = len(blocks)
    for j in range(k,n):
        if blocks[j] == 'W':
            w += 1
        if blocks[j-k] == 'W':
            w -= 1
        best = min(best,w)
    return best

print (minrecolor("WBBWWBBWBW",7))
print (minrecolor("WBWBBBW",2))