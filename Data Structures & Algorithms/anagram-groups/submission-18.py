from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = defaultdict(list)
        for word in strs:
            signature = "".join(sorted(word))
            ret[signature] += [word]
        return list(ret.values())
