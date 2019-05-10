import pygame
import blockclass
import Game
blockimage = pygame.image.load('pad1.png')

window_width = 512
window_height = 512
colour = (255,255,255)

game = Game.Game()



def rungame():
    global gamepad
    global background,icon1,icon2
    global clock
    gamepad.blit(background,(0,0))
    crashed = False
    i = 0
    howmuch_block = 0
    gamecontinue = True

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
                    print(game.checkFlippable(clix, cliy, -1))
                    if game.gameBoard[clix][cliy] == 0 and len(game.checkFlippable(clix, cliy, -1)) > 0:
                        toFlip_player = game.place(clix, cliy, -1)
                        if len(toFlip_player) > 0:
                            howmuch_block += 1
                            for f in toFlip_player:
                                gamepad.blit(icon1,(blockclass.board[f[0]][f[1]].block_x,blockclass.board[f[0]][f[1]].block_y))
                            gamepad.blit(icon1,(blockclass.board[clix][cliy].block_x,blockclass.board[clix][cliy].block_y))

                        i = i + 1

                elif i%2 == 1 and gamecontinue : # 컴퓨터 턴

                    if game.gameBoard[clix][cliy] == 0 and len(game.checkFlippable(clix,cliy, 1)) > 0:
                        toFlip_com = game.place(clix, cliy, 1)
                        if len(toFlip_com) > 0:
                            howmuch_block += 1
                            for f in toFlip_com:
                                gamepad.blit(icon2,(blockclass.board[f[0]][f[1]].block_x,blockclass.board[f[0]][f[1]].block_y))
                            gamepad.blit(icon2,(blockclass.board[clix][cliy].block_x,blockclass.board[clix][cliy].block_y))


                        i = i + 1

                        #하우머치블록 64개이거나 곱하기0ㅇ일시 게임종료
                if (len(toFlip_player) == 0 and len(toFlip_com) == 0) or howmuch_block == 64 :
                    gamecontinew = False
                    gamepad.blit(text, text.get_rect())

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
    icon2 = pygame.image.load('icon2_2.png')

    pygame.display.set_caption('reversi')

    clock = pygame.time.Clock()

    font = pygame.font.Font("freesansbold.ttf", 40)
    text = font.render(u"안녕하세요", True, (255, 0, 0))








    rungame()

initgame()
