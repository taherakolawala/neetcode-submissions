class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cd = {}
        for num in nums:
            cd[num] = cd.get(num, 0) + 1
        sortlist = sorted(cd.items(), reverse=True, key=lambda item: item[1])
        print(sortlist)
        ret_list = []
        for i in range(k):
            ret_list.append(sortlist[i][0])
        return ret_list




        
        