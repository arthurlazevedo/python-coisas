import requests
import json
from typing import Dict
from fastapi import FastAPI, Query
from glob import glob


def criar_arquivos_json_exemplo():
  url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
  response = requests.get(url)

  dados_restaurantes = response.json()
  lista_restaurantes: Dict[str, list[dict]] = {}


  if response.status_code == 200:
    for restaurantes in dados_restaurantes:
      if restaurantes['Company'] not in lista_restaurantes.keys():
        lista_restaurantes[restaurantes['Company']] = []
      lista_restaurantes[restaurantes['Company']].append({
        'item': restaurantes['Item'],
        'preço': restaurantes['price'],
        'descrição': restaurantes['description']
      })

    for nome, dados in lista_restaurantes.items():
      with open('jsons/' + nome.replace(' ', '-').lower() + '.json', 'w') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

  print(response.status_code)

def converter(restaurante: str):
  match restaurante:
    case 'burger-king' | 'pizza-hut' | 'taco-bell':
      return restaurante.replace('-', ' ').title()
    case 'wendy’s':
      return 'Wendy\'s'
    case 'mcdonald’s':
      return 'MC Donald\'s'
    case 'kfc':
      return 'KFC'

app = FastAPI()

@app.get('/items/')
def restaurantes(restaurante: str = Query(None)):
  try:
    if restaurante:
      nome_arquivo = restaurante.replace(' ', '-').lower()
      with open(f'jsons/{nome_arquivo}.json', 'r') as arquivo:
        return json.load(arquivo)

    lista_restaurantes = {}

    for arquivo_json in glob('jsons/*.json'):
      nome = converter(arquivo_json[arquivo_json.index('/') + 1:arquivo_json.index('.')])
      with open(arquivo_json, 'r') as arquivos:
        lista_restaurantes[nome] = json.load(arquivos)

    return lista_restaurantes
  except Exception as e:
    return {'Erro': f'O erro foi {e.__cause__}'}



if __name__ == '__main__':
  import uvicorn
  uvicorn.run(app, host="localhost", port=8000)