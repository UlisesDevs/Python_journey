'''
En Python podemos almacenar diferentes tipos de datos en una variable y esta misma variable la podemos re asignar con otro tipo
de dato diferente, pero solo lo hemos hecho con un tipo de dato a la vez y si quisieramos por ejemplo almacenar los nombres de
distintas mascotas? esto supondria hacer una variable para cada mascota

    perro1 = "Solovino"
    perro2 = "Firulais"

y asi sucesivamente por cada mascota que tengamos, para simplificar esa tarea tenemos las listas, que en resumen es una serie de
datos almacenados en una sola variable.
'''
["Solovino", "Firulais", "Pedro", "Cheems", "Doge"]

'''
Su sintaxis es la siguiente:
    Dentro de corchetes podemos escribir distintos tipos de datos, ya sean strings, enteros, flotantes etc, 
    Nuestra lista pude contener solo un tipo de datos o varios combinados

        [True, False, 1, 2, "texto", 2.5]

    Podemos declarar nuestra lista solo abriendo y cerrando corchetes, pero para poder trabajar con ella
    necesitamos agregarla a una variable 

        mascotas = ["Solovino", "Firulais", "Pedro", "Cheems", "Doge"]

    Al trabajar con listas estas se almacenan en indices, es como si enumeraramos el contenido de la lista, pero
    con la particularidad que se comienzan a enumerar desde el 0 y no del uno, por ejemplo, de la lista de mascotas
    "Solovino" ocupa el indice 0 mientras que "Dogue" ocupa el indice 4, es importante tener esto en cuenta ya que
    para poder trabajar con los elementos de las listas por lo general se mandan a llamar con su indice

    Nuestra lista tiene una longitud, la longitud es el total de elementos dentro de nuestra lista, regresando a nuestra lista de
    mascotas, esta tiene 5 elementos por lo tanto su longitud es de 5, 
'''

#Teniendo lo anterior en cuenta vamos a ver como trabajr con las listas
mascotas = ["Solovino", "Firulais", "Pedro", "Cheems", "Doge"]

print("Imprime la lista de mascotas completa: ", mascotas)

#Imprimir un solo elemento de la lista
print("\nImprime la mascota en el indice 0: ", mascotas[0])
print("\nImprime la mascota en el indice 4: ", mascotas[4])

#Para saber la longitud de nuestra lista usamos la funcion len() y dentro del parentesis la lista de la cual queremos saber su longitud
print("\nLa longitud de la lista mascotas es: ", len(mascotas))

#Para asignar un nuevo valor en un indice en especifico
mascotas[1] = "Grumpy"
print("\nLa lista con el indice 1 actualizado: ", mascotas)

#Podemos copiar el valor de un indice a otro
mascotas[0] = mascotas[4]
print("\nLa lista con el indice 0 copiado del 4: ", mascotas)
#Nota: al acto de actualizar indices individuales dentro de las listas se le conoce como indexacion

#Borrar un elemento dentro de la lista
del mascotas[0]
print("\nLista con el elemento borrado: ", mascotas)
#Al borrar un elemento nuestros indices cambian al igual que la longitud de la lista
print("\nAhora el elemento en el indice 0 es: ", mascotas[0])
print("\nLa nueva longitud de nuestra lista es: ", len(mascotas))

'''
Podemos utilizar indices negativos lo que hara que de acuerdo al numero que especifiquemos comenzara por el ultimo
al primero, ejemplo, el -1 representa al ulltimo elemento de nuestra lista, el -2 el penultimo y asi sucesivamente.
'''
print("\nEl ultimo elemento de nuestra lista es: ", mascotas[-1])
print("\nEl penultimo elemento de nuestra lista es: ", mascotas[-2])