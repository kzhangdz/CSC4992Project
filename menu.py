import tkinter as tk
#from homemenu import HomeMenu

#define default fonts
TITLE_FONT = ('Verdana', 12)

class Menu(tk.Tk):

    def __init__(self, *args, **kwargs):
        # initialize tkinter
        tk.Tk.__init__(self, *args, **kwargs)

        # Initialize window
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #create menu frames/pages
        self.frames = {}

        #add new frames in this for loop
        for eachFrame in (HomeMenu, SinglePlayerMenu):
            frame = eachFrame(container, self)
            self.frames[eachFrame] = frame
            frame.grid(row=0, column = 0, sticky="nsew")

        self.showFrame(HomeMenu)

    def showFrame(self, controller):
        '''display function to show menu frames'''
        frame = self.frames[controller]
        frame.tkraise() #send passed frame to front

class HomeMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Memory Game", font=TITLE_FONT)
        label.pack(pady=10, padx=10)

        #create single player button
        singlePlayerButton = tk.Button(self, text="Single Player",
                                       command=lambda: controller.showFrame(SinglePlayerMenu))
        singlePlayerButton.pack()

        #create two player button
        #FIXME: add command to show frame
        twoPlayerButton = tk.Button(self, text="Two Player")
        twoPlayerButton.pack()

class SinglePlayerMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Single Player", font=TITLE_FONT)
        label.pack(pady=10, padx=10)

        #create back button
        backButton = tk.Button(self, text="Back",
                                       command=lambda: controller.showFrame(HomeMenu))
        backButton.pack()
        

if __name__ == "__main__":
    menus = Menu()
    menus.mainloop()





    
