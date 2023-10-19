import numpy as np
import copy as c
from Actions import * 

nodes =0

def AlphaBetaSimple(LastMove, boardState, depth, alpha, beta, Player):
    global nodes
    nodes+=1
    
    if depth == 0 or WinState(boardState):
        return LastMove, SimpleHeuristic(boardState), nodes
    #min player
    if Player == 'x':
        value = (np.inf)
        BestMove = ''
        
        movesAllowed = getPossibleMoves(boardState, Player)
        
        for moveCode in movesAllowed:
            childBoard = c.deepcopy(boardState)
            childBoard = MovePiece(childBoard, moveCode)
            move, TempVal, n = AlphaBetaSimple(moveCode, childBoard, depth-1, alpha, beta, 'o')
            if TempVal < value:
                value = TempVal
                BestMove = moveCode
            beta = min(beta, TempVal)
        return BestMove, value, nodes 

    #max player
    if Player == 'o':
        value = -(np.inf)
        BestMove = ''
        

        movesAllowed = getPossibleMoves(boardState, Player)
        
        for moveCode in movesAllowed:
            childBoard = c.deepcopy(boardState)
            childBoard = MovePiece(childBoard, moveCode)
            move, TempVal, n = AlphaBetaSimple(moveCode, childBoard, depth-1, alpha, beta, 'x')
            if TempVal > value:
                value = TempVal
                BestMove = moveCode
            alpha = max(alpha, TempVal)
            if beta <= alpha:
                break
        return BestMove, value, nodes

def AlphaBetaCOmplex(LastMove, boardState, depth, alpha, beta, Player):
    global nodes
    nodes+=1
    
    if depth == 0 or WinState(boardState):
        return LastMove, ComplexHeuristic(boardState), nodes
    #min player
    if Player == 'x':
        value = (np.inf)
        BestMove = ''
        movesAllowed = getPossibleMoves(boardState, Player)
        for moveCode in movesAllowed:
            childBoard = c.deepcopy(boardState)
            childBoard = MovePiece(childBoard, moveCode)
            move, TempVal, n = AlphaBetaCOmplex(moveCode, childBoard, depth-1, alpha, beta, 'o')
            if TempVal < value:
                value = TempVal
                BestMove = moveCode
            beta = min(beta, TempVal)
        return BestMove, value, nodes 

    #max player
    if Player == 'o':
        value = -(np.inf)
        BestMove = ''
        

        movesAllowed = getPossibleMoves(boardState, Player)
        
        for moveCode in movesAllowed:
            childBoard = c.deepcopy(boardState)
            childBoard = MovePiece(childBoard, moveCode)
            move, TempVal, n = AlphaBetaCOmplex(moveCode, childBoard, depth-1, alpha, beta, 'x')
            if TempVal > value:
                value = TempVal
                BestMove = moveCode
            alpha = max(alpha, TempVal)
            if beta <= alpha:
                break
        return BestMove, value, nodes