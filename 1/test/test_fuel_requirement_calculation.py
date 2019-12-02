"""
Test class for examples
"""

import pytest
from FuelRequirement import FuelRequirement


class TestFuel:
    @pytest.fixture()
    def supply_test_values(self):
        return [12, 14, 1969, 100756]

    @pytest.fixture()
    def supply_expected_results(self):
        return [2, 2, 654, 33583]

    def test_fuel_requirements(self, supply_test_values, supply_expected_results):
        test_values = supply_test_values
        expected_results = supply_expected_results

        fuel_req = FuelRequirement()

        x = 0
        for mass in test_values:
            assert fuel_req.calculate_fuel_requirements(mass) == expected_results[x]
            x += 1

