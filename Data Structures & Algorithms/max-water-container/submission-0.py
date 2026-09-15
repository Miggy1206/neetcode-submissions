class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxVol = 0
        i = 0
        j = len(heights) - 1
        while(i < j):
            width = j - i
            volume = min(heights[i], heights[j]) * width
            if volume > maxVol:
                maxVol = volume
            if heights[i] > heights[j]:
                j=j-1
            elif heights[j] > heights[i]:
                i=i+1
            else:
                i=i+1
                j=j-1
        return maxVol


        