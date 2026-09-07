from typing import List

class Solution:
    def combination(self, candidates, target):
        result = []
        self.backtrack(candidates, target, 0, [], result)
        return result
    
    def backtrack(self, candidates, target, start, path, result):
        if sum(path) == target:
            result.append(path[:])
            return
        
        if sum(path) > target:
            return

        for i in range(start, len(candidates)):
            path.append(candidates[i])
            self.backtrack(candidates, target, i, path, result)
            path.pop()

s = Solution()
print (s.combination([2,3,6,7], 7)) #[[2,2,3], [7]]
print (s.combination([2], 1)) #[]