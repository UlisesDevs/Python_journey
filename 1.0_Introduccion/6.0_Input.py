'''
Interactuar con el usuario:
    para poder interacuar con el usuario y que este pueda introducir datos a nuestro programa contamos con la funcion
    input(), esta funcion permite al usuario escribir en consola para agregar datos al programa, esto hace a nuestro
    codigo interactivo, es crucial que el metrodo print() sea asignado a una variable si no los datos obtenidos se perderan
    ejemplo:

        escribe = input()
    
    input() puede llevar o no argumentos, aun que con argumentos nos podemos ahorrar alguno que otro print, ejemplo:
'''
#input() sin argumentos
print("Escribe tu nombre: ")
saludo = input()
print("Hola", saludo)

#input() con argumentos
nombre = input("Introduce tu nombre: ")
print("Hola, ", nombre)

'''
los datos introducidos con input() siempre seran una cadena de texto, por lo cual no podemos utilizarlo para realizar 
operaciones matematicas de manera basica, para poder realizar operaciones matematicas debemos hacer una conversion de tipos.
'''
string = input("Introduce el primer numero: ")
string2 = input("Introduce el segundo numero: ")
print("Nota como al ser los dos strings y querer hacer una suma estas se concatenan y no se suman: ", string + string2)

#Nota: al utilizar un simbolo de * en una combinacion de cadenas y numeros este se convierte en un simbolo de replica
print("Nota como el Hola, sera repicado 3 veces: ", 3 * "Hola")
#Recuerda: un numero igual o menor que 0, produce una cadena vacia.

'''
Conversiones de tipos:
    Python nos ofrece dos funciones para especificar un tipo de dato int() y float(), ambas funciones toman un argumento
    e intentan convertirlo a un numero entero o flotante respectivamente, en caso de fallar en la conversion claramente 
    nuestro programa fallara tambien.
'''
numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el segundo numero: "))
print("Ahora si seran sumados: ", numero1 + numero2)

'''
Ahora tenemos una funcion que hace lo contrario, puede convertir un numero a una cadena esta es: str()
'''