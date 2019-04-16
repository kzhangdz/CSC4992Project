import pygame

if __name__ == "__main__":
    while True:
        "Start at main page, single player, or multiplayer?"
        startPage = input("Enter main, single, multi, or quit: ")
        try:
            if startPage == "main":
                import menu
                menu.mainMenu()
            elif startPage == "single":
                import menu
                menu.singlePlayerMenu()
            elif startPage == "multi":
                import menu
                menu.multiPlayerMenu()
            elif startPage == "quit":
                quit()
            else:
                raise ValueError('Your input was not one of the options')
        except ValueError as err:
            print('Start over')
    
    quit()


    
