import pygame
import blockclass
import Game
blockimage = pygame.image.load('pad1.png')

window_width = 512
window_height = 576
colour = (255,255,255)
BLACK = (0,0,0)

game = Game.Game()

def make_text(text,x, y):
    font = pygame.font.Font('freesansbold.ttf', 25)
    surf = font.render(text, True, BLACK, colour)
    gamepad.blit(surf, (x,y))
    return (x,y)



def rungame():
    global gamepad
    global background,icon1,icon2,gameover #이미지
    global clock
    gamepad.blit(background,(0,0))
    crashed = False
    i = 0
    gamecontinue = True
    point_com = 2
    point_player = 2
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
                if i%2 == 0 and gamecontinue :#사용자 턴
            
                    if game.gameBoard[clix][cliy] == 0 and len(game.checkFlippable(clix, cliy, -1)) > 0:
    
                        toFlip_player = game.place(clix, cliy, -1)
                        
                        if len(toFlip_player) > 0:
                            for f in toFlip_player:
                                gamepad.blit(icon1,(blockclass.board[f[0]][f[1]].block_x,blockclass.board[f[0]][f[1]].block_y))
                            gamepad.blit(icon1,(blockclass.board[clix][cliy].block_x,blockclass.board[clix][cliy].block_y))
                            point_player = point_player + len(toFlip_player)+1
                            point_com = point_com - len(toFlip_player)
                    i = i + 1

                elif i%2 == 1 and gamecontinue : # 컴퓨터 턴

                    if game.gameBoard[clix][cliy] == 0 and len(game.checkFlippable(clix,cliy, 1)) > 0:
                        
                        toFlip_com = game.place(clix, cliy, 1)
                        if len(toFlip_com) > 0:
                            for f in toFlip_com:
                                gamepad.blit(icon2,(blockclass.board[f[0]][f[1]].block_x,blockclass.board[f[0]][f[1]].block_y))
                            gamepad.blit(icon2,(blockclass.board[clix][cliy].block_x,blockclass.board[clix][cliy].block_y))
                            point_player = point_player - len(toFlip_player)
                            point_com = point_com + len(toFlip_player)+1                    
                    
                    i = i + 1

                make_text(str(point_player),0,512)
                make_text(str(point_com),448,512)       
                       
                if len(game.getPlaceable(1))==0 and len(game.getPlaceable(-1))==0 :
                    gamepad.blit(gameover, (0,32))
                    gamecontinue = False
                    make_text('you '+str(point_player)+' vs '+' computer '+str(point_com),128, 128)
                print(len(game.getPlaceable(1)),len(game.getPlaceable(-1)))               

        pygame.display.update()
        clock.tick(30)
    pygame.quit()




def initgame():
    global gamepad
    global clock,background,icon1,icon2,gameover

    pygame.init()
    gamepad = pygame.display.set_mode((window_width,window_height))
    background = pygame.image.load('pad1.png')
    icon1 = pygame.image.load('icon1.png')
    icon2 = pygame.image.load('icon2_2.png')
    gameover = pygame.image.load('gameover.png')

    pygame.display.set_caption('reversi')

    clock = pygame.time.Clock()

   








    rungame()

initgame()
