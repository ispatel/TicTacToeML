from board import Board
import random 

class Game:
    def __init__(self) -> None:
        self.board = Board()
    
    def playGame(self): 
        turn = 1 #initialize turn as 2 if you want "O" to go first
        while self.board.full() == False and self.board.win() == False: 
            if turn == 0:
                turn = turn + 1
            randomIndex = random.randint(0,8)
            self.board.update(randomIndex,turn % 2)
            turn += 1

        self.board.print_board()

game1 = Game()
game1.playGame()

#Alternate Turns 
#Make it so update function witll try to update until a possible number is found 
#Print where the winning combo is 
