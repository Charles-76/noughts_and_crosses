class Board:

    def BoardFull(self, ActBoard):
        gamecomplete = True
        for x in range(0, 9):
            if ActBoard[x] == ' ':
                gamecomplete = False
        return gamecomplete
