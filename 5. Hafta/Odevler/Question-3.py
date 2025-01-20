class Shape():
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Rectangle(Shape):
    def calculate_area(self):
        return f"Area: {self.width} * {self.height} = {self.width * self.height}"


class Square(Shape):
    def calculate_area(self):
        return f"Area: {self.width} * {self.height} = {self.width * self.height}"


rectangle1 = Rectangle(5, 6)
square1 = Square(3, 9)

print(rectangle1.calculate_area())  
print(square1.calculate_area())     
