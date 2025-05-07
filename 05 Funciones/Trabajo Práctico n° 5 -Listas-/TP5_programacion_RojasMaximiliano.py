# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

lista = list(range(4, 101, 4))
print(lista)

# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. 
#   ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos! 

lista_5_elementos = ['A', 'B', 'C', "ROJO", "BLANCO"]
print(lista_5_elementos[3])

print(lista_5_elementos[-2])  # Usando indexing

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla.

lista_vacia = []
lista_vacia.append(2025)            # Con append agrego un valor
lista_vacia.append('mayo')
lista_vacia.append(True)
ex_lista_vacia = lista_vacia        # Como el estado de la lista cambió, también el nombre final.
print(ex_lista_vacia)

# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente.

animales = ['perro', 'gato', 'conejo', 'pez']

animales[1] = 'loro'    # El segundo valor de la lista está en el indice [1]
animales[3] = 'oso'
animales[-3] = 'loro'
animales[-1] = 'oso'
print(animales)

# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

# numeros = [8, 15, 3, 22, 7] 
# numeros.remove(max(numeros))
# print(numeros)

    # Lo que sucede en este programa es que la función max() identifica el valor máximo de la lista señalada (numeros)
    # entonces numeros.remove indica que se va a remover un valor de la lista numeros. Finalmente numeros.remove(max(numeros)) indica que 
    # se removerá el valor máximo de la lista en cuestión.

# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.

lista_10_a_30 = list(range (10, 30+1, 5)) 
print(lista_10_a_30[0:2])

# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.
 
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "partner"
autos[2] = "Gordini"
print(autos)

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. 
#     Imprimir la lista resultante por pantalla. 

dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)

# Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes: 
#   compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]] 
#       a) Agregar "jugo" a la lista del tercer cliente usando append. 
#       b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente. 
#       c) Eliminar "pan" de la lista del primer cliente.  
#       d) Imprimir la lista resultante por pantalla. 

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("Jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)

# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos: 
#     ● Posición lista_anidada[0]: 15 
#     ● Posición lista_anidada[1]: True 
#     ● Posición lista_anidada[2][0]: 25.5 
#     ● Posición lista_anidada[2][1]: 57.9 
#     ● Posición lista_anidada[2][2]: 30.6 
#     ● Posición lista_anidada[3]: False 
#     Imprimir la lista resultante por pantalla.

lista_anidada = [15,True,[25.5, 57.9, 30.6],False]         
print(lista_anidada)                                # Acá ingresé los valores directamente a cada posición.

# Segunda versión asignando los valores con .append.
lista_anidada2 = []
lista_anidada2.append(15)
lista_anidada2.append(True)
lista_anidada2.append([])
lista_anidada2.append(False)
lista_anidada2[2].append(25.5)
lista_anidada2[2].append(57.9)
lista_anidada2[2].append(30.6)
print(lista_anidada2)                              
