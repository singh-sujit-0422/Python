# 3. Coordinate Distance
# Problem:
# Create a class Point that represents a 2D point (x, y). Add a method distance_from_origin() that returns the distance from (0, 0).

# Formula:
# sqrt(x² + y²)

import math

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return f'The distance of point ({self.x},{self.y}) from the origin (0, 0) is { math.sqrt(self.x**2 + self.y**2) }'


p1 = Point(3, 4)
p2 = Point(8, 6)
p3 = Point(15, 0)

print(p1.distance_from_origin())
print(p2.distance_from_origin())
print(p3.distance_from_origin())


# Output:
# The distance of point(3, 4) from the origin (0,0) is 5.0
# The distance of point(8, 6) from the origin (0,0) is 10.0
# The distance of point(15, 0) from the origin (0,0) is 15.0

