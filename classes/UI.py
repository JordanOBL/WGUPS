from datetime import datetime
class UI:
    def __init__(self):
        pass

    def print_menu(self):
        print("1. Track Time")
        print("2. Exit")

        try:
            user_input = int(input("Enter a number: "))
            if user_input == 1:
                time = self.track_time()
                return time
            elif user_input == 2:
                exit()
            else:
                print("Invalid Input")
                self.print_menu()
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
        for package in packages:
            print(package)
