class Agent:
# *******************************
# Filename: FindPossibleMove.py
# Description : Find the possilbe moves
# Date      ECR Number  Initials    Change made
# 5/10/22   ECR1        TCS         Added Header Comment
#
# *******************************
    def FindPossibleMoves(self, ActBoard):
        possiblemoves = []
        for x in range(0, 9):
            if ActBoard[x] == ' ':
                possiblemoves.append(x)
        return possiblemoves
