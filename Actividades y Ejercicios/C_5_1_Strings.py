# Modulo para aprender sonbre strings

# En pyrhon un str puede representarse entre comillas simples o dobles
print("Con Comillas Dobles")
print('Con Comillas Simples')
print()

# Podemos concatenar strings con el operador +
print("Hola" + " Gente")
print()

string1 = "La casa"
string2 = " es morada"
string3 = string1 + string2
print(string3)
print()

# Manipulacion de strings, acceso mediante indices
print("Martes" [0])
print("Martes" [5])
# -1 es el ultimo caracter
print("Martes" [-1])
# Intervalos de indices
print("Martes" [1:4])
print()

a = "La casa es de vegetta 777"
print(a[5])
print()

# Salto de linea en strings
print("Un parrafo. \nOtro parrado.")
print() 

# Mostrar \ en un string
print("Para escribit un backslash se usa \\")
print() 

# Obtener la longitud de un string
print(len("Martes"))
print(len("Yo soy."))
print()

# Conversion a mayusculas y minusculas
print("Martes".upper())
print("maRTES".lower()) 
print()

# Remover caracter ubicado en una orilla 
a = "Bien. Martes a las 5."
print(a.strip("."))
print()

# Reemplazar caracteres
a = "Hola !1!"
print(a.replace("1", "!"))
print()

