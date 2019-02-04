import sys, os.path; sys.path.append(os.path.abspath('..'))

from models import *

from . import *

'''
Fields:
    swimmer,
    distance,
    strokes,
    time_taken,
    age_group,
    season    
'''

class ScoreService:
    def __init__(self):
        # assume this is a database
        self._data_store = [
            {
                'swimmer_id': 1,
                'distance': 3,
                'strokes': 5,
                'time_taken': 1,
                'age_group': 'teenager',
                'season': 'ethiopia_season1_2018'
            },
            {
                'swimmer_id': 2,
                'distance': 3,
                'strokes': 2,
                'time_taken': 6,
                'age_group': 'toddler',
                'season': 'ethiopia_season1_2018'
            },
            {
                'swimmer_id': 1,
                'distance': 4,
                'strokes': 3,
                'time_taken': 2,
                'age_group': 'teenager',
                'season': 'ethiopia_season2_2018'
            }
        ]

    # TODO: Try to integrate a strategy design pattern in here for the fetching algorithm
    def getAllBySeason(season):
        data_entry = filter(lambda entry: entry['season'] == season.getName(), self._data_store)
        
        for entry in data_entry:
            entry['swimmer'] = SwimmerService().getById(entry['swimmer_id'])
            del entry['swimmer_id']
            entry['age_group'] = AgeGroupService().getByName(entry['age_group'])
            entry['season'] = season
        
        return map(lambda entry: Score(**entry), data_entry)


    def getAllBySeasonName(self, season_name):
        data_entry = filter(lambda entry: entry['season'] == season_name, self._data_store)
        
        for entry in data_entry:
            entry['swimmer'] = SwimmerService().getById(entry['swimmer_id'])
            del entry['swimmer_id']
            entry['age_group'] = AgeGroupService().getByName(entry['age_group'])
            entry['season'] = SeasonService().getByName(entry['season'])
        
        return map(lambda entry: Score(**entry), data_entry)
            

    def getAllBySeasonWithAgeGroup(age_group, season):
        data_entry = filter(lambda entry: entry['season'] == season.getName() and entry['age_group'] == age_group.getName(), self._data_store)
        
        for entry in data_entry:
            entry['swimmer'] = SwimmerService().getById(entry['swimmer_id'])
            del entry['swimmer_id']
            entry['age_group'] = AgeGroupService().getByName(entry['age_group'])
            entry['season'] = SeasonService().getByName(entry['season'])
        
        return map(lambda entry: Score(**entry), data_entry)


    def getAllBySeasonWithAgeGroupNames(age_group_name, season_name):
        data_entry = filter(lambda entry: entry['season'] == season_name and entry['age_group'] == age_group_name, self._data_store)
        
        for entry in data_entry:
            entry['swimmer'] = SwimmerService().getById(entry['swimmer_id'])
            del entry['swimmer_id']
            entry['age_group'] = AgeGroupService().getByName(entry['age_group'])
            entry['season'] = SeasonService().getByName(entry['season'])
        
        return map(lambda entry: Score(**entry), data_entry)    