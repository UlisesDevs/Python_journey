'''
Alcances o Scopes:

    En Python, scope se refiere al contexto en el que las variables y nombres
    son visibles y accesibles. Determina qué variables se pueden usar en diferentes
    partes de tu código. Python maneja el scope de manera jerárquica y estática, lo que
    significa que cada variable tiene un alcance determinado en el momento en que el
    código es compilado, y no cambia durante la ejecución.

Tipos de Scope en Python:

Python utiliza una regla conocida como LEGB para determinar el alcance de las variables:

    Local (L): El scope local es el que pertenece a una función. Las variables definidas
    dentro de una función solo son accesibles desde esa función.

    Enclosing (E): Si una función está anidada dentro de otra, el scope enclosing
    es el que pertenece a la función que envuelve a la función interna.

    Global (G): Las variables globales son las que están definidas en el nivel del módulo,
    es decir, fuera de todas las funciones y clases.

    Built-in (B): Estas son las variables y funciones que vienen predefinidas en Python,
    como print(), len(), etc.
'''

#Scope local:
def funcion_local():
    x = 10  # 'x' es una variable local
    print(x)

funcion_local()

#Scope Enclosing
def funcion_externa():
    x = 20
    def funcion_interna():
        print(x)  # 'x' está en el scope de la función que encierra a funcion_interna
    funcion_interna()

funcion_externa()

#Scope Global
x = 30  # 'x' es una variable global

def funcion_global():
    print(x)  # Puede acceder a la variable global 'x'

funcion_global()

#Para modificar una variable global dentro de una función, debes usar la palabra clave global:
x = 100  # Variable global

def modificar_global():
    global x
    x = 200  # Modifica la variable global 'x'

modificar_global()
print(x)

'''
Si estás trabajando con funciones anidadas y quieres modificar una variable en el enclosing scope
(el scope de la función externa), puedes usar la palabra clave nonlocal:
'''
def funcion_externa():
    x = 50
    def funcion_interna():
        nonlocal x  # Modifica la variable en el scope de 'funcion_externa'
        x = 75
    funcion_interna()
    print(x)

funcion_externa()



