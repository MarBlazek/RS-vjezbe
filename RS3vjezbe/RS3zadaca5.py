'''
Definirajte korutinu secure_data koja će simulirati enkripciju osjetljivih podataka. Kako se u
praksi enkripcija radi na poslužiteljskoj strani, korutina će simulirati enkripciju podataka u trajanju od 3
sekunde. Korutina prima kao argument rječnik osjetljivih podataka koji se sastoji od ključeva prezime ,
broj_kartice i CVV . Definirajte listu s 3 rječnika osjetljivih podataka. Pohranite u listu zadaci kao u
prethodnom zadatku te pozovite zadatke koristeći asyncio.gather() . Korutina secure_data mora za
svaki rječnik vratiti novi rječnik u obliku: {'prezime': prezime , 'broj_kartice': 'enkriptirano',
'CVV': 'enkriptirano'} . Za fake enkripciju koristite funkciju hash(str) koja samo vraća hash
vrijednost ulaznog stringa.
'''
import asyncio
osjetljivi_podaci = [
    {'prezime': 'Anić', 'broj_kartice': '123456789', 'CVV': '123'}
    {'prezime': 'Perić', 'broj_kartice': '987654321', 'CVV': '987'}
    {'prezime': 'Ivić', 'broj_kartice': '753421869', 'CVV': '753'}
]
async def secure_data(podaci):
    await asyncio.sleep (3)
    return {'prezime': prezime , 'broj_kartice': 'enkriptirano',
'CVV': 'enkriptirano'} 
#???

async def main():
    zadaci = [secure_data(podaci) for podaci in osjetljivi_podaci]
    rezultati = await asyncio.gather(zadaci)
    for rezultat in rezultati:
        print(rezultat)


asyncio.run(main())