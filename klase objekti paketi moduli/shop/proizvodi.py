class Proizvod:
    def __init__(self, naziv, cijena, kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self. kolicina = kolicina
    def ispis (self):
        return f"Naziv: {self.naziv}, cijena:{self.cijena}, kolicina: {self.kolicina}"
    
proizvodi = [
    Proizvod("Kava", 4, 100),
    Proizvod("Mlijeko", 2, 50),
]

#def novi_proizvod(self):
#???




