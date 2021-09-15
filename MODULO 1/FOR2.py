suma = 0
for i in range(1, 101):
    if i % 2 == 0:
        suma += i

print(suma)
#ejercicio 1
a=0
b=1
for i in range(0, 10):
    b = b + a
    a = b - a
    print(b)
#ejercicio 2 donde se ingresa el curso, año nacimiento 3 personas, nombres y calcular cuantos años cumplira este año
for persona in range(1, 4):
    nombre = input("Digite su nombre ")
    ano_actual = int(input("Ingrese el año "))
    ano_nacim = int(input("Ingrese el año de nacimiento "))

    edad = ano_actual - ano_nacim

    print(f"{nombre} va a cumplir en el año actual {edad} años")