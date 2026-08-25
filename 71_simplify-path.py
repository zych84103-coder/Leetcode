class Solution():
    def simplifyPath(self, path: str) -> str:
        stack = []
        parts = path.split('/')
        for part in parts:
            if part == '' or part == '.':
                continue
            elif part == '..':
                stack.pop() 
            else:
                stack.append(part)
        result = '/' + '/'.join(stack)
        return result
        
s = Solution()
print (s.simplifyPath("/.../a/../b/c/../d/./"))