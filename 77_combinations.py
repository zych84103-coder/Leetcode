from typing import List

class solution():
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.backtrack(n, k, 1,[],result)
        return result

    def backtrack(self, n, k, start, path, result):
        if len(path) == k:
            result.append(path[:])
            return

        # 终止条件 2（剪枝）：剩下的全选也不够 k 个，提前结束
        if len(path) + (n - start + 1) < k:
            return
        
        path.append(start)
        self.backtrack(n, k, start+1, path,result)
        path.pop()

        self.backtrack(n, k, start+1, path,result)
    
s = solution()
print (s.combine(n = 4, k = 2)) #[[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
print (s.combine(n = 1, k = 1)) #[[1]]