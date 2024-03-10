# SEMANAS 01 _ 02 
# Comparación de los lenguajes de programación JAVA, PYTHON y C 
# Operaciones Básicas:
# 1. Realiza la suma, resta, multiplicación y división de 

#Pedimos al usuario para que ingrese dos numeros
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Realizamos las operaciones
suma = num1 + num2   # SUMA
resta = num1 - num2   #RESTA
multiplicacion = num1 * num2  #MULTIPLICACION

if num2 != 0: # Num2 tienes que ser disntito de cero.
    division = num1 / num2 #Se divide num1 con num2
else:
    division = "No es posible dividir por cero." #Si el valor es cero se imprime esto

# Se imprimen los resultados
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")


# Verificación de Número Par o Impar:
# 2.Solicita un número al usuario y determina si es par o impar.

# Pedimos al usuario para que ingrese dos numeros
numero = int(input("Ingresa un número: "))

#Vamos a analizar si es par o impar
#La expresión % en Python es el operador de módulo que devuelve el residuo de la división de un número por otro.
if numero % 2 == 0: 
    print(f"{numero} es un número par.") # El resultado de la operación es un número par.
else:
    print(f"{numero} es un número impar.") # El resultado de la operación no es un número par.
    
# Área de un Triángulo: 
# 3. Pide la base y la altura de un triángulo al usuario y calcula su área. 

# Solicitamos al usuario que nos dé valores para la altura y base del triángulo
base = float(input("Ingresa la base del triángulo: "))
altura = float(input("Ingresa la altura del triángulo: "))

# Realizamos la formula para hallar el area
area_triangulo = (base * altura) / 2

# Se imprime le resultado.
print(f"El área del triángulo con base {base} y altura {altura} es: {area_triangulo:.2f}")
    

#%% Calculadora de Factorial: 
# 4. Crea una función que calcule la factorial de un número. 

def factorial(n): # Se define el factorial
    if n == 0 or n == 1: #Verificamos si el valor de n es igual a 0 o 1.
        return 1
    else:
        return n * factorial(n-1)# calculamos el factorial de n multiplicándolo por el factorial de n-1

# PEDIMOS UN NUMERO AL USUARIO
numero = int(input("Ingresa un número: "))

# CALCULAMOS EL FACTORIAL Y MOSTRAMOS EL RESULTADO
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")

#%% Número Primo: 
# 5. Verifica si un número ingresado por el usuario es primo o no.

def es_primo(numero):
    if numero < 2: # Verificamos que el número sea menor que 2
        return False # Si el número es menor que 2 retrona False
    for i in range(2, int(numero**0.5) + 1):# Se inicializa un bucle for que itera sobre los valores de i que van desde 2 hasta la raíz cuadrada entera de numero más 1.
        if numero % i == 0:# En cada iteración del bucle se verifica si la variable número es divisible por i.
            return False # Se imprime 
    return True

# Se solicita ingresar un numero:
numero_usuario = int(input("Ingresa un número: "))

# Se verifica si el numero es primo e imprime lo siguiente
if es_primo(numero_usuario):
    print(f"{numero_usuario} es un número primo.") # si es primo
else:
    print(f"{numero_usuario} no es un número primo.") # si no es primo


# Inversión de Cadena:
# 6. Toma una cadena de texto y muestra su inversión. 

def invertir_cadena(cadena): # Se define invertir_cadena como un metodo
    cadena_invertida = cadena[::-1]# Se invierte la cadena
    return cadena_invertida

# Se solicita al usuario una cadena
cadena_original = input("Ingresa una cadena de texto: ")

# nos devuelve la cadena invertida
resultado = invertir_cadena(cadena_original)
print(f"La cadena invertida es: {resultado}")

# Suma de Números Pares: 
# 7.Calcula la suma de los números pares en un rango especificado por el usuario.

# Solicitamos que se ingrese dos numeros para que se considere un rango:
inicio = int(input("Ingresa el inicio del rango: "))
fin = int(input("Ingresa el fin del rango: "))

# Iniciamos un contado en cero:
suma_pares = 0

# Calculamos la suma de los numeros pares dentro del rango definido
for numero in range(inicio, fin + 1): # Agrega +1 a la variable fin
    if numero % 2 == 0:
        suma_pares += numero

#Se imprime el siguiente resultado.
print(f"La suma de los números pares en el rango [{inicio}, {fin}] es: {suma_pares}")


# Lista de Cuadrados:
# 8.  Crea una lista de los cuadrados de los primeros 10 números naturales.

# Se crea una lista con los 10 primeros numeros calculando sus respectivos cuadrados:
cuadrados = [n**2 for n in range(1, 11)]

# Se imprimen los sigueintes resultados:
print("Lista de cuadrados de los primeros 10 números naturales:")
print(cuadrados) # Se llama al metodo


# Contador de Vocales: 
# 9. Cuenta el número de vocales en una cadena de texto. 

# Se solicita al usuario que se ingrese un texto:
cadena = input("Ingresa una cadena de texto: ")

# Se inicializa el contador contador_vocales en cero
contador_vocales = 0

# Se define las vocales en mayusuculas y minusculas
vocales = "aeiouAEIOU"

# la siguiente funcion cuenta las vocales en mayusculas y minusculas
for letra in cadena:
    if letra in vocales:
        contador_vocales += 1

# Se imprime el siguiente resultado:
print(f"El número de vocales en la cadena es: {contador_vocales}")



#%% Números de la Serie Fibonacci:
# 10.Genera los primeros 10 números de la serie Fibonac

#Se crea la funcion para los n nuemros fibonacci:
def fibonacci(n):
    fib_series = [0, 1]  # Se inicializa la serie con los primeros dos números
    while len(fib_series) < n: # Se cuenta la dsitancia 
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

# Se obtiene los 10 primeros numeros fibonacci 

primeros_10_fibonacci = fibonacci(10)

# Se muestra el resultado
print("Primeros 10 números de la serie Fibonacci:")
print(primeros_10_fibonacci)

# Ordenamiento de Lista: 
# 11.Ordena una lista de números ingresados por el usuario de menor a mayor.

# Se solicita al ususario que ingrese numeros
entrada_usuario = input("Ingresa una lista de números: ")

# Se convierte los numeros en una lista:
numeros = [float(numero) for numero in entrada_usuario.split()]

# Se ordena los numeros de la lista de menor a mayor
numeros_ordenados = sorted(numeros)

# Se imprime la respuesta:
print("Lista ordenada de menor a mayor:", numeros_ordenados)


# 12. Verifica si una palabra ingresada por el usuario es un palíndromo. 

def es_palindromo(palabra): #Se defina el palindromo
    palabra = palabra.lower()  # Convierte la cadena de entrada a minúsculas
    palabra_invertida = palabra[::-1]   # Crea una versión invertida de la cadena
    return palabra == palabra_invertida # Se devuelve la cadena invertida

# Se colicita al usuario el ingreso de una palabra:
palabra_usuario = input("Ingresa una palabra: ")

# Con el siguiente metodo se verifica si la palabra es un palindromo.
if es_palindromo(palabra_usuario):
    print(f"{palabra_usuario} es un palíndromo.") # Es un palindromo
else:
    print(f"{palabra_usuario} no es un palíndromo.") # No es un palindromo
    
    
#%% Generador de Tablas de Multiplicar: 
# 13. Crea un programa que genere la tabla de multiplicar de un número ingresado por el usuario.

# Se pide al usuario que ingrese un numero:
numero = int(input("Ingresa un número para generar su tabla de multiplicar: "))

# se imprime la tabla de multiplicar del numero ingresado
print(f"Tabla de multiplicar del {numero}:")

for i in range(1, 11): # Se inicia el bucle en el rango
    resultado = numero * i # En cada iteración se calcula el resultado de la multiplicación del número dado
    print(f"{numero} x {i} = {resultado}") # Se imprime el numero y el resultado

# Cálculo del Área de un Círculo: 
# 14. Pide el radio de un círculo al usuario y calcula su área. 

import math

# Pide un radio al ususario
radio = float(input("Ingresa el radio del círculo: "))

# Calculamos ela rea de un circulo
area_circulo = math.pi * radio**2
# Se imprime el resultado
print(f"El área del círculo con radio {radio} es: {area_circulo:.2f}")

# Suma de Dígitos: 
# 15.  Toma un número entero y calcula la suma de sus dígitos.

# Se pide al usuario que ingrese un numero entero
numero = int(input("Ingresa un número entero: "))

# calculamos la suma de los numeros
suma_digitos = sum(int(digito) for digito in str(abs(numero)))

# Se imprime el resultado
print("La suma de los dígitos es:", suma_digitos)

