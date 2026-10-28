
from sklearn.neighbors import KNeighborsClassifier

# Datos: tamaño y altura
X = [[2, 10], [3, 12], [2, 11],
     [7, 25], [8, 28], [7, 26]]

# 0 = margarita, 1 = girasol
y = [0, 0, 0, 1, 1, 1]

modelo = KNeighborsClassifier(n_neighbors=3)

modelo.fit(X, y)

flor = [[3, 11]]
resultado = modelo.predict(flor)

if resultado[0] == 0:
    print("La flor es una margarita")
else:
    print("La flor es un girasol")

