'''
Que es un Operador?:
    Un operador es un simbolo del lenguaje de programacion, el cual es capaz de hacer operaciones con los valores.
    Operadores disponibles en Python:
'''
#Exponenciacion: se representa por los signos ** 
print("Esto es el resultado de una Exponenciacion: ", 2 ** 3)

#Multiplicacion: se representa por el signo *
print("Esto es el resultado de una Multiplicacion: ", 2 * 3)

#Divivion: se representa por el signo /
#Nota: el resultado de una division siempre es flotante
print("Esto es el resultado de una division: ", 10 / 2)

#Division entera: se representa por los signos //
#Nota: el redondeo siempre sucede hacia abajo (En ingles se suele lamar floor division)
print("Esto es el resultado de una division entera: ", 10 // 2)

'''
Residuo o modulo: se representa por el signo %
el resultado de este operador es el residuo que queda de la division entera
'''
print("Esto es el resultado de un modulo: ", 14 % 4)
'''
14 // 4 da como resultado un 3 → esta es la parte entera, es decir el cociente;
3 * 4 da como resultado 12 → como resultado de la multiplicación entre el cociente y el divisor;
14 - 12 da como resultado 2 → este es el residuo.
'''
#Recuerda no dividir entre 0, realizar una division entera entre 0 y tampoco encontrar el residuo de una division entre 0

#Suma: se representa con el signo +
print("Esto es el resultado de una suma: ", 10 + 10)

#Resta: ser epresenta por el signo -
print("Esto es el resultado de una resta: ", 15 - 10)

'''
Operadores unarios y binarios.
    un operador unario es aquel con solo un operando, ejemplo:
        +1  o  -1
    un operador binario es aquel con dos operandos, ejemplo:
        1 * 1  o  2 + 4
'''

'''
Prioridad de operadores:
    Al igual que en las matematicas Python prioriza unos operadores por sobre otros el orden de prioridad es el siguiente:

        1 --- **
        2 --- Unarios (+, -), Los operadores unarios a la derecha del operador exponencial enlazan con mayor fuerza
        3 --- *, /, //, %
        4 --- +, -
'''
'''
Enlazado:
    Que pasa cuando tenemos mas de un operador con la misma prioridad?, este seria priorizado de acuerdo a su enlazado
    por ejemplo:
'''
print("El resultado del enlazado de modulo es: ", 9 % 6 % 2)
#El resultado es 1 ya que el enlazado del modulo es de izquierda a derecha

print("El resultado del enlazado de exponeciacion es: ", 2 ** 2 ** 3)
#Caso contrario con el enlazado de exponenciacion que es de derecha a izquierda

#Sabiendo lo anterior cual crees que sea el resultado de la siguiente expresion?:
print("El resultado es: ", 2 * 3 % 5)

'''
Operadores y parentesis:
    Python permite el uso de parentesis para mejorar la legibilidad de las operaciones y sigue las mismas reglas de la aritmetica
    la cual es:
        Las sub expresiones dentro de los parentesis siempre se calculan primero
    sabiendo esto cual crees que sea el resultado de la siguiente expresion?
'''
print("El resultado de la expresion con parentesis es: ",(5 * ((25 % 13) + 100) / (2 * 13)) // 2)
    