import unittest

import os
import sys
sys.path.append(os.path.abspath('..'))

from lattern_fish import Fish
from simulation import Simulation

class RunTestCase(unittest.TestCase):
    def setUp(self):
        self.f1 = Fish(3)
        self.f2 = Fish(4)
        self.f3 = Fish(3)
        self.f4 = Fish(1)
        self.f5 = Fish(2)
        self.fishes = [self.f1, self.f2, self.f3, self.f4, self.f5]

    def test_after_1_day(self):
        sim = Simulation(self.fishes, 1)
        actual = sim.run()
        expected = [Fish(i) for i in [2,3,2,0,1]]
        self.assertEqual(actual, expected)

    def test_after_2_day(self):
        sim = Simulation(self.fishes, 2)
        actual = sim.run()
        expected = [Fish(i) for i in [1, 2, 1, 6, 0, 8]]
        self.assertEqual(actual, expected)

    def test_simulate_days(self):
        num_of_fish_spawned = self.f1.simulate_days(0, 1)
        self.assertEqual(num_of_fish_spawned, 1)

    def test_simulate_days2(self):
        num_of_fish_spawned = self.f1.simulate_days(0, 2)
        self.assertEqual(num_of_fish_spawned, 1)

    def test_simulate_days3(self):
        num_of_fish_spawned = self.f1.simulate_days(0, 3)
        self.assertEqual(num_of_fish_spawned, 1)

    def test_simulate_days4(self):
        num_of_fish_spawned = self.f1.simulate_days(0, 4)
        self.assertEqual(num_of_fish_spawned, 2)

    def test_simulate_days5(self):
        num_of_fish_spawned = self.f1.simulate_days(0, 9)
        self.assertEqual(num_of_fish_spawned, 2)

    def test_simulate_days6(self):
        num_of_fish_spawned = self.f1.simulate_days(0, 11)
        self.assertEqual(num_of_fish_spawned, 3)
