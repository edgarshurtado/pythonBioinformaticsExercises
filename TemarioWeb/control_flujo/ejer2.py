# Escribir un programa equivalente a wc que cuenta las líneas, las palabras y
# los caracteres

from sys import argv

src = open(argv[1])

palabras = 0
lineas = 0
caracteres = 0

for line in src:
    lineas += 1
    line = line.strip().split()
    palabras += len(line)
    for word in line:
        caracteres += len(word)
print(lineas, palabras, caracteres)