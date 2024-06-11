import os
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv
from pymongo import MongoClient
from utils.external_api_operations import get_pokemon_details
from utils.request_response_operations import get_image_by_url

load_dotenv()

host = os.getenv('SERVER_HOST')
port = os.getenv('DATABASE_PORT')
database = os.getenv('DATABASE_NAME')
collection = os.getenv('DATABASE_COLLECTION')


class PokemonsInteractor:
    def __init__(self):
        self.client = MongoClient(f'mongodb://{host}:{port}/')

        cursor = self.client[database]
        self.collection = cursor[collection]

    def get_image_by_name(self, pokemon_name):
        document = self.collection.find_one({'pokemon_name': pokemon_name}, {'pokemon_image': 0})
        return document

    def get_all_images(self):
        documents = self.collection.find()
        output = [{'pokemon_id': item['_id'], 'pokemon_name': item['pokemon_name'], 'pokemon_image_url': item['pokemon_image_url']} for item in documents]
        return output

    def insert_image(self, pokemon_name):
        pokemon_id, pokemon_image_url = get_pokemon_details(pokemon_name=pokemon_name)
        pokemon_image = get_image_by_url(image_url=pokemon_image_url)

        document = self.collection.find_one({'pokemon_name': pokemon_name})

        if document:
            if document['pokemon_image'] == pokemon_image:
                return 'Pokemon already exists in the database'

            self.collection.delete_one({'pokemon_name': pokemon_name})

        self.collection.insert_one({'_id': pokemon_id, 'pokemon_name': pokemon_name, 'pokemon_image_url': pokemon_image_url, 'pokemon_image': pokemon_image})
        return None

    def delete_image(self, pokemon_name):
        document = self.collection.find_one({'pokemon_name': pokemon_name})

        if document is None:
            return f'Pokemon {pokemon_name} does not exist'

        self.collection.delete_one({'pokemon_name': pokemon_name})

    def show_image(self, pokemon_name):
        document = self.collection.find_one({'pokemon_name': pokemon_name})

        if document:
            image_byte_arr = document['pokemon_image']
            image = Image.open(BytesIO(image_byte_arr))
            image.show()
        else:
            return f'Pokemon {pokemon_name} does not exist'

    def edit_image(self, pokemon_name, new_pokemon_image_url):
        document = self.collection.find_one({'pokemon_name': pokemon_name})

        if document is None:
            return f'Pokemon {pokemon_name} does not exist'

        if document['pokemon_image_url'] == new_pokemon_image_url:
            return 'You are providing the same existing pokemon image'

        response = get_image_by_url(image_url=new_pokemon_image_url)

        if response is None:
            return f'You are trying to insert invalid image. Please check the URL that you provided'

        self.collection.update_one({'pokemon_name': pokemon_name}, {'$set': {'pokemon_image_url': new_pokemon_image_url, 'pokemon_image': response}})
