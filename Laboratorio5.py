# Semana 5
# 1. Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números primos
def es_primo(numero):
    # Verifica si el número es menor o igual a 1
    if numero <= 1:
        return False  # Los números menores o iguales a 1 no son primos

    # Itera sobre los números desde 2 hasta la raíz cuadrada del número + 1
    for i in range(2, int(numero ** 0.5) + 1):
        # Si el número es divisible por cualquier número en este rango, no es primo
        if numero % i == 0:
            return False

    return True  # Si el número no es divisible por ningún número, es primo


def numeros_primos(conjunto):
    primos = set()  # Inicializa un conjunto para almacenar los números primos

    # Itera sobre cada número en el conjunto dado
    for num in conjunto:
        # Verifica si el número es primo utilizando la función es_primo()
        if es_primo(num):
            # Si el número es primo, agrégalo al conjunto de números primos
            primos.add(num)

    return primos  # Devuelve el conjunto de números primos


# Ejemplo de uso:
conjunto_de_numeros = {2, 3, 4, 5, 6, 7, 8, 9, 10}

# Imprime el conjunto original
print("Conjunto original:", conjunto_de_numeros)

# Llama a la función numeros_primos para obtener el conjunto de números primos dentro del conjunto dado
numeros_primos_en_conjunto = numeros_primos(conjunto_de_numeros)

# Imprime el conjunto de números primos
print("Conjunto de números primos:", numeros_primos_en_conjunto)

#2. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que comienzan con una letra determinada.

def palabras_con_letra_inicial(conjunto_palabras, letra):
    # Función que recibe un conjunto de palabras y una letra inicial y devuelve las palabras que comienzan con esa letra
    palabras_con_letra = set()  # Inicializamos un conjunto para almacenar las palabras que comienzan con la letra dada
    
    # Iteramos sobre cada palabra en el conjunto dado
    for palabra in conjunto_palabras:
        # Comprobamos si la palabra comienza con la letra dada, ignorando mayúsculas y minúsculas
        if palabra.lower().startswith(letra.lower()):
            palabras_con_letra.add(palabra)  # Agregamos la palabra al conjunto si cumple la condición
    
    return palabras_con_letra  # Devolvemos el conjunto de palabras que comienzan con la letra especificada

# Ejemplo de uso:
conjunto_de_palabras = {"Hola", "Python", "Programación", "lápiz", "avión", "Manzana"}
letra_inicial = "P"

# Imprimimos el conjunto de palabras original
print("Conjunto de palabras original:", conjunto_de_palabras)

# Llamamos a la función palabras_con_letra_inicial para obtener las palabras que comienzan con la letra dada
palabras_con_letra_dada = palabras_con_letra_inicial(conjunto_de_palabras, letra_inicial)

# Imprimimos las palabras que comienzan con la letra dada
print("Palabras que comienzan con la letra '{}':".format(letra_inicial), palabras_con_letra_dada)

# 3. Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que son divisibles por un número determinado.

def numeros_divisibles(conjunto_numeros, divisor):
    # Función que recibe un conjunto de números y un divisor, y devuelve los números divisibles por el divisor
    numeros_divisibles = set()  # Inicializamos un conjunto para almacenar los números divisibles
    
    # Iteramos sobre cada número en el conjunto dado
    for numero in conjunto_numeros:
        # Verificamos si el número es divisible por el divisor
        if numero % divisor == 0:
            numeros_divisibles.add(numero)  # Agregamos el número al conjunto si es divisible por el divisor
    
    return numeros_divisibles  # Devolvemos el conjunto de números divisibles por el divisor

# Ejemplo de uso:
conjunto_de_numeros = {2, 3, 4, 5, 6, 7, 8, 9, 10}
divisor = 3

# Imprimimos el conjunto de números original
print("Conjunto de números original:", conjunto_de_numeros)

# Llamamos a la función numeros_divisibles para obtener los números divisibles por el divisor dado
numeros_divisibles_por_divisor = numeros_divisibles(conjunto_de_numeros, divisor)

# Imprimimos los números divisibles por el divisor
print("Números divisibles por {}: ".format(divisor), numeros_divisibles_por_divisor)

# 4. Escriba una función que reciba dos conjuntos de números y devuelva un conjunto con los números que están en ambos conjuntos."""

def numeros_en_comun(conjunto1, conjunto2):
    # Función que recibe dos conjuntos de números y devuelve los números que están en ambos conjuntos
    numeros_comunes = conjunto1.intersection(conjunto2)
    # La función intersection() devuelve un conjunto que contiene los elementos que están presentes en ambos conjuntos
    
    return numeros_comunes
    # Devolvemos el conjunto que contiene los números comunes a ambos conjuntos

# Ejemplo de uso:
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}

# Imprimimos los conjuntos originales
print("Conjunto 1:", conjunto1)
print("Conjunto 2:", conjunto2)

# Llamamos a la función numeros_en_comun para encontrar los números que están en ambos conjuntos
numeros_comunes = numeros_en_comun(conjunto1, conjunto2)

# Imprimimos los números en común
print("Números en común:", numeros_comunes)

#5. Escriba una función que reciba dos conjuntos de números y devuelva un conjunto con los números que están en el primer conjunto 
# pero no en el segundo.

def numeros_en_primero_no_en_segundo(conjunto1, conjunto2):
    # Función que recibe dos conjuntos de números y devuelve los números que están en el primer conjunto pero no en el segundo
    numeros_diferentes = conjunto1.difference(conjunto2)
    # La función difference() devuelve un conjunto que contiene los elementos que están en el primer conjunto pero no en el segundo
    return numeros_diferentes
    # Devolvemos el conjunto que contiene los números que están en el primer conjunto pero no en el segundo

# Ejemplo de uso:
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}

# Imprimimos los conjuntos originales
print("Conjunto 1:", conjunto1)
print("Conjunto 2:", conjunto2)

# Llamamos a la función numeros_en_primero_no_en_segundo para encontrar los números que están en el primero pero no en el segundo conjunto
numeros_diferentes = numeros_en_primero_no_en_segundo(conjunto1, conjunto2)

# Imprimimos los números que están en el primero pero no en el segundo conjunto
print("Números en el primero pero no en el segundo:", numeros_diferentes)

# 6. Escriba una función que reciba dos conjuntos de números y devuelva un conjunto con los números que están en el segundo conjunto
# pero no en el primero.

def numeros_en_segundo_no_en_primero(conjunto1, conjunto2):
    # Función que recibe dos conjuntos de números y devuelve los números que están en el segundo conjunto pero no en el primero
    numeros_diferentes = conjunto2.difference(conjunto1)
    # La función difference() devuelve un conjunto que contiene los elementos que están en el segundo conjunto pero no en el primero
    return numeros_diferentes
    # Devolvemos el conjunto que contiene los números que están en el segundo conjunto pero no en el primero

# Ejemplo de uso:
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}

# Imprimimos los conjuntos originales
print("Conjunto 1:", conjunto1)
print("Conjunto 2:", conjunto2)

# Llamamos a la función numeros_en_segundo_no_en_primero para encontrar los números que están en el segundo pero no en el primer conjunto
numeros_diferentes = numeros_en_segundo_no_en_primero(conjunto1, conjunto2)

# Imprimimos los números que están en el segundo pero no en el primer conjunto
print("Números en el segundo pero no en el primero:", numeros_diferentes)

# 7. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son anagramas

def encontrar_anagramas(conjunto_palabras):
    # Función que recibe un conjunto de palabras y devuelve un conjunto con las palabras que son anagramas

    anagramas = set()  # Inicializamos un conjunto para almacenar los anagramas encontrados
    conteo_palabras = {}  # Creamos un diccionario para almacenar el conteo de letras en cada palabra

    # Iteramos sobre cada palabra en el conjunto dado
    for palabra in conjunto_palabras:
        # Convertimos la palabra a una tupla de letras ordenadas alfabéticamente
        letras_ordenadas = tuple(sorted(palabra))

        # Agregamos la tupla de letras ordenadas al diccionario y aumentamos su conteo
        conteo_palabras[letras_ordenadas] = conteo_palabras.get(letras_ordenadas, 0) + 1

    # Iteramos sobre los elementos del diccionario
    for letras_ordenadas, conteo in conteo_palabras.items():
        # Si hay más de una palabra con las mismas letras ordenadas, son anagramas
        if conteo > 1:
            # Iteramos sobre las palabras con las letras ordenadas dadas
            for palabra in conjunto_palabras:
                # Si la palabra tiene las letras ordenadas correspondientes, la agregamos al conjunto de anagramas
                if tuple(sorted(palabra)) == letras_ordenadas:
                    anagramas.add(palabra)

    return anagramas

# Ejemplo de uso:
conjunto_de_palabras = {"roma", "amor", "casa", "saca", "perro", "arroz"}

# Imprimimos el conjunto de palabras original
print("Conjunto de palabras:", conjunto_de_palabras)

# Llamamos a la función encontrar_anagramas() y mostramos los resultados
print("Anagramas encontrados:", encontrar_anagramas(conjunto_de_palabras))

# 8. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son palíndromos."""

def palabras_palindromos(conjunto_palabras):
    # Función que recibe un conjunto de palabras y devuelve las palabras que son palíndromos
    palindromos = set()  # Inicializamos un conjunto para almacenar los palíndromos
    
    for palabra in conjunto_palabras:  # Iteramos sobre cada palabra en el conjunto dado
        if palabra == palabra[::-1]:   # Comprobamos si la palabra es igual a su reverso
            palindromos.add(palabra)    # Si la palabra es igual a su reverso, la añadimos al conjunto de palíndromos
            
    return palindromos  # Devolvemos el conjunto de palabras que son palíndromos

# Ejemplo de uso:
conjunto_de_palabras = {"radar", "oso", "cívico", "sol", "anana", "python"}

# Imprimimos el conjunto de palabras original
print("Conjunto de palabras original:", conjunto_de_palabras)

# Llamamos a la función palabras_palindromos() y mostramos los palíndromos encontrados
print("Palíndromos en el conjunto:", palabras_palindromos(conjunto_de_palabras))


# 9. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que tienen una longitud determinada."""

def palabras_longitud(conjunto_palabras, longitud):
    # Función que recibe un conjunto de palabras y una longitud, y devuelve las palabras con la longitud especificada
    palabras_con_longitud = set()  # Inicializamos un conjunto para almacenar las palabras con la longitud especificada
    
    for palabra in conjunto_palabras:  # Iteramos sobre cada palabra en el conjunto dado
        if len(palabra) == longitud:   # Comprobamos si la longitud de la palabra es igual a la longitud especificada
            palabras_con_longitud.add(palabra)  # Si la longitud de la palabra es la requerida, la añadimos al conjunto
            
    return palabras_con_longitud  # Devolvemos el conjunto de palabras con la longitud especificada

# Ejemplo de uso:
conjunto_de_palabras = {"Hola", "Python", "Programación", "lápiz", "avión", "Manzana"}
longitud_deseada = 5

# Imprimimos el conjunto de palabras original
print("Conjunto de palabras original:", conjunto_de_palabras)

# Llamamos a la función palabras_longitud() y mostramos las palabras con la longitud deseada
print("Palabras con longitud {}: ".format(longitud_deseada), palabras_longitud(conjunto_de_palabras, longitud_deseada))

# 10. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que contienen una letra determinada."""

def palabras_con_letra(conjunto_palabras, letra):
    # Función que recibe un conjunto de palabras y una letra, y devuelve las palabras que contienen la letra especificada
    palabras_con_la_letra = set()  # Inicializamos un conjunto para almacenar las palabras con la letra especificada
    
    for palabra in conjunto_palabras:  # Iteramos sobre cada palabra en el conjunto dado
        if letra in palabra:   # Comprobamos si la letra está presente en la palabra
            palabras_con_la_letra.add(palabra)  # Si la letra está presente, añadimos la palabra al conjunto
    
    return palabras_con_la_letra  # Devolvemos el conjunto de palabras que contienen la letra especificada

# Ejemplo de uso:
conjunto_de_palabras = {"Hola", "Python", "Programación", "lápiz", "avión", "Manzana"}
letra_deseada = 'a'

# Imprimimos el conjunto de palabras original
print("Conjunto de palabras original:", conjunto_de_palabras)

# Llamamos a la función palabras_con_letra() y mostramos las palabras que contienen la letra deseada
print("Palabras que contienen la letra '{}': ".format(letra_deseada), palabras_con_letra(conjunto_de_palabras, letra_deseada))
 
# 11. Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que están ordenados de menor a mayor"""

def numeros_ordenados_menor_a_mayor(conjunto_numeros):
    # Función que recibe un conjunto de números y devuelve los números ordenados de menor a mayor
    numeros_ordenados = sorted(conjunto_numeros)  # Ordenamos el conjunto de números
    return set(numeros_ordenados)  # Devolvemos el conjunto ordenado de menor a mayor

# Ejemplo de uso:
conjunto_de_numeros = {5, 2, 8, 1, 9, 3}
print("Conjunto de números original:", conjunto_de_numeros)  # Mostramos el conjunto original
numeros_ordenados = numeros_ordenados_menor_a_mayor(conjunto_de_numeros)  # Llamamos a la función
print("Números ordenados de menor a mayor:", numeros_ordenados)  # Mostramos el resultado ordenado

# 12. Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que 
# están ordenados de mayor a menor.
def ordenar_mayor_menor(numeros):
  """
  Esta función recibe un conjunto de números y devuelve un conjunto con los números ordenados de mayor a menor.

  Parámetros:
    numeros: Un conjunto de números.

  Retorno:
    Un conjunto con los números ordenados de mayor a menor.
  """

  # Convertir el conjunto a una lista
  lista_numeros = list(numeros)

  # Ordenar la lista de mayor a menor
  lista_numeros.sort(reverse=True)

  # Convertir la lista a un conjunto
  conjunto_ordenado = set(lista_numeros)

  # Devolver el conjunto ordenado
  return conjunto_ordenado

# Ejemplo de uso
numeros = {1, 5, 3, 2, 4}
conjunto_ordenado = ordenar_mayor_menor(numeros)
print(conjunto_ordenado)

# 13. Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que están duplicados.
def encontrar_duplicados(numeros):
  """
  Esta función recibe un conjunto de números y devuelve un conjunto con los números que están duplicados.

  Parámetros:
    numeros: Un conjunto de números.

  Retorno:
    Un conjunto con los números duplicados.
  """

  # Convertir el conjunto a una lista
  lista_numeros = list(numeros)

  # Crear un conjunto vacío para almacenar los números duplicados
  numeros_duplicados = set()

  # Recorrer la lista
  for i in range(len(lista_numeros)):
    # Si el elemento actual no está en el conjunto de números duplicados
    if lista_numeros[i] not in numeros_duplicados:
      # Agregar el elemento al conjunto de números duplicados
      numeros_duplicados.add(lista_numeros[i])
    # Si el elemento actual ya está en el conjunto de números duplicados
    else:
      # Agregar el elemento a la lista de números duplicados
      numeros_duplicados.add(lista_numeros[i])

  # Devolver el conjunto de números duplicados
  return numeros_duplicados

# Ejemplo de uso
numeros = {1, 2, 3, 4, 2, 5, 1}
numeros_duplicados = encontrar_duplicados(numeros)
print(numeros_duplicados)

# 14. Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que no están duplicados.
def encontrar_no_duplicados(numeros):
  """
  Esta función recibe un conjunto de números y devuelve un conjunto con los números que no están duplicados.

  Parámetros:
    numeros: Un conjunto de números.

  Retorno:
    Un conjunto con los números no duplicados.
  """

  # Convertir el conjunto a una lista
  lista_numeros = list(numeros)

  # Crear un conjunto vacío para almacenar los números no duplicados
  numeros_no_duplicados = set()

  # Recorrer la lista
  for i in range(len(lista_numeros)):
    # Si el elemento actual no está en el conjunto de números no duplicados
    if lista_numeros[i] not in numeros_no_duplicados:
      # Agregar el elemento al conjunto de números no duplicados
      numeros_no_duplicados.add(lista_numeros[i])

  # Devolver el conjunto de números no duplicados
  return numeros_no_duplicados

# Ejemplo de uso
numeros = {1, 2, 3, 4, 2, 5, 1}
numeros_no_duplicados = encontrar_no_duplicados(numeros)
print(numeros_no_duplicados)

# 15. Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que son primos y están ordenados de menor a mayor.
def encontrar_primos(numeros):
  """
  Esta función recibe un conjunto de números y devuelve un conjunto con los números primos ordenados de menor a mayor.

  Parámetros:
    numeros: Un conjunto de números.

  Retorno:
    Un conjunto con los números primos ordenados de menor a mayor.
  """

  # Crear un conjunto vacío para almacenar los números primos
  numeros_primos = set()

  # Recorrer el conjunto de números
  for numero in numeros:
    # Si el número es primo
    if es_primo(numero):
      # Agregar el número al conjunto de números primos
      numeros_primos.add(numero)

  # Ordenar el conjunto de números primos de menor a mayor
  numeros_primos_ordenados = sorted(numeros_primos)

  # Devolver el conjunto de números primos ordenados
  return numeros_primos_ordenados

# Función para determinar si un número es primo
def es_primo(numero):
  """
  Esta función determina si un número es primo.

  Parámetros:
    numero: Un número entero.

  Retorno:
    True si el número es primo, False si no lo es.
  """

  # Si el número es 1, no es primo
  if numero == 1:
    return False

  # Recorrer los números del 2 al cuadrado del número
  for i in range(2, int(numero**0.5) + 1):
    # Si el número es divisible por otro número, no es primo
    if numero % i == 0:
      return False

  # Si el número no es divisible por ningún otro número, es primo
  return True

# Ejemplo de uso
numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
numeros_primos = encontrar_primos(numeros)
print(numeros_primos)

# 16. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son palíndromos y están ordenadas de menor a mayor.
def encontrar_palindromos(palabras):
  """
  Esta función recibe un conjunto de palabras y devuelve un conjunto con las palabras palíndromas ordenadas de menor a mayor.

  Parámetros:
    palabras: Un conjunto de palabras.

  Retorno:
    Un conjunto con las palabras palíndromas ordenadas de menor a mayor.
  """

  # Crear un conjunto vacío para almacenar las palabras palíndromas
  palabras_palindromas = set()

  # Recorrer el conjunto de palabras
  for palabra in palabras:
    # Si la palabra es un palíndromo
    if es_palindromo(palabra):
      # Agregar la palabra al conjunto de palabras palíndromas
      palabras_palindromas.add(palabra)

  # Ordenar el conjunto de palabras palíndromas de menor a mayor
  palabras_palindromas_ordenadas = sorted(palabras_palindromas)

  # Devolver el conjunto de palabras palíndromas ordenadas
  return palabras_palindromas_ordenadas

# Función para determinar si una palabra es un palíndromo
def es_palindromo(palabra):
  """
  Esta función determina si una palabra es un palíndromo.

  Parámetros:
    palabra: Una cadena de caracteres.

  Retorno:
    True si la palabra es un palíndromo, False si no lo es.
  """

  # Convertir la palabra a minúsculas
  palabra_minusculas = palabra.lower()

  # Invertir la palabra
  palabra_invertida = palabra_minusculas[::-1]

  # Si la palabra original y la palabra invertida son iguales, la palabra es un palíndromo
  return palabra_minusculas == palabra_invertida

# Ejemplo de uso
palabras = {"Ana", "somos", "oso", "Anita lava la tina", "ropero"}
palabras_palindromas = encontrar_palindromos(palabras)
print(palabras_palindromas)


# 17. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que tienen una longitud determinada y están ordenadas de menor a mayor.
def encontrar_palabras_longitud(palabras, longitud):
  """
  Esta función recibe un conjunto de palabras y una longitud, y devuelve un conjunto con las palabras que tienen esa longitud y están ordenadas de menor a mayor.

  Parámetros:
    palabras: Un conjunto de palabras.
    longitud: La longitud deseada de las palabras.

  Retorno:
    Un conjunto con las palabras que tienen la longitud especificada y están ordenadas de menor a mayor.
  """

  # Crear un conjunto vacío para almacenar las palabras con la longitud deseada
  palabras_longitud_especifica = set()

  # Recorrer el conjunto de palabras
  for palabra in palabras:
    # Si la longitud de la palabra coincide con la longitud deseada
    if len(palabra) == longitud:
      # Agregar la palabra al conjunto de palabras con la longitud deseada
      palabras_longitud_especifica.add(palabra)

  # Ordenar el conjunto de palabras con la longitud deseada de menor a mayor
  palabras_longitud_especifica_ordenadas = sorted(palabras_longitud_especifica)

  # Devolver el conjunto de palabras con la longitud deseada ordenadas
  return palabras_longitud_especifica_ordenadas

# Ejemplo de uso
palabras = {"casa", "perro", "gato", "mesa", "silla", "banana"}
longitud = 5
palabras_longitud_especifica = encontrar_palabras_longitud(palabras, longitud)
print(palabras_longitud_especifica)


# 18. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que contienen una letra determinada y están ordenadas de mayor a menor.
def encontrar_palabras_letra(palabras, letra):
  """
  Esta función recibe un conjunto de palabras y una letra, y devuelve un conjunto con las palabras que contienen esa letra y están ordenadas de mayor a menor.

  Parámetros:
    palabras: Un conjunto de palabras.
    letra: La letra que se desea buscar en las palabras.

  Retorno:
    Un conjunto con las palabras que contienen la letra especificada y están ordenadas de mayor a menor.
  """

  # Convertir la letra a minúscula
  letra_minuscula = letra.lower()

  # Crear un conjunto vacío para almacenar las palabras que contienen la letra
  palabras_con_letra = set()

  # Recorrer el conjunto de palabras
  for palabra in palabras:
    # Si la letra se encuentra en la palabra
    if letra_minuscula in palabra.lower():
      # Agregar la palabra al conjunto de palabras que contienen la letra
      palabras_con_letra.add(palabra)

  # Ordenar el conjunto de palabras que contienen la letra de mayor a menor
  palabras_con_letra_ordenadas = sorted(palabras_con_letra, reverse=True)

  # Devolver el conjunto de palabras que contienen la letra ordenadas
  return palabras_con_letra_ordenadas

# Ejemplo de uso
palabras = {"casa", "perro", "gato", "mesa", "silla", "banana"}
letra = "a"
palabras_con_letra = encontrar_palabras_letra(palabras, letra)
print(palabras_con_letra)


# 19. Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que están ordenados de menor a mayor y que no están duplicados.
def encontrar_numeros_ordenados(numeros):
  """
  Esta función recibe un conjunto de números y devuelve un conjunto con los números que no están duplicados y que están ordenados de menor a mayor.

  Parámetros:
    numeros: Un conjunto de números.

  Retorno:
    Un conjunto con los números no duplicados ordenados de menor a mayor.
  """

  # Convertir el conjunto a una lista
  lista_numeros = list(numeros)

  # Eliminar los duplicados de la lista
  lista_numeros_sin_duplicados = list(set(lista_numeros))

  # Ordenar la lista de menor a mayor
  lista_numeros_ordenados = sorted(lista_numeros_sin_duplicados)

  # Convertir la lista ordenada a un conjunto
  numeros_ordenados_sin_duplicados = set(lista_numeros_ordenados)

  # Devolver el conjunto con los números ordenados y no duplicados
  return numeros_ordenados_sin_duplicados

# Ejemplo de uso
numeros = {1, 2, 3, 4, 2, 5, 1, 6, 7, 8, 7}
numeros_ordenados_sin_duplicados = encontrar_numeros_ordenados(numeros)
print(numeros_ordenados_sin_duplicados)

# 20. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son 
# palíndromos, tienen una longitud determinada y están ordenadas de menor a mayor
def encontrar_palindromos_longitud(palabras, longitud):
  """
  Esta función recibe un conjunto de palabras y una longitud, y devuelve un conjunto con las palabras que son palíndromos, tienen esa longitud y están ordenadas de menor a mayor.

  Parámetros:
    palabras: Un conjunto de palabras.
    longitud: La longitud deseada de las palabras.

  Retorno:
    Un conjunto con las palabras que son palíndromos, tienen la longitud especificada y están ordenadas de menor a mayor.
  """

  # Crear un conjunto vacío para almacenar las palabras palíndromas con la longitud deseada
  palabras_palindromos_longitud_especifica = set()

  # Recorrer el conjunto de palabras
  for palabra in palabras:
    # Si la longitud de la palabra coincide con la longitud deseada
    if len(palabra) == longitud:
      # Si la palabra es un palíndromo
      if es_palindromo(palabra):
        # Agregar la palabra al conjunto de palabras palíndromas con la longitud deseada
        palabras_palindromos_longitud_especifica.add(palabra)

  # Ordenar el conjunto de palabras palíndromas con la longitud deseada de menor a mayor
  palabras_palindromos_longitud_especifica_ordenadas = sorted(palabras_palindromos_longitud_especifica)

  # Devolver el conjunto de palabras palíndromas con la longitud deseada ordenadas
  return palabras_palindromos_longitud_especifica_ordenadas

# Función para determinar si una palabra es un palíndromo
def es_palindromo(palabra):
  """
  Esta función determina si una palabra es un palíndromo.

  Parámetros:
    palabra: Una cadena de caracteres.

  Retorno:
    True si la palabra es un palíndromo, False si no lo es.
  """

  # Convertir la palabra a minúsculas
  palabra_minusculas = palabra.lower()

  # Invertir la palabra
  palabra_invertida = palabra_minusculas[::-1]

  # Si la palabra original y la palabra invertida son iguales, la palabra es un palíndromo
  return palabra_minusculas == palabra_invertida

# Ejemplo de uso
palabras = {"Ana", "somos", "oso", "Anita lava la tina", "ropero"}
longitud = 5
palabras_palindromos_longitud_especifica = encontrar_palindromos_longitud(palabras, longitud)
print(palabras_palindromos_longitud_especifica)
