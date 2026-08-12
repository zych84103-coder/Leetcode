from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in nums:
            result = result ^ i
        return result

# ----- 测试区 -----
s = Solution()
print(s.singleNumber([4, 1, 2, 1, 2]))   # 应该输出 4
print(s.singleNumber([2, 2, 1]))          # 应该输出 1
print(s.singleNumber([1]))                # 应该输出 1
print(s.singleNumber([0, 0, 5]))          # 应该输出 5