'''
LAMBDA
1.
lambda x: x**2
print((lambda x: x**2)(3))
2.
zbroji_pa_kvadriraj = lambda a, b: (a+b)**2
print(zbroji_pa_kvadriraj(5,2))
3.
kvadriraj_duljinu = lambda niz: len(niz)**2
print(kvadriraj_duljinu([1,2,3,4]))
4.
pomnozi_i_potenciraj = lambda x,y: (y*5) ** x
print(pomnozi_i_potenciraj(2,4))
5.
paran_broj= lambda x: True if x % 2 == 0 else None
print(paran_broj(6))

FUNKCIJE VIŠEG REDA
1.
nizovi=["jabuka", "kruška", "banana", "naranča"]
kvadrirane_duljine = list(map(lambda niz: len(niz)**2, nizovi))
print(kvadrirane_duljine)
2.
lista = [1,21,33,45,2,2,1,-32,9,10]
veci_od_5 = list(filter(lambda x: x > 5, lista))
print(veci_od_5)
3.
brojevi =[10,5,12,15,20]
transform = dict(map(lambda x: (x, x**2), brojevi))
print(transform)
4.
studenti = [
{"ime": "Ivan", "prezime": "Ivić", "godine": 19},
{"ime": "Marko", "prezime": "Marković", "godine": 22},
{"ime": "Ana", "prezime": "Anić", "godine": 21},
{"ime": "Petra", "prezime": "Petrić", "godine": 13},
{"ime": "Iva", "prezime": "Ivić", "godine": 17},
{"ime": "Mate", "prezime": "Matić", "godine": 18}
]
svi_punoljetni = all(map(lambda student: student["godine"]>=18, studenti))
print(svi_punoljetni)
5.
rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples","pjesma", "otorinolaringolog"]
min_duljina = int(input("Unesite minimalnu duljinu riječi: "))
duge_rijeci = list(filter(lambda rijec: len(rijec) > min_duljina, rijeci))
print(duge_rijeci)
COMPREHENSION
1. 
parni_kvadrati = [x**2 for x in range (20, 51) if x%2 == 0]
print(parni_kvadrati)
2.
rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples",
"pjesma", "otorinolaringolog"]
duljine_sa_slovom_a = [len(rijec) for rijec in rijeci if "a" in rijec]
print(duljine_sa_slovom_a)
3.
kubovi = [{x: x**3 if x%2 !=0 else x} for x in range (1,11)]
print(kubovi)
4.
korijeni = {x: round(x**0.5,2) for x in range (50,501,50)}
print(korijeni)
5.
studenti = [
{"ime": "Ivan", "prezime": "Ivić", "bodovi": [12, 23, 53, 64]},
{"ime": "Marko", "prezime": "Marković", "bodovi": [33, 15, 34, 45]},
{"ime": "Ana", "prezime": "Anić", "bodovi": [8, 9, 4, 23, 11]},
{"ime": "Petra", "prezime": "Petrić", "bodovi": [87, 56, 77, 44, 98]},
{"ime": "Iva", "prezime": "Ivić", "bodovi": [23, 45, 67, 89, 12]},
{"ime": "Mate", "prezime": "Matić", "bodovi": [75, 34, 56, 78, 23]}
]
zbrojeni_bodovi = [{student["prezime"]: sum (student["bodovi"])} for student in studenti]
print(zbrojeni_bodovi)
'''

