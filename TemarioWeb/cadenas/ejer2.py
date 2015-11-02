'''
A partir de un fichero de texto hemos leído la cadena
‘ paciente,nombre,apellido \n’.

¿Cómo podemos eliminar el retorno de carro y los espacios del principio y el
final de la línea?
'''

texto = " paciente,nombre,apellido \n"

#Eliminamos los espacios en blanco a ambos lados de la cadena y el \n
texto = texto.strip()

#Imprimimos resultados
print(texto)