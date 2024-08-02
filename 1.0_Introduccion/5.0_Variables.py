'''
Variables:
    un variable es un espacio en la memoria que se guarda con un valor para despues ser utilizado,
    estas se componen de un nombre y un valor.

Reglas para nombrar una variable:
    Puede estar compuesto por MYUSCULAS, minusculas, digitos y el caracter _
    Debe comenzar con una letra
    El carater _ es considerado un letra
    Hay distincion de mayusculas y minusculas
    No utilizar palabras reservadas
    No comenzar con numeros
    En caso de tener mas de una plabras debe de escribirse en snake_case
    No deben tener espacios

Si quieres revisar la guia de estilos completa visita este enlace:

    https://peps.python.org/pep-0008/

'''
palabras_reservadas = ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

'''
Como crear una variable:
    Una variable puede almacenar cualquier cosa
    para crear una variable hay que seguir la siguiente sintaxis:
        asignarle un nombre, despues con el signo de = asignaremos el valor que esta almacenara ejemplo:

            variable = 1
'''

#Para asignar un nuevo valor a un variable ya existente basta con escribir su nombre y asignarle el nuevo valor, ejemplo:
numero = 1
print("Este es el valor inicial de la variable: ", numero)
numero = numero + 1
print("Este es el nuevo valor de la variable: ", numero)

'''
Operadores abreviados:
    Se utilizan cuando queremos asignar un valor nuevo a nuestra variable con la misma variable, ejempplo:

        numero = numero + 1

    El metodo abreviado para estos casos seria:

        numero += 1
    
    Esto aplica para todos nuestros operadores
'''

'''
Comentarios:
    Los comentarios sirven para poder indicar a quien este leyendo el codigo como funciona, o el significado de algunas variables
    tambien para poder documentar nuestro programa.
    Este tipo de texto es omitido a la hora de compilar nuestro programa por lo cual no sera mostrado al usuario

Los desarrolladores buenos y responsables describen cada pieza importante de código, por ejemplo, el explicar el rol de una variables. Aunque la mejor manera de comentar una variable es dándole un nombre que no sea ambiguo.

Tambien podemos utilizarlo para marcar parte de nuestro codigo que no se necesite actualmente por cualquier razon, ejemplo:

    #print("Este print no se necesita por el momento")

su sintaxis es la siguiente:
'''
#Para agregar comentarios de una sola linea tenemos que colocar el signo # al principio de la linea.
'''
Para agregar comentarios de varias lineas utilizamos 6 comillas, 3 al principio de nuestro
texto y 3 al final de nuestro texto.
'''