# Aprendizaje sobre la importacion y llamado de modulos

# Importación de librerias 
from random import randint as rnd
from math import pi, e 

Lanzamiento = rnd(1, 6) 
if Lanzamiento < 4:
    print(pi * Lanzamiento)
else:
    print(e * Lanzamiento) 

# Importar funciones como modulos
# Se importa una funcion especifica de un archivo aparte donde se encuentra la funcion
from C_4_1_2_Funciones import es_par

numero = int(input("Dime un numero y te dire si es par o no: "))
if es_par(numero):
    print("El numero es par!")
else:
    print("El numero es impar!")





