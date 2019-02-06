from abc import ABC, abstractmethod

class AbstractSwimmerService(ABC):

    @abstractmethod   
    def getById(self, swimmer_id):
        pass
