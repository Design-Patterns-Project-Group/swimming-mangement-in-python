from abc import ABC, abstractmethod

class AbstractSeasonService(ABC):

    @abstractmethod
    def getByName(self, season_name):
        pass

    @abstractmethod
    def getAll(self):
        pass