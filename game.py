
from board import Board
import random 

class Game:
    def __init__(self) -> None:
        self.board = Board()
        self.turn = 1
    
    def freeSpace(self) -> list:
        # takes in the board and returns a list of all possible spaces that are free
        # by looping through the array and finding and storing the spots in the board
        # list where the element is None
        spaces_taken = self.board.getSpacesTaken()
        freeSpaces = []
        for i in range(len(spaces_taken)):
            if spaces_taken[i] == None:
                freeSpaces.append(i)
        return freeSpaces

    def playGame(self): 
        while self.board.full() == False and self.board.win() == False: 
            # updates board with a random index that is free and decides what turn it is based weather 
            # or not turn is even or odd
            self.board.update(self.freeSpace()[random.randint(0,len(self.freeSpace())-1)],self.turn % 2)
            self.turn += 1
        self.board.print_board()

game1 = Game()
game1.playGame()

#pick a random index in freeSpace to 
#from rand index 