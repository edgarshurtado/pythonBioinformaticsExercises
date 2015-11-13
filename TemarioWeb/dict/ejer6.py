from sys import argv

fhand = open(argv[1])

next(fhand)

tomates = {}
for line in fhand:
    line = line.strip().split()
    colorTomate = line[1]
    nTomates = int(line[2])
    if colorTomate in tomates:
        tomates[colorTomate] += nTomates
    else:
        tomates[colorTomate] = nTomates

print(tomates)

