from abc import ABC, abstractmethod

class AbstractScoreService(ABC):

    @abstractmethod
    def getAllBySeason(self, season):
        pass

    @abstractmethod
    def getAllBySeasonName(self, season_name):            
        pass
        
    @abstractmethod
    def getAllBySeasonWithAgeGroup(self, age_group, season):
        pass

    @abstractmethod
    def getAllBySeasonWithAgeGroupNames(self, age_group_name, season_name):
        pass
