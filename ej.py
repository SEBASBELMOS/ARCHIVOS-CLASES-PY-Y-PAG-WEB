mensaje =  'No basta saber, se debe también aplicar. No es suficiente querer. se debe también hacer. Goethe (1749 1832)'
largo = len(mensaje)
cual= 'be'
cuantos=0
lista = []

donde= 1
i = 0
while (i<largo):
    donde=mensaje[i:].find(cual)
    if (donde>0):
        cuantos=cuantos+1
        i=i+donde+1
        lista.append(donde)
    else:
        i=i+1
print (cuantos)
print (lista)