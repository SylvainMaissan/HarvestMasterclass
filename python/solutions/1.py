class Shape:
    def __init__(self):
        self.pi = 3.14159265359

    def calculate_area_of_circle(self, radius):
        area = self.pi * (radius ** 2)
        return area

    def calculate_area_of_rectangle(self, length, width):
        area = length * width
        return area

    def calculate_circumference_of_circle(self, radius):
        circumference = 2 * self.pi * radius
        return circumference

    def calculate_perimeter_of_rectangle(self, length, width):
        perimeter = 2 * (length + width)
        return perimeter
