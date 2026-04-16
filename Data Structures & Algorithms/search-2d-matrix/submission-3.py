class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        all_elements = (ROWS * COLS)
        l = 0
        r = all_elements - 1

        while l<= r:
            mid = (l + r) // 2
            row_index = mid // COLS
            col_index = mid % COLS
            mid_value = matrix[row_index][col_index]

            if mid_value == target:
                return True
            elif mid_value < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
                