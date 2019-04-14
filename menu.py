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

def mainMenu():
    singleImgDirectory = os.path.join(os.path.abspath(os.curdir), 'images', 'menu', 'button_single-player.png')
    multiImgDirectory = os.path.join(os.path.abspath(os.curdir), 'images', 'menu', 'button_two-player.png')
    imgDirectoryOptions = os.path.join(os.path.abspath(os.curdir), 'images', 'menu', 'hamburger.png')

    singlePlayerButton = ImageButton((DISPLAY_WIDTH*0.33, DISPLAY_HEIGHT*0.5), singleImgDirectory)
    multiPlayerButton = ImageButton((DISPLAY_WIDTH*0.66, DISPLAY_HEIGHT*0.5), multiImgDirectory)
    optionsButton = ImageButton((DISPLAY_WIDTH * 0.9, DISPLAY_HEIGHT * 0.9), imgDirectoryOptions)

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
            if optionsButton.isClicked(event):
                optionMenu('main')

        gameDisplay.fill(FOREST_GREEN)
        singlePlayerButton.draw(gameDisplay)
        multiPlayerButton.draw(gameDisplay)
        TextPrinter.displayTitle("Memory Game")
        optionsButton.draw(gameDisplay)
         
        pygame.display.update()

        #set frames per second
        clock.tick(FPS)

def singlePlayerMenu():
    #buttons
    backButton = Button((DISPLAY_WIDTH*0.1, DISPLAY_HEIGHT*0.1), (80, 40), RED, "Back")
    imgDirectoryOptions = os.path.join(os.path.abspath(os.curdir), 'images', 'menu', 'hamburger.png')
    optionsButton = ImageButton((DISPLAY_WIDTH * 0.9, DISPLAY_HEIGHT * 0.9), imgDirectoryOptions)
    
    gameplay10Button = Button((DISPLAY_WIDTH*0.5, DISPLAY_HEIGHT*0.5), (200, 40), RED, "Easy (10 cards)")
    gameplay14Button = Button((DISPLAY_WIDTH*0.5, DISPLAY_HEIGHT*0.65), (200, 40), RED, "Medium (14 cards)")
    gameplay18Button = Button((DISPLAY_WIDTH*0.5, DISPLAY_HEIGHT*0.8), (200, 40), RED, "Hard (18 cards)")

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
                gameplayMenu(10)
            if gameplay14Button.isClicked(event):
                gameplayMenu(14)
            if gameplay18Button.isClicked(event):
                gameplayMenu(18)
            if optionsButton.isClicked(event):
                optionMenu('single')

            gameDisplay.fill(FOREST_GREEN)
            backButton.draw(gameDisplay)
            optionsButton.draw(gameDisplay)

            gameplay10Button.draw(gameDisplay)
            gameplay14Button.draw(gameDisplay)
            gameplay18Button.draw(gameDisplay)
            
            TextPrinter.displayText("Single Player", (DISPLAY_WIDTH*0.50, DISPLAY_HEIGHT*0.3), 75, BLACK)
            pygame.display.update()

            #set frames per second
            clock.tick(FPS)

def multiPlayerMenu():
    #buttons
    backButton = Button((DISPLAY_WIDTH*0.1, DISPLAY_HEIGHT*0.1), (80, 40), RED, "Back")
    imgDirectoryOptions = os.path.join(os.path.abspath(os.curdir), 'images', 'menu', 'hamburger.png')
    optionsButton = ImageButton((DISPLAY_WIDTH * 0.9, DISPLAY_HEIGHT * 0.9), imgDirectoryOptions)

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
            if optionsButton.isClicked(event):
                optionMenu('multi')

            gameDisplay.fill(FOREST_GREEN)
            backButton.draw(gameDisplay)
            TextPrinter.displayText("Multi Player", (DISPLAY_WIDTH*0.50, DISPLAY_HEIGHT*0.3), 75, BLACK)
            optionsButton.draw(gameDisplay)

            #test checkbox
            musicCheckbox.draw(gameDisplay)
            pygame.display.update()

            #set frames per second
            clock.tick(FPS)

def gameplayMenu(numCards):
    #needs to pass in parameters that define game state
    #alternatively, options menu should open in a new frame above the current one

    #declare button (SB: eliminated back button. Can only cancel gameplay from options menu)
    #backButton = Button((DISPLAY_WIDTH*0.1, DISPLAY_HEIGHT*0.1), (80, 40), RED, "Back")
    imgDirectoryOptions = os.path.join(os.path.abspath(os.curdir), 'images', 'menu', 'hamburger.png')
    optionsButton = ImageButton((DISPLAY_WIDTH * 0.9, DISPLAY_HEIGHT * 0.9), imgDirectoryOptions)

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

            '''if backButton.isClicked(event):
                #call main menu
                singlePlayerMenu()'''
            if optionsButton.isClicked(event):
                optionMenu('gameplay')

            #switch card state if clicked
            for card in currentDeck.deck:
                if card.isClicked(event):
                    print(card.cardImageDirectories[card.status], card.position)
                    card.switchStatus()

            #background
            gameDisplay.fill(FOREST_GREEN)
            #backButton.draw(gameDisplay)
            optionsButton.draw(gameDisplay)
            currentScore.displayScore()
            currentScore.displayMultiplier()

            #show cards
            for card in currentDeck.deck:
                card.showCard() 

            #check state of deck to see if cards should be flipped
            currentDeck.checkDeckStatus(currentScore)
            
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
            gameDisplay.fill(FOREST_GREEN)

            TextPrinter.displayText(displayMessage, (DISPLAY_WIDTH*0.5, DISPLAY_HEIGHT*0.4), 75, BLACK)
            
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
                print(len(userName))
                try:
                    if len(userName) > 10:
                        raise ValueError('Data should not exceed 10 characters. Length was {}'.format(len(userName)))
                    print(userName)
                    saveScore(userName, score, numCards)

                    #send user to high score display
                    highScoreDisplayMenu(numCards)
                except ValueError as err:
                    print("Did not save user. Character length exceeded.")

            if highScoreDisplayButton.isClicked(event):
                highScoreDisplayMenu(numCards)
            if menuButton.isClicked(event):
                #call main menu
                mainMenu()

            #background
            gameDisplay.fill(FOREST_GREEN)

            TextPrinter.displayText("Enter your name", (DISPLAY_WIDTH*0.5, DISPLAY_HEIGHT*0.3), 75, BLACK)
            TextPrinter.displayText("Limit: 10 characters", (DISPLAY_WIDTH*0.5, DISPLAY_HEIGHT*0.4), 25, BLACK)
            
            score.displayScore()

            highScoreDisplayButton.draw(gameDisplay)
            menuButton.draw(gameDisplay)

            userInput.draw(gameDisplay)
            
            pygame.display.update()

            #set frames per second
            clock.tick(FPS)

def highScoreDisplayMenu(numCards):
    scoreList = getTop10Scores(numCards)
    menuButton = Button((DISPLAY_WIDTH*0.5, DISPLAY_HEIGHT*0.8), (200, 80), RED, "Return to Menu")
    highScoreLabel = "High Scores (" + str(numCards) + " Cards)"

    recursionButton = Button((DISPLAY_WIDTH*0.2, DISPLAY_HEIGHT*0.9), (200, 80), RED, "Test Recursion")

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
            if recursionButton.isClicked(event):
                #call main menu
                testRecursion(scoreList)
                     
            #background
            gameDisplay.fill(FOREST_GREEN)

            TextPrinter.displayText(highScoreLabel, (DISPLAY_WIDTH*0.5, DISPLAY_HEIGHT*0.1), 65, BLACK)

            scoreYPos = DISPLAY_HEIGHT * 0.2
            for row in scoreList:
                #display name
                TextPrinter.displayText(str(row[0]), (nameXPos, scoreYPos), 30, BLACK)
                #display score
                TextPrinter.displayText(str(row[1]), (scoreXPos, scoreYPos), 30, BLACK)
                #increase position counter
                scoreYPos += DISPLAY_HEIGHT * 0.05

            menuButton.draw(gameDisplay)
            recursionButton.draw(gameDisplay)
            
            pygame.display.update()

            #set frames per second
            clock.tick(FPS)

def testRecursion(scoreList):
    def Sort(sub_li): 
        sub_li.sort(key = lambda x: x[0]) 
        return sub_li 

    sortedScores = Sort(scoreList)
    print(sortedScores)

    userKey = input("Enter a name to get its index: ")
    def binarySearchNestedList(arr, left, right, val):
        if right >= left:
            mid = (left + right)//2
            if arr[mid][0] == val:
                return mid
            elif arr[mid][0] > val:
                return binarySearchNestedList(arr, left, mid-1, val)
            elif arr[mid][0] < val:
                return binarySearchNestedList(arr, mid+1, right, val)
            else:
                return -1
        else:
            return -1 #not found

    left = 0
    right = len(sortedScores) - 1
    resultingIndex = binarySearchNestedList(sortedScores, left, right, userKey)

    print("Index of {} is {}".format(userKey, resultingIndex))
    

# option menu can only be called from four pages (the previous_page): 'main', 'single', 'multi', 'gameplay'
def optionMenu(previous_page):
	
	# positions (maybe move to constant.py)
	top_left = (DISPLAY_WIDTH * 0.05, DISPLAY_HEIGHT * 0.07)	# back button position
	
	
	# button images
	imgDirectoryBack = os.path.join(os.path.abspath(os.curdir), 'images', 'menu', 'back_button3.png')
	imgDirectoryCredits = os.path.join(os.path.abspath(os.curdir), 'images', 'menu', 'button_credits.png')
	imgDirectoryInstructions = os.path.join(os.path.abspath(os.curdir), 'images', 'menu', 'instructions.png')
	imgDirectoryStatistics = os.path.join(os.path.abspath(os.curdir), 'images', 'menu', 'stats.png')
	
	# declared buttons
	backButton = ImageButton(top_left, imgDirectoryBack)
	creditsButton = ImageButton((DISPLAY_WIDTH * 0.5, DISPLAY_HEIGHT * 0.6), imgDirectoryCredits)
	instructionsButton = ImageButton((DISPLAY_WIDTH * 0.5, DISPLAY_HEIGHT * 0.7), imgDirectoryInstructions)
	statiscticsButton = ImageButton((DISPLAY_WIDTH * 0.5, DISPLAY_HEIGHT * 0.8), imgDirectoryStatistics)
	
	# slider bar (placeholder)
	imgDirectorySlider = os.path.join(os.path.abspath(os.curdir), 'images', 'menu', 'slider_bar.png')
	slider = ImageButton((DISPLAY_WIDTH * 0.5, DISPLAY_HEIGHT * 0.5), imgDirectorySlider)
	
	
	# cancel gameplay, button position
	bottom_right = (DISPLAY_WIDTH * 0.9, DISPLAY_HEIGHT * 0.9)
	imgDirectoryClose = os.path.join(os.path.abspath(os.curdir), 'images', 'menu', 'button_x.png')	# 'cancel_game.png'
	closeButton = ImageButton(bottom_right, imgDirectoryClose)
	
	
	
	running = True		# keeps page open
	
	while running:
		
		# display info
		gameDisplay.fill(FOREST_GREEN)
		TextPrinter.displayTitle("Bela Memoro")
		
		backButton.draw(gameDisplay)
		creditsButton.draw(gameDisplay)
		instructionsButton.draw(gameDisplay)
		statiscticsButton.draw(gameDisplay)
		slider.draw(gameDisplay)
		
		if previous_page == 'gameplay':
			closeButton.draw(gameDisplay)
		
		for event in pygame.event.get():
			
			# pressing exit or escape
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
			
			# button presses (back, credits page, close gameplay, stats, instructions)
			if backButton.isClicked(event):
				if previous_page == 'gameplay':
					return
				elif previous_page == 'main':
					mainMenu()
				elif previous_page == 'single':
					singlePlayerMenu()
				elif previous_page == 'multi':
					multiPlayerMenu()
			if closeButton.isClicked(event):
				mainMenu()


			'''	correct these page name OR create these pages
			if creditsButton.isClicked(event):
				creditsPage()
			
			if instructionsButton.isClicked(event):
				instructionsPage()
			
			if statisticsButton.isClicked(event):
				statsPage()
			'''
			
			# volume slider bar
			
		
		pygame.display.update()
		clock.tick(FPS)


if __name__ == "__main__":
    startPage = input("Choose start page (main, highscore): ")

    if startPage == "highscore":
        highScoreMenu(Score(), 10)
    elif startPage == "options":
        optionMenu('single')
    else:
        mainMenu()
    quit()
