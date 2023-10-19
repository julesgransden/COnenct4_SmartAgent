from Actions import *
from MiniMax import *
from alphaBeta import *
from GameStates import *

Board = initialState
printBoard(Board)

while(True):
        
    
    while(True):
        moveCode = input("Enter Move Code (location + direction(N, S, W, E), + nbr of steps ):")
        newLocation = getNewLocation(moveCode)
        
        try:
            if newLocation<11 or newLocation%10 > 7 or newLocation/10.0 > 7.7:
                #check boundries
                raise ValueError("You may not play this move because it is out of bounds, pick a new move")
            elif Board[getCurrentLocationofPiece(moveCode)] in list(Board.keys()):
                 #check if piece is there is a piece at given location
                raise ValueError("You may not play this move because there is no piece at this location, try again and pick a piece of type //" +'o'+"// , pick a new move")
            elif newLocation in list(Board.keys()):
                 #check if piece is already at new location
                raise ValueError("You may not play this move because a piece is already at your final location, pick a new move")
            elif Board[getCurrentLocationofPiece(moveCode)] != 'o':
                 #check if piece is of the correct type
                raise ValueError("You may not play this move because it is not your piece, try again and pick a piece of type //" +'o'+"// , pick a new move")
            else:
                break
        except ValueError as e:
            print("Error: ", e)
            
    MovePiece(Board,moveCode)    
    printBoard(Board)   
    
    oponentMoveCode = AlphaBetaCOmplex(None,Board, 3,-np.inf,np.inf, 'x')
    print(oponentMoveCode[0])
    MovePiece(Board,oponentMoveCode[0])
    printBoard(Board)
    if WinState(Board):
        print("!!!!!!!!!!!!!!!!!!!! PLAYER 'X' WINS THE GAME !!!!!!!!!!!!!!!!")
        break
    
    # MoveCode = AlphaBetaCOmplex(None,Board, 4,-np.inf,np.inf, 'o')        
    # print(MoveCode[0])
    # MovePiece(Board,MoveCode[0])
    # printBoard(Board)
    # if WinState(Board):
    #     print("!!!!!!!!!!!!!!!!!!!! PLAYER 'O' WINS THE GAME !!!!!!!!!!!!!!!!")
    #     break


    