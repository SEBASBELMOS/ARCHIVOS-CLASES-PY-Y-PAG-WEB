## /n puee servir para saltar lineas de codigo

import random

num_secreto = random.randint(1, 10)

intentos = 1
print("Programa juego de adivinar numero")
while intentos < 5:
    try:
        numero = int(input("Diga un numero entre 1 y 10 "))
        if numero == num_secreto:
            print("Ganador!!!")
            break
        else:
            print("No es el numero")
            if num_secreto > numero:
                print("El numero adivinado es mayor")
            else:
                print("El numero secreto es menor")
    except:
        print("Debe digita solo numeros enteros")
    intentos += 1