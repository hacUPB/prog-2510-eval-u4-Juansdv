Al iniciar el programa se le mostrará un menú principal en el que tendrá 4 opciones.
1.	Archivos
2.	Procesar archivo .txt
3.	Procesar archivo .csv
4.	Salir

Para el submenú 1. Archivos:
Se le mostrará otro submenú en el que el programa le da la ruta actual y luego le pregunta si quiere ver los archivos en la ruta en la que está o, por el contrario, cambiarla. También hay una tercera opción para volver al menú principal.
Si desea ver los archivos en la ruta actual el programa le mostrará todos los archivos que haya en esa ruta.
Si desea cambiar la ruta el programa le pedirá la nueva ruta (Se recomienda meterla con C:\ Incluida. Como detalle adicional, Si le dio por error a cambiar la ruta, el programa le permite volver al menú principal escribiendo “-1” en la consola. Una vez cambiada la ruta, el programa le mostrará los archivos en esa nueva ruta.

Para el submenú 2. Procesar archivo .txt:
Se le mostrará otro submenú en el que el programa le dice que se analizara el archivo que finaliza con la extensión “.txt”.
Se le pedirá una opción dentro de las siguientes:
•	Contar el número de palabras: El programa analizará el archivo que se le mostró al usuario anteriormente y le dará los datos de las palabras, la cantidad de caracteres sin espacio y la cantidad de caracteres con espacio.

•	Reemplazar una palabra: El programa analizará el archivo que se le mostró al usuario anteriormente y se le mostrará el texto. Luego de esto se le pide al usuario la palabra que desea reemplazar. En caso de que haya varias palabras repetidas, el programa le mostrara en el texto las palabras resaltadas y tendrá que elegir una de ellas para reemplazar. Luego de esto se le pedirá que ingrese la nueva palabra y por ultimo se le mostrará el texto con la palabra cambiada.
Como detalles adicionales si la palabra no existe en el texto, se le pedirá ingresar la palabra nuevamente.

•	Ver histograma: se le mostrará al usuario el histograma de las vocales en el texto. A su vez, también la cantidad de cada una de las vocales en el texto.

Para el submenú 3. Procesar archivo .csv:
Se le mostrará otro submenú en el que se le pide al usuario digitar una opción dentro de las siguientes:

•	Mostrar primeras 15 filas: Se le mostrara al usuario las 15 primeras filas del archivo .csv.

•	Calcular estadísticas: Se le mostrará al usuario otro submenú en el que tendrá que decidir sobre que columna calcular las estadísticas.
Como detalles: 
Si la columna no contiene datos numéricos se le pedirá al usuario ingresar una nueva columna.
Si el usuario digita un índice diferente a los que se les muestra en pantalla se le pedirá ingresar nuevamente un nuevo índice.
Finalmente, cuando seleccione una columna con datos numéricos, se le mostrara en pantalla los datos estadísticos de la columna que haya escogido.

•	Graficar columna: Nuevamente se le pedirá al usuario ingresar una columna que contenga datos numéricos y se graficara.
