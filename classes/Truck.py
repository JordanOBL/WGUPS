from datetime import datetime, timedelta, time

class Truck:
    MAX_CAPACITY = 16
    SPEED = 18
    HUB = "4001 South 700 East"
    DAY = 10
    MONTH = 5
    YEAR = 2025


    def __init__(self, id, start_time=datetime(2025, 5, 10, 8, 0)):
        #Truck Number
        self.id = id
        self.max_capacity = self.MAX_CAPACITY
        self.location = self.HUB
        self.packages = {}
        self.mileage = 0.0
        self.speed = self.SPEED
        #dateTime(year, month, day, hour, minute)
        self.start_time = start_time
        self.current_time = self.start_time
        

    
    def add_package(self, package):
        self.packages[package.getID()] = package
        package.setTruckId(self.id)

    def is_full(self):
        return len(self.packages) == self.max_capacity
    
    def update_mileage(self, distance):
        self.mileage += distance

    def update_time(self, distance):
        time = distance / self.speed
        self.current_time = self.current_time + timedelta(hours=time)

    def return_to_hub(self, graph):
        distance = graph.get_weight(self.location, self.HUB)
        self.update_mileage(distance)
        self.location = self.HUB



    def deliver(self, graph, end_time=datetime(2025, 5, 10, 23, 59), start_time=datetime(2025, 5, 10, 8, 0) ):
        self.current_time = start_time
        if self.id == 3 and start_time.time() < time(9,5):
            self.current_time = datetime(2025, 5, 10, 9, 5)
        #print(f"Delivering optimal route for truck {self.id}...")
      
        for package in self.packages.values():  
            if package.getStatus() == 'Delayed' and end_time.time() > time(9,5):
                package.setSatus('En Route')
                
            if package.getStatus() != 'Delayed' and self.current_time.time() < end_time.time():
                package.setSatus('En Route')
        
        #Loop through all packages
        #Get closest to current location
        while len(self.packages) > 0 and self.current_time.time() < end_time.time():
            curr_package = None
            delivery_distance = None
            lowest_delivery_distance = float('inf')
            for package in self.packages.values():
            
                delivery_distance = graph.get_weight(self.location, package.getAddress())
                if package.getID() == 9 and self.current_time.time() < datetime(self.YEAR,self.MONTH, self.DAY, 10, 20).time():
                    continue
                if self.packages.get(9, None) != None and self.packages.get(9).getAddress() != '410 S State St' and self.current_time.time() >= datetime(self.YEAR,self.MONTH, self.DAY, 10, 20).time():
                    self.packages[9].setAddress("410 S State St")
                    self.packages[9].setCity("Salt Lake City")
                    self.packages[9].setState("UT")
                    self.packages[9].setZip("84111")
                if package.getID() == 6 or package.getID() == 25:
                    curr_package = package
                    lowest_delivery_distance = delivery_distance
                    break
                elif delivery_distance < lowest_delivery_distance:
                    curr_package = package
                    lowest_delivery_distance = delivery_distance
            self.location = curr_package.getAddress()
            self.update_mileage(lowest_delivery_distance)
            self.update_time(lowest_delivery_distance)
            if self.current_time.time() < end_time.time():
                curr_package.deliver(self.current_time.time(), self.id)
                del self.packages[int(curr_package.getID())]
        
        if self.id == 1:
            self.return_to_hub(graph)
        #print(f"All packages delivered: {float(self.mileage)} miles")
        return self

    

def create_trucks(num_of_trucks):
    #init trucks
    trucks = []
    for i in range(num_of_trucks):
        trucks.append(Truck(i + 1))
    return trucks

def load_trucks(trucks, packages):
    #print("\nLoading Trucks...")
    truck1_package_list = [13, 14, 15,16,20] #Delivered together
    truck2_package_list = [3, 18, 36, 38, 37, 11, 5, 8, 22, 23] #must be on truck 2
    truck3_package_list = [28,9, 32, 25, 6, 12] #delayed packaged

    #MUST HAVE ON TRUCK 1
    for package_id in truck1_package_list:
        trucks[0].add_package(packages.search(package_id))
    #MUST HAVES ON TRUCK 2
    for package_id in truck2_package_list:
        trucks[1].add_package(packages.search(package_id))
    #MUST HAVES ON TRUCK 3
    for package_id in truck3_package_list:
        trucks[2].add_package(packages.search(package_id))

    #rest of the packages loaded
    for i in range(1,packages.getCount()):
        if i not in truck1_package_list and i not in truck2_package_list and i not in truck3_package_list:
            if trucks[0].is_full() == False:
                trucks[0].add_package(packages.search(i))
            elif trucks[1].is_full() == False:
                trucks[1].add_package(packages.search(i))
            elif trucks[2].is_full() == False:
                trucks[2].add_package(packages.search(i))
    #print("All trucks successfully loaded!\n")

    


