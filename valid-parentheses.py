def is_valid(s):
    result = []
    dic = {')':'(', ']':'[', '}':'{'}
    for i in s:
        if i in '([{':
            result.append(i)
        else:
            if not result:
                return False
            if result[-1] != dic[i]:
                return False
            result.pop()
    return result == []

# 测试
print(is_valid("()"))      # True
print(is_valid("(]"))      # False
print(is_valid("([)]"))    # False
print(is_valid("{[]}"))    # True