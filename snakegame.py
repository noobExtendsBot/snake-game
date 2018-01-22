#!/usr/bin/python

#Snake Game

import pygame, sys, random, time
check_errors = pygame.init()                                                                                            #initialize pygame

if check_errors[1] > 0:                                                                                                 #(6,0) => second element of tuple shows the number of error occured
    print("(!) Had {} initializing erros,exiting ...".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) PyGame successfully initialized!")

#Game window

playSurface = pygame.display.set_mode((720, 460))                                                                       #create a display screen where game will be displayed
pygame.display.set_caption("Snake Game")                                                                                #add a window set caption

#All the colors variable will be defined here

red = pygame.Color(255,0,0)                                                                                             #red color for gameover
green = pygame.Color(0,255,0)                                                                                           #green color for snake
black = pygame.Color(0,0,0)                                                                                             #score display box
white = pygame.Color(255,255,255)                                                                                       #background for game window
brown = pygame.Color(165,42,42)                                                                                         #food color

#Creating Game Variables

fpsController = pygame.time.Clock()                                                                                     #fpsController it will generally control how fast snake is going to run
score = 0                                                                                                               #define and initialize variable to zero
snakePos = [100,50]                                                                                                     #snake Position where it will be born
snakeBody = [[100,50], [90,50], [80,50]]                                                                                #snake Body every rectangle is aligned one after another using 2D array
foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]                                                         #creating random position for food spwan
foodSpawn = True                                                                                                        #create a foodSpawn variable and set it to True
direction = 'RIGHT'                                                                                                     #variable 'direction' will keep count of present direction
changeto = direction                                                                                                    #'changeto' variable will take account of direction where we have to switch

#Game over function

def gameOver():
    myFont = pygame.font.SysFont('monaco',72)                                                                           #choose the font from system font for game over display with font size
    GOsurf = myFont.render('Game Over!',True,red)                                                                       #render the font with text on screen with anti-alising as true
    GOrect = GOsurf.get_rect()                                                                                          #get the rectangular area on the surface
    GOrect.midtop = (360, 180)
    playSurface.blit(GOsurf,GOrect)
    pygame.display.flip()
    showScore(12)
    time.sleep(5)
    pygame.quit()                                                                                                       #game display exit
    sys.exit()                                                                                                          #console exit
#show score
def showScore(choice=1):
    sFont = pygame.font.SysFont('monaco',20)
    Ssurf = sFont.render('Score: {0}'.format(score), True, black)
    Srect = Ssurf.get_rect()
    if choice == 1:
        Srect.midtop = (80,10)
    else:
        Srect.midtop = (360, 120)
    playSurface.blit(Ssurf, Srect)
    pygame.display.flip()

#gameOver()

#Events
#MAIN LOGIC of game

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeto='RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeto='LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeto='UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeto='DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
    # validation of direction

    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeto == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeto == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10

    # snake body mechanism

    snakeBody.insert(0,list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score += 1
        foodSpawn = False
    else:
        snakeBody.pop()
    if foodSpawn == False:
        foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]

    foodSpawn = True

    playSurface.fill(white)
    for pos in snakeBody:
        #playerSurface, color , rectangular component
        pygame.draw.rect(playSurface, green,pygame.Rect(pos[0],pos[1],10,10))
    pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0], foodPos[1], 10, 10))

    if snakePos[0]>710 or snakePos[0]<0:
        gameOver()
    if snakePos[1]>450 or snakePos[1]<0:
        gameOver()
    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            gameOver()
    pygame.display.flip()
    showScore()
    fpsController.tick(15)



