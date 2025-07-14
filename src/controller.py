# Controller é responsável por controlar todas as etapas

import requests

from db import SessionLocal, engine, Base
from models import Pokemon
from schema import PokemonSchema

Base.metadata.create_all(engine)

def get_pokemon_data(id: int) -> PokemonSchema:

    resp = requests.get(url = f'https://pokeapi.co/api/v2/pokemon/{id}')

    if resp.status_code == 200:
        data = resp.json()

        data_name = data['name']
        data_types = data['types']
        data_weight = data['weight']

        type_name_list = []
        for type in data_types:

            type_name_list.append(type['type']['name'])

        types = ', '.join(type_name_list)

        return PokemonSchema(name = data_name, types = types, weight = data_weight)
    
    else:

        return None
    
def add_pokemon_to_db(pokemon_schema: PokemonSchema) -> Pokemon:

    with SessionLocal() as db:

        db_pokemon = Pokemon(name = pokemon_schema.name,
                             types = pokemon_schema.types, 
                             weight = pokemon_schema.weight)
        
        db.add(db_pokemon)
        db.commit()
        db.refresh(db_pokemon)

    return db_pokemon