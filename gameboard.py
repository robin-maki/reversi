import pygame
import blockclass
import search,game
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
                pos = pygame.mouse.get_pos()
                clix = pos[0]//64
                cliy = pos[1]//64
                    
                    
                if i%2 == 0 :#사용자 턴
                    
                    if blockclass.board[clix][cliy].blockstate == 0 and len(game.checkFlippable(clix, cliy, -1)) > 0:
                        print('뒤집을수잇는거:',game.checkFlippable(clix, cliy, -1))
                        toFlip = game.place(clix, cliy, -1)
                        if len(toFlip) > 0:
                            for f in toFlip:
                                gamepad.blit(icon1,(blockclass.board[f[0]][f[1]].block_x,blockclass.board[f[0]][f[1]].block_y))
                            gamepad.blit(icon1,(blockclass.board[clix][cliy].block_x,blockclass.board[clix][cliy].block_y))
                        
                        
                        i = i + 1
                    
                    
                elif i%2 == 1 : # 컴퓨터 턴
                    
                    if blockclass.board[clix][cliy].blockstate == 0 and len(game.checkFlippable(clix,cliy, 1)) > 0:    
                        print('뒤집을수잇는거:',game.checkFlippable(clix, cliy, 1))
                        toFlip = game.place(clix, cliy, 1)
                        if len(toFlip) > 0:
                            for f in toFlip:
                                gamepad.blit(icon2,(blockclass.board[f[0]][f[1]].block_x,blockclass.board[f[0]][f[1]].block_y))
                            gamepad.blit(icon2,(blockclass.board[clix][cliy].block_x,blockclass.board[clix][cliy].block_y))
                        
                        
                        i = i + 1
                    
                print('말종류:',blockclass.board[clix][cliy].blockstate)
        
                print('i:',i,'x랑y',clix,cliy)
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
