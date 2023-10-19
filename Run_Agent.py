from MiniMax import *
from alphaBeta import *
from gserver_sock import *
from GameStates import *
from Actions import *
import sys

ai_player = 'o'

if __name__ == "__main__":
    port = 12345
    host = '156trlinux-1.ece.mcgill.ca'
    gameID = 1
    depth = 3

    for idx in range(1, len(sys.argv)):
        if(sys.argv[idx]=='-c'):
            ai_player = sys.argv[idx+1]
        elif(sys.argv[idx]=='-p'):
            try:
                port = int(sys.argv[idx+1])
            except:
                print("Invalid port number, port number must be integer")
        elif(sys.argv[idx]=='-h'):
            host = sys.argv[idx+1]
        elif(sys.argv[idx]=='-g'):
            gameID = sys.argv[idx+1]
           
    if(
        ai_player is None or
        port is None or
        host is None or
        gameID is None
    ):
        print("Invalid or missing arguments. Usage:\n python3 agent/py -c [colour] -h [server host address] -p [port] -g [gameID]")
        exit(0)

    gserver = gserver(host, port)
    gserver.Connect(gameID, ai_player)

    current_game_env = initialState
    player_turn = 'white'
    
    # import time     # REMOVE FOR TOURNAMENT

    while not WinState(current_game_env):
        # start_time = time.time()            # REMOVE FOR TOURNAMENT
        if(player_turn == ai_player):
            action = AlphaBetaCOmplex(None, current_game_env, depth, -float('Inf'), float('Inf'), player_turn)
            gserver.Send(action[0])

        try:
            nextMove = (gserver.Receive())[0]
        except TimeoutError:
            exit(0)
            
        current_game_env = MovePiece(current_game_env, nextMove)
        if(player_turn == 'o'):
            player_turn = 'x'
        else:
            player_turn = 'o'
    print("!!!!!!!!!!!!!!!!!!!! PLAYER  "+ player_turn+ "  WINS THE GAME !!!!!!!!!!!!!!!!") 