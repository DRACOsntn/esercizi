#scrivere un programma che calcoli il minimo e il massimo di una lista
#di numeri interi random compresi nell'intervallo 0,100

#sottoproblemi: 1) calcolare il minimo di una lista
#               2) calcolare il massimo di una lista
#               3) generare una lista di n numeri random nell'intervallo 0,100

def generaLista(n):
    myList=[]
    for i in range (0,n):
        elemento= random.randint (0,100)
        myList.append(elemento)
    return(myList)