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
    
        self.point6 = Point(1, 1)
        self.point7 = Point(3, 3)

    def test_is_line(self):
        is_valid_line = self.point1.is_valid_line(self.point2)
        self.assertEqual(is_valid_line, True)

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

    def test_points_in_diagonal_line(self):
        actual = self.point4.points_in_line(self.point5)
        expected = [self.point4, self.point5, Point(8, 8)]
        self.assertEqual(set(actual), set(expected))
        self.assertEqual(len(actual), len(expected))

    def test_points_in_diagonal_line2(self):
        actual = self.point6.points_in_line(self.point7)
        expected = [self.point6, self.point7, Point(2, 2)]
        self.assertEqual(set(actual), set(expected))
        self.assertEqual(len(actual), len(expected))

    def test_points_is_not_diagonal(self):
        p1 = Point(0, 0)
        p2 = Point(10, 11)
        is_diagonal = p1.is_diagonal_with_45_degree_slope(p2)
        self.assertEqual(is_diagonal, False)


    def test_points_in_diagonal_line_switch_point_order(self):
        actual = self.point7.points_in_line(self.point6)
        expected = [self.point6, self.point7, Point(2, 2)]
        self.assertEqual(set(actual), set(expected))
        self.assertEqual(len(actual), len(expected))

    def test_is_diagonal_with_45_degree_slope(self):
        is_diagonal_45_degrees = self.point4.is_diagonal_with_45_degree_slope(self.point5)
        self.assertEqual(is_diagonal_45_degrees, True)

    def test_is_not_diagonal_with_45_degree_slope(self):
        is_diagonal_45_degrees = self.point1.is_diagonal_with_45_degree_slope(self.point5)
        self.assertEqual(is_diagonal_45_degrees, False)
