class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        row = [{} for i in range(n)]
        column = [{} for i in range(n)]
        box = [[{} for i in range(3)] for i in range(3)]

        for i in range(n):
            for j in range(n):
                val = board[i][j]

                if val == '.':
                    continue

                if val not in row[i]:
                    if val not in column[j]:
                        if val not in box[i // 3][j // 3]:
                            row[i][val] = 1
                            column[j][val] = 1
                            box[i // 3][j // 3][val] = 1
                            continue
                return False

        return True
