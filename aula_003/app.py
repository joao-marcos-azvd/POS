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
bibliotecas: List[Biblioteca] = []
emprestimos: List[Emprestimo] = []

 
# USUÁRIO - + ou - comentado
# Rota para listar Livros - Comentar
@app.get("/usuarios/", response_model=List[Usuario])
def listar_usuarios():
    return usuarios

# Rota para criar/adicionar usuários
@app.post("/usuarios/", response_model=Usuario)
def adicionar_user(usuario_criado:Usuario): # Aqui esse variável "usuario_criado" eu não entendi  tão bem, mas ela vai servir para criar o usuário.
    usuarios.append(usuario_criado) # Adicionamdo na lista de usuários
    return usuario_criado # Retornamdo o usuário criado

# Rota de deletar o usuário
@app.delete("/usuarios/{usuario_nome}", response_model=Usuario)
def excluir_usuario(usuario_nome:str): # Varoável que vou usar pra saber qual usuário eu apago
    for num, usuario in enumerate(usuarios): # Usando um for pra vê de 1 em 1
        if usuario.username == usuario_nome: # Verificando de é o usuário
            del usuarios[num] # Apagando
            return usuario
    # Em caso de erro 404, eu retorno isso aqui
    raise HTTPException(status_code=404, detail="Usuário não localizado!")




# LIVRO - Comentar
# Rota para listar Livros
@app.get("/livros/", response_model=List[Livro])
def listar_livros():
    return livros


# Rota para criar/adicionar livros - COMENTAR
@app.post("/livros/", response_model=Livro)
def adicionar_liv(livor_adicionado:Livro): 
    livros.append(livor_adicionado)
    return livor_adicionado 


# Rota de deletar o livros
@app.delete("/livros/{livro_titulo}", response_model=Livro)
def excluir_livro(livro_titulo:str): 
    for num, livro in enumerate(livros): 
        if livro.titulo == livro_titulo: 
            del livros[num]
            return livro
    raise HTTPException(status_code=404, detail="Livro não localizado!")




# BIBLIOTECA - Comentar
# Rota para listar Bibliotecas
@app.get("/bibliotecas/", response_model=List[Biblioteca])
def listar_bibliotecas():
    return bibliotecas


# Rota para criar/adicionar Bibliotecas 
@app.post("/bibliotecas/", response_model=Biblioteca)
def adicionar_bib(biblioteca_adicionada:Biblioteca): 
    bibliotecas.append(biblioteca_adicionada) 
    return biblioteca_adicionada 


# Rota de deletar o Bibliotecas
@app.delete("/bibliotecas/{biblioteca_nome}", response_model=Biblioteca)
def excluir_biblioteca(biblioteca_nome:str): 
    for num, Biblioteca in enumerate(bibliotecas): 
        if Biblioteca.nome == biblioteca_nome:
            del bibliotecas[num] 
            return Biblioteca
    raise HTTPException(status_code=404, detail="Biblioteca não localizada!")




# EMPRESTIMO - COMENTAR
# Rota para listar Emprestimos
@app.get("/emprestimos/", response_model=List[Emprestimo])
def listar_emprestimos():
    return emprestimos


# Rota para criar/adicionar Emprestimos
@app.post("/emprestimos/", response_model=Emprestimo)
def adicionar_emp(emprestimo_adicionado:Emprestimo): 
    emprestimos.append(emprestimo_adicionado) 
    return emprestimo_adicionado 


# Rota de deletar emprestimos - ISSO AQUI TÁ DANDO ERRO, MAS TÁ "PRESTANDO"
@app.delete("/emprestimos/{emprestimo_usu_nome}", response_model=Emprestimo)
def excluir_emprestimo(emprestimo_usu_nome:str): 
    for num, emprestimo in enumerate(emprestimos): 
        if emprestimo.usuario.username == emprestimo_usu_nome:
            del emprestimos[num] 
            return Emprestimo
    raise HTTPException(status_code=404, detail="Emprestimo não localizado!")