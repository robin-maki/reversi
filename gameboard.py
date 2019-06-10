import pygame
import neuralnet
import game
import time,random
import learn

blockimage = pygame.image.load('pad1.png')

window_width = 512

window_height = 576

colour = (255,255,255)

BLACK = (0,0,0)



game = game.Game()

def showcurrentscore(player,com):
    '''
    현재 점수를 출력하는 함수이다.
    '''
    global patch
    patch_s=pygame.transform.scale(patch,(70,36))
    gamepad.blit(patch_s,(22,515))
    gamepad.blit(patch_s,(470,515))
    make_text(str(player),22,515)
    make_text(str(com),470,515)
    pygame.display.update()

def showmyturn():
    '''
    플레이어의 턴임을 출력하는 함수이다.
    '''
    patch_m=pygame.transform.scale(patch,(300,36))
    gamepad.blit(patch_m,(150,515))
    make_text('It is your turn !',150, 515)
    pygame.display.update()

def showcomturn():
    '''
    컴퓨터의 턴임을 출력하는 함수이다.
    '''
    patch_m=pygame.transform.scale(patch,(300,36))
    gamepad.blit(patch_m,(150,515))
    make_text('computer turn',150, 515)
    pygame.display.update()
def make_text(text,x, y):

    '''
    게임상에 텍스트를 출력하는 함수.
    text = 출력할 텍스트
    x,y = 좌표
    '''

    backcolour = (64,42,19)
    font = pygame.font.Font('freesansbold.ttf', 25)
    surf = font.render(text, True, colour,backcolour)
    gamepad.blit(surf, (x,y))

    return (x,y)







def rungame():

    global gamepad

    global background,icon1,icon2,gameover,patch,play #이미지

    global mainbgm #소리

    global clock

    gamepad.blit(background,(0,0))

    crashed = False

    i = 0

    gamecontinue = True

    score = [2,2]

    gamepad.blit(icon1,(192,192))

    gamepad.blit(icon1,(256,256))

    gamepad.blit(icon2,(192,256))

    gamepad.blit(icon2,(256,192))

    gamepad.blit(play,(240,556))

    learn.init()
    n = learn.learningList[0]



    while not crashed:

        for event in pygame.event.get():



            if event.type == pygame.QUIT:
                '''
                창 닫을 시 게임 종료
                '''

                crashed = True

            if event.type == pygame.MOUSEBUTTONUP and gamecontinue:

                pos = pygame.mouse.get_pos()

                clix = pos[0]//64

                cliy = pos[1]//64

                if cliy>7:
                    if pos[0]>=240 and pos[0]<=272 and pos[1]>556:
                        pygame.mixer.music.stop()
                    
                    clix = 4
                    cliy = 4


        
                if (i%2==0) and game.gameBoard[clix][cliy] == 0 and len(game.checkFlippable(clix, cliy, -1)) > 0:
                    '''
                    클릭시 사용자가 놓을 곳이 있는 경우
                    돌을 놓는다.
                    '''
                    toFlip_player = game.place(clix, cliy, -1)

                    if len(toFlip_player) > 0:

                        for f in toFlip_player:

                            gamepad.blit(icon1, (f[0] * 64, f[1] * 64))
                        
                        
                        pygame.mixer.Sound.play(playerchange)

                    score[0] = score[0] + len(toFlip_player)

                    score[1] = score[1] - len(toFlip_player)+1

                    showcurrentscore(score[0],score[1])
                    i = i + 1
            
                    cb = n.predict(game,1)

                    if (gamecontinue == True) and bool(cb)==False and len(game.getPlaceable(-1))!=0 :
                        ''' 
                        사용자가 돌을 둔 후
                        컴퓨터 둘 때 없을시 메세지 출력 후
                        사용자의 턴으로 넘어감.
                        '''
                        patch_m=pygame.transform.scale(patch,(300,36))
                        gamepad.blit(patch_m,(150,515))
                        make_text("COM haven't !!",150, 515)
                        pygame.display.update()
                        time.sleep(0.5)

                        showmyturn()

                        i = i + 1

                    

                    
                    if (bool(cb) == True) and game.gameBoard[cb[0]][cb[1]] == 0 and len(game.getPlaceable(-1))!=0:
                        
                        '''
                        사용자가 돌을 둔 후
                        컴퓨터가 둘 곳이 있을 시
                        돌을 놓음.
                        '''
                        showcomturn()
                        time.sleep(random.random()+0.5)
                        toFlip_com = game.place(cb[0], cb[1], 1)
                        if len(toFlip_com) > 0:

                            
                            for f in toFlip_com:

                                gamepad.blit(icon2, (f[0] * 64, f[1] * 64))

                            pygame.mixer.Sound.play(comchange)


                        score[0] = score[0] - len(toFlip_com)+1

                        score[1] = score[1] + len(toFlip_com) 

                        showcurrentscore(score[0],score[1])

                        showmyturn()

                        i = i + 1

                        

                    
            if (gamecontinue == True) and len(game.getPlaceable(-1))==0 and len(game.getPlaceable(1))!=0:
                
                '''
                플레이어가 놓을 곳이 없고, 컴퓨터가 둘 곳이 있을 시
                메시지를 띄운 후
                컴퓨터의 턴으로 넘어감.
                '''

                patch_m=pygame.transform.scale(patch,(300,36))
                gamepad.blit(patch_m,(150,515))
                make_text('UR unavailable',150, 515)
                pygame.display.update()
                time.sleep(0.5)
                
                showcomturn() 
                cb = n.predict(game,1)
                i = i + 1

                    
                if (bool(cb) == True) and game.gameBoard[cb[0]][cb[1]] == 0:

                    time.sleep(random.random()+0.5)

                    toFlip_com = game.place(cb[0], cb[1], 1)

                    if len(toFlip_com) > 0:

                        for f in toFlip_com:

                            gamepad.blit(icon2, (f[0] * 64, f[1] * 64))

                        pygame.mixer.Sound.play(comchange)


                        score[0] = score[0] - len(toFlip_com)+1

                        score[1] = score[1] + len(toFlip_com) 

                        showcurrentscore(score[0],score[1])
                        i = i + 1
                    showmyturn()
        
             
                


        if len(game.getPlaceable(1))==0 and len(game.getPlaceable(-1))==0 : 

            '''
            두 쪽 모두 놓을 곳이 없을 시
            게임을 종료함

            '''    
            gamepad.blit(gameover, (0,32))

            gamecontinue = False

            if score[0]>score[1]:
                make_text('.        YOU WIN !        .',128, 515)
            elif score[0]<score[1]:
                make_text('.        YOU Lose TT         .',128, 515)
            else:
                make_text('.                Draw               .',128,515)



        pygame.display.update()

        clock.tick(30)

    pygame.quit()




def initgame():

    global gamepad

    global clock,background,icon1,icon2,gameover,patch,play#이미지

    global mainbgm,playerchange,comchange #소리



    pygame.init()

    gamepad = pygame.display.set_mode((window_width,window_height))
    
    background = pygame.image.load('pad1.png')
    icon1 = pygame.image.load('icon1.png')
    icon2 = pygame.image.load('icon2_2.png')
    gameover = pygame.image.load('gameover.png')
    patch = pygame.image.load('patch.png')
    play = pygame.image.load('play.png')

    playerchange = pygame.mixer.Sound('playerchange.wav')
    comchange = pygame.mixer.Sound('comchange.wav')
    mainbgm = pygame.mixer.music.load('mainbgm.mp3')

    pygame.mixer.music.play(-1)

    pygame.display.set_caption('reversi')

    clock = pygame.time.Clock()

    rungame()



initgame()