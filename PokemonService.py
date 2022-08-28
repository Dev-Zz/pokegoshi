import requests
from Models import Mascote

class PokemonService:
    def get_data(escolha_pokemon):

        url = 'https://pokeapi.co/api/v2/pokemon/'
        response = requests.request("GET", url+escolha_pokemon)
        response = response.json()

        habilidades = []
        for i in response["abilities"]:
            habilidades.append(i["ability"]["name"])    
        mascote = Mascote(response["name"], response["height"], response["weight"], response["id"], habilidades)
        
        return mascote