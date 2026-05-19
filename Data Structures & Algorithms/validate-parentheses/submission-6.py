class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return True
        pairs = {')':'(',']':'[','}':'{'}
        stk = []
        for char in s:
            if stk and char in pairs:
                if pairs[char] == stk[-1]:
                    print('pop')
                    stk.pop()
                else:
                    return False
            else:    
                print('add')
                stk.append(char)    
            print(stk)
        if not stk:
            return True
        return False