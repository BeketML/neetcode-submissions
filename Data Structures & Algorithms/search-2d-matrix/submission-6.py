class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix) # 4
        COLS = len(matrix[0]) # 3
        ALL_VALUES = ROWS * COLS # 12

        l = 0
        r = ALL_VALUES - 1 # 11

        while l <= r:
            mid = (l + r) // 2 # 5
            row_index = mid // COLS # 1
            col_index = mid % COLS # 2

            if matrix[row_index][col_index] == target:
                return True
            elif matrix[row_index][col_index] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False

        