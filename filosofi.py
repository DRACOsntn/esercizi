class Filosofo:
    def __init__(self, nome, anno):
        self.nome = nome
        self.anno = anno
    def caratteristiche(self):
        car=(str("inserisci caratteristiche del filosofo"))
        print(car)
        
    def stampa(self):
        print("Il nome del filosofo è:", self.nome)
        print("L'anno di nascita del filosofo è:", self.anno) 


class ScuolaFilosofica:
    def __init__(self, nome, fondatore, epoca):
        self.nome = nome
        self.fondatore = fondatore
        self.epoca = epoca
        self._filosofi = []
        
    def descrivi(self):
        return ("La scuola filosofica è " + self.nome +", fondata da " + self.fondatore +", nell'epoca " + self.epoca )

    def aggiungiFilosofo(self, filosofo):
        self._filosofi.append(filosofo)

    def stampaFilosofi(self):
        print("Filosofi della scuola:", self.nome)
        for filosofo in self._filosofi:
            filosofo.stampa()


class Stoicismo(ScuolaFilosofica):
    def __init__(self, nome, fondatore, epoca, virtu):
        super().__init__(nome, fondatore, epoca)
        self.virtu = virtu

    def descrivi(self):
        return (super().descrivi()+" La virtù principale è: " + self.virtu)


class Epicureismo(ScuolaFilosofica):
    def __init__(self, nome, fondatore, epoca, piacere):
        super().__init__(nome, fondatore, epoca)
        self.piacere = piacere

    def descrivi(self):
        return (super().descrivi() +" Il tipo di piacere perseguito è: "+self.piacere)


if __name__ == "__main__":

    stoicismo = Stoicismo("visionaresimo", "patrizio", "ellenistica", "visione")
    epicureismo = Epicureismo("Epicureismo", "morbi", "ellenistica","aura")
    filosofo1 = Filosofo("prof piccio", 1988)
    filosofo2 = Filosofo("rama", 2009)
    filosofo3 = Filosofo("tom", 2009)
    filosofo7 = Filosofo("pucci",2010)
    filosofo4 = Filosofo("adolfo", 1945)
    filosofo5 = Filosofo("benny", 1922)
    filosofo6 = Filosofo("ottavi",67)
    filosofo8 = Filosofo("prof milleri",1967)
    stoicismo.aggiungiFilosofo(filosofo1)
    stoicismo.aggiungiFilosofo(filosofo2)
    stoicismo.aggiungiFilosofo(filosofo3)
    stoicismo.aggiungiFilosofo(filosofo7)
    epicureismo.aggiungiFilosofo(filosofo4)
    epicureismo.aggiungiFilosofo(filosofo5)
    epicureismo.aggiungiFilosofo(filosofo6)
    epicureismo.aggiungiFilosofo(filosofo8)
    print(stoicismo.descrivi())
    print(epicureismo.descrivi())
    stoicismo.stampaFilosofi()
    epicureismo.stampaFilosofi()