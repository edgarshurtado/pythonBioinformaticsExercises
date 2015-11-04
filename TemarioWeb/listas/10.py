'''
File: 10.py
Author: Me
Description: Crea una lista con los números del 0 al 9 y extrae los pares, los impares, 
los 5 primeros y los 5 últimos por separado.
'''
lista = list(range(10))

#numeros pares
print(lista[0::2])

#numeros impares
print(lista[1::2])

#5 primeros números
print(lista[:5])
print(lista[5:])
