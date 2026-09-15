class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        maxArray = 0

        counter = 0
        for i in range(0,len(nums)-1):
            if nums[i] + 1 == nums[i+1]:
                counter +=1
            elif nums[i] == nums[i+1]:
                continue
            else:
                counter = 0
            if maxArray < counter:
                maxArray = counter





        return maxArray + 1
        