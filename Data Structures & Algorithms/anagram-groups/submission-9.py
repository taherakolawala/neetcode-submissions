from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        strsdict = defaultdict(list)

        for string in strs:
            sortstr = tuple(sorted(string))
            strsdict[sortstr].append(string)

        sol = []
        
        for strs in strsdict.values():
            sol.append(strs)        
        
        return sol
        
        
            
