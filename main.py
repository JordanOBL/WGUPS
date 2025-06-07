from classes.UI import UI
from classes.Package import Package
from classes.Truck import Truck, create_trucks, load_trucks
from classes.Graph import Graph
from classes.HashTable import load_create_packages_hash_table
from datetime import datetime

def main():
    #init ui
    ui = UI()
    print("Welcome to WGUPS!")
    #Read in Package info
    
    
    #Run Program
    running = True
    while running:
        packages = load_create_packages_hash_table("./assets/packageData.csv")

        #init graph
        graph = Graph()
        graph.build_graph('./assets/WGUPS Distance CSV Table.csv')

        #print menu
        user_end_time = ui.print_menu()
        
        #create Trucks
        trucks = create_trucks(3)

        #load packages
        load_trucks(trucks,packages)

        #Deliver Packages
        trucks[0].deliver(graph, user_end_time)
        trucks[1].deliver(graph, user_end_time)
        trucks[2].deliver(graph, user_end_time, trucks[0].current_time)

        #print results
        ui.print_packages(packages)
        ui.print_total_miles_driven(trucks)
        
if __name__ == "__main__":
    main()

