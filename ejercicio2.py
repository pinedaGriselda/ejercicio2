import requests

url = 'https://api.datos.gob.mx/v1/calidadAire'

data = requests.get(url)

valor_buscado = "58c780bf281e87010078f491"

if data.status_code == 200:
    data = data.json()
    for x in data['results']:
        if x['_id'] == valor_buscado:      
           for y in x['stations']:
               for z in y['measurements']:
                   resultados = {'value':z['value'], 'unit':z['unit'], 'pollutant':z['pollutant']}
            
print(resultados)
           