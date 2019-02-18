'''file that stores all menu pages'''

import pygame
from pygameEnvironment import *
from constant import *
from button import Button
from textPrinter import TextPrinter

def mainMenu():
    #buttons
    singlePlayerButton = Button((DISPLAY_WIDTH*0.20, DISPLAY_HEIGHT*0.5), (200, 80), RED, "Single Player")
    multiPlayerButton = Button((DISPLAY_WIDTH*0.50, DISPLAY_HEIGHT*0.5), (200, 80), RED, "Multi Player")

    #game loop
    running = True

    while running:
        #events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_ESCAPE: # quit when pressing escape
                     pygame.quit()

            if singlePlayerButton.isClicked(event):
                #call single player menu
                singlePlayerMenu()
            if multiPlayerButton.isClicked(event):
                #call multi player menu
                multiPlayerMenu()

        gameDisplay.fill(FOREST_GREEN)
        singlePlayerButton.draw(gameDisplay)
        multiPlayerButton.draw(gameDisplay)
        TextPrinter.displayTitle("Memory Game")
        pygame.display.update()

        #set frames per second
        clock.tick(FPS)

def singlePlayerMenu():
    #buttons
    backButton = Button((DISPLAY_WIDTH*0.1, DISPLAY_HEIGHT*0.1), (100, 80), RED, "Back")
    
    #game loop
    running = True

    while running:
        #events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_ESCAPE: # quit when pressing escape
                     pygame.quit()

            if backButton.isClicked(event):
                #call main menu
                mainMenu()

            gameDisplay.fill(FOREST_GREEN)
            backButton.draw(gameDisplay)
            pygame.display.update()

            #set frames per second
            clock.tick(FPS)

def multiPlayerMenu():
    #buttons
    backButton = Button((DISPLAY_WIDTH*0.1, DISPLAY_HEIGHT*0.1), (100, 80), RED, "Back")
    
    #game loop
    running = True

    while running:
        #events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_ESCAPE: # quit when pressing escape
                     pygame.quit()

            if backButton.isClicked(event):
                #call main menu
                mainMenu()

            gameDisplay.fill(FOREST_GREEN)
            backButton.draw(gameDisplay)
            pygame.display.update()

            #set frames per second
            clock.tick(FPS)
