from typing import List

class solution():
    def majorityElement(self, nums: List[int]) -> int:
        #用count来控制candidate的变化
        candidate = 0
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        return candidate


#stack pop&append
#        result = []
#        for num in nums:
#            if not result or num == result[-1]:
#                result.append(num)
#            else:
#                result.pop()
#        return result[0]

s = solution()
print (s.majorityElement([3,2,3]))  #3
print (s.majorityElement([2,2,1,1,1,2,2]))  #2