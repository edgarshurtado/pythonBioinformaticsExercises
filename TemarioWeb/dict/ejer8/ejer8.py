from sys import argv

files = argv[1:]
files = map(open, files)

experimentsSets = []

for experiment in files:
    expSet = set()
    for line in experiment:
        line = line.strip()
        expSet.add(line)
    experimentsSets.append(expSet)

print("Los dos sets:")
print(experimentsSets[0])
print(experimentsSets[1])
print("Sólo en experimento 1")
print(experimentsSets[0].difference(experimentsSets[1]))
print("Sólo en experimento 2")
print(experimentsSets[1].difference(experimentsSets[0]))
print("Comunes a los 2 experimentos")
print(experimentsSets[1].intersection(experimentsSets[0]))
