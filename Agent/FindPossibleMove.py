class Agent:
    def FindPossibleMoves(self, ActBoard):
        possiblemoves = []
        for x in range(0, 9):
            if ActBoard[x] == ' ':
                possiblemoves.append(x)
        return possiblemoves
