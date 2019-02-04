import sys, os.path; sys.path.append(os.path.abspath('..'))

from models import *

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
                'age_group': 'teenager',
                'season': 'ethiopia_season1_2018'
            },
            {
                'swimmer_id': 1,
                'distance': 4,
                'strokes': 3,
                'time_taken': 2,
                'age_group': 'teenager',
                'season': 'ethiopia_season1_2018'
            }
        ]

    def getAllBySeason(season):
        raise NotImplemented()

    def getAllBySeasonName(season_name):
        raise NotImplemented()

    def getAllBySeasonWithAgeGroup(age_group, season):
        raise NotImplemented()

    def getAllBySeasonWithAgeGroupNames(age_group_name, season_name):
        raise NotImplemented()
    