from classes.UI import UI
from classes.Package import Package, read_create_packages
from classes.Truck import Truck, create_trucks, load_trucks
from classes.Graph import Graph


def main():
    #init ui
    ui = UI()
    print("Welcome to WGUPS!")
    #Read in Package info
    packages = read_create_packages("/Users/jordan/Documents/WGU/course_work/DA2/wgups/assets/packageData.csv")

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
        ui.print_menu()
        trucks[0].deliver(graph, 0.00, 0)
        user_input = int(input("Enter a number: "))



if __name__ == "__main__":
    main()

