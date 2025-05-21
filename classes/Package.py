from enum import Enum
from classes.HashTable import HashTable

def read_create_packages(filename):
    #open file (CSV)
    #Id, Address, City, State, Zip, Deadline, Weight, Notes
    file = open(filename, "r")
    lines = file.readlines()
    packages = HashTable(len(lines))
    file.seek(0)
    for line in file:
        line = line.strip().split(",")
        newPackage = Package(int(line[0]),line[1].strip(),line[2],line[3],line[4],line[5],line[6],line[7])
        packages.insert(newPackage)

    file.close()
    return packages



class Status(Enum):
    AT_HUB = 'At Hub'
    EN_ROUTE = 'En Route'
    DELIVERED = 'Delivered'

class Package:
    def __init__(self, id, address, city, state, zip, deadline, weight, notes=''):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = Status.AT_HUB

    def getStatus(self):
        return self.status

    def getID(self):
        return self.id

    def getDeadline(self):
        return self.deadline

    def getWeight(self):
        return self.weight

    def getNotes(self):
        return self.notes

    def getAddress(self):
        return self.address

    def getCity(self):
        return self.city

    def getState(self):
        return self.state

    def getZip(self):
        return self.zip
 
    def setID(self, id):
        self.id = id

    def setDeadline(self, deadline):
        self.deadline = deadline

    def setWeight(self, weight):
        self.weight = weight

    def setNotes(self, notes):
        self.notes = notes

    def setAddress(self, address):
        self.address = address

    def setSatus(self, status):
        self.status = status

    def deliver(self):
        self.status = Status.DELIVERED
        print(f'Package {self.id}: DELIVERED')


