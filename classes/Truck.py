class Truck:
    MAX_CAPACITY = 16
    SPEED = 18
    HUB = "4001 South 700 East"

    def __init__(self, id, capacity):
        #Truck Number
        self.id = id
        self.max_capacity = self.MAX_CAPACITY
        self.location = self.HUB
        self.packages = {}
        self.mileage = 0.0
        self.speed = self.SPEED

    
    def add_package(self, package):
        self.packages[package.getID()] = package

    def is_full(self):
        return len(self.packages) == self.max_capacity



    def deliver(self, graph, total_miles, time):
        print(f"Delivering optimal route for truck {self.id}...")
        #Loop through all packages
        #Get closest to current location
        while len(self.packages) > 0:
            curr_package = None
            distance = None
            lowest_distance = float('inf')
            for package in self.packages.values():
                distance = graph.get_weight(self.location, package.getAddress())
                if distance < lowest_distance:
                    curr_package = package
                    lowest_distance = distance
            self.location = curr_package.getAddress()
            self.update_mileage(lowest_distance)
            curr_package.deliver()
            del self.packages[curr_package.getID()]
        print(f"All packages delivered: {float(self.mileage)} miles")
        return self.mileage

    def update_mileage(self, distance):
        self.mileage += distance

def create_trucks(num_of_trucks):
    #init trucks
    trucks = []
    for i in range(num_of_trucks):
        trucks.append(Truck(i + 1, 16))
    return trucks

def load_trucks(trucks, packages):
    print("\nLoading Trucks...")
    truck1_package_list = [13, 14, 15,16, 19,20] #Delivered together
    truck2_package_list = [3, 18, 36, 38] #must be on truck 2
    truck3_package_list = [25, 28, 32] #delayed packaged

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
    print("All trucks successfully loaded!\n")

    


