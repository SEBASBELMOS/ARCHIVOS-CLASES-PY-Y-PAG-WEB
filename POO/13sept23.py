"""Ejercicio
Se requiere un programa que modele el concepto de una persona. Una persona posee nombre, 
apellido, número de documento de identidad y año de nacimiento. La clase debe tener un método inicializador 
(constructor) que inicialice los valores de sus respectivos atributos.
La clase debe incluir los siguientes métodos:

• Definir un método que imprima en pantalla los valores de los atributos del objeto.

En un método llamado main se deben crear dos personas y mostrar los valores de sus atributos en pantalla.
Realizar Diagrama de Clases y Codigo
"""

class Person:
    def __init__(self, name, l_name, doc_id, year_birth):
        self.name = name
        self.l_name = l_name
        self.doc_id = doc_id
        self.year_birth = year_birth
        
    def printer(self):
        print(f"Nombre: {self.name}")
        print(f"Apellido: {self.l_name}")
        print(f"Documento de Identidad: {self.doc_id}")
        print(f"Año de Nacimiento: {self.year_birth}")
        
def main():
    person1 = Person("Juan", "Paz", "12345678", 1990)
    person2 = Person("Pepito", "Pérez", "87654321", 1985)

    print("Datos de la Persona 1:")
    person1.printer()

    print("\nDatos de la Persona 2:")
    person2.printer()

main()