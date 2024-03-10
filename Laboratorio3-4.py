# Ejercicio parte 01:
# Recursividad:
# 1) Ejercicio 1: Escribe una función recursiva que imprima los números pares del 1 al 100.
def imprimir_pares(numero): # Se define el metodo imprimir_pares
    """
    Esta función imprime los números pares del 1 al 100 de forma recursiva.

    Args:
        numero: El número actual.
    """

    if numero > 100: # Se verifica que el numero sea mayor que 100
        return

    if numero % 2 == 0: # Se verifica que el numero no tengo residuo
        print(numero)

    imprimir_pares(numero + 1) #el contador mas 1

# Ejemplo de uso
imprimir_pares(10)


# 2) Ejercicio 2: Escribe una función recursiva que imprima la suma de los números del 1 al n.
def suma_recursiva(n): # Se define el metodo.
  """
  Esta función imprime la suma de los números del 1 al n de forma recursiva.

  Args:
      n: El número límite.
  """

  if n == 0: #Se verifica que n es igual a cero
    return 0
  else:
    return n + suma_recursiva(n-1) # Se resta menos 1 para seguir con el bucle.

# Ejemplo de uso
numero = 5 # Se define el numero en 5
suma = suma_recursiva(numero) # Se define la suma recursiva
print(f"La suma de los números del 1 al {numero} es: {suma}")


# 3) Ejercicio 3: Escribe una función recursiva que imprima la pirámide de números del 1 al n.
def imprimir_piramide(n): #se feine el metodo
  """
  Esta función imprime la pirámide de números del 1 al n de forma recursiva.

  Args:
      n: El número límite.
  """

  if n == 0: 
    return
  else:
    for i in range(1, n + 1): #Vemos que la variable i con un contador 
      print(" " * (n - i), end="")
      print("*" * i)
    imprimir_piramide(n-1) #Se define la variable n en resta.

# Ejemplo de uso
numero = 10
imprimir_piramide(numero) #Se imrpime la muestra de numeros.


# 4) Ejercicio 4: Escribe una función recursiva que imprima la pirámide de números invertidos del 1 al n.
def imprimir_piramide_invertida(n): #Definimos la funcion
  """
  Esta función imprime la pirámide de números invertidos del 1 al n de forma recursiva.

  Args:
      n: El número límite.
  """

  if n == 0:
    return
  else:
    for i in range(n, 0, -1):
      print(" " * (n - i), end="")
      print("*" * i)
    imprimir_piramide_invertida(n-1)

# Ejemplo de uso
numero = 15
imprimir_piramide_invertida(numero) #Se llama a la funcion con un numero de muestra

# 5) Ejercicio 2: Escribe una función recursiva que imprima la tabla de multiplicar del n.
def imprimir_tabla_multiplicar(n, multiplicador=1): #Se define la funcion
  """
  Esta función imprime la tabla de multiplicar del n de forma recursiva.

  Args:
      n: El número del que se quiere imprimir la tabla de multiplicar.
      multiplicador: El multiplicador actual.
  """

  if multiplicador > 10: 
    return

  resultado = n * multiplicador
  print(f"{n} x {multiplicador} = {resultado}")

  imprimir_tabla_multiplicar(n, multiplicador + 1) #Se llama a la funcion con un contador +1

# Ejemplo de uso
numero = 6
imprimir_tabla_multiplicar(numero) #Se imprime con un numero de muestra

# Arreglos y Matrices:
# 6) Crea una matriz de números reales.
# Crear una matriz de 3x3 con números reales aleatorios
matriz_aleatoria = [[random.random() for i in range(3)] for j in range(3)]

# Se crea una matriz de 2x2 con valores específicos
matriz_especifica = [[1.2, 3.4], [5.6, 7.8]]

# Se imprime las matrices:
print(matriz_aleatoria)
print(matriz_especifica)


# 7) Crea una matriz de números complejos.
import numpy as np #ÇSe importa el numpy

# Se crea una matriz de 3x3 con números complejos aleatorios
matriz_aleatoria = np.random.rand(3, 3) + np.random.rand(3, 3) * 1j

# Se crea una matriz de 2x2 con valores específicos
matriz_especifica = np.array([[1.2 + 3.4j, 5.6 + 7.8j], [9.0 + 10.2j, 11.4 + 12.6j]])

# Se imprime las matrices
print(matriz_aleatoria)
print(matriz_especifica)

# 8) Crea una matriz de matrices.
# Se crea una matriz de 2x2 de matrices de 3x3
matriz_matrices = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

# Se imprime la matriz de matrices
for i in range(len(matriz_matrices)):
  for j in range(len(matriz_matrices[i])):
    print(matriz_matrices[i][j])
  print()

# 9) Accede al elemento central de una matriz.
# Se crea una matriz de 3x3
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Se calcula la posición del elemento central
fila_central = len(matriz) // 2
columna_central = len(matriz[0]) // 2

# Buscamos el elemento central
elemento_central = matriz[fila_central][columna_central]

# Se imprime el elemento central
print(elemento_central)

# 10) Suma dos matrices de diferentes tamaños.
import numpy as np
# Se crea dos matrices de diferentes tamaños
matriz_grande = np.array([[1, 2, 3], [4, 5, 6]])
matriz_pequena = np.array([7, 8, 9])
# Modificamos la matriz pequeña para que coincida con el tamaño de la matriz grande
matriz_pequena_redimensionada = np.resize(matriz_pequena, (2, 3))
# Se suma las matrices
suma_matrices = matriz_grande + matriz_pequena_redimensionada
# Imprimimos la suma
print(suma_matrices)

# 11) Multiplica una matriz por un número.
# Se crea una matriz
matriz = [[1, 2, 3], [4, 5, 6]]

# Se multiplica la matriz por un número
numero = 6
matriz_multiplicada = numero * matriz #Se multipliza la matriz por el numero

# Se imprime la matriz multiplicada
print(matriz_multiplicada)

# 12) Calcula la media de los elementos de una matriz.
# Creamos una matriz
matriz = [[1, 2, 3], [4, 5, 6]]

# se calcula la suma de los elementos de la matriz
suma_elementos = sum(sum(fila) for fila in matriz)

# se calcula la cantidad de elementos de la matriz
numero_elementos = len(matriz) * len(matriz[0])

# Calculamos la media de los numeros
media = suma_elementos / numero_elementos

# Imprimimos la media
print(media)

# Semana 3 y 4 la ultima parte:

#Ejercicio 1:
#Crea una matriz de números aleatorios de tamaño 100x100.

import numpy as np  #Importamos la librería NumPy y se renombra como np
# Creamos una matriz de números de tamaño 100x100
matriz_aleatoria = np.random.rand(100, 100)
# Se imprime las matrices
print("Matriz de números aleatorios de tamaño 100x100:")
print(matriz_aleatoria)  #Se imprime el metodo matriz con numeros.

#Ejercicio 2: Calcula la media, la mediana y la desviación estándar de los elementos de una matriz.

import numpy as np  # Importamos la librería NumPy y la renombramos como np

# Se crea una matriz de números aleatorios de tamaño 100x100
matriz_aleatoria = np.random.rand(100, 100)

# Se calcula la media de los elementos de la matriz
media = np.mean(matriz_aleatoria)

# Se calcula la mediana de los elementos de la matriz
mediana = np.median(matriz_aleatoria)

# s e calcula la desviación estándar de los elementos de la matriz
desviacion_estandar = np.std(matriz_aleatoria)

# Se imprime los resultados
print("Media de los elementos de la matriz:", media)  # Mostramos la media de los elementos de la matriz
print("Mediana de los elementos de la matriz:", mediana)  # Mostramos la mediana de los elementos de la matriz
print("Desviación estándar de los elementos de la matriz:", desviacion_estandar)  # Mostramos la desviación estándar de los elementos de la matriz

#Ejercicio 3: Escribe una función que encuentre el elemento máximo de una matriz.

import numpy as np  # Importamos la librería NumPy y la renombramos como np

def encontrar_maximo(matriz):
    # Función para encontrar el elemento máximo de una matriz
    maximo = np.max(matriz)  # Utilizamos la función np.max() de NumPy para encontrar el elemento máximo
    return maximo  # Se devuelve el elemento máximo encontrado

# Creamos una matriz utilizando np.array que es una función de la librería NumPy que crea matrices multidimensionales y
# que nos permite convertir listas bidimensionales en matrices NumPy.
matriz_ejemplo = np.array([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9]])

# Llamamos a la función para encontrar el máximo de la matriz de ejemplo
maximo_encontrado = encontrar_maximo(matriz_ejemplo)

# Mostramos el máximo encontrado
print("El elemento máximo de la matriz es:", maximo_encontrado)

#Ejercicio 4:Escribe una función que encuentre la submatriz de mayor suma de una matriz

import numpy as np  # Importamos la librería NumPy y la renombramos como np

def encontrar_submatriz_maxima(matriz):
    # Función para encontrar la submatriz de mayor suma dentro de una matriz dada
    max_suma = float('-inf')  # Inicializamos la máxima suma con un valor negativo infinito
    submatriz_maxima = None  # Inicializamos la submatriz de mayor suma como vacía

    # Recorremos todas las submatrices posibles dentro de la matriz
    for i in range(len(matriz)):  # Iteramos sobre las filas de la matriz
        for j in range(len(matriz[0])):  # Iteramos sobre las columnas de la matriz
            for k in range(i, len(matriz)):  # Definimos el límite superior de las filas de la submatriz
                for l in range(j, len(matriz[0])):  # Definimos el límite superior de las columnas de la submatriz
                    # Calculamos la suma de la submatriz actual
                    suma_actual = np.sum(matriz[i:k+1, j:l+1])

                    # Si la suma actual es mayor que la máxima suma registrada hasta ahora
                    if suma_actual > max_suma:
                        max_suma = suma_actual  # Actualizamos la máxima suma
                        submatriz_maxima = matriz[i:k+1, j:l+1]  # Actualizamos la submatriz de mayor suma

    return submatriz_maxima  # Devolvemos la submatriz de mayor suma encontrada

# Creamos una matriz de ejemplo de tamaño 4x4 utilizando np.array que es una función de la librería NumPy que crea matrices multidimensionales Y 
# permite convertir listas bidimensionales en matrices NumPy.
matriz_ejemplo = np.array([[1, 2, 3, 4],
                            [5, 6, 7, 8],
                            [9, 10, 11, 12],
                            [13, 14, 15, 16]])

# Llamamos a la función para encontrar la submatriz de mayor suma.
submatriz_maxima_encontrada = encontrar_submatriz_maxima(matriz_ejemplo)

# Mostramos la submatriz de mayor suma encontrada
print("La submatriz de mayor suma es:")
print(submatriz_maxima_encontrada)

# Ejercicio 5: Escribe una función que encuentre la matriz de covarianza de dos matrices

import numpy as np  # Importamos la librería NumPy y la renombramos como np

def matriz_covarianza(matriz1, matriz2):
    # Función para calcular la matriz de covarianza entre dos matrices dadas
    covarianza = np.cov(matriz1, matriz2)  # Calculamos la matriz de covarianza utilizando np.cov()
    return covarianza  # Devolvemos la matriz de covarianza calculada

# Creamos dos matrices de ejemplo utilizando np.array que 
#Es una función de la librería NumPy que crea matrices multidimensionales Y 
#Permite convertir listas bidimensionales en matrices NumPy.
matriz1 = np.array([[1, 2, 3],  # Creamos la matriz1 con 2 filas y 3 columnas
                     [4, 5, 6]])

matriz2 = np.array([[7, 8, 9],  # Creamos la matriz2 con 2 filas y 3 columnas
                     [10, 11, 12]])

# Llamamos a la función para encontrar la matriz de covarianza de las dos matrices
matriz_cov = matriz_covarianza(matriz1, matriz2)

# Se imprime el resutlado de la covarianza:
print("Matriz de covarianza de las dos matrices:")
print(matriz_cov)
