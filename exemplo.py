import requests
from pydantic import BaseModel

 # Para validacao dos tipos de dados
class PokemonSchema(BaseModel): # contrato de dados, schema de dados, view da api
    name: str
    types: str
    weight: int

    class Config:
        from_attributes = True # para comunicar com o ORM (sqlalchemy)

def get_pokemon_data(id: int) -> PokemonSchema:

    resp = requests.get(url = f'https://pokeapi.co/api/v2/pokemon/{id}')

    data = resp.json()

    data_name = data['name']
    data_types = data['types']
    data_weight = data['weight']

    type_name_list = []
    for type in data_types:

        type_name_list.append(type['type']['name'])

    types = ', '.join(type_name_list)

    return PokemonSchema(name = data_name, types = types, weight = data_weight)


if __name__ == '__main__':

    print(get_pokemon_data(6))
    print(get_pokemon_data(25))
    print(get_pokemon_data(37))