# Trabajo Práctico Recursividad, Rojas Maximiliano.


# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
# función para calcular y mostrar en pantalla el factorial de todos los números enteros 
# entre 1 y el número que indique el usuario.

def factorial(n):
    if n == 0:
        return 1
    else:  
        return n * factorial(n-1)

n = int(input("Ingresá un número entero mayor a 0: "))
print(f"El factorial del número ingresado es {factorial(n)}")
for i in range(1, n):
    print(f"El factorial de {i} es {factorial(i)}")

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
# Posteriormente, muestra la serie completa hasta la posición que el usuario especifique. 

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
# Solicitamos la posición.
posicion = int(input("Ingresá la posición hasta la cual querés ver la serie de Fibonacci: "))

# Acá mostramos la serie completa hasta la posición
for i in range(posicion + 1):
    print(f"La posición ({i}) tiene valor = {fibonacci(i)}")

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, 
# utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un algoritmo general. 

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

# Probamos la función con valores ingresados por el usuario.
base = int(input("Ingresá la base: "))
exponente = int(input("Ingresá el exponente (mayor o igual a 0): "))

resultado = potencia(base, exponente)
print(f"{base}^{exponente} = {resultado}")

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal 
#    y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
numero = int(input("Ingresá un número entero positivo: "))
binario = decimal_a_binario(numero)
print(f"El número {numero} en binario es: {binario}")    

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es. 
# Requisitos: 
# La solución debe ser recursiva. 
# No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

palabra = input("Ingrese una palabra: ")
print(es_palindromo(palabra)) 

#  6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo 
#     y devuelva la suma de todos sus dígitos.    
    
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)
n = int(input("Ingrese un número entero: "))
print(f"La suma de todos los digitos es: {suma_digitos(n)}")    

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
#    bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
#     último nivel con un solo bloque. 
 
#    Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
#    nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide. 

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)
n = int(input("Cuantos bloques hay en la base?: "))
print(f"La cantidad total de bloques es: {contar_bloques(n)}")    

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
#    número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
#    aparece ese dígito dentro del número.

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)
numero = int(input("Ingrese un número entero: "))    
digito = int(input("Ingrese un número de 1 dígito: "))
suma = contar_digito(numero, digito)
print(f"El digito {digito} aparece {suma} vez/veces.")