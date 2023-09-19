class Car():
    def __init__(self, brand, model, color, engine_type):
        self.brand = brand
        self.model = model
        self.color = color
        self.engine_type = engine_type
    
    def print_att(self, printd):
        print(self.brand, self.model, self.color, self.engine_type)
    

car = Car("Mclaren", "P1", "Negro", "Gasolina")
car2 = Car("Tesla", "X", "Blanco", "Electrico")
car3 = Car("Toyota", "TXL", "Gris", "Diesel")

print(car.model)
print(car2.brand)
print(car3.engine_type)

car.print_att()
