from Board import Display_Board
from Board import CheckIfWin
from Board import CheckBoardFull
from Player import CheckMoveIsPossible
from Agent import FindPossibleMove
from Agent import MakeRandomMove

###############################################################
#   Filename: Main.py
#   Descxription: 
#
#   Version:    ECR:    Updatea:
#


Disp = Display_Board.Board()
CheckWin = CheckIfWin.Board()
Full = CheckBoardFull.Board()
Check = CheckMoveIsPossible.Player()
Agent = FindPossibleMove.Agent()

MakeMove = MakeRandomMove.Agent()

actual_board = Disp.init_board()

Player = (input("Do you want to go first? Y/N"))

if Player[0] == 'N' or Player[0] == 'n': 
        possible_moves = Agent.FindPossibleMoves(actual_board)
        movemade = MakeMove.PossibleMoves(possible_moves)
        ComputerChar  = 'X'
        PlayChar = 'O'
        actual_board[movemade] = ComputerChar
else:
        ComputerChar  = 'O'
        PlayChar = 'X'

Disp.display_board(actual_board)

BoardFull = False
Winner = False

while BoardFull == False and Winner == False:

    ValidMove = False

    while ValidMove == False:

        input_b = int(input("Enter go: "))

        ValidMove = Check.CheckMoveIsPossible(input_b, actual_board)

    actual_board[input_b] = PlayChar
    Disp.display_board(actual_board)

    #Check Board Full
    BoardFull = Full.BoardFull(actual_board)
    #Check Winner
    Winner = CheckWin.CheckWin(actual_board,PlayChar)

    if Winner == False:

        possible_moves = Agent.FindPossibleMoves(actual_board)
        movemade = MakeMove.PossibleMoves(possible_moves)
        actual_board[movemade] = ComputerChar
  
        #Check Board Full
        BoardFull = Full.BoardFull(actual_board)
        #Check Winner
        Winner = CheckWin.CheckWin(actual_board,ComputerChar)

        Disp.display_board(actual_board)
