'''
Que pasa cuando tenemos una lista y queremos mandar llamar uno por uno los elementos
que estan dentro de esta? para hacer uso de estos, por ejemplo imprimir por 
separado cada uno de ellos, tal vez en listas cortas se te haga facil escribir
print(lista[0]), print(lista[1]) y asi sucesivamente, pero en casos donde nuestra lista 
este formada por 10 elementos o mas, esta tarea se vuelve tediosa con ese metodo, es aqui
donde podemos utilizar el ciclo for, para poder iterar sobre cada uno de nuestros elementos
y hacer algo con ellos, ejemplo  
'''
nombres_mascotas = [
    "Luna",
    "Max",
    "Bella",
    "Rocky",
    "Lucy",
    "Charlie",
    "Milo",
    "Daisy",
    "Toby",
    "Nala",
    "Simba",
    "Cooper",
    "Mia",
    "Buddy",
    "Chloe"
]

'''
Esto imprimira todo el contenido de la lista uno por uno sin importar si agregamos 
o quitamos elementos de nuestra lista
'''
for i in range(len(nombres_mascotas)):
    print(nombres_mascotas[i])

#Y que si tenemos una lista con enteros y queremos sumar el total de ellos?
numeros = [23, 56, 2, 7, 23, 19, 8, 6]
total = 0
for i in range(len(numeros)):
    total += numeros[i]
print("\nEl total de la suma de la lista es: ", total)

'''
Un segundo aspecto del ciclo for es que puede ocultar las acciones que se conectan
a la indexacion y entregar todos los elementos de manera practica
'''
total = 0 
for numero in numeros:
    total += numero
print("\nEl segundo aspecto de for: ", total)

#Apliquemos lo mismo para la lista de mascotas
for nombre in nombres_mascotas:
    print(nombre)
#Esta forma itera directamente sobre los elementos de la lista sin utilizar indices
#Por lo cual lo vuelve mas conciso y legible

#Para poder intercambiar valores dentro de una lista podemos utilizar lo siguiente
numeros[0], numeros[-1] = numeros[-1], numeros[0]
numeros[1], numeros[-2] = numeros[-2], numeros[1]
print("\nLa lista de numeros con los valores intercambiados", numeros)
#Pero para hacerlo automatico en una lista mas larga?
length = len(numeros)
for i in range(length // 2):
    numeros[i], numeros[length - i - 1] = numeros[length - i - 1], numeros[i]
print("\nLa otra lista con los cambios automaticos: ", numeros)

