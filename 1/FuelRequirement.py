"""
Class for Fuel Requirements
"""


class FuelRequirement:
    fuel_requirement: int

    def __init__(self):
        self.fuel_requirement = 0

    def round_down(self, value, decimals=0):
        multiplier = 10 ** decimals
        return int(value * multiplier) / multiplier

    def calculate_fuel_requirements(self, mass: int):
        required_fuel = int(self.round_down(mass / 3) - 2)
        return required_fuel
