'''file that stores all menu pages'''

import pygame
from pygameEnvironment import *
from constant import *
from button import Button
from button import ImageButton
from card import *
from cardDeck import *
from checkbox import *
from score import *
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
         
        pygame.display.update()

        #set frames per second
        clock.tick(FPS)

def singlePlayerMenu():
    #buttons
    backButton = Button((DISPLAY_WIDTH*0.05, DISPLAY_HEIGHT*0.05), (80, 40), RED, "Back")
    gameplayButton = Button((DISPLAY_WIDTH*0.5, DISPLAY_HEIGHT*0.5), (80, 40), RED, "Start w/ 10 cards")    

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
            if gameplayButton.isClicked(event):
                #call main menu
                gameplayMenu(10)

            gameDisplay.fill(FOREST_GREEN)
            backButton.draw(gameDisplay)

            gameplayButton.draw(gameDisplay)
            
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

def gameplayMenu(numCards):
    #needs to pass in parameters that define game state
    #alternatively, options menu should open in a new frame above the current one

    #declare button
    backButton = Button((DISPLAY_WIDTH*0.05, DISPLAY_HEIGHT*0.05), (80, 40), RED, "Back")

    #declare card deck
    currentDeck = CardDeck("theme1", numCards)

    #declare score
    currentScore = Score()

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
                singlePlayerMenu()

            #switch card state if clicked
            for card in currentDeck.deck:
                if card.isClicked(event):
                    print(card.cardImageDirectories[card.status], card.position)
                    card.switchStatus()

            #background
            gameDisplay.fill(FOREST_GREEN)
            backButton.draw(gameDisplay)
            currentScore.displayScore()

            #show cards
            for card in currentDeck.deck:
                card.showCard() 

            #check state of deck to see if cards should be flipped
            currentDeck.checkDeckStatus(currentScore)
            
            pygame.display.update()

            #if all cards face up, send user to results screen
            if currentDeck.checkAllFaceUp():
                resultMenu(currentScore)

            #set frames per second
            clock.tick(FPS)

def resultMenu(score):
    #buttons
    menuButton = Button((DISPLAY_WIDTH*0.3, DISPLAY_HEIGHT*0.5), (200, 80), RED, "Return to Menu")

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

            if menuButton.isClicked(event):
                #call main menu
                mainMenu()

            #background
            gameDisplay.fill(FOREST_GREEN)

            TextPrinter.displayText("Congratulations!", (DISPLAY_WIDTH*0.5, DISPLAY_HEIGHT*0.4), 75, BLACK)
            
            score.displayScore()

            menuButton.draw(gameDisplay)
            
            pygame.display.update()

            #set frames per second
            clock.tick(FPS)

if __name__ == "__main__":
    mainMenu()
    quit()
