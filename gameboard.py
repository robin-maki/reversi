import pygame
blockimage = pygame.image.load('pad.png')

window_width = 512
window_height = 512
colour = (255,255,255)



def rungame():
    global gamepad
    global background
    global clock
    
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
        gamepad.blit(background,(0,0))
        pygame.display.update()
        clock.tick(30)
    pygame.quit()


    
    
def initgame():
    global gamepad
    global clock,background
    
    pygame.init()
    gamepad = pygame.display.set_mode((window_width,window_height))
    background = pygame.image.load('pad1.png')
    
    pygame.display.set_caption('reversi')
    
    clock = pygame.time.Clock()
    rungame()
    
initgame()