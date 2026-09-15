class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result =[]
        nums.sort()
        dict = {}
        for i in range(0,len(nums)-2):
            j = i + 1
            k = len(nums) - 1
            while(j < k):
                sumN = nums[i] + nums[j] + nums[k]
                if sumN > 0:
                    k=k-1
                elif (sumN < 0):
                    j=j+1
                else:
                    key = str(nums[i]) + "" + str(nums[j]) + "" + str(nums[k])
                    if key not in dict:
                        result.append([nums[i], nums[j], nums[k]])
                        dict[key] = True
                    else:
                        dict[key] = True
                    k=k-1
                    j=j+1
        return result
                



        