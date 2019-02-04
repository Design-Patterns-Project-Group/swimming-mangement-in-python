import sys, os.path; sys.path.append(os.path.abspath('..'))

from models import *

class SwimmerService:
    def __init__(self):
        # assume this is a database
        self._data_store = [
            {
                'id': 1,
                'first_name' : 'Abebe',
                'last_name' : 'Bekila'
            },
            {
                'id': 2,
                'first_name' : 'Abebe2',
                'last_name' : 'Bekila2'
            },
            {
                'id': 3,
                'first_name' : 'Abebe3',
                'last_name' : 'Bekila3'
            },
            {
                'id': 4,
                'first_name' : 'Abebe4',
                'last_name' : 'Bekila4'
            },
            {
                'id': 5,
                'first_name' : 'Abebe5',
                'last_name' : 'Bekila5'
            }
        ]

    def getById(self, swimmer_id):
        raise NotImplemented()
    
    