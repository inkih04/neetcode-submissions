class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        len_row = len(matrix)
        len_col = len(matrix[0])
        j = (len_row * len_col) - 1

        while i <= j:
            m = (i + j) // 2
            r = m // len_col
            c = m % len_col

            if target == matrix[r][c]:
                return True
            elif matrix[r][c] > target:
                j = m - 1
            else:
                i = m + 1

        
        return False

        
    



        