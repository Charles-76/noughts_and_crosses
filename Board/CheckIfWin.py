class Board:
    def CheckWin(self, ActBoard, currentPlayer):
        possibleWin =  [[0, 1, 2], [3, 4, 5], [6,7,8], [0,3,6], [1,4,7], [2,5,8]
        , [0,4,8],[2,4,6]]
        winner = False
        for x in range(0, 8):
            if ActBoard[possibleWin[x][0]] == currentPlayer and ActBoard[possibleWin[x][1]] == currentPlayer and ActBoard[possibleWin[x][2]] == currentPlayer:
                print ("We have a winner")
                winner = True
        return winner


