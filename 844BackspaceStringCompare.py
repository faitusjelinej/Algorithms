class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(s):
            stack = []
            for c in s:
                if c == '#' and stack:
                    stack.pop()
                elif c != '#':
                    stack.append(c)
            return stack
        return helper(s) == helper(t)                
