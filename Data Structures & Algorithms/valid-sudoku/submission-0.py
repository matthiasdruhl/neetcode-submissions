class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        setRow = defaultdict(set)
        setCol = defaultdict(set)
        setCorn = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in setRow[r] or board[r][c] in setCol[c] or board[r][c] in setCorn[(r//3, c//3)] :
                    return False
                setRow[r].add(board[r][c])
                setCol[c].add(board[r][c])
                setCorn[(r//3, c//3)].add(board[r][c])
        return True
                

