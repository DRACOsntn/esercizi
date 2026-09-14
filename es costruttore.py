class Atomo:
    def __init__ (self, massa, simbolo, numero_atomico):
        self.massa = massa
        if numero_atomico < 0:
            raise ValueError("il numero atomico deve essere positivo")
        else:
            self.numero_atomico = numero_atomico
        self.simbolo = simbolo
        self.numero_atomico = numero_atomico
    


idrogeno = Atomo(1.008, "H", 1)
try:
    ferro = Atomo(55.845, "Fe", 26)
except ValueError:
    print("il numero atomico deve essere positivo")
    

    