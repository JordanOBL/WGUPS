from operator import itemgetter

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
        print(f"package address: {package.address}")
        self.packages[str(package.id)] = package

    def is_full(self):
        return len(self.packages) == self.max_capacity



    def deliver(self, graph, total_miles, time):
        print(f"Creating optimal route for truck {self.id}")
        while len(self.packages) > 0:
            print(len(self.packages))
            next_package = None
            for idx, (package_id, package) in enumerate(self.packages.items()):
                lowest_distance = float('inf')
                distance = graph.get_weight(self.location, package.address)
                if distance < lowest_distance:
                    next_package = package
            self.location = package.address
            self.update_mileage(distance)
            del self.packages[next_package.id]



    def update_mileage(self, distance):
        print(f"new mileage: {self.mileage} + {distance}")
        self.mileage += distance



def create_trucks(num_of_trucks):
    #init trucks
    trucks = []
    for i in range(num_of_trucks):
        trucks.append(Truck(i + 1, 16))
    return trucks

def load_trucks(trucks, packages):
    print("Loading Trucks...")
    truck1_package_list = [13, 14, 15,16, 19,20] #Delivered together
    truck2_package_list = [3, 18, 36, 38] #must be on truck 2
    truck3_package_list = [25, 28, 32] #delayed packaged

    #MUST HAVE ON TRUCK 1
    for package_id in truck1_package_list:
        trucks[0].add_package(packages[str(package_id)])
    #MUST HAVES ON TRUCK 2
    for package_id in truck2_package_list:
        trucks[1].add_package(packages[str(package_id)])
    #MUST HAVES ON TRUCK 3
    for package_id in truck3_package_list:
        trucks[2].add_package(packages[str(package_id)])

    #rest of the packages loaded
    for i in range(1, len(packages)):
        if i not in truck1_package_list and i not in truck2_package_list and i not in truck3_package_list:
            if trucks[0].is_full() == False:
                trucks[0].add_package(packages[str(i)])
                
            elif trucks[1].is_full() == False:
                trucks[1].add_package(packages[str(i)])
                break
            elif trucks[2].is_full() == False:
                trucks[2].add_package(packages[str(i)])
    print("All trucks loaded")
    print(f"truck 1: {len(trucks[0].packages)}")
    print(f"truck 2: {len(trucks[1].packages)}")
    print(f"truck 3: {len(trucks[2].packages)}")

    


