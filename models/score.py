class Score:
    def __init__(
                self,
                swimmer,
                distance,
                strokes,
                time_taken,
                age_group,
                season
            ):
        self._swimmer = swimmer
        self._distance = distance
        self._stokes = strokes
        self._time_taken = time_taken
        self._age_group = age_group
        self._season = season
        # TODO: validate age of swimmer adheres to the specs. of the age_group
        # TODO: assert values for type checking
    
    def getSwimmer(self):
        return self._swimmer
    
    def getDistance(self):
        return self._distance

    def getStokes(self):
        return self._stokes
    
    def getTimeTaken(self):
        return self._time_taken
    
    def getAgeGroup(self):
        return self._age_group

    def getSeason(self):
        return self._season
