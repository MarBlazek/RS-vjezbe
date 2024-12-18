from aiohttp import web

proizvodi = [
{"id": 1, "naziv": "Laptop", "cijena": 5000},
{"id": 2, "naziv": "Miš", "cijena": 100},
{"id": 3, "naziv": "Tipkovnica", "cijena": 200},
{"id": 4, "naziv": "Monitor", "cijena": 1000},
{"id": 5, "naziv": "Slušalice", "cijena": 50}
]
#Prva ruta vraća listu proizvoda u JSON formatu
async def get_proizvodi(request):
    return web.json_response(proizvodi)

#druga rutu vraća točno jedan proizvod prema ID-u.
async def get_proizvod_by_id(request):
    proizvod_id = int(request.match_info['id'])
    proizvod = None
    for p in proizvodi:
        if p['id'] == proizvod_id:
            proizvod = p
            break
    
    if proizvod is None:
        return web.json_response({'error': 'Proizvod s traženim ID-em ne postoji'}, status=404)
    
    return web.json_response(proizvod)

app=web.Application()
#app.router.add_get(path, handler_function) - dvije rute poslužitelja
app.router.add_get('/proizvodi', get_proizvodi)
app.router.add_get('/proizvodi/{id}', get_proizvod_by_id)

if __name__ == '__main__':
    web.run_app(app, port= 8081)