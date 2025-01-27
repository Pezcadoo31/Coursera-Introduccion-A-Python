# Aprender a usar PRINT en Python
# Calcular el precio gastado en un estacionamiento e imprimirlo en pantalla 
Pesos_por_hora = 200
Llegada = 20
Salida = 22
Precio = (Salida - Llegada) * Pesos_por_hora
print("El precio a pagar es de: ", Precio)

# Imprimir expresiones 
print((3+5//4-2 )-2**4+3*(7-2))

# Imprimir variables calculadas previamente 
Fahrenheit = 91
Celcius = (Fahrenheit - 32) * 5/9
print(Celcius)

#Imprimir expresiones con variables 
temperatura = 33
print(temperatura >= 30)

# Imprimir multiples expresiones 
Episodio = 3
print("Episodio", Episodio, "del libro")

# Cambiar el termino de linea 
Nombre = "Christian" 
Edad = 38
print("Soy", Nombre, end=" ")
print("y tengo", Edad, "años")
print("cumplidos ")

#Cambiar el separador de expresiones 
print("El tesoro", "esta", "en", "la", "isla", "del", "coco", sep=" --- ")






