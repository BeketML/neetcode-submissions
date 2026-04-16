class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows_count = len(matrix)
        cols_count = len(matrix[0])

        all_elements = rows_count * cols_count

        lowest = 0
        highest = all_elements - 1

        while lowest <= highest:
            mid_index = (lowest + highest) // 2
            row = mid_index // cols_count
            col = mid_index % cols_count

            mid_value = matrix[row][col]

            if mid_value == target:
                return True
            elif mid_value < target:
                lowest = mid_index + 1
            else:
                highest = mid_index - 1

        return False
        