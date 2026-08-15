from typing import List

class solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return set(set1 & set2)
 
s = solution()
print (s.intersection(nums1=[1,2,2,1], nums2=[2,2]))    #2
print (s.intersection(nums1=[4,9,5], nums2=[9,4,9,8,4]))    #9,4