'''
Definirajte korutinu autentifikacija() koja će simulirati autentifikaciju korisnika na
poslužiteljskoj strani. Korutina kao ulazni parametar prima rječnik koji opisuje korisnika, a sastoji se
od ključeva korisnicko_ime , email i lozinka . Unutar korutine simulirajte provjeru korisničkog
imena na način da ćete provjeriti nalaze li se par korisnicko_ime i email u bazi korisnika. Ova
provjera traje 3 sekunde.

Ako se korisnik ne nalazi u bazi, vratite poruku "Korisnik {korisnik} nije pronađen."
Ako se korisnik nalazi u bazi, potrebno je pozvati vanjsku korutinu autorizacija() koja će simulirati
autorizaciju korisnika u trajanju od 2 sekunde. Funkcija kao ulazni parametar prima rječnik korisnika iz baze
i lozinku proslijeđenu iz korutine autentifikacija() . Autorizacija simulira dekripciju lozinke (samo
provjerite podudaranje stringova) i provjeru s lozinkom iz baze_lozinka. Ako su lozinke jednake, korutine
vraća poruku "Korisnik {korisnik}: Autorizacija uspješna." , a u suprotnom "Korisnik
{korisnik}: Autorizacija neuspješna." .

Korutinu autentifikacija() pozovite u main() funkciji s proizvoljnim korisnikom i lozinkom.
'''
import asyncio

baza_korisnika = [
{'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
{'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
{'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
{'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

baza_lozinka = [
{'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
{'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
{'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
{'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]

async def autentifikacija(korisnik):
    await asyncio.sleep(3)  
    for podatak in baza_korisnika:
        if (podatak['korisnicko_ime'] == korisnik['korisnicko_ime'] and podatak['email'] == korisnik['email']):
            return f"Korisnik {korisnik['korisnicko_ime']} je pronađen."
    return f"Korisnik {korisnik['korisnicko_ime']} nije pronađen."

async def autorizacija(korisnik_iz_baze, unesena_lozinka):
    await asyncio.sleep (2)
    for podatak in baza_lozinka:
        if podatak ['lozinka'] == unesena_lozinka:
            return f"Korisnik {korisnik_iz_baze}: Autorizacija uspješna."
        else:
            return f"Korisnik {korisnik_iz_baze}: Autorizacija neuspješna."


async def main():
    korisnik = {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com', 'lozinka': 'neka_lozinka'}
    rezultat = await autentifikacija(korisnik)
    print(rezultat)

asyncio.run(main())



