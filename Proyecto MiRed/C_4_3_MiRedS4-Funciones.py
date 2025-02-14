#Hola.
#En esta ocasion vamos a continuar con el codigo de nuestra red social,
#al cual le habiamos agregado un menu.
#
#El programa de la semana anterior permit­a:
#1. Obtener datos del usuario
#2. Consultar y mostrar varios mensajes de estado del usuario
#3. Escoger entre distintas acciones que el usuario puede realizar
#

#Si lograste agregar una opcion nueva al sistema, por ejemplo, para escribir los datos
#del perfil del usuario, habras notado que tienes que escribir de nuevo el codigo necesario
#con un print por cada dato. El codigo se vera como esta mas abajo.

'''
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
nombre = input("Para empezar, dime cómo te llamas. ")
print()
print("Hola ", nombre, ", bienvenido a PEZ-RED")
print()

# Cálculo de edad
año = int(input("Para preparar tu perfil, dime en qué año naciste. "))
edad = 2025 - año 
print()

# Cálculo de estatura
estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil. ¿Cuánto mides? Dímelo en metros. "))
estatura_m = int(estatura)
estatura_cm = int( (estatura - estatura_m)*100 )

# Cantidad de amigos
num_amigos = int(input("Muy bien. Finalmente, cuéntame cuantos amigos tienes. "))

#Con los datos recolectados escribimos en pantalla un texto que resuma los datos que hemos obtenido
print()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
print("--------------------------------------------------")
print("Nombre:  ", nombre)
print("Edad:    ", edad, "años")
print("Estatura:", estatura_m, "metros y", estatura_cm, "centímetros")
print("Amigos:  ", num_amigos)
print("--------------------------------------------------")
print("Gracias por la información. Esperamos que disfrutes con PEZ-RED")
print()

#Esta opcion permite entrar al ciclo. Solo interesa que no sea 0.
opcion = 1
while opcion != 0:
    print("Acciones disponibles:")
    print("  1. Escribir un mensaje público")
    print("  2. Escribir un mensaje solo a algunos amigos")
    print("  3. Mostrar los datos de perfil")
    print("  4. Actualizar el perfil de usuario")
    print("  0. Salir")
    opcion = int(input("Ingresa una opción: "))

    #Código para la opción 1. Publicar un mensaje.
    if opcion == 1:
        mensaje = input("Ahora vamos a publicar un mensaje. ¿Qué piensas hoy? ")
        print()
        print("--------------------------------------------------")
        print(nombre, "dice:", mensaje)
        print("--------------------------------------------------")

    #Código para la opción 2. Publicar un mensajes a un grupo de personas.
    elif opcion == 2:
        mensaje = input("Ahora vamos a publicar un mensaje a un grupo de amigos. ¿Qué quieres decirles? ")
        print()
        for i in range(num_amigos):
            nombre_amigo = input("Ingresa el nombre de tu amigo o amiga: ")
            print("--------------------------------------------------")
            print(nombre, "dice:", "@"+nombre_amigo, mensaje)
            print("--------------------------------------------------")

    #Código para la opción 3. Publicar los datos del perfil del usuario.
    elif opcion == 3:
        print("--------------------------------------------------")
        print("Nombre:   ", nombre)
        print("Edad:     ", edad, "años")
        print("Estatura: ", estatura_m, "m y ", estatura_cm, "centímetros")
        print("Amigos:   ", num_amigos)
        print("--------------------------------------------------")

    #Código para la opción 4. Actualizar los datos del perfil del usuario.
    elif opcion == 4:
        #Repetimos el código para solicitar datos
        # Solicitud de nombre
        nombre = input("Para empezar, dime cómo te llamas. ")
        print()
        print("Hola ", nombre, ", bienvenido a PEZ-RED")
        print()

        # Cálculo de edad
        año = int(input("Para preparar tu perfil, dime en qué año naciste. "))
        edad = 2025 - año 
        print()

        # Cálculo de estatura
        estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil. ¿Cuánto mides? Dímelo en metros. "))
        estatura_m = int(estatura)
        estatura_cm = int( (estatura - estatura_m)*100 )

        # Cantidad de amigos
        num_amigos = int(input("Muy bien. Finalmente, cuéntame cuantos amigos tienes. "))

        print()
        print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
        # Repetimos el código para mostrar los datos del usuario.
        print("--------------------------------------------------")
        print("Nombre:  ", nombre)
        print("Edad:    ", edad, "años")
        print("Estatura:", estatura_m, "metros y", estatura_cm, "centímetros")
        print("Amigos:  ", num_amigos)
        print("--------------------------------------------------")
        print()

    #Código para la opción 0. Salir.
    elif opcion == 0:
        print("Has decidido salir.")

    #Código para la opción que no coincida con ninguna anterior.
    else:
        print("No conozco la opción que has ingresado. Inténtalo otra vez.")

print()
print("Gracias por usar PEZ-RED. ¡Hasta pronto!")
print()

'''

#Si pruebas este código, verás que funciona correctamente, pero nuestro programa ahora es bastante largo.
#Casi 140 líneas.
#Esto en sí no es malo. Sin embargo, si le pones atención, verás que hay código que hemos tenido
#que repetir completamente. Por ejemplo, el código para mostrar el perfil de un usuario está escrito tres veces.
#Si ahora queremos agregar un nuevo dato del usuario, por ejemplo, el país en que vive, debemos modificar
#al menos tres partes distintas del programa.
#Esto lo podemos hacer, talvez sin cometer errores, en un programa pequeño como éste.
#Pero en programas más grandes, es muy fácil que nos olvidemos de actualizar una parte del código,
#o que no recordemos todas las partes que hay que modificar.

#Cuando tenemos instrucciones que se repiten tantas veces en distintas partes del programa,
# es una indicación de que talvez necesitamos agregar funciones.

#Te invitamos a pensar en al menos 3 alternativas o funcionalidades de este código
#que podrían convertirse en una función.

# Funciones 
# 1. Bienvenida 
def bienvenida():
    print("Bienvenido a ... ")
    print(''' 
                                                      .___
    ______   ____ ________         _______   ____   __| _/
    \____ \_/ __ \\___   /  ______ \_  __ \_/ __ \ / __ | 
    |  |_> >  ___/ /    /  /_____/  |  | \/\  ___// /_/ | 
    |   __/ \___  >_____ \          |__|    \___  >____ | 
    |__|        \/      \/                      \/     \/ 

    ''')

# 2. Perfil de usuario
def perfil_usuario():
    # Solicitud de nombre
    nombre = input("Para empezar, dime cómo te llamas. ")
    print()
    print("Hola ", nombre, ", bienvenido a PEZ-RED")
    print()

    # Cálculo de edad
    año = int(input("Para preparar tu perfil, dime en qué año naciste. "))
    edad = 2025 - año
    print()

    # Cálculo de estatura
    estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil. ¿Cuánto mides? Dímelo en metros. "))
    estatura_m = int(estatura)
    estatura_cm = int((estatura - estatura_m) * 100)
    print() 

    # Cantidad de amigos
    num_amigos = int(input("Muy bien. Finalmente, cuéntame cuantos amigos tienes. "))
    print()

    # Retornar los valores como una tupla
    return nombre, edad, estatura_m, estatura_cm, num_amigos

# 3. Datos del perfil de usuario
def datos_usuario():
    # Con los datos recolectados escribimos en pantalla un texto que resuma los datos que hemos obtenido
    print()
    print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
    print("--------------------------------------------------")
    print("Nombre:  ", nombre)
    print("Edad:    ", edad, "años")
    print("Estatura:", estatura_m, "metros y", estatura_cm, "centímetros")
    print("Amigos:  ", num_amigos)
    print("--------------------------------------------------")
    print("Gracias por la información. Esperamos que disfrutes con PEZ-RED")
    print()

# 4. Escribir mensaje al público
def msj_publico():
    mensaje = input("Ahora vamos a publicar un mensaje. ¿Qué piensas hoy? ")
    print()
    print("--------------------------------------------------")
    print(nombre, "dice:", mensaje)
    print("--------------------------------------------------")

# 5. Escribir mensaje a amigos
def msj_amigos():
    mensaje = input("Ahora vamos a publicar un mensaje a un grupo de amigos. ¿Qué quieres decirles? ")
    print()
    for i in range(num_amigos):
        nombre_amigo = input("Ingresa el nombre de tu amigo o amiga: ")
        print("--------------------------------------------------")
        print(nombre, "dice:", "@"+nombre_amigo, mensaje)
        print("--------------------------------------------------")

# 6. Menu de opciones
def menu ():
    print("Acciones disponibles:")
    print("  1. Escribir un mensaje público")
    print("  2. Escribir un mensaje solo a algunos amigos")
    print("  3. Mostrar los datos de perfil")
    print("  4. Actualizar el perfil de usuario")
    print("  0. Salir")

# 7. Despedida
def despedida():
    print()
    print("Gracias por usar PEZ-RED. ¡Hasta pronto!")
    print()
    

# Inicia programa normal 
bienvenida()

(nombre, edad, estatura_m, estatura_cm, num_amigos) = perfil_usuario()

datos_usuario()

opcion = 1
while opcion != 0:
    menu()
    opcion = int(input("Ingresa una opción: "))

    if opcion == 1:
        msj_publico()

    elif opcion == 2:
        msj_amigos()

    elif opcion == 3:
        datos_usuario()

    elif opcion == 4:
        (nombre, edad, estatura_m, estatura_cm, num_amigos) = perfil_usuario()
        datos_usuario()

    elif opcion == 0:
        print("Has decidido salir.")

    else:
        print("No conozco la opción que has ingresado. Inténtalo otra vez.")

despedida()