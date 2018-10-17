#initialisation ---------------------------------------------------
import pygame
#import time
    
#settings file read ------------------------------
config = open("Settings.txt","r")
settings=config.read().split("z")
config.close()

res=settings[0].split("x")
resolution = []
for nums in res:
    resolution.append(int(nums))


gameDisplay = pygame.display.set_mode(resolution)

if settings[2]=="1":
    pygame.display.toggle_fullscreen()
    

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


pygame.display.set_caption("Game")

clock = pygame.time.Clock()

#movement
speed=6
xChange=0
yChange=0








class sprite():
    registry=[]
    
    def __init__(self,x,y,size,sType,colour):
        self.registry.append(self)
        self.x=x
        self.y=y
        self.size=size
        self.sType=sType
        self.colour=colour
        if self.sType!="Map":  
            self.xChange=0
            self.yChange=0
            self.timeLeave=0
        
    def kill(self):
        del self


size=[int(resolution[0]/24.7),int(resolution[1]/9.36)]

player=sprite(20,20,[size[0],size[1]],"Player",blue)
enemy1=sprite(320,200,[size[0],size[1]],"Enemy",red)
enemy2=sprite(600,200,[size[0],size[1]],"Enemy",red)
enemy3=sprite(300,200,[size[0],size[1]],"Enemy",red)
enemy4=sprite(100,100,[size[0],size[1]],"Enemy",red)
map1=sprite(0,(resolution[1]-resolution[1]/48.6),[resolution[0],resolution[1]/40],"Map",black)
map2=sprite(400,100,[100,20],"Map",black)
map3=sprite(200,260,[200,150],"Map",black)



def end():
    pygame.quit()
    pygame.joystick.quit()
    quit()
    

#collision with sprites --------------------------------------------------------
def spriteColide():
    cols=[]
    for n in range(len(sprite.registry)):
        for m in range(len(sprite.registry)):
            if n!=m:
                if sprite.registry[n].x+sprite.registry[n].size[0] >= sprite.registry[m].x and sprite.registry[n].x<=sprite.registry[m].x+sprite.registry[m].size[0] and \
                sprite.registry[n].y+sprite.registry[n].size[1]>=sprite.registry[m].y and sprite.registry[n].y<=sprite.registry[m].y+sprite.registry[m].size[1]:
                    col=n,m
                    cols.append(col)
    #print(cols)
    return cols

while True:
    def up():
        player.yChange=-speed
        return
    def down():
        player.yChange=speed
        return
    def left():
        player.xChange=-speed
        return
    def right():
        player.xChange=speed
        return
    
    
    keys=pygame.key.get_pressed()   
    if keys[119]==True or keys[32]==True:
        up()
    if keys[115]==True:
        down()
    if keys[97]==True:
        left()
    if keys[100]==True:
        right()
        
        
    for event in pygame.event.get():
        keys=pygame.key.get_pressed()
        if event.type==pygame.QUIT:
            end()
        if event.type==pygame.KEYDOWN:
            #print(event.key)
            if event.key==292:
                pygame.display.toggle_fullscreen()
            if event.key==119 or event.key==32:#w
                up()
            if event.key==115:#s
                down()
            if event.key==97:#a
                left()
            if event.key==100:#d
                right()
        if event.type==pygame.KEYUP:
            if event.key==119 or event.key==32:#w
                if player.yChange==-speed:
                    player.yChange=0
            if event.key==115:#s
                if player.yChange==speed:
                    player.yChange=0
            if event.key==97:#a
                if player.xChange==-speed:
                    player.xChange=0
            if event.key==100:#d
                if player.xChange==speed:
                    player.xChange=0
                
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
            elif hat==(0,0):
                yChange=0
                xChange=0
            #print(hat)

    #joystick.get_axis(0)
    #if event.type == pygame.JOYBUTTONDOWN:
    #        if joystick.get_button(9)==1:
    
    """
    #gravity--------------------------------------------------
    if player.timeLeave==0:
        if player.y<resolution[1]-player.size[1]:
            player.timeLeave=pygame.time.get_ticks()/1000
            print(player.timeLeave)
    elif player.y==resolution[1]-player.size[1]:
        player.timeLeave=0
    
    
    time=pygame.time.get_ticks()/1000
    if player.yChange==0:
        timeStart=pygame.time.get_ticks()/1000
        player.yChange=player.yChange+1
    elif player.yChange>0:
        player.yChange=player.yChange+128*(time-timeStart)**1.8
    """
    
    colisions=spriteColide()
    
    
    if colisions!=[]:
        for n in range(len(colisions)):
            colision=colisions[n]
        
            #print(colision)
            #sprites[colision[1]].colour=red
            spriteA=sprite.registry[int(colision[0])]
            spriteB=sprite.registry[int(colision[1])]
            """
            if spriteA.sType=="Map":
                if spriteB.yChange>0 and (spriteB.y+spriteB.size[1])==spriteA.y:
                    spriteB.yChange=0
                    spriteB.y=spriteA.y-(spriteB.size[1])
                #elif sprite.registry[colB].yChange<0:
                #    sprite.regisrty[]"""
            
            if spriteB.sType=="Map" and spriteA.sType!="Map":
                if spriteA.yChange>=0 and spriteA.y<spriteB.y and (spriteA.y+spriteA.size[1])>=spriteB.y and (spriteA.y+spriteA.size[1])<=(spriteB.y+spriteB.size[1]):
                    print("ya")
                    spriteA.timeLeave=0
                    spriteA.yChange=0
                    spriteA.y=spriteB.y-(spriteA.size[1])
                if spriteA.yChange<=0 and spriteA.y>spriteB.y and spriteA.y+spriteA.size[1]>spriteB.y+spriteB.size[1] and spriteA.y>=(spriteB.y) and spriteA.y<=(spriteB.y+spriteB.size[1]):
                    print("yb")
                    spriteA.yChange=0
                    spriteA.y=spriteB.y+(spriteB.size[1])
                    
                if spriteA.xChange>=0 and spriteA.x<spriteB.x and (spriteA.x+spriteA.size[0])>=spriteB.x and (spriteA.x+spriteA.size[0])<=(spriteB.x+spriteB.size[0]):
                    print("xa")
                    spriteA.xChange=0
                    spriteA.x=spriteB.x-(spriteA.size[0])
                if spriteA.xChange<=0 and spriteA.x+spriteA.size[0]>spriteB.x+spriteB.size[0] and spriteA.x>=(spriteB.x) and spriteA.x<=(spriteB.x+spriteB.size[0]):
                    print("xb")
                    spriteA.xChange=0
                    spriteA.x=spriteB.x+(spriteB.size[0])    
                    
                
            #else:
                #sprite.registry[colB].kill()
                #del sprite.registry[(colB)]
            
    """
    else:
        for n in range(len(sprites)-1):
            sprites[n+1].colour=black
    """
    """
    for n in range(len(sprite.registry)):
        if sprite.sType!="Map":
            sprite[n].yChange=sprite[n].yChange+9.81*
            
    """        #v=u+at
    
    player.x+=player.xChange
    player.y+=player.yChange
    
    
    #box
    gameDisplay.fill(white)
    for n in range(len(sprite.registry)):
        pygame.draw.rect(gameDisplay,sprite.registry[n].colour,(sprite.registry[n].x,sprite.registry[n].y,sprite.registry[n].size[0],sprite.registry[n].size[1]))
        
    clock.tick(60)

    pygame.display.update()
    

end()
