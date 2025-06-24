import requests

def Listar_Todos_Livros (url):
    todos_livros = requests.get(f'{url}/livros')
    return todos_livros
