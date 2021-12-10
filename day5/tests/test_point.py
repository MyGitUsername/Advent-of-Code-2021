import unittest

import os
import sys
sys.path.append(os.path.abspath('..'))

from point import Point


class PointTestCase(unittest.TestCase):
    def setUp(self):
        self.point1 = Point(4, 1)
        self.point2 = Point(1, 1)
        self.point3 = Point(4, 5)
        self.point4 = Point(9, 7)
        self.point5 = Point(7, 9)
    
    def test_is_line(self):
        is_line = self.point1.is_line(self.point2)
        self.assertEqual(is_line, True)

    def test_points_in_line_horizontal(self):
        actual = self.point1.points_in_line(self.point2)
        expected = [Point(1, 1), Point(2, 1), Point(3, 1), Point(4, 1)]
        self.assertEqual(set(actual), set(expected))
        self.assertEqual(len(actual), len(expected))

    def test_points_in_line_vertical(self):
        actual = self.point1.points_in_line(self.point3)
        expected = [Point(4, 1), Point(4, 2), Point(4, 3), Point(4, 4), Point(4, 5)]
        self.assertEqual(set(actual), set(expected))
        self.assertEqual(len(actual), len(expected))

    def test_points_in_line_same_point(self):
        actual = self.point1.points_in_line(self.point1)
        expected = [self.point1]
        self.assertEqual(set(actual), set(expected))
        self.assertEqual(len(actual), len(expected))

    def test_is_diagonal_with_45_degree_slope(self):
        is_diagonal_45_degrees = self.point4.is_diagonal_with_45_degree_slope(self.point5)
        self.assertEqual(is_diagonal_45_degrees, True)

    def test_is_not_diagonal_with_45_degree_slope(self):
        is_diagonal_45_degrees = self.point1.is_diagonal_with_45_degree_slope(self.point5)
        self.assertEqual(is_diagonal_45_degrees, False)
