from typing import List

class solution():
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i = 0
        j = n - 1
        while i < j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                return [i+1,j+1]
s = solution()
print (s.twoSum([2,7,11,15], 9)) #[1,2]
print (s.twoSum([2,3,4],6)) #[1,3]
print (s.twoSum([-1,0], -1)) #[1,2]