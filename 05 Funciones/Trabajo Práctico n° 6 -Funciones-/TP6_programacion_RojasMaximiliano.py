
# TP Funciones.

# 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. 
#    Llamar a esta función desde el programa principal.

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()    

#  2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre 
#     y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), 
#     deberá de volver: “Hola Marcos!”. 
#     Llamar a esta función desde el programa principal solicitando el nombre al usuario

def saludar_usuario(nombre):
    return (f"Hola {nombre}!")

nombre_usuario = input("Ingrese su nombre: ")
print(saludar_usuario(nombre_usuario))

# 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros
#    e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
#    Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def infomacion_personal(nombre, apellido, edad, residencia):
    return(f"Soy {nombre} {apellido} tengo {edad} años y vivo en {residencia}")

nombre_usuario = input("Hola! por favor, ingresá tu nombre: ")
apellido_usuario = input("Ingresá tu apellido: ")
edad_usuario = input("Ingresá tu edad: ")
residencia_usuario = input ("Decime de donde sos: ")

print(infomacion_personal(nombre_usuario, apellido_usuario, edad_usuario, residencia_usuario))

#  4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva 
#     el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva 
#     el perímetro del círculo. Solicitar el radio al usuario y llamabas funciones para mostrar los resultados.

import math

def calcular_area_circulo(radio):
    area = (radio**2) * math.pi
    return(f"El area del circulo es {area:.2f}") 

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return(f"El perimetro del circulo es {perimetro:.2f}") 

radio_usuario = float(input("Por favor, ingrese el radio que desea calcular: "))

print(calcular_area_circulo(radio_usuario)," y ",(calcular_perimetro_circulo(radio_usuario)))

#  5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro
#     y devuelva la cantidad de horas correspondientes. 
#     Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    horas = segundos // 3600
    return horas

segundos = int(input("Ingrese la cantidad de segundos deseada: "))
print("La cantidad de horas ingresadas son:",segundos_a_horas(segundos))

#  6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro 
#     e imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range (1, 11):
        print(f"{numero} x {i} = {numero * i}")

num = int(input("Ingrese un número: "))  
tabla_multiplicar(num)  

#  7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros 
#     y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
#     Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return(f"La suma de {a} + {b} es: {suma}\n"
           f"La resta de {a} - {b} es: {resta}\n"
           f"la multiplicacion de {a} * {b} es: {multiplicacion}\n"
           f"La division de {a} / {b} es: {division:.2f}")

num1 = int(input("Ingrese un primer núumero: "))
num2 = int(input("Ingrese un segundo número: "))
print(operaciones_basicas(num1, num2))    

#  8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, 
#     y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar
#     el resultado con dos decimales.

def calcular_imc(peso, altura):
    indice_masa_corporal = peso / (altura ** 2)
    return indice_masa_corporal

peso = float(input("Por favor ingrese su peso (kg): "))
altura = float(input("Ahora ingrese su altura (mts): "))

imc = (calcular_imc(peso, altura))
print(f"Su Indice de Masa Corporal es: {imc:.2f}")

#  9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius 
#     y devuelva su equivalente en Fahrenheit. 
#     Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

def celsius_a_farenheit(celsius):
    temperatura = (celsius * 9/5) + 32
    return temperatura

grados_celsius = float(input("Por favor ingrese la temperatura en grados celsius: "))
grados_farenheit = celsius_a_farenheit(grados_celsius)

print(f"La temperatura {grados_celsius} celsius en grados farenheit es: {grados_farenheit:.2f} ")

#  10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva 
#     el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

num1 = int(input("Ingrese la primer nota: "))
num2 = int(input("Ingrese la segunda nota: "))
num3 = int(input("Ingrese la tercer not: "))

print("El promedio de sus notas es ", calcular_promedio(num1, num2, num3))