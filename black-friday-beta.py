"""Sebastian Belalcazar Mosquera - 2230118 - 1/09/23
Por si tiene alguna duda, me gusta manejar las variables en ingles, en este caso las funciones 
deben tener un nombre especifico pero algunas variables las definí en ingles"""
import pandas as pd

def calcularPrecio(code, C, P, D):
    try:
        indice = C.index(code)
        price = P[indice]
        discount = D[indice]
        final_price = price - (price * (discount / 100))
        return final_price
    except ValueError:
        return None

def calcularTotal(sales, C, P, D):
    total = 0
    for code in sales:
        final_price = calcularPrecio(code, C, P, D)
        if final_price is not None:
            total += final_price
    return total

def hallarSecciones(sales, C, S):
    secciones = set()
    for code in sales:
        try:
            indice = C.index(code)
            seccion = S[indice]
            secciones.add(seccion)
        except ValueError:
            pass
    return list(secciones)

def descuentosPorSeccion(D, S):
    discounts = {}
    for i in range(len(S)):
        seccion = S[i]
        discount = D[i]
        if discount > 50:
            if seccion in discounts:
                discounts[seccion] += 1
                #print(f"seccion; {seccion}")
                #print(f"discount; {discount}")
                #print(f"C; {C}")
            else:
                discounts[seccion] = 1
    return discounts

C = ["iPhone", "Gafas", "iPad", "Jean", "Pepsi"]
P = [300, 100, 360, 60, 30]
D = [10, 20, 60, 40, 50]
S = ["Electrónica", "Ropa", "Electrónica", "Ropa", "Alimentos"]

descuentos_seccion = descuentosPorSeccion(D, S)

data = {"Producto": C, "Precio": P, "Descuento": D, "Tipo": S}

df = pd.DataFrame(data)

print("\nDescuentos por Sección:")
#print("Sección | Productos con más del 50% de descuento")
df_filtrado = df[df['Descuento'] >= 50]
print(df_filtrado)
#for seccion, productos in descuentos_seccion.items():
    #print(seccion, productos)

sales_user = []
while True:
    code = input("Ingrese el código del producto (o 'fin' para finalizar): ")
    if code == 'fin':
        break
    if code not in C:
        print("Digito el código incorrecto. Intente nuevamente.")
    else:
        sales_user.append(code)

total_sales = calcularTotal(sales_user, C, P, D)

secciones_visit = hallarSecciones(sales_user, C, S)

print(f"\nTotal a pagar por las compras: ${total_sales:.2f}")
print(f"\nSecciones a visitar: {secciones_visit}")
