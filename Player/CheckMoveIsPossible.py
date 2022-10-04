class Player:
    def CheckMoveIsPossible(self, NewPos, ActBoard):
        clearPos = ' '
        if ActBoard[NewPos] != clearPos:
            print ("You can't go there")
            GoPossible = False
        else:
            GoPossible = True
            
        return GoPossible







