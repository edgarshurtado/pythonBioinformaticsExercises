from sys import argv

fhand = open(argv[1])
patrones = argv[2:]
lineNumber = 0

for line in fhand:
    line = line.strip()
    lineNumber += 1
    for patron in patrones:
        if patron in line:
            print(lineNumber, line)