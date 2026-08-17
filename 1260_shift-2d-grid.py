from typing import List

class solution():
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        total = m * n

        if k == 0 or k % total == 0:
            return grid
        
        #展平
        flat = []
        for i in grid:
            for j in i:
                flat.append(j)

        #位移
        k = k % total
        shifted = flat[-k:] + flat[:-k]
        
        #合并graft
        result = []
        for k in range(0,total,n):
            result.append(shifted[k:k+n])
        return result

s = solution()
print (s.shiftGrid([[1,2,3],[4,5,6],[7,8,9]], k = 1)) #[[9,1,2],[3,4,5],[6,7,8]]
print (s.shiftGrid([[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4)) #[[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
print (s.shiftGrid([[1,2,3],[4,5,6],[7,8,9]], k = 9))   #[[1,2,3],[4,5,6],[7,8,9]]