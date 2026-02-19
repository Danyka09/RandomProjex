import requests
base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}pokemon/{name}"
    response = requests.get(url)
    response_json = response.json()
    pokename = response_json['name']
    print(pokename)
get_pokemon_info("PIKACHU")