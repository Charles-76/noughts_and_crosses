class Board:
# *******************************
# Filename: CheckBoardFull.py
# Description : Checks if the board is full
# Date      ECR Number  Initials    Change made
# 5/10/22   ECR1        TCS         Added Header Comment
#
# *******************************
    def BoardFull(self, ActBoard):
        gamecomplete = True
        for x in range(0, 9):
            if ActBoard[x] == ' ':
                gamecomplete = False
        return gamecomplete
