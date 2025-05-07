# pip install fastapi uvicorn 
# pip install -r requeriments.txt
# python -m venv .virtual
# .\.virtual\Scripts\activate
# uvicorn main:app

from fastapi import FastAPI, HTTPException
from models import * # Importando os modelos do models.py
from typing import List # Isso aqui é pra validar um tipo de dado, o LIST

app = FastAPI() # Instancia do FatsAPI

# Criando listas de 4/5 classes do código. Lista de usuários, livros e emprestimos
usuarios: List[Usuario] = [] 
livros: List[Livro] = []
emprestimos: List[Emprestimo] = []
 
# Rota para listar usuários
@app.get("/usuarios/", response_model=List[Usuario])
def listar_usuarios():
    return usuarios

# Rota para criar/adicionar usuários
@app.post("/usuarios/", response_model=Usuario)
def adicionar_user(usuario_criado:Usuario): # Aqui esse variável "usuario_criado" eu não entendi  tão bem, mas ela vai servir para criar o usuário.
    usuarios.append(usuario_criado) # Adicionamdo na lista de usuários
    return usuario_criado # Retornamdo o usuário criado

# # Rota de deletar o usuário
@app.delete("/usuarios/{usuario_nome}", response_model=Usuario)
def excluir_usuario(usuario_nome:str):
    for num, usuario in enumerate(usuarios):
        if usuario.username == usuario_nome:
            del usuarios[num]
            return usuario
    raise HTTPException(status_code=404, detail="Não localizado")

# Resposta do Gemini:
# Rota de deletar o usuário
# @app.delete("/usuarios/{usuario_nome}", response_model=Usuario)
# def excluir_usuario(usuario_nome: str):
#     usuario_deletado = None  # Inicializa uma variável para armazenar o usuário deletado
#     for num, usuario in enumerate(usuarios):
#         if usuario.nome == usuario_nome:
#             usuario_deletado = usuarios.pop(num) # Remove e retorna o elemento removido
#             return usuario_deletado
#     raise HTTPException(status_code=404, detail="Não localizado")