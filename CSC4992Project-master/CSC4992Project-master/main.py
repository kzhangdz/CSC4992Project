import pygame

if __name__ == "__main__":
    "Start at main page, single player, or multiplayer?"
    startPage = input("Enter main, single, multi, or quit: ")

    if startPage == "single":
        import menu
        menu.singlePlayerMenu()
    elif startPage == "multi":
        import menu
        menu.multiPlayerMenu()
    elif startPage == "quit":
        quit()
    else:
        import menu
        menu.mainMenu()
    quit()


    
