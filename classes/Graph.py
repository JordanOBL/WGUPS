import csv
class Graph:
    def __init__(self):
        #maybe dont need to store nodes(hubnames) after edges are created
        self.nodes = []
        self.edges = {}


    def build_graph(self, filename):
        print("Creating Graph...")

        with open(filename, mode='r') as csvfile:
            distanceReader = csv.reader(csvfile) #open CSV file for reading
            next(distanceReader) #Skip cursor past top row holding addresses
            distanceReader = list(distanceReader) #turn csv rows into list object

            for i in range(len(distanceReader)): # save hub names to iterate over
                hub = distanceReader[i][0]
                self.nodes.append(hub.strip())

            for i in range(len(self.nodes)): #create edges as dict for O(1) lookup -- key: set{hubname, hubname}, value: weight
                for j in range(i+1, len(self.nodes)):
                    weight = distanceReader[j][i + 1]
                    if weight:
                        self.edges[frozenset({self.nodes[i],self.nodes[j]})] = float(weight)
        print("Graph created!...")
        
        print(self.edges.items())

    def get_weight(self, loc1, loc2):
        if loc1 == loc2:
            return float(0)
        return self.edges[frozenset({loc1, loc2})]

