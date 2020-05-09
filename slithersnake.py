import pygame,sys
import time
import random

#initialise the game
pygame.init()

#set up the colors
BLACK = [0,0,0]
WHITE = [255,255,255]
RED = [255,0,0]

#set up the window
WIDTH = 800
HEIGHT = 600

#set up the screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Slither Snake')

font = pygame.font.SysFont(None,25, bold = True)

#function to quit game
def myquit(): 
    pygame.quit()
    sys.exit()


#setting up the clock
clock = pygame.time.Clock() #it keeps the track of event based on time
FPS = 5                    # it is the frames per second
blockSize = 20              # this is the block size of the snake in which it moves
noPixel = 0                 


#function to draw snake
def snake(blockSize,snakelist):
    for size in snakelist:
        pygame.draw.rect(screen,BLACK,[size[0]+5,size[1],blockSize,blockSize],2)

#function to display message on screen
def message_to_screen(msg,color):
    screen_text = font.render(msg,True,color)
    screen.blit(screen_text,[WIDTH/2,HEIGHT/2])

#main loop of the game
def gameLoop():

    gameExit = False
    gameOver = False

    #starting co-ordinates of snake
    lead_x = WIDTH/2
    lead_y = HEIGHT/2

    change_pixels_of_x = 0
    change_pixels_of_y = 0

    snakelist = []
    snakelength = 1

    #random co-ordinates of apple
    randomAppleX = round(random.randrange(0,WIDTH-blockSize)/10.0)*10
    randomAppleY = round(random.randrange(0,HEIGHT-blockSize)/10.0)*10

    #event loop
    while not gameExit:
        while gameOver == True:
            screen.fill(WHITE)
            message_to_screen('Game Over!! Press c to play again or q to quit', RED)
            pygame.display.update()

            for event in pygame.event.get():
                if even.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True

                if event.type == KEYDOWN:
                    if event.key == K_q:
                        gameOver = False
                        gameExit = True

                    if event.type == K_q:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        myquit()
                    leftArrow = event.key == pygame.K_LEFT
                    rightArrow = event.key == pygame.K_RIGHT
                    upArrow = event.key == pygame.K_UP
                    downArrow = event.key == pygame.K_DOWN
                    
                    if leftArrow:
                        change_pixels_of_x = - blockSize
                        change_pixels_of_y = noPixel
                    elif rightArrow:
                        change_pixels_of_x = blockSize
                        change_pixels_of_y = noPixel
                    elif upArrow:
                        change_pixels_of_x = noPixel
                        change_pixels_of_y = -blockSize
                    elif downArrow:
                        change_pixels_of_x = noPixel
                        change_pixels_of_y = blockSize
                if lead_x >= WIDTH or lead_x < 0 or lead_y >= HEIGHT or lead_y < 0:
                     gameOver = True
        lead_x += change_pixels_of_x
        lead_y += change_pixels_of_y

        screen.fill(WHITE)
        AppleThickness = 20

        print([int(randomAppleX),int(randomAppleY),AppleThickness,AppleThickness])
        pygame.draw.rect(screen,RED,[int(randomAppleX)+1,int(randomAppleY)+1,AppleThickness,AppleThickness])

        allspriteslist = []
        allspriteslist.append(lead_x)
        allspriteslist.append(lead_y)
        snakelist.append(allspriteslist)

        if len(snakelist)> snakelength:
            del snakelist[0]

        for eachSegment in snakelist[:-1]:
            if eachSegment == allspriteslist:
                gameOver = True

         # actual drawing snake
        snake(blockSize,snakelist)
        pygame.display.update()

        #when snake eats the apple
        if lead_x >= randomAppleX and lead_x <= randomAppleX + AppleThickness:
            if lead_y >= randomAppleY and lead_y <= randomAppleY + AppleThickness:
                randomAppleX = round(random.randrange(0,WIDTH-blockSize)/10.0)*10
                randomAppleY = round(random.randrange(0,HEIGHT-blockSize)/10.0)*10 
                snakelength += 1
        clock.tick(FPS)  
    pygame.quit()
    quit()
gameLoop()










                











