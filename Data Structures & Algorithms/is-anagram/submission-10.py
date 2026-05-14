from collections import defaultdict 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        anagram_dict = defaultdict(int)

        for char in s:
            anagram_dict[char] += 1
        
        for char in t:
            anagram_dict[char] -= 1
            if anagram_dict[char] < 0:
                return False

        for count in anagram_dict.values():
            if count != 0:
                return False

        return True
