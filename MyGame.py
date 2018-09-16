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
        
#gameDisplay.fill(0,0,0)
pygame.display.update()
time.sleep(3)

def end():
    pygame.quit()
    quit()


end()