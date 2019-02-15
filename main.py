import pygame
from constant import *
import os.path
from textPrinter import TextPrinter
from pygameEnvironment import *

#test image
imgDirectory = os.path.join(os.path.abspath(os.curdir), 'images', 'menu', 'back_button.gif')
testImg = pygame.image.load(imgDirectory)

def showTestImg(x,y):
    display.blit(testImg, (x,y))

#coordinates
x = (DISPLAY_WIDTH * 0.45)
y = (DISPLAY_HEIGHT * 0.8)

def gameLoop():
    #create game loop
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #gameExit = True
                pygame.quit()
                quit()
            #print(event)

        
        #create background
        display.fill(FOREST_GREEN)
        TextPrinter.displayTitle("Memory Game")
        showTestImg(x,y)
        pygame.display.update()

        #set frame rate
        clock.tick(30)

if __name__ == "__main__":
    gameLoop()
    pygame.quit()
    quit()


    
