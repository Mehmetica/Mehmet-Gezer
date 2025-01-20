
class Rectangle():
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def area(self):
        area_calculation=self.height*self.width
        return area_calculation
    
    def perimeter(self):
        perimeter_calculation= 2*(self.height+self.width)
        return perimeter_calculation
    
rectangle1= Rectangle(5,7)

print(f"Area of the given rectangle is: {rectangle1.area()} m2")
print(f"Perimeter of the given rectangle is: {rectangle1.perimeter()} m")
