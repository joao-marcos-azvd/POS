import requests
from ListarTodosLivros import Listar_Todos_Livros

# Criando a função e os parametros que devem ser passados
def Editar_Livro (url, titulo, novos_dados):
    # Criando uma variável pra guardar todos os livros 
    livros = Listar_Todos_Livros(url=url)
    for livro in livros: # Percorendo a lista de dicionários
        if titulo.lower() == livro['titulo'].lower():  # compara ignorando maiúsculas/minúsculas:
            # Aqui é onde eu vou editar os dados do livro
            livro_editado = requests.put(f'{url}/livros/{livro['titulo']}', json=novos_dados)
            if livro_editado.status_code == 200:
                return (f"Livro editado com sucesso! {livro_editado.text}")
            else:
                return (f"Erro! {livro_editado.status_code}")
    # Aqui é pra caso o livor não esteja cadastrado no sistema
    return ('Livro não encontrado!')