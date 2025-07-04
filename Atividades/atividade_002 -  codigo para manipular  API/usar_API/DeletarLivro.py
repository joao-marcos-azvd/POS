import requests
from ListarTodosLivros import Listar_Todos_Livros

def Deletar_Livro(url, titulo):
    # pegando todos os livors
    livros = Listar_Todos_Livros(url=url) 
    # return livros
    for livro in livros: # Percorendo a lista de dicionários
        if titulo.lower() == livro['titulo'].lower():  # compara ignorando maiúsculas/minúsculas:
            # Aqui é onde eu vou apagar o livro, usando o delete
            livro_deletado = requests.delete(f'{url}/livros/{livro['titulo']}') # A url tava incompleta. Tava {url}/{livro['titulo']}
            if livro_deletado.status_code == 200:
                return (f'Livro deletado com sucesso!')
            else:
                return (f'Erro! {livro_deletado.status_code} - {livro_deletado}')
    # Aqui é pra caso o livor não esteja cadastrado no sistema
    return ('Livro não encontrado!')
