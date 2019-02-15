# initialisation ---------------------------------------------------
import pygame
import time

# settings file read ------------------------------
config = open("Settings.txt", "r")
settings = config.read().split("z")
config.close()

res = settings[0].split("x")
resolution = []
for nums in res:
    resolution.append(int(nums))

# detect actual monitor size
display = pygame.display.set_mode((0, 0))
infoObject = pygame.display.Info()
monitorResolution = [infoObject.current_w, infoObject.current_h]
# print(monitorResolution)


gameDisplay = pygame.display.set_mode(resolution,16)


global difficulty
if settings[2] == "1":
    pygame.display.toggle_fullscreen()  #only works in a linux enviroment
    

if settings[1] == "Easy":
    difficulty = 15
elif settings[1] == "Hard":
    difficulty = 30
else:
    difficulty = 20

# pygame.font.init()
pygame.init()

# colour definitions -----------------------------------------------
white = (240, 240, 240)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (80, 80, 80)

# initilization ------------------------------------------------------
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

# variables --------------------------------------------------------

scale = int(resolution[1] / 14.1)
speed = scale/5
jumpHeight = 1.2*speed
#print(speed, jumpHeight, scale)
global gameOver
gameOver = False


class sprite():
    registry = []

    def __init__(self, x, y, size, sType, colour):
        for n in range(2):
            size[n]=float(size[n])*scale          
        self.registry.append(self)
        self.x = x*scale
        self.y = y*scale
        self.size = size
        self.sType = sType
        self.colour = colour
        
        if self.sType == "EnemyM":
            self.vx = speed
            self.vy = 0
        else:
            self.vx = 0
            self.vy = 0
        self.timeLeave = 0
        self.onGround = False
        if self.sType == "Player":
            self.health = 100
            self.iTime = 0
                    
    def up(self):
        if self.onGround == True:
            self.timeLeave = pygame.time.get_ticks()  # current time
            self.vy = - jumpHeight
        self.onGround = False
        return

    def left(self):
        self.vx = -speed
        return

    def right(self):
        self.vx = speed
        return

    def damage(self):
        global difficulty
        damageHP = difficulty
        if self.sType != "Player":
            print("Type Error")
        else:
            if self.health > damageHP:
                if pygame.time.get_ticks() > self.iTime:
                    self.health -= damageHP
                    self.iTime = pygame.time.get_ticks()+250
            else:
                self.health = 0
                global gameOver
                gameOver = "Fail"

                
    def kill(self):
        del self


#sprites ---------------------------------------------------------------------------------------------------------

# spriteName = sprite(x, y, [width, height], type, colour)

player = sprite(3, 9, [1, 1.6], "Player", blue)
map1 = sprite(-100, ((resolution[1] - resolution[1] /48)/scale), [1000, resolution[1] / 40], "Map", black)
map2 = sprite(-15,-5,[1,20], "Map",black)

map3 = sprite(6, 9, [1.5, 0.5], "Map", black)
map4 = sprite(2, 7, [2,1.5], "Map", black)
map5 = sprite(11,3, [1,8], "Map", black)


spike1 = sprite(11.5,13.5,[19.3,0.6],"EnemyS",red)
map6 = sprite(15,3, [1,8], "Map", black)
map7 = sprite(25,3, [1,8], "Map", black)
map8 = sprite(30,3, [1,11], "Map", black)

map9 = sprite(35.5,7.5, [6.5,1], "Map", black)
map10 = sprite(35,-10, [1,18.5],"Map",black)
enemy1 = sprite(35,13, [1,1.6], "EnemyM",red)
map11 = sprite(45,9, [1,5],"Map",black)

map12 = sprite(40,3.5, [7,1],"Map",black)
spike2 = sprite(45,13.5, [11,0.6],"EnemyS",red)
map13 = sprite(55, 1,[2,1],"Map",black)
map14 = sprite(57,1,[1,15],"Map",black)
map15 = sprite(63,-10,[1,19],"Map",black)
enemy2 = sprite(58,3,[1,1.6],"EnemyM",red)

map16 = sprite(70,9,[0.5,1],"Map",black)
map17 = sprite(75,5,[0.5,1],"Map",black)
map18 = sprite(82,3,[0.5,1],"Map",black)
map19 = sprite(89,1,[5,1],"Map",black)
portal = sprite(93,0,[1,1.6],"Exit",green)
spike3 = sprite(73,13.5,[100,0.6],"EnemyS",red)
 
def gameEnd(result,score):
    if result == "Fail":
        print("GAME OVER")
        print("SCORE: "+str(round(score)))
    else:
        print("GAME COMPLETE")
        print("SCORE: "+str(round(score)))
    time.sleep(0.5)
    end()

def end():
    pygame.quit()
    pygame.joystick.quit()
    quit()


# collision detection --------------------------------------------------------
def spriteColide():
    cols = []
    for n in range(len(sprite.registry)):
        for m in range(len(sprite.registry)):
            if n != m:
                if sprite.registry[n].x + sprite.registry[n].size[0] >= sprite.registry[m].x and \
                   sprite.registry[n].x <= sprite.registry[m].x + sprite.registry[m].size[0] and \
                   sprite.registry[n].y + sprite.registry[n].size[1] >= sprite.registry[m].y and \
                   sprite.registry[n].y <= sprite.registry[m].y + sprite.registry[m].size[1]:
                    col = n, m
                    cols.append(col)
    # print(cols)
    return cols

while gameOver == False:
    
    keys = pygame.key.get_pressed()
    if keys[119] or keys[32]:
        player.up()
    if keys[97]:
        player.left()
    if keys[100]:
        player.right()
        
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            end()
        if event.type == pygame.KEYDOWN:
            # print(event.key)
            if event.key == 292:
                pygame.display.toggle_fullscreen()
            if event.key == 119 or event.key == 32:  # w
                player.up()
            if event.key == 97:  # a
                player.left()
            if event.key == 100:  # d
                player.right()
        if event.type == pygame.KEYUP:
            if event.key == 119 or event.key == 32:  # w
                if player.vy == -speed:
                    player.vy = 0
            if event.key == 97:  # a
                if player.vx == -speed:
                    player.vx = 0
            if event.key == 100:  # d
                if player.vx == speed:
                    player.vx = 0

        if event.type == pygame.JOYAXISMOTION:
            print("Joy", event)
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joy button pressed", event)
            if joystick.get_button(2)==1:
                player.up()

    # joystick-----------------------------------

    joystick_count = pygame.joystick.get_count()

    if joystick_count > 0:    
        for i in range(joystick_count):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()

            hats = joystick.get_numhats()
            for i in range(hats):
                hat = joystick.get_hat(i)
                if hat == (1, 0):# right
                    player.right()
                elif hat == (-1, 0):# left
                    player.left()
                elif hat == (0, 1):# up
                    player.up()
                #elif hat == (0, -1):# down
                elif hat == (0, 0):
                    player.vx = 0
                #print(hat)

    # joystick.get_axis(0)
    # if event.type == pygame.JOYBUTTONDOWN:
    #        if joystick.get_button(9)==1:


    #Move Sprites-------------------------------------------------------------
    
    for n in range(len(sprite.registry)):
        sprite.registry[n].x += sprite.registry[n].vx
        sprite.registry[n].y += sprite.registry[n].vy

    #print(enemy1.x,enemy1.y)


    #Collision Handling
        
    colisions = spriteColide()

    if colisions != []:
        colFlag = 0
        for n in range(len(colisions)):
            colision = colisions[n]
            spriteA = sprite.registry[int(colision[0])]
            spriteB = sprite.registry[int(colision[1])]
            
            if spriteB.sType == "Map" and spriteA.sType != "Map":
                if spriteA.sType == "Player":
                    colFlag += 1
                sides = ""
                if spriteA.vy >= 0 and spriteA.y < spriteB.y and (spriteA.y + spriteA.size[1]) >= spriteB.y and (
                        spriteA.x + spriteA.size[0] > spriteB.x and spriteA.x < spriteB.x + spriteB.size[0]):
                    sides = sides + "u"
                if spriteA.vy <= 0 and spriteA.y + spriteA.size[1] > spriteB.y + spriteB.size[1] and spriteA.y <= (
                        spriteB.y + spriteB.size[1]) and (
                        spriteA.x + spriteA.size[0] > spriteB.x and spriteA.x < spriteB.x + spriteB.size[0]):
                    sides = sides + "d"
                if spriteA.vx >= 0 and spriteA.x < spriteB.x and (
                        spriteA.x + spriteA.size[0]) >= spriteB.x and spriteA.y + spriteA.size[
                    1] > spriteB.y and spriteA.y < spriteB.y + spriteB.size[1]:
                    sides = sides + "l"
                if spriteA.vx <= 0 and spriteA.x + spriteA.size[0] > spriteB.x + spriteB.size[
                    0] and spriteA.x <= spriteB.x + spriteB.size[0] and spriteA.y + spriteA.size[
                    1] > spriteB.y and spriteA.y < spriteA.y + spriteA.size[1]:
                    sides = sides + "r"

                #if spriteA.sType == "Player":  #test data
                #    print(sides)
                if sides == "u":                    
                    spriteA.timeLeave = pygame.time.get_ticks()  # current time
                    spriteA.onGround = True
                    #print(pygame.time.get_ticks())
                    spriteA.vy = 0
                    spriteA.y = spriteB.y - (spriteA.size[1])
                elif sides == "d":
                    spriteA.vy = 0
                    spriteA.y = spriteB.y + (spriteB.size[1])
                elif sides == "l":
                    if spriteA.sType == "EnemyM":
                        spriteA.vx = spriteA.vx*-1
                    else:
                        #spriteA.onGround = True #
                        spriteA.vx = 0
                        spriteA.x = spriteB.x - (spriteA.size[0])
                elif sides == "r":
                    if spriteA.sType == "EnemyM":
                        spriteA.vx = spriteA.vx*-1
                    else:
                        #spriteA.onGround = True #
                        spriteA.vx = 0
                        spriteA.x = spriteB.x + (spriteB.size[0])
                elif sides == "dr":
                    if (spriteB.x + spriteB.size[0] - spriteA.x) > (spriteB.y + spriteB.size[1] - spriteA.y):
                        spriteA.vy = 0
                        spriteA.y = spriteB.y + spriteB.size[1]
                    else:
                        spriteA.vx = 0
                        spriteA.x = spriteB.x + spriteB.size[0]
                elif sides == "dl":
                    if ((spriteA.x + spriteA.size[0]) - spriteB.x) > (spriteB.y + spriteB.size[1] - spriteA.y):
                        spriteA.vy = 0
                        spriteA.y = spriteB.y + spriteB.size[1]
                    else:
                        spriteA.vx = 0
                        spriteA.x = spriteB.x - spriteA.size[0]
                elif sides == "ul":
                    spriteA.onGround = True #
                    if (spriteA.x + spriteA.size[0] - spriteB.x) > (spriteA.y + spriteA.size[1] - spriteB.y):
                        spriteA.vy = 0
                        spriteA.y = spriteB.y - spriteA.size[1]
                    else:
                        spriteA.vx = 0
                        spriteA.x = spriteB.x - spriteA.size[0]
                elif sides == "ur":
                    spriteA.onGround = True #
                    if (spriteB.x + spriteB.size[0] - spriteA.x) > (spriteA.y + spriteA.size[1] - spriteB.y):
                        spriteA.vy = 0
                        spriteA.y = spriteB.y - spriteA.size[1]
                    else:
                        spriteA.vx = 0
                        spriteA.x = spriteB.x + spriteB.size[0]

                        # if the two are equal then it will pick the second option
                elif sides == "udl":
                    spriteA.vx = 0
                    spriteA.x = spriteB.x - spriteA.size[0]
                elif sides == "udr":
                    spriteA.vx = 0
                    spriteA.x = spriteB.x + spriteB.size[0]
                elif sides == "ulr":
                    spriteA.vy = 0
                    spriteA.y = spriteB.y - spriteA.size[1]
                elif sides == "dlr":
                    spriteA.vy = 0
                    spriteA.y = spriteB.y + spriteB.size[1]
                else:
                    break
                    print(sides)

            #Enemy
            elif spriteA.sType == "Player" and (spriteB.sType == "EnemyM" or spriteB.sType == "EnemyS"):
                spriteA.damage()

            elif spriteA.sType == "EnemyM":
                if spriteB.sType == "Player":
                    spriteB.damage()

            #Exit
            elif spriteA.sType == "Player" and spriteB.sType == "Exit":
                gameOver = "Win"
                
        if colFlag == 0:
            player.onGround = False
    else:
        player.onGround = False 
    #print(player.onGround)

    
    #gravity--------------------------------------------------
                    
    if False == player.onGround:
        player.vy = player.vy + 1.5*((pygame.time.get_ticks()-player.timeLeave)/1000) # v = u + a*t
        #print((pygame.time.get_ticks()-player.timeLeave)/1000) #log

    
  


    #Display
        
    camX = player.x - (resolution[0]/2)
    if player.y > resolution[1]/3:
        camY = 0
    else:
        camY = player.y - (resolution[1]/3)
    
    gameDisplay.fill(white)
    
    
    for n in range(len(sprite.registry)):
        pygame.draw.rect(gameDisplay, sprite.registry[n].colour, \
                         (sprite.registry[n].x-camX, sprite.registry[n].y-camY, sprite.registry[n].size[0], sprite.registry[n].size[1]))

    #health bar
    pygame.draw.rect(gameDisplay, black, (21.5*scale,0.4*scale,3*scale,0.6*scale))
    if player.health != 0:
        pygame.draw.rect(gameDisplay, red, (21.6*scale,0.5*scale,2.8*scale*player.health/100,0.4*scale))

    clock.tick(60)
    
    pygame.display.update()

gameEnd(gameOver,(player.x-resolution[0]/3)/scale)
