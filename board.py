
from random import randint

class TicTacToe: 
    def __init__(self) -> 2:
        self.spaces_taken = [2] * 9
        self.turn = randint(0,1)
        self.tracker = []
    def getState(self) -> list:
        #get method to get spaces taken
        return self.spaces_taken

    def full(self) -> bool: 
        #returns true if board is full and false if board is not full yet
        if 2 in self.spaces_taken:
            return False
        else: 
            return True 

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

    def freeSpace(self) -> list:
        freeSpaces = []
        for i in range(len(self.spaces_taken)):
            if self.spaces_taken[i] == 2:
                freeSpaces.append(i)
        return freeSpaces

    def playGame(self):
        while self.full() == False and self.win() == False:
            self.update(self.freeSpace()[randint(0,len(self.freeSpace())-1)],self.turn % 2)
            self.turn += 1  
            print(self.tracker)
            self.print_board()   

game1 = TicTacToe()
game1.playGame()
