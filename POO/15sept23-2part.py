class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

class Motocicleta(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

class Camioneta(Vehiculo):
    def __init__(self, color, ruedas, carga):
        super().__init__(color, ruedas)
        self.carga = carga

def catalogar(vehiculos, ruedas=None):
    if ruedas is not None:
        vehiculos_filtrados = [vehiculo for vehiculo in vehiculos if vehiculo.ruedas == ruedas]
        print(f"Se han encontrado {len(vehiculos_filtrados)} vehículos con {ruedas} ruedas:")
    else:
        vehiculos_filtrados = vehiculos
        print("Catálogo de vehículos:")

    for vehiculo in vehiculos_filtrados:
        print(f"Tipo: {type(vehiculo).__name__}")
        print(f"Color: {vehiculo.color}")
        print(f"Número de ruedas: {vehiculo.ruedas}")

bicicleta = Bicicleta("Rojo", 2, "Deportiva")
coche = Coche("Azul", 4, 120, 2000)
motocicleta = Motocicleta("Negro", 2, 180, 1000)
camioneta = Camioneta("Blanco", 4, 1500)

vehiculos = [bicicleta, coche, motocicleta, camioneta]

catalogar(vehiculos)

print("\nFiltrando por 2 ruedas:")
catalogar(vehiculos, ruedas=2)

print("\nFiltrando por 4 ruedas:")
catalogar(vehiculos, ruedas=4)
