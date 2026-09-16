class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        m = {}
        res = []
        nums.sort() #Sort list

        for i in range(0,len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                add = nums[i] + nums[l] + nums[r]
                key = str(nums[i]) + "-" + str(nums[l]) + "-" + str(nums[r])
                if add == 0:
                    if key not in m:
                        res.append([nums[i],nums[l],nums[r]])
                        m[key] = True
                    l = l + 1
                    r = r - 1
                elif add < 0:
                    l = l + 1
                else:
                    r = r - 1
            
        return res
                 
        