class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = dict()
        for string in strs:
            count = [0]*26
            for char in string:
                index = ord(char) - ord('a')
                count[index] += 1
            key = tuple(count)
            if key in strs_dict:
                strs_dict[key].append(string)
            else:
                strs_dict[key] = [string]
        return list(strs_dict.values())


        # strs_dict = dict()
        # for i in range(0, len(strs)):
        #     signature = ''.join(sorted(strs[i]))
        #     if signature in strs_dict:
        #         strs_dict[signature].append(strs[i])
        #     else:
        #         strs_dict[signature] = [strs[i]]
        # return list(strs_dict.values())
        
        
            
