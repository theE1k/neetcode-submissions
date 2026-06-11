class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
    
        while matrix:
            mid = len(matrix) // 2
            if target > matrix[mid][-1]:
                matrix = matrix[mid+1:]
            elif matrix[mid][0] <= target <= matrix[mid][-1]:
                return target in matrix[mid]
            else:
                matrix = matrix[:mid]

        return False

