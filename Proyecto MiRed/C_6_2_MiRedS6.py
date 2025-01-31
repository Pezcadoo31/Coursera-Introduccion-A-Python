#Hola
#Ahora que ya conocemos como utilizar listas, podemos agregar una funcionalidad mucho mas interesante
#a nuestra red social, y que nos hacia falta: administrar listas de amigos y de mensajes

#Hemos agregado dos valores nuevos para el perfil del usuario: una lista de amigos, y una lista de mensajes
#que llamaremos "muro"

#La lista de mensajes reemplazara a nuestro antiguo valor "num_amigos". Al conocer la lista de amigos,
#tambien conoceremos la cantidad de amigos. Observa como leemos la lista de amigos en la funcion
#obtener_lista_amigos.
#Observa tambien como se han modificado las funciones leer_archivo() y escribir_archivo()
#para ser concordantes con la nueva estructura de los archivos ".user"

#La segunda caracteristica sera la publicacion de un muro.
#En el archivo de cada usuario, luego de escribir su estado actual, agregaremos una lista de los mensajes
#que han sido publicados por sus amigos, de manera de formar una lista de mensajes que llamaremos "muro", o 'timeline',
#presente en casi todas las redes sociales.

'''
#En este modulo estan todos las funciones  que hemos creado hasta ahora
import C_6_2_S6Red as Red


Red.mostrar_bienvenida()
nombre = Red.obtener_nombre()
print("Hola ", nombre, ", bienvenido a PEZ-RED")

#Verificamos si el archivo existe
if Red.existe_archivo(nombre+".user"):
    #Esto lo hacemos si ya habÃra un usuario con ese nombre
    print("Leyendo datos de usuario", nombre, "desde archivo.")
    (nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos, estado, muro) = Red.leer_usuario(nombre)

else:
    #En caso que el usuario no exista, consultamos por sus datos tal como lo haciamos antes
    print()
    edad = Red.obtener_edad()
    (estatura_m, estatura_cm) = Red.obtener_estatura()
    sexo = Red.obtener_sexo()
    pais = Red.obtener_pais()
    amigos = Red.obtener_lista_amigos()
    estado = ""
    muro = []

#En ambos casos, al llegar aqui­ ya conocemos los datos del usuario
print("Muy bien. Estos son los datos de tu perfil.")
Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos)
Red.mostrar_mensaje(nombre, estado)

#Ahora podemos mostrar el menu y consultar las opciones
opcion = 1
while opcion != 0:
    opcion = Red.opcion_menu()
    if opcion == 1:
        estado = Red.obtener_mensaje()
        Red.publicar_mensaje(nombre, amigos, estado, muro)
    elif opcion == 2:
        Red.mostrar_muro(muro)
    elif opcion == 3:
        Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos)
    elif opcion == 4:
        edad = Red.obtener_edad()
        (estatura_m, estatura_cm) = Red.obtener_estatura()
        sexo = Red.obtener_sexo()
        pais = Red.obtener_pais()
        amigos = Red.obtener_lista_amigos()
        Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos)
    elif opcion == 0:
        print("Has decidido salir. Guardando perfil en ",nombre+".user")
        Red.escribir_usuario(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos, estado,muro)
        print("Archivo",nombre+".user","guardado")

print("Gracias por usar PEZ-RED. ¡Hasta pronto!")
'''

#Prueba este programa, e intenta enviar un mensaje a los amigos que pertenecen a tu lista.
#Te invitamos a ejecutar los siguientes desafios:
#1. Agrega una opcion que permita agregar un nuevo amigo a tu lista. En este caso no utilizaremos confirmacion
#   de parte del destinatario, de manera que la relacion de amistad puede perfectamente existir en un solo sentido.
#
#2. Agrega una opcion que permita mostrar los ultimos estados de todos los amigos.
#   Ten en cuenta que esto no es equivalente a publicar los mensajes de tu muro, sino que necesitaras
#   leer una li­nea particular de los archivos de cada usuario en tu lista de amigos.
#

# Soluciones a los desafios propuestos 
import C_6_2_S6Red as Red

Red.mostrar_bienvenida()
nombre = Red.obtener_nombre()
print("Hola ", nombre, ", bienvenido a PEZ-RED")

#Verificamos si el archivo existe
if Red.existe_archivo(nombre+".user"):
    #Esto lo hacemos si ya habÃra un usuario con ese nombre
    print("Leyendo datos de usuario", nombre, "desde archivo.")
    (nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos, estado, muro) = Red.leer_usuario(nombre)

else:
    #En caso que el usuario no exista, consultamos por sus datos tal como lo haciamos antes
    print()
    edad = Red.obtener_edad()
    (estatura_m, estatura_cm) = Red.obtener_estatura()
    sexo = Red.obtener_sexo()
    pais = Red.obtener_pais()
    amigos = Red.obtener_lista_amigos()
    estado = ""
    muro = []

#En ambos casos, al llegar aqui­ ya conocemos los datos del usuario
print("Muy bien. Estos son los datos de tu perfil.")
Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos)
Red.mostrar_mensaje(nombre, estado)

#Ahora podemos mostrar el menu y consultar las opciones
opcion = 1
while opcion != 0:
    opcion = Red.opcion_menu()
    if opcion == 1:
        estado = Red.obtener_mensaje()
        Red.publicar_mensaje(nombre, amigos, estado, muro)
    elif opcion == 2:
        Red.mostrar_muro(muro)
    elif opcion == 3:
        Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos)
    elif opcion == 4:
        edad = Red.obtener_edad()
        (estatura_m, estatura_cm) = Red.obtener_estatura()
        sexo = Red.obtener_sexo()
        pais = Red.obtener_pais()
        amigos = Red.obtener_lista_amigos()
        Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos)
    elif opcion == 5: # Desafio 1
        amigos = Red.agregar_amigos(amigos)
        print("Ahora tienes", len(amigos), "amigos")
    elif opcion == 6:
        Red.leer_mensajes(amigos) # Desafio 2
    elif opcion == 0:
        print("Has decidido salir. Guardando perfil en ",nombre+".user")
        Red.escribir_usuario(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos, estado,muro)
        print("Archivo",nombre+".user","guardado")

print("Gracias por usar PEZ-RED. ¡Hasta pronto!")

