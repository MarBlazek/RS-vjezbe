'''
Definirajte dvije korutine koje će simulirati dohvaćanje podataka s weba. Prva korutina neka vrati
listu proizvoljnih rječnika (npr. koji reprezentiraju podatke o korisnicima) nakon 3 sekunde, a druga
korutina neka vrati listu proizvoljnih rječnika (npr. koji reprezentiraju podatke o proizvodima) nakon 5
sekundi. Korutine pozovite konkurentno korištenjem asyncio.gather() i ispišite rezultate. Program
se mora izvršavati ~5 sekundi.
'''
import asyncio

async def dohvat_podataka():
    rječnik_korisnici = {'Ime' : "Ivan", 'Prezime': "Ivić"}
    await asyncio.sleep(3)
    return rječnik_korisnici

async def dohvat_podataka2():
    rječnik_proizvodi = {'Ime': "mlijeko", 'Količina': '5', 'Cijena': '2'}
    await asyncio.sleep (5)
    return rječnik_proizvodi

async def main():
    rječnik_korisnici, rječnik_proizvodi = await asyncio.gather(dohvat_podataka(), dohvat_podataka2())

    print (rječnik_korisnici)
    print (rječnik_proizvodi)

asyncio.run(main())