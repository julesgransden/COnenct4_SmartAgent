import numpy as np

#returns the list of locations of X pieces on board
def getListofXpieces(list):
    res = []
    for k,v in list.items():
        if v=='x': res.append(k)
    return res

#returns the list of locations of O pieces on board
def getListofOpieces(list):
    res = []
    for k,v in list.items():
        if v=='o': res.append(k)
    return res

#prints board 
def printBoard(board):
    updatedboard = np.full((7,7), " ")
    for k,v in board.items():
        temp = str(k)
        coordX =  int(temp[1])-1#collumn number
        coordY =  int(temp[0])-1#row number
        updatedboard[coordX,coordY] = v
    print(updatedboard)

#gets current location of piece when given a certain moveCode
def getCurrentLocationofPiece(MoveCode):
    return int(MoveCode[0:2])

#gets new location after being given move code
def getNewLocation(MoveCode):
    locationOfPiece = getCurrentLocationofPiece(MoveCode)
    direction = MoveCode[2]
    nbrSquares = int(MoveCode[3])
    if direction == "N": a=-1
    elif direction == "S": a=1
    elif direction == "E": a=10
    elif direction == "W": a=-10
    return locationOfPiece+(a*nbrSquares)

#returns the number of oponents surrounding said piece
def NumberOfOpponentPiecesSurrounding(Board, locationOfPiece, type):
        surroundingPieces = (locationOfPiece-10, locationOfPiece-10+1, locationOfPiece-10-1, locationOfPiece+10, locationOfPiece+10+1,locationOfPiece+10-1,locationOfPiece+1,locationOfPiece-1)
        if type == 'x': 
            NumberOfNearbyOponents = len(list(set(surroundingPieces)&set(getListofOpieces(Board))))
        else: 
            NumberOfNearbyOponents = len(list(set(surroundingPieces)&set(getListofXpieces(Board))))
        
        return NumberOfNearbyOponents

#returns the number of friendly pieces surrounding said piece
def NumberOfFriendlyPiecesSurrounding(Board, locationOfPiece, type):
        surroundingPieces = (locationOfPiece-10, locationOfPiece-10+1, locationOfPiece-10-1, locationOfPiece+10, locationOfPiece+10+1,locationOfPiece+10-1,locationOfPiece+1,locationOfPiece-1)
        if type == 'x': 
            NumberOfNearbyOponents = len(list(set(surroundingPieces)&set(getListofXpieces(Board))))
        else: 
            NumberOfNearbyOponents = len(list(set(surroundingPieces)&set(getListofOpieces(Board))))
        
        return NumberOfNearbyOponents
    
# returns the number of steps allowed considering oponent pieces surounding
def nbrOfStepsAllowed(boardState, locationOfPiece,type):
    nbrOfOpponentsAround = NumberOfOpponentPiecesSurrounding(boardState, locationOfPiece, type)
    if nbrOfOpponentsAround == 0:
        return [1,2,3]
    elif nbrOfOpponentsAround ==1:
        return [1,2]
    elif nbrOfOpponentsAround ==2:
        return [1]
    else:
        return [0]

#When given a player type and a board state generate a list of all possible Move Code for that type of player
def getPossibleMoves(board, type):
    #get list of pieces of a certain type on the board
    if type=="x":
        listofPieces = getListofXpieces(board)
    else:
        listofPieces = getListofOpieces(board)
    res = [] # store result in array of all possible move code for that type in the board
    #go through all pieces and generate all their possible moves
    for piece in listofPieces:
        nbrofSteps = nbrOfStepsAllowed(board, piece, type)
        directions = ['S', 'E', 'W', 'N']
        for j in directions:
            if j == "N": a=-1
            elif j == "S": a=1
            elif j == "E": a=10
            elif j == "W": a=-10
            for k in nbrofSteps:
                jumpLocation2, jumpLocation3 = None,None
                moveCode = str(piece) + j + str(k)
                newLocation = getNewLocation(moveCode)
                
                if k>1:
                    jumpLocation2 = getNewLocation(str(piece) + j + str(k-1))
                if k==3:
                    jumpLocation3 = getNewLocation(str(piece) + j + str(k-2))
                #check if in bounds
                if not(newLocation<11 or newLocation%10 > 7 or newLocation/10.0 > 7.7 or newLocation%10 ==0 ):
                    if not(newLocation in list(board.keys())): 
                        if not(jumpLocation2 in list(board.keys())) :
                            if not(jumpLocation3 in list(board.keys())) :
                                res.append(moveCode)
    return res

#Move Piece and return new Board State
def MovePiece(board, MoveCode):
    newLocation = getNewLocation(MoveCode)
    currentLocation = getCurrentLocationofPiece(MoveCode)
    #pop and replace old key with new key in dictionary, i.e.new location of piece
    piece = board.pop(currentLocation)
    board[newLocation] = piece
    return board

#returns true if any of the pieces are in win state
def WinState(board):
    #check for both x and o type of player
        pieces = getListofXpieces(board)
        for curr in pieces:
            WinPatterns = np.array([[curr-10, curr-10+1,curr+1], [curr-10, curr-10-1,curr-1], [curr+10, curr+10-1,curr-1], [curr-10, curr-10+1,curr+1]])
            for j in range(4):
                if len(list(set(WinPatterns[j])&set(getListofXpieces(board)))) == 3:
                    return True
    
        pieces = getListofOpieces(board)  
        for curr in pieces:
            WinPatterns = np.array([[curr-10, curr-10+1,curr+1], [curr-10, curr-10-1,curr-1], [curr+10, curr+10-1,curr-1], [curr-10, curr-10+1,curr+1]])
            for j in range(4):
                if len(list(set(WinPatterns[j])&set(getListofOpieces(board)))) == 3:
                    return True
        return False

#This simple heuristic will give your state +1 when you have 'o' pieces in winning state
# and -1 for any 'x' pieces surrounding each other
def SimpleHeuristic(board):
    res =0
    #for o pieces
    Opieces = getListofOpieces(board)
    for curr in Opieces:
        WinPatterns = np.array([[curr-10, curr-10+1,curr+1], [curr-10, curr-10-1,curr-1], [curr+10, curr+10-1,curr-1], [curr-10, curr-10+1,curr+1]])
        for j in range(4):
            if len(list(set(WinPatterns[j])&set(Opieces))) == 3:
                res+=1
    #for x pieces
    Xpieces = getListofXpieces(board)
    for curr in Opieces:
        WinPatterns = np.array([[curr-10, curr-10+1,curr+1], [curr-10, curr-10-1,curr-1], [curr+10, curr+10-1,curr-1], [curr-10, curr-10+1,curr+1]])
        for j in range(4):
            if len(list(set(WinPatterns[j])&set(Xpieces))) == 3:
                res-=1
    return res

#This more complex heuristic will give a score based on the number of pieces side by side....
#Also, we will be giving points if the piece is stuck because that means that it is surrounded by 3 pieces therefore not allowing
# the opponent to make a square - which is great defense :)
def ComplexHeuristic(board):
    res =0
    #for o pieces
    Xpieces = getListofXpieces(board)
    Opieces = getListofOpieces(board)
    for curr in Opieces:
        #here are the patterns that will score points
        WinPatterns = np.array([[curr-10, curr-10+1,curr+1], [curr-10, curr-10-1,curr-1], [curr+10, curr+10-1,curr-1], [curr-10, curr-10+1,curr+1]])
        DoublePattern = np.array([curr-10, curr-1, curr+10, curr+1, curr-10+1, curr-10-1, curr+10+1, curr+10-1 ])
        Triplepattern = np.array([[curr-10, curr-10+1], [curr-10, curr-10-1], [curr+10, curr+10-1], [curr+10, curr+10+1], [curr+1, curr+10+1], [curr+1, curr-10+1], [curr-1, curr+10-1], [curr-1, curr-10-1]])
        for j in range(4):
            #check if win pattern and give reward
            #       x x
            #       x x
            if len(list(set(WinPatterns[j])&set(Opieces))) == 3: res+=100000
            #check if piece is blocking an opposing win to happen
            #       x o
            #       x x
            if len(list(set(WinPatterns[j])&set(Xpieces))) == 3: res+=0
        for j in range(8):    
            #check if piece has two friendly pieces next to him
            #       x
            #       x x
            if len(list(set(Triplepattern[j])&set(Opieces))) == 2: res+=0
            #check if piece has a another friendly piece next to him
            #       x x
            elif DoublePattern[j] in Opieces == 1: res+=0
    #for x pieces
    for curr in Xpieces:
        #here are the patterns that will score points
        WinPatterns = np.array([[curr-10, curr-10+1,curr+1], [curr-10, curr-10-1,curr-1], [curr+10, curr+10-1,curr-1], [curr-10, curr-10+1,curr+1]])
        DoublePattern = np.array([curr-10, curr-1, curr+10, curr+1, curr-10+1, curr-10-1, curr+10+1, curr+10-1 ])
        Triplepattern = np.array([[curr-10, curr-10+1], [curr-10, curr-10-1], [curr+10, curr+10-1], [curr+10, curr+10+1], [curr+1, curr+10+1], [curr+1, curr-10+1], [curr-1, curr+10-1], [curr-1, curr-10-1]])
        for j in range(4):
            #check if win pattern and give reward
            #       x x
            #       x x
            if len(list(set(WinPatterns[j])&set(Xpieces))) == 3: res-=100000
            #check if piece is blocking an opposing win to happen
            #       o x
            #       o o
            elif len(list(set(WinPatterns[j])&set(Opieces))) == 3: res-=0
        for j in range(8):
            #check if piece has two friendly pieces next to him
            #       x
            #       x x
            if len(list(set(Triplepattern[j])&set(Xpieces))) == 2: res-=0
            #check if piece has a another friendly piece next to him
            #       x x
            elif DoublePattern[j] in Xpieces == 1: res-=0
    return res