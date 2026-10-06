from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Cargamos un conjunto de datos
iris = datasets.load_iris()

X = iris.data

y = iris.target

X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Creamos el modelo SVM
modelo = SVC(kernel='linear')

# Entrenamiento del modelo
modelo.fit(X_entrenamiento, y_entrenamiento)

predicciones = modelo.predict(X_prueba)

precision = accuracy_score(y_prueba, predicciones)


print("Predicciones:", predicciones)
print("Valores reales:", y_prueba)
print("Precisión del modelo:", precision)