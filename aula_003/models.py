from pydantic import BaseModel
from datetime import date

class Usuario(BaseModel):
    username:str
    password:str
    data_criacao:date 

class Livro(BaseModel):
    titulo:str
    ano:int
    edicao:int

class Biblioteca(BaseModel):
    nome:str
    acervo:list
    usuario:list 

class Emprestimo(BaseModel):
    usuario:Usuario
    livro:Livro
    data_emprestimo:date
    data_devolucao:date

