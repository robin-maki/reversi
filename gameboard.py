import pygame

window_width = 512
window_height = 512
colour = (255,255,255)
blockimage = pygame.image.load('images/pad.png')

def rungame():
    global gamepad
    global clock
    
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
        gamepad.fill(colour)
        pygame.display.update()
        clock.tick(30)
    pygame.quit()

class gameblock :
    global blockimage
    block = 0
    gamepad.bilt(blockimage(x,y))
    
    
def initgame():
    global gamepad
    global clock
    
    pygame.init()
    gamepad = pygame.display.set_mode((window_width,window_height))
    
    pygame.display.set_caption('reversi')
    
    clock = pygame.time.Clock()
    rungame()
    
initgame()