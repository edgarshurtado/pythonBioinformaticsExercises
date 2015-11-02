'''
1. Separa la lista ['id_paciente', 'fase1', '37.1', '39.3', '38.1'] en tres variables: id_paciente, fase_ensayo, serie_temperaturas.

2. Convierte los números (que están representados por cadenas de texto) de la serie de temperaturas anterior en números con coma flotante.

3. añade  a la lista de números una nueva temperatura, 37.2.

4. Añade a las temperaturas la lista: [36.5, 37.3].
'''

lista = ['id_paciente', 'fase1', '37.1', '39.3', '38.1']

id_paciente = lista[0]
fase_ensayo = lista[1]
serie_temperaturas = lista[2:]

print("Lista original", serie_temperaturas)

#Convertir en float
serie_temperaturas = list(map(float, serie_temperaturas))
print("convertir nums en float", serie_temperaturas)
  #map devuelve un iterable, por lo que uso el constructor list
  #para crear la lista resultado

#Añade una nueva temperatura
serie_temperaturas.append(37.2)
print("Añadir una nueva temp", serie_temperaturas)

#Añade lista
serie_temperaturas.extend([36.5, 37.3])
print("Añadir una lista entera", serie_temperaturas)

#Cantidad de temperaturas
print("Nº de temperaturas", len(serie_temperaturas))

#Imprimir la lista con comas
print(", ".join(map(str,serie_temperaturas)))
