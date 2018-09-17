#initialisation ---------------------------------------------------
import pygame
import time
    


#pygame.font.init()
pygame.init()
    
#colour definitions -----------------------------------------------
white = (240,240,240)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
grey = (80,80,80)
    
#variables --------------------------------------------------------
resolution = [1280,720]
    
gameDisplay = pygame.display.set_mode(resolution) 
pygame.display.set_caption("Game") 

def end():
    pygame.quit()
    quit()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end()
        if event.type == pygame.KEYDOWN:
            
            print(event)
#gameDisplay.fill(0,0,0)
    pygame.display.update()



end()