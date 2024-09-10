'''
Que es una funcion?
    Una funcion es un bloque de codigo que puede ser invocado en cualquier parte 
    de nuestro programa las veces que la necesitemos, nos sirve para evitar reescribir
    codigo a menudo y simplifica la compreencion de nuestro programa, existen distintas
    razones para trabajar con funciones:

        Si un fragmento de codigo necesita utilizarse muchas veces en nuestro programa
        cuando esto sucede no es necesario volver a escribir el bloque que necesitamos 
        una y otra vez, con solo escribir una vez nuestra funcion e invovcarla las veces
        que la necesitemos sera suficiente.

        Nota: Una funcion bien escrita puede comprenderse con solo mirarla

        Si tu codigo se vuelve tan extenso que leerlo y comprenderlo se hace complicado
        si este es el caso hay que considerar el uso de funciones para descomponer
        el problema en pequeños problemas por separado e implementar cada uno con una
        funcion diferente, a esto se le llama "Descomposicion", esta descomposicion
        continua hasta que tienes un conjunto de funciones cortas, faciles de comprender
        y probar.
        De esta forma tambien podemos delegar la ralizacion de distintas funciones
        a distintos desarroolladores ya que cada uno tendra que escribir un conjunto 
        bien definido de funciones que al final resuelvan el problema en comun.

De donde provienen las funciones?
    Las funciones provienen de distintos lugares:

        De Python mismo, llamadas funciones integradas (como print()) estas estan a nuestra
        disposicion en el momento que las invoquemos

        De modulos, esatas funciones necesitan ser importadas primero para poder invocarlas

        Escritas por nosotros mismos, en este caso nosotros definiremos la funcion y la 
        invocaremos cuando la necesitemos.
'''

'''
Sintaxis:

    Una funcion se define con la palabra reservada def

    Despues un espacio y el nombre de la funcion, la cual tiene las mismas reglas para ser
    nombradas que las variables

    A continuacion del nombre de nuestra funcion se ponen parentesis (), dentro de los cuales
    escribiremos los parametros en caso de necesitarlos

    Se termina la linea con dos puntos :

    El cuerpo de nuestra funcion ira indentado en la linea siguiente de los dos puntos, la 
    funcion termina donde termine nuestra indentacion.

        def function_name():
            cuerpo de la función 
'''
def saludo():
    print("Hola, Mundo!")

'''
Hasta este momento solo hemos definido nuestra funcion pero si ejecutas el codigo veras que no sucede nada
esto es por que tambien necesitamos invocar la funcion para poder mosrtar el resultado, la manera
de invocar una funcion es escribiendo el nombre de la funcion seguida de dos parentesis y en caso
de que nuestra funcion lo necesite debemos escribir los argumentos dentro de estos.
'''
saludo()
'''
Nota: "parametros" y "argumentos" pueden ser lo mismo, pero los parametros se definen al momento
de definir nuestra funcion y los argumentos se introducen al momento de invocar nuestra funcion.

Nota: No puedes invocar una funcion antes de definirla.
'''

'''
Funciones con parametros:
    Para definir una funcion con parametros estos se tienen que declarar dentro de los prentesis
    al momento de declarar la funcion:

        def funcion(parametro):
            cuerpo de la funcion
'''
def saludo_2(nombre):
    print("Hola,",nombre)
'''
los parametros son como variables que solo seran leidas y utiles dentro de nuestra funcion
en este caso declaramos un parametro que recibe un nombre, entonces no importa si fuera de
nuestra funcion declaramos una variable con el mismo nombre de un parametro en alguna
funcion.
'''
'''
Al momento de invocar una funcion que requiere parametros, tendremos que ingresar los argumentos
requeridos dentro de los parentesis

    funcion(argumentos)

Nota: si no ingresamos los argumentos de una funcion parametrizada nos dara error 
'''
saludo_2("Ulises")

'''
Una funcion puede contener tantos paramatros como necesitemos pero ten en cuenta que 
entre mas parametros se complica la legibilidad del codigo
'''
def hobby(nombre,pasatiempo):
    print("A",nombre,"le gusta",pasatiempo)
hobby("Ulises","Programar")
'''
Nota: los parametros son posicionales, por lo que tendremos que ingresar los argumentos
en el orden que se declaran los parametros para obtener el resultado deseado
'''
hobby("dibujar","Ulises")
'''
Existe una manera distinta de pasar argumentos sin importar la posicion y estos son
los argumentos de palabras clave los cuales se asignan como variables por lo tanto 
no importa la posicion en que se escriban por que ya los estaremos asignando
'''
hobby(pasatiempo = "cantar",nombre = "Ulises")
#nota que pasamos los argumentos al revez pero como los asignamos a su parametro correspondiente el resultado es el deseado
#es obvio que no podemos pasar un argumento que no existe lo cual nos arrojara un error

'''
podemos combinar argumentos posicionales y argumentos de palabra calve siempre y cuando pasemos primero
los argumentos posicionales y despues los de palabras clave
'''
def concat(a,b,c):
    print(a,"+",b,"+",c,"=",a+b+c)
concat(1,c = 3,b = 4)

'''
funciones con parametros predefinidos:
    podemos declarar parametros con valores predefinidos con la siguiente sintaxis
'''
def pelicula(nombre = "Ulises",pelicula = "Pulp Finction"):
    print("La pelicula favorita de",nombre,"es",pelicula)
pelicula()
'''
Ahora que nuestra funcion tiene parametros predefinidos, podemos mandarla llamar sin argumentos ya que 
estos estan declarados y se sabe cual es su valor, a continuacion se muestran distintas formas de 
pasar los argumentos a una funcion con parametros predefinidos, revisa los resultados de cada una de ellas.
'''
pelicula("Juan","Spiderman")
pelicula(pelicula = "Harry Potter")

''''
Retornando el resultado de una funcion
'''