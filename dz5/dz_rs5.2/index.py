from aiohttp import web

products = [
    {"naziv": "Jabuka", "cijena": 0.5, "kolicina": 100},
    {"naziv": "Kruška", "cijena": 0.7, "kolicina": 50},
    {"naziv": "Banana", "cijena": 0.6, "kolicina": 75}
]
async def handler_proizvodi(request):
    return web.json_response(products)

async def post_proizvod(request):
    data = await request.json()
    
    print("Primljeni podaci:", data)
    
    products.append(data)
    
    return web.json_response(products)

app = web.Application()
app.router.add_get('/proizvodi', handler_proizvodi)  
app.router.add_post('/proizvodi', post_proizvod)  

web.run_app(app, port=8081)