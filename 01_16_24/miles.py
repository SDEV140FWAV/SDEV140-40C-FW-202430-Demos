starting_mileage = int(input("Enter the starting mileage: "))
ending_mileage = int(input("Enter the ending mileage: "))
gallons_used = int(input("Enter the gallons of gas used: "))
distance_driven = ending_mileage - starting_mileage
miles_per_gallon = distance_driven / gallons_used

print("The miles per gallon is ", miles_per_gallon)