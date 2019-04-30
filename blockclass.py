import pygame

board = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
class gameblock :
   
    blockstate = 0
    
    block_row = 0
    block_col = 0
    
    block_x = block_row*64
    block_y = block_col*64
    
    def setblockrow(self,row):
        self.block_row = row + 1
        self.block_x = row*64
    def getrow(self):
        return self.block_row
        
    def setblockcol(self,col):
        self.block_col = col + 1
        self.block_y = col*64
    def getcol(self):
        return self.block_col
    
  

    

for i in range(8):
    for j in range(8):
        board[i][j] = gameblock()
        
        board[i][j].setblockrow(i)
        board[i][j].setblockcol(j)
        
board[3][3].blockstate,board[4][4].blockstate = -1,-1
board[4][3].blockstate,board[3][4].blockstate = 1,1

