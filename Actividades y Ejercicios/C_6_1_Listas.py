# Modulo para aprender a trabajar con listas

# Escribir listas
no_olvidar = ["huevos", "aguacate", "lechuga","naranjas", 7000]
print(type(no_olvidar)) # Mostrara que es clase lista
print(no_olvidar, "\n") # Mostrara la lista completa

# Listas con variables y expresiones 
mesa = 5
producto = "exppresso"
cantidad = 5
costo = 500
pedido = [producto, mesa, cantidad, costo, cantidad*costo]
print(pedido, "\n")

# Listas con listas
un_pedido = ["expresso", 5, 2, 500, 1000]
otro_pedido = ["cortado", 8, 3, 800, 2400]
especial = ["cafe del dia", 10]
pedidos = [un_pedido, otro_pedido, especial]
print (pedidos, "\n")

# Listas vacias
lista1 = []
lista2 = list()
print(lista1)
print(lista2, "\n")

# Manipulacion de listas
# Acceder a posiciones dentro de la lista 
print(no_olvidar[2]) # Mostrara lo que se encuentre en el indice 2

# Acceder a secicones (slices) de la lista
print(no_olvidar[1:4], "\n") # Mostrara los elementos de la posicion 1 a la 4-1

# Listas con for 
for elem in no_olvidar:
    print("No olvidar ", elem)

# Modificando elementos de la lista
print()
no_olvidar [1] = "queso"
no_olvidar [3] = 1000
print(no_olvidar, "\n")

# Inserción y eliminación en listas 
# Concatenación y repetición de listas
cosas = ["piedra", "papel", "tijera"]   
tambien = ["apio", "tomates"]
print(cosas + tambien)
print(tambien * 2, "\n")

# Agregar un elemento al final de la lista 
no_olvidar.append("apio")
print(no_olvidar)
print(no_olvidar[-1], "\n") # Mostar el nuevo elemento en lista

# Agregar mas de un elemento al final de la lista
no_olvidar.extend(["tomates", "papas"])
print(no_olvidar)
print(no_olvidar[-2]) 
print(no_olvidar[-1], "\n") 

# Agregar un elemento en una posicion especifica
no_olvidar.insert(2, 5000)
print(no_olvidar)
print(no_olvidar[2], "\n")

# Eliminar el primer elemento de una lista 
print(no_olvidar)
comprado = no_olvidar.pop(0)
print (no_olvidar)
print ("Ya se ha comprado", comprado, "\n")

# Eliminar un elemento en especifico en una lista
print(no_olvidar)   
comprado = no_olvidar.remove("apio")
print(no_olvidar)
print("Ya se ha comprado", comprado, "\n")

# Funciones sobre listas
# Conocer la longitud de una lista 
no_olvidar = ["huevos", "aguacate", "lechuga","naranjas", 7000]
print(no_olvidar)
print("Hay", len(no_olvidar), "cosas por comprar")
no_olvidar.append("jamon")
print(no_olvidar)
print("Ahora hay", len(no_olvidar), "cosas por comprar", "\n")

# Saber si un elemento existe en una lista
print("Debo comprar vino?...", ("vino" in no_olvidar), "\n")  

# Conocer la posicion de un elemento en una lista
print("lechuga:", no_olvidar.index("lechuga"), "\n")

# Separar un string y formar una lista 
# Metodo 1 
texto = input("Escribe una lista de palabras separadas por coma: ")
print("Primero:", texto[0])
print("No. Lista:", texto)
lista = []
inicio = 0
for i in range(0, len(texto)):
    if texto[i] == ",":
        lista.append(texto[inicio:i])
        inicio = i + 1
lista.append(texto[inicio:])
print("Lista:", lista, "\n")

# Metodo 2 split(separador) 
texto = input("Escribe una lista de palabras separadas por coma: ")
lista = texto.split(",")
print("Lista:", lista, "\n")

# Ordenar elementos de una lista
no_olvidar = ["huevos", "aguacate", "lechuga","naranjas"]
print("Original:", no_olvidar)
no_olvidar.sort()
print("Ordenado:", no_olvidar, "\n")

precios = [5000, 1000, 2000, 3000]
print("Original:", precios)
precios.sort()
print("Ordenado:", precios, "\n")

comprar = [[100, "huevos"], [200, "aguacate"], [50, "lechuga"], [500, "naranjas"]]
print("Original:", comprar)
comprar.sort()
print("Ordenado:", comprar, "\n")

