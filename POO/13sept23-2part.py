"""Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y 
la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje 
con el resultado de la nota y si ha aprobado o no.
Con base en la anterior clase, crear una lista de 34 alumnos y realizar un análisis de datos básico 
para conocer el porcentaje y la cantidad de estudiantes dentro de las siguientes categorías:

• Deficiente (O — 2.9)
• Aceptable (3 — 3.7)
• Bueno (3.8 — 4.4)
• Sobresaliente (4.5 — 5.0)

Además, mostrar la cantidad de estudiantes que reprobaron y aprobaron la asignatura
Imprimir un mensaje con el resultado del análisis.
Realizar el Diagrama de Clases y el codigo"""
import random

names = ["Juan", "María", "Pedro", "Laura", "Carlos", "Ana", "Diego", "Sofía", "Luis", "Elena"]
last_names = ["González", "Martínez", "Pérez", "López", "Díaz", "Rodríguez", "Gómez", "Fernández", "Sánchez", "García"]

class Alumno:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        
    def printer(self):
        print(f"Nombre: {self.name}")
        print(f"Nota: {self.grade:.1f}")

    def resultado(self):
        if self.grade <= 2.9:
            return "Deficiente"
        elif 3 <= self.grade <= 3.7:
            return "Aceptable"
        elif 3.8 <= self.grade <= 4.4:
            return "Bueno"
        elif 4.5 <= self.grade <= 5.0:
            return "Sobresaliente"
        else:
            return "Nota inválida"

def generar_std_random():
    name = random.choice(names) + " " + random.choice(last_names)
    grade = (random.uniform(0, 50)/10)
    return Alumno(name, grade)

def analysis_stud(lista_alumnos):
    deficiente = aceptable = bueno = sobresaliente = reprobados = aprobados = 0

    for alumno in lista_alumnos:
        grade = alumno.grade
        if grade <= 2.9:
            deficiente += 1
            reprobados += 1
        elif 3 <= grade <= 3.7:
            aceptable += 1
            aprobados += 1
        elif 3.8 <= grade <= 4.4:
            bueno += 1
            aprobados += 1
        elif 4.5 <= grade <= 5.0:
            sobresaliente += 1
            aprobados += 1

    tot_std = len(lista_alumnos)

    return {
        "Deficiente": (deficiente, (deficiente / tot_std) * 100),
        "Aceptable": (aceptable, (aceptable / tot_std) * 100),
        "Bueno": (bueno, (bueno / tot_std) * 100),
        "Sobresaliente": (sobresaliente, (sobresaliente / tot_std) * 100),
        "Reprobados": (reprobados, (reprobados / tot_std) * 100),
        "Aprobados": (aprobados, (aprobados / tot_std) * 100)
    }

if __name__ == "__main__":
    lista_alumnos = [generar_std_random() for _ in range(34)]

    for alumno in lista_alumnos:
        alumno.printer()

    resultado = analysis_stud(lista_alumnos)
    print("\nResultado del análisis:")
    for categoria, (cantidad, porcentaje) in resultado.items():
        print(f"{categoria}: {cantidad} estudiantes ({porcentaje:.0f}%)")
