# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
#    deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. 

edad = int(input("Por favor ingrese su edad: "))

if edad > 18:
    print("Es mayor de edad")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
#    mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.   

nota = int(input("Por favor ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")    

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
#    número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; }
#    en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
#    operador de módulo (%) en Python para evaluar si un número es par o impar.     

num = int(input("Por favor ingrese un número: "))

if num % 2 == 0:
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par.")    

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
#    siguientes categorías pertenece: 
#       ● Niño/a: menor de 12 años. 
#       ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
#       ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
#       ● Adulto/a: mayor o igual que 30 años.     

edad2 = int(input("Ingrese su edad: "))

if edad2 >= 30:
    print("Eres adulto/a.")
elif edad2 >= 12 and edad2 < 18:
    print("Eres adolescente.") 
elif edad2 >= 18 and edad2 < 30:
    print("Eres adulto/a joven.")       
else:
    print("Eres niño/a.")
    
# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
#   (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
#   pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
#   pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
#   de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string. 

texto = "Hola"
print(len(texto))

contrasena = input("Ingrese su contraseña:")

if len(contrasena) >= 8 and len(contrasena) <= 14:
    print("Ha ingresado una constraseña correcta")
else:
    print("Por favor ingrese una contraseña entre 8 y 14 caracteres")    

# 6) La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se 
#   pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio: 
#       ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la 
#   mediana es mayor que la moda. 
#       ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, 
#   la mediana es menor que la moda. 
#       ● Sin sesgo: cuando la media, la mediana y la moda son iguales. 
#   Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista 
#   numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
#   hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. 

import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 

from statistics import mode, median, mean 

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana and media > moda:
        print(f"Hay sesgo positivo porque media({media}) es mayor que la mediana({mediana}) y mediana mayor que moda({moda}).")
elif moda > mediana and mediana > media:
       print(f"Hay sesgo negativo porque media({media}) es menor que la mediana({mediana}) y mediana menor que moda({moda}).") 
else:
       print(f"No hay sesgo porque media({media}), mediana({mediana}) y moda({moda}) son iguales.")   

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
#   termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; 
#   en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

frase = input("Ingrese la frase o palabra: ")

if frase[-1] in "aeiou":
    frase +="!"
    print(frase)
else:  
    print(frase)     

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
# dependiendo de la opción que desee: 
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
# usuario e imprimir el resultado por pantalla.

nombre = input("Por favor ingrese su nombre: ")
num = int(input("Ingrese por favor como desea que se escriba su nombre:(1) mayúsculas, (2) minúsculas (3) primer letra en mayúsculas: "))

if num == 1:
    print(nombre.upper())
elif num == 2:
    print(nombre.lower()) 
else:
    print(nombre.title())      

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
#    magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla: 
#       ● Menor que 3: "Muy leve" (imperceptible). 
#       ● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
#       ● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños). 
#       ● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras débiles). 
#       ● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
#       ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).     

magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve" " (imperceptible).")
elif magnitud >= 3 and magnitud < 4:
    print("Leve" " (ligeramente perceptible).")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado" " (sentido por personas, pero generalmente no causa daños).")   
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte" " (puede causar daños en estructuras débiles).")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte" " (puede causar daños significativos).")     
else:
    print("Extremo" " (puede causar graves daños a gran escala).")

# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año 
#     Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
#     del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
#     si el usuario se encuentra en otoño, invierno, primavera o verano.


hemisferio = input("En que hemisferio se encuentra? ('N' para norte - 'S' para sur): ").upper()
mes = int(input("Por favor ingrese el mes: (1 -12) "))
dia = int(input("Por favor igrese el dia: (1 - 31) "))

if hemisferio == "N":
    if (1 <= mes <= 2) or dia >= 21 and mes == 12 or dia <= 20 and mes == 3:
        print("Usted se encuentra en invierno")
    elif (4 <= mes <= 5) or dia >= 21 and mes == 3 or dia <= 20 and mes == 6:
        print("Usted se encuentra en primavera")
    elif (7 <= mes <= 8) or dia >= 22 and mes == 6 or dia <= 20 and mes == 9:
        print("Usted se encuentra en verano")
    elif (4 <= mes <= 5) or dia >= 21 and mes == 3 or dia <= 20 and mes == 6:
        print("Usted se encuentra en otoño")
elif hemisferio == "S":
     if (1 <= mes <= 2) or dia >= 21 and mes == 12 or dia <= 20 and mes == 3:
        print("Usted se encuentra en verano")
     elif (4 <= mes <= 5) or dia >= 21 and mes == 3 or dia <= 20 and mes == 6:
        print("Usted se encuentra en otoño")
     elif (7 <= mes <= 8) or dia >= 22 and mes == 6 or dia <= 20 and mes == 9:
        print("Usted se encuentra en invierno")
     elif (4 <= mes <= 5) or dia >= 21 and mes == 3 or dia <= 20 and mes == 6:
        print("Usted se encuentra en primera")               