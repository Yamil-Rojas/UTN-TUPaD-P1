# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
#   (incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 

for num in range(0,100+1):
    print(num)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
#    dígitos que contiene.

num = int(input("Ingresa un número: "))
cant_digitos = len(str(num))
    #el input puede tambien no llevar la conversión a int y eso ahorra la conversion a str posterior
    # -pero no exactamente lo que pide la consigna)
print(f"El número ingresado contiene {cant_digitos} dígitos. ")    

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
#    dados por el usuario, excluyendo esos dos valores. 

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
acu = 0

if num1 > num2:
    for i in range (num2+1, num1):
        acu += i
else:        
    for i in range (num1+1, num2):
        acu += i
print(f"La suma de todos los valores del rango es {acu}")       

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia.
#    El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0. 

num = int(input("Ingresa un número (0 para terminar): "))
acu = 0 

while num != 0:
    acu += num
    num = int(input("Ingresa un número (0 para terminar): "))

print(f"El total acumulado es {acu}")    

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#    programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

num_aleatorio = random.randint(0, 9)
contador = 1
adivinar = -1

while adivinar != num_aleatorio: 
    adivinar = int(input("Adivina cual es el número secreto entre 0 y 9: "))
    contador += 1 

print(f"Correcto! lo has logrado en {contador} intentos.")
    
#  6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
#     entre 0 y 100, en orden decreciente.

for i in range (100-2, 0, -2):
    print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
# número entero positivo indicado por el usuario. 

num = int(input("Ingrese un número entero positivo: "))
acu = 0

if num > 0:
    for i in range (0, num): #Si quiero incluir el valor que otorga el usuario escribo num+1
        acu += i
else:
    print("El número debe ser positivo")        

print(f"La suma total es: {acu}")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, 
#    el programa debe indicar cuántos de estos números son pares, cuántos son impares, 
#    cuántos son negativos y cuántos son positivos. 
# (Nota: para probar el programa puedes usar una cantidad menor, 
# pero debe estar preparado para procesar 100 números con un solo cambio). 

pares = impares = positivos = negativos = 0

for i in range (5): #puede modificarse el rango a la cantidad deseada
    num = int(input("Ingrese un número: "))

    if num % 2 == 0:
        pares += 1
    else:
        impares += 1  
    if num > 0:
        positivos += 1
    else:
        negativos += 1
        
print (f"Los números pares son: {pares}. \nLos números impares son: {impares}.")
print(f"Los números positivos son: {positivos}. \nLos números negativos son: {negativos}.")                

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
#    media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
#    poder procesar 100 números cambiando solo un valor).        

contador = 0
acumulador = 0

for i in range (5): #puede modificarse el rango a la cantidad deseada
    num = int(input("Ingrese un número: "))
    contador += 1
    acumulador += num

media = acumulador / contador
print(f"La media es: {media}")    

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. 
#     Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = int(input("Ingrese un número: "))
invertido = 0

while num > 0:
    digito = num % 10
    invertido = invertido * 10 + digito
    num = num // 10

print(invertido)     