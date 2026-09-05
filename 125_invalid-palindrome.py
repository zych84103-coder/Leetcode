class Solution:
    def isPalindrome(self, s:str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())    # 过滤出字母和数字，并统一转为小写
        start = 0
        end = len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

s = Solution()
print (s.isPalindrome("A man, a plan, a canal: Panama"))