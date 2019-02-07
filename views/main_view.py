from . import AbstractMainView
from tkinter import *

# TODO : implement the Tkinter GUI

class MainView(AbstractMainView):
    def __init__(self, score_service, season_service):
        self._score_service = score_service
        self._season_service = season_service
        self.prepareGUI()
    
    def prepareGUI(self):
        self._root = Tk()
        self._root.mainloop()