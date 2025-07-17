from fastapi import FastAPI,HTTPException
from models import Usuario,Livro,Biblioteca,Emprestimo
from typing import List
import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # durante o desenvolvimento
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

bibliotecas: List[Biblioteca] = []

@app.get("/bibliotecas",response_model=List[Biblioteca])
def listar_bibliotecas():
    return bibliotecas

@app.get("/bibliotecas/{nome}",response_model=Biblioteca)
def listar_biblioteca(nome:str):
    for biblioteca in bibliotecas:
        if biblioteca.nome ==nome:
            return biblioteca
    raise HTTPException(404,"Não localizado.")

@app.post("/bibliotecas")
def cadastrar_biblioteca(nome:str):
    data = {
        "nome":nome,
        "acervo":[],
        "usuarios":[],
        "emprestimos":[]
    }
    biblioteca = Biblioteca(**data)
    bibliotecas.append(biblioteca)
    
@app.delete("/bibliotecas/{nome}",response_model=Biblioteca)
def listar_biblioteca(nome:str):
    for id,biblioteca in enumerate(bibliotecas):
        if biblioteca.nome ==nome:
            bibliotecas.pop(id)
            return biblioteca
    raise HTTPException(404,"Não localizado.")

@app.get("/usuarios/",response_model=List[Usuario])
def listar_usuarios(nome_biblioteca:str):
    for biblioteca in bibliotecas:
        if biblioteca.nome == nome_biblioteca:
            return biblioteca.usuarios
    raise HTTPException(404,"Não localizado.")

@app.get("/usuarios/{username}", response_model=Usuario)
def listar_usuario(nome_biblioteca:str, nome_usuario:str):
    for biblioteca in bibliotecas:
        if biblioteca.nome == nome_biblioteca:
            for usuario in biblioteca.usuarios:
                if usuario.username == nome_usuario:
                    return usuario
    raise HTTPException(404,"Usuário não localizado")

@app.post("/usuarios/")
def criar_usuario(nome_biblioteca:str,novo_usuario:Usuario):
    for biblioteca in bibliotecas:
        if biblioteca.nome == nome_biblioteca:
            return biblioteca.usuarios.append(novo_usuario)
    raise HTTPException(404,"Não localizado.")
   
@app.delete("/usuarios/{username}",response_model=Usuario)
def excluir_usuario(nome_biblioteca:str,nome_usuario:str):
    for biblioteca in bibliotecas:
        if biblioteca.nome == nome_biblioteca:
            for id,usuario in enumerate(biblioteca.usuarios):
                if usuario.username == nome_usuario:
                    biblioteca.usuarios.pop(id)
                    return usuario
    raise HTTPException(404,"Usuário não localizado")

@app.get("/livros",response_model=List[Livro])
def listar_livros(nome_biblioteca:str):
    for biblioteca in bibliotecas:
        if biblioteca.nome == nome_biblioteca:
            return biblioteca.acervo
    raise HTTPException(404,"não localizado")  
 
@app.get("/livros/{titulo}",response_model=Livro)
def listar_livros(nome_biblioteca:str, titulo_livro:str):
    for biblioteca in bibliotecas:
        if biblioteca.nome == nome_biblioteca:
            for livro in biblioteca.acervo:
             if livro.titulo == titulo_livro:
                return livro
    raise HTTPException(404,"Não localizado")

@app.delete("/livros/{titulo}",response_model=Livro)
def deletar_livro(nome_biblioteca:str,titulo_livro:str):
    for biblioteca in bibliotecas:
        if biblioteca.nome == nome_biblioteca:
            for id, livro in enumerate(biblioteca.acervo):
                if livro.titutlo == titulo_livro:
                    biblioteca.acervo.pop(id)
                    return livro
    raise HTTPException(404,"Não localizado")

@app.post("/livros", response_model=Livro)
def criar_livro(nome_biblioteca:str,novo_livro:Livro):
    for biblioteca in bibliotecas:
        if biblioteca.nome == nome_biblioteca:
            biblioteca.acervo.append(novo_livro)
            return novo_livro
    raise HTTPException(404,"Não localizado")

@app.get("/emprestimos",response_model=List[Emprestimo])
def listar_emprestimos(nome_biblioteca:str):
    for biblioteca in bibliotecas:
        if biblioteca.nome == nome_biblioteca:
            return biblioteca.emprestimos
    raise HTTPException(404,"Não localizado")

@app.post("/emprestimos")
def cadastrar_emprestimos(nome_biblioteca:str,usuario:str,livro:str):
    user = None
    book = None
    for biblioteca in bibliotecas:
        if biblioteca.nome == nome_biblioteca:
            for u in biblioteca.usuarios:
                if u.username == usuario:
                    user = u
            for l in biblioteca.acervo:
                if l.titulo == livro:
                    book = l
            if user and book:
                data = {
                    "usuario":user,
                    "livro":book,
                    "data_emprestimo":datetime.datetime.now().date(),
                    "data_devolucao":datetime.date(2025,5,31),
                }
                emprestimo = Emprestimo(**data)
                biblioteca.emprestimos.append(emprestimo)
    if not user or not book:
        raise HTTPException(404,"Não localizado")
