import pygame

pygame.init()

#declare size
displayWidth = 800
displayHeight = 600

#declare colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

#test image
#testImg = pygame.image.load('back_button.gif')

# set window size
display = pygame.display.set_mode((displayWidth, displayHeight))

#set window name
pygame.display.set_caption('Memory Game')

#set up clock
clock = pygame.time.Clock()

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

        pygame.display.update()

        #set frame rate
        clock.tick(30)

if __name__ == "__main__":
    gameLoop()
    pygame.quit()
    quit()


    
