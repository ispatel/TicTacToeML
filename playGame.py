from Minimax import minimax
from board import TicTacToe
from random import randint
from Minimax import turn 

def playGame(RandPlayer = True):
    #Player 1 is the Ai 
    #Player 0 is the human 
    game = TicTacToe()
    print('{} went first!'.format(game.turn))
    while game.full() == False and game.win() == False: 
        if game.turn % 2 == 1: 
            game.update(turn(game.spaces_taken),1)
        elif game.turn % 1 == 0: 
            game.update(game.freeSpace()[randint(0,len(game.freeSpace())-1)],game.turn % 2)
        game.turn += 1
        game.print_board()
     
    game.print_board()

playGame(RandPlayer=True)
