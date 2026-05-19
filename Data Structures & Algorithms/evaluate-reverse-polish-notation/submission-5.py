class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opset = set('+-*/')
        stk = []
        for t in tokens:
            print('stk:', stk)
            if not stk:
                stk.append(int(t))
            elif t in opset:
                b = stk.pop()
                a = stk.pop()
                if t=='+': 
                    stk.append(a+b)
                elif t=='-':
                    stk.append(a-b)
                elif t=='*':
                    stk.append(a*b)
                elif t=='/':
                    stk.append(int(a/b))
            else:
                stk.append(int(t))
        print('stk:', stk)
        return stk[-1]

