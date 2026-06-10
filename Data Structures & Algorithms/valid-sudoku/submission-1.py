class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column_list = [set() for _ in range(len(board))]
        row_list = [set() for _ in range(len(board))]
        box_list = [set() for _ in range(len(board))]
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                colum_set = column_list[j]
                row_set = row_list[i]
                box = i//3 * 3 + j //3 
                box_set = box_list[box]
                if num in row_set or num in colum_set or num in box_set:
                    return False
                row_set.add(num)
                colum_set.add(num)
                box_set.add(num)
        return True

