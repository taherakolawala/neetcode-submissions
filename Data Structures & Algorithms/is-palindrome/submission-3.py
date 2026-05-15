class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = "".join(c for c in s.lower() if c.isalnum())
        # backInd = -1
        # frwdInd = 0
        # frwdstr = ""
        # backstr = ""
        # for i in range (len(s)):
        #     frwdstr += s[frwdInd]
        #     backstr += s[backInd]
        #     backInd -= 1
        #     frwdInd += 1
        # print(frwdstr)
        # print(backstr)
        # if (frwdstr == backstr):
        #     return True
        # return False

        s = "".join(c for c in s.lower() if c.isalnum())
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True