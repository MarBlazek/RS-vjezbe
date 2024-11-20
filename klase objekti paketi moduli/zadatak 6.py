'''
1.
class Automobil:
    def __init__(self, marka, model, godina_proizvodnje, kilometraza):
        self.marka = marka
        self.model = model 
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraza = kilometraza
    def ispis(self):
        return f"Automobil je marke {self.marka}, model {self.model}, proizveden {self.godina_proizvodnje} i ima {self.kilometraza} kilometara"

automobil = Automobil ("Kia", "Rio", "2021.", 35000)

print(automobil.ispis())

2.
class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b 
    
    def zbroj(self):
        return (self.a + self.b) 
    def oduzimanje(self):
        return (self.a - self.b)
    def mnozenje(self):
        return(self.a * self.b)
    def dijeljenje(self):
        return(self.a / self.b)
    def potenciranje(self):
        return(self.a ** self.b)
    def korijen(self):
        korijen_a = self.a ** 0.5
        korijen_b = self.b ** 0.5
        return(f"Korijen od {self.a} je {korijen_a}, korijen od {self.b} je {korijen_b}")
k = Kalkulator(4,9)
print("zbroj: ", k.zbroj())
print("oduzimanje: ", k.oduzimanje())
print("množenje: ", k.mnozenje())
print("dijeljenje: ", k.dijeljenje())
print("potenciranje: ", k.potenciranje())
print("korijen: ", k.korijen())

3.
class Student:
    def __init__(self, ime, prezime, godine, ocjene):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene
    def prosjek(self):
        return sum (self.ocjene) / len(self.ocjene)     

studenti = [
{"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
{"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
{"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
{"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
{"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
{"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
]

studenti_objekti = [Student(student["ime"], student["prezime"], student["godine"], student["ocjene"]) for student in studenti]

najbolji_student = ???

4. 
import math
class Krug:
    def __init__(self, r):
        self.r = r
    def opseg(self):
        return 2*self.r* math.pi
    def povrsina(self):
        return self.r ** 2 * math.pi
    
krug = Krug (9)

print(krug.opseg())
print(krug.povrsina())

5.

class Radnik:
    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa
    def work(self):
        print(f"Radim na poziciji {self.pozicija}")

class Manager (Radnik):
    def __init__(self, ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa)
        self.department = department
    def work(self):
        print(f"Radim na poziciji {self.pozicija} u odjelu {self.department}")
    def give_raise(self): ???
        print()

radnik = Radnik ("Ana", "trgovac", 1000)
manager = Manager ("Iva", "prodavac", 900, "prodaja")

radnik.work()
manager.work()
'''


    


