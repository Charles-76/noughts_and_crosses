class Player:
# *******************************
# Filename: CheckMoveIsPossible.py
# Description : Check if move is possible
# Date      ECR Number  Initials    Change made
# 5/10/22   ECR1        TCS         Added Header Comment
#
# *******************************
    def CheckMoveIsPossible(self, NewPos, ActBoard):
        clearPos = ' '
        if ActBoard[NewPos] != clearPos:
            print ("You can't go there")
            GoPossible = False
        else:
            GoPossible = True
            
        return GoPossible







