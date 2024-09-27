'''
Las funciones recursivas son aquellas que se llaman a sí mismas como parte de su proceso de ejecución.
Esto se utiliza para resolver problemas que pueden ser divididos en subproblemas más pequeños del mismo
tipo. En esencia, una función recursiva resuelve un problema llamándose a sí misma hasta que se alcanza
una condición base (o caso base) que detiene la recursión.

Características de una Función Recursiva:

    Caso base (condición de parada): Es la condición que indica cuándo la función debe dejar de llamarse a sí misma.
    Sin un caso base, la recursión continuará indefinidamente, provocando un desbordamiento de la pila (stack overflow).

    Caso recursivo: Es el escenario donde la función sigue llamándose a sí misma, con una versión más simple del problema inicial.
'''

'''
Ejemplo Básico: Factorial de un Número

El factorial de un número n se define como el producto de todos los números enteros positivos hasta n. Por ejemplo,
el factorial de 5 (escrito como 5!) es:

    5 != 5 x 4 x 3 x 2 x 1 = 1205 != 5 x 4 x 3 x 2 x 1 = 120

Esta es una definición naturalmente recursiva, ya que:

    n != n x ( n - 1 ) ! n != n x ( n - 1 ) !
'''
def factorial(n):
    # Caso base: Si n es 0 o 1, el factorial es 1
    if n == 0 or n == 1:
        return 1
    # Caso recursivo: n * factorial de n-1
    else:
        return n * factorial(n - 1)

# Ejemplo de uso:
print(factorial(5))  # Salida: 120

'''
Ejemplo 2: Serie de Fibonacci

La serie de Fibonacci es una secuencia de números donde cada número es la suma de los dos anteriores.
La secuencia empieza con 0 y 1, y se define como:

    F ( 0 ) = 0, F ( 1 ) = 1
    F ( n ) = F ( n - 1 ) + F ( n - 2 ) para n ≥ 2 F ( n ) = F ( n - 1 ) + F ( n - 2 ) para n≥2
'''
def fibonacci(n):
    # Caso base: F(0) = 0, F(1) = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Caso recursivo: Suma de los dos números anteriores en la serie
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Ejemplo de uso:
print(fibonacci(6))  # Salida: 8 (0, 1, 1, 2, 3, 5, 8)


'''
Consideraciones sobre Recursión

    Complejidad: La recursión es a menudo más intuitiva para problemas que se pueden dividir en subproblemas más
    pequeños, pero puede ser menos eficiente en términos de memoria y tiempo de ejecución. Por ejemplo, el cálculo
    de Fibonacci con recursión puede ser ineficiente debido a la recalculación de valores repetidos.

        Optimización: Una técnica común para optimizar las funciones recursivas es el memoization
        (almacenar los resultados de subproblemas ya resueltos).

    Recursión vs. Iteración: Muchas funciones recursivas se pueden reescribir utilizando un bucle iterativo,
    lo que a menudo es más eficiente. La recursión puede ser más fácil de entender en algunos casos, pero la
    iteración tiende a ser más eficiente para la mayoría de los problemas prácticos.
'''

#Ejemplo Mejorado con Memoization: Fibonacci
def fibonacci_memo(n, memo={}):
    # Caso base
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Si el resultado ya está en memo, no recalculamos
    if n in memo:
        return memo[n]
    # Caso recursivo con memoization
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]
# Ejemplo de uso:
print(fibonacci_memo(6))  # Salida: 8

#Código Recursivo para Potencia
def potencia(a, b):
    # Caso base: cualquier número elevado a 0 es 1
    if b == 0:
        return 1
    # Caso recursivo: a * a^(b-1)
    else:
        return a * potencia(a, b - 1)
# Ejemplo de uso:
print(potencia(2, 3))  # Salida: 8 (2^3 = 2 * 2 * 2 = 8)

