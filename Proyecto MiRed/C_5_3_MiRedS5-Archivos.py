#Hola.
#Hasta ahora nuestra red social incluye estas caracteristicas:

#El programa de la semana anterior permitia:
#1. Obtener datos del usuario
#2. Consultar y mostrar varios mensajes de estado del usuario
#3. Escoger entre distintas acciones que el usuario puede realizar
#4. Modificar el perfil del usuario
#
#Y ademas algunas de estas funcionalidades estan encapsulados en un modulo, de manera
#que tu codigo principal es cada vez mas corto y puedes concentrarte en la funcionalidad principal.

#Vamos por la siguiente evolucion de nuestra red social.

#Habras notado que cada vez que ejecutamos nuestro programa de red social, debemos ingresar
#todos los datos del usuario que esta utilizando el programa, antes de poder alcanzar
#el menu de opciones. Esto es bastante engorroso.

#Sin embargo, ahora sabemos que podemos utilizar memoria secundaria de nuestro computador,
#esto es, espacio del disco, para guardar archivos. Vamos a usar esto para que nuestro
#programa pueda recordar los datos de los usuarios, y evitar tener que escribirlos en cada ocasion.

# Y la estrategia que usaremos es la siguiente.
# Cada vez que un usuario nuevo utilice nuestro programa, vamos a guardar un archivo con sus datos.
# El nombre de este archivo será el nombre del usuario, seguido de la extensión '.user'.
# En este archivo guardaremos una línea por cada variable importante de nuestro usuario.

# De esta manera, la próxima vez que ejecutemos nuestro programa, lo primero que haremos será preguntar
# el nombre del usuario, y ver si existe un archivo con ese nombre.
# Si existe, entonces lo leemos desde el disco, y evitamos tener que preguntar todos sus datos.
# Si no existe, entonces seguimos comportándonos como antes, lo tratamos como un usuario nuevo, y preguntamos
# sus datos para luego crear un archivo.

'''
# Recordemos que en este módulo están todas las funciones adicionales que hemos creado.
import C_5_3_S5Red as Red
# El módulo 'os' nos permitirá consultar si un archivo existe.
import os

Red.mostrar_bienvenida()
nombre = Red.obtener_nombre()
print("Hola ", nombre, ", bienvenido a PEZ-RED")

#Verificamos si el archivo existe
if os.path.isfile(nombre+".user"):
    #Esto lo hacemos si ya habi­a un usuario con ese nombre
    print("Leyendo datos de usuario", nombre, "desde archivo.")
    archivo_usuario = open(nombre+".user","r")
    nombre = archivo_usuario.readline()
    edad = int(archivo_usuario.readline())
    estatura = float(archivo_usuario.readline())
    estatura_m = int(estatura)
    estatura_cm = int( (estatura - estatura_m)*100 )
    sexo = archivo_usuario.readline()
    pais = archivo_usuario.readline()
    num_amigos = int(archivo_usuario.readline())
    estado = archivo_usuario.readline()
    #Una vez que hemos leido los datos del usuario no debemos olvidar cerrar el archivo
    archivo_usuario.close()

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
        archivo_usuario = open(nombre+".user","w")
        archivo_usuario.write(nombre+"\n")
        archivo_usuario.write(str(edad)+"\n")
        archivo_usuario.write(str(estatura_m + estatura_cm/100)+"\n")
        archivo_usuario.write(sexo+"\n")
        archivo_usuario.write(pais+"\n")
        archivo_usuario.write(str(num_amigos)+"\n")
        archivo_usuario.write(estado+"\n")
        #Una vez que hemos escrito todos los datos del usuario en el archivo, no debemos olvidar cerrarlo
        archivo_usuario.close()
        print("Archivo",nombre+".user","guardado")



print("Gracias por usar PEZ-RED. ¡Hasta pronto!")
'''

#Cuando ejecutes este programa por primera vez, veras que se crea un archivo nuevo en tu computador
#cada vez que ingresas con el nombre de un usuario nuevo. Prueba a ingresar
#con un nombre de usuario que ya habias usado antes.

#Este programa es bastante mas completo que los que teniamos antes, sin embargo aun tiene cosas
#por mejorar. Por ejemplo, ¿que ocurre si el archivo esta mal escrito, o si le falta alguna linea?
#¿Que ocurre si en una ocasion ingreso mi nombre con mayusculas, y en otra ocasion lo hago con minusculas?
#
#Te invitamos a corregir dos detalles en este programa
#1. Al leer las lineas del archivo, siempre se leen como ultimos caracteres, algunos caracteres blancos como
#   espacios y el caracter de cambio de linea ('\n'). Esto hace que los nombres de archivos creados incluyan
#   estos caracteres adicionales. Puedes utilizar los metodos de str para eliminar este tipo de caracteres
#   que llamamos "no imprimibles"
#2. Utiliza tu conocimiento de funciones para crear funciones que lean desde un archivo,
#   y retornen el conjunto de datos leidos, de manera de encapsular el proceso de lectura y escritura,
#   y reducir el tamaño de tu codigo.


# Codigo con correcciones de la actividad
# Para la corrección de este codigo se crearon las funciones leer_datos y escribir_datos en el modulo C_5_3_S5Red.py
# Mientras que para la corrección de los datos no imprimibles se utilizo el metodo strip() para eliminar los espacios en blanco
import C_5_3_S5Red as Red
import os

Red.mostrar_bienvenida()
nombre = Red.obtener_nombre()
print()
print("Hola ", nombre, ", bienvenido a PEZ-RED")

#Verificamos si el archivo existe
if os.path.isfile(nombre+".user"):
    #Esto lo hacemos si ya habi­a un usuario con ese nombre
    print("Leyendo datos de usuario", nombre, "desde archivo.")
    # Se llama a la función leer_datos, ahora el código es más limpio
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
        # Se llama a la función escribir_datos, para guardar los datos del usuario
        Red.escribir_usuario(nombre, edad, estatura_m, estatura_cm, sexo, pais, num_amigos, estado)
        print("Archivo",nombre+".user","guardado")

print("Gracias por usar PEZ-RED. ¡Hasta pronto!")

# Si quisieramos corregir la parte de que el usuario entre con mayusculas o minusculas, 
# se podria solucionar con la función upper() que convierte todo a mayusculas o lower() que convierte todo a minusculas
# en la función obtener_nombre() de C_5_3_S5Red.py