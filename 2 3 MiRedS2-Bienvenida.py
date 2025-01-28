#Hola, para empezar con nuestro proyecto de red social, vamos a utilizar
#las herramientas que conocemos para ejecutar algunas acciones.
#
#Primero, mostraremos un mensaje en pantalla dando la bienvenida al usuario
#y escribiendo el nombre de la red.

#A continuacion preguntaremos algunos datos al usuario para poder construir su perfil,
#y guardaremos esta informacion en variables.

#Finalmente, escribiremos en pantalla todos los datos que hemos recolectado, y permitiremos
#al usuario escribir un mensaje de estado.

#Te invito a examinar el codigo, leer los comentarios y comprender los tipos de datos
#que estamos utilizando en cada caso.


#Para conocer un poco mas del usuario, vamos a preguntarle algunos datos.
#Por ejemplo, su año de nacimiento, y aprovecharemos este dato descubrir la edad del usuario.
#¿Como lo haremos?, usaremos una variable para guardar el resultado del calculo de
#la edad del usuario. Este es un dato de tipo entero.

#A continuacion le preguntaremos al usuario su estatura en metros. Este es un dato de tipo float,
#y usaremos esta informacion para calcular los centimetros

#Finalmente escribiremos en pantalla los datos que hemos recordado del usuario usando print y le solicitaremos
#que escriba un mensaje para desplegar en pantalla.

############################################################
# Lo primero que haremos sera escribir un mensaje de bienvenida al usuario
# con el nombre de la red. Puedes modificar este mensajes para que represente el nombre de tu propia red
# Considera que al escribir """ tambiÃ©n estamos delimitado un string, pero al hacerlo de esta manera,
# cambios de li­nea que ocurran en el codigo se considerarÃ¡n como parte del string.
# Si no estas convencido, prueba el funcionamiento reemplazando los delimitadores por "

print("Bienvenido a ... ")
print("""
                                                  .___
______   ____ ________         _______   ____   __| _/
\____ \_/ __ \\___   /  ______ \_  __ \_/ __ \ / __ | 
|  |_> >  ___/ /    /  /_____/  |  | \/\  ___// /_/ | 
|   __/ \___  >_____ \          |__|    \___  >____ | 
|__|        \/      \/                      \/     \/ 

""")

#Primera interaccion. Solicitamos al usuario que ingrese su nombre,
#y lo guardamos en una variable de tipo str
nombre = input("Para empezar, dime como te llamas. ")
print()
print("Hola ", nombre, ", bienvenido a Mi Red")
print()

#Segunda interaccion. Solicitamos el ingreso del año, y utilizamos este
#dato para estimar la edad de la persona. ¿Por que decimos que solo estamos "estimando" su edad?
#¿Que ocurre si eliminamos la conversion a tipo de dato 'int' de la siguiente li­nea?
año = int(input("Para preparar tu perfil, dime en que año naciste. "))
edad = 2025-año 
print()

#Tercera interaccion. Solicitamos la estatura, medida en metros.
#Utilizamos la conversion a 'int', y una expresion para convertir esto
#a una medida en metros y centimetros
estatura = float(input("Cuentame mas de ti, para agregarlo a tu perfil. ¿Cuanto mides? Dimelo en metros. "))
estatura_m = int(estatura)
estatura_cm = int( (estatura - estatura_m)*100 )
print()

#Cuarta interaccion. Consultamos cuantos amigos tiene el usuario.
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

#Finalmente, solicitamos un mensaje de prueba que sirva para publicar un estado del usuario.
mensaje = input("Ahora vamos a publicar tu primer mensaje. ¿Que piensas hoy? ")
print()
print("--------------------------------------------------")
print(nombre, "dice:", mensaje)
print("--------------------------------------------------")
print()

#Ahora puedes practicar solicitando mas datos al usuario. Solo tienes que usar apropiadamente input() y print()
#1. Escribe 3 solicitudes de datos al usuario, por ejemplo sexo, numero de telefono, ciudad donde vive,
#   pais de nacimiento, direccion, etc. Guarda esos datos en variables del tipo, y finalmente escribelos en pantalla
#   utilizando print. Puedes agregar todas las li­neas que necesites.

# Interaciones creadas por abdy_vincent

#Quinta interaccion. Solicitamos el ingreso del sexo del usuario.
print("Continuemos con la creacion de tu perfil")
sexo = input("Por favor, dime el sexo con el que te identificas: ")
print("Perfecto,", nombre, "ahora sabemos que eres", sexo)
print()

# Sexta interaccion. Solicitamos el ingreso del numero de telefono del usuario.
telefono = input("Por favor, dime cual es tu numero de telefono: ")
print("Gracias,", nombre, "tu numero de telefono ha sido guardado")
print()

# Septima interacción. Solicitamos su dirección del usuario, al igual que su lugar de nacimiento. 
Pais_de_nacimeinto = input("Perfecto, ¿por que no nos cuentas en que pais naciste ? ")
Ciudad_de_residencia = input ("¿En que ciudad vives actualmente? ")
Direccion = input("No olvides registrar tu dirección ")
print()

# Nuevo resumen del usuario
print()
print("Muy bien,", nombre, ". Entonces podemos actualizar tu perfil con estos datos.")
print("--------------------------------------------------")
print("Nombre:              ", nombre)
print("Edad:                ", edad, "años")
print("Estatura:            ", estatura_m, "metros y", estatura_cm, "centimetros")
print("Amigos:              ", num_amigos)
print("Sexo:                ", sexo)
print("Num. telefono:       ", telefono)
print("Pais de Nacimeinto:  ", Pais_de_nacimeinto)
print("Ciudad de Residencia:", Ciudad_de_residencia)
print("Dirección:           ", Direccion)
print("--------------------------------------------------")
print("Gracias por la informacion. Esperamos que disfrutes con PEZ-RED")
print()
