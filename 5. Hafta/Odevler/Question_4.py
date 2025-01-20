class Vehicle():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    
    def __str__(self):
        return f"""
        Brand: {self.make}
        Model: {self.model}
        Year: {self.year}
        """

class SUV(Vehicle):
    def __init__(self, make, model, year,four_wheel_drive):
        super().__init__(make, model, year)
        self.four_wheel_drive=four_wheel_drive

    def __str__(self):
        return super().__str__()+f"Four wheel drive?: {self.four_wheel_drive} "

    


class SportsCar(Vehicle):
    def __init__(self, make, model, year,max_speed):
        super().__init__(make, model, year)
        self.max_speed=max_speed
    
    def __str__(self):
        return super().__str__()+f"Max Speed: {self.max_speed}"
    

sport_car1= SportsCar("BMW","750i",2025,399)
print("sport car:\n",sport_car1)

suv1=SUV("Volvo","S90",2023,"Yes")
print("SUV: ",suv1)
    