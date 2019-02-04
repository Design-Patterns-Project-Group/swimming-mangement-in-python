import sys, os.path; sys.path.append(os.path.abspath('..'))

from models import *

class SwimmerService:
    def __init__(self):
        # assume this is a database
        self._data_store = [
            {
                'id': 1,
                '' : 13,
                'max_age' : 18
            },
            {
                'name': 'toddler',
                'min_age' : 1,
                'max_age' : 5
            },
            {
                'name': 'youth',
                'min_age' : 18,
                'max_age' : 25
            }
        ]

    def getByName(self, group_name):
        data_entry = filter(lambda entry: entry['name'] == group_name, self._data_store)
        
        try:
            data_entry = data_entry[0]
            if not data_entry: raise
        except:
            raise Exception('could not find an age group by that name')

        return AgeGroup(**data_entry)
