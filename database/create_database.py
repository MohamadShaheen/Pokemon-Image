import os
import json
from dotenv import load_dotenv
from pymongo import MongoClient
from utils.external_api_operations import get_pokemon_details
from utils.request_response_operations import get_image_by_url

load_dotenv()

host = os.getenv('SERVER_HOST')
port = os.getenv('DATABASE_PORT')
database = os.getenv('DATABASE_NAME')
collection = os.getenv('DATABASE_COLLECTION')


def create_database():
    with open('../config.json', 'r') as file:
        config = json.load(file)

    if config['create_database'] == 1:
        print('Database already created')
        return

    client = MongoClient(f'mongodb://{host}:{port}/')
    my_database = client[database]
    my_collection = my_database[collection]

    with open('../data/pokemons_data.json', 'r') as file:
        data = json.load(file)

    for entry in data:
        pokemon_name = entry['name']
        pokemon_id, pokemon_image_url = get_pokemon_details(pokemon_name=pokemon_name)
        pokemon_image = get_image_by_url(image_url=pokemon_image_url)

        document = my_collection.find_one({'pokemon_name': pokemon_name})

        if document:
            if document['pokemon_image'] == pokemon_image:
                print(f'Image already stored in database as {pokemon_name}')
                continue

            my_collection.delete_one({'pokemon_name': pokemon_name})

        my_collection.insert_one({'_id': pokemon_id, 'pokemon_name': pokemon_name, 'pokemon_image_url': pokemon_image_url, 'pokemon_image': pokemon_image})
        print(f'The image of {pokemon_name} was successfully stored in the database!')

    config['create_database'] = 1

    with open('../config.json', 'w') as file:
        json.dump(config, file, indent=4)


create_database()
