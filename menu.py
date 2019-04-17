'''file that stores all menu pages'''

import pygame
from pygameEnvironment import *
from constant import *
from button import Button
from button import ImageButton
from card import *
from cardDeck import *
from checkbox import *
from directoryParser import *
from inputBox import *
from score import *
from textPrinter import TextPrinter
import os
import copy
from statistics import *

stats = Statistics() #global

def mainMenu():
    #buttons
    #singlePlayerButton = Button((DISPLAY_WIDTH*0.33, DISPLAY_HEIGHT*0.5), (200, 80), RED, "Single Player")
    #multiPlayerButton = Button((DISPLAY_WIDTH*0.66, DISPLAY_HEIGHT*0.5), (200, 80), RED, "Multi Player")

    imgDirectory = os.path.join(os.path.abspath(os.curdir), 'images', 'menu', 'button_single-player.png')
    singlePlayerButton = ImageButton((DISPLAY_WIDTH*0.33, DISPLAY_HEIGHT*0.5), imgDirectory)

    imgDirectory = os.path.join(os.path.abspath(os.curdir), 'images', 'menu', 'button_two-player.png')
    multiPlayerButton = ImageButton((DISPLAY_WIDTH*0.66, DISPLAY_HEIGHT*0.5), imgDirectory)

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
                #singlePlayerMenu()
                statisticsMenu() #- Ibrahim, trying to display temp stats

        gameDisplay.fill(BLACK)  #FOREST_GREEN
        singlePlayerButton.draw(gameDisplay)
        multiPlayerButton.draw(gameDisplay)
        #TextPrinter.displayTitle("Memory Game")
        TextPrinter.displayText("Memory Game", (DISPLAY_WIDTH*0.50, DISPLAY_HEIGHT*0.15), 75, BLUE)
        #test button
        testButton.draw(gameDisplay)

        pygame.display.update()

        #set frames per second
        clock.tick(FPS)

def singlePlayerMenu():
    global stats
    #buttons
    backButton = Button((DISPLAY_WIDTH*0.1, DISPLAY_HEIGHT*0.1), (80, 40), RED, "Back")
    gameplay10Button = Button((DISPLAY_WIDTH*0.5, DISPLAY_HEIGHT*0.5), (200, 40), RED, "Start w/ 10 cards")
    gameplay14Button = Button((DISPLAY_WIDTH*0.5, DISPLAY_HEIGHT*0.65), (200, 40), RED, "Start w/ 14 cards")
    gameplay18Button = Button((DISPLAY_WIDTH*0.5, DISPLAY_HEIGHT*0.8), (200, 40), RED, "Start w/ 18 cards")

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
            if gameplay10Button.isClicked(event):
                stats.raiseGamesPlayed()
                print(stats.GamesPlayed)
                gameplayMenu(10)
            if gameplay14Button.isClicked(event):
                stats.raiseGamesPlayed()
                print(stats.GamesPlayed)
                gameplayMenu(14)
            if gameplay18Button.isClicked(event):
                stats.raiseGamesPlayed()
                print(stats.GamesPlayed)
                gameplayMenu(18)

            gameDisplay.fill(BLACK) # FOREST_GREEN
            backButton.draw(gameDisplay)

            gameplay10Button.draw(gameDisplay)
            gameplay14Button.draw(gameDisplay)
            gameplay18Button.draw(gameDisplay)

            TextPrinter.displayText("Single Player", (DISPLAY_WIDTH*0.50, DISPLAY_HEIGHT*0.3), 75, BLUE)  #changed-ibrahim
            pygame.display.update()

            #set frames per second
            clock.tick(FPS)

def statisticsMenu():
    global stats

    #statistic = Statistics()
    #buttons
    backButton = Button((DISPLAY_WIDTH*0.1, DISPLAY_HEIGHT*0.1), (80, 40), RED, "Back")

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

            gameDisplay.fill(BLACK) #FOREST_GREEN
            backButton.draw(gameDisplay)

            TextPrinter.displayText("Statistics", (DISPLAY_WIDTH*0.50, DISPLAY_HEIGHT*0.15), 75, BLUE) #changed-ibrahim
            #TextPrinter.displayText(str(stats.CardsClicked), (DISPLAY_WIDTH*0.30, DISPLAY_HEIGHT*0.35), 50, FOREST_GREEN)
            stats.displayStats() #IBRAHIM DISPLAY doesnt work
            pygame.display.update()

            #set frames per second
            clock.tick(FPS)

def multiPlayerMenu():
    #buttons
    backButton = Button((DISPLAY_WIDTH*0.1, DISPLAY_HEIGHT*0.1), (80, 40), RED, "Back")

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

            gameDisplay.fill(BLACK) #FOREST_GREEN
            backButton.draw(gameDisplay)
            TextPrinter.displayText("Multi Player", (DISPLAY_WIDTH*0.50, DISPLAY_HEIGHT*0.3), 75, BLUE) #changed-ibrahim

            #test checkbox
            musicCheckbox.draw(gameDisplay)
            pygame.display.update()

            #set frames per second
            clock.tick(FPS)

def gameplayMenu(numCards):
    global stats
    #needs to pass in parameters that define game state
    #alternatively, options menu should open in a new frame above the current one

    #declare button
    backButton = Button((DISPLAY_WIDTH*0.1, DISPLAY_HEIGHT*0.1), (80, 40), RED, "Back")

    #declare card deck
    #FIXME: refactor use different themes
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

            #print(event)  #TESTING FOR EVENT

            if backButton.isClicked(event):
                #call main menu
                singlePlayerMenu()

            #switch card state if clicked
            for card in currentDeck.deck:
                if card.isClicked(event):
                    stats.raiseCardsClicked()
                    print(stats.CardsClicked)  #testing
                    print(card.cardImageDirectories[card.status], card.position)
                    card.switchStatus()

            #background
            gameDisplay.fill(BLACK)  #FOREST_GREEN
            backButton.draw(gameDisplay)
            currentScore.displayScore()
            currentScore.displayMultiplier()

            #show cards
            for card in currentDeck.deck:
                card.showCard()

            #check state of deck to see if cards should be flipped
            currentDeck.checkDeckStatus(currentScore, stats) #checks for cards matched

            pygame.display.update()

            #if all cards face up, send user to results screen
            if currentDeck.checkAllFaceUp():
                resultMenu(currentScore, "Congratulations!", numCards)

            #set frames per second
            clock.tick(FPS)

def resultMenu(score, displayMessage, numCards):
    #buttons
    highScoreButton = Button((DISPLAY_WIDTH*0.5, DISPLAY_HEIGHT*0.6), (200, 80), RED, "Save Score")
    menuButton = Button((DISPLAY_WIDTH*0.5, DISPLAY_HEIGHT*0.8), (200, 80), RED, "Return to Menu")

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
            if highScoreButton.isClicked(event):
                #call main menu
                highScoreMenu(score, numCards)

            #background
            gameDisplay.fill(BLACK) #FOREST_GREEN

            TextPrinter.displayText(displayMessage, (DISPLAY_WIDTH*0.5, DISPLAY_HEIGHT*0.4), 75, BLUE) #changed-ibrahim

            score.displayScore()

            menuButton.draw(gameDisplay)

            highScoreButton.draw(gameDisplay)

            pygame.display.update()

            #set frames per second
            clock.tick(FPS)

def highScoreMenu(score, numCards):
    #declare input box
    userInput = InputBox(DISPLAY_WIDTH*0.425, DISPLAY_HEIGHT*0.55, DISPLAY_WIDTH*0.1, DISPLAY_HEIGHT*0.1)

    highScoreDisplayButton = Button((DISPLAY_WIDTH*0.5, DISPLAY_HEIGHT*0.7), (200, 80), RED, "View High Scores")
    menuButton = Button((DISPLAY_WIDTH*0.5, DISPLAY_HEIGHT*0.9), (200, 80), RED, "Return to Menu")

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

            userName = userInput.handle_event(event)

            userInput.update()

            if userName != None: #if userInput box was given an input
                print(userName)
                DirectoryParser.saveScore(userName, score, numCards)

                #send user to high score display
                highScoreDisplayMenu(numCards)

            if highScoreDisplayButton.isClicked(event):
                highScoreDisplayMenu(numCards)
            if menuButton.isClicked(event):
                #call main menu
                mainMenu()

            #background
            gameDisplay.fill(BLACK) #FOREST_GREEN

            TextPrinter.displayText("Enter your name", (DISPLAY_WIDTH*0.5, DISPLAY_HEIGHT*0.4), 75, BLUE) #changed-ibrahim

            score.displayScore()

            highScoreDisplayButton.draw(gameDisplay)
            menuButton.draw(gameDisplay)

            userInput.draw(gameDisplay)

            pygame.display.update()

            #set frames per second
            clock.tick(FPS)

def highScoreDisplayMenu(numCards):
    scoreList = DirectoryParser.getTop10Scores(numCards)
    menuButton = Button((DISPLAY_WIDTH*0.5, DISPLAY_HEIGHT*0.8), (200, 80), RED, "Return to Menu")
    highScoreLabel = "High Scores (" + str(numCards) + " Cards)"

    #positions of text
    nameXPos = DISPLAY_WIDTH*0.33
    scoreXPos = DISPLAY_WIDTH*0.66
    scoreYPos = 0 #will be modified later in code

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
            gameDisplay.fill(BLACK) #FOREST_GREEN

            TextPrinter.displayText(highScoreLabel, (DISPLAY_WIDTH*0.5, DISPLAY_HEIGHT*0.1), 65, BLUE) #changed-ibrahim

            scoreYPos = DISPLAY_HEIGHT * 0.2
            for row in scoreList:
                #display name
                TextPrinter.displayText(str(row[0]), (nameXPos, scoreYPos), 30, BLUE) #changed-ibrahim
                #display score
                TextPrinter.displayText(str(row[1]), (scoreXPos, scoreYPos), 30, BLUE) #changed-ibrahim
                #increase position counter
                scoreYPos += DISPLAY_HEIGHT * 0.05

            menuButton.draw(gameDisplay)

            pygame.display.update()

            #set frames per second
            clock.tick(FPS)

if __name__ == "__main__":
    startPage = input("Choose start page (main, highscore): ")

    if startPage == "highscore":
        highScoreMenu(Score(), 10)
    else:
        mainMenu()
    quit()
