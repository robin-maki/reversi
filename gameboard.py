import pygame
import blockclass
import search
blockimage = pygame.image.load('pad.png')

window_width = 512
window_height = 512
colour = (255,255,255)



def rungame():
    global gamepad
    global background,icon1,icon2
    global clock
    gamepad.blit(background,(0,0))
    crashed = False
    i = 0
    
    gamepad.blit(icon1,(192,192))
    gamepad.blit(icon1,(256,256))
    gamepad.blit(icon2,(192,256))
    gamepad.blit(icon2,(256,192))
    
    while not crashed:
        for event in pygame.event.get():
    
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.MOUSEBUTTONUP:
        
                if i%2 == 0 :
                    pos = pygame.mouse.get_pos()
                    clicked_x = pos[0]//64
                    clicked_y = pos[1]//64
                    count_up = search.upsearch(clicked_x,clicked_y,i)
                    count_down = search.downsearch(clicked_x,clicked_y,i)
            
                    #print('잇는지',blockclass.board[clicked_x][clicked_y].blockstate == 0)
                    #print('갯수',count_up)
                    print('상태',blockclass.board[clicked_x][clicked_y].blockstate)
                    print('칸수',clicked_x,clicked_y)
                    
                    if (bool(count_up) == True or bool(count_down)== True) and blockclass.board[clicked_x][clicked_y].blockstate == 0 :
                        pos_x = blockclass.board[clicked_x][clicked_y].block_x
                        pos_y = blockclass.board[clicked_x][clicked_y].block_y
                        gamepad.blit(icon1,(pos_x,pos_y))
                        
                        if bool(count_up) == True :    
                            blockclass.board[clicked_x][clicked_y].blockstate = -1
                            for i in range(count_up):
                                blockclass.board[clicked_x][clicked_y-(i+1)].blockstate = -1
                                gamepad.blit(icon1,(blockclass.board[clicked_x][clicked_y-(i+1)].block_x,
                                                blockclass.board[clicked_x][clicked_y-(i+1)].block_y))
                        if bool(count_down) == True : 
                            print(count_down)
                            blockclass.board[clicked_x][clicked_y].blockstate = -1
                            for i in range(count_down):
                                blockclass.board[clicked_x][clicked_y+(i+1)].blockstate = -1
                                gamepad.blit(icon1,(blockclass.board[clicked_x][clicked_y+(i+1)].block_x,
                                                blockclass.board[clicked_x][clicked_y+(i+1)].block_y))
                            
                        i = i + 1
                    
                    else :
                        print('byungshin')
                elif i%2 == 1 :
                    pos = pygame.mouse.get_pos()
                    clicked_x = pos[0]//64
                    clicked_y = pos[1]//64
                    if blockclass.board[clicked_x][clicked_y].blockstate == 0 :
                        pos_x = blockclass.board[clicked_x][clicked_y].block_x
                        pos_y = blockclass.board[clicked_x][clicked_y].block_y
                        gamepad.blit(icon2,(pos_x,pos_y))
                        blockclass.board[clicked_x][clicked_y].blockstate = 1
                        i = i + 1
                    else :
                        print('byungshin')
        
        pygame.display.update()
        clock.tick(30)
    pygame.quit()


    
    
def initgame():
    global gamepad
    global clock,background,icon1,icon2
    
    pygame.init()
    gamepad = pygame.display.set_mode((window_width,window_height))
    background = pygame.image.load('pad1.png')
    icon1 = pygame.image.load('icon1.png')
    icon2 = pygame.image.load('icon2.png')
    
    pygame.display.set_caption('reversi')
    
    clock = pygame.time.Clock()
    
    
    
    rungame()
    
initgame()