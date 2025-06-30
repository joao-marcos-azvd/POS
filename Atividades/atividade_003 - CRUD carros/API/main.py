from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from models import Carro

app = FastAPI()

carros: List[Carro] = []

@app.post("/carro", response_model=Carro)
def adicionar_carro(carro: Carro):
    for car in carros:
        if car.placa == carro.placa:
            raise HTTPException(status_code=400, detail="Placa já cadastrada no sistema!")
    carros.append(carro)
    return carro

@app.get("/carros", response_model=List[Carro])
def listar_carros():
    return carros

@app.get("/carro/{placa}", response_model=Carro)
def buscar_carro(modelo: str):
    for car in carros:
        if car.modelo == modelo:
            return car
    raise HTTPException(status_code=404, detail="Carro não encontrado!")

@app.delete("/carro/{placa}", response_model=Carro)
def deletar_carro(modelo: str):
    for index, carro in enumerate(carros):
        if carro.modelo == modelo:
            return carros.pop(index)
    raise HTTPException(status_code=404, detail="Carro não encontrado!")

@app.put("/carro/{placa}", response_model=Carro)
def editar_carro(placa: str, carro_editado: Carro):
    for index, carro in enumerate(carros):
        if carro.placa == placa:
            if carro.placa != carro_editado.placa:
                for c in carros:
                    if c.placa == carro_editado.placa:
                        raise HTTPException(status_code=400, detail="Nova placa já cadastrada!")
            carros[index] = carro_editado
            return carro_editado

    raise HTTPException(status_code=404, detail="Carro não encontrado!")
