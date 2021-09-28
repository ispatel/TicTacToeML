
from board import TicTacToe
import numpy as np
data = np.load("TicTacToeData.npy",allow_pickle=True)

finalBoards = []

for i in range(len(data)):
    finalBoards.append(data[i][len(data[i])-1])

#a function that returns a list of all final boards that match the current board

def match(state) -> list:
    spaceTaken = []
    for (pos,val) in enumerate(state):
        if val == 1 or val == 0: 
            spaceTaken.append(pos)

    my_list = []
    boardMatch = []

    for (pos,val) in enumerate(finalBoards):
        for i in spaceTaken:
            if state[i] == val[i]:
                my_list.append(True)
            else:
                my_list.append(False)
        if False not in my_list:
            boardMatch.append(val)
            my_list = []
        my_list = [] 
        
    newBoardMatch = []
    for i in boardMatch: 
        newBoardMatch.append(i.tolist())

    boardMatch = newBoardMatch

    newBoardMatch = []
    for i in boardMatch:
        if i not in newBoardMatch:
            newBoardMatch.append(i)
    
    boardMatch = newBoardMatch
    return boardMatch
    
print([1, 0, 2, 0, 2, 2, 1, 2, 2])
print(match([1, 0, 2, 0, 2, 2, 1, 2, 2]))
print(len(match([1, 0, 2, 0, 2, 2, 1, 2, 2])))
print(type(match([1, 0, 2, 0, 2, 2, 1, 2, 2])[3]))