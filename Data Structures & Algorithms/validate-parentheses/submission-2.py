class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return False
        pairs = {')':'(',']':'[','}':'{'}
        stk = []
        for char in s:
            if stk and char in pairs and pairs[char] == stk[-1]:
                print('pop')
                stk.pop()
            else:    
                print('add')
                stk.append(char)    
            print(stk)
        if not stk:
            return True
        return False