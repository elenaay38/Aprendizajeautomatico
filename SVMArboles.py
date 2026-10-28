
from sklearn.svm import SVC

# Datos
X = [[2, 10], [3, 12], [4, 15],
     [10, 40], [12, 45], [15, 50]]

# 0 = árbol pequeño, 1 = árbol grande
y = [0, 0, 0, 1, 1, 1]

modelo = SVC(kernel="linear")
modelo.fit(X, y)

arbol = [[3, 13]]
resultado = modelo.predict(arbol)

if resultado[0] == 0:
    print("Es un árbol pequeño")
else:
    print("Es un árbol grande")
