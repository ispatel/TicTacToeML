from numpy import inf




def turn(board): 
    bestScore = -inf
    move = 0
    for pos,val in enumerate(board): 
        if val == 2: 
            board[pos] = 1
            score = minimax(board,0,False)
            board[pos] = 2
            print(pos,score)
            if score > bestScore: 
                bestScore = score
                move = pos
    return move

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
        
def minimax(board, depth, isMaximizing): 
    scores = {
        1:1,
        0:-1,
        None:0,
    }

    full = True if 2 not in board else False
    if win(board) != None or full: 
        return scores[win(board)]
    # ai = 1 
    # non ai = 0 

    if isMaximizing: 
        bestScore = -inf
        for pos,val in enumerate(board): 
            if val == 2:
                board[pos] = 1
                score = minimax(board,depth + 1, False)
                #print(board,score)
                board[pos] = 2
                bestScore = max([score,bestScore])
        return bestScore
    else: 
        bestScore = inf
        for pos,val in enumerate(board): 
            if val == 2: 
                board[pos] = 0
                score = minimax(board,depth + 1, True)
                board[pos] = 2
                bestScore = min([score,bestScore])
        return bestScore

