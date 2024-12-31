#Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
import math

class Circle:
    """
    A class to represent a circle.
    """

    def __init__(self, radius):
        """
        Initialize a Circle with a given radius.

        Parameters:
        radius (float): The radius of the circle.
        """
        self.radius = radius

    def calculate_area(self):
        """
        Calculate the area of the circle.

        Returns:
        float: The area of the circle.
        """
        return math.pi * (self.radius ** 2)

    def calculate_perimeter(self):
       
        return 2 * math.pi * self.radius

circle = Circle(5)  # Create a Circle object with radius 5
area = circle.calculate_area()
perimeter = circle.calculate_perimeter()

print(f"Circle with radius {circle.radius}")
print(f"Area: {area:.2f}")
print(f"Perimeter: {perimeter:.2f}")