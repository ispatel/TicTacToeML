
from board import TicTacToe
import numpy as np

data = np.load("TicTacToeData.npy",allow_pickle=True)

finalBoards = []

for i in range(len(data)):
    finalBoards.append(data[i][len(data[i])-1])

#a function that returns a list of all final boards that match the current board

def taken(state): 
    spaceTaken = []
    for (pos,val) in enumerate(state):
        if val == 1 or val == 0: 
            spaceTaken.append(pos)
    return spaceTaken

def match(state) -> list:
    spaceTaken = taken(state)

    temporary_list = []
    boardMatch = []

    for val in (finalBoards):
        for i in spaceTaken:
            if state[i] == val[i]:
                temporary_list.append(True)
            else:
                temporary_list.append(False)
        if False not in temporary_list:
            boardMatch.append(val)
            temporary_list = []
        temporary_list = [] 
        
    newBoardMatch = []
    newBoardMatch = [i.tolist() for i in boardMatch]
    boardMatch = newBoardMatch

    newBoardMatch = []
    for i in boardMatch:
        if i not in newBoardMatch:
            newBoardMatch.append(i)
    
    boardMatch = newBoardMatch
    return boardMatch

def finalMatchFormat(match): 
    # return a list of tuples where the first value of the tuple is the 
    # match and the second value of the tuple is how the game ended
    # example ([1,1,1,0,0,2,2,2], "1 win")
    
    def win(board):
        for i in range(3):
            if board[i] == board[i+3] and board[i+3] == board[i+6] and board[i]!=2:
                return board[i]
            for i in range(7):
                if i==0 or i==3 or i==6:
                    if board[i] == board[i+1] and board[i+1] == board[i+2] and board[i]!=2:
                        return board[i]
            if board[0] == board[4] and board[4] == board[8] and board[0]!=2:
                return board[0]
            if board[2] == board[4] and board[4] == board[6] and board[2]!=2:
                return board[2]
        return None

    newMatch = [(match[i],win(match[i])) for i in range(len(match))]
    
    return newMatch

def enumerator(state,finalmatch) -> dict:
    indexList = [0,1,2,3,4,5,6,7,8]
    takenSpaces = taken(state) 
    freeSpace = [i for i in indexList if i not in takenSpaces]

    win = tie = loss = 0
    for (pos,val) in enumerate(freeSpace):
        # win = [win + 1 for pos in finalmatch if finalmatch[1][pos] == finalmatch[2]]
        print(val,finalmatch[val][1]) 
    return win 
    
print([1, 0, 2, 0, 2, 2, 1, 2, 2])
print(match([1, 0, 2, 0, 2, 2, 1, 2, 2]))
# print(len(match([1, 0, 2, 0, 2, 2, 1, 2, 2])))

testMatch = match([1, 0, 2, 0, 2, 2, 1, 2, 2])
print(finalMatchFormat(testMatch))

testMatchFormatted = finalMatchFormat(testMatch)

print("=-==-=-=-=-=-=-=-=--=-=-=-=-==-")
enumerator([1, 0, 2, 0, 2, 2, 1, 2, 2],testMatchFormatted)
# print(enumerator([1, 0, 2, 0, 2, 2, 1, 2, 2],testMatchFormatted))
