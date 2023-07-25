import numpy as np
n=20
k=
row_initial=
colunm_initial=
board=np.zeros([n,n])
temp=np.zeros([n,n])

board[row_initial,colunm_initial]=1
for i in range(0,n):
  for j in range(0,n):
      if board[i,j]>0:
        for 
          temp[i+,j+]=board[i+,j+]+board[i,j]

print(board)
