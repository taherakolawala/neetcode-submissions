class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'(': ')', '[': ']', '{': '}'}
        for i in range(len(s)):
            if s[i] in brackets:
                stack.append(s[i])
                continue
            if len(stack) == 0 or s[i] != brackets[stack[-1]]:
                return False
            else:
                stack.pop()
        return not stack