class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        res = []

        heapS = []

        for x, y in points:
            calc = (x ** 2) + (y ** 2)
            heapS.append([calc,x,y])
        heapq.heapify(heapS)

        while k > 0:
            dist, x, y = heapq.heappop(heapS)
            res.append([x,y])
            k-=1
        
        return res
        