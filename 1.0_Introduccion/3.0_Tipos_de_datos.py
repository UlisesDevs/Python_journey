'''
Literales:
    una literal es un valor fijo en el codigo, este puede ser de distintos tipos y se pueden almacenar o no en variables
    existen literales que por si solas nos dan a entender el valor que tienen como, los numeros enteros, flotantes, booleanos
    pero las cadenas de texto necesitan forsosamente de comillas para identificarlas como tal ejemplo, "Esta es una cadena de texto"
    estas tambien representan los tipos de datos.

Numeros enteros:
    Son todos aquellos que no tienen una parte fraccionaria (o punto decimal), al declarar un tipo de dato como numero entero o asiganrlo
    a una variable no puede contener otra cosa en el que no sean numeros, por ejemplo si queremos declarar un numero que represente
    millones por legibilidad lo escribimos de esta manera: 1,000,000 pero Python no acepta este tipo de notacion por lo tanto 
    debemos representarlo asi: 1000000, pero si te das cuenta es difil de leer a simple vista, para esto Python nos permite 
    anotar numeros con guiones bajos ejemplo: 1_000_000, vamos a ver un par de ejemplos.
'''
numero_grande = 1000000
numero_grande_con_guion_bajo = 1_000_000
print(numero_grande, numero_grande_con_guion_bajo)
'''
Para codificar numeros negativos seguimos la misma sintaxis pero agregamos un guion medio al numero ejemplo: -10, en este caso
tambien aplica la misma regla de los guiones bajos.

Python tambien acepta la notacion de numero octales (0o20) y hexadecimales (0x1A), al igual si queremos convertir decimales
a estos dos ultimos podemos utilizar las funciones oct() y hex() ejemplo:
'''
numero_octal = 8
print(oct(numero_octal))
numero_hexadecimal = 10
print(hex(numero_hexadecimal))

'''
Numeros flotantes:
    Son aquellos numeros que tienen una parte decimal no vacia, al igual que con los enteros este solo acepta numeros y el punto
    una pequeña regla es que que se puede omitir el 0 cuando es el unico antes del punto decimal ejemplo: .5 o 1.
    esto no cambiara su tipo ni su valor.
    
    Hay que tener en cuenta que el punto es el que define si un numero es entero o flotante, ya que no es lo mismo 4 que 4.0
    por que Python los interpreta de maneras distintas

    En ambos casos para enteros y flotantes, para representar numero muy grandes o muy pequeños Python permite la notacion
    cientifica por ejemplo:
        para representar la velocidad de la luz escribimos 300000000 lo cual en notacion cientifia seria 3 x 10^8 
        (tres por diez elevado a la octava potencia)
        en Python representamos la notacion cientifica on las letras "E o e" ejemplo, para la velocidad de la luz 3e8
        en donde el numero despues de la "e" tiene que ser un entero mientras que antes de esta puede ser flotante.

        en caso contrario para los numeros muy pequeños ejemplo, 0.0000000000000000000001 en notacion cientifica seria 
        6.62607 x 10^-34 y en Python lo podemos representar asi: 6.62607E-34
        veamos un par de ejemplos:
'''
velocidad_luz = 3e8
plank = 6.62607E-3
print(velocidad_luz,plank)
#Python siempre elige la forma mas corta de presentar un numero, ejemplo:
print(0.0000000000000000000001)

'''
Cadenas de texto:
    Las cadenas de texto se utilizan cuando se requiere procesar texto, y en Python las representamos entre ccomillas dobles ""
    o comillas simples ''
    para poder imprimir comillas en nuestra consola podemos utilizar la siguiente sintaxis:
'''
print("Me gusta el \"Cafe\"")
#El ejemplo anterior tambien funciona si utilizamos comillas simples, pero hay que ser coherentes si se inicia con una no se puede cerrar con la otra ejemplo, "Hola" bien, "Adios' mal.
print('Me gustan los "Chilaquiles"')
#Para insertar apostrofes podemos hacer algo similar al primer ejemplo
print("I\'m Ulises")
'''
Una cadena de texto puede estar vacia "" o " ", de igual manera si nosotros ponemos un numero entre comillas este sera
considerado una cadena de texto en vez de un entero o flotante, ejemplo: "2" o "1.5"
'''

'''
Valores Booleanos:
    Los valores booleanos son un poco abstractos ya que reprecentan veracidad y nos sirven en comparaciones
    estan representados por dos valores True o False, estos siempre se escriben con la primer letra en 
    mayuscula y sin comillas de ningun tipo, ya que si se les puesieran alguna de estas dos serian considerados
    adenas de texto, ejemplo:
'''
print(True > False)
print(True < False)