class AgeGroup:
    def __init__(self, name, min_age, max_age):
        self._name = name
        self._min_age = min_age
        self._max_age = max_age
    
    def getName(self):
        return self._name
        
    def getMinAge(self):
        return self._min_age
    
    def getMaxAge(self):
        return self._max_age

    def verifySwimmer(self, swimmer):
        raise NotImplemented('yet :)')
    