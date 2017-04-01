class Solution(object):
    def countBattleships(self, board):
        count = 0;
        i = 0
        j = 0

        if(len(board) == 1):
            while(j<len(board[i])):
                if(board[i][j] == 'X'):
                    count = count + 1
                    if ((j+1) < len(board[i]) and board[i][j + 1] == 'X'):
                        j = j + 1
                        while (j + 1 < len(board[i]) and board[i][j + 1] == 'X'):
                            j = j + 1
                j += 1

        else:
            while( i < len(board)):
                j = 0
                while(j < len(board[i])):
                    if(board[i][j] == 'X'):
                        if ((j+1) < len(board[i]) and board[i][j + 1] == 'X'):
                            j = j + 1
                            while (j + 1 < len(board[i]) and board[i][j + 1] == 'X'):
                                j = j + 1
                            count = count + 1
                        elif( i - 1 < 0 or board[i - 1][j] != 'X'):
                            count += 1
                    j += 1
                i += 1

        return count

s = Solution()
print(s.countBattleships(["..","XX"]))
