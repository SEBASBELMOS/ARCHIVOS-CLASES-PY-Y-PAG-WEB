import random
import math

radio_circulo1 = 10
radio_circulo2 = 40
radio_circulo3 = 80

centro_x = 80
centro_y = 80

lado_cuadrado = 160

n = 1000

premio_30 = 0
premio_40 = 0
premio_50 = 0

for _ in range(n):
    x = random.uniform(centro_x - lado_cuadrado / 2, centro_x + lado_cuadrado / 2)
    y = random.uniform(centro_y - lado_cuadrado / 2, centro_y + lado_cuadrado / 2)
    
    distancia = math.sqrt((x - centro_x) ** 2 + (y - centro_y) ** 2)
    
    if distancia <= radio_circulo1:
        premio_50 += 1
    elif distancia <= radio_circulo2:
        premio_40 += 1
    elif distancia <= radio_circulo3:
        premio_30 += 1

print("Resultados de la simulación:")
print(f"Dardos en el círculo de $50: {premio_50}")
print(f"Dardos en el círculo de $40: {premio_40}")
print(f"Dardos en el círculo de $30: {premio_30}")