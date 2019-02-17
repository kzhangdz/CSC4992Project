import pygame
from constant import *
import os.path
from textPrinter import TextPrinter
from pygameEnvironment import *
from card import Card

#test image
imgDirectory = os.path.join(os.path.abspath(os.curdir), 'images', 'menu', 'back_button.gif')
testImg = pygame.image.load(imgDirectory)

def showTestImg(x,y):
    gameDisplay.blit(testImg, (x,y))

#coordinates
x = (DISPLAY_WIDTH * 0.45)
y = (DISPLAY_HEIGHT * 0.8)

def main_menu():
    #create background
    gameDisplay.fill(FOREST_GREEN)
    TextPrinter.displayTitle("Memory Game")
    showTestImg(x,y)
    pygame.display.update()

def gameLoop():
    #create game loop
    running = True
    while running:
        main_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #print(event)

        #set frame rate
        clock.tick(30)

if __name__ == "__main__":
    gameLoop()
    pygame.quit()
    quit()


    
