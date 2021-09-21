
from board import TicTacToe
import numpy as np 

data = []

for i in range(100000):
    #np.append(data,TicTacToe().playGame())
    data.append(TicTacToe().playGame())

data = np.array(data,dtype=object)

print(data)
print(type(data))
np.save('TicTacToeData',data)

