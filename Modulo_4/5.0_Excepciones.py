'''
Ahora hablemos un poco del manejo de errores y el testing de nuestros programas:

    El menejo de errores hace referencia hacia el comportamiento que puede tener nuestro programa
    al introducir datos que afecten la ejecucion del mismo y como manejarlos para evitar 
    que tu programa termine abruptamente y poder protejerlo ante errores de entrada o bugs.
    
    por ejemplo, cuando tenemos un programa que en alguna parte necesita hacer una division
    y el usuario ingresa 0, es obvio que no es posible hacer una division entre 0, pero
    como le informamos eso al usuario? y como hacemos para que nuestro programa no termine
    abruptamente ante esto?
    
    si bien podemos hacer comprobaciones de tipo con:
    
        type(value) is int
        
        Esta no es la mejor manera de lidiar con errores y Python nos proporciona un metodo
        mejor para evaluar y atrapar errores.
        
try - except:

    Son palabras reservadas para el proposito de evitar errores en nuestro programa
    
    try:
        En este bloque se coloca el codigo que creemos es propenso a errores
        
    except:
        En este bloque se maneja el error y depenede del desarrollador lo que escribamos aqui 
'''
#Ejemplo para sacar el reciproco de un numero
valor = int(input("Ingresa un numero natural para calcular su reciproco: "))
print('El recíproco de', valor, 'es', 1/valor) 
'''
Si bien al ingresar lo que el programa nos pide no tenemos ningun problema, pero al momento
de ingresar una letra, un simbolo, un enter sin escribir nada o un 0 el programa se 
detendra y arrojara el error.
'''

#Hagamos un primer manejo de errores con try - except (Descomenta el codigo para que observes el comportamiento)
'''
try:
    valor = input("Ingresa un numero natural para calcular su reciproco: ")
    print('El recíproco de', valor, 'es', 1/valor) 
except:
    print("Ese no es un numero :(")
'''
'''
Ahora veremos como aun nuestro programa se detiene al introducir un dato erroneo
pero nos arroja lo que hemos hecho mal, un except solo, se le denomina excepcion predeterminada
'''

#Podemos identificar errores concretos y arrojar un texto para cada uno ademas de poder utilizar mas de un except
#(Descomenta el codigo para que observes el comportamiento)
'''
try:
    valor_str = input("Ingresa un numero natural para calcular su reciproco: ")
    valor = int(valor_str)
    print('El recíproco de', valor, 'es', 1/valor) 
except ValueError:
    print(f"{valor_str},  no es un numero :(")
except ZeroDivisionError:
    print("No se puede dividir entre 0")
'''
'''
Ahora en caso de que ingresemos un simbolo o una letra, este error sera atrapado por
except VaueError e imprimira que no es un numero, despues si tratamos de dividir entre 0
este error sera atrapado por  except ZeroDivisionError: e imprimira que no se puede
dividir entre 0
'''

'''
Ahora resolvamos el 3 error que es cuando se da enter sin escribir nada, si bien al hacer eso nos arroja
el error de ValueError, seria mejor dar luz a el ususario de que hizo mal.
'''
#(Descomenta el codigo para que observes el comportamiento)
'''
try:
    valor_str = input('Ingresa un número natural: ')
    if valor_str == '':  # Verifica si la entrada está vacía
        raise ValueError("Entrada vacía, se esperaba un número")
    
    valor = int(valor_str)
    print('El recíproco de', valor, 'es', 1/valor)
    
except ValueError as e:
    if str(e) == "Entrada vacía, se esperaba un número":
        print(e)  # Muestra el mensaje específico para la entrada vacía
    else:
        print(f"Debes ingresar un número válido, no puedo procesar '{valor_str}'")
except ZeroDivisionError:
    print('La división entre cero no está permitida en nuestro Universo.')
'''
'''
Ahora como vemos podemos asignar variables dentro de los except para poder hacer comprobaciones
dentro del mismo y arrojar distintos mensajes de error, asi poder distinguir un simbolo
de una entrada vacia de enter.
'''

#Ahora podemos utilizar un bucle while para que no nos saque del programa hasta que este haga lo que debe hacer
#(Descomenta el codigo para que observes el comportamiento)
'''
while True:
    try:
        valor_str = input('Ingresa un número natural: ')
        if valor_str == '':  # Verifica si la entrada está vacía
            raise ValueError("Entrada vacía, se esperaba un número")
        
        valor = int(valor_str)
        print('El recíproco de', valor, 'es', 1/valor)
        break
    except ValueError as e:
        if str(e) == "Entrada vacía, se esperaba un número":
            print(e)  # Muestra el mensaje específico para la entrada vacía
        else:
            print(f"Debes ingresar un número válido, no puedo procesar '{valor_str}'")
    except ZeroDivisionError:
        print('La división entre cero no está permitida en nuestro Universo.')
'''

'''
Exepciones que podemos atrapar en except:

    ZeroDivisionError:
        Esta aparece cuando intentas forzar a Python a realizar cualquier operación que provoque una
        división en la que el divisor es cero o no se puede distinguir de cero. Toma en cuenta que hay
        más de un operador de Python que puede hacer que se genere esta excepción (/, //, %).
        
    ValueError:
        Espera esta excepción cuando estás manejando valores que pueden usarse de manera inapropiada en algún
        contexto. En general, esta excepción se genera cuando una función (como int() o float()) recibe un
        argumento de un tipo adecuado, pero su valor es inaceptable.
        
    TypeError:
        Esta excepción aparece cuando intentas aplicar un dato cuyo tipo no se puede aceptar en el contexto actual.
        Mira el ejemplo:

                short_list = [1]
                one_value = short_list[0.5]
        
        No está permitido usar un valor flotante como índice de una lista (la misma regla también se aplica a las tuplas).
        TypeError es un nombre adecuado para describir el problema y una excepción adecuada a generar.
        
    AttributeError:
        Esta excepción llega - entre otras ocasiones - cuando intentas activar un método que no existe en un elemento con
        el que se está tratando. Por ejemplo:
        
            short_list = [1]
            short_list.append(2)
            short_list.depend(3)
        
        La tercera línea de nuestro ejemplo intenta hacer uso de un método que no está incluido en las listas. Este es el
        lugar donde se genera la excepción AttributeError.
'''

'''
Algunos otros conceptos a tomar en cuenta para hacer un buen testing:

Probar el código es esencial para todo desarrollador, ya que es imposible evitar errores. Las pruebas no buscan demostrar
que el código está libre de errores, sino confirmar que existen errores. Los desarrolladores tienden a ser subjetivos con
su propio trabajo, por lo que es importante contar con testers que puedan identificar problemas de manera objetiva.

    - Python es un lenguaje interpretado, lo que significa que solo ejecuta las líneas de código que se usan en cada momento.
    Esto hace que sea vital probar todas las rutas de ejecución del código, ya que algunas líneas podrían no ejecutarse hasta
    que ciertas condiciones se cumplan.

    - Depuración (debugging) es el proceso de eliminar errores del código. Un depurador es una herramienta que permite ejecutar
    el programa línea por línea, inspeccionar el estado de las variables y detener la ejecución en momentos clave para identificar
    fallos.
    
    - Depuración por impresión es una técnica simple en la que se insertan print() para observar cómo fluye el código. Aunque no es
    interactiva como un depurador, sigue siendo útil para localizar errores. Sin embargo, los mensajes de depuración deben eliminarse
    antes de lanzar el código final.
    
    - Errores y testers: Los errores encontrados por testers son positivos, ya que previenen problemas para los usuarios. Aceptar la ayuda
    de los testers es crucial en el ciclo de desarrollo.
    
Consejos de depuracion:

    - Explica el problema a alguien más (o incluso a un "patito de goma", técnica conocida como "Rubber Duck Debugging").
    
    - Aísla el problema comentando partes del código y ejecutando solo el área sospechosa.
    
    - Revisa los cambios recientes en el código, ya que podrían haber introducido el error.
    
    - Tómate un descanso para despejar la mente, lo que puede ayudar a identificar el error con mayor claridad.
    
    - Sé optimista: eventualmente, el error será localizado.
    
Pruebas unitarias:

    Pruebas unitarias son una técnica avanzada que convierte las pruebas en una parte integral del proceso de desarrollo.
    Estas pruebas automatizadas se diseñan junto con el código para garantizar que cualquier cambio en el código se verifique
    inmediatamente. Python incluye el módulo unittest para facilitar este enfoque.
    
    Agregar pruebas unitarias desde el principio es una práctica recomendada en el desarrollo ágil y continuo, ya que reduce el
    tiempo de depuración y garantiza un código más robusto. Adicionalmente, las pruebas automatizadas en combinación con
    herramientas de integración continua (CI/CD) mejoran significativamente la calidad del software.
'''