'''
Guarda la cadena de texto “ACT TGA CTA” en la variable adn y cuenta cuantos
nucleótidos de cada tipo tiene.

Convierte la cadena anterior a minúsculas y elimina los espacios.

5. ¿Cuántos nucleótidos tiene la cadena de texto anterior?
'''
#Preparación de las cadenas de adn
adn = "ACT TGA CTA".lower()
adn = adn.replace(" ", "")

count_nucleotidos = {"A":0, "T":0, "C":0, "G":0}

#Conteo de nucleótidos
count_nucleotidos["A"] = adn.count('a')
count_nucleotidos["T"] = adn.count('t')
count_nucleotidos["G"] = adn.count('g')
count_nucleotidos["C"] = adn.count('c')

print("Nucleótidos: ", count_nucleotidos)
print ("Total nucleótidos: ", len(adn))