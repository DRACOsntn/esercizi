class Atomo:
    def __init__ (self, massa, simbolo, numero_atomico):
        #simbolo, numero_atomico e massa sono attributi pubblici
        self.massa = massa                                                           #pubblico (public), posso accedere agli attributi della classe
        if numero_atomico < 0:
            raise ValueError("il numero atomico deve essere positivo")               #dall'esterno
        else:
            self.numero_atomico = numero_atomico
        self.simbolo = simbolo
        #orbitale è n attributo privato
        self.__orbitale = "2p" 
        
    def nuovaMassa(self):
        self.massa = float ( input ( " inserisci il valore della massa: " ))
        
    def nuovoOrbitale(self):
        self.__orbitale= input("Inserisci il valore: ")
        
        
        
    def stabile(self):
        neutroni=round(self.massa) - self.numero_atomico
        rapporto=neutroni/self.numero_atomico
        if rapporto>= 9.9 and rapporto<=1.6:
            return True
        else:
            return False
        
    def printorbitale(self):
        print(self.__orbitale)
    
    def print_tutto(self):
        print(self.__orbitale)
        print(self.massa)
    
        
    
idrogeno = Atomo(1.008, "H", 1)
idrogeno.stabile()
#per accedere dall'esterno ad un attributo pubblico basta usare la sintassi della riga successiva
print(idrogeno.simbolo)
#per accedere dall'esterno ad un attributo privato necessariamente devo implementare un metodo
idrogeno.print_tutto()

try:
    ferro = Atomo(55.845, "Fe", 26)
except ValueError:
    print("il numero atomico deve essere positivo")
    

    