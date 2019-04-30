import pygame
import blockclass

def upsearch(clicked_x,clicked_y,i):
    upcount = 0
    loop_TF = 1
    while loop_TF == 1 :
        if blockclass.board[clicked_x][clicked_y-1].blockstate == pow(-1,i):
            upcount = upcount + 1
            clicked_y = clicked_y - 1
            if clicked_y == -1:
                loof_TF = 0
            
        else : 
            loop_TF = 0
            
    if blockclass.board[clicked_x][clicked_y-1].blockstate == pow(-1,i+1):
            
        return upcount
    else:
        return 0

def downsearch(clicked_x,clicked_y,i):
    downcount = 0
    loop_TF = 1
    while loop_TF == 1 :
        if blockclass.board[clicked_x][clicked_y+1].blockstate == pow(-1,i):
            downcount = downcount + 1
            clicked_y = clicked_y + 1
            if clicked_y == 8:
                loof_TF = 0
            
        else : 
            loop_TF = 0
        
    if blockclass.board[clicked_x][clicked_y+1].blockstate == pow(-1,i+1):
            
        return downcount
    else:
        return 0    
   

