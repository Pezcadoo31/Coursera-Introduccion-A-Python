# Modulo de conceptos de uso de funciones 

#Valor de retorno
def calculo (numero):
    resultado = (numero - 3) ** 3
    return resultado

print (calculo(8))
salida = calculo(5)
print (salida + 100)
print ()

# Funciones booleanas 
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

print (es_par(8))
print (es_par(7))
print()

# Función para obtener el maximo divisor 
def maximo_divisor(n):
    maximo_actual = 0
    i = 1
    while i < n:
        if n % i == 0:
            maximo_actual = i
        i += 1
    return maximo_actual

print (maximo_divisor(13))
print()

# Funcion para obtener la potencia de cierto numero 
def potencia_positiva(base, exponente):
    if exponente == 0:
        return
    else:
        resultado = 1
        while exponente > 0:
            resultado *= base
            exponente -= 1
        return resultado

print (potencia_positiva(2, 3))

