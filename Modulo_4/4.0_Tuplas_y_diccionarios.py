'''
Antes de comenzar hay un par de conceptos que tenemos que repasar antes de entrar de lleno
con estos dos nuevos tipos de datos.

El primero es la mutabilidad e inmutabilidad:

    Esto se refiere a que un tipo de dato puede ser cambiado durante la ejecucion de nuestro
    programa o no puede, al que se puede cambiar se le llama mutable, al que no se puede
    cambiar se le llama inmutable.

El segundo seria los datos secuenciales:

    Estos hacen referencia a un tipo de dato el cual puede ser analizado secuencialmente
    elemento por elemento por el ciclo for, la lista es uno de ellos.
'''

'''
Tuplas:

    Una tupla es similar a una lista, con la diferencia que la tupla utiliza parentsis
    a diferencia de la lista que utiliza corchetes, ademas la tupla es inmutable, por
    lo cual solo puede ser leido.
'''
#Para declarar una tupla podemos declararla directamente con parentesis o solo comas.
tupla_1 = ("a", "b", "c", "d")
print("Esta es la tupla 1: ", tupla_1)
tupla_2 = "c", "d", "e", "f"
print("Esta es la tupla 2: ", tupla_2)

#Tupla vacia
tupla_vacia = ()

#Tupla de un solo elemento
tupla_de_un_solo_elemento = (1,)
print("Esta es la tupla de un solo elemento: ", tupla_de_un_solo_elemento)
#Es necesario agregar una coma despues del primer elemento al crear una tupla de un solo elemento para que se reconozca como tupla

#Para acceder a los elementos de una tupla se hace por medio de indices similar a las listas
my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print(elem)#Ya que podemos acceder a la tupla mediante el ciclo for significa que es secuencial


'''
Diccionarios:

    El diccionario es una estructura de datos secuencial ademas de ser mutable, esta tiene una estructura
    de claves y valores, siendo la clave la que esta a la izquierda de los dos puntos (:) y el valor el que
    se encuentra a la derecha, su sintaxis es la siguiente.
'''
numeros_de_telefono = {"Ulises": 5566133043, "Julio": 5574652371} #Los nombres son las claves y los numero los valores
print("Este es el diccionario de numeros telefonicos: ", numeros_de_telefono)

#Tambien podemos declarar diccionarios con solo cadenas de texto
alumnos = {"alumno_1": "Ulises", "alumno_2": "Julio"}
print("Este es el diccionario de alumnos: ", alumnos)
#Si se quiere declarar un diccionario vacio solo se escriben las llaves sin contenido
diccionario_vacio = {}

'''
Aqui hay ciertas reglas con los diccionarios:

    Cada clave debe de ser única, no es posible tener una clave duplicada.

    Una clave puede ser un de dato de cualquier tipo, puede ser un número (entero o flotante), incluso una cadena
    pero no una lista.

    Un diccionario no es una lista, una lista contiene un conjunto de valores numerados, mientras que un diccionario
    almacena pares de valores.

    La función len() aplica también para los diccionarios, regresa la cantidad de pares (clave-valor) en el diccionario.

    Un diccionario es una herramienta de un solo sentido, si fuese un diccionario español-francés, podríamos buscar en
    español para encontrar su contraparte en francés más no viceversa.
'''

#Accediendo al valor de una clave.
print("El numero de Ulises es: ", numeros_de_telefono["Ulises"])
#No se puede utilizar una clave que no exista

#Utilizando la sintaxis anterior podemor iterar sobre el diccionario
for alumno in alumnos:
    print(f"El nombre del {alumno} es: ", alumnos[alumno])

'''
Metodos y funciones de los diccionarios:

    .keys(): retorna una lista con todas las claves dentro de un diccionario
'''
print("Estas son las claves del diccionario de alumnos: ", alumnos.keys())

#items(): Retorna una lista con tuplas de cada clave y valor
print("Este es el ejemplo de items(): ", alumnos.items())

'''
Modificar, agregar y borrar valores:

    Ya que los diccionarios son mutables es sencillo modificar sus valores
'''
#Agregar un nuevo valor a el diccionario de alumnos
alumnos["alumno_3"] = "Juan"
print("Este es el diccionario con el nuevo alumno agregado: ", alumnos)

#Modificar un valor ya existente
alumnos["alumno_3"] = "Jose"
print("Este es el diccionario con el alumno modificado: ", alumnos)

#Tambien podemos agregar nuevos con el metodo .update()
alumnos.update({"alumno_4": "Ricardo"})
print("Este es el diccionario con el nuevo alumno agregado mediante el metodo update(): ", alumnos)
#o modificar uno ya existente con el mismo metodo
alumnos.update({"alumno_1": "Mictlan"})
print("Este es el diccionario con el alumno 1 modificado mediante el metodo update(): ", alumnos)

#Para borrar un valor utilizamos la palabra clave del
del alumnos["alumno_1"]
print("Este es el diccionario con el alumno 1 borrado mediante la palabra clave del: ", alumnos)

#Para imprimir solo los valores utilizamos el metodo .values():
print("Estos son los valores del diccionario de alumnos: ", alumnos.values())

#Para devolver una lista ordenada utilizamos la funcion sorted()
print("Esta es una lista ordenada de los valores del diccionario alumnos: ", sorted(alumnos.values()))

#Extra, para eliminar el ultimo valor utilizamos el metodo .popitem():
alumnos.popitem()
print("Diccionario con el ultimo valor borrado mediante .popitem():", alumnos)


#El siguiente programa es un ejemplo de como los diccionarios y las tuplas pueden trabajar juntos
#Descomenta el codigo para que veas el funcionamiento ojo este programa aun no cuenta con manejo de errores(error handler):
'''
school_class = {}

while True:
    name = input("Ingresa el nombre del estudiante: ")
    if name == '':
        break
    
    score = int(input("Ingresa la calificación del estudiante (0-10): "))
    if score not in range(0, 11):
	    break

    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)
        
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)
'''

