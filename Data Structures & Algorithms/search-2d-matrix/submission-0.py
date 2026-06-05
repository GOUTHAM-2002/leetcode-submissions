class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        length = (len(matrix)*len(matrix[0])) - 1
        l,r = 0,length
        while l <= r:
            mid = (l + r )// 2
            rows = mid // (len(matrix[0]))
            cols = mid % (len(matrix[0]))
            if target == matrix[rows][cols]:
                return True
            elif target > matrix[rows][cols]:
                l=mid+1
            else:
                r=mid-1
        return False

        