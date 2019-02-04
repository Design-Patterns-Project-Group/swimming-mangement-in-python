class Swimmer:
    def __init__(self, swimmer_id, first_name, last_name):
        self._id = swimmer_id
        self._first_name = first_name
        self._last_name = last_name
    
    def getId(self):
        return self._id

    def getFirstName(self):
        return self._first_name
    
    def getLastName(self):
        return self._last_name

    def getFullname(self):
        return " ".join([self.getFirstName(), self.getLastName()])
        