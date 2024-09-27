'''
Funcion:
    una funcion en Python es un bloque que nos sirve para agrupar lineas de codigo y poder usarlas posteriormente
    ya sea dentro del mismo archivo o exportandolas a otro, las funciones en Python provienen de 3 fuetnes:

        De Python mismo: es decir son funciones que pertenecen al entorno de Python y no es necesario
            importarlas de nigun lado, un ejemplo de esta es la funcion print().

        De modulos: tambien llamados complementos, estas pueden requerir una instalacion por 
            separado y una importacion.

        De tu codigo: tu puedes escribir las funciones que creas necesarias y mandarlas llamar dentro
            de tu mismo archivo o exportarlas para utilizarlas en otro archivo.

Argumentos en las funciones:
    Los argumentos en una funcion son datos  que necesitamos aportar a estas para que realicen su tarea, una funcion puede o no requerir un argumento, puede tener cualquier cantidad de argumentos asi como tipos de datos, ejemplo de argumento son los datos que escribimos dentro de los parentesis de la funcion print("Hola").

Sintaxis de una funcion:
    para declarar una funcion en Ptyhon comenzaremos por la palabra reservada "def" seguida de un espacio, a continuacion daremos nombre a nuestra funcion seguida de parentesis, dentro de estos parentesis iran nuestros argumentos en caso de necesitarlos y en caso de ser mas de un argumento estos iran separados por coma, cerraremos nuestra declaracion con dos puntos, quedaria de esta forma:

        def nombre_funcion(parametro1, parametro2):
        
    Ahora sigue el cuerpo de la funcion, la cual tiene que ir indentada en la siguiente linea, para esto puedes utilizar 4 espacios o una tabulacion, pero nunca una mezcla de estas dos, ademas de solo incluir una sentencia por linea, ejemplo:

        def nombre_funcion(parametro1, parametro2):
            sentencia1
            sentencia2

    Return:
        en caso que nuestra funcion nos de como resultado un valor tenemos que agregar la palabra reservada "return" al final de nuestra funcion seguida del valor que nos va a regresar, ejemplo:

            def nombre_funcion(parametro1, parametro2):
                sentencia1
                sentencia2
                return sentencia1 + sentencia2

    Invocar una funcion:
        Para invocar una funcion tenemos que escribir el nombre de esta seguida de parentesis y sus parametros en caso de que los requiera, ejemplo:

        nombre_funcion()

    Buenas practicas y convenciones:
        La forma correcta de nombrar funciones en python es con "snake case", esto es separar las palabras con guiones bajos ejemplo: nombre_de_mi_funcion

        siempre utilizar letras minusculas

        El nombre no debe de comenzar por numeros o signos

        Utilizar nombres descriptivos para nuestras funciones

        Cuando tenemos funciones que requieren de muchas sentencias es recomendable que en caso de necesitar el "return" este nos devuelva una variable, ejemplo:

            def nombre_funcion(parametro1, parametro2):
                sentencia1
                sentencia2
                resultado = sentencia1 + sentencia2
                return resultado

        Todo lo anterior mencionado nos ayuda a escribir codigo mas facil de entender y leer

        El uso de funciones dentro de nuestro codigo favorece la reutilizacion y evita que repitamos codigo, es recomendable que siempre separemos nuestro codigo en funciones.

        A continuacion veremos un ejemplo practico de una funcion que suma dos numeros, analizalo, saca tus concluciones y ejecutalo.
'''

def suma(num1, num2):
    resultado = print(num1 + num2)
    return resultado

suma(20, 30)

'''
Nuestra funcion print():
    La funcion print nos sirve para devolver datos legibles para el usuario a traves de la consola, esta funcion
    recibe como argumentos cualquier tipo de dato existente en Python.

En el siguiente ejemplo veremos como trabaja nuestra funcion print()
'''
print("Esta es la primer linea")
print()
print("Esta es otra linea")

'''
Fijate en como mandamos a llamar un print() sin argumentos y en consola se refleja como una linea vacia, podemos tomar
ventaja de este comportmiento pero, a continucion veremos como hacer saltos de linea en consola sin la necesidad de tener 
muchos print() en el codigo.

Caracter de nueva linea:
    este caracter se conforma de una diagonal invertida \ seguida de la letra n, de esta manera \n, asi podremos indicar a 
    nuestra funcion print que queremos un salto de linea en esa posicion, ejemplo:
'''
print("Esta es la primera linea \nEsta es la segunda linea")

'''
Mas de un argumento en nuestra funcion print():
    Cuando introducimos mas de un argumento en nuestro print debemos separarlos por comas ejemplo:
'''
print("Esto","es","mas","de","un","argumento")
'''
Puedes notar que aun que nuestros argumentos no tienen espacios entre si al momento de imprimirlo en consola Python por
iniciativa propia los coloca, se muestran en orden ya que son argumetnos posicionales y ademas se muestran en una sola linea.

Podemos cambiar este comportamiento agregando la palabra clave sep="" y dentro de las comillas indicaremos el caracter que
queremos utilizar en vez de los espacios, ejemplo:
'''
print("Esto","es","mas","de","un","argumento", sep="+") 