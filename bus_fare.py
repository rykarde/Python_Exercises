# state the variables
bus_fare = 4.25
age = int(input("Age of the passenger: "))
fare_type = "Standard"

# check if is kids fare
if age <= 5:
    fare_type = "Kids fare"
    bus_fare = 0
# check if is senior fare
if age >= 60:
    bus_fare = bus_fare - 1
    fare_type = "Senior"

print("The " + fare_type + " bus fare is " + str(bus_fare) + "€.")
