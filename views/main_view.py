from . import AbstractMainView
from tkinter import *

# TODO : implement the Tkinter GUI

class MainView(AbstractMainView):
    def __init__(self, services):
        self._score_service = services.ScoreService()
        self._season_service = services.SeasonService()
        self.prepareGUI()
    
    def prepareGUI(self):
        self._root = Tk()
        self._root.mainloop()