from datetime import datetime
from classes.Colors import bcolors
class UI:
    def __init__(self):
        pass

    def print_menu(self):
        print(f"{bcolors.ENDC}\n1. Track Time")
        print("2. Exit")
        user_time = None

        try:
            user_input = int(input("Enter a number: "))
            if user_input == 1:
                user_time = self.track_time()
                
            elif user_input == 2:
                exit()
            else:
                print("Invalid Input")
                self.print_menu()
            return user_time
        except ValueError:
            print("Invalid Input")
            self.print_menu()

    def track_time(self):
        try:
            hour = int(input('Enter Hour (1 - 12): '))
            if hour < 1 or hour > 12:
                raise ValueError
            minute = int(input('Enter Minutes (0 - 59): '))
            if minute < 0 or minute > 59:
                raise ValueError 
            print("Choose:\n1. AM\n2. PM")
            am_pm = int(input())
            if am_pm == 1:
                if hour == 12:
                    hour = 0
            elif am_pm == 2:
                if hour != 12:
                    hour += 12
            else:
                raise ValueError

            time = datetime(2025, 5, 10, hour, minute)
            return time
        except ValueError:
            print("Invalid Input")
            self.track_time()


    def print_packages(self, packages):
        print(f'{bcolors.OKCYAN}AT HUB{bcolors.ENDC}| {bcolors.WARNING}EN ROUTE {bcolors.ENDC}| {bcolors.OKGREEN}DELIVERED ON TIME {bcolors.ENDC}| {bcolors.FAIL} DELIVERED - NOT ON TIME {bcolors.ENDC}| {bcolors.OKBLUE} DELAYED\n')            
        print(f'{bcolors.ENDC}ID | Address | City | State | Zip | Deadline | Weight | Notes | Status | Delivery Time | Truck\n')
        for package in range(1, packages.getCount()):
            package = packages.search(package)
            print(package)

    def print_total_miles_driven(self, trucks):
        sum = 0
        print("\n")
        for truck in trucks:
            sum += truck.mileage
            print(f"{bcolors.ENDC}Truck {truck.id} Mileage: {truck.mileage}")
        print(f"Total miles driven: {sum}")
            
