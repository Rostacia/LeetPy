class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9

        # Use hash set to record the status
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(N):
            for c in range(N):
                val = board[r][c]
                # Check if position is filled with number
                if val == ".":
                    continue
                
                # Check the row if position has a number
                if val in rows[r]:
                    return False
                rows[r].add(val)

                # Check the column
                if val in cols[c]:
                    return False
                cols[c].add(val)

                # Check the square
                sq = (r//3) * 3 + c//3
                if val in squares[sq]:
                    return False
                squares[sq].add(val)

        return True
