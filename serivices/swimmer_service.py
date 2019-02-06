import sys, os.path

sys.path.append(os.path.abspath('..'))

from models import *

from .abstract_swimmer_service import AbstractSwimmerService

class SwimmerService(AbstractSwimmerService):
    def __init__(self):
        # assume this is a database
        self._data_store = [
            {
                'swimmer_id': 1,
                'first_name' : 'Abebe',
                'last_name' : 'Bekila'
            },
            {
                'swimmer_id': 2,
                'first_name' : 'Abebe2',
                'last_name' : 'Bekila2'
            },
            {
                'swimmer_id': 3,
                'first_name' : 'Abebe3',
                'last_name' : 'Bekila3'
            },
            {
                'swimmer_id': 4,
                'first_name' : 'Abebe4',
                'last_name' : 'Bekila4'
            },
            {
                'swimmer_id': 5,
                'first_name' : 'Abebe5',
                'last_name' : 'Bekila5'
            }
        ]

    def getById(self, swimmer_id):
        data_entry = list(filter(lambda entry: entry['swimmer_id'] == swimmer_id, self._data_store))
        
        try:
            data_entry = data_entry[0]
            
        except:
            raise Exception('could not find a swimmer by that id')

        return Swimmer(**data_entry)    
