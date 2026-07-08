class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def isNotAlphanumeric(c):
            minLowerRange = ord('a')
            maxLowerRange = ord('z')
            minUpperRange = ord('A')
            maxUpperRange = ord('Z')
            numMinRange = ord('0')
            numMaxRange = ord('9')
            if (minLowerRange <= ord(c) <= maxLowerRange) or (minUpperRange <= ord(c) <= maxUpperRange) or(numMinRange <= ord(c) <= numMaxRange):
                return False
            return True

        ptr1, ptr2 =  0, len(s) - 1
        s1 = ""
        s2 = ""
        while ptr1 < ptr2:
            while isNotAlphanumeric(s[ptr1]) and ptr1 < ptr2:
                print('ptr1 check: ', s[ptr1])
                ptr1 += 1
                continue
            while isNotAlphanumeric(s[ptr2]) and ptr1 < ptr2:
                print('ptr2 check ' , s[ptr2])
                ptr2 -= 1
                continue
            print('check ', s[ptr1], ' == ', s[ptr2])
            if s[ptr1].lower() != s[ptr2].lower():
                return False
            ptr1 += 1
            ptr2 -= 1
        return True

    