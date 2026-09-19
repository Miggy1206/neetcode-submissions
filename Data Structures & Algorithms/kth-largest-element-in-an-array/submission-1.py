class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        revList = [n * -1 for n in nums]
        heapq.heapify(revList)

        while (k > 1):
            heapq.heappop(revList)
            k-=1


        return heapq.heappop(revList) * -1
        