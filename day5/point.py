class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_horizontal_line(self, point):
        return self.y == point.y

    def is_vertical_line(self, point):
        return self.x == point.x

    def is_diagonal_with_45_degree_slope(self, point):
        return abs((point.y - self.y) / (point.x - self.x)) == 1

    def is_line(self, point):
        return (self.is_horizontal_line(point) or
                self.is_vertical_line(point)) 
                #  or self.is_diagonal_with_45_degree_slope(point))

    def points_in_vertical_line(self, point):
        min_y = (self.y if self.y < point.y else point.y)
        max_y = (point.y if point.y > self.y else self.y)
        return [Point(self.x, i) for i in range(min_y + 1, max_y)]

    def points_in_horizontal_line(self, point):
        min_x = (self.x if self.x < point.x else point.x)
        max_x = (point.x if point.x > self.x else self.x)
        return [Point(i, self.y) for i in range(min_x + 1, max_x)]

    def points_in_line(self, point):
        points = []
        points.append(self)
        points.append(point)

        if self == point:
            return [self]
        elif self.is_vertical_line(point):
            points = points + self.points_in_vertical_line(point)
        elif self.is_horizontal_line(point):
            points = points + self.points_in_horizontal_line(point)

        return points

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return hash((self.x ,self.y))

    def __str__(self):
        return '%s %s %s' % (self.__class__, self.x, self.y)

    def __repr__(self):
        return 'Point{x: %s, y: %s}' % (self.x, self.y)
