class Vehicle:
    def __init__(self, name, rent_per_day):
        self.name = name
        self.rent_per_day = rent_per_day
        self.available = True

    def calculate_rent(self, days):
        return self.rent_per_day * days


class Car(Vehicle):

    def calculate_rent(self, days):
        total = self.rent_per_day * days
        if days > 5:
            total = total * 0.9
        return total


class Bike(Vehicle):

    def calculate_rent(self, days):
        total = self.rent_per_day * days
        if days > 3:
            total = total * 0.95
        return total


class Customer:
    def __init__(self, name):
        self.name = name
        self.rented_vehicle = None


class RentalSystem:

    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def show_available_vehicles(self):
        print("\nAvailable Vehicles:")
        for i in range(len(self.vehicles)):
            v = self.vehicles[i]
            if v.available:
                print(i, v.name, "- Rs", v.rent_per_day, "per day")

    def rent_vehicle(self, index, customer, days):

        if self.vehicles[index].available:

            vehicle = self.vehicles[index]
            total = vehicle.calculate_rent(days)

            vehicle.available = False
            customer.rented_vehicle = vehicle

            print("\nVehicle Rented Successfully!")
            print("Total Rent = Rs", total)

        else:
            print("\nVehicle Not Available!")

    def return_vehicle(self, customer):

        if customer.rented_vehicle:
            customer.rented_vehicle.available = True
            print("\nVehicle Returned Successfully!")
            customer.rented_vehicle = None
        else:
            print("\nNo Vehicle Rented!")



system = RentalSystem()

system.add_vehicle(Car("Swift Car", 2000))
system.add_vehicle(Car("Innova Car", 3000))
system.add_vehicle(Bike("Activa Bike", 500))
system.add_vehicle(Bike("Royal Enfield", 800))

name = input("Enter Customer Name: ")
customer = Customer(name)

while True:

    print("\n1. Show Available Vehicles")
    print("2. Rent Vehicle")
    print("3. Return Vehicle")
    print("4. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        system.show_available_vehicles()

    elif choice == 2:
        system.show_available_vehicles()
        index = int(input("Enter Vehicle Number: "))
        days = int(input("Enter Number of Days: "))
        system.rent_vehicle(index, customer, days)

    elif choice == 3:
        system.return_vehicle(customer)

    elif choice == 4:
        print("\nThank You for Using Rental System!")
        break
