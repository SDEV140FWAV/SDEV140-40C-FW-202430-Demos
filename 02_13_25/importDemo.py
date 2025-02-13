from breezypythongui import EasyFrame
from car import Car, ElectricCar

class MyWindow(EasyFrame):
    def __init__(self, car:Car):
        super().__init__("Car shopping", width=800, height=600)
        self.car = car
        self.car_display = self.addLabel(text=str(car),row=1, column=1)
        self.odo_display = self.addLabel(text=car.read_odometer(),row=2,column=1)

car = ElectricCar('nissan', 'leaf', 2024)
MyWindow(car).mainloop()