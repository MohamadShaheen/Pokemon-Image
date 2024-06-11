import json
import requests


def get_url():
    try:
        with open('../config.json', 'r') as config_file:
            config = json.load(config_file)
    except FileNotFoundError:
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)

    return config['poke_api_URL']


def get_pokemon_details(pokemon_name):
    response = requests.get(f'{get_url()}/{pokemon_name.lower()}')
    if response.status_code == 200:
        data = response.json()
        id = data['id']
        image = data['sprites']['other']['home']['front_default']
        return id, image
    else:
        return None, None
