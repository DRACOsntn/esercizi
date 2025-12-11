#dati 4 numeri g interi generati random creare una tupla che contenga
#il maggiore dei primi due e il minore dei secondi due.

#sottoproblemi: trovare il maggiore di due numeri
#               trovare il minore di due numeri

def nMaggiore (numero1,numero2):
    if numero1>numero2:
        return numero1
    else:
        return numero2

def nMinore(numero3,numero4):
    if numero3<numero4:
        return numero3
    else:
        return numero4



uno=input("inserire il primo numero")
uno=int(uno)
due=input("inserire il secondo numero")
due=int(due)
tre=input("inserire il terzo numero")
tre=int(tre)
quattro=input("inserire il quarto numero")
quattro=int(quattro)

risultato= nMaggiore(uno,due)
risultato2= nMinore(tre,quattro)
print(risultato)
print(risultato2)

risultato=(1,2,3,4)