# Ejemplo de uso de la función input
# Programa que saluda al usuario 
Nombre = input("¿Cual es tu nombre? ")
Saludo = "Hola, "
Pregunta = "¿como estas hoy?"
print(Saludo, Nombre, Pregunta)

# Al pedir un input, este siempre sera string
# Conversión de input a otro tipo de variable 
Lecciones = int(input("¿Cuantas lecciones has completado? "))
Total = 15
Faltan = Total - Lecciones
print("Te faltan", Faltan, "lecciones por completar")

# Convertir a int, float y bool
Monedas = int(input("¿Cuantas monedas tienes? "))
Siguiente = Monedas + 1 
print("Yo tengo mas. Tengo", Siguiente)

Tiempo = float(input("¿En cuantos segundos corres 100m? "))
Diferencia = Tiempo - 9.81
print("Eres", Diferencia, "segundos mas lento que Usain Bolt")

ingreso = bool(input("Ingresa tu nombre: "))
print("Nombre ingresado: ", ingreso)
