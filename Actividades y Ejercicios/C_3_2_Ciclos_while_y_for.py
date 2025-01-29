# Modulo para comprender el flujo ciclico de un programa

# Ciclo while convirtiendo fahrenheit a celcius
Tempertura = 32
print("Fahrenheit°  Celcius °")
while Tempertura < 73:
    print(Tempertura, "°", "        ", int((Tempertura - 32) * 5/9), "°")
    Tempertura += 1
print()

# Ciclo for para convertir fahrenheit a celcius
print("Fahrenheit°  Celcius °")
for Tempertura in range(21):
    print(Tempertura, "°", "        ", int((Tempertura - 32) * 5/9), "°")
print()

# Comparacion de ambos ciclos
# Ciclo while
print("Ciclo while") 
i = 1
while i < 100:
    if i < 18:
        print(i, "es menor que 18")
    else:
        print(i, "es mayor que 18")
    i += 1
print()

# Ciclo for
print("Ciclo for")
for i in range(1, 100):
    if i < 18:
        print(i, "es menor que 18")
    else:
        print(i, "es mayor que 18")
print()
