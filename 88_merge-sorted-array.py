from typing import List

class Solution:
    def mergesortedarray(self, nums1, m, nums2, n):
        p1 = m-1
        p2 = n-1
        p = m+n-1
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

s = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
s.mergesortedarray(nums1, 3, [2, 5, 6], 3)
print(nums1)  # 输出 [1, 2, 2, 3, 5, 6]
