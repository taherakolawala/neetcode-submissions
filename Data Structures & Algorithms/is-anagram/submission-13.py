class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = dict()
        for i in range(len(s)):
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1
        for i in range(len(t)):
            s_dict[t[i]] = s_dict.get(t[i], 0) - 1
            if s_dict[t[i]] < 0:
                return False
        s_List = list(s_dict.values())
        for i in range(len(s_List)):
            if s_List[i] >= 1:
                return False
        return True 