from classes.UI import UI
from classes.Package import Package
from classes.Truck import Truck, create_trucks, load_trucks
from classes.Graph import Graph
from classes.HashTable import load_create_packages_hash_table
from datetime import datetime

def main():
    #init ui
    ui = UI()
    print("Welcome to WGUPS!\n")
    #Read in Package info
    packages = load_create_packages_hash_table("/Users/jordan/Documents/WGU/course_work/DA2/wgups/assets/packageData.csv")

    #init graph
    graph = Graph()
    graph.build_graph('/Users/jordan/Documents/WGU/course_work/DA2/wgups/assets/WGUPS Distance CSV Table.csv')


    #create Trucks
    trucks = create_trucks(3)

    #load packages
    load_trucks(trucks,packages)
    
    #Run Program
    running = True
    while running:
        user_end_time = ui.print_menu()
        trucks[0].deliver(graph, user_end_time)
        trucks[1].deliver(graph, user_end_time)
        trucks[2].deliver(graph, user_end_time, trucks[0].current_time)
        print(f'total miles: {trucks[0].mileage + trucks[1].mileage + trucks[2].mileage}')
        ui.print_packages(packages)

        



if __name__ == "__main__":
    main()

