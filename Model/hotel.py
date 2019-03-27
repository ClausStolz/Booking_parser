import json

class Hotel:

    def __init__(self, aName, aAdress, aDescription, aServices, aApartments):
        self.Name = aName
        self.Adress = aAdress
        self.Description = aDescription
        self.Services = aServices
        self.Apartments = aApartments

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, ensure_ascii=False)
