#programma che gestisce nome, cognome, eta di due persone

nome_prima = "tommaso"
cognome_prima = "STRA"
eta_prima = 25

nome_seconda = "luigi"
cognome_seconda = "rossi"
eta_seconda = 28

print("età prima persona")
print(eta_prima)
print("età seconda persona")
print(eta_seconda)

#uso degli oggetti

class Persona:
    def __init__(self,nome,cognome,eta,lavoro):            #costruttore
        self.nome = ""
        self.cognome = ""
        self.eta = eta
        self.lavoro = lavoro
    def stampaEta(self):
        print(self.eta)
    def stampaLavoro(self):
        print(self.lavoro)
    def etaSus(self):
        if self.eta >=18:
            print(self.nome)
            print("maggiorenne")
        else:
            print(self.nome)
            print("minorenne")
        
prima_persona = Persona("tommaso","STRA",15,"sbirro")
seconda_persona = Persona("luigi","rossi",28,"pilota")
prima_persona.stampaEta()
seconda_persona.stampaEta()
prima_persona.stampaLavoro()
seconda_persona.stampaLavoro()
prima_persona.etaSus()
seconda_persona.etaSus()