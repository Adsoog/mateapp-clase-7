import matplotlib.pyplot as plt
x1=(3,4,5,6)
y1=(5,6,3,4)
x2=(2,5,8)
y2=(3,4,3)

plt.plot(x1, y1, label = "linea1", linewidth = 4, color = "blue")
plt.plot(x1, y1, label = "linea2", linewidth = 4, color = "green")
plt.title("Diagrama de lineas")
plt.xlabel("Eje y")
plt.xlabel("Eje x")
plt.legend()
plt.grid()
plt.show()