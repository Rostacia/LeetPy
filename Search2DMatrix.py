class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) # rows
        if m == 0:
            return False
        n = len(matrix[0]) # columns

        l, r = 0, m * n - 1

        while l <= r:
            pivot_ind = (l + r)//2
            pivot_el = matrix[pivot_ind//n][pivot_ind % n]
            if pivot_el == target:
                return True
            elif pivot_el > target:
                r = pivot_ind - 1
            else:
                l = pivot_ind + 1
        return False
