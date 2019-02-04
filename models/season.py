class Season:
    def __init__(self, name, start):
        self._name = name # Assumption: name is unique. eg. LeagueName_Summer_2018
        self._start = start
    
    def getName(self):
        return self._name

    def getStartingTime(self):
        # TODO: time formatting
        return self._start