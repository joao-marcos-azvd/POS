from fastapi import FastAPI, HTTPException
import pandas as P

app = FastAPI()

# Carregando o arquivo
arquivo = P.read_csv("../20250702_Pedidos_csv_2025.csv", encoding='utf-16')

# @app.get("/pedidos/")
# def listar_pedidos():
#     return arquivo.to_dict(orient="records")  # retorna uma lista de dicionários

@app.get("/pedidos/{id_pedido}")
def obter_pedido(id_pedido: int):
    if id_pedido in arquivo['id'].values:
        pedido = arquivo[arquivo['id'] == id_pedido].to_dict(orient="records")[0]
        return pedido
    else:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")