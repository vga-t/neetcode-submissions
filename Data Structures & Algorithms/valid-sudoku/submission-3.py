class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict = defaultdict(set)
        column_dict = defaultdict(set)
        box_dict = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c]!=".":
                    if board[r][c] in row_dict[r] or board[r][c] in column_dict[c] or board[r][c] in box_dict[(r//3,c//3)]:
                        return False
                    row_dict[r].add(board[r][c])
                    column_dict[c].add(board[r][c])
                    box_dict[(r//3,c//3)].add(board[r][c])
        return True


        

       
            

        