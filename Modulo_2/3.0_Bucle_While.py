'''
Que es un bucle?:
    Es una secuencia de codigo que se repite hasta que se cumpla una condicion, a diferencia
    de las condcionales if que comienzan a ejecutarse cuando una condicion se cumple, es decir
    si la condicion devulve True esta se seguira ejecutando hasta que arroje un False.
    tomemos como ejemplo lo siguiente:

        mientras haya algo que hacer
            hazlo

    toma en cuenta que la sentencia anterior tambien declara que si no hay nada que hacer, nada ocurre.
'''

'''
Bucle while:
    Un bucle while se de clara con la palabra reservada "while"
    A continuacion declaramos nuestra condicional seguida de dos puntos y un salto de linea
    Dentro de el bucle while van nuestras instrucciones indentadas
    Todas las reglas de indentacion tambien se aplican a while
    Ten en cuenta que el cuerpo del bucle de be poder cambiar el valor de la condicion, de lo contrario
    si esta siempre es True nuestro ciclo sera infinito
'''
#Bucle infinito
#while True:
    #print("Estoy atrapado dentro de un bucle.")
'''
Ya que nuestra condicion siempre es True y nuestro cuerpo nunca cambia esta condicion
se imprimira infinitamente,"Estoy atrapado dentro de un bucle."
'''

#Bucle finito
number = 0
while number < 11:
    print("Dentro del bucle, ", number)
    number += 1
print("Fuera del bucle")
'''
Tenemos nuestra variable number que equivale a 0, en nuestro ciclo while se evalueara que mientras
number sea menor que 11 se va a imprimir "Dentro del bucle, ", number, y despues se agregara mas uno
a nuestra variable number, entonces en nuestra siguiente iteracion nuestra variabel number pasara de valer 0
a valer 1, y como 1 es menor que 11 se vuelve a iterar, asi hasta que nuestra variable number alcance
el valor de 11, en ese momento nuestra comparacion de number < 11 dejara de devolver True y nuestro bucle se detendra.
'''

#Ejercicio:
'''
Un mago junior ha elegido un número secreto. Lo ha escondido en una variable llamada secret_number. 
Quiere que todos los que ejecutan su programa jueguen el juego, Adivina el número secreto, y adivina qué 
número ha elegido para ellos. ¡Quiénes no adivinen el número quedarán atrapados en un bucle sin fin para siempre! 
Desafortunadamente, él no sabe cómo completar el código.

Tu tarea es ayudar al mago a completar el código en el editor de tal manera que el código:

pedirá al usuario que ingrese un número entero;
utilizará un bucle while;
comprobará si el número ingresado por el usuario es el mismo que el número escogido por el mago. 
Si el número elegido por el usuario es diferente al número secreto del mago, el usuario debería ver el mensaje
"¡Ja, ja! ¡Estás atrapado en mi bucle!" y se le solicitará que ingrese un número nuevamente. Si el número ingresado 
por el usuario coincide con el número escogido por el mago, el número debe imprimirse en la pantalla, y el mago debe 
decir las siguientes palabras: "¡Bien hecho, muggle! Eres libre ahora."

¡El mago está contando contigo! No lo decepciones.
'''
#Respuesta
secret_number = 777
print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")
user_number = int(input("Ingresa tu numero: "))
while user_number != secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    user_number = int(input("Intenta de nuevo: "))
print("¡Bien hecho, muggle! Eres libre ahora.")