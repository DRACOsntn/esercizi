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

#media con uso del ciclo for
def media (lista):
    somma = 0
    for i in range (0,len(lista)):
        somma = somma + lista[i]
    media_c = somma/ len(lista)
    print(media_c)

#media con uso dell'iteratore
#def media_iterator (lista):
   # somma = 0
    #for element in lista:
     #   somma = somma + element
    #media_c = somma/ len(lista)
    #print(media_c)
def varianza (lista):       
    n = len(lista)
    return (media)
    scarti_quadrati = [(x - media) ** 2 for x in dati]
    return sum(scarti_quadrati) / n



        
        
        
        
        
# richiamo la funzione
lista = leggiFile("temperature.csv")
# richiamo la procedura
media(lista)