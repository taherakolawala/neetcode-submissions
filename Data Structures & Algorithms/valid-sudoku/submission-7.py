class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        print('BOARD:')
        for row in board:
            print(row)
        print(' ')
        print(' ')
    
        for row in board:
            notNum = -1
            for item in row:
                if item == '.':
                    notNum += 1
            if notNum == -1:
                notNum = 0
            if len(set(row))+notNum == 9:  
                continue
            else:
                return False  
        print('passed row check')
        
        for i in range(9):
            colList = []
            notNum = -1
            for j in range(9):
                colList.append(board[j][i])
            print(colList)
            for item in colList:
                if item == '.':
                    notNum += 1
            if notNum == -1:
                notNum = 0
            if len(set(colList)) + notNum == 9:
                continue
            else:
                return False
        print('pass col check')

        for i in range(1, 8, 3):
            for j in range(1, 8, 3):

                gridList = []
                notNum = -1

                gridList.append(board[i][j]) # 1, 1
                gridList.append(board[i-1][j-1]) # 0, 0 
                gridList.append(board[i-1][j]) # 0, 1
                gridList.append(board[i-1][j+1])  # 0, 2
                gridList.append(board[i][j-1])  # 1, 0
                gridList.append(board[i][j+1])# 1, 2
                gridList.append(board[i+1][j-1])# 2, 0
                gridList.append(board[i+1][j])# 2, 1
                gridList.append(board[i+1][j+1])# 2, 2

                for item in gridList:
                    if item == '.':
                        notNum += 1
                if notNum == -1:
                    notNum = 0
                if len(set(gridList)) + notNum == 9:
                    continue
                else:
                    return False
            
        return True



        