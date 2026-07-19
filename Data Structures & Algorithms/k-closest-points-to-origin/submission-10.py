import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for coord in points:
            dist = math.sqrt(coord[0]**2 + coord[1]**2)
            print(coord, dist)
            heapq.heappush(heap, (dist, coord))
        res = []
        print(heap)
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
