import tkinter as tk

#define default fonts
TITLE_FONT = ('Verdana', 12)

class HomeMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Memory Game", font=TITLE_FONT)
        label.pack(pady=10, padx=10)

        #create single player button
        singlePlayerButton = tk.Button(self, text="Single Player",
                                       command=lambda: controller.showFrame(SinglePlayerPage))
        singlePlayerButton.pack()

        #create two player button
        twoPlayerButton = tk.Button(self, text="Two Player")
