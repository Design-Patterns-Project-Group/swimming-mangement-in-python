import sys, os.path

sys.path.append(os.path.abspath('..'))

from models import *

from . import AbstractSeasonService
'''
 self._name = name # Assumption: name is unique. eg. LeagueName_Summer_2018
        self._start = start
    
'''

class SeasonService(AbstractSeasonService):
    def __init__(self):
        # assume this is a database
        self._data_store = [
            {
                'name': 'ethiopia_season1_2018',
                'start': '1/1/2018'
            },
            {
                'name': 'ethiopia_season2_2018',
                'start': '1/5/2018'
            }
        ]

    def getByName(self, season_name):
        data_entry = list(filter(lambda entry: entry['name'] == season_name, self._data_store))
        
        try:
            data_entry = data_entry[0]
            
        except:
            raise Exception('could not find a season by that name')

        return Season(**data_entry)

    def getAll(self):
        return map(lambda entry: Season(**entry), self._data_store)