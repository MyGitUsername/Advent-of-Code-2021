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

    def is_valid_line(self, point):
        return (self.is_horizontal_line(point) or
                self.is_vertical_line(point) or 
                self.is_diagonal_with_45_degree_slope(point))

    def points_in_vertical_line(self, point):
        min_y = min(self.y, point.y) 
        max_y = max(self.y, point.y)
        return [Point(self.x, i) for i in range(min_y, max_y + 1)]

    def points_in_horizontal_line(self, point):
        min_x = min(self.x, point.x)
        max_x = max(self.x, point.x)
        return [Point(i, self.y) for i in range(min_x, max_x + 1)]

    def points_in_diagonal_line(self, point):
        min_x = min(self.x, point.x)
        max_x = max(self.x, point.x)
        min_y = min(self.y, point.y) 
        max_y = max(self.y, point.y)

        x = min_x 
        if self.x < point.x and self.y < point.y or point.x < self.x and point.y < self.y:
            y = min_y
            points = []
            while x <= max_x and y <= max_y:
                points.append(Point(x, y))
                x += 1
                y += 1
        else:
            y = max_y
            points = []
            while x <= max_x and y >= min_y:
                points.append(Point(x, y))
                x += 1
                y -= 1
        return points

    def points_in_line(self, point):
        points = []

        if self == point:
            return [self]
        elif self.is_vertical_line(point):
            points +=  self.points_in_vertical_line(point)
        elif self.is_horizontal_line(point):
            points +=  self.points_in_horizontal_line(point)
        elif self.is_diagonal_with_45_degree_slope(point):
            points +=  self.points_in_diagonal_line(point)

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
