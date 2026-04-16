class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        low = 0
        high = (rows * cols) -1
        while low <= high:
            mid_index = (low + high) // 2
            row_index = mid_index // cols
            cols_index = mid_index % cols
            mid_result = matrix[row_index][cols_index]

            if mid_result == target:
                return True
            elif mid_result < target:
                low = mid_index + 1
            else:
                high = mid_index - 1
        
        return False

        