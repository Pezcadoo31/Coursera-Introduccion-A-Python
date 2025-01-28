#Hola, ahora que ya sabemos construir una interaccion basica con nuestro programa
#de red social, vamos a agregar nuevas funcionalidades.
#
#Vamos a partir con el mismo programa de la etapa anterior, que permite dos cosas:
#1. Obtener datos del usuario
#2. Consultar y mostrar UN mensaje de estado del usuario
#
#Una caracteristica de los programas con multiples funcionalidades es que ofrecen un menu de acciones
#al usuario. Los menus de opciones permiten que el usuario escoja que accion realizar y podemos
#implementarlos usando un ciclo while que funcionen mientras el usuario no escoja una accion de salida.
#Cada vez que el usuario escoja una accion podemos usar una serie de 'if/elif/else' para ejecutar
#distintas secciones de codigo de acuerdo a lo que el usuario ha solicitado.

#Para empezar vamos a permitir que el usuario publique todos los mensajes que considere desee hasta
#que decida salir voluntariamente del programa.

############################################################
# Bienvenida

print("Bienvenido a ... ")
print(""" 
                                                  .___
______   ____ ________         _______   ____   __| _/
\____ \_/ __ \\___   /  ______ \_  __ \_/ __ \ / __ | 
|  |_> >  ___/ /    /  /_____/  |  | \/\  ___// /_/ | 
|   __/ \___  >_____ \          |__|    \___  >____ | 
|__|        \/      \/                      \/     \/ 

""")

# Solicitud de nombre
nombre = input("Para empezar, dime como te llamas. ")
print()
print("Hola ", nombre, ", bienvenido a PEZ-RED")
print()

# Calculo de edad
año = int(input("Para preparar tu perfil, dime en que año naciste. "))
edad = 2025-año
print()

# Calculo de estatura
estatura = float(input("Cuentame mas de ti, para agregarlo a tu perfil. ¿Cuanto mides? Dimelo en metros. "))
estatura_m = int(estatura)
estatura_cm = int( (estatura - estatura_m)*100 )
print()

# Cantidad de amigos
num_amigos = int(input("Muy bien. Finalmente, cuentame cuantos amigos tienes. "))

#Con los datos recolectados escribimos en pantalla un texto que resuma los datos que hemos obtenido
print()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
print("--------------------------------------------------")
print("Nombre:  ", nombre)
print("Edad:    ", edad, "años")
print("Estatura:", estatura_m, "metros y", estatura_cm, "centimetros")
print("Amigos:  ", num_amigos)
print("--------------------------------------------------")
print("Gracias por la informacion. Esperamos que disfrutes con PEZ-RED")
print()

"""
#Usaremos una variable bool para indicar si el usuario desea continuar
#utilizando el programa o no
continuar = True

#Este ciclo se mantiene en ejecucion hasta que el usuario desee salir
while continuar:

    #Solicitamos opcion al usuario
    opcion = str(input("¿Deseas escribir un mensaje? (S/N) "))

    #Vamos a aceptar que el usuario ingrese un mensaje cuando escriban "S", "s", o nada
    if opcion == "S" or opcion == "s" or opcion == "":
        mensaje = input("Vamos a publicar un mensaje. ¿Que piensas hoy? ")
        print()
        print("--------------------------------------------------")
        print(nombre, "dice:", mensaje)
        print("--------------------------------------------------")
    #En caso que sea otra respuesta, vamos a decidir salir.
    #AsÃ­, en la siguiente iteracion el ciclo terminara
    else:
        continuar = False

#Mensaje de salida, una vez que el ciclo ha terminado.
print("Gracias por usar PEZ-RED. ¡Hasta pronto!")
"""

#Ahora puedes escribir mensajes todas las veces que quieras.
#Observa que hemos utilizado un ciclo while que permite repetir la accion de preguntar por un mensajes
#hasta que el usuario escribe algo distino de "S".

#Pero las redes sociales pueden ejecutar mas acciones que solamente enviar mensajes.

#Te proponemos los siguientes desafios:
"""#1. Este programa termina cada vez que el valor de 'opcion' es distinto a "S" o a "s".
#   Modifique el programa para que el programa termine UNICAMENTE cuando se ingresa "N" o "n".
#   En caso que se ingrese algo distinto, debe volver a solicitar una opcion al usuario.

#Usaremos una variable bool para indicar si el usuario desea continuar
#utilizando el programa o no
continuar = True

#Este ciclo se mantiene en ejecucion hasta que el usuario desee salir
while continuar:

    #Solicitamos opcion al usuario
    opcion = str(input("¿Deseas escribir un mensaje? (S/N) "))

    #Vamos a aceptar que el usuario ingrese un mensaje cuando escriban "S", "s", o nada
    if opcion == "S" or opcion == "s" or opcion == "":
        mensaje = input("Vamos a publicar un mensaje. ¿Que piensas hoy? ")
        print()
        print("--------------------------------------------------")
        print(nombre, "dice:", mensaje)
        print("--------------------------------------------------")
    elif opcion == "N" or opcion == "n":
        continuar = False
    else:
        print("Por favor, ingrese una opcion valida.")
        print()

#Mensaje de salida, una vez que el ciclo ha terminado.
print("Gracias por usar PEZ-RED. ¡Hasta pronto!")
"""

#2. Modifica este menu para que le permita el usuario realizar mas de una accion.
#   Por ejemplo, puedes agregar una accion que permita al usuario modificar su nombre.

#Usaremos una variable bool para indicar si el usuario desea continuar
#utilizando el programa o no
continuar = True

#Este ciclo se mantiene en ejecucion hasta que el usuario desee salir
while continuar:

    #Solicitamos opcion al usuario
    print("""Hola """, nombre, """, Ahora puedes realizar las siguientes acciones:    
          S. Escribir un mensaje
          M. Modificar tu nombre
          N. Salir""")
    opcion = str(input("¿Que deseas hacer? (S-M-N) "))

    #Vamos a aceptar que el usuario ingrese un mensaje cuando escriban "S", "s", o nada
    if opcion== "S" or opcion == "s" or opcion == "":
        mensaje = input("Vamos a publicar un mensaje. ¿Que piensas hoy? ")
        print()
        print("--------------------------------------------------")
        print(nombre, "dice:", mensaje)
        print("--------------------------------------------------")
    elif opcion == "N" or opcion == "n":
        continuar = False
    elif opcion == "M" or opcion == "m":
        nombre = input("Escribe el nombre por el cual cambiaras el que actualmente ocupas. ")
        print()
        print("Hola ", nombre, ", bienvenido a PEZ-RED")
    else:
        print("Por favor, ingrese una opcion valida.")
        print()

#Mensaje de salida, una vez que el ciclo ha terminado.
print("Gracias por usar PEZ-RED. ¡Hasta pronto!")