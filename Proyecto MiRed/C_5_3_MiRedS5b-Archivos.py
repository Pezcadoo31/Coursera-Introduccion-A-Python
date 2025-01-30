#Esta version utiliza archivos para almacenar y leer los datos de cada usuario de nuestra red social.

#Ademas encapsula el proceso de lectura y escritura de archivos en el modulo Red, de manera de hacer
#que el codigo sea mas facil de comprender.
'''
#Recordemos que en este modulo estan todos las funciones adicionales que hemos creado.
import C_5_3_S5Red2 as Red

Red.mostrar_bienvenida()
nombre = Red.obtener_nombre()
print("Hola ", nombre, ", bienvenido a PEZ-RED")

#Verificamos si el archivo existe
if Red.existe_archivo(nombre+".user"):
    #Esto lo hacemos si ya habia un usuario con ese nombre
    print("Leyendo datos de usuario", nombre, "desde archivo.")
    (nombre, edad, estatura_m, estatura_cm, sexo, pais, num_amigos, estado) = Red.leer_usuario(nombre)

else:
    #En caso que el usuario no exista, consultamos por sus datos tal como lo haciamos antes
    print()
    edad = Red.obtener_edad()
    (estatura_m, estatura_cm) = Red.obtener_estatura()
    sexo = Red.obtener_sexo()
    pais = Red.obtener_pais()
    num_amigos = Red.obtener_num_amigos()
    estado = ""

#En ambos casos, al llegar aqui­ ya conocemos los datos del usuario
print("Muy bien. Estos son los datos de tu perfil.")
Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, num_amigos)
Red.mostrar_mensaje(nombre, None, estado)

#Ahora podemos mostrar el menu y consultar las opciones
opcion = 1
while opcion != 0:
    opcion = Red.opcion_menu()
    if opcion == 1:
        estado = Red.obtener_mensaje()
        Red.mostrar_mensaje(nombre, None, estado)

    elif opcion == 2:
        estado = Red.obtener_mensaje()
        for i in range(num_amigos):
            nombre_amigo = input("Ingresa el nombre de tu amigo o amiga: ")
            Red.mostrar_mensaje(nombre, nombre_amigo, estado)

    elif opcion == 3:
        Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, num_amigos)

    elif opcion == 4:
        edad = Red.obtener_edad()
        (estatura_m, estatura_cm) = Red.obtener_estatura()
        sexo = Red.obtener_sexo()
        pais = Red.obtener_pais()
        num_amigos = Red.obtener_num_amigos()
        Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, num_amigos)

    elif opcion == 0:
        print("Has decidido salir. Guardando perfil en ",nombre+".user")
        Red.escribir_usuario(nombre, edad, estatura_m, estatura_cm, sexo, pais, num_amigos, estado)
        print("Archivo",nombre+".user","guardado")

print("Gracias por usar PEZ-RED. ¡Hasta pronto!")
'''

#Te proponemos que completes el siguiente ejercicio:
#1. Ingresa al programa de red social con distintos usuarios. Luego de eso tendras varios archivos con extension
#   '.user'. Abre cualquiera de ellos con un editor de texto y edita algun valor.
#   A continuacion inicia tu programa y entra con el nombre de uno de usuarios. ¿Se actualizan los datos?

"""
 Primero se decidio crear el perfil de Avans 
 Seguido por el de esva 
 Se decidio cambiar el numero de amigos de esva de 1 a 4, asi como su edad de 25 a 52
 Al volver a entrar con el usuario esva, se observa que los datos se han actualizado correctamente

"""

#2. Agrega una nueva opcion que se llame "Cambiar de usuario". Con esta opcion el programa, sin salirse
#   de la red, el programa solicita un nuevo nombre y, en caso que exista un archivo con el nombre
#   de ese usuario, se cargan sus datos. Si el archivo no existe, basta con indicar que no se puede
#   cambiar a ese usuario.

# Codigo con la nueva opcion de cambiar de usuario
import C_5_3_S5Red2 as Red

Red.mostrar_bienvenida()
nombre = Red.obtener_nombre()
print("Hola ", nombre, ", bienvenido a PEZ-RED")

#Verificamos si el archivo existe
if Red.existe_archivo(nombre+".user"):
    #Esto lo hacemos si ya habia un usuario con ese nombre
    print("Leyendo datos de usuario", nombre, "desde archivo.")
    (nombre, edad, estatura_m, estatura_cm, sexo, pais, num_amigos, estado) = Red.leer_usuario(nombre)

else:
    #En caso que el usuario no exista, consultamos por sus datos tal como lo haciamos antes
    print()
    edad = Red.obtener_edad()
    (estatura_m, estatura_cm) = Red.obtener_estatura()
    sexo = Red.obtener_sexo()
    pais = Red.obtener_pais()
    num_amigos = Red.obtener_num_amigos()
    estado = ""

#En ambos casos, al llegar aqui­ ya conocemos los datos del usuario
print("Muy bien. Estos son los datos de tu perfil.")
Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, num_amigos)
Red.mostrar_mensaje(nombre, None, estado)

#Ahora podemos mostrar el menu y consultar las opciones
opcion = 1
while opcion != 0:
    opcion = Red.opcion_menu()
    if opcion == 1:
        estado = Red.obtener_mensaje()
        Red.mostrar_mensaje(nombre, None, estado)

    elif opcion == 2:
        estado = Red.obtener_mensaje()
        for i in range(num_amigos):
            nombre_amigo = input("Ingresa el nombre de tu amigo o amiga: ")
            Red.mostrar_mensaje(nombre, nombre_amigo, estado)

    elif opcion == 3:
        Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, num_amigos)

    elif opcion == 4:
        edad = Red.obtener_edad()
        (estatura_m, estatura_cm) = Red.obtener_estatura()
        sexo = Red.obtener_sexo()
        pais = Red.obtener_pais()
        num_amigos = Red.obtener_num_amigos()
        Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, num_amigos)

    elif opcion == 5:
        nombre = Red.cambiar_usuario(nombre)

    elif opcion == 0:
        print("Has decidido salir. Guardando perfil en ", nombre + ".user")
        Red.escribir_usuario(nombre, edad, estatura_m, estatura_cm, sexo, pais, num_amigos, estado)
        print("Archivo",nombre+".user","guardado")

print("Gracias por usar PEZ-RED. ¡Hasta pronto!")

