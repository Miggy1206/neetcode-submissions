class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        org = []
        for l in matrix:
            org.extend(l)

        left = 0
        right = len(org) - 1
        while(left <= right):
            mid = (left + right) // 2
            if org[mid] == target:
                return True
            elif org[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
        