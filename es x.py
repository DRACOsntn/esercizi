# #data una lista di eventi ciascuno con una probabilità
# di accadimento, contare il numero di eventi con probabilità
#maggiore di 75% oppure con una probabilità scelta dall'utente

#sottoproblemi: 1) contare data una lista gli elementi sopra il 75% oppure sopra soglia
#               2) gemerare una lista di eventi ciascun elemento con range (0,100) oppure (0,1)



import random
def generaLista (n):
    myList=[]
    for i in range (0,n):
        elemento= random.randint (0,100)
        myList.append(elemento)
    return(myList)

def maggioreLista (lista, soglia=75):
    contatore=0
    for i in range (0,len(lista)):
        if lista[i]>soglia:
            contatore= contatore + 1
    print(contatore)
    








