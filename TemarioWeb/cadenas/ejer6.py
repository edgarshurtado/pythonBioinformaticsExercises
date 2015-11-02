'''
Supongamos que quisiésemos imprimir una tabla y que deseamos imprimir el nombre de las muestras (muestra1) y la media de una medida asociada (4.2) dejando 20 espacios para el nombre y 10 para la media y separándolas con un tabulador ¿cómo lo harías?
'''

def lineaTabla(nombre, valor):
  result_line = ""
  result_line += nombre.center(20)
  result_line += "\t"
  result_line += str(valor).center(10)

  return result_line
