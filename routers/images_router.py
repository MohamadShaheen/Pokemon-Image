from fastapi import APIRouter, HTTPException
from DAL.pokemons_interactor import PokemonsInteractor

router = APIRouter()


@router.get('/single-image/')
async def get_single_image(pokemon_name: str):
    pokemons_interactor = PokemonsInteractor()
    response = pokemons_interactor.get_image_by_name(pokemon_name=pokemon_name)

    if response is None:
        raise HTTPException(status_code=404, detail='Pokemon does not exist')

    return response


@router.get('/all-images/')
async def get_all_images():
    pokemons_interactor = PokemonsInteractor()
    response = pokemons_interactor.get_all_images()

    if len(response) == 0:
        raise HTTPException(status_code=404, detail='Did not find any images')

    return response


@router.get('/show-image/')
async def show_image(pokemon_name: str):
    pokemons_interactor = PokemonsInteractor()
    response = pokemons_interactor.show_image(pokemon_name=pokemon_name)

    if response is not None:
        raise HTTPException(status_code=404, detail=response)

    return 'SAWADIKA! Happy Now?'


@router.post('/')
async def create_image(pokemon_name: str):
    pokemons_interactor = PokemonsInteractor()
    response = pokemons_interactor.insert_image(pokemon_name=pokemon_name)

    if response is not None:
        raise HTTPException(status_code=400, detail=response)

    return f'Pokemon {pokemon_name} was successfully added to the database'


@router.delete('/')
async def delete_image(pokemon_name: str):
    pokemons_interactor = PokemonsInteractor()
    response = pokemons_interactor.delete_image(pokemon_name=pokemon_name)

    if response is not None:
        raise HTTPException(status_code=404, detail='Pokemon does not exist')

    return f'Pokemon {pokemon_name} was successfully deleted from the database'


@router.put('/')
async def update_image(pokemon_name: str, new_pokemon_image_url: str):
    pokemons_interactor = PokemonsInteractor()
    response = pokemons_interactor.edit_image(pokemon_name=pokemon_name, new_pokemon_image_url=new_pokemon_image_url)

    if response is not None:
        raise HTTPException(status_code=404, detail=response)

    pokemons_interactor.show_image(pokemon_name=pokemon_name)
    return f'Pokemon {pokemon_name}\'s image was successfully edited'
