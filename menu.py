'''file that stores all menu pages'''

import pygame
from pygameEnvironment import *
from constant import *
from button import Button
from button import ImageButton
from card import *
from cardDeck import *
from checkbox import *
from textPrinter import TextPrinter
import os
import copy

def mainMenu():
    #buttons
    singlePlayerButton = Button((DISPLAY_WIDTH*0.20, DISPLAY_HEIGHT*0.5), (200, 80), RED, "Single Player")
    multiPlayerButton = Button((DISPLAY_WIDTH*0.50, DISPLAY_HEIGHT*0.5), (200, 80), RED, "Multi Player")

    #test button
    imgDirectory = os.path.join(os.path.abspath(os.curdir), 'images', 'menu', 'button_test.png')
    testButton = ImageButton((DISPLAY_WIDTH*0.9, DISPLAY_HEIGHT*0.9), imgDirectory)

    #test CardDeck
    testDeck = CardDeck("theme1", 2)

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
            if testButton.isClicked(event):
                singlePlayerMenu()

        gameDisplay.fill(FOREST_GREEN)
        singlePlayerButton.draw(gameDisplay)
        multiPlayerButton.draw(gameDisplay)
        TextPrinter.displayTitle("Memory Game")
        #test button
        testButton.draw(gameDisplay)
        #test cardDeck
        testDeck.deck[0].showCard(300, 500)
            #pygame.time.wait(3000)
        testDeck.deck[0].setStatus(CardStatus.front)
         
        pygame.display.update()

        #set frames per second
        clock.tick(FPS)

def singlePlayerMenu():
    #buttons
    backButton = Button((DISPLAY_WIDTH*0.05, DISPLAY_HEIGHT*0.05), (80, 40), RED, "Back")
    
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
            TextPrinter.displayText("Single Player", (DISPLAY_WIDTH*0.50, DISPLAY_HEIGHT*0.3), 75, BLACK)
            pygame.display.update()

            #set frames per second
            clock.tick(FPS)

def multiPlayerMenu():
    #buttons
    backButton = Button((DISPLAY_WIDTH*0.05, DISPLAY_HEIGHT*0.05), (80, 40), RED, "Back")

    #test checkbox
    musicCheckbox = Checkbox((DISPLAY_WIDTH*0.5, DISPLAY_HEIGHT*0.5))

    #FIXME: Call checkMusic() function. if musicBox.state == True: ...
    
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
            if musicCheckbox.isClicked(event):
                #check or uncheck music box
                musicCheckbox.switchState()
                if musicCheckbox.state == True:
                    musicCheckbox = Checkbox((DISPLAY_WIDTH*0.5, DISPLAY_HEIGHT*0.5), trueImageDirectory)
                elif musicCheckbox.state == False:
                    musicCheckbox = Checkbox((DISPLAY_WIDTH*0.5, DISPLAY_HEIGHT*0.5))

            gameDisplay.fill(FOREST_GREEN)
            backButton.draw(gameDisplay)
            TextPrinter.displayText("Multi Player", (DISPLAY_WIDTH*0.50, DISPLAY_HEIGHT*0.3), 75, BLACK)

            #test checkbox
            musicCheckbox.draw(gameDisplay)
            pygame.display.update()

            #set frames per second
            clock.tick(FPS)

def gameplayMenu():
    #needs to pass in parameters that define game state
    #alternatively, options menu should open in a new frame above the current one
    pass

if __name__ == "__main__":
    mainMenu()
    quit()
