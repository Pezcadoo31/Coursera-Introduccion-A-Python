# filepath: /c:/Users/abdyv/OneDrive/Documentos/PYTHON/Coursera/Actividades y Ejercicios/C_5_2_Archivos.py
# Módulo de aprendizaje sobre el uso de archivos en Python

# En Python, un archivo se puede abrir con la función open().
# El modo del archivo puede ser de lectura (r), escritura (w), o de agregar (a).
arc = open("c:/Users/abdyv/OneDrive/Documentos/PYTHON/Coursera/Actividades y Ejercicios/archivo.txt", "r")

# Para leer el contenido de un archivo, se puede utilizar el método read().
leer = arc.read()
print(leer)
print()

# Lectura de un archivo línea por línea
leer1 = arc.readline()
print(leer1)
leer2 = arc.readline()
print(leer2)
print()

# Escribir en un archivo
escritura = open("archivo2.txt", "w")  # Aqui me di cuenta que el archivo se creo fuera de la carpeta de actividades y ejercicios 
# y por eso, en arc tuve que escribir la ruta completa del archivo para que lo reconociera
escritura.write("Hola, este es un archivo de texto.")
escritura.write("\n Uno \n Dos \n Tres")

# Cerrar un archivo
arc.close()
escritura.close()


