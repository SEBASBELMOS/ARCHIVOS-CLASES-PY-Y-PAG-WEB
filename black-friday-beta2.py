import pandas as pd

# Definir los vectores
C = ["iPhone", "gafas", "iPad", "Jean", "Pepsi"]
P = [300, 100, 360, 60, 30]
D = [10, 20, 60, 40, 59]
S = ["electrónico", "ropa", "electrónico", "ropa", "alimentos"]

# Crear un diccionario con los vectores
data = {"Producto": C, "Precio": P, "Descuento": D, "Tipo": S}

# Crear un DataFrame con los datos
df = pd.DataFrame(data)

# Función para calcular el precio con descuento
def calcular_precio_con_descuento(codigo_producto, cantidad):
    producto = df[df['Producto'] == codigo_producto]
    if not producto.empty:
        precio_unitario = producto['Precio'].values[0]
        descuento = producto['Descuento'].values[0]
        precio_total = (precio_unitario - (precio_unitario * (descuento / 100))) * cantidad
        seccion = producto['Tipo'].values[0]
        return precio_total, seccion
    else:
        return None, None

# Ingresar código de producto y cantidad
codigo_producto = input("Ingrese el código del producto: ")
cantidad = int(input("Ingrese la cantidad: "))

# Calcular el precio con descuento y mostrarlo
precio_total, seccion = calcular_precio_con_descuento(codigo_producto, cantidad)
if precio_total is not None:
    print(f"Total a pagar por {cantidad} {codigo_producto} en la sección de {seccion}: ${precio_total:.2f}")
else:
    print("Producto no encontrado.")