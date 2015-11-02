'''
En la secuencia "ATG CTA TGA" ¿cómo obtenemos los tres primeros nucleótidos? ¿Los tres últimos? ¿El primero de cada codón? ¿El segundo de cada codón?
'''

def prepararString(string):
  string = string.replace(' ','')
  string = string.lower()
  return string

adn =" ATG CTA TGA"
adn = prepararString(adn)

print("Cadena adn: ", adn)

print("Los 3 primeros nucleótidos")
print(adn[0:3])

print("El primero de cada codón")
print(adn[::3])

print("El segundo de cada codón")
print(adn[1::3])
