'''
Podemos anidar listas en listas es decir, tener una lista de listas, a esto
tambien se le conoce como matriz
'''

lista_1 = [
            [1,2,3,4,5],
            [1,2,3,4,5],
            [1,2,3,4,5],
            [1,2,3,4,5]
          ]

#De esta forma accederemos a cada uno de los elementos dentro de nuestra matriz
for i in lista_1:
    for j in i:
        print(j)

'''
Comprecion de listas:
    Este es un metodo para crear listas sobre la marcha, conforme las vayamos necesitando
    asi no es necesario crear listas estaticas, su sintaxis es la siguiente:

        variable = [ expresión for elemento in iterable ]
'''
#Crea una lista del 1 al 10
lista_creada = [i for i in range(1,11)]
print("\nLista del 1 al 10: ",lista_creada)

#Crea una lista del 1 al 10 de numeros al cuadrado
cadrado = [i ** 2 for i in range(1,11)]
print("\nLista al cuadrado: ",cadrado)

'''
Sitaxis con condicion (filtrado)

    [ expresión for elemento in iterable if condición ]

'''
#Crea una lista con numeros pares
pares = [i for i in range(1,11) if i % 2 == 0]
print("\nLista de numeros pares: ", pares)

'''
Arreglos de dos dimensiones, seria la forma de crear una lista de listas o matriz
'''
tablero = [[i for i in range(8)] for j in range(8)]
print("\nTablero: ", tablero)

'''
Recuerda que la naturaleza de un matriz es multi dimencional, puedes tener matrices
de dos 3, 4 dimenciones, las que necesites, para encontrar un elemento dentro 
de una matriz siempre vas a necesitar dos coordenadas, una vertical (numero de fila)
y una horizontal (numero de columna) 
'''