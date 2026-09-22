from typing import List

def longestCommonPrefix(strs: List[str]):
    if strs == []:
        return ""
    shortlen = min(len(w) for w in strs)
    for i in range(shortlen):
        standard = strs[0][i]   #选标准
        for w in strs:          #每列比较
            if w[i] != standard:
                return strs[0][:i]
    return strs[0][:shortlen]   #如果i停在最后一轮i=shortlen-1，所以是shortlen

print (longestCommonPrefix(["flower","flow","flight"]))
print (longestCommonPrefix(["dog","racecar","car"]))
print (longestCommonPrefix([""]))