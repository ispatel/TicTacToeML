from typing import Match, final
import numpy as np

#loads numpy data
data = np.load("TicTacToeData.npy",allow_pickle=True)

#deletes repreated values in data
L = {array.tobytes(): array for array in data}
data = list(L.values())

def MatchBoard(dataSet,currentBoard):
    # Searches through dataset to find boards that match the current board
    relevantValues = list()
    for i in dataSet: 
        for j in i: 
            if j.tolist() == currentBoard: 
                relevantValues.append(i)

    return relevantValues

def Enumerate(dataset,currentBoard): 
    # Assigns each free space on the board a numerical value to represent which spaces give a high 
    # probability resulting in a win and which spaces have a low probability in resulting in a win 

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

    matchList = MatchBoard(dataset,currentBoard)
    
    matchListLength = [(len(i),i) for i in matchList]

    bestMoves = []
    lowest = 9 
    for i in matchListLength: 
        if i[0] < lowest: 
            lowest = i[0]
            bestMoves = []
            bestMoves.append(i[1])
        if i[0] == lowest: 
            bestMoves.append(i[1])
    
    bestMovesFiltered = list()
    for pos,val in enumerate(bestMoves): 
        if win(bestMoves[pos][len(bestMoves[pos])-1]) == 1: 
            bestMovesFiltered.append(val)

    print(len(bestMovesFiltered[0]))
    #bestMovesFiltered = list of gameboards that will lead to quickest win 

Enumerate(data,[1,1,2,0,1,0,0,2,2])


                

# 1) DataClean -> Delete all repeated trials in data 
# 2) MatchBoard -> Function to find board in trials 
# 3) Enumerate -> Function to find proportion of wins per open spot 