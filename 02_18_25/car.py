import os
import pickle

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def __str__(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        return f"This car has {self.odometer_reading} miles on it."

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("The gas tank is now full.")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 40
    
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def fill_gas_tank(self):
        print("This car doesn't have a gas tank!")

def look_at_car(car:Car):
    print(car)
    print(car.read_odometer())
    car.fill_gas_tank()
    

def main():
    cwd = os.getcwd()
    if not cwd.count("02_18_25"):
        os.chdir("02_18_25")
    """ myCar = ElectricCar('nissan', 'leaf', 2024)
    print(myCar)
    myCar.fill_gas_tank()
    otherCar = Car('honda', 'crv','2014')
    otherCar.fill_gas_tank() 

    look_at_car(otherCar)
    look_at_car(myCar) """
    
    while(True):
        choice = input("Choose an option:\n1. Create a Car\n2. Create an Electric Car\n3. Look at a Car\n4.Exit\n")
        if choice == '1' or choice == "2":
            make = input("Car Make? ")
            model = input("Car Model? ")
            year = input("Car Year? ")
            file = open('cars.txt','ab')
            if choice == '1':
                pickle.dump(Car(make, model, year), file)
            else:
                pickle.dump(ElectricCar(make, model, year), file)
            file.close()
        elif choice == '3':
            
            #if os.path.getsize("cars.txt") > 0:
            #    print("There are no cars to look at.")
            #    continue
            file = open("cars.txt",'rb')
            carList = pickle.load(file)
            for car in carList:
                print(car)
            file.close()
            carNum = int(input("Please choose a car from the list "))
            look_at_car(carList[carNum - 1]) 
        else:
            break

if __name__ == "__main__": #if the file is being run directly instead of imported
    main()

