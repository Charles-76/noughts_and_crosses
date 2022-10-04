import random
class Agent:
    def PossibleMoves(self, possiblemoves:list):
        movemade = random.randint(0, len(possiblemoves)-1)

        print (possiblemoves)
        print (len(possiblemoves))
        print (movemade)

        return possiblemoves[movemade]
