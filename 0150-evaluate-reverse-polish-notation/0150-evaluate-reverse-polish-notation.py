class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators=['+', '-', '*', '/']
        stack=[]
        for i in tokens:
            if i in operators:
                second, first = stack.pop(),  stack.pop()
                if i == '+':
                    tmp=second+first
                elif i=='-':
                    tmp=first - second
                elif i == '*':
                    tmp = first * second
                else:
                    tmp = int(first/second)
                stack.append(tmp)
            else:
                stack.append(int(i))
        return stack[0]