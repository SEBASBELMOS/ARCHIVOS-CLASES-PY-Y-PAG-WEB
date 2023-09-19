class Car():
    def __init__(self, brand, model, color, engine_type):
        self.brand = brand
        self.model = model
        self.color = color
        self.engine_type = engine_type
    
    def update_att(self, new_color, new_model, new_brand, new_engine_type):
        self.color = new_color
        self.brand = new_brand
        self.model = new_model
        self.engine_type = new_engine_type

car = Car("Mclaren", "P1", "Negro", "Gasolina")
car2 = Car("Tesla", "X", "Blanco", "Electrico")
car3 = Car("Toyota", "TXL", "Gris", "Diesel")

print(car.color)
print(car.brand)

car.update_att("Naranja")
print(car.color)

car.update_att
print(car.brand)
