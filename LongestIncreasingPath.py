class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # bfs checking if cell is in bounds and neighbouring cell(s) are greater in value.
        # if neighbouring cell qualifies add 1 to dfs of that cell and check if this is the new maxlength 
        # , then memoize the maxlength to that neighbouring cell.
        # Var: - memo for all cells in grid to save maxlength up to each cell
        #      - list of directions
        #      - no. of rows and cols
        #      - maxPath for final result

        # check if input empty
        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        memo = [[0] * cols for _ in range(rows)]
        maxPath = 0

        def dfs(row, col):
            if memo[row][col] != 0:
                return memo[row][col]

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            maxLen = 1

            for dr, dc in directions:
                neiR, neiC = row + dr, col + dc
                if (0 <= neiR < rows and 0 <= neiC < cols and
                    matrix[neiR][neiC] > matrix[row][col]):
                    maxLen = max(maxLen, 1 + dfs(neiR, neiC))
            
            memo[row][col] = maxLen
            return maxLen
        
        for row in range(rows):
            for col in range(cols):
                maxPath = max(maxPath, dfs(row, col))

        return maxPath
