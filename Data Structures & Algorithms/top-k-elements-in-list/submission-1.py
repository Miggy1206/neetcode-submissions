class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        dict = {}
        for num in nums:
            if num in dict:
                dict[num]+=1
            else:
                dict[num]=1
        for i in range(0,k):
            max_v = 0
            value = 0
            for d in dict:
                if dict[d] > max_v:
                    value = d
                    max_v = dict[d]

            dict.pop(value)
            res.append(value)
        
        return res
        