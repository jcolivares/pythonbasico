#!/usr/bin/python

#Manejo de funciones en python

def cuadrado(x):
	return x*x

numero = input("Dame un numero?")

numero = int(numero)

res= cuadrado(numero)

print("El valor es:", res)

lista = [1, 2, 3, 5, 7, 9]

for i, elemento in enumerate(lista):
	print("Elemento ", i, " en lista =", elemento, "su cuadro =", cuadrado(elemento))

cuadrados = [cuadrado(x) for x in lista]

print(cuadrados)	