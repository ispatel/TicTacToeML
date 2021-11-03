
from random import randint
from numpy import array
from Minimax import turn

class TicTacToe: 
    def __init__(self) -> 2:
        self.spaces_taken = [2] * 9
        self.turn = randint(0,1)
        self.tracker = []

    def full(self) -> bool: 
        #returns true if board is full and false if board is not full yet
        return 2 not in self.spaces_taken

    def print_board(self):
        #prints board in a readable format instead of a  1x9 list
        spaces_taken_formatted = []

        for i in self.spaces_taken:
            if i == 2:
                spaces_taken_formatted.append(" ")
            if i == 0:
                spaces_taken_formatted.append("O")
            if i == 1: 
                spaces_taken_formatted.append("X")

        for i in range(0,7,3):
            print("{} | {} | {}".format(spaces_taken_formatted[i],spaces_taken_formatted[i+1],spaces_taken_formatted[i+2]))
            if i == 0 or i == 3: 
                print("---------")
        print("+++++++++++++++++")
                
    def win(self) -> bool:
        #checks for win 
        """
        need to find a 'cleaner' method to do this 
        """
        for i in range(3):
            if self.spaces_taken[i] == self.spaces_taken[i+3] and self.spaces_taken[i+3] == self.spaces_taken[i+6] and self.spaces_taken[i]!=2:
                return True
        for i in range(7):
            if i==0 or i==3 or i==6:
                if self.spaces_taken[i] == self.spaces_taken[i+1] and self.spaces_taken[i+1] == self.spaces_taken[i+2] and self.spaces_taken[i]!=2:
                    return True
        if self.spaces_taken[0] == self.spaces_taken[4] and self.spaces_taken[4] == self.spaces_taken[8] and self.spaces_taken[0]!=2:
            return True
        if self.spaces_taken[2] == self.spaces_taken[4] and self.spaces_taken[4] == self.spaces_taken[6] and self.spaces_taken[2]!=2:
            return True
        return False

    def update(self,index,player):
        # updates board for turn 
        self.spaces_taken[index] = player
        self.tracker.append(self.spaces_taken.copy()) # <- why does this work?

    def freeSpace(self):
        freeSpaces = []
        for i in range(len(self.spaces_taken)):
            if self.spaces_taken[i] == 2:
                freeSpaces.append(i)
        return freeSpaces

    def playGame(self, ai = False, print = False):
            while self.full() == False and self.win() == False:
                if ai == False: 
                    self.update(self.freeSpace()[randint(0,len(self.freeSpace())-1)],self.turn % 2)
                if ai == True: 
                    self.update(turn(self.spaces_taken),self.turn % 2)
                if print == True:
                    self.print_board()
                self.turn += 1     
            return array(self.tracker)
    


(TicTacToe().playGame(ai=True,print=True))