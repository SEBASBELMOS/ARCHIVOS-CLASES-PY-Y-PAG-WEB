import pandas as pd

#Num 1
print("Pd Series")
rmfc = pd.Series(['Courtois', 'Alaba', 'Bellingham', 'Modric','Vinicius Jr'],
                index = [1,4,5,10,7]
                )

print(rmfc)


print(f"\n Dorsal 1: {rmfc[1]}")
print(f"\n Dorsal 4: {rmfc[4]}")
print(f"\n Dorsal 5: {rmfc[5]}")
print(f"\n Dorsal 10: {rmfc[10]}")
print(f"\n Dorsal 7: {rmfc[7]}")

#Num 2
print("\n Dict")
dict = {1: 'Courtois', 4: 'Alaba', 5:'Bellingham', 10: 'Modric',7: 'Vinicius Jr'}
print(pd.Series(dict))

#Num 3

dict_rmfc = {'Jugador': ['Courtois', 'Alaba', 'Bellingham', 'Modric','Vinicius Jr'],
 'Altura (cm)': [200,180,186,172,176],
 'Dorsal': [1,4,5,10,7],
 'Precio (Millones Euros)':[45,40,120,10,150]
 }

df_rmfc = pd.DataFrame(dict_rmfc, index = [1,4,5,10,7])
print(df_rmfc)

print(df_rmfc.columns)
print(df_rmfc.index)


#Reto Granada FC

dict_gfc = {'Jugador':['Luis Suarez','Jorge Molina', 'Antonio Puertas', 'German Sanchez', 'Luis Milla', 'Luis Manuel Arantes Maximiano'],
'Posicion':['Delantero', 'Delantero', 'Centrocampista', 'Defensa', 'Centrocampista', 'Portero'],
'Numero':[9, 23, 10, 6, 5, 1],
'Altura':[185.0, 187.0, 185.0, 187.0, 175.0, 190.0],
'Goles':[7, 7, 5, 2, 2, 0]}

df_gfc = pd.DataFrame(dict_gfc, index=[9, 23, 10, 6, 5, 1])
print(df_gfc)