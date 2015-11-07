from sys import argv

print("Estamos ejecutando el script", argv[0])

argumento = argv[1]

fichero_leido = []
fichero = open(argumento)

for line in fichero:
    line = line.strip().split()
    fichero_leido.append(line)

print(fichero_leido)