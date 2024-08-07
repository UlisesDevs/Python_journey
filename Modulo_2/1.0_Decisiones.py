'''
Las computadoras conocen dos tipos de respuestas, cierto o falso, nuca obtendras una respuesta
tal como, ummmm tal vez o probablemente si y para este tipo de preuguntas Python utiliza un conjunto de 
operadores muy especiales.

Operador de igualdad == :
    Se encarga de preguntar si dos valores son iguales, no confundir con el operador de asignacion =
    ya que el de igualdad son dos simbolos de igual juntos, el resultado de utilizar este operador sera 
    True o False, ejemplo.
'''
print("2 == 2 es: ", 2 == 2)
print("2 == 2. es: ", 2 == 2.)
print("1 == 2 es: ", 1 == 2)

'''
Operador de desigualdad != :
    Se compone de un signo de admiracion seguido de un signo de igual, esto es el contrario al
    anterior operador ya que se encarga de revisar si dos valores no son iguales, y tambien
    regresara un resultado de True o False, ejemplo.
'''
print("\n2 != 2 es: ",2 != 2)
print("2 != 2. es: ",2 != 2.)
print("1 != 2 es: ",1 != 2)

'''
Operador mayor que > :
    Se encarga de comparar si un valor es mayor a otro, regresara un resultado de True o False.
'''
print("\n10 > 1 es: ",10 > 1)
print("10 > 10 es: ",10 > 10)
print("10 > 20 es: ", 10 > 20)

'''
Operador mayor o igual que >= :
    Se encarga de comparar si un valor es mayor o igual a otro, regresara un resultado de True o False.
'''
print("\n10 >= 1 es: ",10 >= 1)
print("10 >= 10 es: ",10 >= 10)
print("10 >= 20 es: ", 10 >= 20)

'''
Operador menor que < :
    Se encarga de comparar si un valor es menor a otro, regresara un resultado de True o False.
'''
print("\n10 < 1 es: ",10 < 1)
print("10 < 10 es: ",10 < 10)
print("10 < 20 es: ", 10 < 20)

'''
Operador menor o igual que < :
    Se encarga de comparar si un valor es menor o igual a otro, regresara un resultado de True o False.
'''
print("\n10 <= 1 es: ", 10 <= 1)
print("10 <= 10 es: ", 10 <= 10)
print("10 <= 20 es: ", 10 <= 20)

'''
Lo anterior mencionado nos sirve para obtener una respuesta de verdadero o falso y poder tomar una
decisión sobre el futuro de nuestro programa, con esto ahora podemos actualizar nuestra tabla de 
prioridades.

    1 -- +, - unario
    2 -- **
    3 -- *, /, //, %
    4 -- +, - binario
    5 -- <, <=, >, >=
    6 -- ==, !=
'''