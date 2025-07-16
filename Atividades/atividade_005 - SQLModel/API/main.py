from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel, Session, create_engine, select
from models import Pedido
import pandas as pd

app = FastAPI()
url = "sqlite:///pedidos.db"
engine = create_engine(url)
SQLModel.metadata.create_all(engine)

@app.on_event("startup")
def importar_csv():
    df = pd.read_csv("C:/Users/20221101110036/Documents/POS/Atividades/atividade_005 - SQLModel/20250702_Pedidos_csv_2025.csv", encoding="utf-16", sep=";")
    pedidos = [Pedido(**row) for row in df.to_dict(orient="records")]
    with Session(engine) as session:
        if not session.exec(select(Pedido)).first():
            session.add_all(pedidos)
            session.commit()

@app.get("/pedidos/{id_pedido}", response_model=Pedido)
def buscar_pedido(id_pedido: int):
    with Session(engine) as session:
        pedido = session.get(Pedido, id_pedido)
        if pedido:
            return pedido
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
