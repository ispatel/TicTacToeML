import random

class Board: 
    def __init__(self) -> None:
        self.spaces_taken = [None] * 9
    
    def getSpacesTaken(self) -> list:
        #get method to get spaces taken
        return self.spaces_taken

    def full(self) -> bool: 
        #returns true if board is full and false if board is not full yet
        if None in self.spaces_taken:
            return True
        else: return False 
           
    def print_board(self) -> None:
        #prints board in a readable format instead of a  1x9 list
        spaces_taken_formatted = []

        for i in self.spaces_taken:
            if i == None:
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
            if self.spaces_taken[i] == self.spaces_taken[i+3] and self.spaces_taken[i+3] == self.spaces_taken[i+6] and self.spaces_taken[i]!=None:
                return True
        for i in range(7):
            if i==0 or i==3 or i==6:
                if self.spaces_taken[i] == self.spaces_taken[i+1] and self.spaces_taken[i+1] == self.spaces_taken[i+2] and self.spaces_taken[i]!=None:
                    return True
        if self.spaces_taken[0] == self.spaces_taken[4] and self.spaces_taken[4] == self.spaces_taken[8] and self.spaces_taken[0]!=None:
            return True
        if self.spaces_taken[2] == self.spaces_taken[4] and self.spaces_taken[4] == self.spaces_taken[6] and self.spaces_taken[2]!=None:
            return True

    def update(self,index,player) -> None:
        # updates board for turn 
        if self.spaces_taken[index] == None:
            self.spaces_taken[index] = player
        else: 
            print("That space is already taken")
        return None

    def playGame(self): 
        while self.full() == False and self.win == False: 
            self.update(random.randint(0,8),0)
            self.print_board()
