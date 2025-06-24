#pip install requests

# TAREFA: 
    # 1 - Listar todos os livros
    # 2 - Pesquisa livro por título: peça ao usuário o título para pesquisa
    # 3 - Cadastrar um livro: peça ao usuário os dados do livros e envie o json para cadastrar
    # 4 - Deletar um livro: peça ao usuário o título para deletar
    # 5 - Sair
# Notações
    # Usa While True
    # Monitore os status retornados

import requests
# Importando a função que vai listar todos os livros
from ListarTodosLivors import Listar_Todos_Livros

if __name__ == "__main__":
    url = "http://127.0.0.1:8000" # URL da API - Tem que tá rodando e não pode ter o "docs" no final

    # Parte que Max fez em sala
    # r = requests.get(f"{url}/livros")
    # print(r.text)
    # livro = {
    #     "titulo": "Python como Programar",
    #     "ano": 2024,
    #     "edicao": 1
    # }

    # r = requests.post(f"{url}/livros",json=livro)
    # print(r.status_code)
    # print(r.text)

    # pesquisa = "Python como Programar"
    # r = requests.get(f"{url}/livros/{pesquisa}")
    # print(r.status_code)
    # print(r.text)

    # r = requests.delete(f"{url}/livros/{pesquisa}")
    # print(r.status_code)
    
    # Apartir daqui já da atividade 
    todoslivors = Listar_Todos_Livros(url=url)
    print(todoslivors)