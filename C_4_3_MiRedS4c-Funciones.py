#Finalmente, podemos ver que nuestro archivo es cada vez mas grande.

#Vamos a crear un nuevo archivo .py y copiaremos en el todas las funciones que hemos definido.
#Llamaremos a este archivo S4Red.py. Luego, para poder utilizar estas funciones dentro de nuestro archivo
#principal, utilizaremos la instruccion import.
import C_4_3_S4Red as Red

#Aqui­ empieza el programa principal.

Red.mostrar_bienvenida()
(nombre, edad, estatura_m, estatura_cm, num_amigos) = Red.obtener_datos()

print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos)
print("Ya podemos preguntar, recordar y calcular datos. Esperamos que disfrutes con PEZ-RED")
print("--------------------------------------------------")

opcion = 1
while opcion != 0:
    opcion = Red.opcion_menu()
    if opcion == 1:
        mensaje = Red.obtener_mensaje()
        Red.mostrar_mensaje(nombre, None, mensaje)
    elif opcion == 2:
        mensaje = Red.obtener_mensaje()
        for i in range(num_amigos):
            nombre_amigo = input("Ingresa el nombre de tu amigo o amiga: ")
            Red.mostrar_mensaje(nombre, nombre_amigo, mensaje)
    elif opcion == 3:
        Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos)
    elif opcion == 4:
        nombre = Red.obtener_nombre()
        edad = Red.obtener_edad()
        (estatura_m, estatura_cm) = Red.obtener_estatura()
        num_amigos = Red.obtener_num_amigos()
        Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos)
    elif opcion == 0:
        print("Has decidido salir.")

print("Gracias por usar PEZ-RED. ¡Hasta pronto!")

# Como puedes ver, la parte principal de tu programa ahora es mucho más corta.
# Gran parte de la funcionalidad está encapsulada en funciones, y estas funciones están definidas
# en otro archivo que hemos importado.

# Al usar funciones podemos concentrarnos en partes más específicas de nuestro código,
# y nos ayuda a razonar a un nivel más alto.
