import matplotlib.pyplot as plt

x1 = [2,5,6,14]
y1 = [11,22,33,44]

x2 = [2,5,6,15]
y2 = [4,12,18,45]

plt.plot(x1,y1,color="red", linewidth=3,label="F1")
plt.plot(x2,y2,color="blue",linewidth=3,label="F2")

plt.title("grafica Ejemplos")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.legend()
plt.grid()
plt.show()