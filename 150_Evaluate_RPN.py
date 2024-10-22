class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == '+':
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second) + int(first))
            elif t == '*':
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second) * int(first))    
            elif t == '/':
                first = stack.pop()
                second = stack.pop()
                stack.append(int(int(second) / int(first)))  
            elif t == '-':
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second) - int(first))
            else:
                stack.append(int(t))
        return stack[0]                                          
