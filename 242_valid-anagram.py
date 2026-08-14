from typing import List

class solution():
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = {}
        countt = {}
        for alphas in s:
            if alphas in counts:
                counts[alphas] += 1
            else:
                counts[alphas] = 1
        for alphat in t:
            if alphat in countt:
                countt[alphat] += 1
            else:
                countt[alphat] = 1
        return counts == countt
        
s = solution()
print(s.isAnagram(s="anagram", t="nagaram")) #true
print(s.isAnagram(s="rat", t="cat")) #false
