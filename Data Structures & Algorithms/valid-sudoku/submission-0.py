class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
            
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        boxes = [set() for _ in range(n)]
        
        # for rows.
        for i in range(n):
            for j in range(n):
                boxIndex = (i //3) * 3 + (j // 3)
                val = board[i][j]
                if val == '.':
                    continue

                if val in rows[i] or val in cols[j] or val in boxes[boxIndex]:
                    return False

                rows[i].add(val)
                cols[j].add(val)
                boxes[boxIndex].add(val)

            
        return True