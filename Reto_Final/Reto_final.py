import os
import csv
import matplotlib.pyplot as plt


### Menú

def menu():

    while True:
        elegir = str(input("\nMENÚ PRINCIPAL\nElija una opción:\n1. Archivos\n2. Procesar archivo .txt\n3. Procesar archivo .csv\n4. Salir\n")).capitalize()

        match elegir:
            case "1":
                archivos()
            case "2":
                submenu_txt()
            case "3":
                break
            case "4":
                break
            case _:
                break



### Archivos:
## Submenu archivos

def archivos():
    while True:
        print(f"\nRuta actual: {os.getcwd()}")
        ver_a = str(input("Desea ver los archivos en la ruta actual?\n1. Si\n2. No, quiero cambiar la ruta.\n3. Volver al menú principal\n")).capitalize()

        match ver_a:
            case "1":
                ver_archivos()
                break
            case "2":
                cambiar_ruta()
                break
            case "3":
                break     
            case _:
                print("\nUn error ha ocurrido. Intentelo nuevamente.")
        break
    
### Archivos:
## Ver Archivos

def ver_archivos():
    print(f"Los archivos en la ruta actual son:\n")
    lista_archivos = os.listdir()
    for archivo in lista_archivos:
        print(archivo)

### Archivos:
## Cambiar la ruta

def cambiar_ruta():
    while True:
        try:
            print("\nPara cancelar, escriba -1.")
            cambio = str(input("Ingrese la ruta a la que quiere cambiar:\n"))
            if cambio == "-1":
                break
            print(f"Se ha cambiado de ruta exitosamente.\n{os.chdir(cambio)}")
            lista_archivos = os.listdir()
            print(f"Los archivos en esta nueva ruta son:\n ")
            for archivo in lista_archivos:
                print(archivo)
        except FileNotFoundError:
            print("Ha ocurrido un error. Intentelo nuevamente.")


### Texto:
### Submenu archivo .txt

def submenu_txt():

    a = [f for f in os.listdir(os.getcwd()) if f.endswith('.txt')]
    print(f"Se analizara el siguiente archivo: {a}")
    opcion = str(input("\nSubmenu de archivo txt\nElija una opción:\n1. Contar número de palabras y caracteres\n2. Reemplazar palabra\n3. Ver histograma\n4. Volver\n"))
    while True:
        match opcion:
            case "1":
                contar_p()
                break
            case "2":
                remplazar_p()
                break
            case "3":
                histograma_txt()
                break
            case "4":
                break
            case _:
                print("Ha ocurrido un error. Intente nuevamente.")


## Contar palabras

def contar_p():
    abrir = open("archivo_texto.txt", "r")
    num = abrir.read()
    palabras = len(num.split()) 
    caracteres_con_espacio = len(num.strip()) - num.count("\n") 
    caracteres_sin_espacio = caracteres_con_espacio - num.count(" ")



    print(f"El número de palabrás en el archivo es de: {palabras}")
    print(f"La cantidad de caracteres sin espacio es de: {caracteres_sin_espacio}")
    print(f"la cantidad de caracteres con espacio es de: {caracteres_con_espacio}")

    abrir.close()

### Texto:
## Remplazar palabra

def remplazar_p():
    abrir = open("archivo_texto.txt", "r+", encoding="utf-8")
    texto = abrir.read()
    cambiar = texto.maketrans({".":" ", ",":" "})
    convertir = texto.translate(cambiar)
    lista = list(convertir.split())
    print(f"El texto es:\n{texto}")

    while True:
        palabra = str(input("\nIngrese la palabra que quiere reemplazar (Incluya la mayuscula si es el caso):\n"))
        num_palabras = convertir.split().count(palabra)
        

        if num_palabras > 1:
            contador = 1
            for i, p in enumerate(lista):
                if p == palabra:
                    lista[i] = f"{contador}. {palabra.upper()}"
                    contador += 1
            print()
            print(" ".join(lista))
            print(f"\nHay {num_palabras} palabras que coinciden, porfavor seleccione cual desea cambiar")
            print("Arriba se le han resaltado las palabras en el texto. luego digite el número correspondiente a la palabra.\n")


            while True:   
                try:
                    for i in range(num_palabras):  
                        print(f"{i+1}. {palabra}")
                    eleccion = int(input("Porfavor elija una opción:\n"))
                    if eleccion > num_palabras:
                        print("Indice no existe. Vuelva a intentarlo.")
                    indice = lista.index(f"{str(eleccion)}. {palabra.upper()}")
                    break
                except ValueError:
                    print("\nTipo de dato incorrecto. Intentelo nuevamente.")

            
            abrir = open("archivo_texto.txt", "w+")
            reemplazar = str(input("\nIngrese la nueva palabra:\n"))
            cadena = convertir.split()
            cadena.remove(palabra)
            cadena.insert(indice,reemplazar)
            texto_cambiado = " ".join(cadena)
            abrir.write(texto_cambiado)
            abrir.seek(0)
            print(f"La palabra se ha cambiado exitosamente:\n {texto_cambiado}")
            abrir.close()

            break

        elif num_palabras == 1:
            abrir = open("archivo_texto.txt", "w+")
            reemplazar = str(input("\nIngrese la palabra:\n"))
            texto_cambiado = texto.replace(palabra,reemplazar)
            abrir.write(texto_cambiado)
            abrir.seek(0)
            print(f"La palabra se ha cambiado exitosamente:\n {texto_cambiado}")
            abrir.close()
            break

        elif num_palabras == 0:
            print("\nNo se han encontrado palabras. Porfavor vuelva a intentarlo.")

    abrir.close()


### Texto:
## Histograma .txt

def histograma_txt():
    abrir = open("archivo_texto.txt", "r")
    letras = abrir.read()

    letra_a = letras.count("a")
    letra_e = letras.count("e")
    letra_i = letras.count("i")
    letra_o = letras.count("o")
    letra_u = letras.count("u")

    print(f"Número de A: {letra_a}")
    print(f"Número de E: {letra_e}")
    print(f"Número de I: {letra_i}")
    print(f"Número de O: {letra_o}")
    print(f"Número de U: {letra_u}")
    data = [letra_a,letra_e,letra_i,letra_o,letra_u]

    plt.hist(data, bins=15, edgecolor='black')
    plt.title('Vocales')
    plt.xlabel('Valores')
    plt.ylabel('Frecuencia')
    plt.show()

    abrir.close()




### CSV
## Submenu archivo .csv

def submenu_csv():
    pass



#### Ejecutar funciones

def main():
    menu()
    
if __name__ == "__main__":
    main()
~

