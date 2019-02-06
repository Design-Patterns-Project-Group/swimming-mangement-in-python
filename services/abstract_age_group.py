from abc import ABC, abstractmethod

class AbstractAgeGroupService(ABC):
    
    @abstractmethod
    def getByName(self, group_name):
        pass