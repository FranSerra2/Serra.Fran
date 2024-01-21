# -*- coding: utf-8 -*-


import math
#cambiar el nombre funciona dentro del while, separa los numeros binarios
temporal = []
#tiene los resultados de las potencias
resultados = []
binario = raw_input("n\Ingrese un binario: ")
binario = str(binario)
cantidad = len(binario)
copia = binario
copia = int(copia)
i = 1
li = 10**(cantidad-i)
while i <= cantidad:
    num = math.floor(copia/li)
    num = int(num)
    temporal.append(num)
    i = i + 1
    copia = (copia%li)*10
i = 1
for num in temporal:
    potencia = num * 2**(cantidad-i)
    resultados.append(potencia)
    i = i + 1
suma = 0
for potencia in resultados:
    suma = suma + potencia
print suma