'''
Una funcion no pertenece a ningun dato y su forma de invocarla es la siguiente:

    result = function(argument)

Un metodo es propiedad de los datos para los que trabaja y su forma de invocar es la 
siguiente:

    result = list.method(argument)

Los metodos se pueden comportar como funciones pero cambian el estado interno de los 
datos para los que fue invocado
'''

'''
Metodos de listas:

    El mtodo .append() agregara un elemento al final de nuestra lista
'''
mascotas = ["Solovino", "Firulais", "Pedro", "Cheems", "Doge"]
#Agregamos un elemento de tipo string al final de nuestra lista mascotas
mascotas.append("Trololocat")
#Veamos como cambia nuestra lista
print("La lista con el nuevo elemento al final: ", mascotas)

'''
El metodo .insert() solicita dos argumentos el primero es el indice donde queremos insertar
el nuevo elemento y el segundo sera el elemento a insertar, separado por comas

    list.insert(indice, elemento)
'''
mascotas.insert(0, "Paul")
print("\nLa lista con el nuevo elemento insertado: ", mascotas)
'''
Como te daras cuenta este metodo inserta un nuevo elemento y recorre a la derecha los 
elementos existentes
'''
#Podemos delcarar una lista vacia para despues ir insertando los elementos como se requieran
alumnos = []
nuevo_alumno = alumnos.append(input("\nIngrese el nuevo alumno: "))
print("Lista con el nuevo alumno: ", alumnos)