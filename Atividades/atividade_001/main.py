from fastapi import FastAPI, HTTPException
from models import Carro, Cliente, Reserva
from typing import List

app = FastAPI()

# Definindo listas de carros e clientes
carros: List[Carro] = []
clientes: List[Cliente] = []
# Aqui eu defini uma lista para todas as reservas, acho que talvez isso não seja a melhor opção, mas bora vê 👀
reservas: List[Reserva] = []

# CARROS
# Rota pra listar todos os carros
@app.get("/carros/", response_model=List[Carro]) #Esse List[Carro] é inportante pra gerrar uma lista de cada carro, pq se não da erro, já  tentei fazer sem.
def listar_todos_carros():
    return carros

@app.post("/carros/", response_model=Carro)
def cadastrar_carro(novo_carro:Carro): #Instancia do modelo de Carro pra me permitir editar os dados para criar o carro.
    carros.append(novo_carro)
    return novo_carro #Aqui eu retornei pq eu quis mesmo, mas se não, é só tirar o response_model=Carro e isso.

# Definindo rota pra atualizar o valor de carro
@app.put("/carros/{carro_id}", response_model=Carro)
def atualizar_carro(carro_id:int, carro_atualizado:Carro): # Aqui eu pesso pra passar na função o id do carro pra poder fazer a verficação, além de fazer uma instancia de carro pra poder atualizra seu valor
    for index, carro in enumerate(carros): #Esse for é pra sair verificando de um em um na lista de carros (Index > Número, carro >  Cada carro)
        if carro.car_id == carro_id:
            carros[index] = carro_atualizado #Aqui é onde eu substituo os valores
            return carro_atualizado
    raise HTTPException(status_code=404, detail="Carro não localizado!") #Isso aqui tá caso o carro não exista

# Rota pr remover o carro
@app.delete("/carros/{carro_id}", response_model=Carro)
def remover_carro(carro_id:int):
    for index, carro in enumerate(carros):
        if carro_id == carro.car_id:
            del carros[index]
            return carro
    raise HTTPException(status_code=404, detail="Carro inexistente!")

# FAZER: GET /carros/disponiveis: listar apenas os carros disponíveis.

# CLIENTES
# Rota para listar todos os clientes
@app.get("/clientes/", response_model=List[Cliente])
def listar_todos_clientes():
    return clientes

# Rota para cadastrar novos clientes
@app.post("/clientes/")
def cadastrar_ciente(novo_cliente:Cliente):
    clientes.append(novo_cliente) #Aqui eu já não fiz o retorno pra testar mesmo.

# Rota para pesquisar um cliente em expecífico
@app.get("/clientes/{cliente_id}", response_model=Cliente)
def pesquisar_cliente(cliente_id:int):
    for index, cliente in enumerate(clientes): #Esse for aqui é que vai tá servindo pra verificar de um em um se é ou não o cliente que eu quero
        if cliente_id == cliente.cli_id:
            return clientes[index] #Achqo que é assim que ele retorna só um
    raise HTTPException(status_code=404, detail="Cliente inexistente!")

# Rotas de Reservas
# Rota para cadastrar uma nova reserva
@app.post("/reservas/", response_model=Reserva)
def cadastro_reserva(nova_reserva:Reserva):
    for index, carro in enumerate(carros):
        if carro.car_id == nova_reserva.res_id:
            carros[index].car_disponivel = False
            reservas.append(nova_reserva)
            return nova_reserva
        else: 
            return "Esse carro já está reservado para outra pessoa"
    raise HTTPException(status_code=404, detail="Esse carro não foi encontrado no registro")

# Rota para listar todas as reservas
@app.get("/reservas/", response_model=List[Reserva])
def listar_reservas():
    return reservas