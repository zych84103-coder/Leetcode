from typing import List

class Solution():
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    c = a + b
                elif token == "-":
                    c = a - b
                elif token == "*":
                    c = a * b
                elif token == "/":
                    c = int(a / b)
                stack.append(c)
            else:
                stack.append(int(token))
        return stack[0]

s = Solution()
print (s.evalRPN(["2","1","+","3","*"]))    #9
print (s.evalRPN(["4","13","5","/","+"]))   #6
print (s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))    #22