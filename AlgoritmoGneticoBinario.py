import random

TAMANO_POBLACION = 10   # Cantidad de individuos
NUM_BITS = 5             # Cantidad de bits de cada individuo
GENERACIONES = 10        # Cuántas veces repetiremos el proceso
PROB_CRUZA = 0.8         # Probabilidad de que ocurra la cruza
PROB_MUTACION = 0.1      # Probabilidad de mutación de cada bit


def crear_individuo():
    
    individuo = []

    for i in range(NUM_BITS):
        bit = random.randint(0, 1)
        individuo.append(bit)

    return individuo


def crear_poblacion():
    
    poblacion = []

    for i in range(TAMANO_POBLACION):
        individuo = crear_individuo()
        poblacion.append(individuo)

    return poblacion


def binario_a_decimal(individuo):
   
    numero = ""

    for bit in individuo:
        numero += str(bit)

    return int(numero, 2)

def fitness(individuo):
    """
    Indica qué tan bueno es un individuo.

    Nuestro objetivo es maximizar:

        f(x) = x²
    """

    x = binario_a_decimal(individuo)

    return x ** 2

def seleccion(poblacion):
   
    individuo1 = random.choice(poblacion)
    individuo2 = random.choice(poblacion)

    if fitness(individuo1) > fitness(individuo2):
        return individuo1

    else:
        return individuo2


def cruza(padre1, padre2):
   
    if random.random() > PROB_CRUZA:

        return padre1[:], padre2[:]

    punto = random.randint(1, NUM_BITS - 1)

    hijo1 = padre1[:punto] + padre2[punto:]
    hijo2 = padre2[:punto] + padre1[punto:]

    return hijo1, hijo2


def mutacion(individuo):
    
    individuo = individuo[:]

    for i in range(NUM_BITS):

        if random.random() < PROB_MUTACION:

            if individuo[i] == 0:
                individuo[i] = 1
            else:
                individuo[i] = 0

    return individuo


def mostrar_poblacion(poblacion, generacion):

    print("\n")
    print("GENERACIÓN:", generacion)
    print("\n")

    for individuo in poblacion:

        x = binario_a_decimal(individuo)
        aptitud = fitness(individuo)

        print(
            individuo,
            "-> x =", x,
            "-> fitness =", aptitud
        )


def algoritmo_genetico():

    poblacion = crear_poblacion()

    for generacion in range(GENERACIONES):

        mostrar_poblacion(poblacion, generacion)

        nueva_poblacion = []

        while len(nueva_poblacion) < TAMANO_POBLACION:

            padre1 = seleccion(poblacion)
            padre2 = seleccion(poblacion)

            hijo1, hijo2 = cruza(padre1, padre2)

            hijo1 = mutacion(hijo1)
            hijo2 = mutacion(hijo2)

            nueva_poblacion.append(hijo1)

            if len(nueva_poblacion) < TAMANO_POBLACION:
                nueva_poblacion.append(hijo2)

        poblacion = nueva_poblacion


    mejor = max(poblacion, key=fitness)

    print("\n")
    print("MEJOR SOLUCIÓN")
    print("\n")

    print("Individuo:", mejor)
    print("Valor de x:", binario_a_decimal(mejor))
    print("Fitness:", fitness(mejor))


algoritmo_genetico()