# Leer un fichero que contiene una lista de palabras y guardar las palabras en
# una lista

from sys import argv

src = open(argv[1])

palabras = []

for line in src:
    line = line.strip().split()
    palabras.extend(line)

print(palabras)