1. - Escribir un script que tome una serie de numeros y/o palabras separados por espacios de la linea de comandos, y ofrezca como resultado por pantalla la media de los numeros, en una linea, y las palabras introducidas, separadas por comas, en otra.

2. - Escribir un script como el del ejercicio anterior, pero en el que los numeros y/o letras que se introducen en la linea de comandos estan separados por comas.

3. - Escribir un script que tome dos numeros separados por espacios de la linea de comandos, y ofrezca como resultado por pantalla su minimo comun multiplo.

4. - Escribir un script que tome dos numeros separados por espacios de la linea de comandos, y ofrezca como resultado por pantalla su maximo comun divisor.

5. - Escribir un script que tome como primer parametro en la linea de comandos un numero entero, y como segundo una 'C' o una 'F', y ofrezca como resultado por pantalla la conversion de grados Celsius a grados Farenheit o viceversa.

6. - Escribir un script que tome como primer parametro en la linea de comandos la ruta de un fichero, y ofrezca como resultado por pantalla si dicho fichero esta en formato FASTA, FASTQ u otro.

7. - Escribir un script que tome como primer parametro en la linea de comandos una cadena de texto, y como segundo parametro un numero entero, y genere tantos ficheros distintos como indique el valor del segundo parametro, cuyos nombres contengan el texto del primer parametro y un numero desde el 1 hasta el valor indicado en el segundo parametro.

8. - Escribir un script que tome como primer parametro en la linea de comandos la ruta de un fichero en formato FASTA, y genere un fichero en formato FASTA para cada una de las secuencias que hay en dicho fichero input.

9. - Escribir un script que tome como primer parametro en la linea de comandos la ruta de un fichero de genes en formato FASTA, y lo divida en ficheros FASTA de 10 secuencias.

10. - Escribir un script que tome como primer parametro en la linea de comandos la ruta de un fichero en formato FASTA, y genere un fichero para cada una de las longitudes de las secuencias que hay en dicho fichero, donde en cada uno de dichos ficheros haya una lista de los nombres de las secuencias que tienen dicho tamaÃ±o (un nombre por linea).

11. - Escribir un script que tome como parametros en la linea de comandos la ruta de dos ficheros que contienen listas de nombres de genes (un nombre por linea), y ofrezca como resultado tres ficheros: uno con los nombres de los genes comunes a ambos ficheros, otro con los nombres de los genes especificos del primer fichero, y otro con los nombres de los genes especificos del segundo fichero.

12. - Escribir un script que tome como primer parametro en la linea de comandos la ruta de un fichero de texto delimitado por tabuladores que contiene lineas con valores numericos, como segundo parametro un numero entero, y como tercer parametro un numero con decimales, y ofrezca como resultado un fichero con las lineas del fichero input en las que el valor numerico del campo situado en la posicion indicada por el segundo parametro sea mayor al valor indicado en el tercer parametro.

13. - Escribir un script que tome como primer parametro en la linea de comandos la ruta de un fichero de genes en formato FASTA, y genere un fichero FASTA de secuencias no repetidas, indicando en la linea 'header' los nombres de las genes que tienen cada una de dichas secuencias.

14. - Escribir un script que tome como parametros en la linea de comandos las rutas de un numero de ficheros de genes en formato FASTA, y genere como resultado un fichero FASTA con las secuencias de todos los genes que aparecen al menos tres veces en el conjunto de ficheros input.

15. - Escribir un script que tome como parametros en la linea de comandos la ruta de dos ficheros de texto delimitado por comas, y genere un fichero delimitado por tabuladores con la informacion combinada de ambos ficheros usando como identificador para combinar en la misma linea el texto del primer campo en ambos ficheros. Ejemplo:

- input 1:
gen1,transporte,ATGG,5.5
gen2,oxidacion,CGTT,4.5

- input 2:
gen1,mitocondria,467
gen3,nucleo,558

- output:
gen1(tab)transporte(tab)ATGG(tab)5.5(tab)mitocondria(tab)467
gen2(tab)oxidacion(tab)CGTT(tab)4.5(tab)(tab)     
gen3(tab)(tab)(tab)(tab)nucleo(tab)558

