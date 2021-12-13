import unittest

import os
import sys
sys.path.append(os.path.abspath('..'))

from simulation import Simulation

class SimulationTestCase(unittest.TestCase):
    def setUp(self):
        self.crabs = [16,1,2,0,4,2,7,1,2,14]

    def test_find_best_pos(self):
        sim = Simulation(self.crabs, 1)
        sim.find_best_pos()
        self.assertEqual(sim.best_pos, 2)

    def test_fuel_usage(self):
        sim = Simulation(self.crabs, 1)
        sim.find_best_pos()
        self.assertEqual(sim.min_fuel_usage, 37)

    def test_find_best_pos2(self):
        sim = Simulation(self.crabs, 2)
        sim.find_best_pos()
        self.assertEqual(sim.best_pos, 5)

    def test_fuel_usage2(self):
        sim = Simulation(self.crabs, 2)
        sim.find_best_pos()
        self.assertEqual(sim.min_fuel_usage, 168)
