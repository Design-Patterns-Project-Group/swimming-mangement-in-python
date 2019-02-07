from . import AbstractMainView
from tkinter import *

# TODO : implement the Tkinter GUI

class MainView(AbstractMainView):
    def __init__(self, controller):
        self.prepareGUI()
    
    def prepareGUI(self):
        self._root = Tk()
        self._root.mainloop()