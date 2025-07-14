from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel, Field, Session, create_engine, select
import pandas as pd

from typing import Optional
from sqlmodel import SQLModel, Field

class Pedido(SQLModel, table=True):
    IdPedido: int = Field(primary_key=True)
    ProtocoloPedido: Optional[str] = None
    Esfera: Optional[str] = None
    UF: Optional[str] = None
    Municipio: Optional[str] = None
    OrgaoDestinatario: Optional[str] = None
    Situacao: Optional[str] = None
    DataRegistro: Optional[str] = None
    PrazoAtendimento: Optional[str] = None
    FoiProrrogado: Optional[str] = None
    FoiReencaminhado: Optional[str] = None
    FormaResposta: Optional[str] = None  
    OrigemSolicitacao: Optional[str] = None
    IdSolicitante: Optional[int] = None
    AssuntoPedido: Optional[str] = None
    SubAssuntoPedido: Optional[str] = None
    Tag: Optional[str] = None
    DataResposta: Optional[str] = None
    Decisao: Optional[str] = None
    EspecificacaoDecisao: Optional[str] = None

app = FastAPI()
engine = create_engine("sqlite:///pedidos.db")
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
