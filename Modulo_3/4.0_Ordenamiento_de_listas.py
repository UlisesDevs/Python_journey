'''
En el mundo de la programacion existen algoritmos ordenacion y de busqueda los cuales se 
encargan de ordenar estructuras de datos y de hacer busquedas dentro de los mismos
'''

'''
Algoritmo burbuja o bubble sort:
    Es un algoritmo que se encarga  de ir comparando los numeros de 2 en 2 y revisar
    cual de ellos es el mayor y asi intercambiar de posicion en caso de que el primer 
    numero sea mayor al segundo, asi el mayor numero pasara a estar a la derecha de la lista
    o si lo vemos de forma vertical, pasara a estar arriba del todo, viendo esta analogia es
    como si las burbujas (Numero mayor) de un refresco flotaran hacia la superficie, por esto
    se le llama algoritmo burbuja, veamos un ejemplo aplicado a Python.
'''
lista = [58, 73, 24, 87, 12, 39, 65, 5, 18, 92, 42, 88, 33, 1, 79, 45, 81, 70, 23, 60]
cambio = True #Declaramos una variable con el nombre cambio y el valor True para entrar al bucle
longitud = len(lista) #Podemos declarar o no esta variable
while cambio:#Como cambio es igual a True entramos al bucle
    cambio = False #Inmediatamente asignamos False a la variable cambio para asumir que al principio no hay cambios, esta misma asignacion es la que nos sacara del ciclo while cuando nuestra lista este ordenada
    for i in range(longitud - 1): #Iniciamos un Bucle for para iterar desde el primer elemento hasta el penultimo, esto se hace por que si iteraramos sobre el ultimo numero y uno mas, este saldria del rango de la lista
        if lista[i] > lista[i + 1]: #Iniciamos nuestra condicional if comparando el numero en el indice i con el numero en el indice i + 1 (el de la izquierda con el de la derecha), esto se asegura que al llegar al penultimo numero se compare con el ultimo por el +1
            lista[i], lista[i + 1] = lista[i + 1], lista[i] #En caso de que la condicion se cumpla quiere decir que necesitamos hacer un intercambio entonces aplicamos el metodo que aprendimos para hacer los intercambios de manera mas facil
            cambio = True #Si ha habido un cambio establecemos nuestra variable cambio a True para asegurarnos de volver a entrar al ciclo while hasta que tengamos todos los numeros ordenados
print("Esta es la lista ordenada con Bubble sort: ", lista)

'''
Ten en mente esto, simpre es importante aprender las bases para saber como funcionan las cosas de manera simplificada
ahora que ya sabes como funciona un algoritmo de ordenamiento simple, podemos utilizar las herramientas que Python
nos brinda y para esto tenemos los metodos .sort() y .reverse() para ordenar nuestra lista y para invertirla, veamos como funciona.
'''
lista = [58, 73, 24, 87, 12, 39, 65, 5, 18, 92, 42, 88, 33, 1, 79, 45, 81, 70, 23, 60]
lista.sort()
print("\nLista ordenada con .sort(): ", lista)
lista.reverse()
print("\nLista invertida con .reverse(): ", lista)

#Nota: los metodos anteriores tambien funcionan para listas de string
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
nombres_mascotas.sort()
print("\nLista de mascotas ordenada: ", nombres_mascotas)
nombres_mascotas.reverse()
print("\nLista de mascotas invertida: ", nombres_mascotas)