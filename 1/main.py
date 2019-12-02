"""
Advent of Code
Day 1: The Tyranny of the Rocket Equation
Chris Potter
"""


from FuelRequirement import FuelRequirement

fuel = FuelRequirement()

f = open("mass_inputs.txt", "r")

for line in f:
    mass = int(line)
    fuel.fuel_requirement += fuel.calculate_fuel_requirements(mass)

f.close()

print("Total Fuel Requirement: " + str(fuel.fuel_requirement))
