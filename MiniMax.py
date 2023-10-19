import numpy as np
import copy as c
from Actions import * 

nodes =0

def MiniMaxSimple(LastMove, depth, boardState, Player):
    global nodes
    nodes +=1 
    
    if WinState(boardState) or depth == 0:
        return LastMove, SimpleHeuristic(boardState), nodes
    
    if Player == 'x':
        Value = (np.inf)
        players = getListofXpieces(boardState)
        BestMove = ''
        
        for i in range(len(players)):
            movesAllowed = getPossibleMoves(boardState, Player)
            
            for moveCode in movesAllowed:
                childBoard = c.deepcopy(boardState)
                childBoard = MovePiece(childBoard, moveCode)
                Move, v, n = MiniMaxSimple(moveCode, depth-1, childBoard, 'o')
               
                
                if v < Value:
                    Value = v
                    BestMove = moveCode
        
            return BestMove, Value, nodes
    
    if Player == 'o':
        Value = -(np.inf)
        players = getListofOpieces(boardState)
        BestMove = ''
        
        for i in range(len(players)):
            movesAllowed = getPossibleMoves(boardState, Player)
            
            for moveCode in movesAllowed:
                childBoard = c.deepcopy(boardState)
                childBoard = MovePiece(childBoard, moveCode)
                Move, v, n = MiniMaxSimple(moveCode, depth-1, childBoard, 'x')
               
                
                if v > Value:
                    Value = v
                    BestMove = moveCode

            return BestMove, Value, nodes

def MiniMaxComplex(LastMove, depth, boardState, Player):
    global nodes
    nodes +=1 
    
    if WinState(boardState) or depth == 0:
        return LastMove, ComplexHeuristic(boardState), nodes
    
    if Player == 'x':
        Value = (np.inf)
        players = getListofXpieces(boardState)
        BestMove = ''
        
        movesAllowed = getPossibleMoves(boardState, Player)
        
        for moveCode in movesAllowed:
            childBoard = c.deepcopy(boardState)
            childBoard = MovePiece(childBoard, moveCode)
            Move, v, n = MiniMaxComplex(moveCode, depth-1, childBoard, 'o')
            
            
            if v < Value:
                Value = v
                BestMove = moveCode
    
        return BestMove, Value, nodes
    
    if Player == 'o':
        Value = -(np.inf)
        players = getListofOpieces(boardState)
        BestMove = ''
        
        
        movesAllowed = getPossibleMoves(boardState, Player)
        
        for moveCode in movesAllowed:
            childBoard = c.deepcopy(boardState)
            childBoard = MovePiece(childBoard, moveCode)
            Move, v, n = MiniMaxComplex(moveCode, depth-1, childBoard, 'x')
            
            
            if v > Value:
                Value = v
                BestMove = moveCode

        return BestMove, Value, nodes
