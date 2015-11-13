from sys import argv

fhand = open(argv[1])

next(fhand)

tomates = {}
for line in fhand:
    line = line.strip().split()
    nombreTomate, colorTomate, nTomates = line
    nTomates = int(nTomates)
    tomates[nombreTomate] = ([colorTomate, nTomates])

print(tomates)
