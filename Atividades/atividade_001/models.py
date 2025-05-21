from pydantic import BaseModel
from datetime import date

# Modelo de Carro
class Carro(BaseModel):
    car_id:int
    car_modelo:str
    car_marca:str
    car_ano:int
    car_disponivel:bool

# Modelo dE Cliente
class Cliente(BaseModel):
    cli_id:int
    cli_nome:str
    cli_cpf:str
    cli_telefone:str

# Modelo de Reserva
class Reserva(BaseModel):
    res_id:int
    res_cliente_id:int #Esse aqui eu vou precisar fazer um Link com o modelo de Cliente
    res_carro_id:int #Esse também, só que com o de Carro
    res_data_inicio:date
    res_data_fim:date