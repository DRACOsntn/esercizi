class CampioneDNA:
    def __init__(self, codice_campione, sequenza, laboratorio, geni_mappati=None, mutazioni_rilevate=None):
        # si usa .upper() per convertire subito la sequenza in maiuscolo
        self.__codice_campione = codice_campione
        self.__sequenza = sequenza.upper()
        self.laboratorio = laboratorio
        
        if geni_mappati is None:
            self.__geni_mappati = []
        else:
            self.__geni_mappati = geni_mappati
        
        if mutazioni_rilevate is None:
            self.__mutazioni_rilevate = {}
        else:
            self.__mutazioni_rilevate = mutazioni_rilevate
   
    def aggiungi_gene(self, nome_gene):
        gia_presente = False
        for i in self.__geni_mappati:
            if i == nome_gene:
                gia_presente = True
        
        if gia_presente == False:
            self.__geni_mappati.append(nome_gene)
   
    def registra_mutazione(self, posizione, tipo_mutazione):
        self.__mutazioni_rilevate[posizione] = tipo_mutazione
    
    def calcola_percentuale_gc(self):
       conteggio_GC = 0
       lunghezza_totale = 0
       for lettera in self.__sequenza:
            lunghezza_totale = lunghezza_totale + 1
            if lettera == 'G' or lettera == 'C':
                conteggio_GC = conteggio_GC + 1
            if lunghezza_totale > 0:
                percentuale = (conteggio_GC / lunghezza_totale) * 100
            else:
                percentuale = 0.0
            return percentuale
    
    
    def stampa_report(self):
        seq_breve = ""
        contatore = 0
        for lettera in self.__sequenza:
            if contatore < 20:
                seq_breve = seq_breve + lettera
                contatore = contatore + 1
        if contatore == 20:
            seq_breve = seq_breve + "la sequenza è stata abbreviata"
       
        print("Codice:", self.__codice_campione)
        print("Laboratorio:", self.laboratorio)
        print("Sequenza:", seq_breve)
        print("Percentuale GC:", self.calcola_percentuale_gc(), "%")
        print("Geni mappati:", self.__geni_mappati)
        print("Mutazioni:", self.__mutazioni_rilevate)
    

#chiamate
campione = CampioneDNA("DNA-4029", "atcggctagctagc", "LabGen-BioApp", ["geneA"])
campione.aggiungi_gene("ampR")
campione.aggiungi_gene("geneA")  # Non viene aggiunto perché già presente
campione.registra_mutazione(5, "sostituzione")
campione.stampa_report()