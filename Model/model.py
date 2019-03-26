
from bs4 import BeautifulSoup
import json
import urllib3

class Apartment:

    def __init__(self, aName, aCapacity, aBed_types):
        self.Name = aName
        self.Capacity = aCapacity
        self.Bed_types = aBed_types


class Hotel:

    def __init__(self, aName, aAdress, aDescription, aServices, aApartment):
        self.Name = aName
        self.Adress = aAdress
        self.Description = aDescription
        self.Services = aServices
        self.Apartment = aApartment
