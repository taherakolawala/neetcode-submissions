class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c for c in s.lower() if c.isalnum())
        backInd = -1
        frwdInd = 0
        frwdstr = ""
        backstr = ""
        for i in range (len(s)):
            frwdstr += s[frwdInd]
            backstr += s[backInd]
            backInd -= 1
            frwdInd += 1
        print(frwdstr)
        print(backstr)
        if (frwdstr == backstr):
            return True
        return False