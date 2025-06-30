from pydantic import BaseModel

class Carro(BaseModel):
    car_id: int
    car_nome: str
    car_marca: str
    car_modelo: str
    car_placa: str