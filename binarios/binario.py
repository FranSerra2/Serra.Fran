# -*- coding: utf-8 -*-

#Funcion que convierte el numero ingresado a binario
def conversor_binario(num):
    resultado = num
    binario = ""
    while resultado > 0:
        resto = resultado % 2
        resto = str(resto)
        binario = resto + binario
        resultado = resultado / 2
    return binario 
    
num = raw_input("n\Ingrese un numero: ")
num = int(num)
binario = conversor_binario(num)
print binario
