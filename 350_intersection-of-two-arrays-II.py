from typing import List

class solution():
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        collection = {}
        for i in nums1:
            collection[i] = collection.get(i,0) + 1 #n[i] = n.get(i, 0) + 1 是字典计数的标准写法，用来统计元素出现的频率
        result = []

        for i in nums2:
            if collection.get(i,0) > 0:
                result.append(i)
                collection[i] -= 1
        return result
    
s = solution()
print (s.intersect(nums1 = [1,2,2,1], nums2 = [2,2])) #[2,2]
print (s.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4])) #[4,9]