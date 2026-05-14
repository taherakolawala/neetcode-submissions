class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = []
        for char in s:
            s_list.append(char)
        for x in t:
            if x in s_list:
                s_list.remove(x)
            else:
                return False
        if not s_list:
            return True
        return False
            