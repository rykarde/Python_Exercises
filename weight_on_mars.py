gravity = 0.0
earth_gravity = 9.81
planet = input("Pick a planet: Mars, Mercury, Venus, Jupiter? ")
mass = float(input("How much do you weight?: "))
earth_weight = mass * earth_gravity
weight_on_planet = 0.0
new_weight = 0.0

if planet == "Mars" or planet == "Mercury":
    gravity = 3.70
    weight_on_planet = mass * gravity
    new_weight = round(weight_on_planet / earth_gravity, 2)
    print("If you where on " + str(planet) + "you would weight " + str(new_weight) + "Kg.")

elif planet == "Venus":
    gravity = 8.87
    weight_on_planet = mass * gravity
    new_weight = round(weight_on_planet / earth_gravity, 2)
    print("If you where on " + str(planet) + "you would weight " + str(new_weight) + "Kg.")
elif planet == "Jupiter":
    gravity = 24.79
    weight_on_planet = mass * gravity
    new_weight = round(weight_on_planet / earth_gravity, 2)
    print("If you where on " + str(planet) + " you would weight " + str(new_weight) + "Kg.")
else:
    print("Enter a valid planet")






