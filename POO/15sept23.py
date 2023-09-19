class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"El {self.brand} {self.model} está arrancando.")

class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)
        self.num_doors = num_doors

    def open_doors(self):
        print(f"Todas las {self.num_doors} puertas están abiertas.")

class Motorcycle(Vehicle):
    def __init__(self, brand, model, displacement):
        super().__init__(brand, model)
        self.displacement = displacement

    def accelerate(self):
        print(f"La moto con motor de {self.displacement}cc está acelerando.")

if __name__ == "__main__":
    car = Car("Lamborghini", "Aventador", 4)
    motorcycle = Motorcycle("Honda", "CBR600RR", 600)

    car.start()
    car.open_doors()

    print("\n")

    motorcycle.start()
    motorcycle.accelerate()