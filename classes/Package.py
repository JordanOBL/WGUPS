from enum import Enum
from classes.Colors import bcolors
from datetime import datetime, time

class Status(Enum):
    AT_HUB = 'At Hub'
    EN_ROUTE = 'En Route'
    DELIVERED = 'Delivered'
    DELAYED = 'Delayed'

class Package:
    def __init__(self, id, address, city, state, zip, deadline, weight, notes):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        if self.notes.strip().split(" ")[0] == "Delayed":
            self.status = Status.DELAYED
        else:
            self.status = Status.AT_HUB
        self.delivery_time = None
        self.truckId = None

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

    def getDeliveryTime(self):
        return self.delivery_time
 
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

    def setCity(self, city):
        self.city = city

    def setState(self, state):
        self.state = state

    def setZip(self, zip):
        self.zip = zip

    def setTruckId(self, truck_id):
        self.truckId = truck_id

    def setSatus(self, status):
        if status == 'En Route':
            self.status = Status.EN_ROUTE
        elif status == 'Delivered':
            self.status = Status.DELIVERED
        elif status == 'At Hub':
            self.status = Status.AT_HUB

    def deliver(self, time, truck_id):
        self.status = Status.DELIVERED
        self.delivery_time = time
          
    def __str__(self):
        color = bcolors.OKGREEN
        if self.status == Status.AT_HUB:
            color = bcolors.OKCYAN
        elif self.status == Status.DELAYED:
            color = bcolors.OKBLUE
        elif self.status == Status.EN_ROUTE:
            color = bcolors.WARNING
        elif self.status == Status.DELIVERED:
            if self.deadline != "EOD":
                time_arr = self.deadline.split(':')
                hour = int(time_arr[0])
                minute = int(time_arr[1].split(' ')[0])
                if self.delivery_time > time(hour, minute):
                    color = bcolors.FAIL
 
        return f'{color}{self.id} | {self.address} | {self.city} | {self.state} | {self.zip} | {self.deadline} | {self.weight} | {self.notes} | {self.status.value} | {self.delivery_time} | Truck-{self.truckId}'



