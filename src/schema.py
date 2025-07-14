from pydantic import BaseModel

 # Para validacao dos tipos de dados
class PokemonSchema(BaseModel): # contrato de dados, schema de dados, view da api
    name: str
    types: str
    weight: int

    class Config:
        from_attributes = True # para comunicar com o ORM (sqlalchemy)