class Circle:
    def __init__(self, radii):
        self._pi = 3.141 
        self.radii = radii
    def circumference(self):
        return [2 * self._pi * radius for radius in self.radii]
    def area(self):
        return [self._pi * radius ** 2 for radius in self.radii]
    def largest_area(self):
        return max(self.area())
# Example usage:
radii = [10, 501, 22, 37, 100, 999, 87, 351]
my_circle = Circle(radii)

print(my_circle.circumference(),"are the cicumference respectively")
print(my_circle.area(),"are the area respectively")
print(my_circle.largest_area(),"is the largest area among them")