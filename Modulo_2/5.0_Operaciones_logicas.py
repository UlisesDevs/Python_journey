'''
El operador "and" tambien conocido como operador de conjuncion, la ejecucion depende de que las dos 
declaraciones se cumplan, por ejemplo:
    si tenemos tiempo libre y hay buen clima, saldremos a caminar.

para este operador tenemos algo que se denomina tabla de verdad, la cual es el resultado de distintas 
combinaciones de resultados:

False and False = False
False and True = False
True and False = False
True and True = True
'''

'''
Por otro lado tenemos el operador "or" tambien conocido como disyuncion que su ejecucion depende de si 
se cumple una declaracion o la otra, por ejemplo:
    si tu estas el la pizzeria o si yo estoy en la pizzeria, uno de los dos compra la pizza.

Al igual que con and tambien tenemos tabla de verdad para or y es la siguiente:

False or False = False
False or True = True
True or False = True
True or True = True
'''

'''
Operador "not" este operador niega la declaracion por lo que la convierte en lo contrario
su tabla de verdad es la siguiente:

not True = False
not False = True
'''

'''
Operadores bit a bit:
    Para saber como funciona un operador bit a bit, primero tenemos quer recordar como funciona un bit y un byte
    un bit solo tiene dos valores 0 y 1, y un byte es el conjunto de 8 bits, entonces para poder convertir
    numero enteros a binarios tengamos en cuenta la siguiente tabla:

        128 64 32 16 8 4 2 1

    Entonces cada bit ocupa un espacio comenzando de derecha a izquierda en la anterior tabla
    por lo  tanto si queremos representar el numero uno en binario este seria:

        0    0  0  0 0 0 0 1
    
    y por que? por que estamos activando la casilla que ocupa el numero uno en la tabla, por lo tanto
    si queremos representar el numero dos seria:

        0    0  0  0 0 0 1 0

    se activa la casilla donde esta el dos y se desactiva la casilla donde esta el uno
    pero esto es facil por que esos numeros ya estan representados en la tabla, pero que pasa si yo quiero
    representar un numero que no se encuentra en la tabla? por ejemplo el 3, quedaria de la siguiente manera:

        0    0  0  0 0 0 1 1
    
    y por que? por que tenemos activadas las casillas donde se encuentran los numeros 2 y 1, entonces
    2 + 1 = 3, por lo tanto lo anterior seria la represnetacion binaria de el numero 3, siguiedo
    esta logica seremos capaces de representar bastantes numero en binario.
'''

'''
Ahora si, comencemos con nuestros operadores bit a bit, que en resumen vienen siendo los mismos que
nuestros operadores logicos pero se le agrega uno nuevo, el xor (exclusive or), cada uno de estos tiene
una representancion en simbolo serian las sigueintes:

    & - and
    | - or 
    ~ - not
    ^ - xor

Y cada uno cuenta con su tabla de verdad, comencemos con el "&":

    0 & 0 = 0
    0 & 1 = 0
    1 & 0 = 0
    1 & 1 = 1
si te fijas en este caso es como si realizaramos una multiplicacion.

Tabla de "|":

    0 | 0 = 0
    0 | 1 = 1
    1 | 0 = 1
    1 | 1 = 
    
Tabla de "^":

    0 ^ 0 = 0
    0 ^ 1 = 1
    1 ^ 0 = 1
    1 ^ 1 = 0

Y como "~" es negacion su tabla seria:

    ~ 0 = 1
    ~ 1 = 0


Nota:   & requiere exactamente dos 1 s para proporcionar 1 como resultado;
        | requiere al menos un 1 para proporcionar 1 como resultado;
        ^ requiere exactamente un 1 para proporcionar 1 como resultado.

Nota: los argumentos para estos operadores siempre deben de ser enteros y no flotantes
'''

'''
Ahora veamos todo lo anterior con ejemplos practicos, recuerda que para representar numeros binarios 
en Python utilizamos la notacion 0b seguido por el numero binario, ejemplo:

    uno = 0b1
'''
uno = 0b1
print(uno, "En binario es: 0b1")

#Vamos a declarar nuestras variables binarias a(45) y b(50)
a = 0b101101
b = 0b110010

#not bit a bit
print("\nnot de a: ", ~a)
print("not de b: ", ~b)

#and bit a bit
print("\na & b = ", a & b)


#or bit a bit
print("\na | b = ", a | b)


#xor bit a bit
print("\na ^ b = ", a ^ b)

'''
Desplazamiento binario izquierda y derecha:

    como su nombre lo dice estos operadores desplazan nuestros bits a la izquierda o derecha 
    el numero de casillas que indiquemos

    >> = desplazamiento a la derecha
    << = despllazamientos a la izquierda

traigamos de vuelta nuestra tabla de bits

    128 64 32 16 8 4 2 1
     0   0  1  0 1 1 0 1 = 45 

si aplicamos el operador de desplazamiento por ejemplo 45 >> 2 esto indica que vamos a desplazar
nuestro numero binario la cantidad de dos casillas por lo tanto quedaria de la siguietne manera:

    128 64 32 16 8 4 2 1
            0  0 1 0 1 1 0 1 = 11
    
    al despplazarse dos casillas a la derecha los primeros dos bits quedan fuera de la tabla por
    lo tanto ya no se cuentan y se cuentan los que quedan dentro pasando de valer 45 a 11
'''
print("\ndesplazamiento a la derecha de a: ", a >> 2)

#Aplica la misma regla para el desplazamiento a la izquierda
print("\ndesplazamiento a la izquierda de b: ", b << 2)

'''
Nuestro operadores bit a bit tambien los podemos abreviar de la siguiente manera

    &=
    |=
    ^=
    <<=
    >>=
'''
a = 0b101101
b = 0b110010
a &= b
print("\na & abreviado: ", a)

a = 0b101101
b = 0b110010
a |= b
print("\na | abreviado: ", a)

a = 0b101101
b = 0b110010
a ^= b
print("\na ^ abreviado: ", a)

a = 0b101101
b = 0b110010
a >>= 2
b <<= 2
print("\na desplazamiento derecho abreviado: ", a)
print("\nb desplazamiento izquierdo abreviado: ", b)

'''
Aprendido lo anterior nuestra tabla de jerarquias se actualiza:

    1 - ~, + , -  unario
    2 - **
    3 - *, /, //, %
    4 - +, -      binario
    5 - <<, >>
    6 - <, <=, >=, >, 
    7 - ==, !=
    8 - &
    9 - |
    10 - =, +=, -=, *=, /=, %=, &=, ^=, |=, >>=, <<=
'''