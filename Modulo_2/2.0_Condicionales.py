'''
Ahora que sabemos hacer preguntas y regresar valores verdaderos o falsos, es momento de utilizar
estos resultados en mecanismos llamados condicionales, las cuales realizan una accion si se cumple o
no una condicion.
'''

'''
Condicional if:
    Se compone de los siguientes elementos:

        La palabra reservada if
        Una expresion que nos regresa un resultado de True o False
        Dos puntos seguidos de una nueva linea
        Las instrucciones las cuales deben de ir indentadas
        Solo una instruccion por linea
        Nota: para la indentacion no es recomendable usar combinaciones de espacios y tabulaciones
            Simpre utilizar una u otra, aun que se recomienda el uso de cuatro espacios.
        
        Nuestra condicional quedaria de la siguiente manera:

        if true_or_not:
            do_this_if_true

Lo anterior se interpreta de la siguiente manera, si la condicional de la exprecion se cumple (es True)
se ejecutan las instrucciones que estan indentadas, de lo contrario no se ejecuta y el programa sigue con
las proximas lineas.
'''
if 10 > 1:
    print("Si, diez es mayor que uno")

'''
Condicional if - else:
    Esta se compone por la palabra reservada else y es como un plan b en caso de que la primer condicion no se cumpla
    Else no contiene condiciones, ya que esta solo se cumple si las anteriores no se cumplieron
    else va al mismo nivel del if, es decir no tiene indentacion
    se sigue con los dos puntos y un salto de linea
    las instrucciones al igual que las de if tienen que ir indentadas

    Quedaria de la siguiente manera:
    
    if true_or_not:
        do_this_if_true
    else:
        do_this_if_false
'''
if 10 > 20:
    print("Si, diez es mayor que veinte")
else:
    print("No, diez no es mayor que veinte")

'''
if - else, anidados:
    Hay ocaciones en las que necesitaremos utilizar if - else dentro de otro if - else, a esta situacion se le conoce
    como anidacion veamos un ejemplo:

if the_weather_is_good:
    if nice_restaurant_is_found:
        have_lunch()
    else:
        eat_a_sandwich()
else:
    if tickets_are_available:
        go_to_the_theater()
    else:
        go_shopping()

Recuerda que cada else se refiere al if en su mismo nivel de indentacion y nota como esto mejora la legibilidad del codigo
'''

'''
La sentencia elif:
    Esta sentencia se utiliza en caso de que queramos verificar mas de una condicion
    Al igual que if contiene su propia condicion
    Va al mismo nivel que el if

if the_weather_is_good:
    go_for_a_walk()
elif tickets_are_available:
    go_to_the_theater()
elif table_is_available:
    go_for_lunch()
else:
    play_chess_at_home()

El ensamblaje de if - elif - else, se le conoce como cascada
'''

'''
Cosas a tener en cuenta en la condicional if:
    No utilizar un else sin un if precedente
    Else siempre es la ultima condicion, independientemente si se utilizo o no un elif
    Else es una parte opcional y puede omitirse
    Solo se ejecutara un rama else en caso de existir mas a ese nivel de indentacion
'''