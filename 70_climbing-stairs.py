from functools import lru_cache
class Solution:
    @lru_cache(maxsize=None)
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)

if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(10))    # 89
    print(s.climbStairs(35))    # 14930352