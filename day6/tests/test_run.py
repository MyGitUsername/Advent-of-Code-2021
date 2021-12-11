import unittest
import pdb

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


