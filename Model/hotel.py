import json

class Hotel:

    def __init__(self, a_name, a_adress, a_description, a_services, a_apartments):
        self.name = a_name
        self.adress = a_adress
        self.description = a_description
        self.services = a_services
        self.apartments = a_apartments

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, ensure_ascii=False)
