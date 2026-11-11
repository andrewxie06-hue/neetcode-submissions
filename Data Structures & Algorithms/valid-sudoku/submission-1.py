class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                else:
                    row = f"row {i}: {board[i][j]}"
                    col = f"col {j}: {board[i][j]}"
                    block = f"block {i//3} {j//3}: {board[i][j]}" 
                    if row in seen or col in seen or block in seen:
                        return False
                    else:
                        seen.add(row)
                        seen.add(col)
                        seen.add(block)
        return True