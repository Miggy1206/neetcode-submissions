class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        l, r = 0, len(nums1)
        mid = (l + r) // 2
        if len(nums1) % 2:
            return nums1[mid]
        else:
            return (nums1[mid-1] + nums1[mid]) / 2
        

        