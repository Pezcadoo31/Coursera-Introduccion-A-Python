# Modulo para aprender a utilizar if - elsif - else

# Programa que decide si debo llevar paragradas o no
llueve = input("¿Está lloviendo? (True/False) ")
if llueve == "True":
    print("Llevare paraguas")
else:
    print("No llevare paraguas")
print("Ahora saldre a la calle")
print()

# Conjdición mas compleja 
llueve = input("¿Está lloviendo? (True/False) ")
Temperatrura = int(input("¿Cual es la temperatura el dia de hoy? "))
if llueve == "True" and Temperatrura < 20:
    print("Llevare paraguas y abrigo")
else:
    print("No necesito el paraguas o abrigo")
print("Ahora saldre a la calle")
print()

# Omitir else 
print("Comienza la caminata!")
Charco  = input("¿Hay charcos en la calle? (True/False) ")
if Charco == "True":
    print("A saltar!")
print("Fin de la caminata")
print()

# Usando if/else anidados
Lluvia = input("¿Está lloviendo? (True/False) ")
Temperatrura = int(input("¿Cual es la temperatura el dia de hoy? "))
if Temperatrura < 18:
    if Lluvia == "True":
        print("Llevare paraguas y abrigo")
    else:
        print("Solo llevare abrigo")
else:
    print("No necesito el paraguas o abrigo")
print("Ahora saldre a la calle")
print()

# Usando elif
Lluvia = input("¿Está lloviendo? (True/False) ")
Temperatrura = int(input("¿Cual es la temperatura el dia de hoy? "))
if Temperatrura < 18 and Lluvia == "True":
    print("Llevare paraguas y abrigo")
elif Temperatrura < 18 and Lluvia == "False":
    print("Solo llevare abrigo")
else:
    print("No necesito el paraguas o abrigo")
print("Ahora saldre a la calle")
print()

# Reordenando las condiciones descartando casos innecesarios
Lluvia = input("¿Está lloviendo? (True/False) ")
Temperatrura = int(input("¿Cual es la temperatura el dia de hoy? "))
if Temperatrura >= 18:
    print("No llevare paraguas ni abrigo")
elif Lluvia == "True":
    print("Llevare paraguas y abrigo")
else:
    print("Solo llevare abrigo")
print("Ahora saldre a la calle")
print()


