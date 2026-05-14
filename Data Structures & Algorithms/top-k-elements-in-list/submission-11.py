class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cd = {}
        for num in nums:
            cd[num] = cd.get(num, 0) + 1
        topk = dict()
        for i in range(len(nums)):
            topk[i+1] = []
        for num in cd.keys():
            topk[cd[num]].append(num)
        print(topk)
        ret_list = []
        for i in range(len(nums), 0, -1):
            if topk[i] != []:
                ret_list.extend(topk[i])
                print(len(ret_list))
                print(ret_list)
            if len(ret_list) >= k:
                return ret_list[0:k]

        # sortlist = sorted(cd.items(), reverse=True, key=lambda item: item[1])
        # print(sortlist)
        # ret_list = []
        # for i in range(k):
        #     ret_list.append(sortlist[i][0])
        # return ret_list




        
