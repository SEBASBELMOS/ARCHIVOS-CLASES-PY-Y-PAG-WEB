class Car():
    def __init__(self, brand, model, color, engine_type):
        self.brand = brand
        self.model = model
        self.color = color
        self.engine_type = engine_type
        self.__maxprice = 900

    def sell(self):
        print("Precio de venta:" , self.__maxprice)
    # setter method
    def set_max_price(self, price) :
        self.__maxprice = price

car = Car ("kia", "picanto", "rojo", "gasolina")
car.sell ()

# change the price
car.__maxprice = 1000
car.sell ()

# using setter function
car.set_max_price(1000)
car.sell()