# si vuole creare un programma che leggendo da un file di testo contenente una serie di valori
# misurati di temperatura, calcoli la media, varianza e la mediana della distribuzione.

# sottoproblemi: 1) leggere il file riga per riga e creare una lista
#                2) calcolo della media della lista
#                3) calcola la varianza di una lista
#                4) calcola la mediana di una lista

def leggiFile (pathInput):
    temperature = []
    with open (pathInput) as f:
        for line in f:
            #temperature.append(int(line.strip()))
            elemento= int(line.strip())
            temperature.append(elemento)
    return(temperature)


lista = leggiFile("temperature.csv")
            
    