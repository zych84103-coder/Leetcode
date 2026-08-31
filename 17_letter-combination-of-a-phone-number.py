from typing import List

class Solution():
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        result = []
        self.backtrack(digits, 0, [], phone, result)
        return result
    def backtrack(self, digits, start, path, phone, result):
        if start == len(digits):
            result.append(''.join(path))
            return

        for a in phone[digits[start]]:
            path.append(a)
            self.backtrack(digits, start+1, path, phone, result)
            path.pop()

s = Solution()
print (s.letterCombinations('23')) #["ad","ae","af","bd","be","bf","cd","ce","cf"]
print (s.letterCombinations('2')) #["a","b","c"]