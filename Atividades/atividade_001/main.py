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

# Rota pra remover o carro
@app.delete("/carros/{carro_id}", response_model=Carro)
def remover_carro(carro_id:int):
    for index, carro in enumerate(carros): # Percorrer a lista de carros
        if carro_id == carro.car_id:
            del carros[index] # Aqui eu removo o carro
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
# Rota para cadastrar uma nova reserva -- FALTA VALIDAR A DATA
@app.post("/reservas/", response_model=Reserva)
def cadastro_reserva(nova_reserva:Reserva):
    if nova_reserva.res_data_fim >= nova_reserva.res_data_inicio: # Aqui eu verifico se a data fianl é maior que a data inicial!
        for cli_index, cliente in enumerate(clientes): # Percorer a lista de clientes
            if cliente.cli_id == nova_reserva.res_cliente_id: # Verificando se o cliente existe
                for car_index, carro in enumerate(carros): # Esse for serve pra percorer a lista de carros
                    if carro.car_id == nova_reserva.res_carro_id and carro.car_disponivel == True: # Aqui eu verifico se o id é o mesmo e também se o carro tá disponível
                        carros[car_index].car_disponivel = False # Se der tudo certo o carro altomaticamente fica como indisponível
                        reservas.append(nova_reserva) # Adiciono a nova reserva
                        return nova_reserva
                # Se não der certo
                raise HTTPException(status_code=404, detail="Esse carro não está disponível")
        # Se o clinete não existir
        raise HTTPException(status_code=404, detail="Cliente inexistente")
    # Esse HTTPException serve como o tratamento de erro, porque quando a data não tá OK, ele retorna status 500 - Erro interno no servidor (problema no código ou sistema do servidor) -, aí eu trato isso aqui
    raise HTTPException(status_code=500, detail="Datas inconsistentes!")

# Rota para listar todas as reservas
@app.get("/reservas/", response_model=List[Reserva]) # Lista de reservas
def listar_reservas():
    return reservas

# Rota para remover um reserva!
@app.delete("/reservas/{res_id}", response_model=Reserva)
def remover_reserva(id_reserva:int):
    for num_reserva, reserva in enumerate(reservas): # Percorrer a lista de reservas
        if reserva.res_id == id_reserva: # Se o id passado por o mesmo
            for index, carro in enumerate(carros): # Percorrer a lista de carros
                if carro.car_id == reserva.res_carro_id: # Varifica o ID do carro
                    carros[index].car_disponivel = True # Mudar o estado do carro
                    reservas.pop(num_reserva) # Remove a reserva
                    return(reserva)
        # Se a reserva não exite 
        raise HTTPException(status_code=404, detail="Reserva inexistente!")