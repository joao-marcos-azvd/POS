import requests

def Listar_Todos_Livros (url): # Tem que passar a url da aplicação 
    todos_livros = requests.get(f'{url}/livros') # Pegando todos os livros por meio do requests
    if todos_livros.status_code == 200: # Se for 200 deu bom
        return todos_livros.json() # Aqui eu retorno as informações no formato json, pra permitir que elas sejam lidas
    else: # Se não, é pq deu errado!
        return ('Deu erro!')
