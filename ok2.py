#scrivere una funzione che dati due numeri interi resttituisca il maggiore

def nMaggiore (numero1,numero2):
    if numero1>numero2:
        return numero1
    else:
        return numero2
#scrivere una procedura che dato un numero intero stampi a video
#se è pari o dispari


def pd (numero1):
    if numero1%2==0:
        print("il numero è pari")
    else:
        print("il numero è dispari")
        

uno=input("inserire il primo numero")
uno=int(uno)
due=input("inserire il secondo numero")
due=int(due)

risultato= nMaggiore(uno,due)
print(risultato)
pd(risultato)
#dati due numeri interi stampi a video se il maggiore è pari o dispari