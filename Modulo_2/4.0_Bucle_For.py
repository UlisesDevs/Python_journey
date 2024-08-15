'''
Otro tipo de buclle que tenemos en Python es el "for" donde mas que nada importan
mas los giros o vueltas del bucle que las condiciones 

El bucle for sirve para poder explorar grandes cantidades de datos elemento por elemento su sintaxis seria 
la siguiente:

    for i in range(100):
        # do_something()

Se comienza por la palabra clave "for"
Se continua con un espacio y la variable de control, por lo general se comienza con la letra "i", aun que puede
    ser cualquiera que tu elijas
Despues la palabara lave "in" que indicara el rango de valores por el que pasara nuestra variable de control
La funcion range() indicara el rango o numero de veces que se va a repetir nuestro bucle
ejemplo:
'''
for i in range(20):
    print("El valor de i es : ", i)

'''
Funcion range():
    La funcion range() puede aceptar varios argumentos, en el ejemplo anterior si solo introducimos un argumento
    este sera el rango hasta el que queremos que llegue nuestro ciclo, pero en caso de pasar dos argumentos
    range(5, 10), el primero sera el numero por el que se comienza el bucle y el segundo el rango maximo
'''
for j in range(5, 30):
    print("Este es un ciclo que comienza en 5 y llega hasta el 30: ", j)
'''
Ahora si introducimos 3 argumentos, este tercero sera de cuantos en cuantos numero hara el conteo nuestro ciclo for
Nota: los argumentos de range() solo deben de ser numeros enteros, al igual que si sus argumentos estanvacios
este no ejecutara el bucle y por default si no es especifica el conteso por defecto sera de 1 en 1
'''
for k in range(5, 20, 2):
    print("Este es un ciclo que comienza en 5 y va de 2 en 2 hasta e 20: ", k)

#Veamos otro ejemplo, en el cual se muestran las potencias de 2
power = 1
for expo in range(16):
    print("2 a la potencia de", expo, "es", power)
    power *= 2

'''
Las sentencias break y continue:
    Break nos sirve para detener el bucle mientras que continue nos sirve para saltar la vuelta en curso y pasar a la siguiente
'''
# break - ejemplo

print("\nLa instrucción break:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro del bucle.", i)
print("Fuera del bucle.")


# continue - ejemplo

print("\nLa instrucción continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle.", i)
print("Fuera del bucle.")

'''
else tambien puede utilizarse en for y while
'''
#for con else
for i in range(10):
    print(i)
else:
    print("else de for: ",i)

#while con else
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else de while: ", i)

#Aun que else junto con un while y for no son usados a menudo al igual que continue y break, ambos son considerados "sintax sugar"