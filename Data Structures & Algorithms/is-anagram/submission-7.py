class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = dict()
        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1
        for char in t:
            if char in s_dict:
                s_dict[char] -= 1
                if s_dict[char] < 0:
                    return False
            else:
                return False
        return True

        
        # s_list = []
        # for char in s:
        #     s_list.append(char)
        # for x in t:
        #     if x in s_list:
        #         s_list.remove(x)
        #     else:
        #         return False
        # if not s_list:
        #     return True
        # return False
            