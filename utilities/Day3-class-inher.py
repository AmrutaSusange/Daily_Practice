class Vehicle():
    def __init__(self,fuel, price, color):
        self.fuel = fuel
        self.price = price
        self.color = color

    def fillUpTank(self):
        self.fuel = 200
    def emptyTank(self):
        self.fuel = 0

    def fuelLeft(self):
        return self.fuel

class Car(Vehicle):
    def __init__(self, fuel, price, color, speed):
        super().__init__(fuel, price, color)
        self.speed = speed

    def beep(self):
        print("beep beep!")

class Truck(Car):
    def __init__(self, fuel, price, color, speed, tires):
        super().__init__(fuel, price, color, speed)
        self.tires = tires

    def beep(self):
        print("Honk honk!")

if __name__ == '__main__':
    tr = Vehicle(100, 110, 'white')
    tr.fillUpTank()
    cr = Car(50, 60, 'black', 120)
    t = Truck(500, 600, 'orange', 180, 'gorilla')
    cr.beep()
    t.beep()
    print(t.fuel)
    print(cr.fuel)
    print(tr.fuel)

