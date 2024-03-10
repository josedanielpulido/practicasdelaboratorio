# #problema1
# #EJERCICIO PARTE1
# # 1. Validar la edad de un usuario.
# from datetime import datetime

def validar_edad(fecha_nacimiento):
     """Valida la edad de un usuario a partir de su fecha de nacimiento.

     Args:
         fecha_nacimiento: La fecha de nacimiento del usuario en formato YYYY-MM-DD.

     Returns:
         True si el usuario es mayor de edad, False en caso contrario.
     """

     fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
     fecha_actual = datetime.now()
     edad = fecha_actual.year - fecha_nacimiento.year

     if fecha_actual.month < fecha_nacimiento.month:
         edad -= 1

     return edad >= 18

# Ejemplo de uso
 fecha_nacimiento = input("Introduce tu fecha de nacimiento (YYYY-MM-DD): ")

 if validar_edad(fecha_nacimiento):
     print("Eres mayor de edad.")
 else:
     print("Eres menor de edad.")


# # 2. Verificar el tipo de dato de una variable.
    
 # Definir una variable
edad = 25

 # Verificar el tipo de dato de la variable
tipo_dato = type(edad)

 # Imprimir el tipo de dato
 print(tipo_dato)

 #2.1
 # Verificar si la variable `edad` es un número entero
es_numero_entero = isinstance(edad, int)

 # Imprimir el resultado
 print(es_numero_entero)


    
# # 3. Validar el rango de una calificación.
# def validar_calificacion(calificacion):
#     """Valida una calificación.

#     Args:
#         calificacion: La calificación a validar.

#     Returns:
#         True si la calificación es válida, False en caso contrario.
#     """

#     rango_calificacion_valido = (0, 100)
#     return calificacion >= rango_calificacion_valido[0] and calificacion <= rango_calificacion_valido[1]

# # Ejemplo de uso

# calificacion = float(input("Introduce tu calificación: "))

# if validar_calificacion(calificacion):
#     print("Tu calificación es válida.")
# else:
#     print("Tu calificación está fuera del rango válido.")


# # 4. Asegurar que una lista no esté vacía.
# lista = []

# for elemento in lista:
#     # La lista no está vacía
#     print("La lista no está vacía.")
#     break
# else:
#     # La lista está vacía
#     print("La lista está vacía.")

# # 5. Validar la igualdad de dos objetos.
# objeto1 =float(input("ingrese el objeto:"))
# objeto2 = float(input("ingrese el objeto: "))

# if objeto1 == objeto2:
#     print("Los objetos son iguales.")
# else:
#     print("Los objetos son diferentes.")

# # 6. Asegurar que un ciclo while se ejecuta al menos una vez.
# # Definir una variable
# edad = 0

# # Definir una bandera
# se_ha_ejecutado = False

# # Bucle while
# while not se_ha_ejecutado:
#     # Mostrar un mensaje al usuario
#     print("Introduce tu edad: ")

#     # Solicitar la edad al usuario
#     edad = int(input())

#     # Verificar si la edad es válida
#     if edad > 0:
#         # Cambiar la bandera a True
#         se_ha_ejecutado = True

# # Imprimir la edad
# print("Tu edad es:", edad)
 
# # 7. Asegurar que una función retorna un valor específico.
# def sumar(a, b):
#     """
#     Esta función suma dos números.

#     Args:
#         a: El primer número.
#         b: El segundo número.

#     Returns:
#         La suma de los dos números.
#     """

#     resultado = a + b
#     return resultado

# # Ejemplo de uso
# resultado = sumar(1, 2)

# print("El resultado es:", resultado)

# # 8. Validar el estado de una variable después de una operación.
# # Definir una variable
# variable = 10

# # Imprimir el valor de la variable antes de la operación
# print("Valor antes de la operación:", variable)

# # Realizar una operación
# variable += 5

# # Imprimir el valor de la variable después de la operación
# print("Valor después de la operación:", variable)

# # Verificar si el valor de la variable ha cambiado
# if variable > 10:
#     print("El valor de la variable ha cambiado.")
# else:
#     print("El valor de la variable no ha cambiado.")

# 9. Asegurar que un módulo se ha importado correctamente.
# Importar el módulo
try:
    # Importar el módulo
    modulo = __import__("mi_modulo")
except ImportError as error:
    print(error)
else:
    print("El módulo se ha importado correctamente.")



# Ejercicios parte 02:
# 10. Desarrollar el código de buscar nodo en la lista enlazada simple.
class Nodo:
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

def buscar_nodo(lista, valor):
    """
    Esta función busca un nodo en una lista enlazada simple.

    Args:
        lista: La lista enlazada simple.
        valor: El valor del nodo que se busca.

    Returns:
        El nodo encontrado o None si no se encuentra el nodo.
    """

    actual = lista
    while actual is not None:
        if actual.valor == valor:
            return actual
        actual = actual.siguiente

    return None

# Ejemplo de uso
nodo1 = Nodo(10)
nodo2 = Nodo(20)
nodo3 = Nodo(30)

nodo1.siguiente = nodo2
nodo2.siguiente = nodo3

valor_a_buscar = 20

nodo_encontrado = buscar_nodo(nodo1, valor_a_buscar)

if nodo_encontrado is not None:
    print("El nodo con el valor", valor_a_buscar, "se ha encontrado.")
else:
    print("No se ha encontrado un nodo con el valor", valor_a_buscar)

# Suma de Nodos
# 11. Implementa una función que sume todos los nodos de una lista enlazada simple.
class Nodo:
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

def sumar_nodos(lista):
    """
    Esta función suma todos los nodos de una lista enlazada simple.

    Args:
        lista: La lista enlazada simple.

    Returns:
        La suma de todos los nodos de la lista.
    """

    suma = 0
    actual = lista
    while actual is not None:
        suma += actual.valor
        actual = actual.siguiente

    return suma

# Ejemplo de uso
nodo1 = Nodo(10)
nodo2 = Nodo(20)
nodo3 = Nodo(30)

nodo1.siguiente = nodo2
nodo2.siguiente = nodo3

suma_nodos = sumar_nodos(nodo1)

print("La suma de todos los nodos es:", suma_nodos)

# Longitud de la Lista
# 12. Crea una función que devuelva la longitud de una lista enlazada simple.
class Nodo:
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

def obtener_longitud(lista):
    """
    Esta función calcula la longitud de una lista enlazada simple.

    Args:
        lista: La lista enlazada simple.

    Returns:
        La longitud de la lista.
    """

    longitud = 0
    actual = lista
    while actual is not None:
        longitud += 1
        actual = actual.siguiente

    return longitud

# Ejemplo de uso
nodo1 = Nodo(10)
nodo2 = Nodo(20)
nodo3 = Nodo(30)

nodo1.siguiente = nodo2
nodo2.siguiente = nodo3

longitud = obtener_longitud(nodo1)

print("La longitud de la lista es:", longitud)

# Concatenar Listas
# 13. Implementa una función que concatene dos listas enlazadas simples.
class Nodo:
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

def concatenar_listas(lista1, lista2):
    """
    Esta función concatena dos listas enlazadas simples.

    Args:
        lista1: La primera lista enlazada simple.
        lista2: La segunda lista enlazada simple.

    Returns:
        La lista concatenada.
    """

    actual = lista1
    while actual.siguiente is not None:
        actual = actual.siguiente

    actual.siguiente = lista2

    return lista1

# Ejemplo de uso
nodo1 = Nodo(10)
nodo2 = Nodo(20)
nodo3 = Nodo(30)

nodo4 = Nodo(40)
nodo5 = Nodo(50)

nodo1.siguiente = nodo2
nodo2.siguiente = nodo3

nodo4.siguiente = nodo5

lista_concatenada = concatenar_listas(nodo1, nodo4)

actual = lista_concatenada
while actual is not None:
    print(actual.valor)
    actual = actual.siguiente

# Eliminar Duplicados
# 14. Crea una función que elimine los nodos duplicados de una lista enlazada simple.
class Nodo:
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

def eliminar_nodos_duplicados(lista):
    """
    Esta función elimina los nodos duplicados de una lista enlazada simple.

    Args:
        lista: La lista enlazada simple.

    Returns:
        La lista sin nodos duplicados.
    """

    nodos_visitados = set()
    actual = lista
    anterior = None
    while actual is not None:
        if actual.valor in nodos_visitados:
            # Eliminar el nodo duplicado
            anterior.siguiente = actual.siguiente
        else:
            # Agregar el nodo a la lista de nodos visitados
            nodos_visitados.add(actual.valor)
            anterior = actual
        actual = actual.siguiente

    return lista

# Ejemplo de uso
nodo1 = Nodo(10)
nodo2 = Nodo(20)
nodo3 = Nodo(10)
nodo4 = Nodo(30)
nodo5 = Nodo(20)

nodo1.siguiente = nodo2
nodo2.siguiente = nodo3
nodo3.siguiente = nodo4
nodo4.siguiente = nodo5

lista_sin_duplicados = eliminar_nodos_duplicados(nodo1)

actual = lista_sin_duplicados
while actual is not None:
    print(actual.valor)
    actual = actual.siguiente
   
# Invertir Lista
# 15. Implementa una función que invierta el orden de una lista enlazada simple
class Nodo:
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

def invertir_lista(lista):
    """
    Esta función invierte el orden de una lista enlazada simple.

    Args:
        lista: La lista enlazada simple.

    Returns:
        La lista con el orden invertido.
    """

    anterior = None
    actual = lista
    while actual is not None:
        siguiente = actual.siguiente
        actual.siguiente = anterior
        anterior = actual
        actual = siguiente

    return anterior

# Ejemplo de uso
nodo1 = Nodo(10)
nodo2 = Nodo(20)
nodo3 = Nodo(30)

nodo1.siguiente = nodo2
nodo2.siguiente = nodo3

lista_invertida = invertir_lista(nodo1)

actual = lista_invertida
while actual is not None:
    print(actual.valor)
    actual = actual.siguiente
