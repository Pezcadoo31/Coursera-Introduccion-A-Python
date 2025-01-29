# Vamos a modificar el código que acabamos de ver para encapsular algunas partes de él
# en funciones.

# En particular haremos esto con:
# 1. El mensaje de bienvenida
# 2. El código para solicitar datos al usuario.
# 3. El código para mostrar el perfil del usuario
# 4. El código para mostrar un mensaje en pantalla

'''
def mostrar_bienvenida():
    print("Bienvenido a ... ")
    print("""
                  _                  __
       ____ ___  (_)  ________  ____/ /
      / __ `__ \/ /  / ___/ _ \/ __  /
     / / / / / / /  / /  /  __/ /_/ /
    /_/ /_/ /_/_/  /_/   \___/\__,_/

    """)

def obtener_nombre():
    nombre = input("Para empezar, dime cómo te llamas. ")
    return nombre

def obtener_edad():
    año = int(input("Para preparar tu perfil, dime en qué año naciste. "))
    return 2025 - año 

def obtener_estatura():
    estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil. ¿Cuánto mides? Dímelo en metros. "))
    metros = int(estatura)
    centimetros = int((estatura - metros) * 100)
    return (metros, centimetros)

def obtener_num_amigos():
    amigos = int(input("Muy bien. Finalmente, cuéntame cuántos amigos tienes. "))
    return amigos

def mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos):
    print("--------------------------------------------------")
    print("Nombre:   ", nombre)
    print("Edad:     ", edad, "años")
    print("Estatura: ", estatura_m, "m y ", estatura_cm, "centímetros")
    print("Amigos:   ", num_amigos)
    print("--------------------------------------------------")

def opcion_menu():
    print("Acciones disponibles:")
    print("  1. Escribir un mensaje público")
    print("  2. Escribir un mensaje solo a algunos amigos")
    print("  3. Mostrar los datos de perfil")
    print("  4. Actualizar el perfil de usuario")
    print("  0. Salir")
    opcion = int(input("Ingresa una opción: "))
    while opcion < 0 or opcion > 4:
        print("No conozco la opción que has ingresado. Inténtalo otra vez.")
        opcion = int(input("Ingresa una opción: "))
    return opcion

def obtener_mensaje():
    mensaje = input("Ahora vamos a publicar un mensaje. ¿Qué piensas hoy? ")
    return mensaje

def mostrar_mensaje(origen, destinatario, mensaje):
    print("--------------------------------------------------")
    if destinatario == None:
        print(origen, "dice:", mensaje)
    else:
        print(origen, "dice:", "@"+destinatario, mensaje)
    print("--------------------------------------------------")

############################################################
# El código anterior era solamente definición de funciones que serán usadas más adelante
# Ahora empieza el programa principal.

mostrar_bienvenida()
nombre = obtener_nombre()
print()
print("Hola ", nombre, ", bienvenido a PEZ-RED")
print()
edad = obtener_edad()
(estatura_m, estatura_cm) = obtener_estatura()
num_amigos = obtener_num_amigos()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos)
print("Ya podemos preguntar, recordar y calcular datos. Esperamos que disfrutes con PEZ-RED")
print("--------------------------------------------------")

# Ingresamos al ciclo que permite ejecutar acciones
opcion = 1
while opcion != 0:
    # Mostramos el menu
    opcion = opcion_menu()

    #Código para la opción 1. Publicar un mensaje.
    if opcion == 1:
        mensaje = obtener_mensaje()
        mostrar_mensaje(nombre, None, mensaje)

    #Código para la opción 2. Publicar un mensaje a un grupo de personas.
    elif opcion == 2:
        mensaje = obtener_mensaje()
        for i in range(num_amigos):
            nombre_amigo = input("Ingresa el nombre de tu amigo o amiga: ")
            mostrar_mensaje(nombre, nombre_amigo, mensaje)

    #Código para la opción 3. Publicar los datos del perfil del usuario.
    elif opcion == 3:
        mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos)

    #Código para la opción 4. Actualizar los datos del perfil del usuario.
    elif opcion == 4:
        nombre = obtener_nombre()
        edad = obtener_edad()
        (estatura_m, estatura_cm) = obtener_estatura()
        num_amigos = obtener_num_amigos()
        mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos)
    elif opcion == 0:
        print("Has decidido salir.")

print("Gracias por usar PEZ-RED. ¡Hasta pronto!")
'''

#Como puedes ver, una vez que no hay más definiciones de funciones, el programa principal empieza.
#Si lo lees, podrás ver que es mucho más corto, y que hay menos código repetido que en la versión anterior.

#Te proponemos como desafío:
#1. Agrega el atributos como "sexo" y "pais de nacimiento"
#   a los datos que se le piden al usuario, y permite que sean solicitados y leídos usando funciones.
#   Tendrás que identificar en qué partes del código debes hacer esa modificación.


# Codigo de la solucion
def mostrar_bienvenida():
    print("Bienvenido a ... ")
    print(""" 
                                                      .___
    ______   ____ ________         _______   ____   __| _/
    \____ \_/ __ \\___   /  ______ \_  __ \_/ __ \ / __ | 
    |  |_> >  ___/ /    /  /_____/  |  | \/\  ___// /_/ | 
    |   __/ \___  >_____ \          |__|    \___  >____ | 
    |__|        \/      \/                      \/     \/ 

    """)

def obtener_nombre():
    nombre = input("Para empezar, dime cómo te llamas. ")
    return nombre

def obtener_edad():
    año = int(input("Para preparar tu perfil, dime en qué año naciste. "))
    return 2025 - año 

def obtener_estatura():
    estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil. ¿Cuánto mides? Dímelo en metros. "))
    metros = int(estatura)
    centimetros = int((estatura - metros) * 100)
    return (metros, centimetros)

def obtener_num_amigos():
    amigos = int(input("Muy bien. Finalmente, cuéntame cuántos amigos tienes. "))
    return amigos

# Agregamos las funciones para obtener el sexo y el pais de nacimiento
def obtener_sexo():
    sexo = input("¿Cuál es tu sexo? (Masculino/Femenino/*) ")
    return sexo

def pais_nacimiento():
    pais = input("¿En qué país naciste? ")
    return pais

# Modificación al mostrar_perfil para agregar el sexo y el pais de nacimiento
def mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos, sexo, pais):
    print("--------------------------------------------------")
    print("Nombre:   ", nombre)
    print("Edad:     ", edad, "años")
    print("Estatura: ", estatura_m, "m y ", estatura_cm, "centímetros")
    print("Amigos:   ", num_amigos)
    print("Sexo:     ", sexo)
    print("País:     ", pais)   
    print("--------------------------------------------------")

def opcion_menu():
    print("Acciones disponibles:")
    print("  1. Escribir un mensaje público")
    print("  2. Escribir un mensaje solo a algunos amigos")
    print("  3. Mostrar los datos de perfil")
    print("  4. Actualizar el perfil de usuario")
    print("  0. Salir")
    opcion = int(input("Ingresa una opción: "))
    while opcion < 0 or opcion > 4:
        print("No conozco la opción que has ingresado. Inténtalo otra vez.")
        opcion = int(input("Ingresa una opción: "))
    return opcion

def obtener_mensaje():
    mensaje = input("Ahora vamos a publicar un mensaje. ¿Qué piensas hoy? ")
    return mensaje

def mostrar_mensaje(origen, destinatario, mensaje):
    print("--------------------------------------------------")
    if destinatario == None:
        print(origen, "dice:", mensaje)
    else:
        print(origen, "dice:", "@"+destinatario, mensaje)
    print("--------------------------------------------------")

# Inicialización del programa utilizando las funciones
mostrar_bienvenida()

nombre = obtener_nombre()
print()
print("Hola ", nombre, ", bienvenido a PEZ-RED")
print()

edad = obtener_edad()
print()

(estatura_m, estatura_cm) = obtener_estatura()
print()

num_amigos = obtener_num_amigos()
print()

# Agregamos las llamadas a las funciones para obtener el sexo y el pais de nacimiento
sexo = obtener_sexo()
print()
pais = pais_nacimiento()
print()

print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos, sexo, pais)
print("Ya podemos preguntar, recordar y calcular datos. Esperamos que disfrutes con PEZ-RED")
print("--------------------------------------------------")

# Ingresamos al ciclo que permite ejecutar acciones
opcion = 1
while opcion != 0:
    # Mostramos el menu
    opcion = opcion_menu()

    #Código para la opción 1. Publicar un mensaje.
    if opcion == 1:
        mensaje = obtener_mensaje()
        mostrar_mensaje(nombre, None, mensaje)

    #Código para la opción 2. Publicar un mensaje a un grupo de personas.
    elif opcion == 2:
        mensaje = obtener_mensaje()
        for i in range(num_amigos):
            nombre_amigo = input("Ingresa el nombre de tu amigo o amiga: ")
            mostrar_mensaje(nombre, nombre_amigo, mensaje)

    #Código para la opción 3. Publicar los datos del perfil del usuario.
    elif opcion == 3:
        mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos, sexo, pais)

    #Código para la opción 4. Actualizar los datos del perfil del usuario.
    elif opcion == 4:
        nombre = obtener_nombre()
        edad = obtener_edad()
        (estatura_m, estatura_cm) = obtener_estatura()
        num_amigos = obtener_num_amigos()
        sexo = obtener_sexo()
        pais = pais_nacimiento()
        mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos, sexo, pais)
    elif opcion == 0:
        print("Has decidido salir.")

print("Gracias por usar PEZ-RED. ¡Hasta pronto!")







