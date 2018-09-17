#initialisation ---------------------------------------------------
import pygame
#import time
    


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
resolution = [600,400]
gameDisplay = pygame.display.set_mode(resolution) 
pygame.display.set_caption("Game")

clock = pygame.time.Clock()

#movement
speed=5
xChange=0
yChange=0
x=0
y=0


def end():
    pygame.quit()
    pygame.joystick.quit()
    quit()


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            end()
        if event.type==pygame.JOYAXISMOTION:
            print("Joy",event)
        if event.type==pygame.JOYBUTTONDOWN:
            print("Joy button pressed",event)


    #joystick-----------------------------------
            
    joystick_count = pygame.joystick.get_count()  
    #print("count",joystick_count)
    
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        hats = joystick.get_numhats()
        for i in range(hats):
            hat=joystick.get_hat(i)
            if hat==(1,0):
                #right
                xChange=speed
            elif hat==(-1,0):
                #left
                xChange=-speed
            elif hat==(0,1):
                #up
                yChange=-speed
            elif hat==(0,-1):
                #down
                yChange=speed
            #print(hat)

    #joystick.get_axis(0)
    #if event.type == pygame.JOYBUTTONDOWN:
    #        if joystick.get_button(9)==1:
                
                
    x+=xChange
    y+=yChange
    #box
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay,black,(x,y,20,20))
    xChange=0
    yChange=0
    clock.tick(60)

    pygame.display.update()
    

end()
