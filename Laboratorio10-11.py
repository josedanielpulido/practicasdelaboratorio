# Ejercicio parte 01 – Listas Enlazadas Dobles:
# Duplicar Nodos:
# 1. Crea una lista con al menos 4 nodos, duplica cada nodo de la lista e imprime la lista original y la lista 
# duplicada hacia adelante y hacia atrás.
class Nodo:
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

def crear_lista():
    """
    Esta función crea una lista con al menos 4 nodos.

    Returns:
        La lista con al menos 4 nodos.
    """

    nodo1 = Nodo(10)
    nodo2 = Nodo(20)
    nodo3 = Nodo(30)
    nodo4 = Nodo(40)

    nodo1.siguiente = nodo2
    nodo2.siguiente = nodo3
    nodo3.siguiente = nodo4

    return nodo1

def duplicar_lista(lista):
    """
    Esta función duplica cada nodo de una lista.

    Args:
        lista: La lista que se desea duplicar.

    Returns:
        La lista duplicada.
    """

    lista_duplicada = None
    actual = lista
    while actual is not None:
        nuevo_nodo = Nodo(actual.valor)
        if lista_duplicada is None:
            lista_duplicada = nuevo_nodo
        else:
            actual_duplicado = lista_duplicada
            while actual_duplicado.siguiente is not None:
                actual_duplicado = actual_duplicado.siguiente
            actual_duplicado.siguiente = nuevo_nodo
        actual = actual.siguiente

    return lista_duplicada

def imprimir_lista_adelante(lista):
    """
    Esta función imprime una lista hacia adelante.

    Args:
        lista: La lista que se desea imprimir.
    """

    actual = lista
    while actual is not None:
        print(actual.valor)
        actual = actual.siguiente

def imprimir_lista_atras(lista):
    """
    Esta función imprime una lista hacia atrás.

    Args:
        lista: La lista que se desea imprimir.
    """

    anterior = None
    actual = lista
    while actual is not None:
        siguiente = actual.siguiente
        actual.siguiente = anterior
        anterior = actual
        actual = siguiente

    while anterior is not None:
        print(anterior.valor)
        anterior = anterior.siguiente

# Ejemplo de uso
lista_original = crear_lista()

print("Lista original hacia adelante:")
imprimir_lista_adelante(lista_original)

print("Lista original hacia atrás:")
imprimir_lista_atras(lista_original)

lista_duplicada = duplicar_lista(lista_original)

print("Lista duplicada hacia adelante:")
imprimir_lista_adelante(lista_duplicada)

print("Lista duplicada hacia atrás:")
imprimir_lista_atras(lista_duplicada)

# Contar Nodos Pares e Impares:
# 2. Crea una lista con al menos 9 nodos, cuenta cuántos nodos tienen un dato par y cuántos tienen un dato 
# impar e imprime la lista hacia adelante y hacia atrás.
class Nodo:
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

def crear_lista():
    """
    Esta función crea una lista con al menos 9 nodos.

    Returns:
        La lista con al menos 9 nodos.
    """

    nodo1 = Nodo(1)
    nodo2 = Nodo(2)
    nodo3 = Nodo(3)
    nodo4 = Nodo(4)
    nodo5 = Nodo(5)
    nodo6 = Nodo(6)
    nodo7 = Nodo(7)
    nodo8 = Nodo(8)
    nodo9 = Nodo(9)

    nodo1.siguiente = nodo2
    nodo2.siguiente = nodo3
    nodo3.siguiente = nodo4
    nodo4.siguiente = nodo5
    nodo5.siguiente = nodo6
    nodo6.siguiente = nodo7
    nodo7.siguiente = nodo8
    nodo8.siguiente = nodo9

    return nodo1

def contar_pares_impares(lista):
    """
    Esta función cuenta cuántos nodos tienen un dato par y cuántos tienen un dato impar en una lista.

    Args:
        lista: La lista que se desea analizar.

    Returns:
        Una tupla con el número de nodos pares y el número de nodos impares.
    """

    pares = 0
    impares = 0
    actual = lista
    while actual is not None:
        if actual.valor % 2 == 0:
            pares += 1
        else:
            impares += 1
        actual = actual.siguiente

    return pares, impares

def imprimir_lista_adelante(lista):
    """
    Esta función imprime una lista hacia adelante.

    Args:
        lista: La lista que se desea imprimir.
    """

    actual = lista
    while actual is not None:
        print(actual.valor)
        actual = actual.siguiente

def imprimir_lista_atras(lista):
    """
    Esta función imprime una lista hacia atrás.

    Args:
        lista: La lista que se desea imprimir.
    """

    anterior = None
    actual = lista
    while actual is not None:
        siguiente = actual.siguiente
        actual.siguiente = anterior
        anterior = actual
        actual = siguiente

    while anterior is not None:
        print(anterior.valor)
        anterior = anterior.siguiente

# Ejemplo de uso
lista = crear_lista()

pares, impares = contar_pares_impares(lista)

print(f"Número de nodos pares: {pares}")
print(f"Número de nodos impares: {impares}")

print("Lista hacia adelante:")
imprimir_lista_adelante(lista)

print("Lista hacia atrás:")
imprimir_lista_atras(lista)

# Insertar Nodo en Posición Específica:
# 3. Crea una lista con al menos 5 nodos, inserta un nuevo nodo con el dato 15 en la posición 3 e imprime la 
# lista hacia adelante y hacia atrás.
class Nodo:
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

def crear_lista():
    """
    Esta función crea una lista con al menos 5 nodos.

    Returns:
        La lista con al menos 5 nodos.
    """

    nodo1 = Nodo(10)
    nodo2 = Nodo(20)
    nodo3 = Nodo(30)
    nodo4 = Nodo(40)
    nodo5 = Nodo(50)

    nodo1.siguiente = nodo2
    nodo2.siguiente = nodo3
    nodo3.siguiente = nodo4
    nodo4.siguiente = nodo5

    return nodo1

def insertar_nodo(lista, posicion, valor):
    """
    Esta función inserta un nuevo nodo en una lista enlazada simple.

    Args:
        lista: La lista en la que se desea insertar el nuevo nodo.
        posicion: La posición en la que se desea insertar el nuevo nodo.
        valor: El valor del nuevo nodo.

    Returns:
        La lista con el nuevo nodo insertado.
    """

    if posicion < 0:
        raise ValueError("La posición debe ser un número positivo")

    nuevo_nodo = Nodo(valor)
    actual = lista
    anterior = None
    for i in range(posicion):
        anterior = actual
        actual = actual.siguiente

    if anterior is None:
        nuevo_nodo.siguiente = lista
        lista = nuevo_nodo
    else:
        anterior.siguiente = nuevo_nodo
        nuevo_nodo.siguiente = actual

    return lista

def imprimir_lista_adelante(lista):
    """
    Esta función imprime una lista hacia adelante.

    Args:
        lista: La lista que se desea imprimir.
    """

    actual = lista
    while actual is not None:
        print(actual.valor)
        actual = actual.siguiente

def imprimir_lista_atras(lista):
    """
    Esta función imprime una lista hacia atrás.

    Args:
        lista: La lista que se desea imprimir.
    """

    anterior = None
    actual = lista
    while actual is not None:
        siguiente = actual.siguiente
        actual.siguiente = anterior
        anterior = actual
        actual = siguiente

    while anterior is not None:
        print(anterior.valor)
        anterior = anterior.siguiente

# Ejemplo de uso
lista = crear_lista()

print("Lista original:")
imprimir_lista_adelante(lista)

lista = insertar_nodo(lista, 3, 15)

print("Lista con el nuevo nodo insertado:")
imprimir_lista_adelante(lista)

print("Lista hacia atrás:")
imprimir_lista_atras(lista)

# Eliminar Nodos Duplicados:
# 4. Crea una lista con nodos que contengan datos duplicados, elimina todos los nodos duplicados, dejando 
# solo una instancia de cada dato e imprime la lista hacia adelante y hacia atrás.
class Nodo:
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

def crear_lista():
    """
    Esta función crea una lista con nodos que contienen datos duplicados.

    Returns:
        La lista con nodos que contienen datos duplicados.
    """

    nodo1 = Nodo(10)
    nodo2 = Nodo(20)
    nodo3 = Nodo(30)
    nodo4 = Nodo(40)
    nodo5 = Nodo(20)
    nodo6 = Nodo(50)
    nodo7 = Nodo(10)

    nodo1.siguiente = nodo2
    nodo2.siguiente = nodo3
    nodo3.siguiente = nodo4
    nodo4.siguiente = nodo5
    nodo5.siguiente = nodo6
    nodo6.siguiente = nodo7

    return nodo1

def eliminar_duplicados(lista):
    """
    Esta función elimina todos los nodos duplicados de una lista, dejando solo una instancia de cada dato.

    Args:
        lista: La lista con nodos duplicados.

    Returns:
        La lista sin nodos duplicados.
    """

    nodos_visitados = set()
    actual = lista
    anterior = None
    while actual is not None:
        if actual.valor in nodos_visitados:
            anterior.siguiente = actual.siguiente
        else:
            nodos_visitados.add(actual.valor)
            anterior = actual
        actual = actual.siguiente

    return lista

def imprimir_lista_adelante(lista):
    """
    Esta función imprime una lista hacia adelante.

    Args:
        lista: La lista que se desea imprimir.
    """

    actual = lista
    while actual is not None:
        print(actual.valor)
        actual = actual.siguiente

def imprimir_lista_atras(lista):
    """
    Esta función imprime una lista hacia atrás.

    Args:
        lista: La lista que se desea imprimir.
    """

    anterior = None
    actual = lista
    while actual is not None:
        siguiente = actual.siguiente
        actual.siguiente = anterior
        anterior = actual
        actual = siguiente

    while anterior is not None:
        print(anterior.valor)
        anterior = anterior.siguiente

# Ejemplo de uso
lista = crear_lista()

print("Lista original:")
imprimir_lista_adelante(lista)

lista = eliminar_duplicados(lista)

print("Lista sin nodos duplicados:")
imprimir_lista_adelante(lista)

print("Lista hacia atrás:")
imprimir_lista_atras(lista)

# Invertir la Lista:
# 5. Crea una lista con al menos 6 nodos, invierte el orden de la lista (el último elemento se convierte en el 
# primero y viceversa) e imprime la lista hacia adelante y hacia atrás
class Nodo:
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

def crear_lista():
    """
    Esta función crea una lista con al menos 6 nodos.

    Returns:
        La lista con al menos 6 nodos.
    """

    nodo1 = Nodo(10)
    nodo2 = Nodo(20)
    nodo3 = Nodo(30)
    nodo4 = Nodo(40)
    nodo5 = Nodo(50)
    nodo6 = Nodo(60)

    nodo1.siguiente = nodo2
    nodo2.siguiente = nodo3
    nodo3.siguiente = nodo4
    nodo4.siguiente = nodo5
    nodo5.siguiente = nodo6

    return nodo1

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

def imprimir_lista_adelante(lista):
    """
    Esta función imprime una lista hacia adelante.

    Args:
        lista: La lista que se desea imprimir.
    """

    actual = lista
    while actual is not None:
        print(actual.valor)
        actual = actual.siguiente

def imprimir_lista_atras(lista):
    """
    Esta función imprime una lista hacia atrás.

    Args:
        lista: La lista que se desea imprimir.
    """

    anterior = None
    actual = lista
    while actual is not None:
        siguiente = actual.siguiente
        actual.siguiente = anterior
        anterior = actual
        actual = siguiente

    while anterior is not None:
        print(anterior.valor)
        anterior = anterior.siguiente

# Ejemplo de uso
lista = crear_lista()

print("Lista original:")
imprimir_lista_adelante(lista)

lista_invertida = invertir_lista(lista)

print("Lista con el orden invertido:")
imprimir_lista_adelante(lista_invertida)

print("Lista original hacia atrás:")
imprimir_lista_atras(lista)



# Ejercicios parte 02:

# Invertir una cadena:
# # 6. Utilizar una pila para invertir el orden de los caracteres de una cadena.
# class Nodo:
#     def __init__(self, valor, siguiente=None):
#         self.valor = valor
#         self.siguiente = siguiente

# class Pila:
#     def __init__(self):
#         self.cima = None

#     def apilar(self, valor):
#         nuevo_nodo = Nodo(valor)
#         if self.cima is None:
#             self.cima = nuevo_nodo
#         else:
#             nuevo_nodo.siguiente = self.cima
#             self.cima = nuevo_nodo

#     def desapilar(self):
#         if self.cima is None:
#             raise ValueError("La pila está vacía")
#         valor_desapilado = self.cima.valor
#         self.cima = self.cima.siguiente
#         return valor_desapilado

# def invertir_cadena(cadena):
#     """
#     Esta función invierte el orden de los caracteres de una cadena utilizando una pila.

#     Args:
#         cadena: La cadena que se desea invertir.

#     Returns:
#         La cadena con el orden de los caracteres invertido.
#     """

#     pila = Pila()
#     for caracter in cadena:
#         pila.apilar(caracter)

#     cadena_invertida = ""
#     while not pila.esta_vacia():
#         cadena_invertida += pila.desapilar()

#     return cadena_invertida

# # Ejemplo de uso
# cadena = "Hola, mundo!"

# cadena_invertida = invertir_cadena(cadena)

# print(f"Cadena original: {cadena}")
# print(f"Cadena invertida: {cadena_invertida}")

# # Convertir número decimal a binario:
# # 7. Implementar un programa que convierta un número decimal a su representación en sistema binario 
# # utilizando una pila.
# class Nodo:
#     def __init__(self, valor, siguiente=None):
#         self.valor = valor
#         self.siguiente = siguiente

# class Pila:
#     def __init__(self):
#         self.cima = None

#     def apilar(self, valor):
#         nuevo_nodo = Nodo(valor)
#         if self.cima is None:
#             self.cima = nuevo_nodo
#         else:
#             nuevo_nodo.siguiente = self.cima
#             self.cima = nuevo_nodo

#     def desapilar(self):
#         if self.cima is None:
#             raise ValueError("La pila está vacía")
#         valor_desapilado = self.cima.valor
#         self.cima = self.cima.siguiente
#         return valor_desapilado

# def convertir_a_binario(numero):
#     """
#     Esta función convierte un número decimal a su representación en sistema binario utilizando una pila.

#     Args:
#         numero: El número decimal que se desea convertir.

#     Returns:
#         La representación en sistema binario del número decimal.
#     """

#     pila = Pila()
#     while numero > 0:
#         resto = numero % 2
#         numero //= 2
#         pila.apilar(resto)

#     numero_binario = ""
#     while not pila.esta_vacia():
#         numero_binario += str(pila.desapilar())

#     return numero_binario

# # Ejemplo de uso
# numero = 10

# numero_binario = convertir_a_binario(numero)

# print(f"Número decimal: {numero}")
# print(f"Número binario: {numero_binario}")

# # Evaluar expresión posfija:
# # 8. Crear un programa que evalúe una expresión matemática en notación posfija utilizando una pila.
# class Nodo:
#     def __init__(self, valor, siguiente=None):
#         self.valor = valor
#         self.siguiente = siguiente

# class Pila:
#     def __init__(self):
#         self.cima = None

#     def apilar(self, valor):
#         nuevo_nodo = Nodo(valor)
#         if self.cima is None:
#             self.cima = nuevo_nodo
#         else:
#             nuevo_nodo.siguiente = self.cima
#             self.cima = nuevo_nodo

#     def desapilar(self):
#         if self.cima is None:
#             raise ValueError("La pila está vacía")
#         valor_desapilado = self.cima.valor
#         self.cima = self.cima.siguiente
#         return valor_desapilado

# def evaluar_posfija(expresion):
#     """
#     Esta función evalúa una expresión matemática en notación posfija utilizando una pila.

#     Args:
#         expresion: La expresión en notación posfija.

#     Returns:
#         El resultado de la evaluación de la expresión.
#     """

#     pila = Pila()
#     for caracter in expresion:
#         if caracter.isdigit():
#             pila.apilar(int(caracter))
#         else:
#             operador2 = pila.desapilar()
#             operador1 = pila.desapilar()
#             if caracter == "+":
#                 resultado = operador1 + operador2
#             elif caracter == "-":
#                 resultado = operador1 - operador2
#             elif caracter == "*":
#                 resultado = operador1 * operador2
#             elif caracter == "/":
#                 resultado = operador1 / operador2
#             pila.apilar(resultado)

#     return pila.desapilar()

# # Ejemplo de uso
# expresion = "12 3 + 4 2 * -"

# resultado = evaluar_posfija(expresion)

# print(f"Expresión: {expresion}")
# print(f"Resultado: {resultado}")

# # Validar operadores anidados:
# # 9. Verificar si los operadores en una expresión matemática están correctamente anidados utilizando una 
# # pila.
# class Nodo:
#     def __init__(self, valor, siguiente=None):
#         self.valor = valor
#         self.siguiente = siguiente

# class Pila:
#     def __init__(self):
#         self.cima = None

#     def apilar(self, valor):
#         nuevo_nodo = Nodo(valor)
#         if self.cima is None:
#             self.cima = nuevo_nodo
#         else:
#             nuevo_nodo.siguiente = self.cima
#             self.cima = nuevo_nodo

#     def desapilar(self):
#         if self.cima is None:
#             raise ValueError("La pila está vacía")
#         valor_desapilado = self.cima.valor
#         self.cima = self.cima.siguiente
#         return valor_desapilado

# def estan_bien_anidados(expresion):
#     """
#     Esta función verifica si los operadores en una expresión matemática están correctamente anidados utilizando una pila.

#     Args:
#         expresion: La expresión matemática.

#     Returns:
#         True si los operadores están correctamente anidados, False en caso contrario.
#     """

#     pila = Pila()
#     for caracter in expresion:
#         if caracter in "()[]{}":
#             if caracter == "(" or caracter == "[" or caracter == "{":
#                 pila.apilar(caracter)
#             else:
#                 if pila.esta_vacia():
#                     return False
#                 operador_apertura = pila.desapilar()
#                 if (caracter == ")" and operador_apertura != "(") or \
#                    (caracter == "]" and operador_apertura != "[") or \
#                    (caracter == "}" and operador_apertura != "{"):
#                     return False

#     return pila.esta_vacia()

# # Ejemplo de uso
# expresion = "(a + b) * (c - d)"

# if estan_bien_anidados(expresion):
#     print(f"Los operadores en la expresión '{expresion}' están correctamente anidados.")
# else:
#     print(f"Los operadores en la expresión '{expresion}' no están correctamente anidados.")

# # Ordenar una pila:
# # 10. Ordenar los elementos de una pila de manera ascendente utilizando estructuras adicionales.
# def ordenar_pila(pila):
#     """
#     Esta función ordena los elementos de una pila de manera ascendente utilizando una lista como estructura adicional.

#     Args:
#         pila: La pila que se desea ordenar.

#     Returns:
#         La pila con los elementos ordenados de manera ascendente.
#     """

#     lista = []
#     while not pila.esta_vacia():
#         lista.append(pila.desapilar())

#     lista.sort()

#     for elemento in lista:
#         pila.apilar(elemento)

#     return pila

# # Ejemplo de uso
# pila = Pila()
# pila.apilar(10)
# pila.apilar(20)
# pila.apilar(30)
# pila.apilar(40)
# pila.apilar(50)

# pila_ordenada = ordenar_pila(pila)

# while not pila_ordenada.esta_vacia():
#     print(pila_ordenada.desapilar())

# # Eliminar duplicados:
# # 11. Eliminar los elementos duplicados de una pila.
# def eliminar_duplicados(pila):
#     """
#     Esta función elimina los elementos duplicados de una pila utilizando una lista como estructura adicional.

#     Args:
#         pila: La pila que se desea eliminar los elementos duplicados.

#     Returns:
#         La pila con los elementos duplicados eliminados.
#     """

#     lista = []
#     elementos_vistos = set()
#     while not pila.esta_vacia():
#         elemento_actual = pila.desapilar()
#         if elemento_actual not in elementos_vistos:
#             lista.append(elemento_actual)
#             elementos_vistos.add(elemento_actual)

#     for elemento in lista[::-1]:
#         pila.apilar(elemento)

#     return pila

# # Ejemplo de uso
# pila = Pila()
# pila.apilar(10)
# pila.apilar(20)
# pila.apilar(30)
# pila.apilar(40)
# pila.apilar(20)

# pila_sin_duplicados = eliminar_duplicados(pila)

# while not pila_sin_duplicados.esta_vacia():
#     print(pila_sin_duplicados.desapilar())

# # Implementar una calculadora sencilla:
# # 12. Crear una calculadora que pueda realizar operaciones básicas (+, -, *, /) utilizando una pila para evaluar 
# # expresiones.
# class Nodo:
#     def __init__(self, valor, siguiente=None):
#         self.valor = valor
#         self.siguiente = siguiente

# class Pila:
#     def __init__(self):
#         self.cima = None

#     def apilar(self, valor):
#         nuevo_nodo = Nodo(valor)
#         if self.cima is None:
#             self.cima = nuevo_nodo
#         else:
#             nuevo_nodo.siguiente = self.cima
#             self.cima = nuevo_nodo

#     def desapilar(self):
#         if self.cima is None:
#             raise ValueError("La pila está vacía")
#         valor_desapilado = self.cima.valor
#         self.cima = self.cima.siguiente
#         return valor_desapilado

# def evaluar_expresion(expresion):
#     """
#     Esta función evalúa una expresión matemática utilizando una pila.

#     Args:
#         expresion: La expresión matemática.

#     Returns:
#         El resultado de la evaluación de la expresión.
#     """

#     pila = Pila()
#     for caracter in expresion:
#         if caracter.isdigit():
#             pila.apilar(int(caracter))
#         else:
#             operador2 = pila.desapilar()
#             operador1 = pila.desapilar()
#             if caracter == "+":
#                 resultado = operador1 + operador2
#             elif caracter == "-":
#                 resultado = operador1 - operador2
#             elif caracter == "*":
#                 resultado = operador1 * operador2
#             elif caracter == "/":
#                 resultado = operador1 / operador2
#             pila.apilar(resultado)

#     return pila.desapilar()

# # Ejemplo de uso
# expresion = "12 3 + 4 2 * -"

# resultado = evaluar_expresion(expresion)

# print(f"Expresión: {expresion}")
# print(f"Resultado: {resultado}")

# # Comprobar palíndromos:
# # 13. Utilizar una pila para comprobar si una palabra o frase es un palíndromo.
# class Nodo:
#     def __init__(self, valor, siguiente=None):
#         self.valor = valor
#         self.siguiente = siguiente

# class Pila:
#     def __init__(self):
#         self.cima = None

#     def apilar(self, valor):
#         nuevo_nodo = Nodo(valor)
#         if self.cima is None:
#             self.cima = nuevo_nodo
#         else:
#             nuevo_nodo.siguiente = self.cima
#             self.cima = nuevo_nodo

#     def desapilar(self):
#         if self.cima is None:
#             raise ValueError("La pila está vacía")
#         valor_desapilado = self.cima.valor
#         self.cima = self.cima.siguiente
#         return valor_desapilado

# def es_palindromo(texto):
#     """
#     Esta función comprueba si una palabra o frase es un palíndromo utilizando una pila.

#     Args:
#         texto: La palabra o frase que se desea comprobar.

#     Returns:
#         True si la palabra o frase es un palíndromo, False en caso contrario.
#     """

#     pila = Pila()
#     for caracter in texto:
#         pila.apilar(caracter)

#     texto_invertido = ""
#     while not pila.esta_vacia():
#         texto_invertido += pila.desapilar()

#     return texto == texto_invertido

# # Ejemplo de uso
# texto = "Anita lava la tina"

# if es_palindromo(texto):
#     print(f"El texto '{texto}' es un palíndromo.")
# else:
#     print(f"El texto '{texto}' no es un palíndromo.")

# # Simular el proceso de deshacer (undo):
# # 14. Implementar un sistema simple de "deshacer" utilizando dos pilas, una para las acciones y otra para los 
# # deshaceres
# class Nodo:
#     def __init__(self, valor, siguiente=None):
#         self.valor = valor
#         self.siguiente = siguiente

# class Pila:
#     def __init__(self):
#         self.cima = None

#     def apilar(self, valor):
#         nuevo_nodo = Nodo(valor)
#         if self.cima is None:
#             self.cima = nuevo_nodo
#         else:
#             nuevo_nodo.siguiente = self.cima
#             self.cima = nuevo_nodo

#     def desapilar(self):
#         if self.cima is None:
#             raise ValueError("La pila está vacía")
#         valor_desapilado = self.cima.valor
#         self.cima = self.cima.siguiente
#         return valor_desapilado

# def deshacer(pila_acciones, pila_deshaceres):
#     """
#     Esta función realiza la acción de "deshacer" utilizando dos pilas.

#     Args:
#         pila_acciones: La pila que contiene las acciones realizadas.
#         pila_deshaceres: La pila que contiene las acciones que se pueden deshacer.

#     Returns:
#         El valor de la acción deshecha.
#     """

#     accion_deshecha = pila_acciones.desapilar()
#     pila_deshaceres.apilar(accion_deshecha)
#     return accion_deshecha

# def rehacer(pila_acciones, pila_deshaceres):
#     """
#     Esta función realiza la acción de "rehacer" utilizando dos pilas.

#     Args:
#         pila_acciones: La pila que contiene las acciones realizadas.
#         pila_deshaceres: La pila que contiene las acciones que se pueden deshacer.

#     Returns:
#         El valor de la acción rehecha.
#     """

#     accion_rehecha = pila_deshaceres.desapilar()
#     pila_acciones.apilar(accion_rehecha)
#     return accion_rehecha

# Ejemplo de uso
# pila_acciones = Pila()
# pila_deshaceres = Pila()

# # Apilamos algunas acciones
# pila_acciones.apilar("Acción 1")
# pila_acciones.apilar("Acción 2")
# pila_acciones.apilar("Acción 3")

# # Deshacemos una acción
# accion_deshecha = deshacer(pila_acciones, pila_deshaceres)
# print(f"Acción deshecha: {accion_deshecha}")

# # Rehacemos la acción deshecha
# accion_rehecha = rehacer(pila_acciones, pila_deshaceres)
# print(f"Acción rehecha: {accion_rehecha}")
