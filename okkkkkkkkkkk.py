#def sommaLista (lista):
    #somma = 0
    #for element in lista:
     #   somma = somma + element
    #print(somma)
    
##lista = [1,2,3,4]
#ommaLista(lista)
#lista2 = [2,3,4,5]
#sommaLista(lista2)

#scrivere una funzione che data una lista stampi a video il numero degli elementi pari


def nPari (lista):
    contatore = 0
    for element in lista:
        if element%2==0:
            contatore = contatore + 1
    print(contatore)
    
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
nPari(lista)



# scrivere una procedura che data una lista e un numero chiamato alfa stampi a video il
#numero degli elementi della lista piu granndi di alfa

def contaMaggioreAlfa(lista,alfa):
    contatore = 0
    for element in lista:
        if element  > alfa:
            contatore = contatore + 1
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
contaMaggioreAlfa(lista,alfa)


    