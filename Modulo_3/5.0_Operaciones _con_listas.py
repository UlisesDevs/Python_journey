'''
Copiando listas:
    Cuando tratamos de copiar una lista podemos asignar una nueva variable con la variable
    que contiene nuestra lista original? vamos a ver si es posible.
'''
list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)
'''
Te daras cuenta que el resultado al momento de imprimir nuestra lista es 2 y no 1 esto es por
que al copiarla de esa manera copiamos el espacio en memoria asignado a esa lista, por lo tanto
cualquier cambio que realicemos en nuestra primer lista se reflejara en la segunda, pero
si lo que nosotros queremos hacer es copiar la primer lista sin que en la segunda se
realicen los cambios que se le hagan a la primera?, para eso tenemos el operador slice ":"
'''

'''
Operador Slice:
    Este operador nos sirve para copiar el contenido de una lista a una nueva lista
'''
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)
'''
Ahora veras que el resultado al imprimir nuestra segunda lista esta vez es 1 y no 2 como anteriormente,
utilizando el operador solo nos servira para copiar la lista entera
'''
lista = [2, 6, 8, 34, 0, 12]
lista_2 = lista[:]
lista.append(54)
print("Imprime la lista 1: ", lista)
print("Imprime la lista 2: ", lista_2)
'''
Tambien podemos copiar porciones de la lista con la siguiente sintaxis:

    lista_a_copiar[primer_indice:ultimo_indice]

Nota: no se copiara el ultimo indice si no uno anterior al especificado
'''
lista_3 = lista[0:4]
print("Imprime la lista 3: ", lista_3)
#Tamnien funciona con indices negativos
lista_4 = lista[2:-1]
print("Imprime la lista 4: ", lista_4)
'''
Si se omite el primer indice se infiere que queremos copiar desde el indice 0
seria lo mismo que escribir [0:4]
'''
lista_5 = lista[:3]
print("Imprime la lista 5: ", lista_5)
'''
Por otro lado si lo que se omite es el ultimo indice se infiere
que queremos copiar la longitud de la lista y seria lo mismo que escribir

    [1:len(lista_original)]
'''
lista_6 = lista[2:]
print("Imprime la lista 6: ", lista_6)
#Nota: como lo que copiamos es la longitud que al momento es de 7 en este caso, 7 - 1 = 6 por lo tanto se copia el ultimo indice de nuestra lista tambien

'''
Borrando contenido de las listas con el operador slice:
    Para borrar contenido de una lista con el operador slice podemos utilizar la misma sintaxis

        del mi_lista[1:3]
'''
lista = [2, 6, 8, 34, 0, 12]
print("\nLista: ", lista)
del lista[:] #Borrara todo el contenido de la lista
print("Lista borrada: ", lista)
lista = [2, 6, 8, 34, 0, 12]
del lista[1:4]
print("Lista borrada del indice 1 al 4: ", lista)

'''
Comprobando si hay o no elementos dentro de una lista:
    para esto utilizaremos utilizaremos las palabras reservadas "in" y "not in"
    los cuales nos regresaran un Booleano True o False y su sintaxis es la siguiente:

        elemento in my_list
        elemento not in my_list
'''
my_list = [0, 3, 12, 8, 2]
print("\nLista: ", my_list)
print("5 esta en la lista?: ", 5 in my_list)
print("5 no esta en la lista?: ", 5 not in my_list)
print("12 esta en la lista?: ",12 in my_list)




