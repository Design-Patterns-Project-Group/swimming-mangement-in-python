from abc import ABC, abstractmethod

class AbstractMainView(ABC):
    
    @abstractmethod
    def prepareGUI(self):
        pass
