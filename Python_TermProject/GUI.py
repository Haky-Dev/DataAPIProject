from tkinter import *

class Cell(Label) : 
    def __init__(self, container):
        self.xImage = PhotoImage(file = "image/cross.gif")
        self.oImage = PhotoImage(file = "image/circle.gif")
        self.eImage = PhotoImage(file = "image/empty.gif")

        Label.__init__(self, container, image = self.eImage)
        self.data = ' '
        self.bind("<Button-1>", self.click)

    def click(self, event):
       pass
