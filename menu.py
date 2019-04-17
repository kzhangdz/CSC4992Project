'''file that stores all menu pages'''


from pygameEnvironment import *
from constant import *
from card import *
from cardDeck import *
from checkbox import *
from inputBox import *
from score import *
from textPrinter import TextPrinter
import os
import copy

pygame.mixer.music.load('Netherplace.mp3')

from statistics import *

stats = Statistics() #global

def mainMenu():
    #buttons
    singleImgDirectory = os.path.join(os.path.abspath(os.curdir), 'images', 'menu', 'button_single-player.png')
    multiImgDirectory = os.path.join(os.path.abspath(os.curdir), 'images', 'menu', 'button_two-player.png')
    imgDirectoryOptions = os.path.join(os.path.abspath(os.curdir), 'images', 'menu', 'hamburger.png')
    
    singlePlayerButton = ImageButton((DISPLAY_WIDTH*0.33, DISPLAY_HEIGHT*0.5), singleImgDirectory)
    multiPlayerButton = ImageButton((DISPLAY_WIDTH*0.66, DISPLAY_HEIGHT*0.5), multiImgDirectory)

    imgDirectory = os.path.join(os.path.abspath(os.curdir), 'images', 'menu', 'button_two-player.png')
    multiPlayerButton = ImageButton((DISPLAY_WIDTH*0.66, DISPLAY_HEIGHT*0.5), imgDirectory)

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

        gameDisplay.fill(FOREST_GREEN)  #FOREST_GREEN
        singlePlayerButton.draw(gameDisplay)
        multiPlayerButton.draw(gameDisplay)

        TextPrinter.displayTitle("Bela Memoro") # TextPrinter.displayText("Bela Memoro", (DISPLAY_WIDTH*0.15, DISPLAY_HEIGHT*0.09), 30, BLACK)
        TextPrinter.displayText("A Memory Game", (DISPLAY_WIDTH*0.5, DISPLAY_HEIGHT*0.3), 30, BLACK)
        optionsButton.draw(gameDisplay)


        pygame.display.update()

        #set frames per second
        clock.tick(FPS)

def singlePlayerMenu():
    global stats
    #buttons

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
            if optionsButton.isClicked(event):
                optionMenu('single')

            gameDisplay.fill(FOREST_GREEN) # FOREST_GREEN
            backButton.draw(gameDisplay)
            optionsButton.draw(gameDisplay)

            gameplay10Button.draw(gameDisplay)
            gameplay14Button.draw(gameDisplay)
            gameplay18Button.draw(gameDisplay)

            
            TextPrinter.displayText("Single Player", (DISPLAY_WIDTH*0.50, DISPLAY_HEIGHT*0.3), 75, BLACK)
            TextPrinter.displayText("Bela Memoro", (DISPLAY_WIDTH*0.85, DISPLAY_HEIGHT*0.09), 30, BLACK)

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

            gameDisplay.fill(FOREST_GREEN) #FOREST_GREEN
            backButton.draw(gameDisplay)

            TextPrinter.displayText("Statistics", (DISPLAY_WIDTH*0.50, DISPLAY_HEIGHT*0.15), 75, BLACK) #changed-ibrahim
            #TextPrinter.displayText(str(stats.CardsClicked), (DISPLAY_WIDTH*0.30, DISPLAY_HEIGHT*0.35), 50, FOREST_GREEN)
            stats.displayStats() #IBRAHIM DISPLAY doesnt work

            pygame.display.update()

            #set frames per second
            clock.tick(FPS)

def multiPlayerMenu():
    global stats
    #buttons
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
            
            if optionsButton.isClicked(event):
                optionMenu('multi')
                
            if gameplay10Button.isClicked(event):
                stats.raiseGamesPlayed()
                print(stats.GamesPlayed)
                gameplayMenu2(10)
            if gameplay14Button.isClicked(event):
                stats.raiseGamesPlayed()
                print(stats.GamesPlayed)
                gameplayMenu2(14)
            if gameplay18Button.isClicked(event):
                stats.raiseGamesPlayed()
                print(stats.GamesPlayed)
                gameplayMenu2(18)
                

            gameDisplay.fill(FOREST_GREEN) #FOREST_GREEN
            backButton.draw(gameDisplay)

            gameplay10Button.draw(gameDisplay)
            gameplay14Button.draw(gameDisplay)
            gameplay18Button.draw(gameDisplay)
			
            TextPrinter.displayText("Multi Player", (DISPLAY_WIDTH*0.50, DISPLAY_HEIGHT*0.3), 75, BLACK)


            TextPrinter.displayText("Bela Memoro", (DISPLAY_WIDTH*0.85, DISPLAY_HEIGHT*0.09), 30, BLACK)
            optionsButton.draw(gameDisplay)


            #test checkbox
            pygame.display.update()

            #set frames per second
            clock.tick(FPS)

def gameplayMenu(numCards):
    global stats
    #needs to pass in parameters that define game state
    #alternatively, options menu should open in a new frame above the current one

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

            '''if backButton.isClicked(event):
                #call main menu
                singlePlayerMenu()'''
            if optionsButton.isClicked(event):
                optionMenu('gameplay')


            #switch card state if clicked
            for card in currentDeck.deck:
                if card.isClicked(event):
                    stats.raiseCardsClicked()
                    print(stats.CardsClicked)  #testing
                    print(card.cardImageDirectories[card.status], card.position)
                    card.switchStatus()

            #background

            gameDisplay.fill(FOREST_GREEN)
            #backButton.draw(gameDisplay)
            optionsButton.draw(gameDisplay)

            currentScore.displayScore()
            currentScore.displayMultiplier()
            TextPrinter.displayText("Bela Memoro", (DISPLAY_WIDTH*0.15, DISPLAY_HEIGHT*0.09), 30, BLACK)

            #show cards
            for card in currentDeck.deck:
                card.showCard()

            #check state of deck to see if cards should be flipped
            currentDeck.checkDeckStatus(currentScore, stats) #checks for cards matched

            pygame.display.update()

            #if all cards face up, send user to results screen
            if currentDeck.checkAllFaceUp():
                resultMenu(currentScore, "Congratulations!", numCards, "single")

            #set frames per second
            clock.tick(FPS)
			
def gameplayMenu2(numCards):
    global stats
    #needs to pass in parameters that define game state
    #alternatively, options menu should open in a new frame above the current one
    turn = 0
    clickCount = 0
    #declare button
    #backButton = Button((DISPLAY_WIDTH*0.1, DISPLAY_HEIGHT*0.1), (80, 40), RED, "Back")
    #imgDirectoryOptions = os.path.join(os.path.abspath(os.curdir), 'images', 'menu', 'hamburger.png')
    #optionsButton = ImageButton((DISPLAY_WIDTH * 0.9, DISPLAY_HEIGHT * 0.9), imgDirectoryOptions)

    #declare card deck
    #FIXME: refactor use different themes
    currentDeck = CardDeck("theme1", numCards)

    #declare score
    currentScore = MultiplayerScore()
    
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

            #if backButton.isClicked(event):
                #call main menu
                #multiPlayerMenu()
                     
            if optionsButton.isClicked(event):
                optionMenu('gameplay')

            #switch card state if clicked
            for card in currentDeck.deck:
                if card.isClicked(event):
                    clickCount += 1
                    stats.raiseCardsClicked()
                    print(stats.CardsClicked) 
                    print(card.cardImageDirectories[card.status], card.position)
                    print("Turn:", turn, " Clicks:", clickCount)
                    card.switchStatus()

            #background
            gameDisplay.fill(FOREST_GREEN)
            #backButton.draw(gameDisplay)
            optionsButton.draw(gameDisplay)
            currentScore.displayScore()
            currentScore.displayMultiplier()
            #currentScore.displayScore2()
            #currentScore.displayMultiplier2()

            #show cards
            for card in currentDeck.deck:
                card.showCard() 
            
            #check state of deck to see if cards should be flipped
            currentDeck.checkDeckStatus2(currentScore, turn, stats)
            
            pygame.display.update()

            if clickCount >= 2:
                if turn == 0:
                    turn=1
                    clickCount = 0
                elif turn == 1:
                    turn=0
                    clickCount = 0
            #if all cards face up, send user to results screen
            if currentDeck.checkAllFaceUp():
                if currentScore.score > currentScore.score2:
                    resultMenu(currentScore, "Player 1 Wins!", numCards, "multi")
                elif currentScore.score < currentScore.score2:
                    resultMenu(currentScore, "Player 2 Wins!", numCards, "multi")
                else:
                    resultMenu(currentScore, "Players Tied!", numCards, "multi")

            #set frames per second
            clock.tick(FPS)
            
def resultMenu(score, displayMessage, numCards, mode):
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
            gameDisplay.fill(FOREST_GREEN) #FOREST_GREEN

            TextPrinter.displayText(displayMessage, (DISPLAY_WIDTH*0.5, DISPLAY_HEIGHT*0.4), 75, BLACK) #changed-ibrahim

            score.displayScore()

            menuButton.draw(gameDisplay)


            if mode == "single":
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

                try:
                    if len(userName) > 10:
                        raise ValueError('Data should not exceed 10 characters. Length was ()'.format(len(userName)))
                    print(userName)
                    saveScore(userName, score, numCards)

                    highScoreDisplayMenu(numCards)
                except ValueError as err:
                    print('Did not save user. Character length exceeded.')


            if highScoreDisplayButton.isClicked(event):
                highScoreDisplayMenu(numCards)
            if menuButton.isClicked(event):
                #call main menu
                mainMenu()

            #background
            gameDisplay.fill(FOREST_GREEN) #FOREST_GREEN



            TextPrinter.displayText("Enter your name", (DISPLAY_WIDTH*0.5, DISPLAY_HEIGHT*0.4), 75, BLACK)
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
            gameDisplay.fill(FOREST_GREEN) #FOREST_GREEN

            TextPrinter.displayText(highScoreLabel, (DISPLAY_WIDTH*0.5, DISPLAY_HEIGHT*0.1), 65, BLACK) #changed-ibrahim

            scoreYPos = DISPLAY_HEIGHT * 0.2
            for row in scoreList:
                #display name
                TextPrinter.displayText(str(row[0]), (nameXPos, scoreYPos), 30, BLACK) #changed-ibrahim
                #display score
                TextPrinter.displayText(str(row[1]), (scoreXPos, scoreYPos), 30, BLACK) #changed-ibrahim
                #increase position counter
                scoreYPos += DISPLAY_HEIGHT * 0.05

            menuButton.draw(gameDisplay)

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
    # button images
    imgDirectoryCredits = os.path.join(os.path.abspath(os.curdir), 'images', 'menu', 'button_credits.png')
    imgDirectoryInstructions = os.path.join(os.path.abspath(os.curdir), 'images', 'menu', 'instructions.png')
    imgDirectoryStatistics = os.path.join(os.path.abspath(os.curdir), 'images', 'menu', 'stats.png')
    imgDirectoryTrueCheckbox = os.path.join(os.path.abspath(os.curdir),'images', 'menu', 'checkbox_true.png')
    imgDirectoryFalseCheckbox = os.path.join(os.path.abspath(os.curdir),'images', 'menu', 'checkbox_false.png')

    # scaled images
    instruction_icon = pygame.image.load(imgDirectoryInstructions)
    instruction_icon = pygame.transform.scale(instruction_icon, (math.floor(DISPLAY_WIDTH * 0.35), math.floor(DISPLAY_HEIGHT * 0.3)))
    stat_icon = pygame.image.load(imgDirectoryStatistics)
    stat_icon = pygame.transform.scale(stat_icon, (math.floor(DISPLAY_WIDTH * 0.1), math.floor(DISPLAY_HEIGHT * 0.15)))
    trueCheckboxIcon = pygame.image.load(imgDirectoryTrueCheckbox)
    falseCheckboxIcon= pygame.image.load(imgDirectoryFalseCheckbox)

# declared buttons
    creditsButton = ImageButton((DISPLAY_WIDTH * 0.5, DISPLAY_HEIGHT * 0.65), imgDirectoryCredits)
    instructionsButton = ImageButton((DISPLAY_WIDTH * 0.5, DISPLAY_HEIGHT * 0.5), imageFile = instruction_icon)
    statisticsButton = ImageButton((DISPLAY_WIDTH * 0.09, DISPLAY_HEIGHT * 0.9), imageFile = stat_icon)
    musicCheckbox = Checkbox((DISPLAY_WIDTH*0.55, DISPLAY_HEIGHT*0.55))
    trueCheckboxBtn = ImageButton((DISPLAY_WIDTH * 0.55, DISPLAY_HEIGHT * 0.55), imageFile = trueCheckboxIcon)
    falseCheckboxBtn = ImageButton((DISPLAY_WIDTH * 0.55, DISPLAY_HEIGHT * 0.55), imageFile = falseCheckboxIcon)
    musicBtn = 0
    if pygame.mixer.music.get_busy() == False:
        musicBtn = falseCheckboxBtn
    elif pygame.mixer.music.get_busy() == True:
        musicBtn = trueCheckboxBtn
# cancel gameplay
    imgDirectoryClose = os.path.join(os.path.abspath(os.curdir), 'images', 'menu', 'button_x.png')	# 'cancel_game.png'
    closeButton = ImageButton(bottom_right, imgDirectoryClose)

    running = True
# keeps page open
    while running:
        # display info
        gameDisplay.fill(FOREST_GREEN)
        TextPrinter.displayText("Options", (DISPLAY_WIDTH*0.50, DISPLAY_HEIGHT*0.3), 75, BLACK)
        TextPrinter.displayText("Bela Memoro", (DISPLAY_WIDTH*0.85, DISPLAY_HEIGHT*0.09), 30, BLACK)
        TextPrinter.displayText("Music", (DISPLAY_WIDTH*0.45, DISPLAY_HEIGHT*0.55), 30, BLACK)

        backButton.draw(gameDisplay)
        creditsButton.draw(gameDisplay)
        instructionsButton.draw(gameDisplay)
        statisticsButton.draw(gameDisplay)
        #musicCheckbox.draw(gameDisplay)
        musicBtn.draw(gameDisplay)

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
            if musicBtn.isClicked(event):
                if pygame.mixer.music.get_busy() == True:
                    pygame.mixer.music.stop()
                    musicBtn = falseCheckboxBtn
                elif pygame.mixer.music.get_busy() == False:
                    pygame.mixer.music.play(-1)
                    musicBtn = trueCheckboxBtn
            if statisticsButton.isClicked(event):
                statisticsMenu()
            '''if musicCheckbox.isClicked(event):
                musicCheckbox.switchState()
                if pygame.mixer.music.get_busy() == True:
                    pygame.mixer.music.stop()
                elif pygame.mixer.music.get_busy() == False:
                    pygame.mixer.music.play(-1)
              '''                  
        pygame.display.update()
        clock.tick(FPS)
	#pygame.display.update()
	#clock.tick(FPS)

if __name__ == "__main__":
    startPage = input("Choose start page (main, highscore): ")

    if startPage == "highscore":
        highScoreMenu(Score(), 10)
    elif startPage == "options":
        optionMenu('single')
    else:
        mainMenu()
    quit()
