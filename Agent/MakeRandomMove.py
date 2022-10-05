import random
# *******************************
# Filename: MakeRandomMove.py
# Description : Make a random move
# Date      ECR Number  Initials    Change made
# 5/10/22   ECR1        TCS         Added Header Comment
#
# *******************************
class Agent:
    def PossibleMoves(self, possiblemoves:list):
        movemade = random.randint(0, len(possiblemoves)-1)

        print (possiblemoves)
        print (len(possiblemoves))
        print (movemade)

        return possiblemoves[movemade]
